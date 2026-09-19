# Slice17 closing report

Status: CC proposed-done. This is the CC completion report for the
three-contributor workflow; it is not CRC verification, CDC acceptance or a
semantic-implementation authorization.

## Intake and scope

Prompt: `project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice17-run-preparation-method-and-reference-provenance/cc-prompt.md`.
Source baseline: `ce3f77103eff5e07b3533a03c65f158684fc1039`.
Opening planning commit: `c40e52fc1318e6213c60d5e0371fd01aa3208f1d`.
Preserved pre-opening planning baseline: `c6d445b8cf693e0c03a70a79d5b45c07e3337dcb`.
Set A authority: `dee3052c88e0fd9361e74200fd1eea26ade76435`.

The exact eighteen-pair assignment, 555 frozen full pairs, 220 accepted,
335 remaining, and 317 outside pairs were preserved. No source, schema,
runtime, parser, package, memory, extraction, graph, UAT or coverage artifact
was changed. The six changed paths are this report, `ledger.md`, and the four
files under `artifacts/`.

## Row closure attestation

| Row | CC result | Evidence |
| --- | --- | --- |
| S17-1 | Exact Set A membership, current census, accepted non-overlap and outside complement preserved | `artifacts/semantic-membership.json`; `artifacts/validation-evidence.md` |
| S17-2 | Required intake, source readback, authority registry, hashes, ranges and limits recorded | `artifacts/semantic-evidence.md`; `artifacts/semantic-membership.json`; `artifacts/validation-evidence.md` |
| S17-3 | Three native extraction-run records, all 18 matrix fields, availability exclusions and bounded 2,054-record historical census reproduced | `artifacts/semantic-evidence.md`; `artifacts/validation-evidence.md` |
| S17-4 | Every member has contextual meaning, applicability, exceptions, reader/extractor/query/migration consequences and unresolved owner | `artifacts/semantic-membership.json`; `artifacts/handoff.md` |
| S17-5 | Positive no-match, deliberate tool-error and field/shape/target/revision controls are encoded and fail closed | `artifacts/validation-evidence.md` |
| S17-6 | Pinned evidence, exact scope, source/protected-history checks and separate recipe replay route are encoded | `artifacts/validation-evidence.md` |
| S17-7 | Later Set B-E owners, 248-pair complement, P-15, runtime/UAT/memory gates and unresolved questions are handed off | `artifacts/handoff.md`; this report |

## Validation status

The literal precommit route passed with status 0 from the canonical planning
checkout root. It reproduced three parsed extraction-run records: one template
and two synthetic examples; three YAML parse-error records; fifteen
no-opening-frontmatter exclusions; and 2,054 Complete Musician/Erlang records
with zero root presence for the twelve historical comparison paths.

The two declared synthetic paths both returned successful no-match results:
status 0, empty stdout and empty stderr. The deliberate missing input returned
status 128 with nonempty stderr and was classified as a tool error. Evidence
authority, hash, range, singular/plural, empty/absent, added-path, wrong
identity, wrong revision, wrong path and wrong-target controls all returned
the expected status 1.

The committed CC endpoint is
`97a75091b6d124955762f12c72865f72d5aedd53`; its same-endpoint wrapper passed
with status 0. The distinct recipe endpoint
`f82af9b76a5e3bc6aa063141e87445f02cc40b9b` also passed with status 0 when
loaded with the CC registry endpoint above. Missing-recipe and foreign-source
recipe endpoints both failed closed with status 2.

## Proposed-done limits and follow-up

The packet records observations and bounded semantic interpretations only. It
does not define a normative extraction-run schema, requiredness policy,
timestamp format or ordering, migration, source repair, extraction completion,
claim support, memory admission, runtime behavior, package validity, UAT or
coverage acceptance. Slice18-21 and the 248-pair complement retain their
owners. CRC must independently review this packet; CDC retains structural
composition authority and the Operator retains acceptance authority.

Known exploratory failures are preserved in `artifacts/validation-evidence.md`:
two initial historical-query syntax errors, one truncated combined-read output
recovered by contiguous reads, one route jq spacing error, one out-of-bounds
replay range corrected from 1-118 to the actual 1-93, and the first route
invocation from the slice subdirectory rejected by its root-relative scope
check. No compaction, model identity or effort measurement was available.
