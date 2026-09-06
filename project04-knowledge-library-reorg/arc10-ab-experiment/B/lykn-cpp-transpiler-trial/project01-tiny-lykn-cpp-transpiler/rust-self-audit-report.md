# Rust Self-Audit Report

## Metadata

| Field | Value |
| --- | --- |
| RUN_LABEL | framework-main-pre-0.5.0 |
| FRAMEWORK_ENTRYPOINT | `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/collaboration-framework/SKILL.md` |
| TRIAL_ROOT | `/Users/oubiwann/lab/billosys/ai-engineering/workbench/lykn-cpp-transpiler-trial` |
| PROJECT_PLAN | `/Users/oubiwann/lab/billosys/ai-engineering/workbench/lykn-cpp-transpiler-trial/project01-tiny-lykn-cpp-transpiler/project-plan.md` |
| IMPLEMENTATION_ROOT | `/Users/oubiwann/lab/billosys/ai-engineering/workbench/lykn-cpp-transpiler-trial/implementation/lykn-cpp-transpiler` |
| REPORT_PATH | `/Users/oubiwann/lab/billosys/ai-engineering/workbench/lykn-cpp-transpiler-trial/project01-tiny-lykn-cpp-transpiler/rust-self-audit-report.md` |
| Date | 2026.09.05 |
| Arc 03 confirmed closed before audit began | Yes; operator stated "Arc03 is now closed" before this audit began. |

## Sources And Tools Used

Read:

- `/Users/oubiwann/lab/billosys/ai-engineering/workbench/lykn-cpp-transpiler-trial/read-only-self-audit-prompt.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/collaboration-framework/SKILL.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/code-auditing/guides/01-audit-scope-and-map.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/code-auditing/guides/02-findings-and-severity.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/code-auditing/guides/03-scale-aware-auditing.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/code-auditing/guides/04-modernization-synthesis.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/code-auditing/guides/05-audit-to-hardening-handoff.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/project-management/guides/README.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/project-management/guides/04-closing-slices.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/project-management/guides/05-closing-arcs.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/work-verification/guides/01-ledger-discipline.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/work-verification/guides/02-evidence-strength.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/work-verification/guides/03-row-closure.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/work-verification/guides/04-silent-drop-checks.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/work-verification/guides/05-independent-verification.md`
- `/Users/oubiwann/.codex/skills/rust-guidelines/SKILL.md`
- `/Users/oubiwann/.codex/skills/rust-guidelines/guides/11-anti-patterns.md`
- `/Users/oubiwann/.codex/skills/rust-guidelines/guides/02-api-design.md`
- `/Users/oubiwann/.codex/skills/cpp-guidelines/SKILL.md`
- `/Users/oubiwann/lab/lykn/lang/docs/guides/00-lykn-surface-forms.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/workbench/lykn-cpp-transpiler-trial/project01-tiny-lykn-cpp-transpiler/project-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/workbench/lykn-cpp-transpiler-trial/project01-tiny-lykn-cpp-transpiler/ledger.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/workbench/lykn-cpp-transpiler-trial/project01-tiny-lykn-cpp-transpiler/arc03-cli-examples-and-audit-readiness/arc-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/workbench/lykn-cpp-transpiler-trial/project01-tiny-lykn-cpp-transpiler/arc03-cli-examples-and-audit-readiness/ledger.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/workbench/lykn-cpp-transpiler-trial/project01-tiny-lykn-cpp-transpiler/arc03-cli-examples-and-audit-readiness/closing-report.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/workbench/lykn-cpp-transpiler-trial/project01-tiny-lykn-cpp-transpiler/arc03-cli-examples-and-audit-readiness/slice01-cli-and-example-surface/cdc-verification.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/workbench/lykn-cpp-transpiler-trial/project01-tiny-lykn-cpp-transpiler/arc03-cli-examples-and-audit-readiness/slice02-audit-surface-map-and-project-readiness/slice-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/workbench/lykn-cpp-transpiler-trial/project01-tiny-lykn-cpp-transpiler/arc03-cli-examples-and-audit-readiness/slice02-audit-surface-map-and-project-readiness/ledger.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/workbench/lykn-cpp-transpiler-trial/project01-tiny-lykn-cpp-transpiler/arc03-cli-examples-and-audit-readiness/slice02-audit-surface-map-and-project-readiness/closing-report.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/workbench/lykn-cpp-transpiler-trial/project01-tiny-lykn-cpp-transpiler/arc03-cli-examples-and-audit-readiness/slice02-audit-surface-map-and-project-readiness/cdc-verification.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/workbench/lykn-cpp-transpiler-trial/project01-tiny-lykn-cpp-transpiler/arc03-cli-examples-and-audit-readiness/slice02-audit-surface-map-and-project-readiness/artifacts/audit-surface-map.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/workbench/lykn-cpp-transpiler-trial/project01-tiny-lykn-cpp-transpiler/arc03-cli-examples-and-audit-readiness/slice02-audit-surface-map-and-project-readiness/artifacts/project-readiness-evidence.md`
- First-party source files under `/Users/oubiwann/lab/billosys/ai-engineering/workbench/lykn-cpp-transpiler-trial/implementation/lykn-cpp-transpiler/src/`
- First-party test files under `/Users/oubiwann/lab/billosys/ai-engineering/workbench/lykn-cpp-transpiler-trial/implementation/lykn-cpp-transpiler/tests/`
- Fixtures under `/Users/oubiwann/lab/billosys/ai-engineering/workbench/lykn-cpp-transpiler-trial/implementation/lykn-cpp-transpiler/fixtures/`
- Generated examples under `/Users/oubiwann/lab/billosys/ai-engineering/workbench/lykn-cpp-transpiler-trial/implementation/lykn-cpp-transpiler/examples/generated/`

Executed:

- `date +%Y.%m.%d`
- `find ... -maxdepth ... -type f -print` for implementation file inventory
- `rg -n "transpile_to_cpp|ParseError|CodegenError|TranspileError|let|print" src tests fixtures examples`
- `rg -n "unwrap|expect|panic|unsafe|TODO|FIXME|read_to_string|DivisionByZero|non_exhaustive" src tests`
- `nl -ba` and `sed -n` source/guidance inspection commands
- `cargo fmt --check`
- `cargo check`
- `cargo clippy -- -D warnings`
- `cargo test`
- `c++ -std=c++17 -Wall -Wextra -pedantic examples/generated/happy_path.cpp -o /private/tmp/lykn-cpp-transpiler-happy-path-rust-self-audit`
- `/private/tmp/lykn-cpp-transpiler-happy-path-rust-self-audit`
- `c++ -std=c++17 -Wall -Wextra -pedantic examples/generated/arithmetic_mix.cpp -o /private/tmp/lykn-cpp-transpiler-arithmetic-mix-rust-self-audit`
- `/private/tmp/lykn-cpp-transpiler-arithmetic-mix-rust-self-audit`

## Contamination And Deviations

No disallowed cross-condition files, other trial workspaces, previous comparison reports, or external memory sources were opened or used as audit authority. The conversation history included operator/CC/CDC status context from the same trial, including the operator's confirmation that Arc 03 was closed; it was used only to establish the audit boundary. Validation commands created or reused ordinary Cargo build output under `target/` and audit-named smoke binaries under `/private/tmp`; these were treated as transient tool output, not audit artifacts. No source, test, fixture, generated C++, planning, staging, or commit changes were made.

## Executive Summary

The crate is audit-ready: it has a compact module map, structured errors, exact-output fixture coverage, CLI smoke coverage, and clean validation results across Rust and generated C++ examples. The highest-severity issues are accepted Lykn programs that can still emit C++ with undefined or terminating arithmetic behavior, especially non-literal division by zero and signed integer overflow. The dominant issue cluster is semantic safety at the Rust-to-C++ boundary: syntax and direct diagnostics are strong, while runtime arithmetic semantics remain under-specified and under-tested. Notably solid areas include no production `unwrap`/`expect`, explicit `unsafe_code = "forbid"`, focused fixture-backed negative tests, and stdout/stderr separation for the CLI.

## Audit Map

| Area | Files / Surface | Audit Notes |
| --- | --- | --- |
| Crate targets | `Cargo.toml`, `src/lib.rs`, `src/main.rs` | Library plus thin binary target; Rust 2024, MSRV 1.85, `unsafe_code = "forbid"`, `unwrap_used`/`expect_used` denied. |
| Public API | `src/lib.rs`, `src/error.rs` | Public `transpile_to_cpp(&str) -> Result<String, TranspileError>` and public structured error enums. |
| CLI entrypoint | `src/main.rs` | One positional input path, stdout for generated C++, stderr for usage/read/transpile errors. |
| Parser | `src/parser.rs` | Hand lexer/parser for top-level forms, atoms, binary expression arity, identifier validation, and integer parsing. |
| AST | `src/ast.rs` | Minimal internal AST for statements, integer/identifier/binary expressions, and four binary operators. |
| Codegen | `src/codegen.rs` | Emits deterministic C++17 with `const int` bindings and `std::cout` print statements. |
| Error module | `src/error.rs` | Structured `ParseError`, `CodegenError`, and wrapper `TranspileError` with `Display` and `Error`. |
| Tests | `tests/transpile.rs`, `tests/diagnostic_matrix.rs`, `tests/cli.rs` | Exact generated-output tests, invalid fixture diagnostics, and CLI smoke/usage/transpile-error tests. |
| Fixtures | `fixtures/valid/`, `fixtures/invalid/` | Valid happy path and arithmetic mix; invalid syntax, arity, integer, identifier, duplicate, division, and binding-order cases. |
| Generated examples | `examples/generated/happy_path.cpp`, `examples/generated/arithmetic_mix.cpp` | Treated as codegen policy outputs, not a separate C++ audit target. |
| Excluded/generated/build output | `target/`, `/private/tmp/lykn-cpp-transpiler-*-rust-self-audit` | Build and smoke-test outputs only; not durable audit artifacts. |

## Validation Results

| Command | Outcome |
| --- | --- |
| `date +%Y.%m.%d` | Passed; printed `2026.09.05`. |
| `cargo fmt --check` | Passed with no output. |
| `cargo check` | Passed; finished `dev` profile. |
| `cargo clippy -- -D warnings` | Passed; finished `dev` profile with no warnings. |
| `cargo test` | Passed; 0 lib tests, 0 main tests, 4 CLI tests, 1 diagnostic matrix test, 14 transpile tests, 0 doctests. |
| `c++ -std=c++17 -Wall -Wextra -pedantic examples/generated/happy_path.cpp -o /private/tmp/lykn-cpp-transpiler-happy-path-rust-self-audit` | Passed with no compiler output. |
| `/private/tmp/lykn-cpp-transpiler-happy-path-rust-self-audit` | Passed; printed `9`. |
| `c++ -std=c++17 -Wall -Wextra -pedantic examples/generated/arithmetic_mix.cpp -o /private/tmp/lykn-cpp-transpiler-arithmetic-mix-rust-self-audit` | Passed with no compiler output. |
| `/private/tmp/lykn-cpp-transpiler-arithmetic-mix-rust-self-audit` | Passed; printed `3`. |

## Findings

### RUST-001

- Severity: High
- Location: `/Users/oubiwann/lab/billosys/ai-engineering/workbench/lykn-cpp-transpiler-trial/implementation/lykn-cpp-transpiler/src/codegen.rs:52`
- Scale: logical unit
- What is wrong: Division-by-zero protection only rejects `Expr::Integer(0)` as the immediate right operand. Accepted programs such as `(let z 0)` followed by `(print (/ 1 z))` can generate C++ equivalent to `1 / z`.
- Why it matters: The Rust API can return `Ok(String)` for a Lykn program whose generated C++ has undefined or terminating arithmetic behavior when compiled and run. This weakens the promised diagnostic boundary because the failure moves from structured Rust errors into generated C++ runtime behavior.
- Concrete fix direction: Track constant binding values in codegen and reject known-zero divisors, or emit a checked division helper in generated C++ for non-literal divisors. Add fixture-backed tests for zero-valued bindings and zero-valued compound divisor expressions.

### RUST-002

- Severity: High
- Location: `/Users/oubiwann/lab/billosys/ai-engineering/workbench/lykn-cpp-transpiler-trial/implementation/lykn-cpp-transpiler/src/codegen.rs:57`
- Scale: logical unit
- What is wrong: Arithmetic expressions are emitted as plain `int` C++ operations even though the parser only checks that each literal individually fits in `i32`. A valid Lykn expression such as `(+ 2147483647 1)` can be emitted as signed `int` overflow.
- Why it matters: Signed integer overflow is undefined behavior in C++. The transpiler currently has no documented overflow semantics, no rejection of overflowing compound expressions, and no generated runtime guard.
- Concrete fix direction: Define integer semantics explicitly, then either perform checked constant evaluation and reject overflow, widen the generated type with checked bounds, or emit checked arithmetic helpers. Add negative fixtures for addition, subtraction, multiplication, and the `INT_MIN / -1` division edge.

### RUST-003

- Severity: Medium
- Location: `/Users/oubiwann/lab/billosys/ai-engineering/workbench/lykn-cpp-transpiler-trial/implementation/lykn-cpp-transpiler/src/parser.rs:277`
- Scale: function
- What is wrong: C++ reserved identifier screening rejects C++ keywords, names starting with `__`, and names starting with underscore plus uppercase, but it does not reject identifiers containing `__` after the first character, such as `foo__bar`.
- Why it matters: C++ reserves identifiers containing a double underscore anywhere. The transpiler can accept and emit a name that is outside the safe generated-C++ identifier subset it claims to enforce.
- Concrete fix direction: Change the reserved-identifier predicate to reject `name.contains("__")` in addition to the existing keyword and underscore-uppercase checks. Add an invalid fixture and assertion for a non-prefix double-underscore identifier.

### RUST-004

- Severity: Low
- Location: `/Users/oubiwann/lab/billosys/ai-engineering/workbench/lykn-cpp-transpiler-trial/implementation/lykn-cpp-transpiler/src/parser.rs:245`
- Scale: function
- What is wrong: `looks_numeric` treats any atom beginning with `-` as numeric-looking. An atom such as `-foo` is therefore reported as `InvalidInteger` instead of going through identifier validation and receiving the more accurate invalid-identifier diagnostic.
- Why it matters: This does not widen accepted syntax, but it makes diagnostics less precise for malformed identifier-like input. The project emphasizes structured diagnostics, so misleading error classification is a direct auditability and user-feedback gap.
- Concrete fix direction: Treat `-` as numeric only when followed by at least one ASCII digit, then add a focused invalid fixture for a dash-prefixed non-numeric atom.

### RUST-005

- Severity: Low
- Location: `/Users/oubiwann/lab/billosys/ai-engineering/workbench/lykn-cpp-transpiler-trial/implementation/lykn-cpp-transpiler/src/main.rs:33`
- Scale: executable/API
- What is wrong: The CLI read-error branch is present but not covered by `tests/cli.rs`; the CLI tests cover success, transpile diagnostics, and usage diagnostics, but not an unreadable or missing input path.
- Why it matters: File I/O is the first boundary of the binary target. A regression in exit code, stderr text, or stdout separation for read failures would not be caught by the current suite.
- Concrete fix direction: Add a CLI test that invokes the binary with a missing fixture path and asserts exit code `1`, empty stdout, and stderr containing both the path and read failure context.

### RUST-006

- Severity: Low
- Location: `/Users/oubiwann/lab/billosys/ai-engineering/workbench/lykn-cpp-transpiler-trial/implementation/lykn-cpp-transpiler/src/error.rs:22`
- Scale: public API
- What is wrong: The public error enums are exhaustive and not marked `#[non_exhaustive]`. Any future diagnostic variant added to `ParseError`, `CodegenError`, or `TranspileError` becomes a breaking API change for downstream exhaustive matches.
- Why it matters: The crate is a trial artifact now, but its public surface is already structured like a reusable library. Rust API guidance flags public error variant evolution as a common compatibility trap.
- Concrete fix direction: Either mark public error enums `#[non_exhaustive]` before publication or document that the current variant set is intentionally stable. If `#[non_exhaustive]` is added, update tests and downstream matching examples accordingly.

## Coherence Observations

- The crate has a clear narrow shape: parsing and code generation are internal modules, while callers see one fallible public function and typed errors.
- The parser's binary-expression implementation first counts operands, then retains unreachable defensive `None` branches after `found != 2`; this is not a behavioral failure, but it slightly obscures the invariant for future maintainers.
- CLI behavior is deliberately thin and local to `src/main.rs`. Given the one-argument scope, hand parsing is acceptable for this slice, though a future CLI expansion should revisit structured argument parsing.
- Diagnostics consistently use byte offsets rather than line/column spans. That is acceptable for this tiny language core, but line/column spans would become more valuable once programs grow beyond single-screen fixtures.
- The test suite strongly covers syntax and exact-output regression but is less developed around generated C++ semantic safety.

## Negative Findings

- No production `unwrap()` or `expect()` calls were found under `src/`; the only panic-based helpers found were in tests.
- No `unsafe` blocks or unsafe functions were found, and `Cargo.toml` explicitly sets `unsafe_code = "forbid"`.
- No generated C++ was emitted to stderr in the tested CLI success path; success output remained on stdout and stderr stayed empty.
- No accepted C++ keyword identifier path was found; `class` is covered by fixture-backed tests.
- No accepted prefix double-underscore or underscore-uppercase identifier path was found; `__reserved` and `_Upper` are covered by fixture-backed tests.
- No use-before-binding success path was found for either `print` expressions or `let` initializers; both are rejected through codegen binding checks.
- No duplicate binding success path was found; duplicate `let` names return structured `CodegenError::DuplicateBinding`.
- No widening of the valid examples was observed during Arc 03; valid fixtures and generated examples remain exact-output checked.

## Open Questions

- Should the Lykn integer model be specified as checked 32-bit, wrapping 32-bit, arbitrary precision, or "whatever generated C++ `int` does"? The answer determines the right fix for overflow handling.
- Should non-literal division by zero be statically rejected only when provable from constants, or should all generated division use runtime checks?
- Is an empty source file intended to be a valid no-op program? The parser currently accepts it and codegen emits a `main` that returns `0`.
- Are negative integer literals intentionally part of the surface language, or are they an accidental consequence of `i32::parse` accepting leading minus signs?
- Should public error enums be optimized for long-term external SemVer compatibility, or is this crate intentionally internal to the trial?

## Audit-To-Hardening Handoff

Suggested order:

1. Address RUST-001 and RUST-002 together by deciding and encoding integer/division semantics before changing implementation details.
2. Address RUST-003 next, because the fix is small and directly strengthens the existing C++-identifier safety promise.
3. Address RUST-004 and RUST-005 as focused diagnostic/test hardening.
4. Decide RUST-006 before any publication or downstream use of the crate API.

Tests to add or update:

- Invalid fixtures for division by a zero-valued binding and by a zero-valued compound expression if static rejection is chosen.
- Invalid fixtures for overflowing addition, subtraction, multiplication, and `INT_MIN / -1`, or generated-C++ runtime checks if runtime checking is chosen.
- Invalid fixture for `foo__bar` or equivalent non-prefix double-underscore identifier.
- Invalid fixture for `-foo` diagnostic classification.
- CLI test for a missing or unreadable input file.
- API compatibility tests or documented matching guidance if public errors become `#[non_exhaustive]`.

Validation commands to rerun:

- `cargo fmt --check`
- `cargo check`
- `cargo clippy -- -D warnings`
- `cargo test`
- `c++ -std=c++17 -Wall -Wextra -pedantic examples/generated/happy_path.cpp -o /private/tmp/lykn-cpp-transpiler-happy-path`
- `/private/tmp/lykn-cpp-transpiler-happy-path`
- `c++ -std=c++17 -Wall -Wextra -pedantic examples/generated/arithmetic_mix.cpp -o /private/tmp/lykn-cpp-transpiler-arithmetic-mix`
- `/private/tmp/lykn-cpp-transpiler-arithmetic-mix`

Items explicitly not worth changing yet:

- Do not replace the thin CLI with a full argument parser solely for the current one-input-file interface.
- Do not perform a broad C++ style modernization of generated examples outside Rust codegen policy.
- Do not refactor the AST or parser architecture merely to remove small internal redundancy unless it is part of a semantic hardening slice.
- Do not expand the language surface while closing these findings.

## Self-Scoring For Third-Party Assessment

| Measure | Score | Evidence | Notes |
| --- | --- | --- | --- |
| Framework isolation | 3 | Used the assigned main-pre-0.5.0 entrypoint and same-tree framework guides. | No other framework condition was opened. |
| Audit-map completeness | 3 | Report maps crate targets, API, CLI, parser, AST, codegen, errors, tests, fixtures, examples, and exclusions. | Build output treated as transient. |
| Source coverage | 3 | Inspected every first-party Rust source and test file under implementation root. | Fixtures/examples inspected for coverage and codegen policy. |
| Validation discipline | 3 | Ran all requested Rust gates and C++17 generated-example smoke runs. | All passed. |
| Finding specificity | 3 | Each finding includes ID, severity, path/line, scale, failure mode, impact, and fix direction. | Findings are grounded in concrete accepted or untested paths. |
| Severity calibration | 2 | High used for generated C++ undefined/runtime arithmetic behavior; Medium/Low for boundary and coverage issues. | Arithmetic scope ambiguity leaves some calibration uncertainty. |
| Rust-idiom grounding | 2 | Checked public API shape, production panic avoidance, unsafe policy, and public error evolution guidance. | Did not exhaustively quote every Rust pattern chapter. |
| Generated-C++ boundary handling | 3 | Findings focus on Rust codegen and parser policy that produce or permit problematic C++ output. | No separate C++ audit was performed. |
| Negative evidence quality | 3 | Eight specific clean checks are listed with tested or inspected surfaces. | Clean checks are scoped to inspected implementation. |
| Hardening handoff quality | 3 | Handoff orders findings, names tests, repeats validation commands, and excludes nonessential changes. | No hardening was implemented. |
| Threat/limitation honesty | 3 | Open questions separate unresolved semantics from defects. | Conversation-boundary context is recorded. |

## Final Verdict

audit-complete-with-limitations

The requested audit procedure was completed against the current Arc 03-closed implementation, with fresh validation and a whole-crate source/test pass. Limitations remain around semantic intent: integer overflow, non-literal division by zero, empty programs, and negative literals need explicit language decisions before all findings can be converted into unambiguous implementation requirements. No repairs, hardening, reformatting, test additions, planning updates, project closure, or follow-up slices were performed.
