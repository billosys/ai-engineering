# Evidence Strength

Load this guide whenever a ledger row, close report, review, or package gate
needs to distinguish a doer's claim from independently reproduced evidence.
The strength vocabulary is part of the closure contract, not decorative prose.

## Strength Levels

| Strength | Meaning | Closure use |
|---|---|---|
| `asserted` | Claimed done with no evidence attached. | Never valid closure. |
| `attested` | The doer supplied evidence, command output, or a pointer, but it has not been independently re-run. | Proposed-done only. |
| `reproduced` | An independent reviewer re-ran the verification or witnessed the demonstration and observed the same result at this scale. | Minimum valid strength for a `done` row. |
| `reconciled` | The reproduced result is also checked against broader truth: CI, whole-workspace state, generated package shape, external source, or equivalent integration evidence. | Strongest closure evidence. |

A `done` row must reach at least `reproduced` at its own scale. `attested`
evidence is useful because it lets the doer provide a concrete claim, but the
unit remains proposed-done until CDC, a fresh context, CI, the operator, or
another independent reviewer reproduces it.

## Applying Strength At Each Scale

At slice scale, source diffs, grep checks, focused tests, package inspections,
and local-link validations are usually doer-attested first. CDC converts those
claims to reproduced evidence by running the listed verifier or a stronger
equivalent and inspecting the actual artifacts.

At arc scale, pointers to closed child slices are attested evidence for
"children closed" rows. They are not enough for composition rows. Arc
composition requires a reproduced integration demonstration at arc scale.

At project scale, pointers to closed arcs are attested evidence for
"children closed" rows. Project definition-of-done rows require a reproduced
system or acceptance demonstration and may include an explicit operator
judgment when "did we build the right thing" cannot be reduced to a command.

## Evidence Must Be Reproducible

Prefer evidence that a reviewer can run or inspect directly:

- commit SHA plus exact files changed;
- command transcript or validation target;
- grep route that checks the landed text;
- generated package listing;
- local-link validation output;
- CI run, install smoke, or integration demonstration.

"Verified manually" is not enough by itself. If a demonstration cannot be
scripted, record who witnessed it, what state they inspected, and what would
make the claim false.

## Package And Release Gates

For package-oriented work, source scans are not the final boundary. Generated
zips, install staging, package-local Markdown links, and explicit exception
files are the acceptance surface. A doer may attest that a source file exists;
package closure is stronger when the built artifact is inspected and
reconciled against the source intent.

## Common Mistakes

Do not mark asserted evidence as done. Do not treat a doer's command output as
independent reproduction. Do not inherit composition from closed children. Do
not upgrade a warning-heavy package run to failure unless the gate reports hard
failures or the slice ledger defines warnings as failing.

Component history lives in [`../version-history.md`](../version-history.md).
