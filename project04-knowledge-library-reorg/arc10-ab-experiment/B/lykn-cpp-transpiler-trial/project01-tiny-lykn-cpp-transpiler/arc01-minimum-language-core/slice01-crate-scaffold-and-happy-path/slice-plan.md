# Arc 01 Slice 01 Plan: Crate Scaffold and Happy Path

## Goal

Create the first useful, bounded implementation slice for the trial: a Rust
crate that can transpile a tiny valid Lykn-inspired program into deterministic
C++17 and reject at least one invalid program with a structured diagnostic.

## In Scope

- Create `implementation/lykn-cpp-transpiler` as a Cargo crate.
- Use Rust 2024 edition unless the local toolchain blocks it, in which case
  record the blocker and use the smallest compatible edition.
- Implement a small AST for programs, statements, and integer expressions.
- Implement parsing for:
  - `(let name expr)`
  - `(print expr)`
  - integer literals
  - identifiers
  - prefix arithmetic `+`, `-`, `*`, `/` with two operands
- Implement deterministic C++ generation for valid programs.
- Implement `pub fn transpile_to_cpp(source: &str) -> Result<String, TranspileError>`.
- Add a thin CLI that reads one input file and writes generated C++ to stdout.
- Add fixtures:
  - at least one valid source program;
  - at least one invalid source program.
- Add unit or integration tests for the happy path and first invalid path.
- Add one generated C++ example under the crate, preferably
  `examples/generated/happy_path.cpp`.

## Out Of Scope

- Full Lykn parsing or compatibility.
- JavaScript output or semantics.
- Infix expressions.
- Functions, conditionals, loops, strings, arrays, objects, imports, modules,
  macros, comments, source maps, or runtime support.
- Rich CLI options such as `-o`, JSON diagnostics, colors, stdin, or config.
- C++ compilation as a required gate if no C++17 compiler is available.
- Code audit.

## Verification Approach

CC should run:

- `cargo fmt --check`
- `cargo check`
- `cargo clippy -- -D warnings`
- `cargo test`

CC should also inspect generated C++ for the approved subset:

- `#include <iostream>`
- `int main()`
- `const int` locals with brace initialization;
- `std::cout << ... << "\\n";`
- `return 0;`

CDC will later independently rerun these checks, inspect the diff, count ledger
rows, compare source as delivered against scope as specified, and create
`cdc-verification.md` only if the evidence reproduces.

## Exit Criteria

All slice ledger rows must reach final status in CC's closing report with
attested evidence. The slice remains proposed-done until CDC independently
verifies the rows.

Artifacts: source code, fixtures, tests, and generated examples should be
created under `implementation/lykn-cpp-transpiler`. No separate slice
`artifacts/` directory is required for Slice 01.
