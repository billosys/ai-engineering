# Arc 03 Slice 01: Fixtures, CLI, and C++ Gates Ledger

## Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| F-1 | Representative valid source fixtures exist for literal print, let-literal ordering, arithmetic, and the full tiny subset. | `find tests/fixtures/valid -maxdepth 1 -type f -name '*.lyk' -print | sort` | serious | slice-plan | done | attested 2026-09-05: listed `arithmetic.lyk`, `full_tiny_subset.lyk`, `let_literal_order.lyk`, and `print_literal.lyk`. | Expected fixtures are easy for auditors to inspect. |
| F-2 | Representative invalid source fixtures exist for unsupported form, duplicate binding, unsupported operator, extra operand, invalid identifier, unknown identifier, before-bound identifier, and nested missing close. | `find tests/fixtures/invalid -maxdepth 1 -type f -name '*.lyk' -print | sort` | serious | slice-plan | done | attested 2026-09-05: listed eight named invalid fixtures covering all requested behaviors. | Fixture names reveal the behavior. |
| F-3 | Expected deterministic C++ output fixtures exist for at least two valid fixture programs. | `find tests/fixtures/expected -maxdepth 1 -type f -name '*.cpp' -print | sort` | serious | operator-feedback | done | attested 2026-09-05: listed four expected C++ fixtures. | CLI fixture tests assert them exactly. |
| F-4 | CLI success tests consume fixture files and assert exact stdout plus empty stderr. | `cargo test cli_valid_fixtures` | correctness | operator-feedback | done | attested 2026-09-05: passed; `cli_valid_fixtures ... ok`. | Reads valid source and expected C++ fixtures from disk. |
| F-5 | CLI failure tests consume fixture files and assert non-zero exit, empty stdout, and diagnostic stderr. | `cargo test cli_invalid_fixtures` | correctness | operator-feedback | done | attested 2026-09-05: passed; `cli_invalid_fixtures ... ok`. | Covers eight invalid fixture programs. |
| F-6 | At least two deterministic generated C++ examples exist, or equivalent output-shape coverage is documented and tested. | `find examples -maxdepth 1 -type f -name '*.cpp' -print | sort` | polish | operator-feedback | done | attested 2026-09-05: listed `arithmetic.cpp`, `let_literal.cpp`, and `print_literal.cpp`. | Real generated examples exist. |
| F-7 | Generated C++ examples compile as C++17 when a compiler is available. | `cargo test generated_cpp_examples_compile` | serious | operator-feedback | done | attested 2026-09-05: `/usr/bin/c++` selected; test passed and compiled all three examples as C++17. | Test skips only if no compiler is detected. |
| F-8 | At least one compiled generated C++ example is run and its stdout matches the source program semantics. | `cargo test generated_cpp_example_runs` | serious | operator-feedback | done | attested 2026-09-05: `/usr/bin/c++` selected; test passed and asserted `arithmetic.cpp` stdout `35\n124\n`. | Run gate executes the compiled arithmetic example. |
| F-9 | Existing Arc 01 and Arc 02 public API and CLI behavior remain green. | `cargo test print_literal && cargo test let_literal_program && cargo test full_tiny_subset_program && cargo test cli_full_tiny_subset_program` | serious | arc-plan | done | attested 2026-09-05: all four focused filters passed. | Regression guard preserved. |
| F-10 | Documentation or a small fixture note points auditors to the fixture and example surfaces. | `rg -n -e 'tests/fixtures' -e 'examples/' docs tests/fixtures` | polish | slice-plan | done | attested 2026-09-05: matches in `docs/syntax.md` and `tests/fixtures/README.md`. | Uses small local doc surfaces. |
| F-11 | Normal Rust quality gates pass. | `cargo fmt --check && cargo test && cargo clippy -- -D warnings` | serious | slice-plan | done | attested 2026-09-05: passed; 21 library tests, 11 CLI tests, 0 doctests, clippy clean. | Full gate after focused checks. |
| F-12 | CC close report walks F-1 through F-11 and bubbles up whether Slice 02 can build the audit-readiness map from the produced surfaces. | `rg -n -e 'F-1' -e 'F-12' -e 'Bubble-up' arc03-examples-and-audit-readiness/slice01-fixtures-cli-and-cpp-gates/closing-report.md` | serious | project-management | done | attested 2026-09-05: passed; matches at closing report lines 25, 30, 39, 40, 41, and 66. | CC created closing-report; CDC creates cdc-verification. |

## What Worked

- Keeping fixture filenames behavior-oriented made the valid and invalid
  surfaces directly inspectable.
- Reusing expected C++ fixtures in CLI tests removed long duplicated output
  strings from the fixture-driven path.
- The existing examples were already deterministic generated C++ surfaces, so
  this slice could add compile/run tests without changing language behavior.
