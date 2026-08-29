# Warning Policy Classification

Generated from `make check-package-paths` before and after the Slice 04 policy
change.

## Baseline

- `current-warning-baseline.txt`: 0 hard failures, 295 warnings, 3 explicit exceptions.
- `post-warning-policy-check.txt`: 0 hard failures, 295 warnings, 3 explicit exceptions.
- `current-warning-counts.tsv` and `post-warning-counts.tsv` carry package/class/count groupings extracted from the generated package-path inventory.
- The count stayed stable because Slice 04 tightened disposition language without hiding unresolved package usability issues.

## Classes

| Class | Count | Disposition |
|-------|------:|-------------|
| `bundled-reference` | 89 | Warning. Five stale `after-arc02` transitional exception rows were converted to ordinary warnings with later-maintenance expiry labels. |
| `repo-only/provenance` | 149 | Mixed. Three targeted explicit exceptions remain for placeholder or provenance-only paths; the other 146 findings remain warnings. |
| `source-clone-reference` | 26 | Warning. These describe links that resolve in the source checkout but are not bundled paths. They stay visible for later package/reference cleanup. |
| `example-project path` | 25 | Warning. These are examples or illustrative project paths, not bundled artifacts. They remain visible and are not promoted to broad exceptions. |
| Parser false positives | 9 | Warning. These are scanner limitations around non-path prose or generated parse shape. They stay visible rather than being suppressed package-wide. |

## Package Notes

- `javascript-deno-guidelines`: 81 bundled-reference warnings remain for guide-internal shorthand such as `12-deno/*.md` and `13-biome/*.md`.
- `rust-guidelines`: 6 bundled-reference warnings remain for `09-common-pitfalls.md`, which is referenced but not shipped in the package.
- `cpp-guidelines`: 2 bundled-reference warnings remain for parameter-passing image references that are not shipped in the package.
- `collaboration-framework` and `go-guidelines`: targeted explicit exceptions remain limited to placeholder or provenance-only paths already accepted by prior slices.
- Blank or `.` package keys in the generated count artifacts come from findings whose resolved field is blank or the checkout root. This is an extraction/reporting artifact, not a new package target.
