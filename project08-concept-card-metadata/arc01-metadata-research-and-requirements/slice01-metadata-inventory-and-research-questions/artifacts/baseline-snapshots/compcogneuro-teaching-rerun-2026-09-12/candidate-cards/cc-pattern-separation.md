---
record_type: concept-card
id: cc-pattern-separation
revision: 3
title: Pattern Separation
concept_slug: pattern_separation
aliases: [sparse representations, low-overlap encoding]
card_status: candidate-requires-operator-review
method_ref: {id: concept-cards, revision: "1.8.1", path: "knowledge/concept-cards/SKILL.md"}
actor: {id: codex, role: extractor, mode: agent-direct}
created_at: 2026-09-12
source_refs: [{id: ccn-book, revision: e0c697b4d4d134f29cb5c2bbde41b1b6b409b63d, path: "/private/tmp/project05-compcogneuro-book-e0c697b4/chapter-07.md"}]
claim_refs: [{id: claim-pattern-separation-r3, revision: 1, path: "#claim-pattern-separation-r3"}]
source_support_refs: [{id: support-pattern-separation-r3, revision: 1, path: "#support-pattern-separation-r3"}]
cq_refs: [{id: cq-pattern-separation-interference, revision: 1, path: "#cq-pattern-separation-interference"}]
run_refs: [{id: run-compcogneuro-teaching-rerun-20260912, revision: 1, path: "../README.md"}]
extraction_confidence: {assessment: high-for-selected-span, rationale: "Direct extraction from chapter-07.md lines 49 and 67-75.", scope: "pattern separation passage"}
verification_state: unassessed
reconciliation_state: unassessed
memory_admission_ref: null
---

# Concept Card: Pattern Separation

## Concept Boundary

This card covers sparse, low-overlap encoding as the source's explanation for
reduced interference among episodes. It excludes pattern completion except for
the tradeoff between separation and completion.

## Quick Definition And Core Definition

Quick definition: pattern separation makes similar experiences use less
overlapping neural representations so they interfere less.

Core definition: the source describes hippocampal CA fields as firing less
often and more selectively than cortical input areas. Because fewer neurons are
active for each episode, two episodes are less likely to share the same pattern.

## Prerequisites And Key Properties

- Sparse activity: relatively few neurons fire for an episode.
- Low overlap: different events activate fewer shared units.
- Interference reduction: new episodes are less likely to overwrite older ones.
- Tradeoff: too much separation can make cue-driven completion harder.

## Construction Or Recognition

Recognize pattern separation when the explanation ties sparse representation to
lower interference, not merely when it mentions hippocampus or memory.

## Context And Application

Pattern separation supports rapid episodic encoding inside the source's
complementary-learning-systems account.

## Examples

The source's probability example contrasts low activation, such as 1%, with
higher activation, such as 25%: the lower activation case has much less random
overlap between two episodes.

## Common Errors And Common Confusions

- Confusing sparse activity with weak memory.
- Treating separation as all of recall; completion is also needed.
- Treating cited figures or studies as independently verified by this run.

## Source Reference And Support Map

| Body statement | Locator | Support |
| --- | --- | --- |
| Hippocampus uses sparse representations to reduce overlap and interference. | `chapter-07.md` line 49 | `support-pattern-separation-r3` |
| CA fields fire less often than cortex; sparse activity reduces overlap. | `chapter-07.md` line 67 | `support-pattern-separation-r3` |
| Pattern separation supports rapid encoding with minimal interference. | `chapter-07.md` line 75 | `support-pattern-separation-r3` |

## Claims And Evidence

### Claim `claim-pattern-separation-r3`

The source reports that sparse hippocampal representations support rapid
episodic encoding by reducing overlap and therefore interference.

### Support `support-pattern-separation-r3`

Support is direct from the selected Chapter 7 text. Figures and cited studies
remain contextual but unverified in this run.

## Relationships And Competency Questions

- Enables: episodic binding.
- Trades off with: pattern completion.
- Supports: complementary learning systems.

### CQ `cq-pattern-separation-interference`

Why does sparse hippocampal activation reduce interference?

Expected answer: fewer active neurons make different episode patterns less
likely to overlap.

## Provenance And Preparation Limits

Line locators use the pinned Markdown checkout. Figures and cited literature
were not independently reviewed.

## Extraction Notes And Review Boundaries

This card intentionally keeps the numerical example in the teaching body and
the figure/study caveats in review sections.

## Lifecycle And Prior Value

Candidate only; validation, semantic verification, reconciliation, preservation,
operator acceptance and memory admission are unassessed.

## Handoff And Remaining Work

Before full admission, decide whether sparseness, conjunctive representation
and interference should remain together or split.

