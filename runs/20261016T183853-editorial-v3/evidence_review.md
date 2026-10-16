# Evidence review cards

Draft audit aid. Every media passage still requires listening against the original recording. Check interpretation and independence, not just string matches. No student approval is recorded here.

## 01 — What changed: agents can run bounded research loops

The useful development is a more concrete division of research work: agents execute and record iterations, while humans define objectives, choose scaling decisions and retain methodological control. The supplied reports support bounded delegation, not fully autonomous discovery.

### 01-c1

source_claim: Li and Lu report contact precision increasing from 28.2% to 36.6% at a matched 48.4B-token budget, with a human choosing which recipes to scale. This is a human-guided result.

[Hill-Climbing a Protein Language Model: A Taste of Autoresearch for Scientific Discovery](https://jojoml.github.io/blog/2026/nanoproteinlm-agenticls/) · Written passage

Origin: `nanoproteinlm-authors` · Version: `2b0d8382c674620fd174f5c60697d5bdf4728371aa386ebba1986c60e1eef65b`

Saved evidence: `data/assets/084a91218ed6d51df5ab9f17/2b0d8382c674620fd174f5c60697d5bdf4728371aa386ebba1986c60e1eef65b/text.txt`

> Starting from the ESMC recipe, a simple sequential search, with a human deciding which recipes to scale up, gave a recipe with about 30% higher long-range contact precision, from 28.2% to 36.6% P@L, at the same 48.4B-token budget.

### 01-c2

source_claim: Agora describes agents checking out exact parent commits, changing and evaluating code, and recording results. Its reported run occurred between April 26 and May 8, rather than during this publication window.

[Agora: Git as Shared Memory for Collective AutoResearch](https://arxiv.org/abs/2609.18094) · Written passage

Origin: `research-team-2609.18094` · Version: `66025228eaffdbf60602a9c3e085782385578f7304cce9751aff2a52b9936729`

Saved evidence: `data/assets/59b2cb8b434efeeb70a133bc/66025228eaffdbf60602a9c3e085782385578f7304cce9751aff2a52b9936729/text.txt`

> pick a parent, fetch and check out that exact commit, make one change,
> evaluate, commit everything needed to reproduce

[Agora: Git as Shared Memory for Collective AutoResearch](https://arxiv.org/abs/2609.18094) · Written passage

Origin: `research-team-2609.18094` · Version: `66025228eaffdbf60602a9c3e085782385578f7304cce9751aff2a52b9936729`

Saved evidence: `data/assets/59b2cb8b434efeeb70a133bc/66025228eaffdbf60602a9c3e085782385578f7304cce9751aff2a52b9936729/text.txt`

> The run lasted 11 days and 19 hours of
> server time, from the setup commit on April 26 to our cutoff on May 8

### 01-c3

inference: Agora's authors describe human interventions during the run, selection on one 200-text development evaluator and no fresh author rerun of the winner. Its experiment history therefore does not establish independent validation.

[Agora: Git as Shared Memory for Collective AutoResearch](https://arxiv.org/abs/2609.18094) · Written passage

Origin: `research-team-2609.18094` · Version: `66025228eaffdbf60602a9c3e085782385578f7304cce9751aff2a52b9936729`

Saved evidence: `data/assets/59b2cb8b434efeeb70a133bc/66025228eaffdbf60602a9c3e085782385578f7304cce9751aff2a52b9936729/text.txt`

> During the
> run we changed the server three times and the H100 workers’ prompt once.

[Agora: Git as Shared Memory for Collective AutoResearch](https://arxiv.org/abs/2609.18094) · Written passage

Origin: `research-team-2609.18094` · Version: `66025228eaffdbf60602a9c3e085782385578f7304cce9751aff2a52b9936729`

Saved evidence: `data/assets/59b2cb8b434efeeb70a133bc/66025228eaffdbf60602a9c3e085782385578f7304cce9751aff2a52b9936729/text.txt`

> Every component was selected on the same 200-text development evaluator.

[Agora: Git as Shared Memory for Collective AutoResearch](https://arxiv.org/abs/2609.18094) · Written passage

Origin: `research-team-2609.18094` · Version: `66025228eaffdbf60602a9c3e085782385578f7304cce9751aff2a52b9936729`

Saved evidence: `data/assets/59b2cb8b434efeeb70a133bc/66025228eaffdbf60602a9c3e085782385578f7304cce9751aff2a52b9936729/text.txt`

> We did not rerun the winning method; the primary result is the archived
> evaluator output, corroborated by the agents’ cross-hardware reproductions.

### 01-c4

source_claim: Periodic's founders say characterization shifted substantially toward AI assistance while campaign guidance became a mixture of human and AI work. This describes their workflow, not a measured productivity gain.

[Synthesis Superintelligence: from Semiconductors to Superconductors — Periodic Labs’ Liam Fedus and Ekin Dogus Cubuk](https://www.latent.space/p/periodic) · 3864.00–3904.00 seconds (s00305)

Origin: `periodic-labs-interviews` · Version: `2440cc1580de805fb537ea10d57c87f518177ce7fa5c4cf63e2260a65098b0dc`

Saved evidence: `data/assets/ead4cdfb34d1b428c1cd760b/2440cc1580de805fb537ea10d57c87f518177ce7fa5c4cf63e2260a65098b0dc/text.txt`

> So, I think even just using the guidance of campaigns, in the early days, that was fully human-driven. Now, increasingly, it’s a mix of AI-driven and human-driven. And then Doğuş was saying early on we identified that characterization was a big bottleneck. In the early days, it was human-driven, and the scientists were very much overwhelmed, and the balance has shifted significantly towards AI-driven. And this has allowed the scientists who were previously spending all of their time doing these refinements to now elevate their work to something else. But I think we’re. It’s really sort of a function of time. There’it’s always changing at each of these levels.
> Search, Optimization, and Design of Experiments

### 01-c5

source_claim: The founders explicitly call full autonomy a non-goal and describe commercial deployment of their tools to industry partners. Their account should be read as an interested operational perspective.

[Synthesis Superintelligence: from Semiconductors to Superconductors — Periodic Labs’ Liam Fedus and Ekin Dogus Cubuk](https://www.latent.space/p/periodic) · 3046.00–3099.00 seconds (s00230)

Origin: `periodic-labs-interviews` · Version: `2440cc1580de805fb537ea10d57c87f518177ce7fa5c4cf63e2260a65098b0dc`

Saved evidence: `data/assets/ead4cdfb34d1b428c1cd760b/2440cc1580de805fb537ea10d57c87f518177ce7fa5c4cf63e2260a65098b0dc/text.txt`

> Yeah. I think maybe one process is, by having a mix of humans and automation, you can identify really quickly what are some of the bottlenecks in the experimental process, and you start alleviating those bottlenecks one at a time. And so for example, if there’s some really tricky dexterity task that humans are excellent at but you’d have to spend months automating machine, maybe don’t spend a ton of time there. And maybe a more promising thing is something very routine that takes up a huge amount of scientists’ and technicians’ time, and it’s easy to automate. So I think it’there’s this pragmatism to it. But ultimately what we want from the lab is a huge quantity of data, high-quality data, diverse data, and those are our goals. And full autonomy is a non-goal. It’s sort of in the service that we use automation in the service of achieving the goals on the data.

[Synthesis Superintelligence: from Semiconductors to Superconductors — Periodic Labs’ Liam Fedus and Ekin Dogus Cubuk](https://www.latent.space/p/periodic) · 4506.00–4613.00 seconds (s00341)

Origin: `periodic-labs-interviews` · Version: `2440cc1580de805fb537ea10d57c87f518177ce7fa5c4cf63e2260a65098b0dc`

Saved evidence: `data/assets/ead4cdfb34d1b428c1cd760b/2440cc1580de805fb537ea10d57c87f518177ce7fa5c4cf63e2260a65098b0dc/text.txt`

> For ourselves. So we’ve been customer zero. Now what we’re doing is we’re taking these same tools to different industries, and we’we have a huge focus right now in the semiconductor industry. However, in order to do this these are very, private companies. We need to be able to operate within some of the most secure environments. And so our Periodic forward-deployed engineers and researchers will actually be on site working and actually integrating our AI systems, our computational systems to help our partners get to their goal states more quickly. So basically the tools, the know-how that we’ve built in doing our own materials discovery, materials engineering, we’re now bringing to industry. And we think this is the most effective way to get partners to their end states and to their goals, rather than just throwing some technology over the wall and telling them to figure it out. Then these forward-deployed engineers will also do the inference locally, but then also can, train on the data. So again, once we take our system that understands these different areas and we deploy, we can make it expert on the customers or the partners’ data so that they can own their own intelligence and have systems that understand this much more effectively than just hitting some API or some untrained model. And so this is a much expanded, forward-deployment engineering role than typical because this really requires some very deep, machine learning expertise. You have to be incredibly precise from a data training perspective, infrastructure perspective, but also a physics perspective. So we’re working with highly technical industries. They have to understand, different areas of chemistry, material science, some of the devices. And so that, those are the roles we’re building out right now.

### 01-c6

inference: A practical delegation boundary is to let an agent execute bounded changes and preserve failed attempts, while the student fixes the scientific objective and decides which candidates deserve larger validation runs.

[Hill-Climbing a Protein Language Model: A Taste of Autoresearch for Scientific Discovery](https://jojoml.github.io/blog/2026/nanoproteinlm-agenticls/) · Written passage

Origin: `nanoproteinlm-authors` · Version: `2b0d8382c674620fd174f5c60697d5bdf4728371aa386ebba1986c60e1eef65b`

Saved evidence: `data/assets/084a91218ed6d51df5ab9f17/2b0d8382c674620fd174f5c60697d5bdf4728371aa386ebba1986c60e1eef65b/text.txt`

> The scientific outcome the campaign should improve, fixed before search.

[Hill-Climbing a Protein Language Model: A Taste of Autoresearch for Scientific Discovery](https://jojoml.github.io/blog/2026/nanoproteinlm-agenticls/) · Written passage

Origin: `nanoproteinlm-authors` · Version: `2b0d8382c674620fd174f5c60697d5bdf4728371aa386ebba1986c60e1eef65b`

Saved evidence: `data/assets/084a91218ed6d51df5ab9f17/2b0d8382c674620fd174f5c60697d5bdf4728371aa386ebba1986c60e1eef65b/text.txt`

> A larger-budget retraining of the selected recipe against the baseline, testing whether search-time gains carry over.

[Agora: Git as Shared Memory for Collective AutoResearch](https://arxiv.org/abs/2609.18094) · Written passage

Origin: `research-team-2609.18094` · Version: `66025228eaffdbf60602a9c3e085782385578f7304cce9751aff2a52b9936729`

Saved evidence: `data/assets/59b2cb8b434efeeb70a133bc/66025228eaffdbf60602a9c3e085782385578f7304cce9751aff2a52b9936729/text.txt`

> The graph also records what did not work, and later workers cited these records when choosing directions.

## 02 — Which claims survive: local gains need separate validity and transfer checks

The defensible claims are conditional: an intervention helped under a particular protocol, or a verification step exposed a particular failure. A higher search score alone cannot establish scientific usefulness, valid implementation or transfer.

### 02-c1

source_claim: The protein-search authors report that lower validation loss did not identify the strongest contact-precision recipe, and only four of seven changes survived final ablation. Search-time improvement was therefore an incomplete acceptance criterion in this study.

[Hill-Climbing a Protein Language Model: A Taste of Autoresearch for Scientific Discovery](https://jojoml.github.io/blog/2026/nanoproteinlm-agenticls/) · Written passage

Origin: `nanoproteinlm-authors` · Version: `2b0d8382c674620fd174f5c60697d5bdf4728371aa386ebba1986c60e1eef65b`

Saved evidence: `data/assets/084a91218ed6d51df5ab9f17/2b0d8382c674620fd174f5c60697d5bdf4728371aa386ebba1986c60e1eef65b/text.txt`

> Both lowered the loss, and after 12 hours of training both recipes still beat our reference on it. Their contact precision (a proxy metric for downstream protein folding), though, shows a large gap to the best setting.

[Hill-Climbing a Protein Language Model: A Taste of Autoresearch for Scientific Discovery](https://jojoml.github.io/blog/2026/nanoproteinlm-agenticls/) · Written passage

Origin: `nanoproteinlm-authors` · Version: `2b0d8382c674620fd174f5c60697d5bdf4728371aa386ebba1986c60e1eef65b`

Saved evidence: `data/assets/084a91218ed6d51df5ab9f17/2b0d8382c674620fd174f5c60697d5bdf4728371aa386ebba1986c60e1eef65b/text.txt`

> Four of the seven changes survive the final ablation study.

### 02-c2

source_claim: In the kernel authors' first stress-test run, hidden checks falsified 12 of 35 programs that passed the public screen. This establishes failures in that cohort, not a universal agent failure rate.

[Kernel Autoresearch for Open-Ended Model Discovery](https://arxiv.org/abs/2610.10394) · Written passage

Origin: `arxiv-unresolved-team` · Version: `b5c10a5a1f3bc0adb95fe7a8ee96127189a24131d2304c6d0f00b108ccee3a5f`

Saved evidence: `data/assets/0ff8643be07c7b70497b5caf/b5c10a5a1f3bc0adb95fe7a8ee96127189a24131d2304c6d0f00b108ccee3a5f/text.txt`

> In the first run, of 40 unrestricted programs, three fail to execute and two produce an indefinite Gram matrix during the public screen, leaving 35 Tier-1 passes. The hidden suite falsifies 12 of these.

### 02-c3

inference: The kernel study's transfer evidence is mixed: archived DWF won only four of sixteen real-data comparisons, while the three ten-year forward forecasting diagnostics favored CAKE. Broad superiority does not survive these checks.

[Kernel Autoresearch for Open-Ended Model Discovery](https://arxiv.org/abs/2610.10394) · Written passage

Origin: `arxiv-unresolved-team` · Version: `b5c10a5a1f3bc0adb95fe7a8ee96127189a24131d2304c6d0f00b108ccee3a5f`

Saved evidence: `data/assets/0ff8643be07c7b70497b5caf/b5c10a5a1f3bc0adb95fe7a8ee96127189a24131d2304c6d0f00b108ccee3a5f/text.txt`

> With the archived geometry, DWF wins 4 of 16 dataset-by-sample-size comparisons

[Kernel Autoresearch for Open-Ended Model Discovery](https://arxiv.org/abs/2610.10394) · Written passage

Origin: `arxiv-unresolved-team` · Version: `b5c10a5a1f3bc0adb95fe7a8ee96127189a24131d2304c6d0f00b108ccee3a5f`

Saved evidence: `data/assets/0ff8643be07c7b70497b5caf/b5c10a5a1f3bc0adb95fe7a8ee96127189a24131d2304c6d0f00b108ccee3a5f/text.txt`

> These three diagnostic splits favor CAKE for ten-year forward prediction.

### 02-c4

inference: The production report's claim that an immutable evaluator prevents metric gaming is too strong: the same report describes improved coherence producing unusable clusters. Evaluator integrity and metric validity require separate checks.

[AutoResearch at Production Scale: Failure Modes and a Multi-Agent Framework](https://arxiv.org/abs/2609.30541) · Written passage

Origin: `research-team-2609.30541` · Version: `7d04403761d8cb23614022d48ddb879a6de4fb7f5af821bb1d1d2cb773d97ec4`

Saved evidence: `data/assets/7082835cef4c8540dcb8d480/7d04403761d8cb23614022d48ddb879a6de4fb7f5af821bb1d1d2cb773d97ec4/text.txt`

> In both systems the agent can read the evaluator’s output but cannot change its code, so it cannot inflate its own score by gaming the metric.

[AutoResearch at Production Scale: Failure Modes and a Multi-Agent Framework](https://arxiv.org/abs/2609.30541) · Written passage

Origin: `research-team-2609.30541` · Version: `7d04403761d8cb23614022d48ddb879a6de4fb7f5af821bb1d1d2cb773d97ec4`

Saved evidence: `data/assets/7082835cef4c8540dcb8d480/7d04403761d8cb23614022d48ddb879a6de4fb7f5af821bb1d1d2cb773d97ec4/text.txt`

> In System B, the agent discovered that maximizing codebook size trivially improves weighted coherence by creating more fine-grained clusters, but the resulting hierarchy was unusable—deep levels collapsed into singletons.

### 02-c5

source_claim: Malena's authors report that tested published harnesses did not significantly outperform their plain session with frontier backbones under matched model, hardware and budget. Their weaker Gemma backbone nevertheless favored MLEvolve on percentile; the result does not establish universal harness redundancy.

[How Much of a Harness Does a Strong Agent Need for Autonomous ML Engineering?](https://arxiv.org/abs/2609.40303) · Written passage

Origin: `research-team-2609.40303` · Version: `6c598d9a3db4f487a0045a147e48bc3e4064e2b81bf388f4ac0947b9d96c78ec`

Saved evidence: `data/assets/7f0901064878a294934bd154/6c598d9a3db4f487a0045a147e48bc3e4064e2b81bf388f4ac0947b9d96c78ec/text.txt`

> Holding the model, hardware, and budget fixed, none of the published harnesses we tested significantly outperforms the plain agent session with frontier backbones.

[How Much of a Harness Does a Strong Agent Need for Autonomous ML Engineering?](https://arxiv.org/abs/2609.40303) · Written passage

Origin: `research-team-2609.40303` · Version: `6c598d9a3db4f487a0045a147e48bc3e4064e2b81bf388f4ac0947b9d96c78ec`

Saved evidence: `data/assets/7f0901064878a294934bd154/6c598d9a3db4f487a0045a147e48bc3e4064e2b81bf388f4ac0947b9d96c78ec/text.txt`

> The only backbone where Malena presents a significant regression against other baselines is with Gemma 4 31B — the weaker of all models tested — where MLEvolve outperforms according to the percentile metric

### 02-c6

inference: Students should report three separate outcomes: whether a candidate passes validity checks, improves the chosen metric and advances the intended scientific or practical objective. None should silently substitute for another.

[Kernel Autoresearch for Open-Ended Model Discovery](https://arxiv.org/abs/2610.10394) · Written passage

Origin: `arxiv-unresolved-team` · Version: `b5c10a5a1f3bc0adb95fe7a8ee96127189a24131d2304c6d0f00b108ccee3a5f`

Saved evidence: `data/assets/0ff8643be07c7b70497b5caf/b5c10a5a1f3bc0adb95fe7a8ee96127189a24131d2304c6d0f00b108ccee3a5f/text.txt`

> Thus, a correct PSD argument does not make the submitted code a valid kernel on the full domain.

[AutoResearch at Production Scale: Failure Modes and a Multi-Agent Framework](https://arxiv.org/abs/2609.30541) · Written passage

Origin: `research-team-2609.30541` · Version: `7d04403761d8cb23614022d48ddb879a6de4fb7f5af821bb1d1d2cb773d97ec4`

Saved evidence: `data/assets/7082835cef4c8540dcb8d480/7d04403761d8cb23614022d48ddb879a6de4fb7f5af821bb1d1d2cb773d97ec4/text.txt`

> neither has been validated against actual customer outcomes in this study

[Hill-Climbing a Protein Language Model: A Taste of Autoresearch for Scientific Discovery](https://jojoml.github.io/blog/2026/nanoproteinlm-agenticls/) · Written passage

Origin: `nanoproteinlm-authors` · Version: `2b0d8382c674620fd174f5c60697d5bdf4728371aa386ebba1986c60e1eef65b`

Saved evidence: `data/assets/084a91218ed6d51df5ab9f17/2b0d8382c674620fd174f5c60697d5bdf4728371aa386ebba1986c60e1eef65b/text.txt`

> Their contact precision (a proxy metric for downstream protein folding), though, shows a large gap to the best setting.

## 03 — Implications: build an experiment another person can check

The next useful investment is an auditable small experiment: fixed grading, held-out comparisons, recorded provenance, human review and complete resource accounting. Future agent claims become more actionable when another researcher can reconstruct both the result and its selection history.

### 03-c1

source_claim: AI Code King's procedure changes workflow instructions while leaving the underlying model and grading rules unchanged. Its 'self-training' framing should therefore be understood here as instruction optimization.

[My Self Training Claude Code Setup: I Made Claude Code TRAIN ITSELF!](https://www.youtube.com/watch?v=wMQB33rM28I&t=56s) · 56.80–61.78 seconds (s00011)

Origin: `aicodeking` · Version: `91b5117a082251bc859d7cb81ba933c439e1b0450075c2bf98b2b8112bb7d58e`

Saved evidence: `data/assets/youtube-wMQB33rM28I/91b5117a082251bc859d7cb81ba933c439e1b0450075c2bf98b2b8112bb7d58e/text.txt`

> the changes on tasks it hasn't practiced on. The underlying Claude model stays the same.

[My Self Training Claude Code Setup: I Made Claude Code TRAIN ITSELF!](https://www.youtube.com/watch?v=wMQB33rM28I&t=270s) · 270.98–275.98 seconds (s00056)

Origin: `aicodeking` · Version: `91b5117a082251bc859d7cb81ba933c439e1b0450075c2bf98b2b8112bb7d58e`

Saved evidence: `data/assets/youtube-wMQB33rM28I/91b5117a082251bc859d7cb81ba933c439e1b0450075c2bf98b2b8112bb7d58e/text.txt`

> project. The optimizer can change the workflow instructions. The grading rules stay fixed. That

### 03-c2

source_claim: The tutorial recommends comparison on tasks excluded from search, followed by human review of the winning instruction changes. Any human-edited version becomes a new candidate requiring evaluation; this is procedural advice, not an observed gain.

[My Self Training Claude Code Setup: I Made Claude Code TRAIN ITSELF!](https://www.youtube.com/watch?v=wMQB33rM28I&t=649s) · 649.90–653.82 seconds (s00141)

Origin: `aicodeking` · Version: `91b5117a082251bc859d7cb81ba933c439e1b0450075c2bf98b2b8112bb7d58e`

Saved evidence: `data/assets/youtube-wMQB33rM28I/91b5117a082251bc859d7cb81ba933c439e1b0450075c2bf98b2b8112bb7d58e/text.txt`

> instructions on the tasks we kept out of the search. Use fresh project copies and fresh

[My Self Training Claude Code Setup: I Made Claude Code TRAIN ITSELF!](https://www.youtube.com/watch?v=wMQB33rM28I&t=809s) · 809.46–814.14 seconds (s00176)

Origin: `aicodeking` · Version: `91b5117a082251bc859d7cb81ba933c439e1b0450075c2bf98b2b8112bb7d58e`

Saved evidence: `data/assets/youtube-wMQB33rM28I/91b5117a082251bc859d7cb81ba933c439e1b0450075c2bf98b2b8112bb7d58e/text.txt`

> Review the winning instruction diff. Remove anything tied to the practice tasks. Then

[My Self Training Claude Code Setup: I Made Claude Code TRAIN ITSELF!](https://www.youtube.com/watch?v=wMQB33rM28I&t=814s) · 814.14–818.78 seconds (s00177)

Origin: `aicodeking` · Version: `91b5117a082251bc859d7cb81ba933c439e1b0450075c2bf98b2b8112bb7d58e`

Saved evidence: `data/assets/youtube-wMQB33rM28I/91b5117a082251bc859d7cb81ba933c439e1b0450075c2bf98b2b8112bb7d58e/text.txt`

> treat that edited version as a new candidate that needs checking. Even a well-intended

### 03-c3

inference: Campus Talks recommends connecting data to provenance, sharing variable descriptions and executed analysis code, and allowing extra planning time. Applying that guidance to agent experiments means budgeting documentation work alongside execution, with sharing limited to what is appropriate and ethical.

[Campus Talks: How is AI affecting open research?](https://timeshighered.podbean.com/e/campus-talks-how-is-ai-affecting-open-research/) · 974.68–977.60 seconds (s00291)

Origin: `times-higher-education-campus` · Version: `de7f1e6f75069d6e82b0732ba9729ef01809dd0621fa585ccb3cb1690c97dcc9`

Saved evidence: `data/assets/e351f88c9bbc63c033f1aab7/de7f1e6f75069d6e82b0732ba9729ef01809dd0621fa585ccb3cb1690c97dcc9/text.txt`

> is that data needs to be connected

[Campus Talks: How is AI affecting open research?](https://timeshighered.podbean.com/e/campus-talks-how-is-ai-affecting-open-research/) · 977.60–980.00 seconds (s00292)

Origin: `times-higher-education-campus` · Version: `de7f1e6f75069d6e82b0732ba9729ef01809dd0621fa585ccb3cb1690c97dcc9`

Saved evidence: `data/assets/e351f88c9bbc63c033f1aab7/de7f1e6f75069d6e82b0732ba9729ef01809dd0621fa585ccb3cb1690c97dcc9/text.txt`

> to the provenance it comes from, yeah.

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

[Campus Talks: How is AI affecting open research?](https://timeshighered.podbean.com/e/campus-talks-how-is-ai-affecting-open-research/) · 2347.31–2350.51 seconds (s00748)

Origin: `times-higher-education-campus` · Version: `de7f1e6f75069d6e82b0732ba9729ef01809dd0621fa585ccb3cb1690c97dcc9`

Saved evidence: `data/assets/e351f88c9bbc63c033f1aab7/de7f1e6f75069d6e82b0732ba9729ef01809dd0621fa585ccb3cb1690c97dcc9/text.txt`

> make sharing, if it's appropriate and ethical,

### 03-c4

inference: ResearchFlow-Eval's authors report that 14 of 90 end-to-end claims met their criteria, with only one empirical claim met. Their judge received researcher spot-checking, so students should retain human review of AI judgments as a safeguard, without assuming demonstrated judge bias.

[ResearchFlow-Eval: Tracing the Execution Gap in End-to-End Multi-Claim Autoresearch](https://arxiv.org/abs/2610.18088) · Written passage

Origin: `arxiv-unresolved-team` · Version: `9f5a3d8ad0d87cf4b75e0b27ee825183acc71c2811e8bb96e1a59f3c5dca2c35`

Saved evidence: `data/assets/51fd6c05fff2f297f454f717/9f5a3d8ad0d87cf4b75e0b27ee825183acc71c2811e8bb96e1a59f3c5dca2c35/text.txt`

> Of the 90 end-to-end claims, 14 are met, and E5 for GPT-6 Astra is the only empirical claim met in an end-to-end run.

[ResearchFlow-Eval: Tracing the Execution Gap in End-to-End Multi-Claim Autoresearch](https://arxiv.org/abs/2610.18088) · Written passage

Origin: `arxiv-unresolved-team` · Version: `9f5a3d8ad0d87cf4b75e0b27ee825183acc71c2811e8bb96e1a59f3c5dca2c35`

Saved evidence: `data/assets/51fd6c05fff2f297f454f717/9f5a3d8ad0d87cf4b75e0b27ee825183acc71c2811e8bb96e1a59f3c5dca2c35/text.txt`

> A domain researcher spot-checked the judge’s ratings and rationales and found them largely consistent with their own assessment.

### 03-c5

inference: ResearchFlow-Eval permits optimization using test sessions but requires logging access and forbids describing optimization-informed results as untouched estimates. Students should likewise record when evaluation data influenced selection.

[ResearchFlow-Eval: Tracing the Execution Gap in End-to-End Multi-Claim Autoresearch](https://arxiv.org/abs/2610.18088) · Written passage

Origin: `arxiv-unresolved-team` · Version: `9f5a3d8ad0d87cf4b75e0b27ee825183acc71c2811e8bb96e1a59f3c5dca2c35`

Saved evidence: `data/assets/51fd6c05fff2f297f454f717/9f5a3d8ad0d87cf4b75e0b27ee825183acc71c2811e8bb96e1a59f3c5dca2c35/text.txt`

> Train, validation, and test sessions may all be used while optimizing a claim. Every test access must be logged with its purpose, configuration, and result, and test results that informed optimization may not be described as untouched or unbiased estimates.

### 03-c6

inference: Minimal orchestration does not establish low cost: Malena's authors modeled its GLM 5.2 inference cost at $12.12 versus AiScientist's $1.95, while acknowledging that real cache-hit counts were unavailable. Students should measure their own resource use rather than inherit these prices as a complete budget.

[How Much of a Harness Does a Strong Agent Need for Autonomous ML Engineering?](https://arxiv.org/abs/2609.40303) · Written passage

Origin: `research-team-2609.40303` · Version: `6c598d9a3db4f487a0045a147e48bc3e4064e2b81bf388f4ac0947b9d96c78ec`

Saved evidence: `data/assets/7f0901064878a294934bd154/6c598d9a3db4f487a0045a147e48bc3e4064e2b81bf388f4ac0947b9d96c78ec/text.txt`

> At GLM 5.2, Malena’s modeled
> USD cost ($12.12) is \(\approx\)6.2\(\times\) AiScientist’s ($1.95)

[How Much of a Harness Does a Strong Agent Need for Autonomous ML Engineering?](https://arxiv.org/abs/2609.40303) · Written passage

Origin: `research-team-2609.40303` · Version: `6c598d9a3db4f487a0045a147e48bc3e4064e2b81bf388f4ac0947b9d96c78ec`

Saved evidence: `data/assets/7f0901064878a294934bd154/6c598d9a3db4f487a0045a147e48bc3e4064e2b81bf388f4ac0947b9d96c78ec/text.txt`

> none of the harnesses compared
> here report real cache-hit token counts directly

### 03-c7

inference: Watch for evaluations on additional research tasks, evidence-linked claim judgments and transferable held-out improvements. These would make future reports more useful than another unqualified success score, although none alone guarantees replication.

[ResearchFlow-Eval: Tracing the Execution Gap in End-to-End Multi-Claim Autoresearch](https://arxiv.org/abs/2610.18088) · Written passage

Origin: `arxiv-unresolved-team` · Version: `9f5a3d8ad0d87cf4b75e0b27ee825183acc71c2811e8bb96e1a59f3c5dca2c35`

Saved evidence: `data/assets/51fd6c05fff2f297f454f717/9f5a3d8ad0d87cf4b75e0b27ee825183acc71c2811e8bb96e1a59f3c5dca2c35/text.txt`

> For each item it returns an integer rating on a 0–4 scale with item-specific anchors, along with the locations of the supporting evidence and a short rationale.

[ResearchFlow-Eval: Tracing the Execution Gap in End-to-End Multi-Claim Autoresearch](https://arxiv.org/abs/2610.18088) · Written passage

Origin: `arxiv-unresolved-team` · Version: `9f5a3d8ad0d87cf4b75e0b27ee825183acc71c2811e8bb96e1a59f3c5dca2c35`

Saved evidence: `data/assets/51fd6c05fff2f297f454f717/9f5a3d8ad0d87cf4b75e0b27ee825183acc71c2811e8bb96e1a59f3c5dca2c35/text.txt`

> In future work, we will apply ResearchFlow-Eval to additional autoresearch systems, models, and anchor papers.

[My Self Training Claude Code Setup: I Made Claude Code TRAIN ITSELF!](https://www.youtube.com/watch?v=wMQB33rM28I&t=695s) · 695.58–701.74 seconds (s00152)

Origin: `aicodeking` · Version: `91b5117a082251bc859d7cb81ba933c439e1b0450075c2bf98b2b8112bb7d58e`

Saved evidence: `data/assets/youtube-wMQB33rM28I/91b5117a082251bc859d7cb81ba933c439e1b0450075c2bf98b2b8112bb7d58e/text.txt`

> universal coding upgrade. If development improves, but the held-out results stay flat

[My Self Training Claude Code Setup: I Made Claude Code TRAIN ITSELF!](https://www.youtube.com/watch?v=wMQB33rM28I&t=701s) · 701.74–707.58 seconds (s00153)

Origin: `aicodeking` · Version: `91b5117a082251bc859d7cb81ba933c439e1b0450075c2bf98b2b8112bb7d58e`

Saved evidence: `data/assets/youtube-wMQB33rM28I/91b5117a082251bc859d7cb81ba933c439e1b0450075c2bf98b2b8112bb7d58e/text.txt`

> or get worse, we haven't demonstrated a transferable improvement. The search may have fitted the
