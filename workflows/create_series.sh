#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
export PYTHONPATH="$PWD/lib${PYTHONPATH:+:$PYTHONPATH}"
if [[ $# != 1 || ! -f "$1/run.json" ]]; then echo "Expected valid RUN_DIR" >&2; exit 2; fi
r="$1"
started=$(.venv/bin/python -c "from common import now; print(now())")
trap 'code=$?; .venv/bin/python lib/receipt.py create_series "$r" "$started" "$code"' EXIT
.venv/bin/python lib/preserve.py "$r" decisions.jsonl briefs.jsonl articles.jsonl articles video_scripts.jsonl video_scripts review.json
bash editorial/select_items.sh "$r" < "$r/eligible.jsonl" > "$r/decisions.jsonl"
.venv/bin/python review/prepare_student_review.py "$r"
bash editorial/create_briefs.sh "$r" < "$r/decisions.jsonl" > "$r/briefs.jsonl"
bash content/write_articles.sh "$r" < "$r/briefs.jsonl" > "$r/articles.jsonl"
bash content/write_video_scripts.sh "$r" < "$r/briefs.jsonl" > "$r/video_scripts.jsonl"
.venv/bin/python review/evidence_cards.py "$r"
bash review/check_content.sh "$r" > "$r/review.json"
