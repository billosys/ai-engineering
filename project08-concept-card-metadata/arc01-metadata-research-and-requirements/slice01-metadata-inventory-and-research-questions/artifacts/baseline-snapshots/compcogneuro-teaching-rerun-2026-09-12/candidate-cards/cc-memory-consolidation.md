---
record_type: concept-card
id: cc-memory-consolidation
revision: 3
title: Memory Consolidation
concept_slug: memory_consolidation
aliases: [hippocampus-to-neocortex consolidation, sleep consolidation]
card_status: candidate-requires-operator-review
method_ref: {id: concept-cards, revision: "1.8.1", path: "knowledge/concept-cards/SKILL.md"}
actor: {id: codex, role: extractor, mode: agent-direct}
created_at: 2026-09-12
source_refs: [{id: ccn-book, revision: e0c697b4d4d134f29cb5c2bbde41b1b6b409b63d, path: "/private/tmp/project05-compcogneuro-book-e0c697b4/chapter-07.md"}]
claim_refs: [{id: claim-memory-consolidation-r3, revision: 1, path: "#claim-memory-consolidation-r3"}]
source_support_refs: [{id: support-memory-consolidation-r3, revision: 1, path: "#support-memory-consolidation-r3"}]
cq_refs: [{id: cq-consolidation-caveat, revision: 1, path: "#cq-consolidation-caveat"}]
run_refs: [{id: run-compcogneuro-teaching-rerun-20260912, revision: 1, path: "../README.md"}]
extraction_confidence: {assessment: high-for-selected-span, rationale: "Direct extraction from chapter-07.md lines 115-117.", scope: "memory consolidation subsection"}
verification_state: unassessed
reconciliation_state: unassessed
memory_admission_ref: null
---

# Concept Card: Memory Consolidation

## Concept Boundary

This card covers the source's qualified account of memory consolidation from
hippocampal involvement toward neocortical representation. It excludes claims
that consolidation is universal or that sleep fully explains memory transfer.

## Quick Definition And Core Definition

Quick definition: memory consolidation is a proposed process in which memories
initially dependent on hippocampus become strengthened or represented in
neocortical systems over time.

Core definition: the source treats consolidation as plausible but sharply
qualified. Reactivation and retrograde-gradient evidence suggest consolidation
in at least some cases, while weak signals and contested findings prevent a
universal claim.

## Prerequisites And Key Properties

- Initial hippocampal involvement matters in the account.
- Reactivation during sleep or retrieval may create learning opportunities.
- Neocortical memories may become more semanticized and generalized.
- The source's conclusion is explicitly limited.

## Construction Or Recognition

Recognize consolidation when the explanation involves time-dependent change in
hippocampal and neocortical support, not merely any sleep-memory effect.

## Context And Application

The source uses consolidation to connect episodic memory, sleep/wake
reactivation and complementary learning systems.

## Examples

The source mentions rat-maze activity patterns during wakefulness and sleep,
slow-wave oscillations during non-REM sleep, and induced slow waves improving
later hippocampal-dependent memory.

## Common Errors And Common Confusions

- Overstating consolidation as universal.
- Treating weak reactivation as obviously sufficient for learning.
- Ignoring the semanticization prediction for neocortical memory.

## Source Reference And Support Map

| Body statement | Locator | Support |
| --- | --- | --- |
| Consolidation is motivated by gradients and sleep reactivation. | `chapter-07.md` line 115 | `support-memory-consolidation-r3` |
| The source qualifies consolidation as occurring to some extent in some situations. | `chapter-07.md` line 115 | `support-memory-consolidation-r3` |
| Neocortical encoding may become more semanticized. | `chapter-07.md` line 117 | `support-memory-consolidation-r3` |

## Claims And Evidence

### Claim `claim-memory-consolidation-r3`

The source concludes that memory consolidation likely occurs to some extent in
some situations, while retaining caveats about weak reactivation and contested
retrograde-gradient evidence.

### Support `support-memory-consolidation-r3`

Support is direct from the selected Chapter 7 lines. Bibliography entries and
cited studies were not resolved.

## Relationships And Competency Questions

- Related: complementary learning systems.
- May transform: episodic representations toward semanticized neocortical
  representations.

### CQ `cq-consolidation-caveat`

What qualification does the source attach to consolidation?

Expected answer: it likely occurs to some extent in some situations, but the
evidence remains limited and contested.

## Provenance And Preparation Limits

Line locators use the pinned Markdown checkout. Cited studies and bibliography
entries were not inspected.

## Extraction Notes And Review Boundaries

This card keeps the caveat central in the definition rather than repeating it
through every teaching section.

## Lifecycle And Prior Value

Candidate only; validation, semantic verification, reconciliation, preservation,
operator acceptance and memory admission are unassessed.

## Handoff And Remaining Work

Before admission, inspect the cited studies if consolidation becomes important
for the memory protocol.

