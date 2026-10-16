# Student editorial review — six case judgments completed

This is a worksheet, not approval. Fill in your own judgments after inspecting the evidence.

## The Best AI Benchmark Is Your Own Work

Source: https://www.whytryai.com/p/switch-ai-models

Evidence: data/assets/075b80e31faba3a92a3d7712/6d392f0b897d89aba5f23830f5b954824cd8a50f3e5b222e12b93c42db9bf552/text.txt

AI decision: accept

AI reason: Published October 8, within the September 16–October 15 UTC window. Accept as an operational evaluation tutorial for students, not evidence of model superiority or autonomous research gains. The saved passage under 'The fix' specifies representative tasks, explicit evaluation criteria, fresh chats and equal file/tool access; 'Do this now' supplies a judge prompt requiring specific evidence and unverifiable claims to be flagged. These are usable procedures, although the supplied evidence does not include the linked model outputs, repeated trials, held-out tasks or measured costs. The author's statement 'ChatGPT was clearly better for my scoped research' is a personal assessment, not a general result; using ChatGPT to judge its own comparison adds potential evaluator bias. Novelty is a recent worked practitioner demonstration, not a new evaluation method. 'Dig deeper' explicitly promotes paid access to Fun Bench results, establishing a subscription interest; those gated results cannot substantiate performance here. Evidence: [saved text, 'The fix', 'Do this now', 'Dig deeper' and footnote 6](data/assets/075b80e31faba3a92a3d7712/6d392f0b897d89aba5f23830f5b954824cd8a50f3e5b222e12b93c42db9bf552/text.txt).

Student judgment: **AGREE — accept only as an operational testing reference.**

Agree/disagree and why: The student agrees that this can guide test design but cannot establish which model is stronger. They recommend human review to reduce bias when AI evaluates its own output.

Student response (verbatim, Chinese): “我同意，可以作为设计测试的操作参考，但不能用来证明哪个模型更强。最好加上人工复核，避免 AI 评价自己的输出有偏差。”

Recorded from the chat response on October 16, 2026 (America/New_York).

Correction and exact supporting evidence: Proposed policy addition: include human review when using an AI judge, especially when the judge evaluates its own output. The saved source’s “Do this now” section recommends AI judging; the student adds this safeguard. This is a methodological recommendation, not an empirical finding that bias occurred. No factual correction was requested.

Review scope: student judgment on the case presented in chat; independent full-source reading and final publication approval are not asserted.

## Hill-Climbing a Protein Language Model: A Taste of Autoresearch for Scientific Discovery

Source: https://jojoml.github.io/blog/2026/nanoproteinlm-agenticls/

Evidence: data/assets/084a91218ed6d51df5ab9f17/2b0d8382c674620fd174f5c60697d5bdf4728371aa386ebba1986c60e1eef65b/text.txt

AI decision: accept

AI reason: Published September 30, within the authoritative window. Useful original researcher account of reward design and human-gated experimental automation. 'A better PLM recipe' reports contact precision rising from 28.2% to 36.6% P@L at 48.4B tokens; this is an author-reported relative improvement of about 30%, not 30 percentage points or evidence of fully autonomous discovery. 'Failure mode' reports two 72-round searches improving validation loss without matching the best contact precision, directly motivating scrutiny of proxy rewards. 'What survived the human gate' describes two seeds, a noise-aware retention rule and four of seven changes surviving scaled-up ablation. These concrete campaign details provide the new evidence and practical lessons for student experiment design. Limitations: the supplied blog lacks numerical ablation tables, hardware, total search cost, execution logs and independent replication; equal token budgets alone do not establish equal compute cost, and contact precision remains a proxy. The authors describe their own project and promote its adoption; no financial conflict is disclosed in the supplied text. Its referenced paper is the same underlying work, not independent corroboration, and workshop status is not validation. Evidence: [saved text, named sections and 'Authors and links'](data/assets/084a91218ed6d51df5ab9f17/2b0d8382c674620fd174f5c60697d5bdf4728371aa386ebba1986c60e1eef65b/text.txt).

Student judgment: **AGREE — accept as an author-reported case of automated experimentation and potentially misleading metrics.**

Agree/disagree and why: The student agrees this illustrates the experimental process and the risk of misleading metrics, provided the results are explicitly attributed to the authors. They must not be presented as independently verified or as a fully autonomous scientific discovery.

Student response (verbatim, Chinese): “我同意接受，可以用来说明自动实验的过程和指标可能误导的问题，但要明确是作者报告的结果，不能说成已经独立验证或完全自主完成的科学发现。”

Recorded from the chat response on October 16, 2026 (America/New_York).

Correction and exact supporting evidence: Retain explicit author attribution and the human role. The saved source’s “A better PLM recipe” section describes a human deciding which recipes to scale up; “Failure mode” reports the mismatch between loss and contact precision; “What survived the human gate” describes validation. No independent replication is established by this source. The student requests these limits remain explicit, not a factual correction to the saved evidence.

Review scope: student judgment on the case presented in chat; independent full-source reading and final publication approval are not asserted.

## Autoresearch in Mixed-Integer Linear and Nonlinear Programming

Source: https://arxiv.org/abs/2609.39360

Evidence: data/assets/090f19610270f1b804a5bb8a/bc44cd416a3cec196c5ff3ae89d1d7f5f529cfcb851b97b519470fc6baccac09/text.txt

AI decision: accept

AI reason: Published September 30, within the authoritative window. Accept primarily for methodological scrutiny and student lessons about preserving hypotheses, executable states and verification records. Sections 3.2–3.4 specify the idea pool, compatible-parent restoration and evaluator; section 4 supplies baselines, an M4 Pro/24 GB setup, one-hour or twelve-hour horizons, and token accounting. The new contribution is the coupled search organization and its reported benchmark evaluation, not training agent weights. Treat the preprint's performance claims as provisional: section 4.2 calls 1,070,460 tokens a total, while section 4's Metrics defines token values as averages across instances. Table 4 places AutoMIP's sole 6–12-hour success at 41,089 seconds, whereas Appendix H records that late success, acopf_caseactivsg70k_qcqp, at 24,199 seconds. These discrepancies require reconciliation before publishing cost or timing headlines. 'New best' solution claims also lack objective values and independently checked solution certificates in the supplied per-instance tables. Several protocol appendices contain only headings; Appendix B identifies its prompts as standardized templates rather than historical prompts. No independent replication or external researcher assessment is supplied. This is the developers' own evaluation; financial interests are not disclosed here. Evidence: [saved text, §§3–4, Table 4 and Appendices A, B and H](data/assets/090f19610270f1b804a5bb8a/bc44cd416a3cec196c5ff3ae89d1d7f5f529cfcb851b97b519470fc6baccac09/text.txt).

Student judgment: **AGREE — retain methodological discussion with explicit disclosure of inconsistent numbers.**

Agree/disagree and why: The student agrees to retain methodological discussion, but requires explicit disclosure of the numerical inconsistencies. Until the authors clarify them, this source must not substantiate claims of faster execution, lower cost or best results.

Student response (verbatim, Chinese): “我同意保留方法讨论，但要明确指出数字不一致，在作者澄清前不能用来证明更快、更省或取得最佳结果。”

Recorded from the chat response on October 16, 2026 (America/New_York).

Correction and exact supporting evidence: Preserve the restrictions identified in the saved AI decision: section 4 Metrics versus section 4.2 on token accounting, and Table 4 versus Appendix H on success timing. The student requests explicit disclosure and exclusion of speed, cost and best-result conclusions until author clarification. No new factual correction or author clarification was supplied.

Review scope: student judgment on the case presented in chat; independent full-source reading and final publication approval are not asserted.

## Sunday Rundown #159: Cloud Agents & Juggling Costumes

Source: https://www.whytryai.com/p/sunday-rundown-159-cloud-agents

Evidence: data/assets/4eab969d8f8f58425aecc153/7e321e65424e9a2edb24b698e1bca81a81aaeadd44ba001dab6237202ddb0ada/text.txt

AI decision: reject

AI reason: October 4 publication is within the window, but timeliness alone does not establish usefulness. This is a general product-news roundup: its cloud-agent and model-price summaries provide no inspectable computational experiment, research-agent baseline, execution log, held-out result or reproducibility protocol ([saved text, AI releases—OpenAI news](data/assets/4eab969d8f8f58425aecc153/7e321e65424e9a2edb24b698e1bca81a81aaeadd44ba001dab6237202ddb0ada/text.txt)). Linked reports are discovery leads whose underlying evidence is not supplied, so their claims cannot serve as original evidence here. The Stratego result and training-cost figure are also secondary summaries without the experimental support needed to assess a student research workflow ([saved text, AI resources and AI random](data/assets/4eab969d8f8f58425aecc153/7e321e65424e9a2edb24b698e1bca81a81aaeadd44ba001dab6237202ddb0ada/text.txt)). No series-specific methodological novelty is demonstrated. The paid-content promotion establishes the publisher's subscription interest; the supplied text does not establish vendor sponsorship or affiliate relationships ([saved text, All my paid goodies in one place](data/assets/4eab969d8f8f58425aecc153/7e321e65424e9a2edb24b698e1bca81a81aaeadd44ba001dab6237202ddb0ada/text.txt)). Reject as generic AI news rather than defer the whole roundup for missing linked evidence.

Student judgment: **AGREE — reject the roundup as article evidence; retain links as discovery leads.**

Agree/disagree and why: The student agrees to reject this news roundup as article evidence because it lacks experimental details. Linked original materials may be considered only after separate review.

Student response (verbatim, Chinese): “我同意拒绝作为文章证据，因为它只是新闻汇总，缺少实验细节。里面的链接可以作为寻找原始资料的线索，单独审核后再决定是否使用。”

Correction and exact supporting evidence: The saved source’s news and resource sections contain short summaries and outbound links rather than the underlying experimental evidence. Retain these links as discovery leads; do not inherit acceptance from their presence in the roundup. No factual correction was requested.

Review scope: student judgment on the case presented in chat; independent full-source reading and final publication approval are not asserted.

## Sunday Rundown #160: Meeting Summaries & One-Way Hellos

Source: https://www.whytryai.com/p/sunday-rundown-160-meeting-summaries

Evidence: data/assets/78deb02bb43b9240c74487b3/4c16684f04ac89de0cfd2e9942cde9c20a91e0d7aa7d934da6ede6eaa2463817/text.txt

AI decision: reject

AI reason: October 11 is in-window, but recency does not make this general product roundup useful evidence for the series. The 'AI releases' and 'AI research' lists summarize announcements without inspectable experimental methods, budgets, baselines or results. The potentially relevant Epoch and ATLAS entries are only link descriptions; their original reports are not supplied and cannot substantiate research-agent claims here ([saved text](data/assets/78deb02bb43b9240c74487b3/4c16684f04ac89de0cfd2e9942cde9c20a91e0d7aa7d934da6ede6eaa2463817/text.txt), 'AI releases,' 'AI research' and 'AI resources'). This item adds no original experimental evidence or demonstrated methodological novelty for students. Its 'All my paid goodies in one place' section establishes a subscription-promotion interest; sponsorship or affiliate relationships are not established. Reject the roundup rather than treating its linked announcements as independently corroborated sources.

Student judgment: **AGREE — reject the roundup as evidence and review original reports separately.**

Agree/disagree and why: The student agrees that relevant links do not make the roundup sufficient evidence. Original reports require separate review, and a roundup and the original report it summarizes must not count as two independent validations.

Student response (verbatim, Chinese): “我同意，链接相关不代表周报本身有足够证据，应该单独审核原始报告，也不能把周报和原报告算成两份独立验证。”

Correction and exact supporting evidence: The saved source’s “AI resources” section provides brief descriptions and links for ATLAS and “Can AI automate Epoch?” rather than their full methods and results. Retain separate review of original reports and count underlying evidence origins rather than URLs. No factual correction was requested.

Review scope: student judgment on the case presented in chat; independent full-source reading and final publication approval are not asserted.

## Flashcards Are Good. “Gap” Cards Are Better.

Source: https://www.whytryai.com/p/ai-flashcards-knowledge-gaps

Evidence: data/assets/810ca788d6580a6871563f4d/2ec6998b1c53899734b6cb244fefc18311d1635c79e90220c4b2743ae1235252/text.txt

AI decision: reject

AI reason: The supplied October 1 publication date is eligible, but this is a study-aid prompting tutorial rather than evidence about autonomous computational experiments. Its concrete demonstration is an author's puppy-training quiz followed by 37 flashcards; no controlled learning outcomes, validated diagnostic accuracy, execution logs or research-agent evaluation are supplied ([saved text, 'As a test' passage](data/assets/810ca788d6580a6871563f4d/2ec6998b1c53899734b6cb244fefc18311d1635c79e90220c4b2743ae1235252/text.txt#:~:text=As%20a%20test)). Under policy v2, this could establish an operational flashcard procedure, not the headline's superiority claim or the assertion that users will know exactly where their knowledge gaps are. The prompt and accompanying skill offer a workflow, but no demonstrated novelty relevant to experimental automation. The author explicitly promotes a paid-subscriber skill, creating a direct commercial interest ([saved text, 'Dig deeper' and subscription passages](data/assets/810ca788d6580a6871563f4d/2ec6998b1c53899734b6cb244fefc18311d1635c79e90220c4b2743ae1235252/text.txt#:~:text=Dig%20deeper)). General usefulness to students does not make it useful to this series; inaccessible paid material is not the decisive issue.

Student judgment: **AGREE — reject for lack of topic relevance and learning-effect evidence.**

Agree/disagree and why: Usefulness to students does not establish relevance to autonomous research. Generating flashcards does not demonstrate better learning outcomes.

Student response (verbatim, Chinese): “我同意拒绝，对学生有用不代表适合我们的自主研究主题，而且生成卡片也不能证明学习效果更好。”

Correction and exact supporting evidence: The saved source’s “As a test” passage describes a puppy-training quiz and 37 flashcards, without a controlled learning-outcome comparison. No factual correction was requested.

Review scope: student judgment on the case presented in chat; independent full-source reading and final publication approval are not asserted.

Sample coverage: 3/3 accepted and 3/3 rejected or deferred. Collect more candidates if incomplete; do not invent decisions.

## Policy revision

Original policy and outputs: this run’s v2 snapshot and six decisions above. Six student judgments were received in chat. Consolidated at 2026-10-16T18:38:53.792980+00:00.

Change and reason: Policy v3 requires human review of AI-judge conclusions, explicit attribution and human-role disclosure, disclosure of unresolved numeric inconsistencies, separate review of linked originals, evidence-origin deduplication, and topic relevance distinct from general student usefulness. These are grounded in the six student responses above.

Rerun comparison and outcome: editorial-only rerun in ../20261016T183853-editorial-v3/, using the preserved October 15 evidence window. Completed with passing mechanical checks; see that run’s policy_revision.md and draft_differences/. No new live collection is claimed.

## Final approval

Only the student supplies approval.json after reviewing the actual current drafts and review_id.