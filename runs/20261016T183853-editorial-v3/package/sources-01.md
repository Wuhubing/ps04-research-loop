## 01-c1
Li and Lu report contact precision increasing from 28.2% to 36.6% at a matched 48.4B-token budget, with a human choosing which recipes to scale. This is a human-guided result.

Hill-Climbing a Protein Language Model: A Taste of Autoresearch for Scientific Discovery — https://jojoml.github.io/blog/2026/nanoproteinlm-agenticls/
Starting from the ESMC recipe, a simple sequential search, with a human deciding which recipes to scale up, gave a recipe with about 30% higher long-range contact precision, from 28.2% to 36.6% P@L, at the same 48.4B-token budget.

## 01-c2
Agora describes agents checking out exact parent commits, changing and evaluating code, and recording results. Its reported run occurred between April 26 and May 8, rather than during this publication window.

Agora: Git as Shared Memory for Collective AutoResearch — https://arxiv.org/abs/2609.18094
pick a parent, fetch and check out that exact commit, make one change,
evaluate, commit everything needed to reproduce

Agora: Git as Shared Memory for Collective AutoResearch — https://arxiv.org/abs/2609.18094
The run lasted 11 days and 19 hours of
server time, from the setup commit on April 26 to our cutoff on May 8

## 01-c3
Agora's authors describe human interventions during the run, selection on one 200-text development evaluator and no fresh author rerun of the winner. Its experiment history therefore does not establish independent validation.

Agora: Git as Shared Memory for Collective AutoResearch — https://arxiv.org/abs/2609.18094
During the
run we changed the server three times and the H100 workers’ prompt once.

Agora: Git as Shared Memory for Collective AutoResearch — https://arxiv.org/abs/2609.18094
Every component was selected on the same 200-text development evaluator.

Agora: Git as Shared Memory for Collective AutoResearch — https://arxiv.org/abs/2609.18094
We did not rerun the winning method; the primary result is the archived
evaluator output, corroborated by the agents’ cross-hardware reproductions.

## 01-c4
Periodic's founders say characterization shifted substantially toward AI assistance while campaign guidance became a mixture of human and AI work. This describes their workflow, not a measured productivity gain.

Synthesis Superintelligence: from Semiconductors to Superconductors — Periodic Labs’ Liam Fedus and Ekin Dogus Cubuk — https://www.latent.space/p/periodic
3864.0–3904.0 seconds: So, I think even just using the guidance of campaigns, in the early days, that was fully human-driven. Now, increasingly, it’s a mix of AI-driven and human-driven. And then Doğuş was saying early on we identified that characterization was a big bottleneck. In the early days, it was human-driven, and the scientists were very much overwhelmed, and the balance has shifted significantly towards AI-driven. And this has allowed the scientists who were previously spending all of their time doing these refinements to now elevate their work to something else. But I think we’re. It’s really sort of a function of time. There’it’s always changing at each of these levels.
Search, Optimization, and Design of Experiments

## 01-c5
The founders explicitly call full autonomy a non-goal and describe commercial deployment of their tools to industry partners. Their account should be read as an interested operational perspective.

Synthesis Superintelligence: from Semiconductors to Superconductors — Periodic Labs’ Liam Fedus and Ekin Dogus Cubuk — https://www.latent.space/p/periodic
3046.0–3099.0 seconds: Yeah. I think maybe one process is, by having a mix of humans and automation, you can identify really quickly what are some of the bottlenecks in the experimental process, and you start alleviating those bottlenecks one at a time. And so for example, if there’s some really tricky dexterity task that humans are excellent at but you’d have to spend months automating machine, maybe don’t spend a ton of time there. And maybe a more promising thing is something very routine that takes up a huge amount of scientists’ and technicians’ time, and it’s easy to automate. So I think it’there’s this pragmatism to it. But ultimately what we want from the lab is a huge quantity of data, high-quality data, diverse data, and those are our goals. And full autonomy is a non-goal. It’s sort of in the service that we use automation in the service of achieving the goals on the data.

Synthesis Superintelligence: from Semiconductors to Superconductors — Periodic Labs’ Liam Fedus and Ekin Dogus Cubuk — https://www.latent.space/p/periodic
4506.0–4613.0 seconds: For ourselves. So we’ve been customer zero. Now what we’re doing is we’re taking these same tools to different industries, and we’we have a huge focus right now in the semiconductor industry. However, in order to do this these are very, private companies. We need to be able to operate within some of the most secure environments. And so our Periodic forward-deployed engineers and researchers will actually be on site working and actually integrating our AI systems, our computational systems to help our partners get to their goal states more quickly. So basically the tools, the know-how that we’ve built in doing our own materials discovery, materials engineering, we’re now bringing to industry. And we think this is the most effective way to get partners to their end states and to their goals, rather than just throwing some technology over the wall and telling them to figure it out. Then these forward-deployed engineers will also do the inference locally, but then also can, train on the data. So again, once we take our system that understands these different areas and we deploy, we can make it expert on the customers or the partners’ data so that they can own their own intelligence and have systems that understand this much more effectively than just hitting some API or some untrained model. And so this is a much expanded, forward-deployment engineering role than typical because this really requires some very deep, machine learning expertise. You have to be incredibly precise from a data training perspective, infrastructure perspective, but also a physics perspective. So we’re working with highly technical industries. They have to understand, different areas of chemistry, material science, some of the devices. And so that, those are the roles we’re building out right now.

## 01-c6
A practical delegation boundary is to let an agent execute bounded changes and preserve failed attempts, while the student fixes the scientific objective and decides which candidates deserve larger validation runs.

Hill-Climbing a Protein Language Model: A Taste of Autoresearch for Scientific Discovery — https://jojoml.github.io/blog/2026/nanoproteinlm-agenticls/
The scientific outcome the campaign should improve, fixed before search.

Hill-Climbing a Protein Language Model: A Taste of Autoresearch for Scientific Discovery — https://jojoml.github.io/blog/2026/nanoproteinlm-agenticls/
A larger-budget retraining of the selected recipe against the baseline, testing whether search-time gains carry over.

Agora: Git as Shared Memory for Collective AutoResearch — https://arxiv.org/abs/2609.18094
The graph also records what did not work, and later workers cited these records when choosing directions.