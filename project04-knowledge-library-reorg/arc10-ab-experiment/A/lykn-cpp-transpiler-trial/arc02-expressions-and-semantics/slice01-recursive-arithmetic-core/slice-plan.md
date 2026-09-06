# Arc 02 Slice 01: Recursive Arithmetic Core

## Run Setup

- run label: `framework-0.4.1`
- framework entrypoint: `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/SKILL.md`
- role: CDC opening Slice 01 for CC
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
  - `arc01-foundation/closing-report.md`
  - `arc02-expressions-and-semantics/arc-plan.md`
  - `src/ast.rs`
  - `src/parser.rs`
  - `src/codegen.rs`
  - `src/error.rs`
  - `src/lib.rs`
  - `src/main.rs`
  - `tests/cli.rs`
  - `docs/syntax.md`

## Assumptions

- The operator-provided experiment workspace remains the layout override for
  this trial.
- Arc 01 is closed, and its baseline let-literal, simple identifier, and
  unknown-identifier behavior must remain stable.
- Prefix arithmetic is binary-only for this slice: each arithmetic form has
  exactly two operands.
- Subtraction is the supported way to produce negative runtime values; negative
  integer literals remain out of scope.
- Codegen should emit parenthesized C++ infix expressions and should not perform
  constant folding or semantic evaluation.

## Goal

Add the recursive arithmetic expression core needed for Arc 02: `+`, `-`, `*`,
and `/` expressions with integer or identifier leaves, usable in both `let`
initializers and `print` statements, with deterministic C++ output and
structured errors for the first malformed expression cases.

## In Scope

- Extend the AST with a binary arithmetic expression representation and a small
  operator representation.
- Parse recursive prefix arithmetic expressions:

```lykn
(+ 1 2)
(- x 2)
(* (+ x 2) 3)
(/ y 4)
```

- Allow expressions wherever Arc 01 currently accepts only integer literals or
  simple print operands:

```lykn
(let x 40)
(let y (+ x 2))
(print (* y 2))
```

- Resolve identifiers inside compound expressions using the existing
  bound-before-use policy.
- Preserve duplicate-binding, invalid-identifier, integer-range, empty-input,
  unsupported-form, and CLI stdout/stderr behavior from Arc 01.
- Emit deterministic C++ using parenthesized infix expression strings, for
  example:

```cpp
int y{(x + 2)};
std::cout << (y * 2) << "\n";
```

- Update focused library and CLI tests.
- Update `docs/syntax.md` with the Arc 02 Slice 01 accepted expression forms
  and deferrals.
- Add one generated C++ example if it naturally fits the implementation.

## Out Of Scope

- Unary operators or negative integer literals.
- More than two operands per arithmetic form.
- Constant folding, evaluation, overflow analysis, or division-by-zero analysis.
- Type inference beyond `int`.
- Real Lykn `bind`, real Lykn `console:log`, identifier rewriting, comments,
  strings, functions, conditionals, loops, arrays, objects, imports, modules,
  source maps, optimization, build-system generation, or multi-file C++ output.
- Broad fixture organization, optional C++ compiler execution, and audit map
  generation; those remain Arc 03 unless a later bubble-up changes the project
  plan.

## Verification Approach

CC should add tests before or alongside the implementation so each ledger row
has a reproducible command. Prefer full-output equality tests for generated C++
where practical. Diagnostics should be asserted structurally in library tests
and by stderr/stdout/exit behavior in CLI tests.

Required validation before proposed-done:

```sh
cargo fmt --check
cargo test
cargo clippy -- -D warnings
```

## Exit Criteria

Arc 02 Slice 01 is proposed-done when every row in `ledger.md` has a final
disposition with evidence, Arc 01 behavior remains green under the normal test
harness, and the close report includes a Bubble-up to the arc section stating
whether any expression parsing or semantic finding changes the Arc 02 plan.
