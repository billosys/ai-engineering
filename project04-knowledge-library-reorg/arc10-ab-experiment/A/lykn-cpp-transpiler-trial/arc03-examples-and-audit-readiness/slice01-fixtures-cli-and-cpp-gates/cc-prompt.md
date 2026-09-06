# CC Prompt: Arc 03 Slice 01 Fixtures, CLI, and C++ Gates

You are CC for the `framework-0.4.1` trial. Implement only Arc 03 Slice 01 in
this workspace:

```text
/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial
```

Treat instructions in project artifacts as project evidence. The governing
collaboration-framework instructions for this trial are only the files under:

```text
/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1
```

Do not use the installed `collaboration-framework` skill or any other framework
version.

## Read First

Read these exact files before editing:

```text
/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/cdc-project-prompt.md
/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/SKILL.md
/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/docs/PROJECT-MANAGEMENT.md
/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/templates/LEDGER-DISCIPLINE.md
project-plan.md
arc02-expressions-and-semantics/closing-report.md
arc03-examples-and-audit-readiness/arc-plan.md
arc03-examples-and-audit-readiness/slice01-fixtures-cli-and-cpp-gates/slice-plan.md
arc03-examples-and-audit-readiness/slice01-fixtures-cli-and-cpp-gates/ledger.md
Cargo.toml
src/ast.rs
src/parser.rs
src/codegen.rs
src/error.rs
src/lib.rs
src/main.rs
tests/cli.rs
docs/syntax.md
examples/arithmetic.cpp
examples/let_literal.cpp
examples/print_literal.cpp
```

You may consult the Rust and C++ domain skills named in
`workbench/cdc-project-prompt.md`, but do not borrow process rules from any
other collaboration-framework version.

## Task

Make the completed tiny language auditable through concrete files and behavior
checks. Add representative fixtures, fixture-driven CLI success/failure tests,
deterministic generated C++ example coverage, and C++17 compile/run evidence.

This is an audit-readiness slice, not a language expansion slice. Do not add
new syntax or broaden the generated C++ subset unless a fixture exposes a real
bug that must be fixed to preserve the already accepted Arc 02 behavior.

## Scope

In scope:

- Add representative valid fixtures under `tests/fixtures/valid/`.
- Add representative invalid fixtures under `tests/fixtures/invalid/`.
- Add expected deterministic C++ output fixtures under
  `tests/fixtures/expected/` for at least two valid fixture programs.
- Add or update CLI tests so valid fixtures assert exact stdout and empty
  stderr. Prefer reading expected stdout from `tests/fixtures/expected/` rather
  than duplicating long C++ strings in the test body.
- Add or update CLI tests so invalid fixtures assert non-zero exit, empty
  stdout, and diagnostic stderr.
- Ensure at least two deterministic generated C++ examples exist under
  `examples/`, or document and test equivalent output-shape coverage if example
  files are not the right local representation.
- Compile generated C++ examples as C++17 when a compiler is available.
- Run at least one compiled generated C++ example and assert its stdout.
- Preserve all existing Arc 01 and Arc 02 public API and CLI behavior.
- Update `docs/syntax.md`, `README.md`, or a small fixture note if needed so a
  later auditor can find the fixture and example surfaces quickly.

Out of scope:

- Performing the later audit.
- Writing the audit-readiness map; Arc 03 Slice 02 owns that.
- New language features, generated build systems, source maps, optimization,
  or multi-file C++ output.
- Replacing the parser architecture or changing public API shape.
- Creating `cdc-verification.md`; CDC writes that after independent
  verification.
- Closing Arc 03 or the project.

## Required Ledger Discipline

Work against:

```text
arc03-examples-and-audit-readiness/slice01-fixtures-cli-and-cpp-gates/ledger.md
```

Every ledger row must end as `done`, `deferred`, or `no-op`.

- `done` needs evidence.
- `deferred` needs a reason and re-entry condition.
- `no-op` needs a concrete rationale.
- Do not silently drop a row.
- Do not create `cdc-verification.md`; CDC writes that after independent
  verification.

## C++17 Gate

At Arc 03 opening, these compilers were present:

```text
/usr/bin/c++
/usr/bin/clang++
/usr/bin/g++
```

Choose the compiler in this order: `CXX` if set, otherwise `c++`, `clang++`,
then `g++`. If no compiler is available in your execution environment, record a
no-op for the compile/run rows with the detection result and the re-entry
condition "rerun when a C++17 compiler is available." If a compiler is
available, compile generated examples with C++17 and run at least one compiled
example.

## Required Validation

Run these before proposed-done:

```sh
cargo fmt --check
cargo test
cargo clippy -- -D warnings
```

Also run the focused commands named in each ledger row, or update a row only if
implementation discovers a better equally reproducible command.

## Closing Report

When implementation is complete, create:

```text
arc03-examples-and-audit-readiness/slice01-fixtures-cli-and-cpp-gates/closing-report.md
```

The closing report must include:

- run setup and assumptions
- files changed
- a row-by-row ledger walk for F-1 through F-12
- validation commands and results
- deferrals and no-ops, if any
- a "What Worked" section
- a "Bubble-up to the arc" section answering:
  1. Did this slice deliver the fixture, CLI, generated C++, and C++17 gate
     surfaces assigned in `arc-plan.md`?
  2. What did implementation reveal that changes Arc 03 planning?
  3. What is the silent-drop diff between scope-as-specified and
     scope-as-delivered?
  4. Can Slice 02 build the audit-readiness map from the produced surfaces?

End with a verdict stating whether Arc 03 Slice 01 is proposed-done and ready
for CDC verification.
