#!/usr/bin/env bash
set -euo pipefail

curl -sS -X POST "http://127.0.0.1:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{"user_query":"Design a serverless full-stack backend on Cloudflare for a small SaaS. Keep it concise."}' | cat
