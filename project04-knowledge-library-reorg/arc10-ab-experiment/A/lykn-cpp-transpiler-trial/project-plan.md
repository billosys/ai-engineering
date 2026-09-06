# Lykn to Tiny C++ Transpiler Trial: Project Plan

## Run Setup

- run label: `framework-0.4.1`
- framework entrypoint: `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/SKILL.md`
- role: CDC
- status: closed
- depends-on: none
- blocks: later framework comparison and code-audit pass
- related: `/Users/oubiwann/lab/lykn/lang/docs/guides/`

## Framework Files Loaded

- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/SKILL.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/docs/AI-CONSTITUTION-SUPPLEMENT.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/docs/AI-ENGINEERING-METHODOLOGY.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/docs/PROJECT-MANAGEMENT.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/templates/LEDGER-DISCIPLINE.md`

## Reference Files Loaded

- `/Users/oubiwann/.codex/skills/rust-guidelines/SKILL.md`
- `/Users/oubiwann/.codex/skills/rust-guidelines/guides/01-core-idioms.md`
- `/Users/oubiwann/.codex/skills/rust-guidelines/guides/03-error-handling.md`
- `/Users/oubiwann/.codex/skills/rust-guidelines/guides/11-anti-patterns.md`
- `/Users/oubiwann/.codex/skills/rust-guidelines/guides/14-cli-tools/README.md`
- `/Users/oubiwann/.codex/skills/rust-guidelines/guides/14-cli-tools/01-project-setup.md`
- `/Users/oubiwann/.codex/skills/rust-guidelines/guides/14-cli-tools/06-testing.md`
- `/Users/oubiwann/.codex/skills/cpp-guidelines/SKILL.md`
- `/Users/oubiwann/.codex/skills/cpp-guidelines/guides/01-core-idioms.md`
- `/Users/oubiwann/.codex/skills/cpp-guidelines/guides/10-expressions-and-statements.md`
- `/Users/oubiwann/.codex/skills/cpp-guidelines/guides/11-anti-patterns.md`
- `/Users/oubiwann/.codex/skills/cpp-guidelines/guides/13-standard-library.md`
- `/Users/oubiwann/lab/lykn/lang/docs/guides/00-lykn-surface-forms.md`
- `/Users/oubiwann/lab/lykn/lang/docs/guides/01-core-idioms.md`
- `/Users/oubiwann/lab/lykn/lang/docs/guides/05-type-discipline.md`
- `/Users/oubiwann/lab/lykn/lang/docs/guides/16-testing.md`

## Assumptions

- The operator-provided experiment workspace is an explicit layout override for this trial, so the framework's canonical filenames are used inside that workspace instead of creating a separate orphan planning worktree.
- The installed collaboration-framework skill and memory were opened before the scientific-control constraint was read; they are not used as authority for this packet.
- "Lykn-inspired" means S-expression surface forms and prefix arithmetic, informed by Lykn's `(bind x 42)`, `(console:log x)`, and `(+ a b)` examples, but the trial vocabulary is the prompt's `let` and `print`.
- Generated bindings will initially use initialized local `int` declarations to match the trial scope. Whether to upgrade immutable `let` output to `const int` is reserved as an explicit audit/design question.

## Project Goal

Build a small Rust transpiler from a tiny Lykn-inspired syntax to a deliberately tiny C++17 subset. The project should be shallow but real: parser, AST, code generation, errors, CLI, fixtures, tests, generated examples, and enough surface for a later code audit.

## Non-goals

No full Lykn compatibility, JavaScript semantics, functions, conditionals, loops, strings, arrays, objects, modules, macros, comments, source maps, C++ classes, templates, headers, pointers, references, ownership modeling, exceptions, build-system generation, optimization, or multi-file C++ output.

## Trial Syntax and C++ Subset

Accepted source syntax is a small Lisp-like trial language:

```lykn
(let x 40)
(let y (+ x 2))
(print y)
```

The generated C++17 subset is:

```cpp
#include <iostream>

int main() {
    int x{40};
    int y{(x + 2)};
    std::cout << y << "\n";
    return 0;
}
```

The trial keeps Lykn's parenthesized forms and prefix arithmetic, uses `let` instead of Lykn's `bind`, and uses `print` instead of `console:log` so the accepted grammar matches the project prompt.

## Likely Rust Shape

Use one Rust package with a testable library and thin CLI:

- `src/lib.rs`: public `transpile(source: &str) -> Result<String, TranspileError>`
- `src/ast.rs`: `Program`, `Stmt`, `Expr`
- `src/lexer.rs` and/or `src/parser.rs`: small hand-written parser unless CC records a reason to add a parser crate
- `src/codegen.rs`: deterministic C++ emitter
- `src/error.rs`: structured error enum
- `src/main.rs`: thin CLI boundary
- `tests/`: integration tests and fixtures
- `examples/`: generated C++ examples

## Arc Roadmap

| Arc | Capability | Dependencies | Status |
|-----|------------|--------------|--------|
| Arc 01: Foundation | Establish crate, syntax contract, CLI boundary, and first vertical C++ generation path. | none | closed |
| Arc 02: Expressions and Semantics | Extend the Arc 01 literal foundation with arithmetic expressions, compound expression identifier resolution, malformed-expression diagnostics, and semantic hardening beyond simple let-literal programs. | Arc 01 | closed |
| Arc 03: Examples and Audit Readiness | Add representative fixtures, focused CLI behavior coverage, deterministic generated C++ examples or equivalent coverage, optional C++17 compile/run gate, documentation, and audit-readiness map. | Arc 02 | closed |

Arc 02 roadmap refinement after Arc 01 close: the original v1.0 roadmap said
Arc 02 would "Add let bindings, identifiers, arithmetic expressions,
malformed-expression diagnostics, and unknown-identifier checks." Arc 01
delivered the baseline let-literal path, simple identifier prints, and
unknown-identifier checks earlier than that roadmap line implied. The remaining
Arc 02 work is expression and semantic depth, not re-adding the already closed
foundation behavior.

## Arc 03 Close Conditions

When Arc 03 is opened in detail, its `arc-plan.md`, slice ledgers, and close
criteria must include these conditions:

- focused CLI success and failure behavior coverage
- representative valid and invalid source fixtures
- at least two deterministic generated C++ examples, or equivalent coverage
  that gives the later audit the same output-shape evidence
- C++17 compile and run evidence if a compiler is available in the local
  environment
- audit-readiness map covering parser, public API, errors, codegen, CLI, and
  tests
- project close language explicitly stating: "ready for audit, audit not yet
  performed"

## Project Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| P-1 | Arc 01 closes and produces a usable first vertical slice. | Read `arc01-foundation/closing-report.md` and its gate result. | correctness | project-plan | done | attested: `arc01-foundation/closing-report.md` closes 4 arc rows on 2026-09-05, records reproduced CLI composition demos, and records fresh-context gate approval | attested by closed arc |
| P-2 | Arc 02 closes and supports the full tiny source subset. | Read `arc02-*/closing-report.md` and run project acceptance fixtures. | serious | project-plan | done | attested: `arc02-expressions-and-semantics/closing-report.md` closes 4 arc rows on 2026-09-05 and records full-subset CLI acceptance plus representative invalid diagnostics | attested plus project demo |
| P-3 | Arc 03 closes and the project is ready for a later code audit. | Read `arc03-*/closing-report.md`; inspect focused CLI coverage, representative valid/invalid fixtures, deterministic C++ examples or equivalent coverage, C++17 compile/run disposition, and the audit-readiness map. | serious | project-plan | done | attested: `arc03-examples-and-audit-readiness/closing-report.md` closes 5 arc rows on 2026-09-05 and records focused CLI, fixture, generated C++, C++17, and audit-readiness map evidence | audit is not performed in this project |
| P-4 | The arcs compose into the project definition of done. | Run valid/invalid fixtures through the CLI and inspect generated C++ examples. | serious | project-plan | done | reproduced: project close reran `cargo test cli_valid_fixtures`, `cargo test cli_invalid_fixtures`, `cargo test generated_cpp_examples_compile`, `cargo test generated_cpp_example_runs`, `cargo fmt --check`, `cargo test`, and `cargo clippy -- -D warnings`; `closing-report.md` records all arcs closed and the Rust self-audit artifact present | project-scale composition reproduced |
| P-5 | Project close explicitly states audit readiness without claiming that the audit has been performed. | `rg -n 'ready for audit, audit not yet performed' closing-report.md` | serious | operator-feedback | done | reproduced: `closing-report.md` includes the exact phrase "ready for audit, audit not yet performed" while separately recording that `rust-self-audit-report.md` exists as the post-Arc03 audit artifact | exact phrase preserved |

## Evaluation Notes

This project should give the framework comparison concrete evidence at several altitudes: whether the framework creates a usable project roadmap, whether Arc 01's plan gives CC enough implementation guidance without overbuilding, whether the ledger rows are independently reproducible, and whether the resulting Rust/C++ surface is rich enough for a later code audit.

## Version History

- v1.8, 2026-09-05: Closed the project after Arc 03 closure and the read-only Rust self-audit artifact. Marked P-4/P-5 done, set project status to closed, and recorded project-scale fixture, C++ example, full Rust quality-gate, and audit-readiness evidence in `closing-report.md`.
- v1.7, 2026-09-05: Recorded Arc 03 closure from `arc03-examples-and-audit-readiness/closing-report.md`, marked P-3 done, and kept P-4/P-5 open for project-level composition and final project close. No project roadmap change was required.
- v1.6, 2026-09-05: Opened Arc 03 after Arc 02 CDC closure. Added `arc03-examples-and-audit-readiness/arc-plan.md` and the Slice 01 open set for fixture, CLI, generated C++, and C++17 gates; P-3 remains open until Arc 03 closes.
- v1.5, 2026-09-05: Added operator-requested Arc 03 close conditions for focused CLI behavior coverage, representative fixtures, deterministic generated C++ examples or equivalent coverage, C++17 compile/run if available, audit-readiness map coverage, and exact project-close audit-readiness language. Added P-5 so project closure must state "ready for audit, audit not yet performed."
- v1.4, 2026-09-05: Recorded Arc 02 closure from `arc02-expressions-and-semantics/closing-report.md`, marked P-2 done, and kept Arc 03 planned. No project scope change was required.
- v1.3, 2026-09-05: Opened Arc 02 after Arc 01 CDC closure and project-plan refinement. Added `arc02-expressions-and-semantics/arc-plan.md` and the Slice 01 open set for recursive arithmetic core work; P-2 remains open until Arc 02 closes.
- v1.2, 2026-09-05: Reconciled the independent Arc 01 gate finding by refining Arc 02's roadmap wording. Arc 01 delivered baseline let literals, simple identifier prints, and unknown-identifier checks, so Arc 02 now focuses on arithmetic expressions, compound expression identifier resolution, malformed-expression diagnostics, and semantic hardening beyond the literal path.
- v1.1, 2026-09-05: Recorded Arc 01 closure from `arc01-foundation/closing-report.md`, marked P-1 done, and set the project status to active. The initial CDC bookkeeping treated Arc 02's remaining scope as unchanged; v1.2 supersedes that wording after fresh-context gate review.
- v1.0, 2026-09-05: Initial CDC project plan for `framework-0.4.1` trial.
