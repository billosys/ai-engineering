# CC Prompt: Arc 03 Slice 01 - CLI and Example Surface

You are CC implementing Arc 03 Slice 01 for the Lykn C++ transpiler trial.

Run label: `framework-main-pre-0.5.0`.

## Required Context

Read and follow the assigned in-repo framework entrypoint:

- `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/collaboration-framework/SKILL.md`

Also load the relevant framework project-management close guidance and
work-verification ledger/row/silent-drop guidance from the same repository.

Domain references:

- Rust guidelines for crate/API/CLI/test idioms.
- C++ guidelines for generated C++17 output.
- Lykn surface-form guide only for inspiration and scope guardrails.

## Planning Packet

Project root:

- `/Users/oubiwann/lab/billosys/ai-engineering/workbench/lykn-cpp-transpiler-trial/project01-tiny-lykn-cpp-transpiler/project-plan.md`

Arc:

- `../arc-plan.md`
- `../ledger.md`

Slice:

- `slice-plan.md`
- `ledger.md`

Prior evidence:

- `../../arc01-minimum-language-core/closing-report.md`
- `../../arc02-diagnostics-and-negative-coverage/closing-report.md`

Implementation root:

- `/Users/oubiwann/lab/billosys/ai-engineering/workbench/lykn-cpp-transpiler-trial/implementation/lykn-cpp-transpiler`

## Task

Implement the CLI and example-surface slice.

Keep the work tightly scoped:

- Preserve the public library API.
- Add focused automated CLI coverage for success and diagnostic failure paths.
- Add one additional valid fixture using only existing accepted forms.
- Add the deterministic generated C++ counterpart for that new fixture.
- Preserve the existing `happy_path` fixture/example and all invalid diagnostic
  coverage.
- Do not widen the accepted source language.

The CLI may stay thin. Improve it only as needed to make behavior clear,
testable, and comfortable for this trial.

## Required Validation

Run from the implementation root:

```bash
cargo fmt --check
cargo check
cargo clippy -- -D warnings
cargo test
c++ -std=c++17 -Wall -Wextra -pedantic examples/generated/happy_path.cpp -o /private/tmp/lykn-cpp-transpiler-happy-path-arc03-slice01
/private/tmp/lykn-cpp-transpiler-happy-path-arc03-slice01
```

Also compile and run the new generated C++ example with an example-specific
binary path under `/private/tmp`.

If C++ compilation is unavailable, record the exact blocker instead of omitting
the evidence.

## Close Report

Create:

- `closing-report.md`

The close report must include:

- run label and framework/reference files used;
- implementation summary;
- files changed or added;
- exact validation commands and observed results;
- ledger row walk for S01-01 through S01-09;
- explicit statement that accepted syntax was not widened, or the exact
  scope-change rationale if you believe widening is unavoidable.

Leave the slice status as proposed-done pending CDC verification.

