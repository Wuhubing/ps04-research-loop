#!/usr/bin/env bash
set -uo pipefail
cd "$(dirname "$0")"
export PYTHONPATH="$PWD/lib${PYTHONPATH:+:$PYTHONPATH}"
if [[ $# == 2 && "$1" == --package ]]; then
 r="$2"; export RUN_DIR="$r"
 bash review/check_content.sh "$r" > "$r/review.json" || exit 1
 bash publishing/prepare_package.sh "$r" > "$r/package-result.json"; code=$?
 bash reporting/summarize_run.sh "$r" > "$r/summary.json"
 cat "$r/summary.json"; exit "$code"
elif [[ $# != 0 ]]; then
 echo 'Usage: bash run.sh [--package RUN_DIR]' >&2; exit 2
fi
r=$(.venv/bin/python lib/run_setup.py) || exit 2
export RUN_DIR="$r"
echo "Run: $r" >&2
started=$(.venv/bin/python -c 'import json,sys; print(json.load(open(sys.argv[1]))["started_at"])' "$r/run.json")
finish() {
 code=$?
 .venv/bin/python lib/receipt.py run "$r" "$started" "$code"
 bash reporting/summarize_run.sh "$r" > "$r/summary.json"
 cat "$r/summary.json"
}
trap finish EXIT
bash data/store.sh init || exit 1
bash workflows/collect_sources.sh "$r"; collection=$?
bash workflows/create_series.sh "$r"; series=$?
if (( collection || series )); then exit 1; fi
.venv/bin/python -c 'import json,sys; sys.exit(0 if json.load(open(sys.argv[1]))["passed"] else 1)' "$r/review.json"
