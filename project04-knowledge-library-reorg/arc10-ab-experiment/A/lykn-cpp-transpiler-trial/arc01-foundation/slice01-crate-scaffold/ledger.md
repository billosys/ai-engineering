# Arc 01 Slice 01: Crate Scaffold Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| F-1 | The experiment workspace contains a Rust package with `Cargo.toml`, `src/lib.rs`, and `src/main.rs`. | `test -f Cargo.toml && test -f src/lib.rs && test -f src/main.rs` | serious | slice-plan | done | attested: command exited 0 on 2026-09-05 from `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial`; parent repo state `306dfb6` plus ignored workbench files | Run from `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial`. |
| F-2 | A syntax note records that the trial uses `(let ...)` and `(print ...)`, mapped from Lykn's `bind` and `console:log` family, with prefix arithmetic reserved for later slices. | `rg -n -e bind -e 'console:log' -e '\\(print' -e '\\(let' -e prefix docs/syntax.md` | correctness | slice-plan | done | attested: command exited 0 on 2026-09-05 and matched `docs/syntax.md` lines 9, 15, 19, 20, 24, 27, 28, 36 | The note prevents accidental full-Lykn scope creep and explicitly defers `let`, identifiers, and arithmetic for later slices. |
| F-3 | The library exposes a testable `transpile(source: &str) -> Result<String, TranspileError>` API. | `rg -n "pub fn transpile\\(source: &str\\) -> Result<String, TranspileError>" src` | serious | slice-plan | done | attested: command exited 0 on 2026-09-05 and matched `src/lib.rs:17` | Public error type is re-exported from `src/lib.rs`; parser/codegen remain internal modules. |
| F-4 | `(print 42)` generates deterministic C++17 output with iostream, `int main()`, `std::cout`, newline string, and `return 0;`. | `cargo test print_literal` | serious | slice-plan | done | attested: command exited 0 on 2026-09-05; 1 matching library test and 1 matching CLI integration test passed | Test compares the full generated C++ string, not only non-empty output. |
| F-5 | The CLI reads a source file and writes generated C++ to stdout. | `cargo test cli_print_literal` | correctness | slice-plan | done | attested: command exited 0 on 2026-09-05; `cli_print_literal_writes_cpp_to_stdout` passed | Used `std::process::Command` with Cargo's test-provided binary path instead of `assert_cmd` to avoid network dependency additions. |
| F-6 | Unsupported or malformed input produces a structured diagnostic instead of a panic. | `cargo test unsupported_input` | correctness | slice-plan | done | attested: command exited 0 on 2026-09-05; library and CLI unsupported-input tests passed | `(let x 42)` returns `TranspileError::UnsupportedForm` and CLI stderr contains `error: unsupported form `let``. |
| F-7 | The slice adds one generated C++ example for `(print 42)`. | `test -f examples/print_literal.cpp && rg -n 'std::cout << 42 << "\\n";' examples/print_literal.cpp && rg -n 'return 0;' examples/print_literal.cpp` | polish | slice-plan | done | attested: command exited 0 on 2026-09-05 and matched `examples/print_literal.cpp:4` and `:5` | Generated example checked in as `examples/print_literal.cpp`. |
| F-8 | Rust formatting, tests, and warning-oriented checks pass. | `cargo fmt --check && cargo test && cargo clippy -- -D warnings` | serious | slice-plan | done | attested: command exited 0 on 2026-09-05; unit tests 2 passed, CLI integration tests 2 passed, doc-tests 0, clippy finished clean | Clippy was available in the active toolchain; no deferral needed. |

## What Worked

- Keeping the parser, AST, codegen, and CLI boundary separate made each ledger row directly testable.
- Avoiding external dependencies kept the crate buildable in the restricted network environment while still exercising the CLI end to end.
- The narrow structured error enum gives later parser/diagnostic slices an extension point without accepting `let`, identifiers, arithmetic, or multiple statements early.

## Closure

Closed at working-tree state on 2026-09-05: parent repository commit `306dfb6` with ignored trial workspace `workbench/lykn-cpp-transpiler-trial/` containing the slice implementation. Verified by: CC/Sofie local attestation; CDC verification pending.
Rows: 8. Done: 8. Deferred: 0. No-op: 0.
