#!/usr/bin/env bash
set -euo pipefail

curl -sS -X POST "http://127.0.0.1:8000/graph/chat" \
  -H "Content-Type: application/json" \
  -d '{"user_query":"Create a 3-step plan to launch an MVP on Cloudflare."}' | cat

echo

echo "---" 

curl -sS -X POST "http://127.0.0.1:8000/graph/chat" \
  -H "Content-Type: application/json" \
  -d '{"user_query":"What is (17 * 23) + 5?"}' | cat
