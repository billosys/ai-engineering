---
record_type: concept-card
id: cc-episodic-binding
revision: 2
title: Hippocampal Episodic Binding
concept_slug: hippocampal_episodic_binding
aliases: [conjunctive memory, hippocampal binding]
card_status: candidate-requires-operator-review
method_ref: {id: concept-cards, revision: "1.8.0", path: "knowledge/concept-cards/SKILL.md"}
actor: {id: codex, role: extractor, mode: agent-direct}
created_at: 2026-09-12
source_refs: [{id: ccn-book, revision: e0c697b4d4d134f29cb5c2bbde41b1b6b409b63d, path: "/private/tmp/project05-compcogneuro-book-e0c697b4/chapter-07.md"}]
claim_refs: [{id: claim-episodic-binding-r2, revision: 1, path: "#claim-episodic-binding-r2"}]
source_support_refs: [{id: support-episodic-binding-r2, revision: 1, path: "#support-episodic-binding-r2"}]
cq_refs: [{id: cq-episodic-binding-pathway, revision: 1, path: "#cq-episodic-binding-pathway"}]
run_refs: [{id: run-compcogneuro-rich-rerun-20260912, revision: 1, path: "../README.md"}]
extraction_confidence: {assessment: high-for-selected-span, rationale: "Direct extraction from chapter-07.md lines 55-59; figure caption is source context but not independently audited.", scope: "hippocampal anatomy and encoding passage"}
verification_state: unassessed
reconciliation_state: unassessed
memory_admission_ref: null
---

# Concept Card: Hippocampal Episodic Binding

## Concept Boundary

This card covers the source's account of how hippocampal circuitry binds
disparate elements of an episode into a conjunctive memory and reinstates that
pattern during recall. It excludes full hippocampal anatomy, spatial coding,
theta dynamics, novelty, and controlled retrieval except where the selected
passage explicitly marks them as limits or context.

## Quick Definition And Core Definition

Quick definition: hippocampal episodic binding is the source's account of how
EC, DG, CA3, and CA1 activity forms and later reinstates an episodic memory.

Core definition: high-level cortical information converges in entorhinal
cortex and drives DG and CA3 through the perforant pathway, creating a sparse
CA3 engram. CA1 is described as an invertible pattern that can reactivate EC.
Plasticity in CA3 recurrent connections and CA3-to-CA1 connections binds the
engram and associated CA1 pattern so later retrieval can reinstate the episode
out to cortex.

## Prerequisites And Key Properties

- The hippocampus has access to high-level summaries from across the brain.
- DG and CA3 produce a sparse, distinct neural pattern.
- CA3 is described as the main engram for the episode.
- CA1 can reactivate EC, enabling reinstatement beyond the hippocampus.
- Binding is not the whole memory story; the source immediately cautions that
  encoding is distributed and retrieval is supported by cortical learning and
  top-down control.

## Construction Or Recognition

Recognize the concept when the source is explaining how episode elements are
linked into a conjunctive memory and later reinstated. Do not use this card for
every hippocampal function.

## Context And Application

The concept appears under hippocampal anatomy in Chapter 7. It supplies the
mechanistic story behind why the hippocampus is useful for episodic memory.

## Examples

The source uses the ordinary experience of a memory "flooding back" as an
example of reinstatement from CA3 to CA1 to EC to cortex. This is a source
illustration, not an independently verified phenomenological claim.

## Common Errors And Common Confusions

- Over-modularizing memory: the source says simplifying memory as only
  hippocampal binding is inaccurate.
- Confusing the engram with the entire recalled experience. The source treats
  the CA3 engram as part of a reinstatement pathway.
- Ignoring partial cues: the source notes that perforant-pathway learning helps
  reactivate CA3 from partial retrieval cues.

## Source Reference And Support Map

| Assertion | Locator | Support Scope |
| --- | --- | --- |
| Hippocampus receives high-level summary input through EC. | `chapter-07.md` line 55 | Direct source statement. |
| EC drives DG and CA3, producing a sparse CA3 engram. | `chapter-07.md` line 57 | Direct source statement. |
| CA3, CA1, EC, and cortex form the recall/reinstatement pathway. | `chapter-07.md` line 57 | Direct source statement. |
| Memory encoding is distributed beyond this simplified story. | `chapter-07.md` line 59 | Direct source qualification. |

## Claims And Evidence

### Claim `claim-episodic-binding-r2`

The source describes hippocampal episodic binding as a process in which sparse
CA3 engrams and CA1-EC mappings bind episode elements and support later
reinstatement into cortex.

### Support `support-episodic-binding-r2`

Support is direct from `chapter-07.md` lines 55-59. The anatomy figure caption
at line 53 is contextual; the figure itself was not independently audited.

## Relationships And Competency Questions

- Prerequisite: pattern separation contributes to the sparse CA3 engram.
- Related: pattern completion describes recall from partial cues.
- Related: consolidation describes later strengthening outside the hippocampus.

### CQ `cq-episodic-binding-pathway`

According to the source, what pathway allows an encoded episode to be
reinstated during recall?

Expected answer scope: CA3 engram retrieval activates CA1, then EC, then
cortical patterns approximating the original episode.

## Provenance And Preparation Limits

The selected Markdown was read directly from the pinned checkout. No anatomy
figure, external neuroanatomy source, or cited literature was independently
reviewed.

## Extraction Notes And Review Boundaries

This revision adds the source's anti-modularization qualification, which is
important for preventing a too-neat memory-protocol abstraction.

## Lifecycle And Prior Value

No validation, verification, reconciliation, preservation, operator acceptance,
or memory admission has been performed.

## Handoff And Remaining Work

For a full-book run, this card should be checked against figures and any later
appendix/theta material before becoming an accepted hub card.
