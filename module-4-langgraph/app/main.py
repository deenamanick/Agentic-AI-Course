import ast
import os
import uuid
from typing import Any, Dict, List, Literal, TypedDict

from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from langchain_ollama import ChatOllama
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

from langfuse import get_client
from langfuse.langchain import CallbackHandler

from langgraph.graph import END, StateGraph


load_dotenv()


class GraphChatRequest(BaseModel):
    user_query: str


class GraphChatResponse(BaseModel):
    answer: str
    request_id: str
    route: str


def build_llm() -> ChatOllama:
    base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    model = os.getenv("OLLAMA_MODEL", "llama4:scout")

    return ChatOllama(
        model=model,
        base_url=base_url,
        temperature=float(os.getenv("OLLAMA_TEMPERATURE", "0.4")),
    )


def _safe_eval_arithmetic(expression: str) -> str:
    node = ast.parse(expression, mode="eval")

    allowed_nodes = (
        ast.Expression,
        ast.BinOp,
        ast.UnaryOp,
        ast.Add,
        ast.Sub,
        ast.Mult,
        ast.Div,
        ast.FloorDiv,
        ast.Mod,
        ast.Pow,
        ast.USub,
        ast.UAdd,
        ast.Constant,
        ast.Load,
        ast.Call,
        ast.Name,
    )

    for subnode in ast.walk(node):
        if not isinstance(subnode, allowed_nodes):
            raise ValueError("Unsupported expression")
        if isinstance(subnode, ast.Call):
            raise ValueError("Function calls are not allowed")
        if isinstance(subnode, ast.Name):
            raise ValueError("Names are not allowed")

    result = eval(compile(node, "<expr>", "eval"), {"__builtins__": {}}, {})
    return str(result)


class GraphState(TypedDict):
    request_id: str
    route: Literal["general", "math"]
    user_query: str
    messages: List[Any]
    plan: str
    answer: str
    llm: ChatOllama
    langfuse_handler: CallbackHandler


def route_node(state: GraphState) -> Dict[str, Any]:
    text = state["user_query"].strip()
    maybe_math = any(ch.isdigit() for ch in text) and any(op in text for op in ["+", "-", "*", "/", "(", ")"])
    route: Literal["general", "math"] = "math" if maybe_math else "general"
    return {"route": route}


async def plan_node(state: GraphState) -> Dict[str, Any]:
    llm: ChatOllama = state["llm"]  # type: ignore[assignment]
    handler: CallbackHandler = state["langfuse_handler"]  # type: ignore[assignment]

    sys = SystemMessage(
        content=(
            "You are a planning assistant. Create a short plan (3-5 bullets) to answer the user. "
            "Do not answer fully yet."
        )
    )
    human = HumanMessage(content=state["user_query"])

    result = await llm.ainvoke([sys, human], config={"callbacks": [handler]})
    return {"plan": result.content}


def math_tool_node(state: GraphState) -> Dict[str, Any]:
    query = state["user_query"]
    try:
        value = _safe_eval_arithmetic(query)
        answer = value
    except Exception:
        answer = "I couldn't safely evaluate that expression. Please provide a simple arithmetic expression."

    return {"answer": answer}


async def execute_node(state: GraphState) -> Dict[str, Any]:
    llm: ChatOllama = state["llm"]  # type: ignore[assignment]
    handler: CallbackHandler = state["langfuse_handler"]  # type: ignore[assignment]

    sys = SystemMessage(
        content=(
            "You are an expert AI architect. Use the plan to answer concisely. "
            "Return a crisp final answer."
        )
    )

    human = HumanMessage(content=f"User query: {state['user_query']}\n\nPlan:\n{state.get('plan','')}")

    result = await llm.ainvoke([sys, human], config={"callbacks": [handler]})
    return {"answer": result.content}


def finalize_node(state: GraphState) -> Dict[str, Any]:
    messages = state.get("messages", [])
    messages.append(AIMessage(content=state.get("answer", "")))
    return {"messages": messages}


def choose_next(state: GraphState) -> str:
    return "math_tool" if state.get("route") == "math" else "plan"


def build_graph():
    graph = StateGraph(GraphState)

    graph.add_node("route", route_node)
    graph.add_node("plan", plan_node)
    graph.add_node("math_tool", math_tool_node)
    graph.add_node("execute", execute_node)
    graph.add_node("finalize", finalize_node)

    graph.set_entry_point("route")

    graph.add_conditional_edges(
        "route",
        choose_next,
        {
            "math_tool": "math_tool",
            "plan": "plan",
        },
    )

    graph.add_edge("math_tool", "finalize")
    graph.add_edge("plan", "execute")
    graph.add_edge("execute", "finalize")
    graph.add_edge("finalize", END)

    return graph.compile()


app = FastAPI(title="Jeevisoft LangGraph API", version="0.4.0")


@app.post("/graph/chat", response_model=GraphChatResponse)
async def graph_chat(req: GraphChatRequest) -> GraphChatResponse:
    request_id = str(uuid.uuid4())

    llm = build_llm()
    langfuse_handler = CallbackHandler()

    app_state: GraphState = {
        "request_id": request_id,
        "route": "general",
        "user_query": req.user_query,
        "messages": [HumanMessage(content=req.user_query)],
        "plan": "",
        "answer": "",
    }

    metadata = {
        "project": os.getenv("APP_PROJECT", "Jeevi-Academy"),
        "environment": os.getenv("APP_ENV", "Development"),
        "request_id": request_id,
        "langfuse_session_id": request_id,
        "langfuse_tags": [
            f"Project:{os.getenv('APP_PROJECT', 'Jeevi-Academy')}",
            f"Environment:{os.getenv('APP_ENV', 'Development')}",
            "Module:LangGraph",
        ],
    }

    runnable = build_graph()

    result_state: Dict[str, Any] = await runnable.ainvoke(
        {
            **app_state,
            "llm": llm,
            "langfuse_handler": langfuse_handler,
        },
        config={
            "callbacks": [langfuse_handler],
            "metadata": metadata,
        },
    )

    get_client().flush()

    answer = result_state.get("answer", "")
    route = result_state.get("route", "general")

    return GraphChatResponse(answer=str(answer), request_id=request_id, route=str(route))
