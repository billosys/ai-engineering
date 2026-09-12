---
record_type: concept-card
id: cc-memory-forms
revision: 2
title: Memory Forms: Weight-Based And Activation-Based
concept_slug: memory_forms_weight_activation
aliases: [weight-based memory, activation-based memory]
card_status: candidate-requires-operator-review
method_ref: {id: concept-cards, revision: "1.8.0", path: "knowledge/concept-cards/SKILL.md"}
actor: {id: codex, role: extractor, mode: agent-direct}
created_at: 2026-09-12
source_refs: [{id: ccn-book, revision: e0c697b4d4d134f29cb5c2bbde41b1b6b409b63d, path: "/private/tmp/project05-compcogneuro-book-e0c697b4/chapter-07.md"}]
claim_refs: [{id: claim-memory-forms-r2, revision: 1, path: "#claim-memory-forms-r2"}]
source_support_refs: [{id: support-memory-forms-r2, revision: 1, path: "#support-memory-forms-r2"}]
cq_refs: [{id: cq-weight-vs-activation-memory, revision: 1, path: "#cq-weight-vs-activation-memory"}]
run_refs: [{id: run-compcogneuro-rich-rerun-20260912, revision: 1, path: "../README.md"}]
extraction_confidence: {assessment: high-for-selected-span, rationale: "Direct extraction from chapter-07.md line 9.", scope: "Chapter 7 opening memory taxonomy"}
verification_state: unassessed
reconciliation_state: unassessed
memory_admission_ref: null
---

# Concept Card: Memory Forms: Weight-Based And Activation-Based

## Concept Boundary

This card covers the source's broad computational division between
weight-based memory and activation-based memory. It excludes working memory,
recognition, priming details, and episodic-memory mechanisms except where they
depend on this broad distinction.

## Quick Definition And Core Definition

Quick definition: weight-based memory depends on synaptic plasticity, while
activation-based memory depends on ongoing neural activity.

Core definition: the source distinguishes durable memory stored through changed
synaptic weights from more transient, flexible memory sustained by continuing
activation. This distinction frames the memory chapter before the source turns
to episodic memory, recognition, priming, and later working-memory material.

## Prerequisites And Key Properties

- Weight-based memory is associated with synaptic plasticity.
- Activation-based memory is associated with ongoing neural activity.
- Weight-based memory is generally longer lasting.
- Activation-based memory is more transient and flexible.
- The source treats both as mechanistic memory forms, not merely psychological
  categories.

## Construction Or Recognition

Recognize the concept when a memory phenomenon is classified by its mechanism:
changed synaptic weights versus current activation state. Do not use this card
to decide whether a particular task is episodic, semantic, recognition, or
priming without additional source support.

## Context And Application

The distinction appears at the beginning of Chapter 7. It frames the chapter's
later discussion of episodic memory, familiarity-based recognition,
weight-based priming, activation-based priming, and working memory in a later
chapter.

## Examples

The selected line names no worked example, but it places the chapter's later
topics under the distinction. Priming is later split into weight-based and
activation-based forms at lines 153-155.

## Common Errors And Common Confusions

- Confusing the broad mechanism distinction with a full taxonomy of all memory
  types.
- Treating activation-based memory as unimportant because it is transient; the
  source also calls it flexible.
- Treating weight-based memory as a single psychological category; the source
  says it can manifest in innumerable ways because modifiable synapses occur
  throughout the brain.

## Source Reference And Support Map

| Assertion | Locator | Support Scope |
| --- | --- | --- |
| Weight-based memory results from synaptic plasticity and is generally longer lasting. | `chapter-07.md` line 9 | Direct source statement. |
| Activation-based memory depends on ongoing neural activity and is more transient and flexible. | `chapter-07.md` line 9 | Direct source statement. |
| Working memory is outside this selected card. | `chapter-07.md` line 9 | Source cross-reference to Executive Function chapter. |

## Claims And Evidence

### Claim `claim-memory-forms-r2`

The source distinguishes weight-based memory from activation-based memory by
mechanism and persistence: synaptic-plasticity memory tends to last longer,
whereas ongoing-activation memory is transient and flexible.

### Support `support-memory-forms-r2`

Support is direct from `chapter-07.md` line 9. The run did not inspect the
Executive Function chapter, so working memory remains out of scope.

## Relationships And Competency Questions

- Parent framing for priming forms.
- Context for complementary learning systems and consolidation, but not an
  asserted edge warranting a graph relation in this run.

### CQ `cq-weight-vs-activation-memory`

How does the source distinguish weight-based from activation-based memory?

Expected answer scope: by synaptic plasticity versus ongoing neural activity,
with different persistence and flexibility.

## Provenance And Preparation Limits

Line locator uses the pinned Markdown checkout. No figure, citation, or
bibliography dependency is required for the selected claim.

## Extraction Notes And Review Boundaries

This revision preserves the Arc07 boundary but expands the card into the rich
profile. It does not attempt a complete memory taxonomy.

## Lifecycle And Prior Value

Prior Arc07 content is preserved as a simpler candidate. This revision is not
verified, reconciled, accepted, preserved, admitted to memory, or runtime
ingested.

## Handoff And Remaining Work

Operator review should decide whether this concept is too broad for a card or
whether it is useful as a top-level navigation node for the Chapter 7 subset.
