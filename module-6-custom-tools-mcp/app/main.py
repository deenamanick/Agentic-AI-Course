import os
import uuid
import smtplib
from email.mime.text import MIMEText
from typing import Any, Dict

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import yfinance as yf

from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.tools import tool
from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent

from langfuse import get_client
from langfuse.langchain import CallbackHandler

load_dotenv()

# ─── REQUEST & RESPONSE SHAPES ───────────────────────────────────────

class AgentRequest(BaseModel):
    user_query: str

class AgentResponse(BaseModel):
    answer: str
    request_id: str

# ─── TOOL 1: GET STOCK PRICE (READ TOOL - SAFE) ──────────────────────

@tool
def get_stock_price(ticker: str) -> str:
    """
    Fetches the current stock price for a given ticker symbol.
    For Indian stocks on the NSE, append '.NS' (e.g., 'RELIANCE.NS').
    For Indian stocks on the BSE, append '.BO' (e.g., 'TCS.BO').
    
    Args:
        ticker: The stock ticker symbol.
        
    Returns:
        A string containing the current price or an error message.
    """
    try:
        stock = yf.Ticker(ticker)
        todays_data = stock.history(period='1d')
        if todays_data.empty:
            return f"Error: Could not find data for {ticker}. Did you forget .NS or .BO?"
            
        price = todays_data['Close'].iloc[0]
        return f"The current price of {ticker} is ₹{price:.2f}"
    except Exception as e:
        return f"Error fetching price for {ticker}: {str(e)}"

# ─── TOOL 2: SEND EMAIL ALERT (WRITE TOOL - DANGEROUS) ───────────────

@tool
def send_email_alert(to_email: str, subject: str, body: str) -> str:
    """
    Sends an email alert to a specified email address.
    ONLY use this tool if the user explicitly asks you to send an email or alert them.
    
    Args:
        to_email: The email address to send the alert to.
        subject: The subject line of the email.
        body: The main message of the email.
        
    Returns:
        A success string or an error message.
    """
    # 1. SAFETY: MOCKING! 
    # If MOCK_EMAILS is true, we just pretend to send it to avoid spamming during testing.
    is_mock = os.getenv("MOCK_EMAILS", "true").lower() == "true"
    
    if is_mock:
        print(f"\n[MOCK EMAIL] To: {to_email}\nSubject: {subject}\nBody: {body}\n")
        return f"Successfully sent MOCK email alert to {to_email}. (MOCK_EMAILS=true)"

    # 2. Real email sending logic
    sender_email = os.getenv("SMTP_EMAIL")
    sender_password = os.getenv("SMTP_PASSWORD")
    
    if not sender_email or not sender_password:
        return "Error: SMTP credentials not configured in the server. Set SMTP_EMAIL and SMTP_PASSWORD in .env."

    try:
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = to_email

        # NOTE: This uses Gmail's SSL port. Change if using SendGrid/etc.
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
            
        return f"Successfully sent REAL email alert to {to_email}."
        
    except Exception as e:
        return f"Failed to send email: {str(e)}"

# ─── AGENT SETUP ─────────────────────────────────────────────────────

def build_llm():
    provider = os.getenv("LLM_PROVIDER", "groq").lower()
    if provider == "groq":
        return ChatGroq(model=os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"), temperature=0.1)
    if provider == "ollama":
        return ChatOllama(model=os.getenv("OLLAMA_MODEL", "llama4:scout"), temperature=0.1)
    raise ValueError("Unsupported LLM_PROVIDER.")

# Register our custom tools with the agent!
tools = [get_stock_price, send_email_alert]

def get_agent():
    llm = build_llm()
    # We use LangGraph's prebuilt ReAct agent for simplicity here, 
    # as the focus of this module is on the Custom Tools.
    return create_react_agent(llm, tools=tools)

# ─── FASTAPI APP ─────────────────────────────────────────────────────

app = FastAPI(title="Jeevisoft Stock Alert API", version="0.6.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("FRONTEND_ORIGIN", "http://localhost:5173")],
    allow_credentials=False,
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)

@app.post("/agent/chat", response_model=AgentResponse)
async def chat_endpoint(req: AgentRequest) -> AgentResponse:
    request_id = str(uuid.uuid4())
    langfuse_handler = CallbackHandler()
    
    agent = get_agent()
    
    sys_msg = SystemMessage(content="You are a helpful financial assistant. You can check Indian stock prices and send email alerts.")
    human_msg = HumanMessage(content=req.user_query)
    
    metadata = {
        "project": os.getenv("APP_PROJECT", "Jeevi-Academy"),
        "request_id": request_id,
        "langfuse_session_id": request_id,
        "langfuse_tags": ["Module:CustomTools-StockAlert"],
    }
    
    result = await agent.ainvoke(
        {"messages": [sys_msg, human_msg]},
        config={"callbacks": [langfuse_handler], "metadata": metadata}
    )
    
    get_client().flush()
    
    final_answer = result["messages"][-1].content
    return AgentResponse(answer=str(final_answer), request_id=request_id)
