# Arc 03: Examples and Audit Readiness

## Run Setup

- run label: `framework-0.4.1`
- framework entrypoint: `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/SKILL.md`
- role: CDC opening Arc 03
- workspace: `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial`
- parent project: `project-plan.md`

## Framework Files Loaded

- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/cdc-project-prompt.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/SKILL.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/docs/PROJECT-MANAGEMENT.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/templates/LEDGER-DISCIPLINE.md`

## Reference Files Loaded

- `project-plan.md`
- `arc02-expressions-and-semantics/closing-report.md`
- `tests/cli.rs`
- `Cargo.toml`

## Capability

Arc 03 turns the working tiny transpiler into an audit-ready artifact set. It
adds representative valid and invalid fixtures, focused CLI success and failure
coverage over those fixtures, at least two deterministic generated C++ examples
or equivalent output-shape coverage, C++17 compile/run evidence when a compiler
is available, and an audit-readiness map covering parser, public API, errors,
codegen, CLI, and tests.

Arc 03 does not perform the later audit. It prepares the implementation so a
subsequent audit can begin from durable, inspectable evidence.

## Dependencies

- consumes: Arc 01 and Arc 02 CDC closure, especially the final Arc 02 tiny
  expression subset and structured diagnostics
- consumes: project-plan v1.5 operator feedback adding Arc 03 close conditions
- local environment note: at Arc 03 opening, `/usr/bin/c++`, `/usr/bin/clang++`,
  and `/usr/bin/g++` were present, so the C++17 compile/run gate should be run
  unless CC records a concrete environment change
- leaves for post-project work: the independent code audit itself
- keeps out of scope: new language features, generated build systems, source
  maps, optimization, and audit findings/remediation

## Slice Breakdown

| Slice | Scope | Load-bearing for | Status |
|-------|-------|------------------|--------|
| Slice 01: Fixtures, CLI, and C++ Gates | Add representative valid and invalid fixtures, fixture-driven CLI success/failure tests, deterministic generated C++ example coverage, and C++17 compile/run evidence when available. | Slice 02 audit-readiness map and project close | closed |
| Slice 02: Audit Readiness Map | Add an audit-readiness map covering parser, public API, errors, codegen, CLI, and tests; connect docs/examples/fixtures into a readable audit entrypoint; preserve the exact project-close readiness language. | Project close and later audit pass | closed |

## Arc Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| A-1 | Slice 01 closes the fixture, CLI behavior, generated C++ example, and C++17 compile/run gates. | Read `slice01-fixtures-cli-and-cpp-gates/cdc-verification.md`. | serious | arc-plan | done | attested: `slice01-fixtures-cli-and-cpp-gates/cdc-verification.md` verifies 12 rows closed on 2026-09-05 | CDC-closed slice |
| A-2 | Slice 02 closes the audit-readiness map and final audit-entrypoint documentation. | Read `slice02-*/cdc-verification.md`. | serious | arc-plan | done | attested: `slice02-audit-readiness-map/cdc-verification.md` verifies 13 rows closed on 2026-09-05 | CDC-closed slice |
| A-3 | Arc 03 artifacts compose into an audit-ready trial surface. | Run representative valid and invalid fixtures through the CLI; compile/run generated C++ when available; inspect the audit-readiness map for parser/API/error/codegen/CLI/tests coverage. | serious | arc-plan | done | reproduced: `arc03-examples-and-audit-readiness/closing-report.md` records CLI valid/invalid demonstrations, generated C++ compile/run, focused fixture/C++ tests, full quality gates, and audit-readiness map inspection | reproduce at arc scale |
| A-4 | Slice bubble-up findings are dispositioned before project close. | Inspect this file's Version History and both slice close bubble-up sections. | serious | arc-plan | done | reproduced: `arc03-examples-and-audit-readiness/closing-report.md` records both slice bubble-ups inspected, no remediation needed, and Version History v1.1-v1.3 up to date | required before project close |
| A-5 | The project close requirement is preserved exactly: "ready for audit, audit not yet performed". | `rg -n 'ready for audit, audit not yet performed' project-plan.md arc03-examples-and-audit-readiness/arc-plan.md arc03-examples-and-audit-readiness/closing-report.md` | serious | operator-feedback | done | reproduced: exact phrase present in project plan, arc plan, and arc closing report | project close phrase preserved |

## Validation Approach

Arc 03 validation is artifact-first:

- fixture-driven CLI tests for valid and invalid source programs
- exact stdout, stderr, and exit-status assertions for CLI behavior
- deterministic expected C++ output checks for at least two examples, or an
  explicitly equivalent coverage rationale if examples are not the right shape
- C++17 compile/run using `CXX`, `c++`, `clang++`, or `g++` when available
- `cargo fmt --check`
- `cargo test`
- `cargo clippy -- -D warnings`
- direct inspection of the audit-readiness map in Slice 02

## Version History

- v1.4, 2026-09-05: Closed Arc 03 after arc-level composition verification. Recorded A-3 through A-5 closure evidence and fresh-context subagent gate pass. No Arc 03 remediation slice was required.
- v1.3, 2026-09-05: Closed Slice 02 after CDC verification. Recorded A-2 child-close evidence. No Arc 03 scope or sequencing change was required; Arc 03 is ready for arc-level composition checking.
- v1.2, 2026-09-05: Opened Slice 02 after Slice 01 CDC verification. Kept Arc 03 scope unchanged; Slice 02 owns `docs/audit-readiness.md`, documentation cross-links, reproduction-command mapping, and exact audit-readiness boundary language.
- v1.1, 2026-09-05: Closed Slice 01 after CDC verification. Recorded A-1 child-close evidence. No Arc 03 scope or sequencing change was required; Slice 02 remains planned for the audit-readiness map and final audit-entrypoint documentation.
- v1.0, 2026-09-05: Opened Arc 03 after Arc 02 CDC closure and project-plan v1.5 operator feedback. Planned two slices: fixtures/CLI/C++ gates first, then audit-readiness map and project-close preparation.
