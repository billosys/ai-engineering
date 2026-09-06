# Audit Readiness Map

Status: ready for audit, audit not yet performed.

This map is an entrypoint for a later code audit of the tiny Lykn-inspired to
C++17 transpiler. It identifies what to read, what each surface owns, how to
reproduce the current evidence, and where the project boundary ends. It does
not perform the audit, assign severity, or record audit findings.

## Accepted Scope

Accepted tiny-language inputs are ordered parenthesized statements:

- `(print expr)`
- `(let name expr)`

Accepted expressions are base-10 non-negative integer literals,
already-bound identifiers, and recursive binary prefix arithmetic:

- `(+ left right)`
- `(- left right)`
- `(* left right)`
- `(/ left right)`

Generated C++ is one C++17 translation unit using `#include <iostream>`,
`int main()`, local `int` variables, `std::cout << ... << "\n";`, and
`return 0;`.

## Non-goals And Later Audit Boundary

Non-goals include full Lykn compatibility, JavaScript behavior, type inference
beyond `int`, negative integer literals, unary operators, variadic arithmetic,
constant folding, runtime evaluation, division-by-zero analysis, strings,
comments, functions, conditionals, loops, imports, source maps, generated build
systems, and multi-file C++ output.

Out of scope for this map: performing the later audit, writing severity-ranked
findings, and creating `workbench/YYYY.MM.DD-audit-*` reports. A later audit
should use this map as orientation, then apply `docs/CODE-AUDIT.md` from the
assigned framework root.

## Source Surface Map

| Audit topic | Read | Surface ownership |
|-------------|------|-------------------|
| Parser | `src/parser.rs` | Tokenizes source text, parses ordered statements and expressions, enforces statement shape, exact binary arithmetic arity, identifier policy, integer literal range, duplicate binding rejection, and bind-before-use semantics. |
| AST | `src/ast.rs` | Defines the internal AST: `Program`, `Stmt`, `Expr`, and `BinaryOp`. The AST is deliberately small and private to the crate. |
| Public API | `src/lib.rs` | Exposes `transpile(source: &str) -> Result<String, TranspileError>` and `transpile_file(path) -> Result<String, CliError>`, plus library tests for accepted output and structured error variants. |
| CLI | `src/main.rs` | Thin CLI boundary: one source-file argument, C++ output to stdout, usage and diagnostics to stderr, exit code 0 for success, 1 for transpile/read failures, and 2 for usage errors. |
| Diagnostics | `src/error.rs`, `src/parser.rs`, `tests/fixtures/invalid/`, `tests/cli.rs`, `src/lib.rs` | `TranspileError` is the typed diagnostic contract. Parser error paths produce structured variants, invalid fixtures exercise representative failures, CLI tests assert stderr behavior, and library tests assert exact variants. |
| Code generation | `src/codegen.rs`, `examples/*.cpp`, `tests/fixtures/expected/*.cpp` | Emits deterministic C++ output with parenthesized infix arithmetic, local `int` initializers, print statements, and one `main` function. Expected fixtures and examples pin the C++ shape. |
| Fixture and test substrate | `tests/fixtures/valid/`, `tests/fixtures/invalid/`, `tests/fixtures/expected/`, `tests/fixtures/README.md`, `tests/cli.rs`, `src/lib.rs` | Valid fixtures define accepted programs, invalid fixtures define rejected programs, expected fixtures pin generated C++, CLI tests run real files through the binary, and library tests assert API behavior directly. |

## Diagnostic Contract Pointers

Start with `src/error.rs` for the available diagnostic variants:
`EmptyInput`, `DuplicateBinding`, `InvalidIdentifier`, `UnexpectedEnd`,
`UnexpectedToken`, `UnsupportedOperator`, `MissingOperand`, `ExtraOperand`,
`UnsupportedForm`, `InvalidInteger`, and `UnknownIdentifier`.

Then inspect `src/parser.rs` for where those variants are produced:

- `tokenize` rejects empty input.
- `parse_statement` rejects unsupported top-level forms.
- `parse_let_statement` validates names and duplicate bindings.
- `parse_expr` routes atoms and parenthesized arithmetic expressions.
- `parse_arithmetic_expr` rejects unsupported arithmetic operators, missing
  operands, extra operands, and missing closing parentheses.
- `parse_atom_expr` rejects invalid integers, invalid identifiers, unknown
  identifiers, and identifiers used before binding.

Use `tests/fixtures/invalid/` and `cli_invalid_fixtures` in `tests/cli.rs` for
end-to-end diagnostic examples. Use the structured error tests in `src/lib.rs`
for exact variant expectations.

## Generated C++ Pointers

Read `src/codegen.rs` first. Its output contract is intentionally narrow:

- a fixed include and `int main()`;
- one statement emitted per accepted source statement, preserving order;
- `int name{expr};` for `let`;
- `std::cout << expr << "\n";` for `print`;
- fully parenthesized infix output for binary arithmetic.

Examples in `examples/` are generated C++ surfaces suitable for compiler
checks. Expected outputs in `tests/fixtures/expected/` are exact CLI stdout
fixtures for accepted source programs.

## Reproduction Commands

Run these from the crate root:

```sh
cargo test cli_valid_fixtures
cargo test cli_invalid_fixtures
cargo test generated_cpp_examples_compile
cargo test generated_cpp_example_runs
cargo fmt --check
cargo test
cargo clippy -- -D warnings
```

For regression confidence across previous arcs:

```sh
cargo test print_literal
cargo test let_literal_program
cargo test full_tiny_subset_program
cargo test cli_full_tiny_subset_program
```

## Audit Starting Points

1. Confirm the project boundary in this file and `docs/syntax.md`.
2. Review `src/ast.rs` and `src/parser.rs` together so parse-time semantics are
   checked against the actual AST shape.
3. Review `src/error.rs` before evaluating parser diagnostics.
4. Review `src/codegen.rs` against `tests/fixtures/expected/*.cpp` and
   `examples/*.cpp`.
5. Review `src/lib.rs` and `tests/cli.rs` for API and CLI coverage gaps.
6. Run the reproduction commands above before writing any audit findings.
