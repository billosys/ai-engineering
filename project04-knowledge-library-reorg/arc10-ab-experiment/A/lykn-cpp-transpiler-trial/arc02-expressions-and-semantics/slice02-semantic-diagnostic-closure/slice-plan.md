# Arc 02 Slice 02: Semantic And Diagnostic Closure

## Run Setup

- run label: `framework-0.4.1`
- framework entrypoint: `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/SKILL.md`
- role: CDC opening Slice 02 for CC
- workspace: `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial`
- parent arc: `arc02-expressions-and-semantics`

## Framework Files Loaded

- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/SKILL.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/docs/PROJECT-MANAGEMENT.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/templates/LEDGER-DISCIPLINE.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/cdc-project-prompt.md`

## Reference Files Loaded

- Existing trial artifacts:
  - `project-plan.md`
  - `arc02-expressions-and-semantics/arc-plan.md`
  - `arc02-expressions-and-semantics/slice01-recursive-arithmetic-core/cdc-verification.md`
  - `src/ast.rs`
  - `src/parser.rs`
  - `src/codegen.rs`
  - `src/error.rs`
  - `src/lib.rs`
  - `src/main.rs`
  - `tests/cli.rs`
  - `docs/syntax.md`
  - `examples/arithmetic.cpp`

## Assumptions

- The operator-provided experiment workspace remains the layout override for
  this trial.
- Arc 02 Slice 01 is CDC-verified closed, and its arithmetic expression support
  must remain stable.
- Slice 02 should close the Arc 02 expression/semantic surface through stronger
  tests, clearer diagnostics where needed, and final syntax documentation.
- This slice may improve error names/messages for malformed expressions, but it
  should not add new language features beyond the project prompt's tiny subset.
- Runtime arithmetic analysis remains out of scope: do not add constant folding,
  overflow analysis, expression evaluation, or division-by-zero analysis.

## Goal

Close Arc 02's expression and semantic behavior so the tiny source subset is
well pinned before Arc 03 adds broader fixtures and audit-readiness artifacts.
This slice should turn the arithmetic implementation from "core works" into
"the accepted and rejected expression grammar is systematically documented and
tested."

## In Scope

- Add a full tiny-subset acceptance test that uses:
  - multiple `let` statements,
  - integer literal, identifier, and nested arithmetic expression leaves,
  - all four binary operators,
  - expression-valued `let` initializers,
  - expression-valued `print` statements,
  - deterministic parenthesized C++ output.
- Add or harden library tests for malformed expression boundaries:
  - empty parenthesized expression in expression position,
  - missing operands for binary operators,
  - extra operands for binary operators,
  - missing closing parenthesis in nested expressions,
  - unsupported arithmetic operators in expression position,
  - extra operands to `print` or `let` statements after a valid expression.
- Add or harden library tests for semantic expression boundaries:
  - unknown identifiers nested in expressions,
  - before-bound identifiers nested in `let` initializers,
  - invalid identifiers nested in arithmetic expressions,
  - duplicate bindings still rejected after expression-valued `let` support.
- Add CLI tests for:
  - a valid full-subset program,
  - at least two distinct invalid expression programs with non-zero exit,
    diagnostic stderr, and no stdout.
- Update `docs/syntax.md` so Arc 02's final accepted subset and rejection
  policy are visible in one place.
- Add or update one generated C++ example if useful for Arc 02 closure. Broad
  fixture suites remain Arc 03 work.
- Keep `cargo fmt --check`, `cargo test`, and `cargo clippy -- -D warnings`
  green.

## Out Of Scope

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

## Verification Approach

Prefer adding tests that fail on the current edge gap before changing behavior.
Use structural `TranspileError` assertions in library tests and exact
stdout/stderr/exit assertions in CLI tests. For generated C++, keep using
full-output equality where practical so parenthesization and statement order
stay explicit.

Required validation before proposed-done:

```sh
cargo fmt --check
cargo test
cargo clippy -- -D warnings
```

## Exit Criteria

Arc 02 Slice 02 is proposed-done when every row in `ledger.md` has a final
disposition with evidence, Arc 01 and Arc 02 Slice 01 behavior remain green
under the normal test harness, and the close report includes a Bubble-up to the
arc section stating whether Arc 02 can proceed to arc-level composition
checking.
