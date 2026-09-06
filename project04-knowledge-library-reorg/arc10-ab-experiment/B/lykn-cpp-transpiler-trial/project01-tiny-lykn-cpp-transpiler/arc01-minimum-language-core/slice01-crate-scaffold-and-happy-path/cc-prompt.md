# CC Prompt: Arc 01 Slice 01

You are CC for the `framework-main-pre-0.5.0` trial project. Your job is to
implement Arc 01 Slice 01 only. Treat this slice as proposed-done until CDC
independently verifies it.

## Read First

From the ai-engineering repository root:

1. `workbench/cdc-project-prompt.md`
2. `workbench/lykn-cpp-transpiler-trial/project01-tiny-lykn-cpp-transpiler/project-plan.md`
3. `workbench/lykn-cpp-transpiler-trial/project01-tiny-lykn-cpp-transpiler/ledger.md`
4. `workbench/lykn-cpp-transpiler-trial/project01-tiny-lykn-cpp-transpiler/arc01-minimum-language-core/arc-plan.md`
5. `workbench/lykn-cpp-transpiler-trial/project01-tiny-lykn-cpp-transpiler/arc01-minimum-language-core/ledger.md`
6. `workbench/lykn-cpp-transpiler-trial/project01-tiny-lykn-cpp-transpiler/arc01-minimum-language-core/slice01-crate-scaffold-and-happy-path/slice-plan.md`
7. `workbench/lykn-cpp-transpiler-trial/project01-tiny-lykn-cpp-transpiler/arc01-minimum-language-core/slice01-crate-scaffold-and-happy-path/ledger.md`

Use only the assigned framework version named in `workbench/cdc-project-prompt.md`
if you need framework guidance. Do not borrow process rules from installed,
cached, older, newer, or remembered framework copies.

For domain guidance, use these paths if you need to reload them:

- Rust: `/Users/oubiwann/.codex/skills/rust-guidelines/SKILL.md`
- C++: `/Users/oubiwann/.codex/skills/cpp-guidelines/SKILL.md`
- Lykn guides: `/Users/oubiwann/lab/lykn/lang/docs/guides/`

## Implement Only This Slice

Create a Rust crate at:

`workbench/lykn-cpp-transpiler-trial/implementation/lykn-cpp-transpiler`

Implement a tiny Lykn-inspired transpiler with this source language:

```lykn
(let x 1)
(let y (+ x 2))
(print (* y 3))
```

Accepted forms:

- `(let name expr)`
- `(print expr)`
- integer literals
- identifiers
- prefix arithmetic `+`, `-`, `*`, `/` with exactly two operands

Generated C++17 must be one source file with:

- `#include <iostream>`
- `int main()`
- local `const int` variables with brace initialization;
- `std::cout << expr << "\\n";`
- `return 0;`

Use deterministic formatting. Parenthesize generated binary expressions.

## Rust Shape

Prefer this small shape unless the implementation reveals a better equally
small structure:

- `Cargo.toml`
- `src/lib.rs`
- `src/main.rs`
- `src/ast.rs`
- `src/parser.rs`
- `src/codegen.rs`
- `src/error.rs`
- `fixtures/valid/`
- `fixtures/invalid/`
- `examples/generated/`
- `tests/`

Expose a public library API equivalent to:

```rust
pub fn transpile_to_cpp(source: &str) -> Result<String, TranspileError>
```

Use structured errors for user input and parse/codegen failures. Do not use
`unwrap` or `expect` on user-controlled paths. Keep `main.rs` thin: parse CLI
arguments, read the input file, call the library, print C++ to stdout, print
diagnostics to stderr, and return a non-zero failure status.

## Required Tests and Fixtures

Create at least:

- one valid fixture demonstrating two `let` bindings and one `print`;
- one invalid fixture that produces a structured diagnostic;
- tests that assert valid fixture output exactly;
- tests that assert invalid input fails clearly;
- a CLI smoke test if practical within the slice.

Create one generated C++ example, preferably:

`examples/generated/happy_path.cpp`

The example should correspond to the valid fixture and should use only the
approved C++ subset.

## Out Of Scope

Do not implement functions, loops, conditionals, strings, arrays, objects,
imports, modules, macros, comments, source maps, JavaScript semantics, rich CLI
options, C++ classes, templates, headers, pointers, references, ownership
modelling, exceptions, build-system generation, optimization, or multi-file C++
output.

Do not perform the later code audit.

## Validate

From `workbench/lykn-cpp-transpiler-trial/implementation/lykn-cpp-transpiler`,
run:

```sh
cargo fmt --check
cargo check
cargo clippy -- -D warnings
cargo test
```

If a C++17 compiler is available, optionally compile the generated example and
record the command and result. If no compiler is available, record the exact
tool lookup you attempted and treat C++ compilation as a deferred environment
gate, not a silent pass.

## Closing Report

When finished, create:

`workbench/lykn-cpp-transpiler-trial/project01-tiny-lykn-cpp-transpiler/arc01-minimum-language-core/slice01-crate-scaffold-and-happy-path/closing-report.md`

The closing report must include:

- summary of source files created/modified;
- validation commands and results;
- row-by-row walk for every ledger row `S01-01` through `S01-08`;
- artifact inventory;
- any deferrals or no-ops with concrete rationale and re-entry condition;
- bubble-up notes for Arc 01, including scope-as-specified versus
  scope-as-delivered.

Do not create `cdc-verification.md`; CDC owns that.

End your response by saying whether the slice is proposed-done and what CDC
should verify first.
