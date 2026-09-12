# Arc09 Slice03 Closing Report: Regression Examples And Validation

## Status

CC proposed-done. This slice is planning-artifact-only: no source file changed
and no source commit exists. Independent CDC verification remains pending.

## Source And Planning Commits

No source correction was required by the regression checks. The relevant source
baseline is Slice02 commit `1d6bbd08` (`Add rich concept-card profile`). This
planning close packet is pending its own commit and includes the Arc09 ledger,
this slice's `slice-plan.md`, `ledger.md`, `closing-report.md`, and the two
files under `artifacts/`.

## Validation

Focused heading inspection found every required rich-profile affordance in the
template and synthetic example. Wrapper scanning found none of the required
response tokens, response envelopes, or whole-card Markdown wrappers in those
current files or the inspected Arc07 candidate. It found a trailing
`</content>` response envelope in the historical Erlang comparison card; its
Erlang code fence is legitimate example content.

`git -C .worktrees/planning diff --check` passed before closing edits. No
source file changed, so `make check-skills`, `make check-skill-versions`, and
`make check-package-paths` were not rerun; Slice04 owns the final package
inspection after all Arc09 changes.

## Ledger Walk

| Row | CC status | Evidence |
| --- | --- | --- |
| S3-1 | cc-proposed-done | [Regression review](./artifacts/rich-profile-regression-review.md) maps all required rich sections in the current template and example. |
| S3-2 | cc-proposed-done | The review compares the affordances and legacy control limitations in `applied-chord.md` and `application-behaviour.md` without treating either as a schema. |
| S3-3 | cc-proposed-done | The review contrasts the current rich profile with Arc07 `cc-memory-consolidation.md`; no candidate was changed or accepted. |
| S3-4 | cc-proposed-done | [Validation check record](./artifacts/validation-check-record.md) records response-token/wrapper scans and the historical Erlang envelope finding. |
| S3-5 | cc-proposed-done | The review confirms rich prose does not replace typed edge/CQ, source-support, evidence, or lifecycle controls. |
| S3-6 | cc-proposed-done | The artifacts identify the synthetic non-resolving-link limitation, historical wrapper finding, no source correction, and Slice04 package obligation. |

Rows: 6. CC-attested proposed-done: 6. Deferred: 0. No-op: 0. Independent CDC verification: pending.

## Artifact Inventory

The durable Slice03 artifacts are
[rich-profile-regression-review.md](./artifacts/rich-profile-regression-review.md)
and [validation-check-record.md](./artifacts/validation-check-record.md). No
other durable slice-produced artifact was created.

## Bubble-Up To Arc09

Slice03 delivered its assigned regression evidence: it shows that the Slice02
profile restores the historical reader/reference affordances while retaining
the v4 control layer, and it records the known Erlang wrapper residue as a
concrete comparison finding. The silent-drop check found no direct source
blocker, so no unrelated redesign or `document-extraction` change occurred.

No Arc09 plan amendment is needed. Slice04 must reproduce the current review,
run the final source/package gates and archive inspection, retain the synthetic
traceability limitation as a caveat, and prepare the Arc09 closure inputs.
The Arc09 plan names Slice04, but its directory and CC prompt are not yet in
the planning worktree. Create that prompt from `arc09-rich-concept-card-profile/arc-plan.md`
and these Slice03 artifacts before advancing.
