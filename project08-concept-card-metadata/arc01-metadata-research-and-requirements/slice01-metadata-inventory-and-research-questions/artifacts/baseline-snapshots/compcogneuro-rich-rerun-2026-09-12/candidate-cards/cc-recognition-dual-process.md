---
record_type: concept-card
id: cc-recognition-dual-process
revision: 2
title: Recognition: Familiarity And Recollection
concept_slug: recognition_dual_process
aliases: [dual process recognition, familiarity, recollection]
card_status: candidate-requires-operator-review
method_ref: {id: concept-cards, revision: "1.8.0", path: "knowledge/concept-cards/SKILL.md"}
actor: {id: codex, role: extractor, mode: agent-direct}
created_at: 2026-09-12
source_refs: [{id: ccn-book, revision: e0c697b4d4d134f29cb5c2bbde41b1b6b409b63d, path: "/private/tmp/project05-compcogneuro-book-e0c697b4/chapter-07.md"}]
claim_refs: [{id: claim-recognition-dual-process-r2, revision: 1, path: "#claim-recognition-dual-process-r2"}]
source_support_refs: [{id: support-recognition-dual-process-r2, revision: 1, path: "#support-recognition-dual-process-r2"}]
cq_refs: [{id: cq-familiarity-recollection, revision: 1, path: "#cq-familiarity-recollection"}]
run_refs: [{id: run-compcogneuro-rich-rerun-20260912, revision: 1, path: "../README.md"}]
extraction_confidence: {assessment: high-for-selected-span, rationale: "Direct extraction from chapter-07.md lines 143-149; neuroimaging/behavioral studies not inspected.", scope: "Familiarity and Recognition Memory section"}
verification_state: unassessed
reconciliation_state: unassessed
memory_admission_ref: null
---

# Concept Card: Recognition: Familiarity And Recollection

## Concept Boundary

This card covers the source's dual-process recognition account: perirhinal
familiarity and hippocampal recollection are different memory signals that
contribute to recognition. It excludes full recognition-memory literature,
sharpness-model validation, and claims about conscious access mechanisms beyond
the selected passage.

## Quick Definition And Core Definition

Quick definition: dual-process recognition distinguishes a coarse familiarity
signal from explicit recollection of an episode's details.

Core definition: the source says neocortex can support episodic memory traces
with properties different from hippocampal traces. In particular, perirhinal
cortex can produce a coarse graded familiarity signal, while the hippocampus
supports recollective memory: explicit recall of details from a previous
episode.

## Prerequisites And Key Properties

- A stimulus may leave a neocortical trace after a single exposure.
- Perirhinal familiarity is graded and coarse.
- Hippocampal recollection supplies richer episode detail.
- Familiarity can be consciously read out, but the source says the neural
  mechanism for that readout is not identified.
- The source treats the dual-process model as widely accepted after prior
  controversy, but this run does not review the wider evidence base.

## Construction Or Recognition

Recognize this concept when recognition is explained by two distinct signals:
"this seems familiar" and "I can recall the prior episode." Do not collapse
both into a single memory-strength scale unless the source being inspected does
so.

## Context And Application

The concept appears after the hippocampus-specific discussion, as the source
widens the chapter's view of human memory capacities beyond hippocampal
episodic recall.

## Examples

The selected passage does not give a worked behavioral example. It names
preserved familiarity in people with hippocampal lesions and neuroimaging or
behavioral distinctions as data consistent with the model, but the studies are
not inspected here.

## Common Errors And Common Confusions

- Confusing familiarity with recollection. Familiarity is coarse and graded;
  recollection is explicit recall of episode details.
- Treating perirhinal familiarity as full episodic recall.
- Treating conscious access to familiarity as mechanistically solved; the
  source says the readout mechanism is unidentified.

## Source Reference And Support Map

| Assertion | Locator | Support Scope |
| --- | --- | --- |
| Neocortex can support episodic traces with properties different from hippocampal traces. | `chapter-07.md` line 145 | Direct source statement. |
| Perirhinal cortex can produce a coarse familiarity signal. | `chapter-07.md` line 145 | Direct source statement. |
| Hippocampus provides recollective memory for episode details. | `chapter-07.md` line 145 | Direct source contrast. |
| Dual-process recognition is widely accepted and supported by multiple data types. | `chapter-07.md` line 149 | Source-reported field status; external studies not inspected. |

## Claims And Evidence

### Claim `claim-recognition-dual-process-r2`

The source distinguishes recognition memory into perirhinal familiarity and
hippocampal recollection, treating them as different signals with different
properties.

### Support `support-recognition-dual-process-r2`

Support is direct from `chapter-07.md` lines 145 and 149. Named data categories
are not independently reviewed in this run.

## Relationships And Competency Questions

- Contrasts with: hippocampal episodic binding, which concerns explicit
  episode reinstatement.
- Related: priming, because both discuss non-hippocampal memory contributions,
  though familiarity is consciously accessible and priming generally is not.

### CQ `cq-familiarity-recollection`

How does the source distinguish familiarity from recollection?

Expected answer scope: familiarity is a coarse graded signal associated with
perirhinal cortex, while recollection is hippocampal explicit recall of episode
details.

## Provenance And Preparation Limits

No cited studies or Learning chapter material were inspected. The sharpness
hypothesis is source-reported context, not independently verified mechanism.

## Extraction Notes And Review Boundaries

This revision adds explicit contrast and confusion material, which the Arc07
candidate did not spell out. It preserves the caveat that external studies and
the Learning reference remain unresolved.

## Lifecycle And Prior Value

Candidate only. No validation result, semantic verification, reconciliation,
operator acceptance, preservation decision, or memory admission exists.

## Handoff And Remaining Work

A full-book run should inspect whether later sections distinguish priming,
recognition, and working memory well enough to justify stable relationship
edges among them.
