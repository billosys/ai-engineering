# Arc 01 Slice 02: Let Literal Path Plan

## Run Setup

- run label: `framework-0.4.1`
- framework entrypoint: `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/SKILL.md`
- role: CDC opening Slice 02 for CC
- workspace: `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial`
- status: open

## Framework Files Loaded

- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/cdc-project-prompt.md`
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
- `/Users/oubiwann/.codex/skills/cpp-guidelines/SKILL.md`
- `/Users/oubiwann/.codex/skills/cpp-guidelines/guides/01-core-idioms.md`
- `/Users/oubiwann/.codex/skills/cpp-guidelines/guides/10-expressions-and-statements.md`
- `/Users/oubiwann/.codex/skills/cpp-guidelines/guides/11-anti-patterns.md`
- `/Users/oubiwann/lab/lykn/lang/docs/guides/00-lykn-surface-forms.md`
- `/Users/oubiwann/lab/lykn/lang/docs/guides/01-core-idioms.md`
- `/Users/oubiwann/lab/lykn/lang/docs/guides/05-type-discipline.md`
- `/Users/oubiwann/lab/lykn/lang/docs/guides/16-testing.md`

## Assumptions

- The experiment prompt's workspace is the operator-approved layout override for this trial.
- Slice 01 is CDC-verified closed, and its range-policy note is binding for Slice 02 because this slice introduces generated local `int` declarations.
- Slice 02 keeps the already-established public API shape and thin CLI instead of changing crate architecture.
- The trial identifier policy is deliberately narrower than Lykn's full lisp-case-to-camelCase behavior: Slice 02 accepts only C++-safe identifiers matching `[A-Za-z_][A-Za-z0-9_]*`.
- Integer literals accepted by Slice 02 are base-10 non-negative values in `0..=2147483647`. Negative literals and arithmetic-derived negative values remain out of scope until the arithmetic slice defines the expression grammar.

## Goal

Extend the first vertical path into a small multi-statement program path:
literal integer bindings can be declared with `(let name int)`, and later
statements can print either integer literals or identifiers that have already
been bound.

Example accepted input:

```lykn
(let x 40)
(print x)
(print 42)
```

Expected generated C++:

```cpp
#include <iostream>

int main() {
    int x{40};
    std::cout << x << "\n";
    std::cout << 42 << "\n";
    return 0;
}
```

## In Scope

- Preserve the existing Rust package, public `transpile` API, and thin CLI.
- Extend the AST to represent an ordered `Program` with multiple statements.
- Add a `let` statement form whose initializer is an accepted integer literal.
- Allow `print` to print either an accepted integer literal or a previously bound identifier.
- Preserve source statement order in generated C++.
- Generate local `int` declarations using brace initialization: `int x{40};`.
- Validate accepted integer literal range before code generation.
- Validate accepted identifier shape before code generation.
- Reject duplicate bindings and unknown identifiers with structured diagnostics.
- Update `docs/syntax.md` to describe the Slice 02 accepted subset and deferrals.
- Add one generated C++ example for the let-plus-print path.
- Add library and CLI tests for the valid path and the new diagnostics.

## Out Of Scope

- Arithmetic expressions, including `+`, `-`, `*`, and `/`.
- Negative integer literal syntax.
- Printing compound expressions.
- Binding identifiers to identifiers or expressions.
- Lykn lisp-case-to-camelCase identifier conversion.
- Full Lykn `bind`, `console:log`, type annotations, functions, comments, imports, or JavaScript behavior.
- C++ compile/run verification.
- Build-system generation or multi-file C++ output.

## Verification Approach

CC should update the slice ledger while implementing, then close the slice with
a per-row closing report. CDC will later re-run each ledger command from the
assigned workspace.

Required gates:

- `cargo fmt --check`
- `cargo test`
- `cargo clippy -- -D warnings`

The tests should include exact generated C++ string comparisons for at least
one valid multi-statement let-plus-print program and CLI checks for stdout,
stderr, and exit status.

## Exit Criteria

Slice 02 is proposed-done when every row in `ledger.md` has a final disposition
with attested evidence, the closing report walks every row, and the
Bubble-up to the arc section states whether the expanded integer/identifier
policy changes Arc 01 or Arc 02 planning.
