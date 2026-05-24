#!/usr/bin/env bash
set -euo pipefail
TARGET=${1:-http://host.docker.internal:8080}
case "$TARGET" in
  http://127.0.0.1:*|http://localhost:*|http://host.docker.internal:*) ;;
  *) echo "Refusing non-local target: $TARGET" >&2; exit 2 ;;
esac
docker run --rm -t -v "$(pwd):/zap/wrk" ghcr.io/zaproxy/zaproxy:stable zap-baseline.py -t "$TARGET" -c zap/baseline.conf -J reports/zap_baseline.json || true
