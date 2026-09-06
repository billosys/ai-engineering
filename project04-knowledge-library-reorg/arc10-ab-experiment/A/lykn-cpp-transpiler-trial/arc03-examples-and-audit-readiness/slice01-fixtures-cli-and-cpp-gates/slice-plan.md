# Arc 03 Slice 01: Fixtures, CLI, and C++ Gates

## Run Setup

- run label: `framework-0.4.1`
- framework entrypoint: `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/SKILL.md`
- role: CDC opening Slice 01 for CC
- workspace: `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial`
- parent arc: `arc03-examples-and-audit-readiness`

## Framework Files Loaded

- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/cdc-project-prompt.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/SKILL.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/docs/PROJECT-MANAGEMENT.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/templates/LEDGER-DISCIPLINE.md`

## Reference Files Loaded

- `project-plan.md`
- `arc02-expressions-and-semantics/closing-report.md`
- `arc03-examples-and-audit-readiness/arc-plan.md`
- `tests/cli.rs`
- `Cargo.toml`

## Assumptions

- `tests/fixtures/` is the local convention for representative source fixtures
  and expected-output fixtures in this Rust crate.
- `examples/` remains the home for deterministic generated C++ examples.
- At opening, `c++`, `clang++`, and `g++` are available under `/usr/bin`; CC
  should run the C++17 compile/run gate unless the environment changes and the
  closing report records that change.
- This slice may add tests and fixtures, and may refactor existing CLI tests
  just enough to share fixture helpers. It should not change the language
  grammar or generated C++ style.

## Goal

Make the completed tiny language auditable through concrete files and behavior
checks: representative fixtures, CLI success/failure coverage over those
fixtures, deterministic generated C++ examples, and C++17 compile/run evidence.

## In Scope

- Add representative valid fixtures under `tests/fixtures/valid/`.
- Add representative invalid fixtures under `tests/fixtures/invalid/`.
- Add expected deterministic C++ output fixtures under `tests/fixtures/expected/`
  for at least two valid fixture programs.
- Add or update CLI tests so valid fixtures assert exact stdout and empty stderr.
- Add or update CLI tests so invalid fixtures assert non-zero exit, empty
  stdout, and diagnostic stderr.
- Ensure at least two deterministic generated C++ examples exist under
  `examples/`, or document and test equivalent output-shape coverage if example
  files are not the right local representation.
- Compile and run generated C++ examples with C++17 if a compiler is available.
- Preserve existing public API tests and CLI tests.
- Update `docs/syntax.md` or add a small fixture note if needed so a later audit
  can find the fixtures and examples without spelunking.
- Keep `cargo fmt --check`, `cargo test`, and `cargo clippy -- -D warnings`
  green.

## Out Of Scope

- New accepted syntax or new diagnostics beyond fixture/testing needs.
- Changing the parser, AST, code generator, or error enum unless a fixture
  exposes a real bug in the existing Arc 02 behavior.
- Performing the later audit.
- Writing the audit-readiness map; Slice 02 owns that.
- Writing `cdc-verification.md`; CDC writes it after independent verification.
- Closing Arc 03 or the project.

## Verification Approach

Prefer tests that consume real fixture files instead of duplicating long source
strings inside the test body. Keep the existing exact-output style: valid CLI
tests assert exact generated C++ stdout against expected fixture files and
empty stderr; invalid CLI tests
assert failure status, empty stdout, and the expected diagnostic text.

For C++17 compile/run, choose the compiler in this order: `CXX` if set,
otherwise `c++`, `clang++`, then `g++`. If no compiler is available, record a
valid no-op with the exact detection command and re-entry condition. In this
opened environment a compiler is available, so the expected path is to run the
gate.

Required validation before proposed-done:

```sh
cargo fmt --check
cargo test
cargo clippy -- -D warnings
```

## Exit Criteria

Slice 01 is proposed-done when every row in `ledger.md` has a final disposition
with evidence, the close report includes a row-by-row ledger walk, and the
Bubble-up section states whether the fixtures and C++ gates are sufficient for
Slice 02 to build the audit-readiness map.
