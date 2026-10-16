## 03-c1
AI Code King's procedure changes workflow instructions while leaving the underlying model and grading rules unchanged. Its 'self-training' framing should therefore be understood here as instruction optimization.

My Self Training Claude Code Setup: I Made Claude Code TRAIN ITSELF! — https://www.youtube.com/watch?v=wMQB33rM28I
56.8–61.8 seconds: the changes on tasks it hasn't practiced on. The underlying Claude model stays the same.

My Self Training Claude Code Setup: I Made Claude Code TRAIN ITSELF! — https://www.youtube.com/watch?v=wMQB33rM28I
271.0–276.0 seconds: project. The optimizer can change the workflow instructions. The grading rules stay fixed. That

## 03-c2
The tutorial recommends comparison on tasks excluded from search, followed by human review of the winning instruction changes. Any human-edited version becomes a new candidate requiring evaluation; this is procedural advice, not an observed gain.

My Self Training Claude Code Setup: I Made Claude Code TRAIN ITSELF! — https://www.youtube.com/watch?v=wMQB33rM28I
649.9–653.8 seconds: instructions on the tasks we kept out of the search. Use fresh project copies and fresh

My Self Training Claude Code Setup: I Made Claude Code TRAIN ITSELF! — https://www.youtube.com/watch?v=wMQB33rM28I
809.5–814.1 seconds: Review the winning instruction diff. Remove anything tied to the practice tasks. Then

My Self Training Claude Code Setup: I Made Claude Code TRAIN ITSELF! — https://www.youtube.com/watch?v=wMQB33rM28I
814.1–818.8 seconds: treat that edited version as a new candidate that needs checking. Even a well-intended

## 03-c3
Campus Talks recommends connecting data to provenance, sharing variable descriptions and executed analysis code, and allowing extra planning time. Applying that guidance to agent experiments means budgeting documentation work alongside execution, with sharing limited to what is appropriate and ethical.

Campus Talks: How is AI affecting open research? — https://timeshighered.podbean.com/e/campus-talks-how-is-ai-affecting-open-research/
974.7–977.6 seconds: is that data needs to be connected

Campus Talks: How is AI affecting open research? — https://timeshighered.podbean.com/e/campus-talks-how-is-ai-affecting-open-research/
977.6–980.0 seconds: to the provenance it comes from, yeah.

Campus Talks: How is AI affecting open research? — https://timeshighered.podbean.com/e/campus-talks-how-is-ai-affecting-open-research/
2468.7–2471.9 seconds: You can share descriptions of your variables

Campus Talks: How is AI affecting open research? — https://timeshighered.podbean.com/e/campus-talks-how-is-ai-affecting-open-research/
2473.7–2476.4 seconds: You can share code if you have run a program

Campus Talks: How is AI affecting open research? — https://timeshighered.podbean.com/e/campus-talks-how-is-ai-affecting-open-research/
3276.1–3280.3 seconds: But make sure that you build extra time into your planning.

Campus Talks: How is AI affecting open research? — https://timeshighered.podbean.com/e/campus-talks-how-is-ai-affecting-open-research/
2347.3–2350.5 seconds: make sharing, if it's appropriate and ethical,

## 03-c4
ResearchFlow-Eval's authors report that 14 of 90 end-to-end claims met their criteria, with only one empirical claim met. Their judge received researcher spot-checking, so students should retain human review of AI judgments as a safeguard, without assuming demonstrated judge bias.

ResearchFlow-Eval: Tracing the Execution Gap in End-to-End Multi-Claim Autoresearch — https://arxiv.org/abs/2610.18088
Of the 90 end-to-end claims, 14 are met, and E5 for GPT-6 Astra is the only empirical claim met in an end-to-end run.

ResearchFlow-Eval: Tracing the Execution Gap in End-to-End Multi-Claim Autoresearch — https://arxiv.org/abs/2610.18088
A domain researcher spot-checked the judge’s ratings and rationales and found them largely consistent with their own assessment.

## 03-c5
ResearchFlow-Eval permits optimization using test sessions but requires logging access and forbids describing optimization-informed results as untouched estimates. Students should likewise record when evaluation data influenced selection.

ResearchFlow-Eval: Tracing the Execution Gap in End-to-End Multi-Claim Autoresearch — https://arxiv.org/abs/2610.18088
Train, validation, and test sessions may all be used while optimizing a claim. Every test access must be logged with its purpose, configuration, and result, and test results that informed optimization may not be described as untouched or unbiased estimates.

## 03-c6
Minimal orchestration does not establish low cost: Malena's authors modeled its GLM 5.2 inference cost at $12.12 versus AiScientist's $1.95, while acknowledging that real cache-hit counts were unavailable. Students should measure their own resource use rather than inherit these prices as a complete budget.

How Much of a Harness Does a Strong Agent Need for Autonomous ML Engineering? — https://arxiv.org/abs/2609.40303
At GLM 5.2, Malena’s modeled
USD cost ($12.12) is \(\approx\)6.2\(\times\) AiScientist’s ($1.95)

How Much of a Harness Does a Strong Agent Need for Autonomous ML Engineering? — https://arxiv.org/abs/2609.40303
none of the harnesses compared
here report real cache-hit token counts directly

## 03-c7
Watch for evaluations on additional research tasks, evidence-linked claim judgments and transferable held-out improvements. These would make future reports more useful than another unqualified success score, although none alone guarantees replication.

ResearchFlow-Eval: Tracing the Execution Gap in End-to-End Multi-Claim Autoresearch — https://arxiv.org/abs/2610.18088
For each item it returns an integer rating on a 0–4 scale with item-specific anchors, along with the locations of the supporting evidence and a short rationale.

ResearchFlow-Eval: Tracing the Execution Gap in End-to-End Multi-Claim Autoresearch — https://arxiv.org/abs/2610.18088
In future work, we will apply ResearchFlow-Eval to additional autoresearch systems, models, and anchor papers.

My Self Training Claude Code Setup: I Made Claude Code TRAIN ITSELF! — https://www.youtube.com/watch?v=wMQB33rM28I
695.6–701.7 seconds: universal coding upgrade. If development improves, but the held-out results stay flat

My Self Training Claude Code Setup: I Made Claude Code TRAIN ITSELF! — https://www.youtube.com/watch?v=wMQB33rM28I
701.7–707.6 seconds: or get worse, we haven't demonstrated a transferable improvement. The search may have fitted the