---
record_type: source-support
id: support-pattern-separation
revision: 1
subject_ref: {id: claim-pattern-separation, revision: 1, path: "cc-pattern-separation.md#claim-pattern-separation", record_type: claim}
source_support_status: candidate-supported-with-caveat
source_spans:
  - span_id: span-pattern-separation
    source_ref: {id: ccn-book, revision: e0c697b4, path: "../source-acquisition.md"}
    source_snapshot_ref: {id: ps-ccn-book-pilot-20260911, revision: 1, path: "../prepared-source-manifest.md"}
    locator_refs: [{id: loc-ch07-pattern-separation, revision: 1, path: "../locator-map.md#loc-ch07-pattern-separation"}, {id: loc-ch07-pattern-figure, revision: 1, path: "../locator-map.md#loc-ch07-pattern-figure"}]
    selection_boundaries: "chapter-07.md lines 67-75, inclusive, plus directly inspected pattern-separation figure"
    content_or_description: "Paraphrase of sparseness, lower overlap, and the stated consequence for novel episodic encoding."
    context: "The figure illustrates sparse hippocampal and overlapping cortical patterns; it does not replace the text's claim."
    quote_policy: "No quotation retained; text and figure inspected directly."
    checksum_or_edition_note: "chapter-07.md and figure SHA-256 values are recorded in source-acquisition.md and locator-map.md."
prepared_source_refs: [{id: ps-ccn-book-pilot-20260911, revision: 1, path: "../prepared-source-manifest.md"}]
evidence_grade: {assessment: source-reported, rubric_ref: "candidate pilot assessment", rationale: "The source directly states the candidate assertion; it also cites unreviewed literature, so the grade does not extend to independently established neuroscience."}
extraction_confidence: {assessment: high-for-selected-span, rationale: "Direct text and figure inspection; citation dependency kept explicit.", scope: "single source span and figure"}
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

# Source Support: Pattern Separation

## Selected Source Spans

The text defines sparseness and says lower overlap makes pattern separation
important for rapid encoding with less interference. The inspected illustration
visually contrasts sparse hippocampal activations with overlapping cortical ones.

## Assertion-To-Span Comparison

The selected text directly supports the source-reported mechanism statement.
The claim retains the source's hippocampal scope and avoids treating the cited
Marr work or the figure as independently reviewed support.

## Assessments And Preparation Caveats

`@Marr71` was identified at line 67 but its bibliographic record and paper were
not inspected. The Executive Function cross-reference at line 83 is outside the
support span and remains unresolved/contextual. These gaps preclude a stronger
verification claim.

## Lifecycle And Handoff

The support is ready for operator comparison only; no operator decision or
independent verification is recorded.
