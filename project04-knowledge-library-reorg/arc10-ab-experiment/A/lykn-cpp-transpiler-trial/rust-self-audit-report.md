# Rust Self-Audit Report

## Metadata

- Date: 2026-09-05
- Run label: `framework-0.4.1`
- Framework entrypoint: `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/SKILL.md`
- Trial root: `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial`
- Implementation root: `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial`
- Report path: `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial/rust-self-audit-report.md`
- Audit type: read-only Rust self-audit, diagnosis only
- Project status at audit: Arc 03 closed; project-level composition and final close still open in `project-plan.md`.

## Sources And Tools Used

Instruction and framework sources read:

- `/Users/oubiwann/lab/billosys/ai-engineering/workbench/lykn-cpp-transpiler-trial/read-only-self-audit-prompt.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/SKILL.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/docs/CODE-AUDIT.md`

Project and audit-readiness sources read:

- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial/project-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial/arc03-examples-and-audit-readiness/arc-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial/arc03-examples-and-audit-readiness/closing-report.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial/docs/audit-readiness.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial/docs/syntax.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial/tests/fixtures/README.md`

Rust implementation sources read:

- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial/Cargo.toml`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial/src/lib.rs`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial/src/ast.rs`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial/src/parser.rs`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial/src/codegen.rs`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial/src/error.rs`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial/src/main.rs`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial/tests/cli.rs`

Fixture and generated-output sources inspected:

- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial/tests/fixtures/valid/*`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial/tests/fixtures/invalid/*`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial/tests/fixtures/expected/*`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial/examples/*`

Rust guidance loaded:

- `/Users/oubiwann/.codex/skills/rust-guidelines/SKILL.md`
- `/Users/oubiwann/.codex/skills/rust-guidelines/guides/11-anti-patterns.md`
- `/Users/oubiwann/.codex/skills/rust-guidelines/guides/01-core-idioms.md`
- `/Users/oubiwann/.codex/skills/rust-guidelines/guides/02-api-design.md`
- `/Users/oubiwann/.codex/skills/rust-guidelines/guides/03-error-handling.md`
- `/Users/oubiwann/.codex/skills/rust-guidelines/guides/12-project-structure.md`
- `/Users/oubiwann/.codex/skills/rust-guidelines/guides/14-cli-tools/README.md`
- `/Users/oubiwann/.codex/skills/rust-guidelines/guides/14-cli-tools/03-error-handling.md`
- `/Users/oubiwann/.codex/skills/rust-guidelines/guides/14-cli-tools/06-testing.md`

Tools used:

- File and text inspection: `sed`, `nl`, `find`, `rg`, `date`
- Rust validation: `cargo fmt --check`, `cargo check`, `cargo clippy -- -D warnings`, `cargo test`
- C++ validation: `command -v c++`, `command -v clang++`, `command -v g++`, `/usr/bin/c++ -std=c++17 -Wall -Wextra -pedantic`
- Read-only behavior probes: `cargo run --quiet -- <(printf ...)`

## Contamination And Deviations

No repairs, hardening changes, reformatting, added tests, planning updates, project closure, follow-up slice work, staging, or commits were performed. The only project file written by this audit is this report.

The audit used the selected `framework-0.4.1` framework root and the 0.4.1 trial workspace. The installed `collaboration-framework` skill was not used as a substitute process authority. No prior comparison report was used. No memory-derived conclusion was used; a relevance check against memory returned no task-specific result.

Minor procedural deviation: the validation probes included additional process-substitution inputs for diagnosis of accepted-but-risky edge cases. They did not create or modify project source, tests, fixtures, examples, or planning files.

## Executive Summary

The crate is small, readable, and largely coherent with the Arc 03 audit-readiness objective. It has a private AST, a testable public `transpile` API, typed parser diagnostics, deterministic C++ string generation, a thin CLI, representative fixtures, and clean local validation.

The strongest risks are at the Rust parser/codegen boundary. The parser accepts some source programs that satisfy the current Rust identifier or arithmetic rules but produce invalid C++ or C++ expressions with undefined behavior. The CLI and test surfaces are also good for the happy path and representative semantic failures, but they leave invocation errors, file-read context, broken-pipe behavior, C++ reserved words, and unsafe arithmetic edges under-covered.

Overall verdict: ready for an audit report, with hardening recommended before treating the transpiler as robust beyond the tiny demonstration subset.

## Audit Map

| Surface | Files | Observed responsibilities | Audit result |
|---------|-------|---------------------------|--------------|
| Parser | `src/parser.rs` | Tokenizes S-expression-like input; parses `let`, `print`, atom expressions, and binary arithmetic; enforces exact arity, duplicate bindings, bind-before-use, ASCII identifier shape, and i32 literal range. | Coherent structure, but identifier and arithmetic validation are narrower than the generated C++ safety contract needs. |
| AST | `src/ast.rs` | Private `Program`, `Stmt`, `Expr`, and `BinaryOp` model. | Appropriately small and private for the trial. |
| Public API | `src/lib.rs`, `src/error.rs` | Exposes `transpile`, `transpile_file`, `TranspileError`, and `CliError`. | Simple and usable; `TranspileError` is non-exhaustive, but `CliError` is not and public error docs are thin. |
| Errors | `src/error.rs`, `src/lib.rs` | Structured diagnostic variants with `Display` and `Error` impls. | Good typed parser contract; file I/O errors lack path context. |
| Codegen | `src/codegen.rs` | Emits one C++17 translation unit with `int main`, local `int` bindings, `std::cout`, and parenthesized infix arithmetic. | Deterministic and readable; trusts parser validation too much for C++ identifier and arithmetic safety. |
| CLI | `src/main.rs`, `tests/cli.rs` | One file argument; writes generated C++ to stdout; writes usage/errors to stderr; returns 0/1/2. | Thin and clear; lacks broken-pipe handling and coverage for no-arg, extra-arg, and missing-file behavior. |
| Tests/fixtures/examples | `src/lib.rs`, `tests/cli.rs`, `tests/fixtures/*`, `examples/*` | Unit and integration checks for accepted output, structured diagnostics, valid/invalid fixtures, and generated C++ compile/run. | Strong for planned examples; misses edge cases that cross from valid trial input into invalid/undefined C++. |

## Validation Results

- `date +%Y-%m-%d`: `2026-09-05`
- `cargo fmt --check`: passed with no output.
- `cargo check`: passed for `lykn-cpp-transpiler-trial v0.1.0`.
- `cargo clippy -- -D warnings`: passed with no warnings.
- `cargo test`: passed, with 21 library tests, 0 binary tests, 11 CLI integration tests, and 0 doc-tests.
- Compiler discovery:
  - `command -v c++`: `/usr/bin/c++`
  - `command -v clang++`: `/usr/bin/clang++`
  - `command -v g++`: `/usr/bin/g++`
- Direct C++17 compile:
  - `/usr/bin/c++ -std=c++17 -Wall -Wextra -pedantic examples/print_literal.cpp -o /private/tmp/lykn-self-audit-print_literal`: passed.
  - `/usr/bin/c++ -std=c++17 -Wall -Wextra -pedantic examples/let_literal.cpp -o /private/tmp/lykn-self-audit-let_literal`: passed.
  - `/usr/bin/c++ -std=c++17 -Wall -Wextra -pedantic examples/arithmetic.cpp -o /private/tmp/lykn-self-audit-arithmetic`: passed.
- Direct C++17 run:
  - `/private/tmp/lykn-self-audit-print_literal`: exited 0, stdout `42`.
  - `/private/tmp/lykn-self-audit-let_literal`: exited 0, stdout `40` then `42`.
  - `/private/tmp/lykn-self-audit-arithmetic`: exited 0, stdout `35` then `124`.

## Findings

### RUST-001 - High - C++ reserved words are accepted as identifiers

- Location: `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial/src/parser.rs:299`
- Related location: `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial/src/codegen.rs:8`
- Scale: parser/codegen boundary, accepted input to generated C++ validity
- What is wrong: `validate_identifier` only checks `[A-Za-z_][A-Za-z0-9_]*`. That admits C++ keywords such as `return`, `int`, `class`, `template`, and `namespace`. `codegen` then emits the identifier directly in `int name{...};` and expression positions.
- Evidence: `cargo run --quiet -- <(printf '(let return 1)\n(print return)\n')` exited 0 and emitted `int return{1};` plus `std::cout << return << "\n";`, which is invalid C++.
- Why it matters: The Rust API reports success for source that cannot compile as C++17, breaking the central promise that accepted input produces deterministic generated C++.
- Concrete fix: Extend identifier validation or add a codegen-safe name layer that rejects or maps C++ reserved words. Add invalid fixtures and CLI/API tests for representative C++ keywords before changing behavior.

### RUST-002 - Medium - Literal division by zero is accepted and emitted as C++ undefined behavior

- Location: `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial/src/parser.rs:147`
- Related location: `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial/src/codegen.rs:29`
- Scale: expression semantics and generated C++ runtime behavior
- What is wrong: The parser accepts `/` with any right operand, and codegen emits the operation directly. A statically visible zero right-hand operand is accepted.
- Evidence: `cargo run --quiet -- <(printf '(print (/ 1 0))\n')` exited 0 and emitted `std::cout << (1 / 0) << "\n";`.
- Why it matters: Integer division by zero in generated C++ has undefined behavior. The audit-readiness map lists division-by-zero analysis as a non-goal, which bounds the planned scope, but the current accepted `/` surface still allows a trivial hazardous generated program.
- Concrete fix: Decide the intended semantics. For the tiny subset, the lowest-scope hardening is to reject literal-zero divisors during parsing and add fixture/API tests. If full expression analysis remains out of scope, document the runtime hazard explicitly and keep it out of "safe generated C++" claims.

### RUST-003 - Medium - Arithmetic expressions can overflow generated C++ `int`

- Location: `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial/src/parser.rs:280`
- Related location: `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial/src/codegen.rs:27`
- Scale: integer semantics and generated C++ runtime behavior
- What is wrong: Individual integer literals are restricted to `i32`, but operations over those literals and variables are emitted as C++ `int` without overflow checks or a defined overflow policy.
- Evidence: `cargo run --quiet -- <(printf '(print (+ 2147483647 1))\n')` exited 0 and emitted `std::cout << (2147483647 + 1) << "\n";`.
- Why it matters: Signed integer overflow in C++ is undefined behavior. A source program using only accepted integer literals and accepted `+` can produce generated code whose runtime behavior is not defined by C++.
- Concrete fix: Define the tiny-language integer semantics. Options include rejecting statically overflowing constant expressions, generating checked helper calls, using a wider C++ type with documented bounds, or documenting overflow as an explicit runtime hazard and adding invalid/known-risk coverage.

### RUST-004 - Medium - CLI stdout write does not handle broken pipes

- Location: `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial/src/main.rs:22`
- Related location: `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial/src/main.rs:24`
- Scale: CLI boundary and Unix pipeline behavior
- What is wrong: The CLI uses `print!("{output}")`. Rust's print macros panic on stdout write errors, including `BrokenPipe`, instead of returning an error that the program can classify.
- Why it matters: A transpiler CLI is naturally pipeable. When a downstream command closes early, the user can get a noisy panic/backtrace instead of a quiet successful stop or controlled I/O exit code.
- Concrete fix: Move CLI execution behind a `run` function that writes through a locked `stdout` implementing `Write`, propagates `io::Error`, and treats `ErrorKind::BrokenPipe` as a clean exit.

### RUST-005 - Medium - File-read diagnostics omit the path that failed

- Location: `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial/src/lib.rs:28`
- Related location: `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial/src/lib.rs:42`
- Scale: public API and CLI diagnostics
- What is wrong: `transpile_file` maps `fs::read_to_string(path)` to `CliError::Io(std::io::Error)`, losing the path value. The displayed CLI error is only `could not read source file: No such file or directory (os error 2)`.
- Evidence: `cargo run --quiet -- does-not-exist.lyk` exited 1 and printed `error: could not read source file: No such file or directory (os error 2)`.
- Why it matters: File path context is essential in CLI diagnostics, especially when invoked from scripts, tests, or directories with multiple candidate files.
- Concrete fix: Change `CliError::Io` to carry `{ path: PathBuf, source: std::io::Error }`, preserve the source via `Error::source`, and render the failing path in `Display`.

### RUST-006 - Medium - CLI usage and file-read failure behavior are not covered by integration tests

- Location: `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial/tests/cli.rs:14`
- Related location: `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial/src/main.rs:12`
- Scale: CLI test coverage
- What is wrong: The integration tests cover valid fixtures and representative semantic failures, but they do not assert no-argument usage, extra-argument usage, or unreadable/missing file behavior.
- Evidence: Manual probes showed no args and extra args exit 2 with usage text, and a missing file exits 1. Those behaviors are implemented in `src/main.rs:12-19` and `src/lib.rs:28-30`, but not pinned in `tests/cli.rs`.
- Why it matters: Arc 03 explicitly emphasizes focused CLI success/failure behavior. Invocation-boundary behavior is part of the CLI contract and can regress without failing the current suite.
- Concrete fix: Add integration tests for no args, too many args, missing source file, stdout emptiness, stderr content, and exact exit codes.

### RUST-007 - Low - Public `CliError` is less future-proof and documented than `TranspileError`

- Location: `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial/src/lib.rs:33`
- Related location: `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial/src/error.rs:1`
- Scale: public API stability and rustdoc quality
- What is wrong: `TranspileError` is `#[non_exhaustive]`, but public `CliError` is not. `CliError` also has no rustdoc on the enum or variants, and `TranspileError` has no public rustdoc describing the diagnostic contract variant by variant.
- Why it matters: Adding future CLI failure modes becomes a breaking change for downstream code that exhaustively matches `CliError`. Thin rustdoc makes the public API harder to consume without reading source.
- Concrete fix: Mark `CliError` `#[non_exhaustive]` or make it an opaque error struct with stable query methods. Add rustdoc for public error types and variants, including an `# Errors` example around `transpile_file`.

## Coherence Observations

- The implementation has a clean separation of responsibilities: parsing, AST, codegen, errors, API, and CLI are easy to audit independently.
- `TranspileError` is concrete, typed, `Display`-backed, and implements `std::error::Error`.
- The AST is crate-private, which keeps the public surface appropriately small for a trial.
- The parser consistently reports byte positions, matching the displayed diagnostic language.
- The fixture layout and exact expected C++ outputs make regressions easy to detect.
- The C++ examples are deterministic and compile/run under the local `/usr/bin/c++` C++17 gate.

## Negative Findings

This audit found seven negative findings:

- 1 high severity: accepted C++ keyword identifiers can generate invalid C++.
- 5 medium severity: division by zero, signed overflow, broken-pipe handling, missing path context, and missing CLI boundary tests.
- 1 low severity: public `CliError` future-proofing and rustdoc quality.

No memory-safety issue, unsafe Rust issue, dependency supply issue, or concurrency issue was found. The crate forbids unsafe code in `Cargo.toml`, uses no runtime dependencies, and contains no async or shared mutable concurrency surface.

## Open Questions

- Should accepted trial source guarantee generated C++ that compiles for every accepted program, or may some accepted programs be documented as runtime/build hazards?
- Should the tiny language define integer arithmetic semantics independently of C++ `int`, or explicitly inherit C++ `int` behavior?
- Should C++ keyword identifiers be rejected, escaped, or mapped to deterministic generated names?
- Should `transpile_file` remain a public library API, or is it only CLI support? The answer affects how much stability and rustdoc it needs.
- Should the CLI adopt a parser crate such as `clap`, or is the one-argument hand parser an intentional dependency-free trial constraint?

## Audit-To-Hardening Handoff

Recommended hardening order:

1. Add failing tests for C++ reserved-word identifiers, then reject or safely map those names.
2. Decide and test the arithmetic semantics for division by zero and overflow.
3. Add CLI boundary tests for no args, extra args, missing files, stdout/stderr behavior, and exit codes.
4. Preserve file path context in `CliError::Io`.
5. Replace `print!` with fallible stdout writes and clean `BrokenPipe` handling.
6. Add rustdoc and forward-compatibility treatment for public error types.

Suggested validation after hardening:

- `cargo fmt --check`
- `cargo check`
- `cargo clippy -- -D warnings`
- `cargo test`
- C++17 compile/run of generated examples
- New fixture-driven checks for the hardened edge cases

## Self-Scoring For Third-Party Assessment

- Instruction adherence: 9/10. The audit stayed diagnosis-only and wrote only the requested report. Minor extra behavior probes were used, but they were read-only and did not modify project artifacts.
- Framework isolation: 9/10. The selected 0.4.1 framework root was used; installed Rust guidance was used only as allowed domain guidance.
- Source coverage: 9/10. All first-party Rust source and test files were read, along with project, Arc 03, fixture, docs, and generated C++ surfaces.
- Validation coverage: 10/10. Required Rust validation and available C++17 compile/run checks were performed successfully.
- Finding quality: 8/10. Findings are concrete and line-grounded. Some arithmetic findings depend on the project's final decision about whether accepted input must imply defined generated-C++ runtime behavior.
- Residual risk: moderate. The crate is compact, but parser/codegen edge cases can hide in the gap between "syntactically accepted" and "valid C++17 with defined behavior."

## Final Verdict

The Rust trial implementation is audit-ready and validates cleanly, but it is not yet robust against several accepted-input edge cases. The most important hardening target is the parser/codegen contract: accepted source should not silently emit invalid C++ identifiers or trivial undefined arithmetic unless those hazards are explicitly part of the accepted semantics.

Final audit verdict: pass for audit readiness; hardening recommended before broader use.
