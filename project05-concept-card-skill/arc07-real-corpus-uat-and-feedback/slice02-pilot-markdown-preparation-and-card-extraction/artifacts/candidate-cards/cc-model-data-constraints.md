---
record_type: concept-card
id: cc-model-data-constraints
revision: 1
title: Data-constrained computational models
concept_slug: model_data_constraints
aliases: [model constraint]
card_status: candidate-requires-operator-review
method_ref: {id: concept-cards, revision: "1.7.4", path: "../../../../../../../knowledge/concept-cards/SKILL.md"}
actor: {id: codex-cc, role: extractor, mode: agent-direct}
created_at: 2026-09-11
source_refs: [{id: ccn-book, revision: e0c697b4, path: "../source-acquisition.md"}]
prepared_source_refs: [{id: ps-ccn-book-pilot-20260911, revision: 1, path: "../prepared-source-manifest.md"}]
claim_refs: [{id: claim-model-data-constraints, revision: 1, path: "#claim-model-data-constraints"}]
relationship_refs: []
cq_refs: []
run_refs: [{id: run-arc07-s02-pilot, revision: 1, path: "../extraction-run.md"}]
extraction_confidence: {assessment: high-for-selected-span, rationale: "Direct Markdown inspection of one bounded section with stable line locator.", scope: "claim-model-data-constraints"}
validation_refs: []
verification_state: unassessed
verification_refs: []
reconciliation_state: unassessed
reconciliation_refs: []
preservation_refs: []
memory_admission_ref: null
---

# Concept Card: Data-Constrained Computational Models

## Concept Boundary And Summary

This candidate concerns the textbook's methodological condition for trusting a
computational model: constrain it with data at multiple levels and test its
predictions empirically. It excludes a claim that any particular model is true
or that this methodological condition guarantees truth.

## Claims And Evidence

### Claim `claim-model-data-constraints`

The source presents multi-level data constraints and empirically testable
predictions as the answer to distrust of complex, human-made models.

Support: [support-model-data-constraints.md](./support-model-data-constraints.md).

## Relationships And Competency Questions

No relationship edge or competency question is asserted in this pilot. A later
review could ask what distinguishes a source-constrained model from an
unconstrained model, but this candidate does not claim coverage or answerability.

## Provenance And Preparation Limits

The claim was extracted from `chapter-01.md`, lines 37-45, in the pinned
snapshot. The source's general discussion is the only inspected support. No
external scientific-methods literature or downstream chapters were reviewed.

## Lifecycle And Prior Value

Evidence grade and extraction confidence are separate in the support record.
Validation, verification, reconciliation, preservation, and memory admission
are unassessed. This candidate is not operator-accepted or admitted memory.

## Handoff And Remaining Work

An operator should compare the paraphrase to the full selected span, decide
whether its boundary is useful, and either accept, revise, reject, or leave it
unresolved before any downstream use.
