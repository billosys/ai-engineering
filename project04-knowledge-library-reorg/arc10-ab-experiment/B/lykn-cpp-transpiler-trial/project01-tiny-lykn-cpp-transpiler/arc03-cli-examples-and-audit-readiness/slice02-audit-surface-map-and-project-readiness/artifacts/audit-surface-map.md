# Audit Surface Map: Tiny Lykn-Inspired C++ Transpiler

Run label: `framework-main-pre-0.5.0`

Implementation root:
`/Users/oubiwann/lab/billosys/ai-engineering/workbench/lykn-cpp-transpiler-trial/implementation/lykn-cpp-transpiler`

This is an audit-readiness map only. It does not perform the later
diagnosis-only code audit and does not record findings.

## Audit Boundary

In scope for the later audit:

- first-party Rust crate metadata and source;
- public Rust library API;
- Rust binary CLI boundary;
- AST, parser, codegen, and structured error modules;
- valid and invalid Lykn-inspired fixtures;
- Rust integration tests;
- generated C++17 examples committed under `examples/generated/`;
- validation commands and their expected evidence surfaces.

Out of scope for the later audit unless a reviewer explicitly expands scope:

- crate-local `target/` build outputs;
- `/private/tmp/lykn-cpp-transpiler-*` smoke binaries;
- Rust toolchain internals;
- generated test binaries under `target/debug/deps`;
- package/release artifacts, because this trial is not a release slice.

## First-Party Rust Source

Manifest and lint surface:

- `Cargo.toml`: package name, version, Rust 2024 edition, `rust-version =
  "1.85"`, MIT license, `unsafe_code = "forbid"`, and clippy denies
  `unwrap_used` and `expect_used`.

Library/API surface:

- `src/lib.rs`: public crate entrypoint and exported errors.
- Public API contract:
  `pub fn transpile_to_cpp(source: &str) -> Result<String, TranspileError>`.
- Public error exports:
  `pub use error::{CodegenError, ParseError, TranspileError};`.

Internal implementation surfaces:

- `src/ast.rs`: internal `Program`, `Statement`, `Expr`, and
  `BinaryOperator` tree; accepted statements are `Let` and `Print`; accepted
  expression shapes are integer, identifier, and binary expression.
- `src/parser.rs`: lexer and recursive parser; accepts only top-level
  parenthesized `let` and `print` forms plus binary `+`, `-`, `*`, `/`
  expressions; validates identifiers and integer range.
- `src/codegen.rs`: deterministic C++17 text generator; tracks bindings with
  `BTreeSet`; rejects duplicate bindings, unknown identifiers, and direct
  literal division by zero; emits one complete source file.
- `src/error.rs`: public structured diagnostic types and `Display`/`Error`
  implementations.
- `src/main.rs`: thin CLI wrapper; accepts exactly one input path, writes
  generated C++ to stdout, writes usage/read/transpile diagnostics to stderr,
  and returns exit code `0`, `1`, or `2`.

Rust audit guidance likely relevant to these surfaces:

- public API and error typing;
- panic/unwrap handling on user input;
- crate and binary layout;
- CLI stdout/stderr/exit contracts;
- deterministic test and fixture structure.

## Generated C++ Examples

Generated examples are durable example outputs, not first-party handwritten C++
implementation logic:

- `examples/generated/happy_path.cpp`
- `examples/generated/arithmetic_mix.cpp`

Generated C++ subset commitments:

- includes only `#include <iostream>`;
- emits one `int main()`;
- uses `const int` local bindings;
- uses brace initialization for generated locals;
- uses `std::cout << ... << "\n";`;
- emits `return 0;`;
- parenthesizes binary expressions;
- does not emit raw pointers, references, classes, templates, macros, dynamic
  allocation, casts, exceptions, headers, or multi-file output.

C++ audit guidance likely relevant to these surfaces:

- simple scoped locals and const-by-default;
- standard-library I/O;
- initialization style;
- integer arithmetic edge cases;
- generated-code subset drift.

## Fixtures

Valid fixtures:

- `fixtures/valid/happy_path.lykn`
- `fixtures/valid/arithmetic_mix.lykn`

Invalid fixtures:

- `fixtures/invalid/binary_too_few_operands.lykn`
- `fixtures/invalid/binary_too_many_operands.lykn`
- `fixtures/invalid/cpp_reserved_word.lykn`
- `fixtures/invalid/division_by_zero.lykn`
- `fixtures/invalid/duplicate_binding.lykn`
- `fixtures/invalid/hyphenated_identifier.lykn`
- `fixtures/invalid/integer_overflow.lykn`
- `fixtures/invalid/malformed_expression.lykn`
- `fixtures/invalid/malformed_top_level.lykn`
- `fixtures/invalid/missing_let_expression.lykn`
- `fixtures/invalid/missing_print_expression.lykn`
- `fixtures/invalid/missing_top_level_close_paren.lykn`
- `fixtures/invalid/reserved_double_underscore.lykn`
- `fixtures/invalid/reserved_upper_underscore.lykn`
- `fixtures/invalid/trailing_non_form_token.lykn`
- `fixtures/invalid/unsupported_expression_operator.lykn`
- `fixtures/invalid/unsupported_form.lykn`
- `fixtures/invalid/use_before_binding_in_let.lykn`

Fixture contract:

- Valid fixtures must remain within the accepted subset.
- Invalid fixtures are negative coverage for malformed syntax, unsupported
  forms/operators, invalid or unsafe identifiers, integer overflow, duplicate
  bindings, unknown identifiers, and direct literal division by zero.

## Tests

Integration tests:

- `tests/transpile.rs`: exact valid-output comparisons and structured
  diagnostic checks, plus earlier CLI smoke coverage.
- `tests/diagnostic_matrix.rs`: table-driven coverage for remaining invalid
  diagnostic boundaries.
- `tests/cli.rs`: focused CLI success, diagnostic failure, and usage failure
  behavior.

Test contracts:

- generated output is exact-match deterministic text;
- diagnostics are structured enum values for library callers;
- CLI keeps generated C++ on stdout and diagnostics on stderr;
- CLI exits successfully only on valid transpilation.

## Transient Outputs

Crate-local build outputs:

- `target/`
- examples observed: `target/.rustc_info.json`, `target/debug/`, compiled
  test binaries, `.d` dependency files, `.cargo-*` lock files.

Temporary smoke binaries:

- `/private/tmp/lykn-cpp-transpiler-happy-path-arc03-slice01`
- `/private/tmp/lykn-cpp-transpiler-arithmetic-mix-arc03-slice01`
- `/private/tmp/lykn-cpp-transpiler-happy-path-arc03-slice01-cdc`
- `/private/tmp/lykn-cpp-transpiler-arithmetic-mix-arc03-slice01-cdc`
- `/private/tmp/lykn-cpp-transpiler-happy-path-arc03-slice02`
- `/private/tmp/lykn-cpp-transpiler-arithmetic-mix-arc03-slice02`

These are validation byproducts, not durable source or planning artifacts.

## Cross-Cutting Contracts For Later Audit

Public library API:

- `transpile_to_cpp(&str) -> Result<String, TranspileError>` is the crate's
  public behavior boundary.

Accepted syntax:

- top-level `(let name expr)`;
- top-level `(print expr)`;
- integer literals fitting `i32`;
- identifiers accepted by the C++-safe identifier rules;
- binary prefix arithmetic `(+ a b)`, `(- a b)`, `(* a b)`, and `(/ a b)`;
- no functions, loops, strings, modules, comments, imports, arrays, objects,
  mutation, or full Lykn compatibility.

Structured diagnostics:

- `TranspileError::Parse(ParseError)`;
- `TranspileError::Codegen(CodegenError)`;
- parse diagnostics: unexpected end/token, unsupported form, binary arity,
  invalid identifier, unsafe identifier, invalid integer;
- codegen diagnostics: duplicate binding, unknown identifier, direct literal
  division by zero.

CLI behavior:

- exactly one input path is accepted;
- successful transpilation writes generated C++ to stdout and exits `0`;
- usage errors write usage to stderr and exit `2`;
- read/transpile errors write diagnostics to stderr and exit `1`;
- stdout remains empty on diagnostic failures.

Generated output:

- output is one deterministic C++17 source file;
- binary expressions are parenthesized;
- generated locals are `const int` with brace initialization;
- C++ subset avoids features explicitly outside the trial scope.

Validation gates:

- `cargo fmt --check`;
- `cargo check`;
- `cargo clippy -- -D warnings`;
- `cargo test`;
- `c++ -std=c++17 -Wall -Wextra -pedantic` for each generated example;
- direct source/evidence inspection with `find` and `rg`.

## Source Inventory Command

Observed command:

```bash
find src tests fixtures examples -maxdepth 3 -type f | sort
```

Observed output:

```text
examples/generated/arithmetic_mix.cpp
examples/generated/happy_path.cpp
fixtures/invalid/binary_too_few_operands.lykn
fixtures/invalid/binary_too_many_operands.lykn
fixtures/invalid/cpp_reserved_word.lykn
fixtures/invalid/division_by_zero.lykn
fixtures/invalid/duplicate_binding.lykn
fixtures/invalid/hyphenated_identifier.lykn
fixtures/invalid/integer_overflow.lykn
fixtures/invalid/malformed_expression.lykn
fixtures/invalid/malformed_top_level.lykn
fixtures/invalid/missing_let_expression.lykn
fixtures/invalid/missing_print_expression.lykn
fixtures/invalid/missing_top_level_close_paren.lykn
fixtures/invalid/reserved_double_underscore.lykn
fixtures/invalid/reserved_upper_underscore.lykn
fixtures/invalid/trailing_non_form_token.lykn
fixtures/invalid/unsupported_expression_operator.lykn
fixtures/invalid/unsupported_form.lykn
fixtures/invalid/use_before_binding_in_let.lykn
fixtures/valid/arithmetic_mix.lykn
fixtures/valid/happy_path.lykn
src/ast.rs
src/codegen.rs
src/error.rs
src/lib.rs
src/main.rs
src/parser.rs
tests/cli.rs
tests/diagnostic_matrix.rs
tests/transpile.rs
```

## Suggested Later Audit Passes

A later diagnosis-only audit should inspect, at minimum:

1. Rust crate/API/CLI/test audit over `Cargo.toml`, `src/`, `tests/`, and
   fixtures.
2. Generated C++ subset audit over `examples/generated/*.cpp` and the Rust
   codegen that produces them.
3. Cross-contract audit comparing project-plan language boundaries,
   parser/codegen behavior, fixture coverage, CLI behavior, and generated
   examples.

Do not treat this map as a finding report. It is only the scope substrate for
that later audit.
