# Arc 01: Foundation

## Capability

Arc 01 establishes the project foundation: a Rust package, documented trial syntax, a thin CLI boundary, a testable library API, structured errors, deterministic C++ output, and the first small vertical generation paths. It should create enough real implementation surface for later slices without attempting the full expression language.

## Dependencies

- consumes: project prompt, assigned `framework-0.4.1` files, Lykn guide examples, Rust and C++ domain guidelines
- leaves for Arc 02: general arithmetic expression parsing, identifier resolution inside compound expressions, malformed-expression recovery
- leaves for Arc 03: broader fixtures, generated examples, optional C++ compiler integration, final audit map

## Slice Breakdown

| Slice | Scope | Load-bearing for | Status |
|-------|-------|------------------|--------|
| Slice 01: Crate Scaffold | Create the Rust crate, syntax note, thin CLI, library API, literal `(print 42)` vertical path, first diagnostic, tests, and one generated C++ example. | all later slices | closed |
| Slice 02: Let Literal Path | Add `(let name int)` statements, multi-statement programs, printing identifiers bound to integer literals, deterministic statement ordering, and the integer/identifier validity policy needed before generating local `int` declarations. | Arc 02 semantic and expression work | closed |

## Arc Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| A-1 | Slice 01 closes with crate, CLI, library API, tests, and literal print generation. | Read `slice01-crate-scaffold/cdc-verification.md`. | correctness | arc-plan | done | attested: `slice01-crate-scaffold/cdc-verification.md` verifies 8 rows closed on 2026-09-05 | CDC-closed slice |
| A-2 | Slice 02 closes with let literal statements and identifier print support. | Read `slice02-*/cdc-verification.md`. | correctness | arc-plan | done | attested: `slice02-let-literal-path/cdc-verification.md` verifies 13 rows closed on 2026-09-05 after Iteration 01 | CDC-closed slice |
| A-3 | Arc 01 slices compose into the foundation capability. | From the trial workspace, run a valid print-only and let-plus-print example through the CLI and inspect generated C++ output. | serious | arc-plan | done | reproduced: `cargo run --quiet -- <(printf '(print 42)\\n')` and `cargo run --quiet -- <(printf '(let x 40)\\n(print x)\\n(print 42)\\n')` exited 0 on 2026-09-05 and emitted deterministic complete C++ programs | Arc-scale composition check reproduced by CDC and fresh subagent gate |
| A-4 | Slice bubble-up findings are dispositioned before Arc 02 starts. | Inspect this file's Version History and any slice close bubble-up sections. | serious | arc-plan | done | reproduced: Slice 01 ignored-workbench evidence route was handled by direct inspection in CDC verification; Slice 02 range/identifier policy was incorporated in v1.1; Iteration 01 test-isolation finding required no scope change | No remaining Arc 01 bubble-up blocks Arc 02 planning |

## Validation Approach

Arc 01 validation is Rust-first and output-contract focused:

- `cargo fmt --check`
- `cargo test`
- `cargo clippy -- -D warnings` if clippy is installed in the active toolchain
- text checks for deterministic generated C++ including `#include <iostream>`, `int main()`, `std::cout << ... << "\n";`, and `return 0;`

Compiling generated C++ is a project goal, but not required for Slice 01 unless CC finds a local C++17 compiler and records the command/output as extra evidence.

## Version History

- v1.3, 2026-09-05: Closed Arc 01 after arc-level composition checking. Recorded A-3 and A-4 closure evidence; no additional Arc 01 scope or sequencing change was required. Bubble-up to the project is recorded in `closing-report.md` and requires project-plan bookkeeping plus an Arc 02 roadmap wording refinement because baseline let/identifier work landed in Arc 01.
- v1.2, 2026-09-05: Closed Slice 02 after CDC verification of Iteration 01. Recorded A-2 child-close evidence. No Arc 01 scope or sequencing change was required; Arc 01 is ready for arc-level composition checking.
- v1.1, 2026-09-05: Opened Slice 02 after Slice 01 CDC verification. Updated Slice 01 status to closed, recorded A-1 child-close evidence, and expanded Slice 02's scope to make integer range and C++-safe identifier policy explicit before generated local `int` declarations land.
- v1.0, 2026-09-05: Initial Arc 01 plan and ledger.
