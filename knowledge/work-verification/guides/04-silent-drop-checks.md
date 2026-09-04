# Silent-Drop Checks

Load this guide when comparing scope-as-specified to scope-as-delivered. The
silent-drop check is the discipline that keeps a close report from becoming a
summary that forgets inconvenient rows.

## Failure Modes

| Failure mode | What it looks like | Countermeasure |
|---|---|---|
| Silent drop | The opening ledger has N rows, but the close addresses fewer than N. | Count rows and walk every ID. |
| Spec-softening | A row is marked `done`, but evidence proves a weaker guarantee than the criterion stated. | Re-run the verifier and compare the actual guarantee to the wording. |
| Partial adoption | A rule is applied in some files, packages, or routes but skipped in equivalent places. | Use workspace-wide greps or explicit impact maps. |
| Vacuous verification | A test or grep passes without exercising the criterion. | Ask what would fail if the criterion were false. |
| Compliance theatre | The paper record says complete while observed behavior does not match. | Require independent reproduction and artifact inspection. |
| Inherited composition | Arc or project composition is accepted because children closed. | Reproduce composition at the arc or project scale. |
| Wrong-scale iteration | Arc/project gaps are patched informally instead of planned as remediation work. | Create a remediation slice, remediation arc, or recorded re-scope. |

## Row Count Check

The simplest silent-drop check is mechanical:

1. Count ledger rows at open.
2. Count row dispositions in the close report.
3. Confirm every opening ID appears exactly once in the close report.
4. Confirm final ledger counts match the row walk.

If rows are missing, the close report is incomplete. Do not convert missing
rows into implicit deferrals after the fact. Add the row disposition, evidence,
and any required re-entry condition.

## Scope Diff

Every slice close needs a scope diff:

- scope as specified in the prompt, slice plan, and ledger;
- scope as delivered in source, artifacts, docs, package output, and planning
  updates;
- explicit list of anything deferred, no-op, or outside scope.

At arc close, compare arc capability to recomposed slices. At project close,
compare definition of done to recomposed arcs.

## Spec-Softening Check

Evidence must satisfy the claim that was written. A range-based test does not
prove an exact-value claim. A source file existing does not prove it is in the
generated package. A link target present in the repository does not prove the
link works package-locally. When evidence is weaker than the row, either fix
the work, amend the row openly, or mark the row not done.

## Partial-Adoption Check

If a route, pattern, package list, vocabulary replacement, or validation rule
changes in one surface, search equivalent surfaces. Partial adoption is common
when the first file found is fixed and sibling entrypoints, docs, release notes,
Makefile package lists, or package-path exceptions are skipped.

Component history lives in [`../version-history.md`](../version-history.md).
