---
record_type: concept-card
id: cc-model-data-constraints
revision: 3
title: Model Data Constraints
concept_slug: model_data_constraints
aliases: [golden middle, modeling constraints]
card_status: candidate-requires-operator-review
method_ref: {id: concept-cards, revision: "1.8.1", path: "knowledge/concept-cards/SKILL.md"}
actor: {id: codex, role: extractor, mode: agent-direct}
created_at: 2026-09-12
source_refs: [{id: ccn-book, revision: e0c697b4d4d134f29cb5c2bbde41b1b6b409b63d, path: "/private/tmp/project05-compcogneuro-book-e0c697b4/chapter-01.md"}]
claim_refs: [{id: claim-model-data-constraints-r3, revision: 1, path: "#claim-model-data-constraints-r3"}]
source_support_refs: [{id: support-model-data-constraints-r3, revision: 1, path: "#support-model-data-constraints-r3"}]
cq_refs: [{id: cq-model-data-constraint, revision: 1, path: "#cq-model-data-constraint"}]
run_refs: [{id: run-compcogneuro-teaching-rerun-20260912, revision: 1, path: "../README.md"}]
extraction_confidence: {assessment: high-for-selected-span, rationale: "Direct extraction from chapter-01.md lines 39-44.", scope: "selected Chapter 1 principles passage"}
verification_state: unassessed
reconciliation_state: unassessed
memory_admission_ref: null
---

# Concept Card: Model Data Constraints

## Concept Boundary

This card covers the source's claim that cognitive models should be constrained
by empirical data. It excludes a general philosophy of science account and any
evaluation of specific model implementations.

## Quick Definition And Core Definition

Quick definition: model data constraints are the behavioral and neural evidence
that keep cognitive models from becoming unconstrained stories.

Core definition: the source argues for a "golden middle" in which models are
neither so simple that they ignore important data nor so overfit that they lose
generality. Data constrain what a model may claim to explain.

## Prerequisites And Key Properties

- Models are simplified explanations, not copies of the full brain.
- Empirical fit matters, but fit to one dataset is not enough.
- Useful models balance explanatory power, generality and constraint.

## Construction Or Recognition

Recognize the concept when a modeling discussion asks whether the model is
anchored in observed behavior or neural evidence, and whether it still
generalizes beyond the evidence used to build it.

## Context And Application

The source introduces this principle early as part of its modeling philosophy:
cognitive neuroscience should use models to connect mechanisms with data while
avoiding both empty abstraction and narrow curve-fitting.

## Examples

The source's "golden middle" discussion is the core example: a model should be
specific enough to confront data but not so tailored that it merely restates the
observations it was built from.

## Common Errors And Common Confusions

- Treating any data fit as understanding: fitting data can still leave the
  mechanism obscure.
- Treating simplicity as automatically better: a too-simple model may ignore
  crucial constraints.
- Treating a model as a full brain replica: the source frames models as
  selective explanations.

## Source Reference And Support Map

| Body statement | Locator | Support |
| --- | --- | --- |
| Models should balance simplicity, fit and generality. | `chapter-01.md` lines 39-44 | `support-model-data-constraints-r3` |
| The source uses a "golden middle" framing. | `chapter-01.md` line 43 | `support-model-data-constraints-r3` |

## Claims And Evidence

### Claim `claim-model-data-constraints-r3`

The source presents empirical constraint as necessary for useful cognitive
models while warning against both underconstrained simplicity and overfit detail.

### Support `support-model-data-constraints-r3`

Support is direct from the selected Chapter 1 modeling-principles passage.

## Relationships And Competency Questions

- Related: emergent explanation.
- Contrasts with: unconstrained verbal explanation and narrow curve-fitting.

### CQ `cq-model-data-constraint`

What makes a cognitive model constrained rather than merely plausible?

Expected answer: it must be answerable to empirical data while preserving
generality beyond the fitted case.

## Provenance And Preparation Limits

Line locators use the pinned Markdown checkout. No full-book modeling-method
survey or external modeling literature review was performed.

## Extraction Notes And Review Boundaries

This teaching-profile revision condenses the previous candidate while retaining
the source-specific "golden middle" warrant.

## Lifecycle And Prior Value

Candidate only; validation, semantic verification, reconciliation, preservation,
operator acceptance and memory admission are unassessed.

## Handoff And Remaining Work

Before admission, compare the Chapter 1 passage with later modeling examples to
see whether this should remain one card or become a broader modeling-principle
cluster.

