# CC Prompt: Arc 02 Slice 01

You are CC for the `framework-main-pre-0.5.0` trial. Implement Arc 02 Slice 01
only: a diagnostic coverage matrix for the tiny Lykn-inspired Rust-to-C++17
transpiler.

This slice uses the arc-local planning layout and is named Arc 02 Slice 01.

## Read First

Read these files before editing:

1. `workbench/cdc-project-prompt.md`
2. `workbench/lykn-cpp-transpiler-trial/project01-tiny-lykn-cpp-transpiler/project-plan.md`
3. `workbench/lykn-cpp-transpiler-trial/project01-tiny-lykn-cpp-transpiler/arc01-minimum-language-core/closing-report.md`
4. `workbench/lykn-cpp-transpiler-trial/project01-tiny-lykn-cpp-transpiler/arc02-diagnostics-and-negative-coverage/arc-plan.md`
5. `workbench/lykn-cpp-transpiler-trial/project01-tiny-lykn-cpp-transpiler/arc02-diagnostics-and-negative-coverage/ledger.md`
6. `workbench/lykn-cpp-transpiler-trial/project01-tiny-lykn-cpp-transpiler/arc02-diagnostics-and-negative-coverage/slice01-diagnostic-coverage-matrix/slice-plan.md`
7. `workbench/lykn-cpp-transpiler-trial/project01-tiny-lykn-cpp-transpiler/arc02-diagnostics-and-negative-coverage/slice01-diagnostic-coverage-matrix/ledger.md`

If you need framework mechanics, use only the assigned in-repo framework
entrypoint:

`/Users/oubiwann/lab/billosys/ai-engineering/knowledge/collaboration-framework/SKILL.md`

Do not use the installed `collaboration-framework` skill or another framework
copy.

Domain references allowed by the trial prompt:

- Rust: `/Users/oubiwann/.codex/skills/rust-guidelines/SKILL.md`
- C++: `/Users/oubiwann/.codex/skills/cpp-guidelines/SKILL.md`
- Lykn surface forms:
  `/Users/oubiwann/lab/lykn/lang/docs/guides/00-lykn-surface-forms.md`

## Implementation Location

Work only under:

`workbench/lykn-cpp-transpiler-trial/implementation/lykn-cpp-transpiler`

## Required Work

Preserve:

- public API:
  `pub fn transpile_to_cpp(source: &str) -> Result<String, TranspileError>`;
- `fixtures/valid/happy_path.lykn`;
- `examples/generated/happy_path.cpp`;
- all existing Slice 01 and Slice 02 tests and diagnostics.

Add a compact diagnostic matrix in the test suite. A fixture-driven or
table-driven structure is preferred so each negative case is easy for CDC and
the later audit pass to inspect.

Cover remaining invalid cases, using fixtures or inline source as appropriate:

- missing top-level close parenthesis;
- missing expression in `let` or `print`;
- trailing non-form token after a valid statement;
- unsupported expression operator such as `%`;
- integer overflow outside `i32`;
- additional C++-unsafe identifier shapes such as `__reserved` and `_Upper`;
- use-before-binding inside a `let` initializer if not already covered.

Use existing structured error variants when they clearly express the failure.
Add small new variants only when the current diagnostic would be too generic to
make a ledger row genuinely checkable.

## Out Of Scope

Do not add:

- new accepted forms;
- new expression operators;
- full Lykn compatibility;
- lisp-case to camelCase conversion;
- identifier escaping or keyword renaming;
- JSON/color/rich diagnostic rendering;
- multiple-error recovery;
- general evaluator or constant folder;
- CLI feature work beyond necessary test support;
- audit findings or audit report.

## Validation

Run from `workbench/lykn-cpp-transpiler-trial/implementation/lykn-cpp-transpiler`:

- `cargo fmt --check`
- `cargo check`
- `cargo clippy -- -D warnings`
- `cargo test`
- `c++ -std=c++17 -Wall -Wextra -pedantic examples/generated/happy_path.cpp -o /private/tmp/lykn-cpp-transpiler-happy-path-arc02-slice01`
- `/private/tmp/lykn-cpp-transpiler-happy-path-arc02-slice01`

The C++ smoke binary should print `9`.

## Closing Report

Create:

`workbench/lykn-cpp-transpiler-trial/project01-tiny-lykn-cpp-transpiler/arc02-diagnostics-and-negative-coverage/slice01-diagnostic-coverage-matrix/closing-report.md`

The closing report must include:

- run setup and files/references read;
- exact source files and fixtures modified or created;
- validation command results;
- row-by-row walk for every ledger row `S01-01` through `S01-10`;
- artifact inventory;
- explicit deferrals/no-ops, if any;
- bubble-up to Arc 02, including scope-as-specified versus scope-as-delivered.

Do not create `cdc-verification.md`; CDC writes that after independent
verification.

End your report by saying whether the slice is proposed-done pending CDC
verification and what CDC should verify first.
