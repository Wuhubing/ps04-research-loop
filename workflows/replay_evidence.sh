#!/usr/bin/env bash
# Storage/freshness demonstration only. This is never a second live run.
set -euo pipefail
cd "$(dirname "$0")/.."
export PYTHONPATH="$PWD/lib${PYTHONPATH:+:$PYTHONPATH}"
if [[ $# != 1 || ! -f "$1/items.jsonl" ]]; then echo 'Expected a run with items.jsonl' >&2; exit 2; fi
r=$(.venv/bin/python - "$1" <<'PY'
import shutil,sys
from common import *
source=Path(sys.argv[1]);original=read(source/'run.json');stamp=now();dest=Path('runs')/('replay-'+uuid.uuid4().hex[:12]);dest.mkdir(parents=True)
for name in ['config','prompts']:shutil.copytree(source/name,dest/name)
shutil.copyfile(source/'items.jsonl',dest/'items.jsonl')
write(dest/'run.json',dict(run_id=dest.name,started_at=stamp,as_of_date=original['as_of_date'],mode='replay',previous_run_id=original['run_id'],purpose='Replay stored real evidence to demonstrate idempotence and freshness; not a live collection or publication run'))
print(dest)
PY
)
export RUN_DIR="$r"
bash data/store.sh upsert "$r" < "$r/items.jsonl" > "$r/changes.jsonl"
bash data/store.sh list > "$r/corpus.jsonl"
bash processing/filter_items.sh "$r" < "$r/corpus.jsonl" > "$r/eligible.jsonl"
.venv/bin/python - "$r" <<'PY'
from common import *
r=Path(sys.argv[1]);changes=lines(r/'changes.jsonl');result={'mode':'replay','passed':all(x['change']=='unchanged' for x in changes),'records':len(changes),'changes':{k:sum(x['change']==k for x in changes) for k in ['new','changed','unchanged']},'note':'Storage-only replay; no new sources collected, no new series generated, not a second live run'};write(r/'replay_result.json',result);emit(result)
PY
