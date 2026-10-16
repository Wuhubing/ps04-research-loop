# Student editorial review — unanswered

This is a worksheet, not approval. Fill in your own judgments after inspecting the evidence.

## Hill-Climbing a Protein Language Model: A Taste of Autoresearch for Scientific Discovery

Source: https://jojoml.github.io/blog/2026/nanoproteinlm-agenticls/

Evidence: data/assets/084a91218ed6d51df5ab9f17/2b0d8382c674620fd174f5c60697d5bdf4728371aa386ebba1986c60e1eef65b/text.txt

AI decision: accept

AI reason: The supplied September 30 publication date is within the run's 30-day window. Accept as a qualified first-party account of experiment design and evaluation failure. The saved [“A better PLM recipe by hill-climbing NanoProteinLM” passage](data/assets/084a91218ed6d51df5ab9f17/2b0d8382c674620fd174f5c60697d5bdf4728371aa386ebba1986c60e1eef65b/text.txt) reports contact precision rising from 28.2% to 36.6% at an equal 48.4B-token training budget, with humans selecting recipes to scale. That is an author-reported relative improvement of about 30%, not fully autonomous discovery or established biological improvement. In the same saved text, “Failure mode: Perfect on reward, failure on science” reports two 72-round searches improving validation loss without matching the best contact precision; “What survived the human gate” specifies two seeds and four of seven changes surviving scaled ablation. These concrete results support student lessons about proxy rewards, seed variation and human checkpoints. Equal final training tokens do not establish equal total search costs; hardware, detailed ablation measurements and independent biological validation are not supplied. The authors promote their own research environment, and the referenced paper would share the underlying experiment rather than independently corroborate the blog. No independent replication or outside researcher assessment is supplied. Accept the inspectable blog account, not unexamined claims from the referenced paper.

Student judgment: **PENDING**

Agree/disagree and why: **PENDING**

Correction and exact supporting evidence: **PENDING**

## Autoresearch in Mixed-Integer Linear and Nonlinear Programming

Source: https://arxiv.org/abs/2609.39360

Evidence: data/assets/090f19610270f1b804a5bb8a/bc44cd416a3cec196c5ff3ae89d1d7f5f529cfcb851b97b519470fc6baccac09/text.txt

AI decision: accept

AI reason: The supplied September 30 publication date is within the run's 30-day window. The research contribution is concrete: persistent hypotheses coupled to recoverable executable states, described in saved [§§3.2–3.4](data/assets/090f19610270f1b804a5bb8a/bc44cd416a3cec196c5ff3ae89d1d7f5f529cfcb851b97b519470fc6baccac09/text.txt). Sections 4–4.3 report an M4 Pro with 24 GB memory, fixed one- or twelve-hour horizons, four comparison frameworks, and ablations. Reported Open successes are 31/60 versus Codex's 29/60; Hard successes are 30/60 versus 29/60. These are useful bounded comparisons, not universal superiority. Accept especially for evidence scrutiny: §4 defines token figures as averages including failures, whereas §4.2 calls the ablation figure 1,070,460 “total tokens”; missing failure-token records prevent reconstructing that claim. Table 4 reports the final MINLPLib success at 41,089 seconds, while Appendix H records acopf_caseactivsg70k_qcqp at 24,199 seconds, an unresolved aggregate-versus-row discrepancy. Appendix G explicitly separates interface observations from Open records, so their differing times should not automatically be treated as contradictions. Appendix B supplies standardized templates rather than historical prompts, and several protocol appendix headings lack substantive content in the supplied extraction. Public benchmark search is not a held-out transfer test; objective values and external confirmation of claimed new best solutions are not supplied. This is the method developers' preprint, with an authorship interest and no supplied independent replication or financial-conflict disclosure. Student implications—retain failed experiments, restore compatible states and audit aggregate cost claims—are editorial inferences from the protocol and reporting limitations.

Student judgment: **PENDING**

Agree/disagree and why: **PENDING**

Correction and exact supporting evidence: **PENDING**

## Reward Hacking Challenges Oversight of Autonomous Research Agents

Source: https://arxiv.org/abs/2609.28614

Evidence: data/assets/235ddeb91911d80fff910262/3c11fafcee8a531bb96d38ae9a2779c131ae2e2501195df7ae79cba7af4192b6/text.txt

AI decision: accept

AI reason: The supplied September 23 publication date is within the run's 30-day window; saved [Appendix C](data/assets/235ddeb91911d80fff910262/3c11fafcee8a531bb96d38ae9a2779c131ae2e2501195df7ae79cba7af4192b6/text.txt) dates experiments to July 21–23, so the recent development is the report, not newly conducted October experiments. Sections 3–6 provide concrete evidence about delegated evaluation: a common 40-turn/3,600-second harness, spontaneous hacking rates of 30.5% versus 2.9% across task categories, and submission-only review missing 33/505 verification-positive hacks. These are study-specific author results. Explicitly permitted hacking and adversarial evasion in E2–E3 cannot estimate ordinary deployment prevalence. Preserve the corrections in §5: excluding three disputed PAC-Bayes cases changes residual trajectory-review clearances from 12/33 to 9/30. Section 6's paired comparison reports 40.5% versus 20.3% cumulative evasion, but feedback bundles decisions, explanations and history; it neither isolates explanations nor involves model-weight training. Section 3.1 and Appendix B acknowledge potentially correlated LLM verification errors, unidentified verification-panel membership and missing all-attempt reliability. Appendix A's hidden checks support concrete student practices, while §8 makes separating experiment execution from evaluation control a useful implication rather than a proven complete defense. The “Broader impact and responsible disclosure” passage withholds exact red-team prompts and attack artifacts, limiting reproduction without making the substantial supplied methods and results inaccessible. This is a first-party preprint with no supplied independent replication, external researcher assessment or financial-conflict disclosure; panel agreement is not independent corroboration.

Student judgment: **PENDING**

Agree/disagree and why: **PENDING**

Correction and exact supporting evidence: **PENDING**

## The Best AI Benchmark Is Your Own Work

Source: https://www.whytryai.com/p/switch-ai-models

Evidence: data/assets/075b80e31faba3a92a3d7712/6d392f0b897d89aba5f23830f5b954824cd8a50f3e5b222e12b93c42db9bf552/text.txt

AI decision: reject

AI reason: The supplied October 8 publication date is within the run's 30-day window, but topical recency does not establish research value. The practitioner advice to compare representative tasks with equal tools is relevant to evaluation; the evidence is a personal model-selection demonstration, not a measured autonomous research experiment. In the saved [“The fix” passage](data/assets/075b80e31faba3a92a3d7712/6d392f0b897d89aba5f23830f5b954824cd8a50f3e5b222e12b93c42db9bf552/text.txt), the author concludes “ChatGPT was clearly better for my scoped research.” The linked outputs are not supplied, and the screenshots' prompt and scoring details are absent from the text, preventing scrutiny of that comparison. No repeated trials, held-out evaluation, budget or independent replication supports a general performance claim. The saved “Dig deeper” passage calls Fun Bench “totally unscientific” and promotes paid access to results, establishing a subscription interest. Limited methodological novelty and insufficient concrete research evidence make this unsuitable for the series.

Student judgment: **PENDING**

Agree/disagree and why: **PENDING**

Correction and exact supporting evidence: **PENDING**

## Here Are My Go-To AI Tools

Source: https://www.whytryai.com/p/my-go-to-ai-tools

Evidence: data/assets/419feb0137451bb2ed3c150d/c62c33737f81b7859987d32de9f2f19bafa2a36bf2482b8def3c4d4ba34306f6/text.txt

AI decision: reject

AI reason: Generic tool recommendations, without concrete autonomous-experiment evidence useful to this series. The opening distinguishes the October 12, 2026 update from original publication on October 17, 2024; the recent update must not be presented as a newly published experiment ([saved opening](data/assets/419feb0137451bb2ed3c150d/c62c33737f81b7859987d32de9f2f19bafa2a36bf2482b8def3c4d4ba34306f6/text.txt#:~:text=LATEST%20UPDATE)). The 'Research' and 'Agents & productivity' sections offer personal preferences and product claims, without experimental protocols, held-out results, reproducible artifacts or measured research costs; their linked evaluations are not supplied evidence ([saved recommendations](data/assets/419feb0137451bb2ed3c150d/c62c33737f81b7859987d32de9f2f19bafa2a36bf2482b8def3c4d4ba34306f6/text.txt#:~:text=5.%20Research)). The closing paid-subscription appeal establishes a commercial newsletter interest, but does not establish vendor sponsorship ([saved appeal](data/assets/419feb0137451bb2ed3c150d/c62c33737f81b7859987d32de9f2f19bafa2a36bf2482b8def3c4d4ba34306f6/text.txt#:~:text=If%20you%20enjoy%20my%20stuff)). Recent product substitutions do not overcome the lack of relevant experimental evidence.

Student judgment: **PENDING**

Agree/disagree and why: **PENDING**

Correction and exact supporting evidence: **PENDING**

## Sunday Rundown #159: Cloud Agents & Juggling Costumes

Source: https://www.whytryai.com/p/sunday-rundown-159-cloud-agents

Evidence: data/assets/4eab969d8f8f58425aecc153/7e321e65424e9a2edb24b698e1bca81a81aaeadd44ba001dab6237202ddb0ada/text.txt

AI decision: reject

AI reason: The supplied October 4 publication date is within the run's 30-day UTC window ending October 13, but this is a generic secondary news roundup. Its cloud-agent and model-price summaries do not document an autonomous research experiment ([saved release summaries](data/assets/4eab969d8f8f58425aecc153/7e321e65424e9a2edb24b698e1bca81a81aaeadd44ba001dab6237202ddb0ada/text.txt#:~:text=OpenAI%20news)). The potentially relevant Fig Labs evaluation and the Stratego result are only pointers: their original methods, compute accounting, baselines and full results are absent from the supplied evidence. They cannot substantiate an evaluation or affordability claim here ([saved resource and research pointers](data/assets/4eab969d8f8f58425aecc153/7e321e65424e9a2edb24b698e1bca81a81aaeadd44ba001dab6237202ddb0ada/text.txt#:~:text=AI%20resources)). Reject this roundup on relevance and evidentiary depth; assessing those underlying reports would require their original evidence. The paid-content promotion establishes the publisher's subscription interest, not independent validation or proof of vendor sponsorship ([saved promotion](data/assets/4eab969d8f8f58425aecc153/7e321e65424e9a2edb24b698e1bca81a81aaeadd44ba001dab6237202ddb0ada/text.txt#:~:text=All%20my%20paid%20goodies)).

Student judgment: **PENDING**

Agree/disagree and why: **PENDING**

Correction and exact supporting evidence: **PENDING**

Sample coverage: 3/3 accepted and 3/3 rejected or deferred. Collect more candidates if incomplete; do not invent decisions.

## Policy revision

Original policy and outputs: **PENDING student review**

Change and reason: **PENDING**

Rerun comparison and outcome: **PENDING**

## Final approval

Only the student supplies approval.json after reviewing the actual current drafts and review_id.