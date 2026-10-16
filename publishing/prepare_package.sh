#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
export PYTHONPATH="$PWD/lib${PYTHONPATH:+:$PYTHONPATH}"
exec "$PWD/.venv/bin/python" "publishing/prepare_package.py" "$@"
