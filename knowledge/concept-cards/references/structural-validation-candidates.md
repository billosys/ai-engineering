# Structural Validation Candidates

These are deterministic candidates for a future checker or disciplined manual
checklist. They describe shape and local consistency only. Passing them cannot
prove source warrant, semantic meaning, independent verification, operator
acceptance, or durable-memory suitability.

| Candidate | Check | Limit |
| --- | --- | --- |
| Required identity | Required `record_type`, `id`, and `revision` values are present and locally unique. | Does not establish that an identity refers to the right concept. |
| Required sections | Templates' required explanatory sections are present when their record type needs them. | Presence does not establish adequate reasoning. |
| Rich body profile | A rich concept card has every required readable-body section; empty, unavailable, or unresolved sections state an applicability reason. | Does not establish that the prose is useful, complete, or source-faithful. |
| Source-specific examples | Each asserted source-specific example identifies its source snapshot, recoverable locator, claim, and support attachment. | A link shape does not show that the example or generalization is warranted. |
| Review-boundary hygiene | Extraction/review notes do not state validation, verification, reconciliation, operator acceptance, or memory admission without the applicable record. | Does not establish whether linked result records are sound or complete. |
| Reference shape | Singular and plural references name IDs, revisions, and paths where a path is needed. | A resolving path does not establish semantic applicability. |
| Provenance | Concept cards and extraction runs name relevant source/prepared-source or run provenance. | Preparation is not source support. |
| Source support | A claim, edge, or CQ coverage assertion that asserts support has a scoped support record and span/locator reference. | Presence does not show the span warrants the assertion. |
| Edge closure | Edge endpoints resolve inside the available artifact set and roles/direction are structurally present. | Closure does not establish relation meaning. |
| CQ coverage | Each coverage assertion identifies covered references and its support when claimed. | Coverage does not establish answerability or retrieval success. |
| Local graph closure | Local references do not point to missing or ambiguous records after a declared change. | Does not prove external or runtime graph closure. |
| Preservation record | A prior-value disposition identifies prior value, destination when applicable, rationale, and re-entry when unresolved. | Does not decide whether the preservation rationale is sound. |
| Memory-admission gate | An admission record names target, reliance scope, support/evidence, validation, verification, reconciliation, preservation, and required acceptance fields. | Required fields do not authorize admission. |
| Path and slug hygiene | Paths, anchors, slugs, and filenames are resolvable and locally consistent. | Does not prove taxonomy quality or content equivalence. |
| Obvious consistency | Record type, target type, revision references, and declared result scope do not contradict one another. | Cannot settle ambiguous language or hidden context. |

Record pass, fail, not checked, or not applicable with actual scope and reasons.
No executable validator, JSON Schema, or runtime checker is supplied here.
