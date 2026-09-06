# CC Prompt: Arc 01 Slice 02

You are CC for the `framework-main-pre-0.5.0` trial project. Your job is to
implement Arc 01 Slice 02 only: diagnostic hardening for the tiny
Lykn-inspired Rust-to-C++ transpiler.

Treat your work as proposed-done until CDC independently verifies it.

## Read First

From the ai-engineering repository root, read:

1. `workbench/cdc-project-prompt.md`
2. `workbench/lykn-cpp-transpiler-trial/project01-tiny-lykn-cpp-transpiler/project-plan.md`
3. `workbench/lykn-cpp-transpiler-trial/project01-tiny-lykn-cpp-transpiler/arc01-minimum-language-core/arc-plan.md`
4. `workbench/lykn-cpp-transpiler-trial/project01-tiny-lykn-cpp-transpiler/arc01-minimum-language-core/ledger.md`
5. `workbench/lykn-cpp-transpiler-trial/project01-tiny-lykn-cpp-transpiler/arc01-minimum-language-core/slice01-crate-scaffold-and-happy-path/cdc-verification.md`
6. `workbench/lykn-cpp-transpiler-trial/project01-tiny-lykn-cpp-transpiler/arc01-minimum-language-core/slice02-diagnostic-hardening/slice-plan.md`
7. `workbench/lykn-cpp-transpiler-trial/project01-tiny-lykn-cpp-transpiler/arc01-minimum-language-core/slice02-diagnostic-hardening/ledger.md`

Use only the assigned framework version named in `workbench/cdc-project-prompt.md`
if you need framework guidance. Do not borrow process rules from installed,
cached, older, newer, or remembered framework copies.

Domain references are allowed at these paths:

- Rust: `/Users/oubiwann/.codex/skills/rust-guidelines/SKILL.md`
- C++: `/Users/oubiwann/.codex/skills/cpp-guidelines/SKILL.md`
- Lykn guides: `/Users/oubiwann/lab/lykn/lang/docs/guides/`

## Implementation Directory

Work in:

`workbench/lykn-cpp-transpiler-trial/implementation/lykn-cpp-transpiler`

Do not move the crate. Do not edit the framework source files.

## Slice Goal

Harden diagnostics while preserving the Slice 01 language and generated C++.
This is not a language-expansion slice.

The existing public API must remain:

```rust
pub fn transpile_to_cpp(source: &str) -> Result<String, TranspileError>
```

## Required Work

Add or refine structured diagnostics and tests for these categories:

- malformed top-level syntax;
- malformed expression syntax;
- binary operator arity errors, covering too-few and too-many operands;
- unsupported forms;
- unknown identifiers;
- duplicate bindings;
- direct literal division by zero, such as `(/ x 0)`;
- C++-unsafe identifiers, including at least one C++ reserved word and one
  hyphenated identifier.

Keep errors structured through the existing `TranspileError`, `ParseError`, and
`CodegenError` family, or make the smallest compatible extension. Avoid
string-only errors as the public contract.

For C++-unsafe identifiers, reject them. Do not rename, escape, mangle, or
camel-case them in this slice.

For division by zero, detect the direct literal-zero case before emitting C++.
Do not add a general evaluator or constant folder.

Preserve the existing valid fixture and generated C++ output exactly unless you
find a correctness defect. If you believe it must change, record that as a
proposed plan amendment in your closing report before making a wider change.

## Tests And Fixtures

Add focused invalid fixtures under `fixtures/invalid/` where fixtures help the
evidence stay readable. Add or expand tests in `tests/` so each Slice 02 ledger
row is observable.

At minimum, tests should prove:

- the happy-path fixture still transpiles to the exact generated C++ example;
- each new diagnostic category fails clearly;
- at least one invalid CLI invocation exits non-zero, leaves stdout empty, and
  writes the diagnostic to stderr.

## Out Of Scope

Do not implement:

- new accepted language forms;
- full Lykn compatibility;
- lisp-case to camelCase conversion;
- rich diagnostics, JSON diagnostics, colors, recovery, or multiple-error
  reporting;
- general expression evaluation or constant folding;
- C++ keyword renaming or escaping;
- code audit;
- C++ build-system generation or multi-file output.

## Validate

From `workbench/lykn-cpp-transpiler-trial/implementation/lykn-cpp-transpiler`,
run:

```sh
cargo fmt --check
cargo check
cargo clippy -- -D warnings
cargo test
c++ -std=c++17 -Wall -Wextra -pedantic examples/generated/happy_path.cpp -o /private/tmp/lykn-cpp-transpiler-happy-path-slice02
/private/tmp/lykn-cpp-transpiler-happy-path-slice02
```

The C++ smoke binary should print `9`.

If the C++ compiler is unexpectedly unavailable, record the exact command and
blocker as a deferred environment gate. Do not silently skip it.

## Closing Report

When finished, create:

`workbench/lykn-cpp-transpiler-trial/project01-tiny-lykn-cpp-transpiler/arc01-minimum-language-core/slice02-diagnostic-hardening/closing-report.md`

The closing report must include:

- summary of files created or modified;
- validation commands and results;
- row-by-row walk for every ledger row `S02-01` through `S02-10`;
- artifact inventory;
- any deferrals or no-ops with concrete rationale and re-entry condition;
- bubble-up notes for Arc 01, including scope-as-specified versus
  scope-as-delivered and whether Arc 01 needs another slice before arc close.

Do not create `cdc-verification.md`; CDC owns that.

End your response by saying whether the slice is proposed-done and what CDC
should verify first.
