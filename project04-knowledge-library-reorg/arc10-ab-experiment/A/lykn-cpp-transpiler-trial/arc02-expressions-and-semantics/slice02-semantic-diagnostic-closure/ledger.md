# Arc 02 Slice 02: Semantic And Diagnostic Closure Ledger

## Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| D-1 | A full tiny-subset program using multiple lets, expression-valued lets, expression-valued prints, all four binary operators, identifiers, literals, and nested expressions transpiles through the public API with exact deterministic C++ output. | `cargo test full_tiny_subset_program` | serious | slice-plan | done | 2026-09-05: passed; `tests::full_tiny_subset_program ... ok`; CLI test with same filter also matched and passed. | Public API acceptance pin added in `src/lib.rs`. |
| D-2 | The full tiny-subset program is covered through the CLI with exact stdout and empty stderr. | `cargo test cli_full_tiny_subset_program` | correctness | slice-plan | done | 2026-09-05: passed; `cli_full_tiny_subset_program_writes_cpp_to_stdout ... ok`. | CLI exact stdout and empty stderr asserted in `tests/cli.rs`. |
| D-3 | Empty parenthesized expressions in expression position are rejected with a structured diagnostic. | `cargo test empty_expression_reports_structured_error` | correctness | slice-plan | done | 2026-09-05: passed; `tests::empty_expression_reports_structured_error ... ok`. | Uses structured `UnexpectedToken` for `(print ())`. |
| D-4 | Missing operands and extra operands are tested across arithmetic operators, not only `+`. | `cargo test arithmetic_arity_matrix` | correctness | slice-plan | done | 2026-09-05: passed; `tests::arithmetic_arity_matrix ... ok`. | Matrix covers `+`, `-`, `*`, and `/` missing and extra operands. |
| D-5 | Missing closing parentheses in nested expressions produce structured diagnostics and do not panic. | `cargo test nested_expression_unexpected_end` | correctness | slice-plan | done | 2026-09-05: passed; `tests::nested_expression_unexpected_end ... ok`. | Asserts structured `UnexpectedEnd`. |
| D-6 | Unsupported arithmetic operators in expression position are rejected as expression/operator errors. | `cargo test unsupported_operator_matrix` | correctness | slice-plan | done | 2026-09-05: passed; `tests::unsupported_operator_matrix ... ok`. | Matrix covers `%` and `mod`. |
| D-7 | Extra operands after valid `print` and `let` expressions are rejected with structured diagnostics. | `cargo test statement_extra_operand_diagnostics` | correctness | slice-plan | done | 2026-09-05: passed; `tests::statement_extra_operand_diagnostics ... ok`. | Covers `(print 1 2)` and `(let x 1 2)`. |
| D-8 | Invalid identifiers inside arithmetic expressions are rejected structurally without code generation. | `cargo test invalid_identifier_in_expression` | correctness | slice-plan | done | 2026-09-05: passed; `tests::invalid_identifier_in_expression ... ok`. | Extends identifier policy to nested expression leaves. |
| D-9 | Unknown and before-bound identifiers inside nested expressions remain rejected after diagnostic hardening. | `cargo test unknown_identifier_in_expression` | correctness | slice-plan | done | 2026-09-05: passed; `tests::unknown_identifier_in_expression ... ok`. | Covers unknown identifier and let-initializer before-bound use. |
| D-10 | Duplicate bindings, literal print, let-literal programs, and recursive arithmetic core behavior remain supported exactly. | `cargo test duplicate_binding && cargo test print_literal && cargo test let_literal_program && cargo test arithmetic_print_expression && cargo test let_arithmetic_expression` | serious | arc-plan | done | 2026-09-05: passed; all five focused regression filters returned ok. | Protects Arc 01 and Arc 02 Slice 01 behavior. |
| D-11 | `docs/syntax.md` documents the final Arc 02 accepted subset, malformed-expression diagnostics, semantic rejection policy, and explicit Arc 03 deferrals. | `rg -n -e 'Arc 02 final' -e 'full tiny subset' -e 'missing operand' -e 'extra operand' -e 'unsupported arithmetic operator' -e 'Arc 03' docs/syntax.md` | polish | slice-plan | done | 2026-09-05: passed; terms found at docs lines 51, 93, 94, 96, 104, and 128. | Documentation now states Arc 02 final closure and Arc 03 deferrals. |
| D-12 | Any Arc 02 generated example added or changed matches the final documented output style. | `test -f examples/arithmetic.cpp && rg -n -e 'int ' -e 'std::cout <<' -e '\\(' examples/arithmetic.cpp` | polish | slice-plan | done | 2026-09-05: passed; matched `int main`, four `int` bindings, and two `std::cout` lines. | `examples/arithmetic.cpp` updated to full tiny subset output. |
| D-13 | Quality gates pass under the normal workspace toolchain. | `cargo fmt --check && cargo test && cargo clippy -- -D warnings` | serious | slice-plan | done | 2026-09-05: passed; 21 lib tests, 7 CLI tests, 0 doctests, clippy clean. | Full workspace gate run after focused checks. |

## What Worked

- Parser behavior already rejected the requested malformed expression cases with
  structured diagnostics; the slice closed by adding exact tests around that
  behavior rather than expanding parser scope.
- A single full tiny-subset fixture now anchors public API, CLI, docs, and the
  generated example.
- CLI temp-file uniqueness from Arc 01 Slice 02 Iteration 01 held under the new
  CLI coverage.

## Closure

CC proposed-done on 2026-09-05. All D-1 through D-13 rows are done with local
evidence above. No `cdc-verification.md` has been created by CC; CDC remains
responsible for independent reproduction and closure.
