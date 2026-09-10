# Slice01 author closing report — proposed-done design packet

Date: 2026-09-06. Author: CC (Sofie).
Status: author work proposed-done; **slice remains open** for independent design
verification and coordinating contributor/operator decisions. No
cdc-verification.md was written. No toolkit implementation, consumer edits,
commit, package release or acceptance is claimed.

The draft supplies the contract-design capability assigned to Slice01 in the
[arc plan](../arc-plan.md). The [contract](artifacts/status-contract.md) and
[cases](artifacts/contract-cases.md) are concrete proposals for review, with six
explicit decision points. Accepted project choices are retained separately from
the candidate design. [Verification record](artifacts/verification-record.md)
contains actual source baselines, author checks and limitations.

## Scope and artifact inventory

Source baseline: feature/project-status at
`31d96b151781c63004370569d14db556ce21a604`, clean at source-read check.
Planning baseline: `be76ba3` on planning, with Project06 bootstrap untracked.
Planning/source commit: **none requested or created**; no future commit hash is
claimed. The only authored/updated paths, relative to this slice, are:

- `artifacts/status-contract.md` — field, hierarchy, evidence, count, extraction,
  view and compatibility contract; Q-01–06 alternatives and handoff.
- `artifacts/contract-cases.md` — three complete fictional JSON records, worked
  variations, 38 numbered cases, six-project Lykn mapping and ledger coverage.
- `artifacts/verification-record.md` — sanitized source inspection and author
  verification provenance, commands/results and limitations.
- `ledger.md` — disclosed evidence-only amendment; all seven criteria retained
  and left open pending independent review.
- `closing-report.md` — this proposed-done row walk and bubble-up.

The design brief, seed reconnaissance, slice plan, prompt, arc/project files
and both consumer trees were left untouched. Temporary authoring/check scripts
under `/tmp` are not toolkit code or durable product artifacts. Reproduction
responsibilities and results are retained in the verification record.

## Ledger row walk

“done” below is the **CC-proposed disposition**, supported only by attested
evidence; it is not a final ledger status or independent verification. The
ledger deliberately stays open. No row is deferred/no-op or silently dropped.

| ID | Proposed disposition | Evidence and actual author verification | Remaining review boundary |
| --- | --- | --- | --- |
| S-01 | done, attested | Contract sections 2–4 enumerate required/optional/null fields, qualified identities and references. Parsed/walked all three C-01 records with direct and arc slices. | Independent field/record review; accept Q-01/Q-04 ownership and version choices. |
| S-02 | done, attested | Contract sections 3–4, C-02–04/C-19–22/C-37–38 separate lifecycle, delivery, evidence, closure and acceptance; author checked each expected failure against its rule. | Independent semantic review and Q-02 acceptance; no actual validator tested. |
| S-03 | done, attested | Contract section 5; C-01 computes 1/2 at collection/project and 1/1 at arc. C-05/C-10–17 cover optional detail, mismatches, duplicates and unknown/zero counts. | Review Q-03 count meaning; implement/run negative fixtures later. |
| S-04 | done, attested | Refreshed Lykn revision/dirty state and all six project shapes; matrix covers archive, dense/decimal arcs, direct research slices, seed, physical evidence and pending operator review. | Real adoption census and historical judgments remain operator/consumer work. |
| S-05 | done, attested | Read Rootstock keys/templates in place; contract sections 8–10 map all observed field families, views, gates, findings, port lane and lessons to retained/changed/optional behavior. | Q-05 disposition must be accepted; no browser demonstration or private fixture copy. |
| S-06 | done, attested | Contract section 10 and C-32–34 distinguish local format compatibility, source provenance, dependencies and explicit upgrades from installed skill metadata. | Slice02 runtime/dialect/manifest and later copy-isolation/migration tests. |
| S-07 | done, attested | Local file links, JSON parsing/C-01 reference and arithmetic checks, whitespace checks, seven-row/38-case/six-decision inventory, and same-context scope review recorded. | Coordinating contributor/operator review of Q-01–06 and independent design verification are pending. |

## What worked and limitations

The single-owner model makes missing optional pages different from broken
promised links. A leaf-slice example exposes double-counting and direct-slice
omissions. Field-union inspection catches legacy findings variations that a
single sample would miss. Explicitly separating an evidence type (measurement,
command result) from strength prevents historical/physical observations from
being mistaken for independently reproduced completion.

Document/record checks establish inspectability and internal examples, not
schema correctness or renderer behavior. The proposed negative cases, offline
rendering, freshness, snapshot upgrades and UAT have not been executed. Source
inspection supports the migration mapping, not acceptance of the original
Rootstock view or Lykn's historical work. No user/operator has accepted the new
field choices in this implementing context.

## Bubble-up to the arc

1. **Assigned capability:** delivered a proposed common/scale-specific data
   contract and worked acceptance cases, matching the Slice01 breakdown. The
   packet is ready for independent review; it is not an approved Arc02 input.
2. **Findings for coordinating judgment:** all three inspected Rootstock project
   summaries disagree with their arc sums, strengthening the need for explicit
   coverage/ownership. Q-01–04 and Q-06 settle field/behavior tradeoffs; Q-05
   needs an explicit port-lane/lessons disposition. The recommended link-only
   core leaves full optional modules unimplemented; choosing modules requires
   corresponding Slice02 design and later implementation/UAT scope. Do not
   treat that recommendation as an accepted deferral. No parent plan was edited
   and no next slice opened from this implementing context.
3. **Scope-as-specified versus delivered:** both required artifacts, every
   ledger row, all six Lykn shapes, Rootstock extraction/view mapping, evidence
   and count distinctions, local-copy/evolution boundary, and review questions
   are present. Verification consists of the actual author checks recorded.
   Schema/runtime/CLI/package/upgrade/UAT design details remain the already
   planned Slice02 work, and implementation/consumer rebuild remain later arcs.
   Independent acceptance and operator design decisions are outstanding gates,
   not work silently marked complete or moved to a backlog.

Before advancing, the coordinating contributor should review Q-01–06, reproduce
the document checks, assess whether the adjacent-capability disposition changes
the arc plan, and record its own verification/decision evidence. The current
prompt requires review before implementation; this report does not bypass it.
