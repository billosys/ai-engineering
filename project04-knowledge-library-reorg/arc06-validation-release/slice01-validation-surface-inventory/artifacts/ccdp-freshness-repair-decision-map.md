# CCDP freshness repair decision map

## Current CCDP Freshness

CCDP remains a separate protocol/package surface under `protocols/ccdp/`, not
an installable assistant skill package. Arc06 must preserve that
protocol/package separation.

Current commands and results:

| Command | Current behavior | Disposition |
| --- | --- | --- |
| `make ccdp-package` | fails during freshness check before writing a current package | blocker for final CCDP package validation |
| `make check-ccdp-package` | fails at the `ccdp-package` prerequisite | blocked by same stale assembled-spec condition |

Observed failure:

```text
>> checking CCDP assembled spec freshness
tools/ccdp-assembler/target/release/ccdp-assembler --validate --src-dir src --output /private/tmp/ccdp-package-freshness.<tmp> --version 0.2
ERROR: protocols/ccdp/composite-cognition-dispatch-protocol.md is stale
Run 'make -C protocols/ccdp ccdp-rfc' and commit the generated refresh.
make: *** [ccdp-package] Error 1
```

`make check-ccdp-package` emits the same prerequisite failure because the target
depends on `ccdp-package`.

## Repair Options

| Repair option | Required authorization | Expected validation after repair | Notes |
| --- | --- | --- | --- |
| Refresh assembled protocol | Explicit Slice03 source-edit authorization for `protocols/ccdp/composite-cognition-dispatch-protocol.md` by running `make -C protocols/ccdp ccdp-rfc` or equivalent | `make ccdp-package` exits 0; `make check-ccdp-package` exits 0 | Preferred if the source chapters are authoritative and the assembled spec should be regenerated. |
| Adjust CCDP package freshness check | Explicit Slice03 source-edit authorization for `Makefile`, `protocols/ccdp/Makefile`, or `protocols/ccdp/tools/ccdp-assembler/**`, depending on the defect | `make ccdp-package` exits 0 for the accepted freshness model; `make check-ccdp-package` exits 0 | Only appropriate if the freshness check is wrong rather than the assembled spec being stale. |
| Accept stale package as final disposition | Explicit operator acceptance in Slice03 or Slice04 that CCDP freshness is waived | `make ccdp-package` and `make check-ccdp-package` remain failing or are marked no-op by accepted release disposition | This weakens Project04's final validation story and should be treated as a release blocker unless the operator accepts it. |

## No-Edit Boundary for Slice01

Slice01 did not edit source and did not refresh `protocols/ccdp/**`.

Paths requiring later authorization before repair:

- `protocols/ccdp/composite-cognition-dispatch-protocol.md`
- `protocols/ccdp/src/**`
- `protocols/ccdp/json/**`
- `protocols/ccdp/templates/**`
- `protocols/ccdp/visual-guide/**`
- `protocols/ccdp/tools/ccdp-assembler/**`
- source `Makefile` CCDP targets, if the repair changes target behavior

## Decision Needed

Slice03 should decide between:

1. repair by refreshing the assembled CCDP spec and validating the current
   `ccdp.zip` package path; or
2. record an explicit operator-accepted final disposition if CCDP freshness is
   intentionally not repaired.

Until that happens, CCDP package freshness remains Arc06's primary blocker.
