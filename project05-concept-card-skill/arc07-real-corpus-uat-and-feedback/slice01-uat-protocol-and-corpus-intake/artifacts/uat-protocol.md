# Real-Corpus UAT Protocol

## Decision Under Test

This UAT asks whether the current document-extraction and concept-card skills
can carry a bounded, already-Markdown scholarly source into inspectable
candidate records while preserving source identity, claim-level support,
qualifications, and explicit review boundaries. It does not test textbook
truth, whole-corpus throughput, production retrieval, or a deployed memory
system.

## Research Questions

| ID | Question | Decision signal |
| --- | --- | --- |
| UAT-1 | Can a reviewer locate each sampled claim in the pinned source without interpretive guesswork? | Stable source identity and usable locators are retained. |
| UAT-2 | Can the sample be decomposed into one-concept records without losing qualifications or causal/mechanistic distinctions? | Candidate records remain bounded and readable. |
| UAT-3 | Are citations, figures, and cross-references handled as dependencies rather than silently promoted to support? | Dependent material is directly inspected or explicitly caveated. |
| UAT-4 | Is the review burden visible and workable for a human operator? | Review decisions, revisions, and unresolved items are recorded. |
| UAT-5 | Do the resulting records expose enough provenance and relationship structure for a later projection? | A bounded handoff shape is demonstrable without implementing it. |

## Execution Sequence

1. Obtain a temporary checkout at the commit in `corpus-intake.md`; record the
   actual checkout identity and sampled-file preparation evidence.
2. Produce a structure map and stable locator convention before extracting
   claims. Record any source condition that limits reliable locators.
3. Generate a deliberately small candidate set only from the selected sections
   in `pilot-sampling-plan.md`.
4. Conduct an operator review that marks each candidate as accepted for this
   UAT, revised, rejected, or unresolved. These review states do not constitute
   independent CDC verification or memory admission.
5. Assemble the evidence packet: source map, candidate records, review notes,
   unresolved dependencies, and measure results. Compare it to the stop
   conditions before expanding scope.

## Measures And Evidence

| Measure | Pass condition | Evidence to retain |
| --- | --- | --- |
| Traceability | Every candidate has the pinned source identity and a locator that a reviewer can follow. | Manifest, source map, record locator, and review result. |
| Preparation completeness | Sampled files have heading/anchor and dependency mapping before extraction. | Structure map plus readiness/caveat record. |
| One-concept discipline | Each retained candidate has one reviewable concept or explicitly becomes an unresolved/rejected item. | Candidate record and operator rationale. |
| Support fidelity | Claim wording, qualifications, and evidence boundaries match the inspected source; indirect citations or figures remain caveated. | Side-by-side review notes and source excerpts/locators. |
| Operator burden | The operator can identify why every item passed, changed, stopped, or remained unresolved. | Time/work log, decision log, and unresolved list. |
| Handoff readiness | Provenance, locator, lifecycle, relationship, and competency-question fields can be named without inventing a runtime. | Completed handoff checklist in `rag-handoff-assumptions.md`. |

The first five measures are pre-generation acceptance conditions, not merely
post hoc observations. Slice02 must record counts and qualitative failure
reasons for the actual candidates; this protocol intentionally sets no
throughput target.

## Stop Conditions

Stop the pilot, preserve the evidence gathered, and report the condition if:

- the acquired source cannot be tied to the pinned identity;
- a proposed claim cannot be located or its wording/support cannot be reviewed;
- a figure, table, citation, or external dependency is necessary to the claim
  but cannot be inspected or caveated honestly;
- a candidate cannot be made one-concept without concealing substantive
  qualifications or relationships;
- the work expands from the declared sample to a whole-corpus or unrelated
  source run; or
- execution requires a graph database, retrieval service, MCP server,
  embeddings, or memory write to appear successful.

## Confounds And Limitations

The corpus is pre-authored Markdown, so this UAT does not exercise OCR,
conversion, scan quality, or hostile document structure. A small sample cannot
establish recall, scalability, subject-matter correctness, or generality across
disciplines. Operator review is an implementation-facing acceptance signal, not
independent CDC verification. No retrieval evaluation is performed, so any
later RAG claim needs its own data, questions, and comparison protocol.
