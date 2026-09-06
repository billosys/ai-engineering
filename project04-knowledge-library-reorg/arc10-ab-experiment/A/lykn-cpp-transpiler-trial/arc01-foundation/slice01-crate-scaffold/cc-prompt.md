# CC Prompt: Arc 01 Slice 01

You are CC, the implementation agent, for the `framework-0.4.1` Lykn-to-tiny-C++ transpiler trial.

## Read First

1. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/SKILL.md`
2. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/docs/PROJECT-MANAGEMENT.md`
3. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/templates/LEDGER-DISCIPLINE.md`
4. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial/project-plan.md`
5. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial/arc01-foundation/arc-plan.md`
6. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial/arc01-foundation/slice01-crate-scaffold/slice-plan.md`
7. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial/arc01-foundation/slice01-crate-scaffold/ledger.md`
8. Rust domain skill: `/Users/oubiwann/.codex/skills/rust-guidelines/SKILL.md`
9. C++ domain skill: `/Users/oubiwann/.codex/skills/cpp-guidelines/SKILL.md`
10. Lykn references: `/Users/oubiwann/lab/lykn/lang/docs/guides/00-lykn-surface-forms.md` and `/Users/oubiwann/lab/lykn/lang/docs/guides/01-core-idioms.md`

Use only the collaboration framework from the `0.4.1` entrypoint above. Do not substitute the installed collaboration-framework skill or any other framework version.

## Working Directory

Work in:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial`

## Objective

Implement Arc 01 Slice 01: create the Rust crate and first vertical transpilation path for exactly `(print <integer-literal>)`.

## Implement

- Create a Rust package in the working directory.
- Keep `src/main.rs` thin and put testable logic in library modules.
- Expose `pub fn transpile(source: &str) -> Result<String, TranspileError>`.
- Define a structured `TranspileError` suitable for parser/diagnostic growth in later slices.
- Support exactly `(print 42)`-style input in this slice.
- Generate deterministic C++17 shaped like:

```cpp
#include <iostream>

int main() {
    std::cout << 42 << "\n";
    return 0;
}
```

- Add `docs/syntax.md` explaining the trial syntax, including the relationship to Lykn's `bind`, `console:log`, and prefix arithmetic examples.
- Add CLI behavior: read one source file argument and write generated C++ to stdout; diagnostics go to stderr with a non-zero exit.
- Add tests covering successful library transpilation, successful CLI transpilation, and one unsupported or malformed input diagnostic.
- Add `examples/print_literal.cpp` as the generated example.

## Do Not Implement

- Do not add `let` support yet.
- Do not add identifiers, arithmetic expressions, multiple statements, strings, comments, functions, conditionals, loops, source maps, or C++ compile/build-system generation.
- Do not perform the later code audit.
- Do not edit the framework source files.

## Validate

Run the ledger Verify commands from `ledger.md`, including:

```sh
cargo fmt --check
cargo test
cargo clippy -- -D warnings
```

If `clippy` or any optional local tool is unavailable, record the exact failure and a re-entry condition rather than weakening the row silently.

## Report Back

Update `ledger.md` with final statuses and evidence strength `attested` for completed rows. Then create `closing-report.md` in this slice directory with:

- the commit or working-tree state where the work landed,
- a row-by-row disposition for all 8 ledger rows,
- exact validation commands and outcomes,
- any deferrals or no-ops with rationale and re-entry conditions,
- a `Bubble-up to the arc` section answering whether the slice delivered its assigned Arc 01 piece, what it revealed, and whether there were any silent drops.

End by stating whether the slice is proposed-done and ready for CDC verification.
