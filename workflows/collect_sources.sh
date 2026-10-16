#!/usr/bin/env bash
set -uo pipefail
cd "$(dirname "$0")/.."
export PYTHONPATH="$PWD/lib${PYTHONPATH:+:$PYTHONPATH}"
if [[ $# != 1 || ! -f "$1/run.json" ]]; then echo "Expected valid RUN_DIR" >&2; exit 2; fi
r="$1"; failed=0
started=$(.venv/bin/python -c "from common import now; print(now())")
trap 'code=$?; .venv/bin/python lib/receipt.py collect_sources "$r" "$started" "$code"' EXIT
.venv/bin/python lib/preserve.py "$r" candidates candidates.jsonl items.jsonl changes.jsonl corpus.jsonl eligible.jsonl exclusions.jsonl
mkdir -p "$r/candidates"
for name in feeds youtube podcasts; do
 bash "collectors/fetch_${name}.sh" "$r" > "$r/candidates/$name.jsonl" || failed=1
done
cat "$r/candidates/feeds.jsonl" "$r/candidates/youtube.jsonl" "$r/candidates/podcasts.jsonl" > "$r/candidates.jsonl"
cat "$r/candidates.jsonl" | bash processing/extract_content.sh "$r" > "$r/items.jsonl" || failed=1
bash data/store.sh upsert "$r" < "$r/items.jsonl" > "$r/changes.jsonl" || exit 1
bash data/store.sh list > "$r/corpus.jsonl" || exit 1
bash processing/filter_items.sh "$r" < "$r/corpus.jsonl" > "$r/eligible.jsonl" || exit 1
exit "$failed"
