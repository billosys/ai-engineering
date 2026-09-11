---
record_type: source-support
id: support-memory-consolidation
revision: 1
subject_ref: {id: claim-memory-consolidation, revision: 1, path: "cc-memory-consolidation.md#claim-memory-consolidation", record_type: claim}
source_support_status: candidate-supported-with-caveat
source_spans:
  - span_id: span-memory-consolidation
    source_ref: {id: ccn-book, revision: e0c697b4, path: "../source-acquisition.md"}
    source_snapshot_ref: {id: ps-ccn-book-pilot-20260911, revision: 1, path: "../prepared-source-manifest.md"}
    locator_refs: [{id: loc-ch07-consolidation, revision: 1, path: "../locator-map.md#loc-ch07-consolidation"}]
    selection_boundaries: "chapter-07.md lines 113-115, inclusive"
    content_or_description: "Paraphrase preserving the source's on-balance conclusion and its weak-reactivation and controversy qualifications."
    context: "The paragraph surveys observations and a cited study; it is not a direct inspection of the cited study."
    quote_policy: "No quotation retained; source inspected directly."
    checksum_or_edition_note: "chapter-07.md SHA-256 recorded in source-acquisition.md."
prepared_source_refs: [{id: ps-ccn-book-pilot-20260911, revision: 1, path: "../prepared-source-manifest.md"}]
evidence_grade: {assessment: source-reported-with-caveat, rubric_ref: "candidate pilot assessment", rationale: "The source directly states the qualified conclusion, but its cited primary studies and bibliography resolution were not inspected."}
extraction_confidence: {assessment: high-for-selected-span, rationale: "Direct reading preserved the source's explicit qualifications.", scope: "single source span"}
actor: {id: codex-cc, role: extractor, mode: agent-direct}
created_at: 2026-09-11
run_refs: [{id: run-arc07-s02-pilot, revision: 1, path: "../extraction-run.md"}]
validation_refs: []
verification_state: unassessed
verification_refs: []
reconciliation_state: unassessed
reconciliation_refs: []
preservation_refs: []
memory_admission_ref: null
---

# Source Support: Memory Consolidation

## Selected Source Spans

The selected paragraph names the proposed process, observes weak reactivation,
notes controversy about temporally graded gradients, and then gives an
explicitly limited on-balance conclusion.

## Assertion-To-Span Comparison

The candidate repeats the source's scope and qualifications. It deliberately
does not claim that consolidation is universal, that sleep alone causes it, or
that the cited study independently establishes the conclusion.

## Assessments And Preparation Caveats

The source's citation key was inspected in context. `references.bib` and the
underlying cited work were not resolved or read, so they remain an unresolved
dependency. This is why the support status and evidence grade carry caveats.

## Lifecycle And Handoff

No operator or independent reviewer has assessed this candidate. The next step
is review against the pinned passage and, if needed, targeted bibliography work.
