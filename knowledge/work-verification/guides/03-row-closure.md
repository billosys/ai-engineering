# Row Closure

Load this guide before updating a ledger, writing a closing report, or checking
whether a row disposition is valid. It focuses on row mechanics: final
statuses, evidence, row walks, and close artifacts.

## Final Statuses

Every row starts `open` and must end in exactly one final status:

| Status | Valid when | Required evidence |
|---|---|---|
| `done` | The criterion was met as written or by an explicit accepted amendment. | Evidence pointer and strength, reaching at least `reproduced` after independent review. |
| `deferred` | The criterion is not done and is intentionally moved to a later gate. | Concrete reason and re-entry condition. |
| `no-op` | The criterion does not require action for a specific reason. | Rationale that a reviewer can check against the diff and plan. |

`open` is never a final status. A bare "done" is not evidence. "Later" is not
a deferral reason. "Not needed" is not a no-op rationale.

## Working Protocol For CC

1. Read the ledger before editing.
2. Work against the ledger, and raise amendment needs openly.
3. Update row evidence as work lands; use `attested` for doer-supplied
   evidence.
4. In the closing report, walk every row by ID.
5. Name uncertainty and caveats rather than softening the criterion.
6. Include an artifact inventory: produced artifacts under the slice
   `artifacts/` directory by default, an operator-recorded override, or
   "none" checked against the diff.

## Reviewing Protocol For CDC

1. Count opening rows and closing-report rows.
2. For every `done` row, run the verifier or stronger equivalent.
3. For every `deferred` row, check the reason and re-entry condition.
4. For every `no-op` row, check the rationale against the artifacts.
5. Inspect the diff for missing rows, weaker guarantees, partial adoption, and
   artifact-placement mismatches.
6. Record useful success patterns in "What Worked" where the slice close
   calls for it.

## Slice Closing Report Shape

A slice `closing-report.md` should include:

- exact source commit, if source changed;
- exact planning commit placeholder if the first close packet cannot know its
  own hash yet;
- explicit file lists for source and planning commits;
- validation command results;
- row-by-row ledger walk;
- artifact inventory;
- bubble-up to the arc, including scope-as-specified versus
  scope-as-delivered.

If the close-packet commit necessarily records `pending until this report is
committed`, follow with a small metadata commit that records the actual close
commit hash if the project convention requires it.

## Arc And Project Closure

Arc and project closure use the same row mechanics. The row classes change:
children closed, children compose, and bubble-up findings dispositioned. The
composition row at each scale must be reproduced at that scale; it cannot be
closed solely by pointing to child close reports.

## Copyable Tables

Use the retained full template when a project needs a copyable ledger table:
[`../templates/LEDGER-DISCIPLINE.md`](../templates/LEDGER-DISCIPLINE.md).

Component history lives in [`../version-history.md`](../version-history.md).
