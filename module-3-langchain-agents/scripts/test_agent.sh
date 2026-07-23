#!/usr/bin/env bash
set -euo pipefail

curl -sS -X POST "http://127.0.0.1:8000/agent/chat" \
  -H "Content-Type: application/json" \
  -d '{"user_query":"What is (17 * 23) + 5? Use tools if needed."}' | cat
