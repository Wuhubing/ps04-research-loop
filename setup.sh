#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
command -v uv >/dev/null
command -v ffmpeg >/dev/null
command -v codex >/dev/null
uv venv --python 3.11 .venv
uv pip install --python .venv/bin/python -r requirements.lock.txt
codex login status
