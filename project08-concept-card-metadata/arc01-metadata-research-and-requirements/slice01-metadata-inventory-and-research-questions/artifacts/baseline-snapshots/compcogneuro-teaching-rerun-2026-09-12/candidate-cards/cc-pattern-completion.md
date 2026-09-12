---
record_type: concept-card
id: cc-pattern-completion
revision: 3
title: Pattern Completion
concept_slug: pattern_completion
aliases: [cue-driven completion]
card_status: candidate-requires-operator-review
method_ref: {id: concept-cards, revision: "1.8.1", path: "knowledge/concept-cards/SKILL.md"}
actor: {id: codex, role: extractor, mode: agent-direct}
created_at: 2026-09-12
source_refs: [{id: ccn-book, revision: e0c697b4d4d134f29cb5c2bbde41b1b6b409b63d, path: "/private/tmp/project05-compcogneuro-book-e0c697b4/chapter-07.md"}]
claim_refs: [{id: claim-pattern-completion-r3, revision: 1, path: "#claim-pattern-completion-r3"}]
source_support_refs: [{id: support-pattern-completion-r3, revision: 1, path: "#support-pattern-completion-r3"}]
cq_refs: [{id: cq-pattern-completion-cue, revision: 1, path: "#cq-pattern-completion-cue"}]
run_refs: [{id: run-compcogneuro-teaching-rerun-20260912, revision: 1, path: "../README.md"}]
extraction_confidence: {assessment: high-for-selected-span, rationale: "Direct extraction from chapter-07.md lines 77-89.", scope: "pattern completion passage"}
verification_state: unassessed
reconciliation_state: unassessed
memory_admission_ref: null
---

# Concept Card: Pattern Completion

## Concept Boundary

This card covers the source's account of retrieving a fuller memory from a
partial cue. It excludes general recall theory and pattern separation except as
the relevant tradeoff.

## Quick Definition And Core Definition

Quick definition: pattern completion uses a partial cue to reactivate the
larger memory pattern associated with it.

Core definition: the source describes pattern completion as a hippocampal
capacity that works against the extreme of pattern separation. If memories were
only separated, small cues would not recover them; completion lets a cue bring
back the associated episode.

## Prerequisites And Key Properties

- A partial cue overlaps with the stored representation.
- The system can reactivate associated features.
- Completion must be balanced with separation to avoid interference.

## Construction Or Recognition

Recognize pattern completion when a source explains recall from partial
information rather than initial encoding of distinct events.

## Context And Application

The source introduces completion after separation to show why episodic memory
requires a balance: distinct episodes must be kept apart, yet usable cues must
still retrieve them.

## Examples

A fragment of a remembered event can trigger recovery of associated context,
such as a location cue bringing back the broader episode.

## Common Errors And Common Confusions

- Confusing completion with separation: completion recovers from partial cues;
  separation reduces overlap during encoding.
- Treating completion as perfect replay; the selected source does not establish
  that.
- Ignoring the tradeoff: too much separation makes completion harder.

## Source Reference And Support Map

| Body statement | Locator | Support |
| --- | --- | --- |
| Pattern completion supports retrieval from partial cues. | `chapter-07.md` lines 77-89 | `support-pattern-completion-r3` |
| Completion trades off with separation. | `chapter-07.md` lines 77-89 | `support-pattern-completion-r3` |

## Claims And Evidence

### Claim `claim-pattern-completion-r3`

The source presents pattern completion as the cue-driven complement to pattern
separation in episodic memory.

### Support `support-pattern-completion-r3`

Support is direct from the selected Chapter 7 passage; cited model references
were not resolved.

## Relationships And Competency Questions

- Trades off with: pattern separation.
- Supports: episodic recall.

### CQ `cq-pattern-completion-cue`

What problem does pattern completion solve that pattern separation alone would
not solve?

Expected answer: it lets a partial cue recover a fuller stored episode.

## Provenance And Preparation Limits

Line locators use the pinned Markdown checkout. External model citations were
not inspected.

## Extraction Notes And Review Boundaries

This card keeps the concept compact and leaves cited-model review for later.

## Lifecycle And Prior Value

Candidate only; validation, semantic verification, reconciliation, preservation,
operator acceptance and memory admission are unassessed.

## Handoff And Remaining Work

Full-book work should check whether later chapters add recognition, attention
or executive-function interactions that change this boundary.

