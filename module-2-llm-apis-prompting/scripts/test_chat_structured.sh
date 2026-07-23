#!/usr/bin/env bash
set -euo pipefail

curl -sS -X POST "http://127.0.0.1:8000/chat/structured" \
  -H "Content-Type: application/json" \
  -d '{"user_query":"Create a 3-step plan to ship a small SaaS backend on Cloudflare."}' | cat
