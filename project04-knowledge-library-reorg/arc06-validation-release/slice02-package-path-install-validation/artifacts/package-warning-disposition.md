# package warning disposition

## Summary

`make check-package-paths` produced warning-only output and exited 0.

```text
zips scanned: 12
markdown files scanned: 171
hard failures: 0
warnings: 310
explicit exceptions: 3
```

Release-readiness impact: accepted for Slice02 package/path/install validation.
The warnings do not block installable skill package validation because hard
failures are 0 and the generated packages build and install successfully.

## Warning Classes

| Warning class | Disposition | Release-readiness impact | Repair / no-repair rationale |
| --- | --- | --- | --- |
| JavaScript/Deno guide-internal shorthand | accepted as warning-only for Slice02 | non-blocking | Existing package-path checker classifies these as bundled-reference warning rows; package build and install smoke still pass. |
| repo-only/provenance references | accepted or explicitly excepted where recorded | non-blocking | These refer to source/provenance context rather than package-local loader paths. |
| source-clone references | accepted as warning-only | non-blocking | These are meaningful in a source clone and do not prevent package installability. |
| example-project paths | accepted as warning-only | non-blocking | Example paths are not required package files. |
| parser false positives | accepted as warning-only | non-blocking | The checker identifies parser noise rather than missing package payload. |

## Explicit Exceptions

The checker reported explicit exceptions: 3. These remain governed by
`package-path-exceptions.tsv`; Slice02 found no reason to edit that file.

## Repair Decision

No-repair decision: no source repair is required in Slice02.

Reasons:

- `make check-package-paths` exits 0.
- hard failures: 0.
- `make all` exits 0.
- generated package inspection confirms all expected roots and entrypoints.
- isolated install smoke testing passes.

Deferred item: the warning-only classes should be noted in final release
readiness, but they do not require a package/path/install source edit now.
