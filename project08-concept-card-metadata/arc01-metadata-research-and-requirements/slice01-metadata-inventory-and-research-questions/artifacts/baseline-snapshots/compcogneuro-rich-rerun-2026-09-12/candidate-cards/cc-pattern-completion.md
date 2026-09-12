---
record_type: concept-card
id: cc-pattern-completion
revision: 2
title: Pattern Completion From Partial Cues
concept_slug: pattern_completion
aliases: [cued recall, content addressable memory]
card_status: candidate-requires-operator-review
method_ref: {id: concept-cards, revision: "1.8.0", path: "knowledge/concept-cards/SKILL.md"}
actor: {id: codex, role: extractor, mode: agent-direct}
created_at: 2026-09-12
source_refs: [{id: ccn-book, revision: e0c697b4d4d134f29cb5c2bbde41b1b6b409b63d, path: "/private/tmp/project05-compcogneuro-book-e0c697b4/chapter-07.md"}]
claim_refs: [{id: claim-pattern-completion-r2, revision: 1, path: "#claim-pattern-completion-r2"}]
source_support_refs: [{id: support-pattern-completion-r2, revision: 1, path: "#support-pattern-completion-r2"}]
cq_refs: [{id: cq-pattern-completion-cue, revision: 1, path: "#cq-pattern-completion-cue"}]
run_refs: [{id: run-compcogneuro-rich-rerun-20260912, revision: 1, path: "../README.md"}]
extraction_confidence: {assessment: high-for-selected-span, rationale: "Direct extraction from chapter-07.md lines 79-83; cited model paper not inspected.", scope: "pattern completion subsection"}
verification_state: unassessed
reconciliation_state: unassessed
memory_admission_ref: null
---

# Concept Card: Pattern Completion From Partial Cues

## Concept Boundary

This card covers pattern completion as the source's account of recall from a
partial cue to a fuller stored pattern. It excludes search-engine theory,
computer memory architecture, and detailed anatomical optimization except as
analogies or context in the selected source.

## Quick Definition And Core Definition

Quick definition: pattern completion is recall in which a partial cue triggers
completion of the original memory pattern.

Core definition: the source describes human memory as content-addressable:
sufficiently specific information can cue recovery of related episodic
memories. In the hippocampus, recurrent CA3 connections and perforant-pathway
learning make it more likely that a subset of the original pattern can
reactivate the rest.

## Prerequisites And Key Properties

- There is a previously encoded pattern.
- The retrieval cue is partial but sufficiently specific.
- CA3 recurrent connections bind parts of the encoded pattern.
- Perforant-pathway learning helps reactivate original DG/CA3 neurons from a
  partial cue.
- Pattern completion is in tension with pattern separation.

## Construction Or Recognition

Recognize this concept when a source explains recall by completion from a cue,
not by a location-independent pointer or exact stored address.

## Context And Application

The concept follows the source's discussion of pattern separation. The source
emphasizes that encoding would be useless if completed memories could not later
be recalled.

## Examples

The source's summer-camp question illustrates how a partial cue can elicit
related memories. Web search is used as an analogy for content addressability,
not as evidence about brain mechanisms.

## Common Errors And Common Confusions

- Confusing pattern completion with pattern separation. Separation supports
  distinct encoding; completion supports recall from partial cues.
- Treating stronger completion as always better. The source says too much
  completion can reactivate old memories instead of encoding genuinely novel
  episodes.
- Treating the web-search analogy as a claim about implementation.

## Source Reference And Support Map

| Assertion | Locator | Support Scope |
| --- | --- | --- |
| Pattern completion is recall from partial cue to full original pattern. | `chapter-07.md` line 79 | Direct source statement. |
| CA3 recurrent connections facilitate completion. | `chapter-07.md` line 81 | Direct source statement. |
| Pattern separation and completion trade off. | `chapter-07.md` line 83 | Direct source statement with cited-model caveat. |

## Claims And Evidence

### Claim `claim-pattern-completion-r2`

The source reports that pattern completion allows a partial retrieval cue to
reactivate a fuller encoded memory pattern, supported in hippocampus by CA3
recurrent connections and related encoding changes.

### Support `support-pattern-completion-r2`

Support is direct from `chapter-07.md` lines 79-83. The
`@OReillyMcClelland94` citation is not independently inspected.

## Relationships And Competency Questions

- Contrasts with: pattern separation.
- Depends on: episodic binding and encoded CA3 engrams.

### CQ `cq-pattern-completion-cue`

What makes a partial cue effective for recall in the source's account?

Expected answer scope: it can reactivate enough of the encoded pattern for CA3
recurrent connections and learned pathways to complete the rest.

## Provenance And Preparation Limits

The selected source was directly readable Markdown. No external model paper,
Executive Function chapter, or simulation was inspected.

## Extraction Notes And Review Boundaries

This revision makes the separation/completion tradeoff explicit while avoiding
a reviewed edge claim beyond the selected passage.

## Lifecycle And Prior Value

Candidate only. No validation, verification, reconciliation, preservation,
operator acceptance, or memory admission exists.

## Handoff And Remaining Work

A future full-book run should connect this card to theta, executive-control,
and simulation material only after inspecting those sections.
