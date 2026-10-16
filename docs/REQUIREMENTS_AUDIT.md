# PS04 requirement audit

Reference: preserved README.md and ARCHITECTURE.md. This is an evidence-based delivery checklist, not a claim of perfect compliance.

| Requirement | Evidence / current state |
|---|---|
| Defined topic, audience, recurring publication | Research Loop; student researchers; SUBMISSION.md |
| At least 12 substantive items, six independent sources, two per type | Second live run: 23 eligible items, 18 written / 2 YouTube / 3 podcast. Conservative publisher grouping and shared Periodic Labs origin disclosed. |
| Last 30 calendar days | Actual UTC windows retained; unknown/future/old exclusions tested. Second collection September 16–October 15. Editorial v3 freezes that window explicitly. |
| Full content and timestamped media evidence | data/assets and versioned references; raw recordings excluded from Git, recovery instructions retained |
| AI editorial policy and logged decisions | config/editorial_policy.md; run snapshots, model calls, decisions.jsonl |
| Human review: 3 accept and 3 reject/defer | Actual six chat responses retained; policy v3 and draft differences |
| Three distinct articles, 600–900 words, 3 independent sources each | Mechanical review passes; body counts 733 / 745 / 730; source/claim cards retained |
| Written, YouTube and podcast evidence used across series | source_usage.json and evidence_review.md |
| All 16 Bash interfaces, independent component ownership | Implemented; only store interface accesses SQLite; original architecture preserved |
| Versioning, dedup, dates and failure handling | 11 passing contract tests; actual 429 receipt and next-date recovery; separate 26-observation unchanged replay |
| Two actual runs on different dates | October 14 and October 15 live runs; eight new-to-corpus items all predate first run, no changed versions; no fabricated novelty |
| Formal packaging tied to human decision | approval.json transcribes explicit publication authorization; matching package manifest; source listening not asserted |
| Three 3–5 minute videos | 244.32 / 269.79 / 261.49 seconds; student listened and approved |
| Google Vids / HeyGen production | 01 visuals authored in Vids; 02/03 locally authored and imported, then actually exported through Vids. Precise hybrid provenance disclosed; not all visuals Vids-authored. |
| Free articles and unlisted videos with mutual links | All six URLs recorded and reciprocal links saved; Everyone and Unlisted verified in UI. Signed-out access still pending; YouTube external clickable links need channel verification. |
| Separate 4–6 minute technical demo | 5:19 video exported, decoded and delivered as a GitHub release asset; production record retains hash and automatic QA. AI narration disclosed; student must understand the demonstrated system. |
| GitHub repository and submission documentation | Public Wuhubing/ps04-research-loop created and pushed; final push verification recorded in SUBMISSION.md |
| Reflection and costs | Student suggests larger literature search and cross-domain insights; implementation tradeoffs documented; subscription and local compute costs unknown |
| Original audio quotation verification | PENDING genuine student listening to the 16 linked source excerpts; finished-video listening does not fulfill this check |
| One-week working plan | Original seven-day plan retained with actual early completion dates; elapsed work was not backdated or inflated |

Remaining human checks are not replaced by generated text or test results. The technical demo uses saved real records and clearly labeled storage replay, not a simulated second live run.
