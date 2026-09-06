# Arc 02 Closing Report: Diagnostics and Negative Coverage

Metadata:

| Field | Value |
| --- | --- |
| project | project01-tiny-lykn-cpp-transpiler |
| arc | arc02-diagnostics-and-negative-coverage |
| role | CDC |
| status | closed |
| run-label | framework-main-pre-0.5.0 |
| close-date | 2026-09-05 |
| implementation-head | `9d8bbe2f95ceff7fc90acfb8c45c3f3a52c7a2f0` |
| source-control note | `workbench/` is ignored; this close records local ignored-workbench evidence, not a repository commit. |

## Capability Verdict

Arc 02 delivered the intended diagnostic and negative-coverage surface.

The arc remained narrow: it did not widen the accepted language, and it did
not rework the Slice 01 API, valid fixture, or generated happy-path C++ example.
Its only slice added fixture-backed matrix coverage for remaining malformed or
unsupported inputs and independently verified the existing structured
diagnostics against those cases.

## Slice Walk

| Slice | Status | Evidence | CDC Disposition |
| --- | --- | --- | --- |
| Slice 01: Diagnostic Coverage Matrix | closed | `slice01-diagnostic-coverage-matrix/cdc-verification.md` | Independently verified; matrix covers the planned invalid cases and keeps generated happy-path behavior intact. |

No second Arc 02 slice was opened because Slice 01 and the prior Arc 01 Slice
02 diagnostic hardening already satisfied the arc's stated capability.

## Composition Verification

CDC reproduced the arc-scale composition from the crate root:

```bash
cargo fmt --check
cargo check
cargo clippy -- -D warnings
cargo test --test diagnostic_matrix
cargo test
c++ -std=c++17 -Wall -Wextra -pedantic examples/generated/happy_path.cpp -o /private/tmp/lykn-cpp-transpiler-arc02-close
/private/tmp/lykn-cpp-transpiler-arc02-close
```

Observed result:

- formatting, check, clippy, diagnostic-matrix tests, and full tests passed;
- the C++17 smoke binary printed `9`;
- `cargo test` reported 14 passing integration tests and no failing tests;
- the generated C++ happy-path example remained valid.

## Arc Ledger Walk

| Row | Status | Evidence |
| --- | --- | --- |
| A02-01 | done | Slice 01 CDC verification closed the planned diagnostic matrix. |
| A02-02 | done | Arc-scale verification re-ran matrix and full tests, inspected fixture-backed matrix coverage, and preserved C++ smoke evidence. |
| A02-03 | done | Bubble-up was applied: Arc 03 should focus on CLI/example polish and audit-readiness mapping, not more Arc 02 negative-diagnostic slices. |

## Bubble-Up

Arc 02 leaves the project with a stable enough diagnostic surface to move on.
The next arc should make the executable surface more comfortable to use and
make the later code-audit pass easier to scope.

Recommended Arc 03 shape:

- Slice 01: CLI and example surface polish, including at least one additional
  valid fixture/generated C++ example and focused CLI behavior tests.
- Slice 02: audit-readiness surface map and project close preparation, without
  performing the later audit itself unless the operator explicitly asks for it.

## Project Plan Impact

The project plan is updated to mark Arc 02 closed and Arc 03 active. The
project remains in scope and does not need a fourth arc based on current
evidence.

## Verdict

Arc 02 is formally closed. Arc 03 is eligible to open.

