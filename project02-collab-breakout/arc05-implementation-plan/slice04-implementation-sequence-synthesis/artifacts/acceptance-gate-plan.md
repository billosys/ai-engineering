# Acceptance Gate Plan

```yaml
project: project02-collab-breakout
arc: arc05-implementation-plan
slice: slice04-implementation-sequence-synthesis
status: proposed-done
artifact-status: acceptance gate plan
source-files-edited: false
```

## Grounding

This acceptance gate plan consumes verified Slice01, verified Slice02,
verified Slice03, and the operator-accepted architecture. It separates Arc05
close from future source implementation. This slice is planning-only and
implementation has not started.

## Arc05 Close Gates

| Gate | Required proof | Go condition | No-go condition |
|------|----------------|--------------|-----------------|
| Slice prerequisites | Slice01, Slice02, and Slice03 `cdc-verification.md` files record `verified-closed`. | All prerequisite close packets exist and were CDC-reproduced. | Any prerequisite slice is missing CDC verification. |
| Slice04 artifacts | Six required Slice04 artifacts exist under `artifacts/`. | `find artifacts -maxdepth 1 -type f -name '*.md'` lists the required files. | A required artifact is missing or outside the slice artifact home. |
| Slice04 ledger | Rows F-1 through F-9 are marked `done` with attested evidence. | Every local ledger Verify command passes from the slice directory. | Any row remains open, deferred without reason, no-op without rationale, or unsupported by evidence. |
| Source boundary | Source files remain untouched. | `git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet` passes. | The source checkout has tracked diff caused by this planning slice. |
| Close packet structure | `closing-report.md` contains verdict, artifact inventory, ledger row walk, silent-drop diff, bubble-up, what worked, and closure summary. | Closing report row count matches opening ledger row count. | Missing row walk entry or missing bubble-up. |
| CDC verification | CDC independently reproduces the close packet. | Slice04 status becomes `verified-closed`. | CDC finds a failed Verify command, missing artifact, source edit, or silent drop. |

## Source Implementation Entry Gates

Source implementation may begin only after all of these are true:

- Arc05 Slice04 has CDC verification.
- Arc05 has a formal `closing-report.md` with composition verdict delivered,
  or the operator explicitly starts implementation from the verified Slice04
  packet before formal arc close.
- The operator gives an explicit source implementation decision.
- The source checkout is clean.
- The implementation prompt includes the ordered source-edit sequence, context
  packet, explicit file-list commit rules, co-author trailers, source/package
  path contract, and no generated-zip commit rule.

## Operator Decisions

| Decision | Default recorded by Slice04 | When to revisit |
|----------|-----------------------------|-----------------|
| top-level `SKILL.md` compatibility | Keep as temporary source-checkout shim, not generated package payload, until README and component-root routes are stable. | Revisit if the operator prefers direct removal or if duplicate source entrypoints confuse the loader. |
| generic component packaging helper | Prefer a generic helper only if it reduces duplicated Makefile package rules without hiding per-component payload lists. | Revisit during Makefile package integration. |
| composer zip payload | Keep `collaboration-framework.zip` composer-only with posture guides and route table. | Revisit only with explicit offline-use requirement to vendor specialist docs. |
| default install behavior | Install all eight component zips by default through `INSTALL_ZIPS`; keep CCDP outside install. | Revisit if install footprint becomes a release concern. |
| accepted package-path warnings | Accept only explicit, bounded warnings after link repair. | Revisit if `make check-package-paths` reports hard failures or unbounded warnings. |

## Source Implementation Required Proof

The future implementation close must include:

- Source implementation commits with explicit file lists and both
  `Co-authored-by` trailers.
- A component coverage table showing all eight accepted components.
- `make check-skills` output after `ALL_SKILL_FILES` is updated.
- Component package target output for every component package.
- `make collab-framework`, `make all`, and `make check-package-paths` output.
- Package-path exception disposition if `package-path-exceptions.tsv` changes.
- Generated zip root and payload inspection.
- Conditional `make ccdp-package` and `make check-ccdp-package` output if
  CCDP surfaces are touched.
- Source checkout cleanliness after generated artifacts are cleaned or left
  ignored.

## No-Go Conditions

- Arc05 is not CDC-verified or source implementation lacks explicit operator
  authorization.
- Source checkout starts dirty for reasons unrelated to the implementation
  slice and the operator has not acknowledged the dirty tree.
- Any accepted component is missing a source root, `SKILL.md`, or sibling
  `version-history.md`.
- `make check-skills`, `make check-package-paths`, `make all`, or required
  component package targets fail without a recorded blocker and re-entry
  condition.
- CCDP files are touched without running the conditional CCDP gates.
- Generated zip artifacts are committed unintentionally.
- Package-path exceptions are used to hide repairable package-local link
  failures.

## Composition Gate

Arc05 composes if the implementation surface map, component file plan,
package/README/validation plan, and this implementation sequence together
cover every accepted component and every cross-cutting gate without source
edits. After Slice04 CDC verification, the remaining Arc05 work is formal arc
close and independent composition review, not another planning slice.
