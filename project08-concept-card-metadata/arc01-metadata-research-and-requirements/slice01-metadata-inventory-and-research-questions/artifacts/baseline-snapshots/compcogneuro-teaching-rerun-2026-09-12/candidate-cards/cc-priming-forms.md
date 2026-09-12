---
record_type: concept-card
id: cc-priming-forms
revision: 3
title: Priming Forms
concept_slug: priming_forms
aliases: [repetition priming, semantic priming]
card_status: candidate-requires-operator-review
method_ref: {id: concept-cards, revision: "1.8.1", path: "knowledge/concept-cards/SKILL.md"}
actor: {id: codex, role: extractor, mode: agent-direct}
created_at: 2026-09-12
source_refs: [{id: ccn-book, revision: e0c697b4d4d134f29cb5c2bbde41b1b6b409b63d, path: "/private/tmp/project05-compcogneuro-book-e0c697b4/chapter-07.md"}]
claim_refs: [{id: claim-priming-forms-r3, revision: 1, path: "#claim-priming-forms-r3"}]
source_support_refs: [{id: support-priming-forms-r3, revision: 1, path: "#support-priming-forms-r3"}]
cq_refs: [{id: cq-priming-nonconscious, revision: 1, path: "#cq-priming-nonconscious"}]
run_refs: [{id: run-compcogneuro-teaching-rerun-20260912, revision: 1, path: "../README.md"}]
extraction_confidence: {assessment: high-for-selected-span, rationale: "Direct extraction from chapter-07.md lines 137-166.", scope: "priming passage"}
verification_state: unassessed
reconciliation_state: unassessed
memory_admission_ref: null
---

# Concept Card: Priming Forms

## Concept Boundary

This card covers the source's distinction among priming effects. It excludes a
full theory of implicit memory and any independent review of priming studies.

## Quick Definition And Core Definition

Quick definition: priming is a prior-exposure effect in which processing is
changed by earlier experience without requiring conscious recollection.

Core definition: the source distinguishes repetition priming, where the same
stimulus is processed more easily later, and semantic priming, where related
meaning facilitates processing. These effects show memory-like influence
without necessarily involving explicit recall.

## Prerequisites And Key Properties

- Prior exposure changes later processing.
- The effect can occur without conscious recollection.
- Different priming forms depend on what relation holds between prime and
  target.

## Construction Or Recognition

Recognize priming when earlier exposure changes speed, accuracy or ease of
later processing without requiring the subject to intentionally remember the
earlier event.

## Context And Application

The source places priming among memory forms that broaden the chapter beyond
episodic recollection and recognition.

## Examples

Repetition priming occurs when a previously seen word or object is processed
more easily later. Semantic priming occurs when a related word helps process a
target word.

## Common Errors And Common Confusions

- Treating priming as conscious recall.
- Merging repetition and semantic priming.
- Treating any improvement after practice as priming without checking the task
  relation.

## Source Reference And Support Map

| Body statement | Locator | Support |
| --- | --- | --- |
| Priming changes later processing after prior exposure. | `chapter-07.md` lines 137-166 | `support-priming-forms-r3` |
| Repetition and semantic priming are distinct forms. | `chapter-07.md` lines 137-166 | `support-priming-forms-r3` |

## Claims And Evidence

### Claim `claim-priming-forms-r3`

The source presents priming as a memory-related effect in which prior exposure
facilitates later processing without requiring explicit recollection.

### Support `support-priming-forms-r3`

Support is direct from the selected Chapter 7 priming passage; cited studies
and simulations were not inspected.

## Relationships And Competency Questions

- Related: memory forms and recognition.
- Contrasts with: episodic recollection.

### CQ `cq-priming-nonconscious`

Why can priming count as memory-like even without explicit recollection?

Expected answer: prior exposure changes later processing, so past experience
affects behavior without conscious recall.

## Provenance And Preparation Limits

Line locators use the pinned Markdown checkout. Priming studies and simulations
were not independently reviewed.

## Extraction Notes And Review Boundaries

This revision favors a compact distinction among priming forms and leaves
simulation details for later review.

## Lifecycle And Prior Value

Candidate only; validation, semantic verification, reconciliation, preservation,
operator acceptance and memory admission are unassessed.

## Handoff And Remaining Work

Full-book extraction should decide whether repetition priming and semantic
priming deserve separate cards.

