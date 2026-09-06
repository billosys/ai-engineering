# CC Prompt: Arc 01 Slice 02 Let Literal Path

You are CC for the `framework-0.4.1` trial. Implement Arc 01 Slice 02 in this
workspace:

```text
/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial
```

## Read First

Use only the assigned framework root for collaboration-framework instructions:

```text
/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1
```

Do not use the installed `collaboration-framework` skill or any other framework
version. Do not inspect or borrow from the other framework version under test.

Read these files before editing:

- `workbench/cdc-project-prompt.md` from the framework root above
- `SKILL.md` from the framework root above
- `templates/LEDGER-DISCIPLINE.md` from the framework root above, especially Section A
- `project-plan.md`
- `arc01-foundation/arc-plan.md`
- `arc01-foundation/slice01-crate-scaffold/cdc-verification.md`
- `arc01-foundation/slice02-let-literal-path/slice-plan.md`
- `arc01-foundation/slice02-let-literal-path/ledger.md`
- existing source files under `src/`
- existing tests under `tests/`
- `docs/syntax.md`

Domain references are allowed, but only as domain guidance rather than
collaboration-framework guidance:

- `/Users/oubiwann/.codex/skills/rust-guidelines/SKILL.md`
- `/Users/oubiwann/.codex/skills/cpp-guidelines/SKILL.md`
- `/Users/oubiwann/lab/lykn/lang/docs/guides/00-lykn-surface-forms.md`
- `/Users/oubiwann/lab/lykn/lang/docs/guides/01-core-idioms.md`
- `/Users/oubiwann/lab/lykn/lang/docs/guides/05-type-discipline.md`
- `/Users/oubiwann/lab/lykn/lang/docs/guides/16-testing.md`

## Assignment

Implement Slice 02 only: the let-literal path.

Extend the existing Rust crate so the public API and CLI accept a small
multi-statement source file with integer literal bindings and prints of either
integer literals or already-bound identifiers.

Valid input example:

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

## Scope Rules

In scope:

- Preserve the public `transpile(source: &str) -> Result<String, TranspileError>` API.
- Preserve the thin file-to-stdout CLI shape.
- Extend the AST to represent ordered multi-statement programs.
- Add `(let name int)` as a statement.
- Allow `(print 42)` and `(print name)`.
- Preserve source statement order in generated C++.
- Generate local `int` declarations with brace initialization, for example `int x{40};`.
- Validate integer literals before generating C++.
- Validate identifiers before generating C++.
- Reject duplicate bindings.
- Reject printing an unknown identifier or printing an identifier before its binding.
- Update `docs/syntax.md`.
- Add `examples/let_literal.cpp`.
- Add focused library and CLI tests for the valid path and diagnostics.

Out of scope:

- Arithmetic expressions.
- Negative integer literals.
- Printing compound expressions.
- Binding identifiers to identifiers or expressions.
- Full Lykn identifier conversion, including lisp-case to camelCase.
- Real Lykn `bind`, `console:log`, type annotations, functions, comments, imports, or JavaScript behavior.
- C++ compile/run verification.
- Build-system generation or multi-file output.

## Required Policies

Identifier policy:

- Accept only ASCII C++-safe trial identifiers matching `[A-Za-z_][A-Za-z0-9_]*`.
- Reject invalid names with a structured `TranspileError` variant.
- Do not silently rewrite names.

Integer policy:

- Accept only base-10 non-negative literals in `0..=2147483647`.
- Reject larger literals with a structured diagnostic.
- Keep negative literals out of scope for this slice.

Error policy:

- User input failures return typed errors; do not panic on malformed or unsupported source.
- It is fine to extend the existing `TranspileError` enum. Keep it matchable and user-readable.
- CLI errors should go to stderr with a non-zero exit code and no generated C++ on stdout.

Dependency policy:

- Prefer continuing without new dependencies for this slice unless a dependency materially improves correctness.
- If you add a dependency, record why in the ledger and closing report.

## Ledger

Work against `arc01-foundation/slice02-let-literal-path/ledger.md`.

As you implement, update every row's `Status` and `Evidence` with attested
evidence. At close, every row must be `done`, `deferred`, or `no-op`; no row
may remain `open`.

## Validation

Run these from the trial workspace:

```text
cargo fmt --check
cargo test
cargo clippy -- -D warnings
```

Also run any focused tests named in the ledger rows while developing.

## Closing Report

When the slice is proposed-done, create:

```text
arc01-foundation/slice02-let-literal-path/closing-report.md
```

The closing report must include:

- row-by-row ledger disposition for all 13 rows
- commands run and outcomes
- changed files
- deferrals or no-op rationales, if any
- a "Bubble-up to the arc" section answering:
  1. Did this slice deliver the piece of Arc 01 assigned in `arc-plan.md`?
  2. What did this slice reveal that the arc plan did not anticipate?
  3. What is the silent-drop diff between scope-as-specified and scope-as-delivered?

Do not create `cdc-verification.md`; CDC owns that after your report.

## Report Back

When complete, report:

- whether the slice is proposed-done
- ledger row counts by status
- validation commands and results
- the path to the closing report
- any bubble-up findings CDC must review before Arc 01 can close
