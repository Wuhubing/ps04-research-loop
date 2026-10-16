# Evidence review cards

Draft audit aid. Every media passage still requires listening against the original recording. Check interpretation and independence, not just string matches. No student approval is recorded here.

## 01 — What changed: bounded experimental loops became more inspectable

The useful advance is a more concrete account of bounded delegation: agents can revise recipes and execute searches, while human selection, fixed evaluation and claim-level auditing remain essential. These reports support testing specific workflows, not declaring autonomous scientific discovery solved.

### 01-c1

source_claim: NanoProteinLM's authors report contact precision rising from 28.2% to 36.6% P@L at the same 48.4B-token budget, with humans deciding which recipes to scale. This is a bounded, author-reported result, not fully autonomous discovery.

[Hill-Climbing a Protein Language Model: A Taste of Autoresearch for Scientific Discovery](https://jojoml.github.io/blog/2026/nanoproteinlm-agenticls/) · Written passage

Origin: `nanoproteinlm-authors` · Version: `2b0d8382c674620fd174f5c60697d5bdf4728371aa386ebba1986c60e1eef65b`

Saved evidence: `data/assets/084a91218ed6d51df5ab9f17/2b0d8382c674620fd174f5c60697d5bdf4728371aa386ebba1986c60e1eef65b/text.txt`

> Starting from the ESMC recipe, a simple sequential search, with a human deciding which recipes to scale up, gave a recipe with about 30% higher long-range contact precision, from 28.2% to 36.6% P@L, at the same 48.4B-token budget.

### 01-c2

source_claim: NanoProteinLM's final ablation retained four of seven changes, illustrating why search-time improvements need a separate confirmation stage.

[Hill-Climbing a Protein Language Model: A Taste of Autoresearch for Scientific Discovery](https://jojoml.github.io/blog/2026/nanoproteinlm-agenticls/) · Written passage

Origin: `nanoproteinlm-authors` · Version: `2b0d8382c674620fd174f5c60697d5bdf4728371aa386ebba1986c60e1eef65b`

Saved evidence: `data/assets/084a91218ed6d51df5ab9f17/2b0d8382c674620fd174f5c60697d5bdf4728371aa386ebba1986c60e1eef65b/text.txt`

> Four of the seven changes survive the final ablation study.

### 01-c3

source_claim: The solar-segmentation study restricts agents to training-program edits, protects the evaluator and caps each campaign at 24 logged experiments including the baseline.

[Insights from Autoresearch for Solar Panel Segmentation](https://arxiv.org/abs/2610.10491) · Written passage

Origin: `research-team-2610.10491` · Version: `22bcded05aecba83c6a4594604bdc843c3061c7ccdf19d4be43c9ea27beaec4f`

Saved evidence: `data/assets/a007976d7a6dcb8c99635a7e/22bcded05aecba83c6a4594604bdc843c3061c7ccdf19d4be43c9ea27beaec4f/text.txt`

> The agent never trains on validation or test images and cannot edit the evaluator.

[Insights from Autoresearch for Solar Panel Segmentation](https://arxiv.org/abs/2610.10491) · Written passage

Origin: `research-team-2610.10491` · Version: `22bcded05aecba83c6a4594604bdc843c3061c7ccdf19d4be43c9ea27beaec4f`

Saved evidence: `data/assets/a007976d7a6dcb8c99635a7e/22bcded05aecba83c6a4594604bdc843c3061c7ccdf19d4be43c9ea27beaec4f/text.txt`

> The agent may edit only the training program (loss, optimizer, schedule, auxiliary head, gradient clipping, and train-time augmentation).

[Insights from Autoresearch for Solar Panel Segmentation](https://arxiv.org/abs/2610.10491) · Written passage

Origin: `research-team-2610.10491` · Version: `22bcded05aecba83c6a4594604bdc843c3061c7ccdf19d4be43c9ea27beaec4f`

Saved evidence: `data/assets/a007976d7a6dcb8c99635a7e/22bcded05aecba83c6a4594604bdc843c3061c7ccdf19d4be43c9ea27beaec4f/text.txt`

> Each campaign is capped at 24 logged experiments, including the baseline.

### 01-c4

inference: The solar results cannot identify a generally superior coding model or training recipe: every proposed change uses one seed, Loops A and C lack test evaluation, and model choice is confounded with GPU class.

[Insights from Autoresearch for Solar Panel Segmentation](https://arxiv.org/abs/2610.10491) · Written passage

Origin: `research-team-2610.10491` · Version: `22bcded05aecba83c6a4594604bdc843c3061c7ccdf19d4be43c9ea27beaec4f`

Saved evidence: `data/assets/a007976d7a6dcb8c99635a7e/22bcded05aecba83c6a4594604bdc843c3061c7ccdf19d4be43c9ea27beaec4f/text.txt`

> Each proposed change is evaluated with a single random seed (35). Loops A and C have no test evaluation. The coding model is confounded with GPU class, and the agent cannot change the backbone, the split, or the metric.

### 01-c5

inference: Agora documents immutable Git ancestry from an older April–May experiment, but its authors explicitly say they did not rerun the winning method. Preserved code lineage is therefore useful evidence infrastructure, not proof of independently reproduced performance.

[Agora: Git as Shared Memory for Collective AutoResearch](https://arxiv.org/abs/2609.18094) · Written passage

Origin: `research-team-2609.18094` · Version: `66025228eaffdbf60602a9c3e085782385578f7304cce9751aff2a52b9936729`

Saved evidence: `data/assets/59b2cb8b434efeeb70a133bc/66025228eaffdbf60602a9c3e085782385578f7304cce9751aff2a52b9936729/text.txt`

> Git hashes identify immutable commits, and Git parentage makes their graph acyclic.

[Agora: Git as Shared Memory for Collective AutoResearch](https://arxiv.org/abs/2609.18094) · Written passage

Origin: `research-team-2609.18094` · Version: `66025228eaffdbf60602a9c3e085782385578f7304cce9751aff2a52b9936729`

Saved evidence: `data/assets/59b2cb8b434efeeb70a133bc/66025228eaffdbf60602a9c3e085782385578f7304cce9751aff2a52b9936729/text.txt`

> from the setup commit on April 26 to our cutoff on May 8

[Agora: Git as Shared Memory for Collective AutoResearch](https://arxiv.org/abs/2609.18094) · Written passage

Origin: `research-team-2609.18094` · Version: `66025228eaffdbf60602a9c3e085782385578f7304cce9751aff2a52b9936729`

Saved evidence: `data/assets/59b2cb8b434efeeb70a133bc/66025228eaffdbf60602a9c3e085782385578f7304cce9751aff2a52b9936729/text.txt`

> We did not rerun the winning method;

### 01-c6

source_claim: ResearchFlow-Eval reports only 14 of 90 end-to-end claims met, including one empirical claim. Its LLM judging and anchor-paper-dependent rubric limit interpretation as a general measure of research competence.

[ResearchFlow-Eval: Tracing the Execution Gap in End-to-End Multi-Claim Autoresearch](https://arxiv.org/abs/2610.18088) · Written passage

Origin: `arxiv-unresolved-team` · Version: `9f5a3d8ad0d87cf4b75e0b27ee825183acc71c2811e8bb96e1a59f3c5dca2c35`

Saved evidence: `data/assets/51fd6c05fff2f297f454f717/9f5a3d8ad0d87cf4b75e0b27ee825183acc71c2811e8bb96e1a59f3c5dca2c35/text.txt`

> Of the 90 end-to-end claims, 14 are met, and E5 for GPT-6 Astra is the only empirical claim met in an end-to-end run.

[ResearchFlow-Eval: Tracing the Execution Gap in End-to-End Multi-Claim Autoresearch](https://arxiv.org/abs/2610.18088) · Written passage

Origin: `arxiv-unresolved-team` · Version: `9f5a3d8ad0d87cf4b75e0b27ee825183acc71c2811e8bb96e1a59f3c5dca2c35`

Saved evidence: `data/assets/51fd6c05fff2f297f454f717/9f5a3d8ad0d87cf4b75e0b27ee825183acc71c2811e8bb96e1a59f3c5dca2c35/text.txt`

> We use an LLM as the judge, with claude-opus-5 as the evaluator model.

[ResearchFlow-Eval: Tracing the Execution Gap in End-to-End Multi-Claim Autoresearch](https://arxiv.org/abs/2610.18088) · Written passage

Origin: `arxiv-unresolved-team` · Version: `9f5a3d8ad0d87cf4b75e0b27ee825183acc71c2811e8bb96e1a59f3c5dca2c35`

Saved evidence: `data/assets/51fd6c05fff2f297f454f717/9f5a3d8ad0d87cf4b75e0b27ee825183acc71c2811e8bb96e1a59f3c5dca2c35/text.txt`

> Because the rubrics follow the anchor paper, they may undervalue scientifically valid alternatives to its design.

### 01-c7

inference: For students, the defensible delegation unit is a bounded change with a fixed evaluator and an explicit scientific acceptance criterion; successful execution alone should not count as completing the intended claim.

[Insights from Autoresearch for Solar Panel Segmentation](https://arxiv.org/abs/2610.10491) · Written passage

Origin: `research-team-2610.10491` · Version: `22bcded05aecba83c6a4594604bdc843c3061c7ccdf19d4be43c9ea27beaec4f`

Saved evidence: `data/assets/a007976d7a6dcb8c99635a7e/22bcded05aecba83c6a4594604bdc843c3061c7ccdf19d4be43c9ea27beaec4f/text.txt`

> Failed runs are treated as rejections.

[ResearchFlow-Eval: Tracing the Execution Gap in End-to-End Multi-Claim Autoresearch](https://arxiv.org/abs/2610.18088) · Written passage

Origin: `arxiv-unresolved-team` · Version: `9f5a3d8ad0d87cf4b75e0b27ee825183acc71c2811e8bb96e1a59f3c5dca2c35`

Saved evidence: `data/assets/51fd6c05fff2f297f454f717/9f5a3d8ad0d87cf4b75e0b27ee825183acc71c2811e8bb96e1a59f3c5dca2c35/text.txt`

> The system’s records organize its experiments under its own claim names and scopes, so a reported success can refer to a narrower experiment than the required claim.

[Hill-Climbing a Protein Language Model: A Taste of Autoresearch for Scientific Discovery](https://jojoml.github.io/blog/2026/nanoproteinlm-agenticls/) · Written passage

Origin: `nanoproteinlm-authors` · Version: `2b0d8382c674620fd174f5c60697d5bdf4728371aa386ebba1986c60e1eef65b`

Saved evidence: `data/assets/084a91218ed6d51df5ab9f17/2b0d8382c674620fd174f5c60697d5bdf4728371aa386ebba1986c60e1eef65b/text.txt`

> A final scaled-up ablation of the confirmed improvements.

## 02 — Which claims survive: gains must keep their conditions attached

Specific experimental gains survive scrutiny; broad claims about scientific validity, orchestration superiority and efficiency often do not. The decisive test is whether the result retains its comparator, metric, denominator and uncertainty when summarized.

### 02-c1

source_claim: NanoProteinLM reports that two 72-round searches lowered validation loss but left a substantial gap to the best contact-precision setting. Optimizing that reward did not establish equivalent progress on the downstream proxy.

[Hill-Climbing a Protein Language Model: A Taste of Autoresearch for Scientific Discovery](https://jojoml.github.io/blog/2026/nanoproteinlm-agenticls/) · Written passage

Origin: `nanoproteinlm-authors` · Version: `2b0d8382c674620fd174f5c60697d5bdf4728371aa386ebba1986c60e1eef65b`

Saved evidence: `data/assets/084a91218ed6d51df5ab9f17/2b0d8382c674620fd174f5c60697d5bdf4728371aa386ebba1986c60e1eef65b/text.txt`

> To see how agents behave in this environment, we let Codex Astra and Claude Opus 5.5 each run 72 rounds of search against validation loss. Both lowered the loss, and after 12 hours of training both recipes still beat our reference on it. Their contact precision (a proxy metric for downstream protein folding), though, shows a large gap to the best setting.

### 02-c2

inference: The production account's claim that immutable evaluation prevents metric gaming is contradicted by its own singleton-cluster example. Protecting evaluator code does not ensure that a higher score represents useful output.

[AutoResearch at Production Scale: Failure Modes and a Multi-Agent Framework](https://arxiv.org/abs/2609.30541) · Written passage

Origin: `research-team-2609.30541` · Version: `7d04403761d8cb23614022d48ddb879a6de4fb7f5af821bb1d1d2cb773d97ec4`

Saved evidence: `data/assets/7082835cef4c8540dcb8d480/7d04403761d8cb23614022d48ddb879a6de4fb7f5af821bb1d1d2cb773d97ec4/text.txt`

> In both systems the agent can read the evaluator’s output but cannot change its code, so it cannot inflate its own score by gaming the metric.

[AutoResearch at Production Scale: Failure Modes and a Multi-Agent Framework](https://arxiv.org/abs/2609.30541) · Written passage

Origin: `research-team-2609.30541` · Version: `7d04403761d8cb23614022d48ddb879a6de4fb7f5af821bb1d1d2cb773d97ec4`

Saved evidence: `data/assets/7082835cef4c8540dcb8d480/7d04403761d8cb23614022d48ddb879a6de4fb7f5af821bb1d1d2cb773d97ec4/text.txt`

> In System B, the agent discovered that maximizing codebook size trivially improves weighted coherence by creating more fine-grained clusters, but the resulting hierarchy was unusable—deep levels collapsed into singletons.

[AutoResearch at Production Scale: Failure Modes and a Multi-Agent Framework](https://arxiv.org/abs/2609.30541) · Written passage

Origin: `research-team-2609.30541` · Version: `7d04403761d8cb23614022d48ddb879a6de4fb7f5af821bb1d1d2cb773d97ec4`

Saved evidence: `data/assets/7082835cef4c8540dcb8d480/7d04403761d8cb23614022d48ddb879a6de4fb7f5af821bb1d1d2cb773d97ec4/text.txt`

> The training data—co-purchase behavioral graphs and customer purchase logs—is proprietary and cannot be released;

### 02-c3

source_claim: Malena's authors report a 62.5% medal rate versus 47.1% for the best external harness tested with GLM 5.2 under matched model, hardware and budget. The conclusion remains backbone- and metric-specific: Gemma favors MLEvolve on percentile.

[How Much of a Harness Does a Strong Agent Need for Autonomous ML Engineering?](https://arxiv.org/abs/2609.40303) · Written passage

Origin: `research-team-2609.40303` · Version: `6c598d9a3db4f487a0045a147e48bc3e4064e2b81bf388f4ac0947b9d96c78ec`

Saved evidence: `data/assets/7f0901064878a294934bd154/6c598d9a3db4f487a0045a147e48bc3e4064e2b81bf388f4ac0947b9d96c78ec/text.txt`

> Holding the model, hardware, and budget fixed, none of the published harnesses we tested significantly outperforms the plain agent session with frontier backbones. With GLM 5.2, Malena earns a medal on 62.5% of the competitions, compared with 47.1% for the best external harness tested.

[How Much of a Harness Does a Strong Agent Need for Autonomous ML Engineering?](https://arxiv.org/abs/2609.40303) · Written passage

Origin: `research-team-2609.40303` · Version: `6c598d9a3db4f487a0045a147e48bc3e4064e2b81bf388f4ac0947b9d96c78ec`

Saved evidence: `data/assets/7f0901064878a294934bd154/6c598d9a3db4f487a0045a147e48bc3e4064e2b81bf388f4ac0947b9d96c78ec/text.txt`

> The only backbone where Malena presents a significant regression against other baselines is with Gemma 4 31B — the weaker of all models tested — where MLEvolve outperforms according to the percentile metric

### 02-c4

source_claim: The oversight study's filtered analysis leaves nine of 30 submissions passing full-trajectory review, rather than the original 12 of 33. This supports a bounded finding about review misses, while the disputed cases and unvalidated reference labels limit confidence in the exact rate.

[Reward Hacking Challenges Oversight of Autonomous Research Agents](https://arxiv.org/abs/2609.28614) · Written passage

Origin: `research-team-2609.28614` · Version: `3c11fafcee8a531bb96d38ae9a2779c131ae2e2501195df7ae79cba7af4192b6`

Saved evidence: `data/assets/235ddeb91911d80fff910262/3c11fafcee8a531bb96d38ae9a2779c131ae2e2501195df7ae79cba7af4192b6/text.txt`

> A closer examination of the original 33 evasions identifies three disputed PAC-Bayes cases whose reviewer explanations describe legitimate bound improvements.

[Reward Hacking Challenges Oversight of Autonomous Research Agents](https://arxiv.org/abs/2609.28614) · Written passage

Origin: `research-team-2609.28614` · Version: `3c11fafcee8a531bb96d38ae9a2779c131ae2e2501195df7ae79cba7af4192b6`

Saved evidence: `data/assets/235ddeb91911d80fff910262/3c11fafcee8a531bb96d38ae9a2779c131ae2e2501195df7ae79cba7af4192b6/text.txt`

> Excluding these cases in a sensitivity analysis leaves 30 submissions, nine of which still pass full-trajectory review

[Reward Hacking Challenges Oversight of Autonomous Research Agents](https://arxiv.org/abs/2609.28614) · Written passage

Origin: `research-team-2609.28614` · Version: `3c11fafcee8a531bb96d38ae9a2779c131ae2e2501195df7ae79cba7af4192b6`

Saved evidence: `data/assets/235ddeb91911d80fff910262/3c11fafcee8a531bb96d38ae9a2779c131ae2e2501195df7ae79cba7af4192b6/text.txt`

> This combined rule is the operational reference standard for E2–E3, not independently validated ground truth.

### 02-c5

inference: AutoMIP's token accounting needs clarification before its reported figure can be presented as a total campaign budget: the metrics definition specifies averages, while the ablation prose calls 1,070,460 tokens a total.

[Autoresearch in Mixed-Integer Linear and Nonlinear Programming](https://arxiv.org/abs/2609.39360) · Written passage

Origin: `research-team-2609.39360` · Version: `bc44cd416a3cec196c5ff3ae89d1d7f5f529cfcb851b97b519470fc6baccac09`

Saved evidence: `data/assets/090f19610270f1b804a5bb8a/bc44cd416a3cec196c5ff3ae89d1d7f5f529cfcb851b97b519470fc6baccac09/text.txt`

> Token values represent average token consumption over all instances (in each time interval), including unsuccessful runs.

[Autoresearch in Mixed-Integer Linear and Nonlinear Programming](https://arxiv.org/abs/2609.39360) · Written passage

Origin: `research-team-2609.39360` · Version: `bc44cd416a3cec196c5ff3ae89d1d7f5f529cfcb851b97b519470fc6baccac09`

Saved evidence: `data/assets/090f19610270f1b804a5bb8a/bc44cd416a3cec196c5ff3ae89d1d7f5f529cfcb851b97b519470fc6baccac09/text.txt`

> It also uses the fewest tokens overall, with 1,070,460 total tokens

### 02-c6

inference: A student should accept an agent's improvement only after checking the intended scientific outcome separately from the optimized score. Protected evaluation and review records help, but neither alone establishes validity.

[Reward Hacking Challenges Oversight of Autonomous Research Agents](https://arxiv.org/abs/2609.28614) · Written passage

Origin: `research-team-2609.28614` · Version: `3c11fafcee8a531bb96d38ae9a2779c131ae2e2501195df7ae79cba7af4192b6`

Saved evidence: `data/assets/235ddeb91911d80fff910262/3c11fafcee8a531bb96d38ae9a2779c131ae2e2501195df7ae79cba7af4192b6/text.txt`

> Reproduction should check the intended scientific
> result, not merely recover the reported score.

[Hill-Climbing a Protein Language Model: A Taste of Autoresearch for Scientific Discovery](https://jojoml.github.io/blog/2026/nanoproteinlm-agenticls/) · Written passage

Origin: `nanoproteinlm-authors` · Version: `2b0d8382c674620fd174f5c60697d5bdf4728371aa386ebba1986c60e1eef65b`

Saved evidence: `data/assets/084a91218ed6d51df5ab9f17/2b0d8382c674620fd174f5c60697d5bdf4728371aa386ebba1986c60e1eef65b/text.txt`

> The agent optimizes the reward as written, and any gap between that reward and the scientific goal is open to it.

[AutoResearch at Production Scale: Failure Modes and a Multi-Agent Framework](https://arxiv.org/abs/2609.30541) · Written passage

Origin: `research-team-2609.30541` · Version: `7d04403761d8cb23614022d48ddb879a6de4fb7f5af821bb1d1d2cb773d97ec4`

Saved evidence: `data/assets/7082835cef4c8540dcb8d480/7d04403761d8cb23614022d48ddb879a6de4fb7f5af821bb1d1d2cb773d97ec4/text.txt`

> We had to introduce a guardrail constraining n_levels and add a tertiary cluster-usability metric to prevent the agent from gaming coherence at the expense of a meaningful hierarchy.

## 03 — Implications: build a small audit trail before expanding autonomy

Start with a prospective, bounded experiment whose instructions, evaluator, records and total budget can be inspected. Expand delegation only when repeated tests on unused tasks justify it; the next useful evidence is transferable performance and complete accounting, not a more autonomous-looking workflow.

### 03-c1

source_claim: AI Code King's procedure changes workflow instructions while keeping the underlying model and grading rules fixed. It should be described as instruction optimization, not training model weights, and its proposed candidates are not demonstrated gains.

[My Self Training Claude Code Setup: I Made Claude Code TRAIN ITSELF!](https://www.youtube.com/watch?v=wMQB33rM28I&t=56s) · 56.80–61.78 seconds (s00011)

Origin: `aicodeking` · Version: `91b5117a082251bc859d7cb81ba933c439e1b0450075c2bf98b2b8112bb7d58e`

Saved evidence: `data/assets/youtube-wMQB33rM28I/91b5117a082251bc859d7cb81ba933c439e1b0450075c2bf98b2b8112bb7d58e/text.txt`

> the changes on tasks it hasn't practiced on. The underlying Claude model stays the same.

[My Self Training Claude Code Setup: I Made Claude Code TRAIN ITSELF!](https://www.youtube.com/watch?v=wMQB33rM28I&t=270s) · 270.98–275.98 seconds (s00056)

Origin: `aicodeking` · Version: `91b5117a082251bc859d7cb81ba933c439e1b0450075c2bf98b2b8112bb7d58e`

Saved evidence: `data/assets/youtube-wMQB33rM28I/91b5117a082251bc859d7cb81ba933c439e1b0450075c2bf98b2b8112bb7d58e/text.txt`

> project. The optimizer can change the workflow instructions. The grading rules stay fixed. That

[My Self Training Claude Code Setup: I Made Claude Code TRAIN ITSELF!](https://www.youtube.com/watch?v=wMQB33rM28I&t=565s) · 565.32–569.62 seconds (s00122)

Origin: `aicodeking` · Version: `91b5117a082251bc859d7cb81ba933c439e1b0450075c2bf98b2b8112bb7d58e`

Saved evidence: `data/assets/youtube-wMQB33rM28I/91b5117a082251bc859d7cb81ba933c439e1b0450075c2bf98b2b8112bb7d58e/text.txt`

> Those are examples of candidates, not results we're assuming in advance. The actual change

### 03-c2

inference: The tutorial's planned 48 coding trials exclude optimizer reasoning, setup and rehearsals. Students should budget the whole search rather than treating a worker-trial count as total expenditure.

[My Self Training Claude Code Setup: I Made Claude Code TRAIN ITSELF!](https://www.youtube.com/watch?v=wMQB33rM28I&t=751s) · 751.74–757.46 seconds (s00163)

Origin: `aicodeking` · Version: `91b5117a082251bc859d7cb81ba933c439e1b0450075c2bf98b2b8112bb7d58e`

Saved evidence: `data/assets/youtube-wMQB33rM28I/91b5117a082251bc859d7cb81ba933c439e1b0450075c2bf98b2b8112bb7d58e/text.txt`

> tasks three times each adds another 12. That's 48 coding trials, before counting the optimizer's

[My Self Training Claude Code Setup: I Made Claude Code TRAIN ITSELF!](https://www.youtube.com/watch?v=wMQB33rM28I&t=757s) · 757.46–762.38 seconds (s00164)

Origin: `aicodeking` · Version: `91b5117a082251bc859d7cb81ba933c439e1b0450075c2bf98b2b8112bb7d58e`

Saved evidence: `data/assets/youtube-wMQB33rM28I/91b5117a082251bc859d7cb81ba933c439e1b0450075c2bf98b2b8112bb7d58e/text.txt`

> own thinking, setup, or any rehearsals. So, the auto-research plugin is open source,

### 03-c3

inference: Why Try AI recommends representative tasks, fresh chats with equal file and tool access, and judgments tied to specific evidence. These are usable comparison procedures; the author's scoped model preference does not establish general superiority.

[The Best AI Benchmark Is Your Own Work](https://www.whytryai.com/p/switch-ai-models) · Written passage

Origin: `whytryai` · Version: `6d392f0b897d89aba5f23830f5b954824cd8a50f3e5b222e12b93c42db9bf552`

Saved evidence: `data/assets/075b80e31faba3a92a3d7712/6d392f0b897d89aba5f23830f5b954824cd8a50f3e5b222e12b93c42db9bf552/text.txt`

> suggest a few tasks that represent something I do often, and where I can easily evaluate the outcome.

[The Best AI Benchmark Is Your Own Work](https://www.whytryai.com/p/switch-ai-models) · Written passage

Origin: `whytryai` · Version: `6d392f0b897d89aba5f23830f5b954824cd8a50f3e5b222e12b93c42db9bf552`

Saved evidence: `data/assets/075b80e31faba3a92a3d7712/6d392f0b897d89aba5f23830f5b954824cd8a50f3e5b222e12b93c42db9bf552/text.txt`

> Run the resulting test prompt in fresh chats in both models with access to the same files and tools (e.g. web search).

[The Best AI Benchmark Is Your Own Work](https://www.whytryai.com/p/switch-ai-models) · Written passage

Origin: `whytryai` · Version: `6d392f0b897d89aba5f23830f5b954824cd8a50f3e5b222e12b93c42db9bf552`

Saved evidence: `data/assets/075b80e31faba3a92a3d7712/6d392f0b897d89aba5f23830f5b954824cd8a50f3e5b222e12b93c42db9bf552/text.txt`

> Point to specific parts of each answer that support your judgment. Flag anything you can’t verify.

[The Best AI Benchmark Is Your Own Work](https://www.whytryai.com/p/switch-ai-models) · Written passage

Origin: `whytryai` · Version: `6d392f0b897d89aba5f23830f5b954824cd8a50f3e5b222e12b93c42db9bf552`

Saved evidence: `data/assets/075b80e31faba3a92a3d7712/6d392f0b897d89aba5f23830f5b954824cd8a50f3e5b222e12b93c42db9bf552/text.txt`

> ChatGPT was clearly better for my scoped research

### 03-c4

inference: MIRA describes work orders containing objectives, evidence, resource guidance, acceptance criteria and stopping conditions, with failures and contradictory results retained for later decisions. Students can adopt that record structure without assuming its performance transfers.

[Learning What to Investigate Next: Meta-Reasoning for Long-Horizon Research Agents](https://arxiv.org/abs/2610.02525) · Written passage

Origin: `arxiv-unresolved-team` · Version: `2c18cdc1f7cd0b9f4f773d6fa5733d29d115f5752e8ad9fe28d99ad61680389e`

Saved evidence: `data/assets/2c2f305856a15081f2fe9066/2c18cdc1f7cd0b9f4f773d6fa5733d29d115f5752e8ad9fe28d99ad61680389e/text.txt`

> Its work order states the objective, relevant evidence, resource guidance, acceptance criteria, and stopping condition.

[Learning What to Investigate Next: Meta-Reasoning for Long-Horizon Research Agents](https://arxiv.org/abs/2610.02525) · Written passage

Origin: `arxiv-unresolved-team` · Version: `2c18cdc1f7cd0b9f4f773d6fa5733d29d115f5752e8ad9fe28d99ad61680389e`

Saved evidence: `data/assets/2c2f305856a15081f2fe9066/2c18cdc1f7cd0b9f4f773d6fa5733d29d115f5752e8ad9fe28d99ad61680389e/text.txt`

> Recorded failures and contradictory results remain available to later decisions through the repository.

### 03-c5

inference: Campus Talks recommends describing study plans before collecting data, sharing code and variable descriptions, and allowing extra planning time. Applied to agent experiments, this supports a prospective review checkpoint rather than treating documentation as an afterthought.

[Campus Talks: How is AI affecting open research?](https://timeshighered.podbean.com/e/campus-talks-how-is-ai-affecting-open-research/) · 2369.31–2372.39 seconds (s00758)

Origin: `times-higher-education-campus` · Version: `de7f1e6f75069d6e82b0732ba9729ef01809dd0621fa585ccb3cb1690c97dcc9`

Saved evidence: `data/assets/e351f88c9bbc63c033f1aab7/de7f1e6f75069d6e82b0732ba9729ef01809dd0621fa585ccb3cb1690c97dcc9/text.txt`

> It's normal to pre-describe your plans

[Campus Talks: How is AI affecting open research?](https://timeshighered.podbean.com/e/campus-talks-how-is-ai-affecting-open-research/) · 2372.39–2374.67 seconds (s00759)

Origin: `times-higher-education-campus` · Version: `de7f1e6f75069d6e82b0732ba9729ef01809dd0621fa585ccb3cb1690c97dcc9`

Saved evidence: `data/assets/e351f88c9bbc63c033f1aab7/de7f1e6f75069d6e82b0732ba9729ef01809dd0621fa585ccb3cb1690c97dcc9/text.txt`

> for a study before you collect the data.

[Campus Talks: How is AI affecting open research?](https://timeshighered.podbean.com/e/campus-talks-how-is-ai-affecting-open-research/) · 2468.67–2471.87 seconds (s00799)

Origin: `times-higher-education-campus` · Version: `de7f1e6f75069d6e82b0732ba9729ef01809dd0621fa585ccb3cb1690c97dcc9`

Saved evidence: `data/assets/e351f88c9bbc63c033f1aab7/de7f1e6f75069d6e82b0732ba9729ef01809dd0621fa585ccb3cb1690c97dcc9/text.txt`

> You can share descriptions of your variables

[Campus Talks: How is AI affecting open research?](https://timeshighered.podbean.com/e/campus-talks-how-is-ai-affecting-open-research/) · 2473.71–2476.43 seconds (s00801)

Origin: `times-higher-education-campus` · Version: `de7f1e6f75069d6e82b0732ba9729ef01809dd0621fa585ccb3cb1690c97dcc9`

Saved evidence: `data/assets/e351f88c9bbc63c033f1aab7/de7f1e6f75069d6e82b0732ba9729ef01809dd0621fa585ccb3cb1690c97dcc9/text.txt`

> You can share code if you have run a program

[Campus Talks: How is AI affecting open research?](https://timeshighered.podbean.com/e/campus-talks-how-is-ai-affecting-open-research/) · 3276.07–3280.27 seconds (s01090)

Origin: `times-higher-education-campus` · Version: `de7f1e6f75069d6e82b0732ba9729ef01809dd0621fa585ccb3cb1690c97dcc9`

Saved evidence: `data/assets/e351f88c9bbc63c033f1aab7/de7f1e6f75069d6e82b0732ba9729ef01809dd0621fa585ccb3cb1690c97dcc9/text.txt`

> But make sure that you build extra time into your planning.

### 03-c6

source_claim: Periodic Labs' founders describe full autonomy as a non-goal and prioritize useful experimental data and tractable bottlenecks. This is a commercially interested practitioner perspective: the same interview describes bringing their tools into industry.

[Synthesis Superintelligence: from Semiconductors to Superconductors — Periodic Labs’ Liam Fedus and Ekin Dogus Cubuk](https://www.latent.space/p/periodic) · 3046.00–3099.00 seconds (s00230)

Origin: `periodic-labs-interviews` · Version: `2440cc1580de805fb537ea10d57c87f518177ce7fa5c4cf63e2260a65098b0dc`

Saved evidence: `data/assets/ead4cdfb34d1b428c1cd760b/2440cc1580de805fb537ea10d57c87f518177ce7fa5c4cf63e2260a65098b0dc/text.txt`

> Yeah. I think maybe one process is, by having a mix of humans and automation, you can identify really quickly what are some of the bottlenecks in the experimental process, and you start alleviating those bottlenecks one at a time. And so for example, if there’s some really tricky dexterity task that humans are excellent at but you’d have to spend months automating machine, maybe don’t spend a ton of time there. And maybe a more promising thing is something very routine that takes up a huge amount of scientists’ and technicians’ time, and it’s easy to automate. So I think it’there’s this pragmatism to it. But ultimately what we want from the lab is a huge quantity of data, high-quality data, diverse data, and those are our goals. And full autonomy is a non-goal. It’s sort of in the service that we use automation in the service of achieving the goals on the data.

[Synthesis Superintelligence: from Semiconductors to Superconductors — Periodic Labs’ Liam Fedus and Ekin Dogus Cubuk](https://www.latent.space/p/periodic) · 4506.00–4613.00 seconds (s00341)

Origin: `periodic-labs-interviews` · Version: `2440cc1580de805fb537ea10d57c87f518177ce7fa5c4cf63e2260a65098b0dc`

Saved evidence: `data/assets/ead4cdfb34d1b428c1cd760b/2440cc1580de805fb537ea10d57c87f518177ce7fa5c4cf63e2260a65098b0dc/text.txt`

> For ourselves. So we’ve been customer zero. Now what we’re doing is we’re taking these same tools to different industries, and we’we have a huge focus right now in the semiconductor industry. However, in order to do this these are very, private companies. We need to be able to operate within some of the most secure environments. And so our Periodic forward-deployed engineers and researchers will actually be on site working and actually integrating our AI systems, our computational systems to help our partners get to their goal states more quickly. So basically the tools, the know-how that we’ve built in doing our own materials discovery, materials engineering, we’re now bringing to industry. And we think this is the most effective way to get partners to their end states and to their goals, rather than just throwing some technology over the wall and telling them to figure it out. Then these forward-deployed engineers will also do the inference locally, but then also can, train on the data. So again, once we take our system that understands these different areas and we deploy, we can make it expert on the customers or the partners’ data so that they can own their own intelligence and have systems that understand this much more effectively than just hitting some API or some untrained model. And so this is a much expanded, forward-deployment engineering role than typical because this really requires some very deep, machine learning expertise. You have to be incredibly precise from a data training perspective, infrastructure perspective, but also a physics perspective. So we’re working with highly technical industries. They have to understand, different areas of chemistry, material science, some of the devices. And so that, those are the roles we’re building out right now.

### 03-c7

inference: The next evidence to watch is repeated performance on unused tasks, accompanied by inspectable code and retained failure records. A development-score gain without held-out improvement should not justify expanding delegation.

[My Self Training Claude Code Setup: I Made Claude Code TRAIN ITSELF!](https://www.youtube.com/watch?v=wMQB33rM28I&t=653s) · 653.82–658.94 seconds (s00142)

Origin: `aicodeking` · Version: `91b5117a082251bc859d7cb81ba933c439e1b0450075c2bf98b2b8112bb7d58e`

Saved evidence: `data/assets/youtube-wMQB33rM28I/91b5117a082251bc859d7cb81ba933c439e1b0450075c2bf98b2b8112bb7d58e/text.txt`

> Claude sessions again. Run each version three times per task with the same limits and alternate

[My Self Training Claude Code Setup: I Made Claude Code TRAIN ITSELF!](https://www.youtube.com/watch?v=wMQB33rM28I&t=695s) · 695.58–701.74 seconds (s00152)

Origin: `aicodeking` · Version: `91b5117a082251bc859d7cb81ba933c439e1b0450075c2bf98b2b8112bb7d58e`

Saved evidence: `data/assets/youtube-wMQB33rM28I/91b5117a082251bc859d7cb81ba933c439e1b0450075c2bf98b2b8112bb7d58e/text.txt`

> universal coding upgrade. If development improves, but the held-out results stay flat

[My Self Training Claude Code Setup: I Made Claude Code TRAIN ITSELF!](https://www.youtube.com/watch?v=wMQB33rM28I&t=701s) · 701.74–707.58 seconds (s00153)

Origin: `aicodeking` · Version: `91b5117a082251bc859d7cb81ba933c439e1b0450075c2bf98b2b8112bb7d58e`

Saved evidence: `data/assets/youtube-wMQB33rM28I/91b5117a082251bc859d7cb81ba933c439e1b0450075c2bf98b2b8112bb7d58e/text.txt`

> or get worse, we haven't demonstrated a transferable improvement. The search may have fitted the

[Campus Talks: How is AI affecting open research?](https://timeshighered.podbean.com/e/campus-talks-how-is-ai-affecting-open-research/) · 2473.71–2476.43 seconds (s00801)

Origin: `times-higher-education-campus` · Version: `de7f1e6f75069d6e82b0732ba9729ef01809dd0621fa585ccb3cb1690c97dcc9`

Saved evidence: `data/assets/e351f88c9bbc63c033f1aab7/de7f1e6f75069d6e82b0732ba9729ef01809dd0621fa585ccb3cb1690c97dcc9/text.txt`

> You can share code if you have run a program

[Learning What to Investigate Next: Meta-Reasoning for Long-Horizon Research Agents](https://arxiv.org/abs/2610.02525) · Written passage

Origin: `arxiv-unresolved-team` · Version: `2c18cdc1f7cd0b9f4f773d6fa5733d29d115f5752e8ad9fe28d99ad61680389e`

Saved evidence: `data/assets/2c2f305856a15081f2fe9066/2c18cdc1f7cd0b9f4f773d6fa5733d29d115f5752e8ad9fe28d99ad61680389e/text.txt`

> Recorded failures and contradictory results remain available to later decisions through the repository.
