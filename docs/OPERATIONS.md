# Research Loop operations

## Install and run

Run `bash setup.sh`, then `bash run.sh` from the project root. Requires uv, FFmpeg, Python 3.11 and a ChatGPT-authenticated Codex CLI. Dependencies are pinned in requirements.lock.txt. No API key is required for the selected provider. Local speech recognition downloads small.en on first use. Large media and the Python environment are excluded from Git.

The run prints a JSON summary and writes an immutable configuration/prompt snapshot. Publication dates use UTC, inclusive D−29 through D. A run made on October 13 evening in New York can have October 14 as its UTC as-of date. Do not backdate runs.

## Component ownership

The required Bash files are independently runnable. Python helpers belong to their corresponding component. Shared libraries supply I/O, feed parsing, model transport and writing transport only. The store is the sole reader/writer of the SQLite index. Asset text and transcript files remain available outside that index.

`bash data/store.sh init`, `upsert RUN_DIR`, `list`, and `get ITEM_ID [VERSION_ID]` implement the course interface. Record paths are repository-relative. Item identity derives from canonical URLs or native YouTube IDs. Version hashes cover substantive text, segments, title, date, URL, type and publisher; retrieval time is excluded. History retains every version and run observation. Publisher IDs for seeded papers represent their author teams; unknown discovery results remain conservatively grouped until reviewed. Both Periodic founder interviews share one evidence-origin group.

## Recover and replay

The collection and series workflows automatically archive their previous named outputs under the run's history directory. Before directly rerunning a component, preserve its earlier output there as well. Never overwrite earlier policy versions or model-call artifacts. For unchanged configuration, rerun the collection workflow, then the series workflow; receipts remain separate. Only do this while the run's UTC as-of date is still valid. Start a new run on a new UTC date.

Example: `bash workflows/collect_sources.sh runs/RUN_ID`, then `bash workflows/create_series.sh runs/RUN_ID`. Follow with `bash reporting/summarize_run.sh runs/RUN_ID > runs/RUN_ID/summary.json`. Collection errors are not empty success: partial coverage and errors remain visible. An arXiv HTTP 429 is recorded and retried with backoff. Configured original-page metadata recovery may collect supplemental evidence, explicitly labeled direct_metadata_fallback. Such recovery does not count as successful RSS collection; at least two written records must actually originate in RSS/Atom. Media access errors should use permitted audio download and local transcription; failed media do not count as usable evidence.

## Human review and packaging

After the second live run, use `PYTHONPATH=lib .venv/bin/python reporting/compare_runs.py runs/FIRST runs/SECOND > runs/SECOND/comparison.json`. The report identifies new, missing, changed and unchanged eligible evidence, decision differences and whether the two live dates genuinely differ. Inspect failures before treating missing items as expired. The seven-day plan and the one-time second-run follow-up are documented in [DELIVERY_SCHEDULE.md](DELIVERY_SCHEDULE.md).

Review at least three accepted and three rejected/deferred eligible items. If the natural decisions do not supply that sample, collect additional relevant candidates; never force rejection labels merely to hit a quota. Compare your judgment with the AI's actual saved reasons. Copy the v1 policy and results, revise policy in configuration, and run a separately preserved comparison. Document factual corrections and their supporting evidence.

Run `bash review/check_content.sh runs/RUN_ID > runs/RUN_ID/review.json`. Read the actual articles, scripts and evidence, listen to cited audio, and assess whether the interpretation is sound. Only the student may supply the approval decision. approval.json records review_id, decision, reviewer, reviewed_at and notes. An assistant may transcribe an explicit student decision already supplied in chat, identifying the verbatim authorization record and its limited scope; it must never invent approval or original-source listening. No approval is fabricated by this project. Run `bash run.sh --package runs/RUN_ID` after approval. Changes to assessed content invalidate approval. Content checks are mechanical and do not establish scientific validity.

For a readable claim-to-source trail, run `PYTHONPATH=lib .venv/bin/python review/evidence_cards.py runs/RUN_ID`. This creates evidence_review.md with exact source versions, excerpts and media time ranges, plus source_usage.json distinguishing suggested article assignments from actual cited claims and accepted-but-unused items. These are audit aids, not approval. Selection sees full retained material; briefing uses full material when it fits, or the validated extraction path below. Drafting receives the cited passages with surrounding context, explicitly labeled as excerpts; the full source remains available for review.

For large accepted corpora (over 800,000 serialized characters), briefing first uses `editorial/evidence_digest.py` and `prompts/distill_evidence.md` to extract 6–10 key passages per source, including limitations and counterevidence. Each source extraction sees its full retained content. Exact written substrings, real media segment IDs and item/version identity are checked before synthesis. The excerpt cards and synthesis_context.json are saved alongside all prompts and responses; full sources are never deleted or silently truncated. This bounds model input size but introduces selection risk, so reviewers should compare the selected passages with the complete sources. A failed extraction blocks synthesis and preserves completed cards for retry.

Media caching assumes that the same episode/video identity and media URL represents the same recording. This saves repeated transcription but cannot detect an in-place replacement at an unchanged URL. Written sources are fetched again and substantively hashed. A known recording replacement needs an explicitly documented refreshed extraction; do not claim the cache detects every remote edit.

## Google Vids and publication

Use each scene's Narration as the spoken track and subtitle source; Visual describes the accompanying Google Vids scenes. Render three 3–5 minute videos. Replace internal claim comments with accessible citations in the audience-facing versions; retain markers in submitted artifacts. Include article/source links and AI presentation disclosure in each YouTube description. Publish articles with free shareable access and videos as unlisted. Insert real URLs into package/publication_links.json. Verify access in a signed-out browser.

Record a separate 4–6 minute narrated technical demo: architecture and entry point; trace one claim to exact text/audio and editorial decision; demonstrate the second run and deduplication/failure recovery; explain a human correction, policy revision and architectural tradeoff. Do not present a script as a completed recording.

## Testing and costs

Run `.venv/bin/python -m unittest discover -s tests -v`. Tests run in isolated temporary repositories with visibly fictional data; they do not count as evidence or real pipeline runs. Receipts preserve timing, tools and unknown costs. Subscription usage is not a zero-dollar API estimate. Codex event logs preserve available usage/model information; authentication files and credentials are never copied into the project.
