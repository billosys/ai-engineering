# Arc 03 Slice 02: Audit Readiness Map

## Run Setup

- run label: `framework-0.4.1`
- framework entrypoint: `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/SKILL.md`
- role: CDC opening Slice 02 for CC
- workspace: `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial`
- parent arc: `arc03-examples-and-audit-readiness`

## Framework Files Loaded

- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/cdc-project-prompt.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/SKILL.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/docs/PROJECT-MANAGEMENT.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/templates/LEDGER-DISCIPLINE.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/docs/CODE-AUDIT.md`

## Reference Files Loaded

- `project-plan.md`
- `arc03-examples-and-audit-readiness/arc-plan.md`
- `arc03-examples-and-audit-readiness/slice01-fixtures-cli-and-cpp-gates/cdc-verification.md`
- `tests/fixtures/README.md`
- `tests/cli.rs`
- `docs/syntax.md`
- `Cargo.toml`
- `src/ast.rs`
- `src/parser.rs`
- `src/codegen.rs`
- `src/error.rs`
- `src/lib.rs`
- `src/main.rs`

## Assumptions

- The audit-readiness map should live at `docs/audit-readiness.md`, because it
  is documentation about the crate's audit surface rather than a slice-close
  artifact.
- This slice prepares a later audit but does not perform one. It should not
  create audit findings, severity labels, or `workbench/YYYY.MM.DD-audit-*`
  reports.
- The exact phrase "ready for audit, audit not yet performed" must appear in
  the audit-readiness surface and be preserved for project close.
- Arc 03 Slice 01 already produced the representative fixtures, expected C++
  fixtures, generated examples, and C++17 compile/run gate evidence that this
  slice should map.

## Goal

Create a concise audit-readiness entrypoint that tells a later auditor what to
read, what each surface owns, how to reproduce the current gates, and where the
project boundary ends. The result should make the project ready for a later code
audit while explicitly not performing that audit.

## In Scope

- Add `docs/audit-readiness.md` as the audit-readiness map.
- Map parser and AST surfaces: `src/parser.rs` and `src/ast.rs`.
- Map public API and CLI boundary surfaces: `src/lib.rs` and `src/main.rs`.
- Map diagnostics and error-contract surfaces: `src/error.rs`, parser error
  paths, invalid fixtures, and relevant tests.
- Map code generation and generated C++ surfaces: `src/codegen.rs`,
  `examples/*.cpp`, and `tests/fixtures/expected/*.cpp`.
- Map fixture and test surfaces: `tests/fixtures/valid/`,
  `tests/fixtures/invalid/`, `tests/fixtures/expected/`,
  `tests/fixtures/README.md`, `tests/cli.rs`, and library tests in
  `src/lib.rs`.
- Record the reproduction commands a later audit should run, including
  fixture-driven CLI tests, C++17 compile/run tests, and the normal Rust quality
  gates.
- Distinguish in-scope accepted syntax from explicit non-goals and later-audit
  boundaries.
- Cross-link `docs/audit-readiness.md` from `docs/syntax.md` and
  `tests/fixtures/README.md`.
- Preserve existing tests and examples; this slice should be documentation and
  mapping work unless it discovers a broken reference.

## Out Of Scope

- Performing the code audit.
- Writing audit findings, severity-ranked issues, or audit reports.
- Adding new accepted syntax or new generated C++ behavior.
- Refactoring parser, AST, codegen, errors, public API, or CLI behavior except
  for a narrow fix to a broken reference discovered while mapping.
- Closing Arc 03 or the project.
- Writing `cdc-verification.md`; CDC writes it after independent verification.

## Verification Approach

The map should be verified by direct text search and by rerunning the same
behavior gates that make the audit surface credible. The important property is
not prose volume; it is traceability from audit topic to concrete files and
commands.

Required validation before proposed-done:

```sh
cargo fmt --check
cargo test
cargo clippy -- -D warnings
```

## Exit Criteria

Slice 02 is proposed-done when every row in `ledger.md` has a final disposition
with evidence, `docs/audit-readiness.md` covers the required audit surfaces and
reproduction commands, existing gates remain green, and the close report's
Bubble-up section says whether Arc 03 is ready for arc-level composition
checking and project close preparation.
