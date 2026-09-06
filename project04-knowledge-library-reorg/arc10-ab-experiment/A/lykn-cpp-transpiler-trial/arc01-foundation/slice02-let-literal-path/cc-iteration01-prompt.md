# CC Iteration 01 Prompt: Arc 01 Slice 02 Test Isolation Failure

You are CC for the `framework-0.4.1` trial. Slice 02 did not pass CDC
verification. Do not create `cdc-verification.md`; CDC owns that after the
next proposed-done report.

Workspace:

```text
/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial
```

## Read First

Use only the assigned collaboration framework root:

```text
/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1
```

Read:

- `workbench/cdc-project-prompt.md` from the framework root above
- `SKILL.md` from the framework root above
- `templates/LEDGER-DISCIPLINE.md` from the framework root above, especially Section A
- `arc01-foundation/arc-plan.md`
- `arc01-foundation/slice02-let-literal-path/slice-plan.md`
- `arc01-foundation/slice02-let-literal-path/ledger.md`
- `arc01-foundation/slice02-let-literal-path/closing-report.md`
- `tests/cli.rs`

## CDC Finding

CDC reproduced all focused Slice 02 ledger checks, but the full validation gate
failed once under normal `cargo test`.

Failing command:

```text
cargo test
```

Observed failure:

```text
test cli_print_literal_writes_cpp_to_stdout ... FAILED

assertion `left == right` failed
  left: "#include <iostream>\n\nint main() {\n    int x{40};\n    std::cout << x << \"\\n\";\n    std::cout << 42 << \"\\n\";\n    return 0;\n}\n"
 right: "#include <iostream>\n\nint main() {\n    std::cout << 42 << \"\\n\";\n    return 0;\n}\n"
```

The same CLI test suite passed on a focused rerun, and `cargo test --
--test-threads=1` passed. That pattern points to a parallel test-isolation
failure, not a deterministic transpiler logic failure.

The likely cause is `tests/cli.rs::write_temp_source`, which constructs temp
file names from only `std::process::id()` and `SystemTime::now().as_nanos()`.
Parallel tests in the same process can receive the same timestamp resolution
and write different source programs to the same path.

## Required Fix

Fix the CLI integration tests so each test uses a reliably unique temporary
source path under normal parallel `cargo test`.

Acceptable approaches:

- include the test name or an atomic counter in the filename,
- create a per-test temporary directory,
- or use another dependency-free strategy that guarantees no cross-test path collision.

Keep the fix scoped to Slice 02 test isolation unless you discover a real
transpiler bug.

## Required Verification

Run these from the trial workspace:

```text
cargo fmt --check
cargo test
cargo clippy -- -D warnings
```

Also rerun the focused CLI tests:

```text
cargo test cli_print_literal
cargo test cli_let_literal
cargo test cli_semantic_error
```

## Required Report

Update `arc01-foundation/slice02-let-literal-path/ledger.md` and
`arc01-foundation/slice02-let-literal-path/closing-report.md` with the new
attested evidence.

In the closing report, add an Iteration 01 note that includes:

- the root cause of the CDC failure,
- the exact fix,
- the commands rerun,
- whether any ledger row disposition changed,
- whether the Bubble-up to the arc changed.

Then report back to CDC with the revised proposed-done status.
