---
record_type: concept-card
id: cc-memory-forms
revision: 3
title: Memory Forms
concept_slug: memory_forms
aliases: [forms of memory, memory taxonomy]
card_status: candidate-requires-operator-review
method_ref: {id: concept-cards, revision: "1.8.1", path: "knowledge/concept-cards/SKILL.md"}
actor: {id: codex, role: extractor, mode: agent-direct}
created_at: 2026-09-12
source_refs: [{id: ccn-book, revision: e0c697b4d4d134f29cb5c2bbde41b1b6b409b63d, path: "/private/tmp/project05-compcogneuro-book-e0c697b4/chapter-07.md"}]
claim_refs: [{id: claim-memory-forms-r3, revision: 1, path: "#claim-memory-forms-r3"}]
source_support_refs: [{id: support-memory-forms-r3, revision: 1, path: "#support-memory-forms-r3"}]
cq_refs: [{id: cq-memory-forms-taxonomy, revision: 1, path: "#cq-memory-forms-taxonomy"}]
run_refs: [{id: run-compcogneuro-teaching-rerun-20260912, revision: 1, path: "../README.md"}]
extraction_confidence: {assessment: high-for-selected-span, rationale: "Direct extraction from chapter-07.md lines 5-15.", scope: "opening Chapter 7 taxonomy"}
verification_state: unassessed
reconciliation_state: unassessed
memory_admission_ref: null
---

# Concept Card: Memory Forms

## Concept Boundary

This card covers the chapter's top-level distinction among memory forms. It is
a navigation card, not a full account of each memory system.

## Quick Definition And Core Definition

Quick definition: memory forms are the major kinds of memory the source
distinguishes by content, accessibility and supporting mechanisms.

Core definition: the source organizes memory into episodic, semantic,
recognition, priming, conditioning, skill-learning and working-memory forms.
The taxonomy helps prevent one memory phenomenon from being mistaken for
another.

## Prerequisites And Key Properties

- Memory is not a single uniform faculty.
- Some forms involve conscious recollection; others can influence behavior
  without explicit recall.
- Different memory forms can depend on different neural systems and tasks.

## Construction Or Recognition

Use this concept when a passage classifies what kind of memory is involved
before explaining mechanism or evidence.

## Context And Application

The chapter begins with this taxonomy before focusing on episodic memory,
hippocampal mechanisms and related memory phenomena.

## Examples

Episodic memory concerns events and contexts; semantic memory concerns general
knowledge; priming changes later processing without requiring conscious
recollection.

## Common Errors And Common Confusions

- Treating memory as only explicit recall.
- Merging recognition and recall.
- Treating priming or skill learning as failed episodic memory rather than
  different memory forms.

## Source Reference And Support Map

| Body statement | Locator | Support |
| --- | --- | --- |
| The chapter distinguishes multiple memory forms. | `chapter-07.md` lines 5-15 | `support-memory-forms-r3` |
| Episodic and semantic memory are central opening distinctions. | `chapter-07.md` lines 7-11 | `support-memory-forms-r3` |

## Claims And Evidence

### Claim `claim-memory-forms-r3`

The source uses a taxonomy of memory forms to organize the chapter and prevent
overgeneralizing from one memory phenomenon to all memory.

### Support `support-memory-forms-r3`

Support is direct from the opening Chapter 7 passage.

## Relationships And Competency Questions

- Contains or routes to: episodic memory, semantic memory, recognition, priming.
- Related: complementary learning systems.

### CQ `cq-memory-forms-taxonomy`

Why should a memory-protocol design distinguish memory forms before modeling
memory operations?

Expected answer: because different forms involve different contents, access
conditions, tasks and mechanisms.

## Provenance And Preparation Limits

Line locators use the pinned Markdown checkout. The full chapter and appendix
were not exhaustively extracted in this run.

## Extraction Notes And Review Boundaries

This card is intentionally broad and should remain a hub unless later chapter
coverage warrants splitting the taxonomy into separate admitted cards.

## Lifecycle And Prior Value

Candidate only; validation, semantic verification, reconciliation, preservation,
operator acceptance and memory admission are unassessed.

## Handoff And Remaining Work

During full-book extraction, use this as a navigation card and create separate
cards for memory forms that receive substantive treatment.

