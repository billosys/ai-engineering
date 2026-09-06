# Arc 02 Slice 01 Plan: Diagnostic Coverage Matrix

## Goal

Add a compact diagnostic coverage matrix for remaining negative boundary cases
without widening the accepted language.

## Inputs

- Project plan: `../../project-plan.md`
- Arc 01 close report: `../../arc01-minimum-language-core/closing-report.md`
- Arc 02 plan: `../arc-plan.md`
- Current implementation:
  `../../../implementation/lykn-cpp-transpiler`

## In Scope

- Add or refine invalid fixtures and tests for remaining boundary cases such
  as:
  - missing top-level close parenthesis;
  - missing expression in `let` or `print`;
  - trailing non-form token after a valid statement;
  - unsupported expression operator such as `%`;
  - integer overflow outside `i32`;
  - additional C++-unsafe identifier shapes such as `__reserved` and `_Upper`;
  - use-before-binding inside a `let` initializer if not already covered.
- Prefer a compact fixture-driven diagnostic matrix in tests so each case names
  the fixture, expected broad error category, and key structured fields or
  display text.
- Preserve the public library API:
  `pub fn transpile_to_cpp(source: &str) -> Result<String, TranspileError>`.
- Preserve the existing happy-path fixture and generated C++ example exactly.
- Preserve all Slice 02 diagnostics and tests.
- Keep all newly rejected cases out of the accepted language.

## Out Of Scope

- Full Lykn compatibility.
- lisp-case to camelCase conversion.
- Any new accepted language forms or expression operators.
- Rich diagnostic rendering, JSON diagnostics, color, recovery, or
  multiple-error reporting.
- General expression evaluation or constant folding.
- C++ keyword renaming or escaping.
- CLI feature work beyond whatever test harness support is needed.
- Audit report or audit findings.

## Diagnostic Policy

This slice should make negative behavior easier to audit, not more ambitious.
CC may add small error variants if a matrix row would otherwise have to assert
an unhelpful generic message, but should prefer the existing structured error
families when they already express the failure clearly.

The matrix should avoid over-specifying byte positions unless the existing
variant makes the position load-bearing. Tests should prove the right error
category and the important human-facing detail.

## Verification Approach

CC should run from `implementation/lykn-cpp-transpiler`:

- `cargo fmt --check`
- `cargo check`
- `cargo clippy -- -D warnings`
- `cargo test`
- `c++ -std=c++17 -Wall -Wextra -pedantic examples/generated/happy_path.cpp -o /private/tmp/lykn-cpp-transpiler-happy-path-arc02-slice01`
- `/private/tmp/lykn-cpp-transpiler-happy-path-arc02-slice01`

CDC will independently rerun these gates and inspect the fixture matrix,
accepted-language boundary, and preserved happy-path output before closing the
slice.

## Exit Criteria

All `S01` ledger rows must be walked in CC's closing report with attested
evidence. The slice remains proposed-done until CDC independently verifies the
rows and writes `cdc-verification.md`.

Artifacts: source code, fixtures, tests, and generated examples remain under
`implementation/lykn-cpp-transpiler`. No separate slice `artifacts/` directory
is expected for this slice.
