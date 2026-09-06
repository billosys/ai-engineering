# Arc 02 Slice 01: Recursive Arithmetic Core Ledger

## Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| E-1 | The AST represents recursive binary arithmetic expressions and the four operators `+`, `-`, `*`, and `/`. | `rg -n -e 'Binary' -e 'BinaryOp' -e 'Add' -e 'Subtract' -e 'Multiply' -e 'Divide' src/ast.rs` | correctness | slice-plan | done | attested: command exited 0 on 2026-09-05 and matched `src/ast.rs` lines 14, 15, 24, 25, 26, 27, 28, 31, 34, 35, 36, 37, 44, 45, 46, 47 | Keep AST small and codegen-friendly. |
| E-2 | The public API accepts arithmetic expressions in `print`, including at least one nested expression. | `cargo test arithmetic_print_expression` | correctness | slice-plan | done | attested: command exited 0 on 2026-09-05; `arithmetic_print_expression` passed with full-output equality for `(print (* (+ 1 2) 3))` | Example shape: `(print (* (+ 1 2) 3))`. |
| E-3 | The public API accepts expression-valued `let` initializers and identifier leaves inside compound expressions. | `cargo test let_arithmetic_expression` | correctness | slice-plan | done | attested: command exited 0 on 2026-09-05; `let_arithmetic_expression` passed through the public `transpile` API | Example shape: `(let x 40) (let y (+ x 2)) (print y)`. |
| E-4 | Generated C++ for arithmetic uses deterministic parenthesized infix output and preserves statement order. | `cargo test arithmetic_codegen_order` | correctness | slice-plan | done | attested: command exited 0 on 2026-09-05; `arithmetic_codegen_order` passed and compared full C++ output plus statement positions | Prefer full-output equality. |
| E-5 | Unknown or before-bound identifiers inside compound expressions are rejected with structured diagnostics. | `cargo test unknown_identifier_in_expression` | correctness | slice-plan | done | attested: command exited 0 on 2026-09-05; `unknown_identifier_in_expression` passed for nested unknown and before-bound initializer identifiers | Extends Arc 01 identifier policy into nested expressions. |
| E-6 | Malformed arithmetic expressions have structured diagnostics for unsupported operators, missing operands, or extra operands. | `cargo test malformed_expression_reports_structured_error` | correctness | slice-plan | done | attested: command exited 0 on 2026-09-05; test asserts `UnsupportedOperator`, `MissingOperand`, and `ExtraOperand` variants | Slice 02 may harden edge coverage further. |
| E-7 | Negative integer literals remain rejected while binary subtraction expressions are accepted. | `cargo test subtraction_expression_without_negative_literal` | correctness | slice-plan | done | attested: command exited 0 on 2026-09-05; binary subtraction generated `(1 - 2)` and `(print -1)` returned `InvalidInteger` | Avoids confusing unary minus with literal policy. |
| E-8 | Arc 01 literal and let-literal behavior remains supported exactly. | `cargo test print_literal && cargo test let_literal_program` | serious | arc-plan | done | attested: command exited 0 on 2026-09-05; print literal passed through library and CLI filters, and let-literal program passed through the public API | Regression protection for the closed foundation. |
| E-9 | CLI accepts a valid arithmetic program and writes the exact generated C++ to stdout with empty stderr. | `cargo test cli_arithmetic_expression` | correctness | slice-plan | done | attested: command exited 0 on 2026-09-05; `cli_arithmetic_expression_writes_cpp_to_stdout` passed full stdout equality with empty stderr | Extend `tests/cli.rs` without reintroducing temp file collisions. |
| E-10 | CLI reports at least one expression diagnostic with non-zero exit and no stdout. | `cargo test cli_expression_error` | correctness | slice-plan | done | attested: command exited 0 on 2026-09-05; `cli_expression_error_exits_nonzero_without_stdout` passed for unsupported operator `%` | Use an unsupported operator, wrong arity, or unknown nested identifier. |
| E-11 | `docs/syntax.md` documents Arc 02 Slice 01 arithmetic forms, binary arity, expression positions, and explicit deferrals. | `rg -n -e 'Arc 02' -e '\\(\\+ ' -e 'binary' -e 'negative' -e 'constant folding' docs/syntax.md` | polish | slice-plan | done | attested: command exited 0 on 2026-09-05 and matched `docs/syntax.md` lines 49, 51, 56, 60, 63, 70, 85, 88, 89, 90, 92, 93, 111, 112, 115 | Keep the syntax boundary visible for later slices. |
| E-12 | A generated arithmetic C++ example exists if CC adds one, and any added example matches the documented output style. | `test -f examples/arithmetic.cpp && rg -n -e 'int y\\{' -e 'std::cout <<' examples/arithmetic.cpp` | polish | slice-plan | done | attested: `test -f examples/arithmetic.cpp` exited 0 on 2026-09-05; `rg -n -e 'int y\\{' -e 'std::cout <<' examples/arithmetic.cpp` exited 0 and matched lines 5 and 6 | Added `examples/arithmetic.cpp`; Arc 03 still owns broad examples. |
| E-13 | Quality gates pass under the normal workspace toolchain. | `cargo fmt --check && cargo test && cargo clippy -- -D warnings` | serious | slice-plan | done | attested: command exited 0 on 2026-09-05; full tests reported 14 library tests, 6 CLI integration tests, 0 doc-tests, and clippy clean | Full `cargo test` ran normally, not only focused tests. |

## What Worked

_(At slice close. Patterns that made the slice close cleanly.)_

- The Arc 01 parser/tokenizer split accepted recursive expression parsing
  without a new dependency.
- Full-output equality tests made parenthesized infix codegen easy to verify.
- The Slice 02 CLI temp-file isolation fix carried forward, so new CLI tests
  could run safely under the normal parallel harness.

## Closure

Closed at working-tree state on 2026-09-05: parent repository commit `306dfb6`
with ignored trial workspace `workbench/lykn-cpp-transpiler-trial/` containing
the slice implementation. Verified by: CC/Sofie attestation pending CDC
verification in `cdc-verification.md`.
Rows: 13. Done: 13. Deferred: 0. No-op: 0.
