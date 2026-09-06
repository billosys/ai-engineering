# CC Prompt: Arc 02 Slice 02 Semantic And Diagnostic Closure

You are CC for the `framework-0.4.1` trial. Implement only Arc 02 Slice 02 in
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
arc02-expressions-and-semantics/arc-plan.md
arc02-expressions-and-semantics/slice01-recursive-arithmetic-core/cdc-verification.md
arc02-expressions-and-semantics/slice02-semantic-diagnostic-closure/slice-plan.md
arc02-expressions-and-semantics/slice02-semantic-diagnostic-closure/ledger.md
src/ast.rs
src/parser.rs
src/codegen.rs
src/error.rs
src/lib.rs
src/main.rs
tests/cli.rs
docs/syntax.md
examples/arithmetic.cpp
```

You may consult the Rust and C++ domain skills named in
`workbench/cdc-project-prompt.md`, but do not borrow process rules from any
other collaboration-framework version.

## Task

Close Arc 02's expression and semantic behavior for the tiny trial language.
Arc 02 Slice 01 already implemented recursive binary arithmetic. Your job is
to harden and document the accepted and rejected expression grammar so Arc 02
can move to arc-level composition checking after CDC verification.

This is a closure slice, not a scope expansion. Add targeted tests first where
possible, then make the smallest parser/error/codegen/doc changes required for
the ledger rows.

## Scope

In scope:

- Add a public API test for a full tiny-subset program using:
  - multiple `let` statements,
  - expression-valued `let` initializers,
  - expression-valued `print` statements,
  - integer literal, identifier, and nested expression leaves,
  - all four binary operators,
  - exact deterministic C++ output.
- Add a CLI test for the same accepted surface.
- Add or harden structured diagnostic tests for:
  - empty parenthesized expressions in expression position,
  - missing operands across arithmetic operators,
  - extra operands across arithmetic operators,
  - missing closing parentheses in nested expressions,
  - unsupported arithmetic operators in expression position,
  - extra operands after valid `print` and `let` expressions,
  - invalid identifiers inside arithmetic expressions,
  - unknown and before-bound identifiers inside nested expressions.
- Preserve existing Arc 01 and Arc 02 Slice 01 behavior exactly.
- Update `docs/syntax.md` so it clearly states the final Arc 02 accepted subset,
  malformed-expression diagnostics, semantic rejection policy, and Arc 03
  deferrals.
- Add or update `examples/arithmetic.cpp` if that helps represent the final Arc
  02 output style.

Out of scope:

- Unary operators or negative integer literals.
- Variadic arithmetic.
- Runtime evaluation, constant folding, overflow analysis, and
  division-by-zero analysis.
- New syntax beyond `(let ...)`, `(print ...)`, integer literals, identifiers,
  and binary prefix arithmetic expressions.
- Real Lykn `bind`, real Lykn `console:log`, identifier rewriting, comments,
  strings, functions, conditionals, loops, arrays, objects, imports, modules,
  source maps, optimization, build-system generation, or multi-file C++ output.
- Broad fixture organization, optional C++ compiler execution, audit-map
  generation, and final audit; those remain Arc 03.

## Required Ledger Discipline

Work against:

```text
arc02-expressions-and-semantics/slice02-semantic-diagnostic-closure/ledger.md
```

Every ledger row must end as `done`, `deferred`, or `no-op`.

- `done` needs evidence.
- `deferred` needs a reason and re-entry condition.
- `no-op` needs a concrete rationale.
- Do not silently drop a row.
- Do not create `cdc-verification.md`; CDC writes that after independent
  verification.

## Required Validation

Run these before proposed-done:

```sh
cargo fmt --check
cargo test
cargo clippy -- -D warnings
```

Also run the focused commands named in each ledger row, or update the row only
if implementation discovers a better equally reproducible command.

## Closing Report

When implementation is complete, create:

```text
arc02-expressions-and-semantics/slice02-semantic-diagnostic-closure/closing-report.md
```

The closing report must include:

- run setup and assumptions
- files changed
- a row-by-row ledger walk for D-1 through D-13
- validation commands and results
- deferrals and no-ops, if any
- a "What Worked" section
- a "Bubble-up to the arc" section answering:
  1. Did this slice deliver the piece of Arc 02 assigned in `arc-plan.md`?
  2. What did implementation reveal that changes Arc 02 planning?
  3. What is the silent-drop diff between scope-as-specified and
     scope-as-delivered?
  4. After CDC verification, can Arc 02 proceed to arc-level composition
     checking?

End with a verdict stating whether Arc 02 Slice 02 is proposed-done and ready
for CDC verification.
