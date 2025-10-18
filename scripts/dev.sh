#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
APP_DIR="$ROOT_DIR/apps"
WEB_DIR="$ROOT_DIR/web"

cd "$ROOT_DIR"

cleanup() {
  if [[ -n "${UVICORN_PID:-}" ]]; then
    kill "$UVICORN_PID" 2>/dev/null || true
  fi
  if [[ -n "${VITE_PID:-}" ]]; then
    kill "$VITE_PID" 2>/dev/null || true
  fi
}

trap cleanup EXIT

if ! command -v uvicorn >/dev/null; then
  echo "uvicorn is required and was not found in PATH" >&2
  exit 1
fi

if ! command -v npm >/dev/null; then
  echo "npm is required to run the frontend" >&2
  exit 1
fi

export PYTHONPATH="$ROOT_DIR"
uvicorn apps.api.main:app --reload --reload-dir "$APP_DIR" &
UVICORN_PID=$!

declare -a npm_args=(run dev -- --host)
if [[ ! -d "$WEB_DIR/node_modules" ]]; then
  echo "Installing frontend dependencies..."
  (cd "$WEB_DIR" && npm install)
fi

(cd "$WEB_DIR" && npm "${npm_args[@]}") &
VITE_PID=$!

wait -n "$UVICORN_PID" "$VITE_PID"
