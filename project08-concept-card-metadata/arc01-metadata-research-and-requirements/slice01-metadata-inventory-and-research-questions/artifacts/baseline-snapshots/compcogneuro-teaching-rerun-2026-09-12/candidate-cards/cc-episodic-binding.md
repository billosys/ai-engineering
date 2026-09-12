---
record_type: concept-card
id: cc-episodic-binding
revision: 3
title: Episodic Binding
concept_slug: episodic_binding
aliases: [hippocampal binding, conjunctive episodic representation]
card_status: candidate-requires-operator-review
method_ref: {id: concept-cards, revision: "1.8.1", path: "knowledge/concept-cards/SKILL.md"}
actor: {id: codex, role: extractor, mode: agent-direct}
created_at: 2026-09-12
source_refs: [{id: ccn-book, revision: e0c697b4d4d134f29cb5c2bbde41b1b6b409b63d, path: "/private/tmp/project05-compcogneuro-book-e0c697b4/chapter-07.md"}]
claim_refs: [{id: claim-episodic-binding-r3, revision: 1, path: "#claim-episodic-binding-r3"}]
source_support_refs: [{id: support-episodic-binding-r3, revision: 1, path: "#support-episodic-binding-r3"}]
cq_refs: [{id: cq-episodic-binding-conjunction, revision: 1, path: "#cq-episodic-binding-conjunction"}]
run_refs: [{id: run-compcogneuro-teaching-rerun-20260912, revision: 1, path: "../README.md"}]
extraction_confidence: {assessment: high-for-selected-span, rationale: "Direct extraction from chapter-07.md lines 49-65.", scope: "hippocampal episodic binding passage"}
verification_state: unassessed
reconciliation_state: unassessed
memory_admission_ref: null
---

# Concept Card: Episodic Binding

## Concept Boundary

This card covers the source's account of hippocampal binding of event features
into episode representations. It excludes full hippocampal anatomy and recall
mechanisms except where they clarify binding.

## Quick Definition And Core Definition

Quick definition: episodic binding combines features of an experience into a
recoverable representation of an event.

Core definition: the source describes hippocampal pathways as receiving inputs
from many cortical areas and forming conjunctive representations. Binding lets
distributed features such as object, place and context participate in one
episodic memory.

## Prerequisites And Key Properties

- Inputs arrive from distributed cortical representations.
- Binding creates conjunctive episode-level representations.
- Sparse hippocampal activity helps reduce overlap among episodes.
- Binding supports later recall only in conjunction with completion mechanisms.

## Construction Or Recognition

Recognize episodic binding when a source explains how separately represented
features become connected as one remembered event.

## Context And Application

The source uses binding to motivate hippocampal specialization for episodic
memory: the system can rapidly encode a coherent event without treating each
feature as a separate memory.

## Examples

A parking memory binds location, occasion and contextual details into one
episode rather than storing each cue independently.

## Common Errors And Common Confusions

- Treating binding as a passive list of features rather than a conjunctive
  representation.
- Treating binding alone as recall; recall also needs cue-driven completion.
- Treating hippocampus as an isolated module; the source emphasizes cortical
  inputs and interactions.

## Source Reference And Support Map

| Body statement | Locator | Support |
| --- | --- | --- |
| Hippocampus supports sparse, conjunctive episodic representations. | `chapter-07.md` lines 49-65 | `support-episodic-binding-r3` |
| Cortical input pathways help form bound episode representations. | `chapter-07.md` lines 53-65 | `support-episodic-binding-r3` |

## Claims And Evidence

### Claim `claim-episodic-binding-r3`

The source presents hippocampal episodic binding as forming sparse conjunctive
representations from distributed inputs.

### Support `support-episodic-binding-r3`

Support is direct from the selected Chapter 7 hippocampal-pathway passage.

## Relationships And Competency Questions

- Supported by: pattern separation.
- Paired with: pattern completion.

### CQ `cq-episodic-binding-conjunction`

Why does episodic memory need conjunctive representation?

Expected answer: because an episode combines multiple distributed features into
one event representation.

## Provenance And Preparation Limits

Line locators use the pinned Markdown checkout. Anatomy figures were not
independently audited.

## Extraction Notes And Review Boundaries

This revision keeps anatomy detail minimal and foregrounds the usable concept.

## Lifecycle And Prior Value

Candidate only; validation, semantic verification, reconciliation, preservation,
operator acceptance and memory admission are unassessed.

## Handoff And Remaining Work

Check later chapter coverage before deciding whether binding, sparse coding and
conjunctive representation should split into separate admitted cards.

