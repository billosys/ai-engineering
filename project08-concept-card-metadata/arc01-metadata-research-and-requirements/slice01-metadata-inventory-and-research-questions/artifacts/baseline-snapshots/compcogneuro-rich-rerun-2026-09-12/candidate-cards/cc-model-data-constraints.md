---
record_type: concept-card
id: cc-model-data-constraints
revision: 2
title: Data-Constrained Computational Models
concept_slug: model_data_constraints
aliases: [model constraint, empirical model constraint]
card_status: candidate-requires-operator-review
method_ref: {id: concept-cards, revision: "1.8.0", path: "knowledge/concept-cards/SKILL.md"}
actor: {id: codex, role: extractor, mode: agent-direct}
created_at: 2026-09-12
source_refs: [{id: ccn-book, revision: e0c697b4d4d134f29cb5c2bbde41b1b6b409b63d, path: "/private/tmp/project05-compcogneuro-book-e0c697b4/chapter-01.md"}]
prepared_source_refs: []
claim_refs: [{id: claim-model-data-constraints-r2, revision: 1, path: "#claim-model-data-constraints-r2"}]
source_support_refs: [{id: support-model-data-constraints-r2, revision: 1, path: "#support-model-data-constraints-r2"}]
relationship_refs: []
cq_refs: [{id: cq-model-constraint-trust, revision: 1, path: "#cq-model-constraint-trust"}]
run_refs: [{id: run-compcogneuro-rich-rerun-20260912, revision: 1, path: "../README.md"}]
extraction_confidence: {assessment: high-for-selected-span, rationale: "Direct extraction from chapter-01.md lines 37-45; no external modeling literature inspected.", scope: "selected Chapter 1 methodological passage"}
validation_refs: []
verification_state: unassessed
verification_refs: []
reconciliation_state: unassessed
reconciliation_refs: []
preservation_refs: []
memory_admission_ref: null
---

# Concept Card: Data-Constrained Computational Models

## Concept Boundary

This card covers the source's criterion for making computational models
scientifically accountable: a model should be constrained by data at as many
levels as possible and should generate testable predictions. It excludes
claims that a constrained model is true, that unconstrained models are useless,
or that any particular model in the book has already met this standard.

## Quick Definition And Core Definition

Quick definition: a data-constrained computational model is a model whose
trustworthiness depends on empirical constraints and testable predictions.

Core definition: in the source's account, distrust of complex human-made models
is answered not by making them maximally detailed, but by tying them to data
from multiple levels and exposing their predictions to empirical testing. The
source also qualifies the modeling target: the goal is a middle ground that
captures important cognitive phenomena while simplifying neural detail enough
to support understanding.

## Prerequisites And Key Properties

- The model is complex enough to need empirical constraint rather than mere
  verbal plausibility.
- Constraint should come from multiple levels where possible, not a single
  favored data source.
- Prediction and empirical testing are part of the model's accountability.
- Simplicity remains a competing value: the source favors the simplest model
  that captures the most relevant data.

## Construction Or Recognition

Recognize the concept when a modeling claim answers "why trust this model?" by
pointing to inspected data constraints and testable predictions. Do not count a
model as data-constrained merely because it is computational, biologically
detailed, or rhetorically plausible.

## Context And Application

The concept appears in the textbook's Chapter 1 methodological framing. It is
used to justify computational cognitive neuroscience as a way to study complex
brain-cognition relations without either hand-waving verbally or attempting an
unreadably complete replica of the brain.

## Examples

The selected source gives an example class rather than a named model: a useful
model may simplify neurons and networks while still capturing cognitive
phenomena and making predictions about neural-level changes such as disease,
pharmacology, genetics, or task parameters. No specific downstream model was
inspected in this run.

## Common Errors And Common Confusions

- Confusing "computational" with "empirically constrained." The source treats
  modeling as accountable only when tied to data and predictions.
- Confusing maximal biological detail with understanding. The source warns
  that a perfectly detailed replica could remain as incomprehensible as the
  brain itself.
- Treating simplification as a defect by itself. The source frames
  simplification as necessary when it preserves the important data.

## Source Reference And Support Map

| Assertion | Locator | Support Scope |
| --- | --- | --- |
| Models should be constrained by data and testable predictions. | `chapter-01.md` lines 37-37 | Direct source statement. |
| The preferred modeling level balances neural simplification and cognitive functionality. | `chapter-01.md` lines 41-45 | Direct source statement with qualifications. |
| A model can make neural-level predictions about cognitive phenomena. | `chapter-01.md` line 45 | Direct source statement; examples are source examples, not verified cases. |

## Claims And Evidence

### Claim `claim-model-data-constraints-r2`

The source presents multi-level data constraints and empirically testable
predictions as the main answer to distrust of complex computational models.

### Support `support-model-data-constraints-r2`

The support is direct for the source's methodological claim in
`chapter-01.md` line 37, with contextual qualifications from lines 39-45. The
run did not inspect external scientific-methods literature or any model's
actual empirical record.

## Relationships And Competency Questions

- Prerequisite candidate: understanding the source's "computational approach"
  helps interpret later model-specific claims.
- Related candidate: emergence, because the same chapter later describes
  reconstruction of complex phenomena from simpler mechanisms.

### CQ `cq-model-constraint-trust`

What must a computational cognitive neuroscience model show, in the source's
account, before its predictions deserve trust?

Expected answer scope: it must be constrained by data at multiple levels and
generate predictions that can be tested empirically.

## Provenance And Preparation Limits

The source was already Markdown. No document-extraction repair was performed.
Line locators are one-based line numbers from the pinned local checkout. No
external citations, figures, or downstream chapters were resolved for this
card.

## Extraction Notes And Review Boundaries

This is a richer revision of the Arc07 candidate for the same concept. It adds
recognition cues, examples, confusions, and a CQ while preserving the original
boundary that this is a methodological claim, not proof that any model is true.
It has not been independently semantically verified.

## Lifecycle And Prior Value

The Arc07 revision remains prior value. This revision is candidate material
only: no operator acceptance, reconciliation, preservation decision, or memory
admission has been performed.

## Handoff And Remaining Work

An operator should decide whether this concept is useful for the memory-protocol
corpus and whether the middle-ground modeling passage belongs in this same card
or in a separate "golden middle" modeling-strategy card.
