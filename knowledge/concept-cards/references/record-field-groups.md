# Record Field Groups

This reference groups fields already used by sibling templates. It provides a
reviewable convention, not a closed schema: local artifact homes may add fields
when they preserve identity, scope, provenance, and lifecycle separation.

| Construct | Core identity and scope | Provenance and attachments | Lifecycle and body focus |
| --- | --- | --- | --- |
| Concept card | `id`, `revision`, `title`, `concept_slug`, `card_status` | source/prepared-source, claim, edge, CQ, and run refs | extraction confidence; result refs; boundary and summary |
| Claim | `id`, `revision`, `statement`, `assertion_kind`, `card_ref` | source/prepared-source, source-support, and run refs | evidence grade, extraction confidence, states/results; assertion and counterevidence |
| Source support | `id`, `revision`, `subject_ref`, `source_support_status` | embedded source spans, locators, snapshots, prepared-source refs | evidence grade, extraction confidence, scoped comparison |
| Source locator/span | `id`, `revision`, source and snapshot identity, locator type/value | original/prepared mapping, selection boundaries, quote policy | resolution observation and access caveat |
| Relationship edge | `id`, `revision`, relationship type, endpoints, endpoint roles, direction/symmetry | edge-specific support and run refs | evidence grade, extraction confidence, meaning and lifecycle refs |
| Competency question | `id`, `revision`, question, roles, status, requirement source | coverage assertions and covered/support refs | answerability, retrieval observations, lifecycle and re-entry |
| Extraction run | `id`, `revision`, operation, method/prompt, actor, intended and actual scope | source/prepared snapshots, prior runs, worker outputs, output refs | extraction confidence, result refs, coverage and handoff |
| Validation result | `id`, `revision`, target refs, contract, validator, scope | evidence and run refs, checks/findings/warnings | structural outcome, cannot-prove limit, applicability |
| Verification result | `id`, `revision`, target refs, verifier, review context, criteria | evidence, source/prepared snapshots, support and run refs | semantic observations, outcome, state effects, applicability |
| Reconciliation result | `id`, `revision`, conflict class, affected refs, reconciler | support/evidence/run and prior-result refs | decision, resulting refs, state effects, preservation links |
| Preservation decision | `id`, `revision`, prior and destination refs, actor | source support, evidence, run and acceptance refs | disposition, unique value, operator-review need, re-entry |
| Memory admission | `id`, `revision`, target refs, intended use, reliance scope, authority | support, result, run, and acceptance refs | gate summaries, decision stage, admission, rationale, re-entry |

Use stable IDs and revisions. A singular `*_ref` identifies one target; a
`*_refs` list identifies multiple targets. Each reference should retain the
target ID, revision, and path when needed to locate the record. Empty lists mean
no records are attached, not that the associated review passed.

Keep evidence grade about warrant and extraction confidence about the extraction
act. Validation, verification, reconciliation, preservation, and admission are
separate result concerns. Prepared-source references retain upstream provenance
from `document-extraction`; source support still identifies the actual
assertion-to-span comparison.
