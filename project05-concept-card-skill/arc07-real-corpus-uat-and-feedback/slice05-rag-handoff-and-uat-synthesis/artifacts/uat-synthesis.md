# Arc07 UAT Synthesis

## Decision Addressed

Arc07 tested whether the delivered preparation and concept-card skills could
take a bounded, upstream-authored Markdown source into inspectable candidate
records while retaining source identity, support, qualifications, and review
boundaries. It did not test textbook truth, whole-book throughput, retrieval,
runtime operation, or memory admission.

## Slice Walk

| Slice | Evidence and result | Remaining limit |
| --- | --- | --- |
| Slice01 | Pinned the corpus commit/tree, recorded CC-BY-4.0 handling and inventory, set UAT questions/measures/stop conditions, selected Chapter 1 and Chapter 7 pilot material, and named downstream handoff expectations. | Intake did not approve whole-book processing or runtime ingestion. |
| Slice02 | Prepared the bounded Markdown sample and produced four candidate cards with four source-support records, direct inspection of two relevant figures, and seven friction findings. | No operator review occurred; bibliography and cross-reference dependencies stayed caveated. |
| Slice03 | Dispositioned F-1 through F-7 without silent drops. F-2 became the `document-extraction` 1.4.4 citation-bearing Markdown audit; F-1 and F-3 through F-7 were checked no-ops grounded in existing guidance. | The refinement does not resolve the corpus's `ccnlab.bib` versus `references.bib` ambiguity or authorize runtime work. |
| Slice04 | Added six Chapter 7 candidates and linked the four pilot inputs into a bounded ten-card memory-protocol subset, with self-check sampling, dependency audit, review packet, and full-book re-entry condition. | The output remains partial and candidate-only; no independent semantic verification or operator decision occurred. |

## Measures And Observations

| UAT measure | Arc07 observation | Claim boundary |
| --- | --- | --- |
| Traceability | Pinned snapshot, chapter hashes, headings, and line locators were retained; sampled locators recovered. | Long Markdown paragraphs make locator granularity a retained caveat. |
| Preparation completeness | Structure/locator/dependency records were created for the selected scope. | This does not demonstrate preparation completeness for all ten chapters or every figure. |
| One-concept discipline | Four pilot and six expanded candidates preserve stated boundaries and qualifications. | Boundary fitness still needs operator review; no semantic acceptance is implied. |
| Support fidelity | Candidate support remained source-scoped; figures, citations, and cross-references were inspected or caveated. | Self-checking and source-reported evidence are not independent verification. |
| Operator burden | The review packets make required decisions and evidence visible. | No operator performed the review, so burden/workability was not measured in use. |
| Handoff readiness | Record identity, provenance, lifecycle, and downstream needs can be named without a runtime. | This is a planning handoff only, not evidence of successful retrieval or import. |

## Findings And Disposition

- F-2 was the sole accepted source refinement: direct bibliography-resource and
  key lookup are now required before a mapping is asserted.
- F-1 and F-3 through F-7 were checked no-ops because existing live guidance
  already covered locator identity, figure inspection, one-concept boundaries,
  qualification retention, operator workflow, and runtime exclusion.
- EF-1 retains the full-book re-entry requirement; EF-2 retains bibliography
  ambiguity as a caveat; EF-3 retains cross-chapter references as contextual,
  not direct support.

No stop condition fired for the bounded run. That fact supports only the
declared subset: it does not establish corpus completeness, generality,
retrieval quality, or runtime readiness.
