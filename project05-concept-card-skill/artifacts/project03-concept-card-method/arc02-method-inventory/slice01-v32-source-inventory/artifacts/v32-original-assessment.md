# v3.2 Original Assessment

Source: assistant assessment from rollout
`/Users/oubiwann/.codex/sessions/2026/08/30/rollout-2026-08-30T00-37-26-01a0512c-3454-7e33-b0d7-2bbe781903e9.jsonl`,
assistant message at JSONL line 148.

Corroboration: the operator supplied screenshots of the same assessment in the
current Project03 planning session. Those screenshots are treated as evidence
for preservation, not as process instructions.

Preservation note: this memo preserves the original assessment made before
Project03 was opened. The preserved text uses the then-current phrase `v3.3`;
later operator direction changed the target to v4.0. Project03 treats that
recommendation as applying to v4.0 while preserving the original wording below.

The response footer memory citation from the original assistant message is
omitted here because it was execution metadata, not part of the concept-card
method assessment.

## Preserved Assessment

**Verdict**

v3.2 is genuinely good. Not "good for an old prompt," but good as a
knowledge-engineering method: it has atomicity, source fidelity, provenance,
authority control, typed relationships, competency questions, re-extraction
rules, preservation checks, and validation. The core shape still stands.

Where it now feels underpowered is not ontology theory so much as modern LLM
operations. The docs assume the LLM is mainly a careful extractor. Today I'd
treat extraction as one stage in a provenance-bearing cognitive pipeline:
generate candidate cards, validate structure, reconcile graph edges, grade
evidence, sample-audit semantic fidelity, and only then admit cards into
durable memory.

**What Still Holds**

The strongest parts are the golden rules in
[`0009-howto-concept-card-extraction-with-llms-v3.2.md`](/Users/oubiwann/lab/billosys/ai-engineering/workbench/0009-howto-concept-card-extraction-with-llms-v3.2.md:36):
one concept per card, source-faithful synthesis, explicit relationships,
confidence, and sacred provenance. That is a very healthy substrate design.

The competency-question layer is also a major win. It ties cards to use, not
just description. That aligns with classic ontology engineering, where
competency questions are both requirements and evaluation criteria, and it also
aligns with newer work using language models to support CQ generation and
ontology/KG documentation, such as RevOnt's 2024 work on extracting CQs from
knowledge graphs ([ScienceDirect](https://doi.org/10.1016/J.WEBSEM.2024.100822)).

The re-extraction discipline in
[`0009`](/Users/oubiwann/lab/billosys/ai-engineering/workbench/0009-howto-concept-card-extraction-with-llms-v3.2.md:585)
is especially mature: source primary, old card secondary, v3 template target,
preserve unique value. That is exactly the right anti-amnesia posture.

**What Needs Updating**

The confidence field is too flat now. `high/medium/low` is useful, but it
mixes several dimensions: source explicitness, extractor certainty,
verification status, and downstream usability. CCDP gives us a better
vocabulary: a card could carry `ASSERTED`, `HEURISTIC`, `VALIDATED`,
`CROSS_CHECKED`, or `HUMAN_ATTESTED` style evidence grades, while still
separately recording extraction confidence.

Parallel extraction needs a reconciliation phase.
[`0010`](/Users/oubiwann/lab/billosys/ai-engineering/workbench/0010-a-guide-for-parallel-concept-card-re-extraction-v3.2.md:311)
balances work across five agents, but the method needs an explicit merge
authority that checks duplicate concepts, inconsistent slugs, relationship
asymmetry, taxonomy drift, and competing definitions across agents.

Validation is too shell-grep-shaped. The checks in
[`0010`](/Users/oubiwann/lab/billosys/ai-engineering/workbench/0010-a-guide-for-parallel-concept-card-re-extraction-v3.2.md:625)
are useful, but v3.3 should move toward schema validation plus semantic QA:
YAML schema, required sections, enum checks, slug graph closure, bidirectional
relationship rules where applicable, CQ coverage reports, and source-span spot
checks.

The cards are graph-ready, but not yet graph-native. Modern GraphRAG work shows
why this matters: GraphRAG builds graph indexes and community summaries for
global corpus questions ([arXiv:2404.16130](https://arxiv.org/abs/2404.16130));
LightRAG combines graph structures with vector representations and incremental
updates ([arXiv:2410.05779](https://arxiv.org/abs/2410.05779)); HippoRAG uses
KG plus Personalized PageRank for associative retrieval
([arXiv:2405.14831](https://arxiv.org/abs/2405.14831)), with HippoRAG 2
explicitly framed as non-parametric continual learning/memory
([arXiv:2502.14802](https://arxiv.org/abs/2502.14802)). Your method already
contains the hand-built version of that direction.

**CCDP Fit**

The "right spot" feels like this: concept-card extraction is not CCDP itself;
it is a high-value cognitive service behind CCDP.

A CCDP dispatcher would route `extract-concepts`, `validate-card`,
`reconcile-ontology`, `audit-provenance`, and `memory-admission` capabilities.
The card itself becomes durable content with provenance evidence. CCDP's
distinction that cognitive outputs are claims, not data, maps perfectly onto
concept cards: an extracted card should not enter memory as "truth"; it enters
as a claim with evidence, source spans, extraction trace, validation status,
and audit history. That mirrors the CCDP spec's provenance-grade posture in
[`the protocol`](/Users/oubiwann/lab/billosys/ai-engineering/protocols/ccdp/composite-cognition-dispatch-protocol.md:146).

**Memory Fit**

For LLM memory augmentation, this is closer to "semantic consolidation" than
ordinary retrieval. Raw notes are episodic memory. Concept cards are
consolidated semantic memory. Skill files are procedural memory or policy
memory: distilled guidance ready for action.

That is why I like this effort so much: it sits between reading and cognition.
MemGPT-style systems manage memory tiers and context movement
([arXiv:2310.08560](https://arxiv.org/abs/2310.08560)); generative-agent
architectures store experiences, reflect, and retrieve memories for planning
([arXiv:2304.03442](https://arxiv.org/abs/2304.03442)). Your cards answer a
slightly different question: what must be true of a memory before we let future
cognition lean on it?

My short version: v3.2 is a strong knowledge-substrate method. v3.3 should
become an evidence-graded, schema-validated, graph-reconciled
memory-consolidation protocol. That would make it fit naturally under both the
ai-engineering substrate pillar and CCDP's claim/provenance/audit worldview.
