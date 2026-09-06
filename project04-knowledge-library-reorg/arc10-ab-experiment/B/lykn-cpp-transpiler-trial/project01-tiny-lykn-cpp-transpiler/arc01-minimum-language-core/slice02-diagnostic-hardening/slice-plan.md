# Arc 01 Slice 02 Plan: Diagnostic Hardening

## Goal

Harden the first transpiler implementation's error behavior without widening
the accepted language. Slice 02 should turn the diagnostic gaps left after
Slice 01 into explicit, tested behavior while preserving the happy-path C++17
output that CDC already verified.

## Inputs

- Arc 01 plan: `../arc-plan.md`
- Arc 01 Slice 01 CDC verification:
  `../slice01-crate-scaffold-and-happy-path/cdc-verification.md`
- Current implementation:
  `../../../implementation/lykn-cpp-transpiler`

## In Scope

- Add or refine invalid fixtures for:
  - malformed top-level syntax;
  - malformed expression syntax;
  - binary operator arity errors;
  - unsupported forms;
  - unknown identifiers;
  - duplicate bindings;
  - division by literal zero where detection is feasible without adding an
    evaluator;
  - C++-unsafe identifiers such as C++ reserved words or Lykn-style hyphenated
    names.
- Keep diagnostics structured through the existing error types or a minimal
  compatible extension of them.
- Preserve the public library API:
  `pub fn transpile_to_cpp(source: &str) -> Result<String, TranspileError>`.
- Preserve the existing valid fixture and generated C++ output exactly unless
  CC finds a correctness issue and records it as a proposed plan amendment.
- Add focused tests for each newly specified diagnostic category.
- Keep the CLI thin, but add a regression test for one invalid CLI path if the
  existing CLI smoke test does not already cover it.

## Out Of Scope

- Expanding the accepted language beyond Slice 01.
- Full Lykn compatibility.
- lisp-case to camelCase conversion.
- Rich diagnostic rendering, source spans beyond the current byte positions,
  JSON diagnostics, color, recovery, or multiple-error reporting.
- General expression evaluation or constant folding beyond detecting literal
  zero as the direct right operand of division.
- C++ keyword renaming or escaping; for this slice, reject unsafe identifiers
  rather than transform them.
- C++ build-system generation, multiple C++ files, or code audit.

## Diagnostic Policy

This slice should make the tiny language's boundary boring and checkable:

- Unsupported forms should stay parse errors.
- Malformed syntax should identify the expected shape closely enough for a user
  to fix the input.
- Unknown identifiers and duplicate bindings should stay codegen errors unless
  CC has a narrow reason to move them earlier.
- Division by direct literal zero should be rejected as a diagnostic because the
  generated C++ would otherwise contain undefined behavior.
- Identifiers accepted by the parser must also be safe C++ local variable names
  for the tiny generated subset. Reject reserved words and names containing
  hyphens.

## Verification Approach

CC should run from `implementation/lykn-cpp-transpiler`:

- `cargo fmt --check`
- `cargo check`
- `cargo clippy -- -D warnings`
- `cargo test`
- `c++ -std=c++17 -Wall -Wextra -pedantic examples/generated/happy_path.cpp -o /private/tmp/lykn-cpp-transpiler-happy-path-slice02`
- `/private/tmp/lykn-cpp-transpiler-happy-path-slice02`

CDC will independently rerun these gates and inspect new invalid fixtures,
tests, and error-type changes before closing the slice.

## Exit Criteria

All Slice 02 ledger rows must be walked in CC's closing report with attested
evidence. The slice remains proposed-done until CDC independently verifies the
rows and writes `cdc-verification.md`.

Artifacts: source code, fixtures, tests, and any generated examples remain
under `implementation/lykn-cpp-transpiler`. No separate slice `artifacts/`
directory is expected for Slice 02.
