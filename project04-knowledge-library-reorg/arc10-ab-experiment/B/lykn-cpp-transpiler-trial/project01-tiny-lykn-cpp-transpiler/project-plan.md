# Project 01: Tiny Lykn-Inspired C++ Transpiler

Metadata:

| Field | Value |
| --- | --- |
| project | project01-tiny-lykn-cpp-transpiler |
| status | closed |
| depends-on | none |
| blocks | later framework-effectiveness audit pass |
| related | framework-main-pre-0.5.0; `/Users/oubiwann/lab/lykn/lang/docs/guides/`; Rust and C++ domain skills |

## Run Setup

Run label: `framework-main-pre-0.5.0`.

Framework entrypoint used for this plan:
`/Users/oubiwann/lab/billosys/ai-engineering/knowledge/collaboration-framework/SKILL.md`.

Layout note: the assigned framework's default planning layout uses an orphan
`planning` worktree and `projectNN-<slug>` directories. The trial prompt
explicitly overrides file placement to the experiment workspace
`/Users/oubiwann/lab/billosys/ai-engineering/workbench/lykn-cpp-transpiler-trial`,
so this packet uses a canonical `project01-...` planning directory inside that
workspace. Implementation work is reserved for
`workbench/lykn-cpp-transpiler-trial/implementation/lykn-cpp-transpiler`.

Assumptions:

- This is a small experiment project, not a package release for the
  `ai-engineering` repository.
- Planning and implementation both live under the experiment workspace because
  the prompt explicitly says to place created files there.
- The tiny language is Lykn-inspired, not Lykn-compatible. It uses
  S-expression syntax and the ideas behind Lykn `bind` and `console:log`, but
  exposes trial-specific `(let name expr)` and `(print expr)` forms because the
  trial scope asks for integer `let` bindings and `print` statements.
- The first implementation slice may create the Rust crate; CDC will verify
  it later and must not treat CC's closing report as independent evidence.

## Project Goal

Build a small Rust implementation of a compiler/transpiler from a tiny
Lykn-inspired source language to one deterministic C++17 source file.

The project should produce enough real implementation surface for a later code
audit: parser and AST code, code generation code, structured errors, a library
API plus thin CLI, valid and invalid fixtures, tests, and generated C++
examples.

## Non-Goals

- Full Lykn compatibility.
- JavaScript semantics.
- C++ classes, templates, headers, pointers, references, ownership modelling,
  exceptions, build-system generation, optimization, multi-file C++ output, or
  broad formatting work.
- Type inference beyond treating every accepted expression as `int`.
- Functions, conditionals, loops, strings, arrays, objects, imports, modules,
  macros, comments, source maps, or runtime support.

## Target Language Shape

Accepted source forms:

```lykn
(let x 1)
(let y (+ x 2))
(print (* y 3))
```

Expressions:

- integer literals;
- identifiers;
- prefix arithmetic forms: `(+ a b)`, `(- a b)`, `(* a b)`, `(/ a b)`;
- parenthesized forms only; no infix syntax in the initial language.

Generated C++17:

```cpp
#include <iostream>

int main() {
    const int x{1};
    const int y{(x + 2)};
    std::cout << (y * 3) << "\n";
    return 0;
}
```

Guideline commitments:

- Use `const int` local variables for generated bindings unless a later slice
  deliberately adds mutation.
- Use brace initialization for generated locals.
- Use `std::cout << ... << "\n";`, not `std::endl`.
- Emit no raw pointers, references, classes, templates, macros, dynamic
  allocation, casts, or exception-handling constructs.
- Parenthesize generated binary expressions to keep precedence explicit.

## Rust Crate Shape

Expected crate directory:
`workbench/lykn-cpp-transpiler-trial/implementation/lykn-cpp-transpiler`.

Planned shape:

- `Cargo.toml` with Rust 2024 edition.
- `src/lib.rs` containing the public library API.
- `src/main.rs` as a thin CLI wrapper.
- `src/ast.rs`, `src/parser.rs`, `src/codegen.rs`, and `src/error.rs` or an
  equivalent small module split.
- `tests/` for integration behavior.
- `fixtures/valid/` and `fixtures/invalid/`.
- `examples/generated/` for one or two generated C++ files.

The preferred API is a simple fallible function such as:

```rust
pub fn transpile_to_cpp(source: &str) -> Result<String, TranspileError>
```

The CLI should initially accept an input path and write generated C++ to
stdout, with non-zero exit on diagnostics.

## Validation Gates

Expected local gates by project close:

- `cargo fmt --check`
- `cargo check`
- `cargo clippy -- -D warnings`
- `cargo test`
- fixture checks for valid and invalid source programs
- generated C++ snapshot comparison or equivalent deterministic-output tests
- at least one generated C++ example compiled with a C++17 compiler if one is
  available in the environment; otherwise record the exact missing-tool blocker

## How References Are Used

Lykn guides are used only to borrow surface language cues: S-expressions,
immutable binding by default, typed-number discipline as inspiration, and
`console:log` as the source idea behind trial `print`.

Rust guidance is used to keep implementation idiomatic: conventional Cargo
layout, library/binary separation, structured error types for library paths,
recoverable parse/codegen failures as `Result`, and no panic/unwrap paths for
user input.

C++ guidance is used to constrain generated output: standard-library-first I/O,
simple scoped locals, initialized immutable values, explicit expression
parentheses, and avoidance of C++ features outside this trial's subset.

## Arc Roadmap

| Arc | Status | Capability | Depends On |
| --- | --- | --- | --- |
| Arc 01: Minimum Language Core | closed | Establish crate shape, AST/parser/codegen skeleton, happy-path transpilation, fixtures, and first diagnostics. | none |
| Arc 02: Diagnostics and Negative Coverage | closed | Harden the remaining diagnostic and negative-coverage boundaries not already absorbed by Arc 01 Slice 02; was: harden malformed expression, unknown identifier, unsupported syntax, and divide-by-zero diagnostic behavior with targeted tests. | Arc 01 |
| Arc 03: CLI, Examples, and Audit Readiness | closed | Make the thin CLI comfortable, add a second generated C++ example, keep C++17 smoke verification explicit, and prepare an audit surface map. | Arc 02 |

Do not exceed these three arcs without recording a specific scope-change reason.

## Project Definition of Done

The project is ready for the later code-audit pass when all project ledger rows
are closed with independently reproduced or reconciled evidence, Arc 03 has
closed, and CDC has confirmed that the resulting codebase has enough real
surface for parser/API/error/codegen/test audit findings.

## Current Status

Project 01 is formally closed. Arc 01, Arc 02, and Arc 03 are closed; the
project ledger is closed with reproduced/reconciled evidence; the final
read-only Rust self-audit artifact is present at `rust-self-audit-report.md`;
and no fourth arc is currently indicated.

## Version History

| Version | Date | Change |
| --- | --- | --- |
| 1.9 | 2026-09-05 | Recorded formal project close after all three arcs closed and the read-only Rust self-audit artifact landed; no fourth arc indicated. |
| 1.8 | 2026-09-05 | Recorded formal Arc 03 close and project eligibility for close/readiness assessment; no fourth arc indicated. |
| 1.7 | 2026-09-05 | Opened Arc 03 Slice 02 for audit surface mapping and project-readiness evidence. |
| 1.6 | 2026-09-05 | Recorded Arc 03 Slice 01 CDC closure; no project roadmap change required. |
| 1.5 | 2026-09-05 | Recorded formal Arc 02 close and opened Arc 03 plus Arc 03 Slice 01. |
| 1.4 | 2026-09-05 | Recorded Arc 02 Slice 01 CDC closure and eligibility for formal Arc 02 close. |
| 1.3 | 2026-09-05 | Recorded formal Arc 01 close and narrowed Arc 02 around remaining diagnostic coverage because Arc 01 Slice 02 already delivered the basic diagnostic-hardening roadmap items. |
| 1.2 | 2026-09-05 | Recorded Arc 01 Slice 02 CDC closure and eligibility for formal Arc 01 close. |
| 1.1 | 2026-09-05 | Opened Arc 01 Slice 02 after Slice 01 CDC verification; status-only update with no roadmap expansion. |
| 1.0 | 2026-09-05 | Initial CDC project plan for the `framework-main-pre-0.5.0` trial. |
