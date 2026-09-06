# CC Prompt: Arc 03 Slice 02 - Audit Surface Map and Project Readiness

You are CC implementing Arc 03 Slice 02 for the Lykn C++ transpiler trial.

Run label: `framework-main-pre-0.5.0`.

## Required Context

Read and follow the assigned in-repo framework entrypoint:

- `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/collaboration-framework/SKILL.md`

Also load from the same repository:

- the project-management planning and slice-close guidance;
- work-verification ledger, row-closure, evidence-strength, independent
  verification, and silent-drop guidance;
- code-auditing audit-scope/map guidance, only for map shape and audit
  readiness. Do not perform the audit.

Domain references:

- Rust guidelines for crate/API/CLI/test audit surfaces.
- C++ guidelines for generated C++17 subset review surfaces.
- Lykn surface-form guide only for syntax-scope context.

## Planning Packet

Project:

- `/Users/oubiwann/lab/billosys/ai-engineering/workbench/lykn-cpp-transpiler-trial/project01-tiny-lykn-cpp-transpiler/project-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/workbench/lykn-cpp-transpiler-trial/project01-tiny-lykn-cpp-transpiler/ledger.md`

Arc:

- `../arc-plan.md`
- `../ledger.md`

Slice:

- `slice-plan.md`
- `ledger.md`

Prior evidence:

- `../slice01-cli-and-example-surface/cdc-verification.md`
- `../../arc01-minimum-language-core/closing-report.md`
- `../../arc02-diagnostics-and-negative-coverage/closing-report.md`

Implementation root:

- `/Users/oubiwann/lab/billosys/ai-engineering/workbench/lykn-cpp-transpiler-trial/implementation/lykn-cpp-transpiler`

## Task

Create the audit-readiness and project-readiness artifacts for this tiny
transpiler trial.

Create:

- `artifacts/audit-surface-map.md`
- `artifacts/project-readiness-evidence.md`

Keep the work tightly scoped:

- Map the surfaces a later diagnosis-only code audit must inspect.
- Distinguish first-party Rust source, generated C++ examples, fixtures,
  tests, transient `target/` outputs, and `/private/tmp` smoke binaries.
- Name the important contracts: public library API, CLI stdout/stderr/exit
  behavior, structured diagnostics, accepted syntax, deterministic generated
  output, and validation gates.
- Walk project ledger rows `P-01` through `P-06` with evidence pointers,
  readiness status, blockers if any, and clear CDC/project-close re-entry
  conditions.
- Preserve implementation behavior. Do not widen accepted syntax.

Do not:

- perform the later code audit;
- create final audit report files;
- refactor production source merely for polish;
- change generated C++ semantics;
- mark the project independently closed.

## Required Validation

Run from the implementation root:

```bash
cargo fmt --check
cargo check
cargo clippy -- -D warnings
cargo test
c++ -std=c++17 -Wall -Wextra -pedantic examples/generated/happy_path.cpp -o /private/tmp/lykn-cpp-transpiler-happy-path-arc03-slice02
/private/tmp/lykn-cpp-transpiler-happy-path-arc03-slice02
c++ -std=c++17 -Wall -Wextra -pedantic examples/generated/arithmetic_mix.cpp -o /private/tmp/lykn-cpp-transpiler-arithmetic-mix-arc03-slice02
/private/tmp/lykn-cpp-transpiler-arithmetic-mix-arc03-slice02
```

Also inspect the source and evidence surface with commands equivalent to:

```bash
find src tests fixtures examples -maxdepth 3 -type f | sort
rg -n "transpile_to_cpp|ParseError|CodegenError|TranspileError|let|print" src tests fixtures examples
```

If C++ compilation is unavailable, record the exact blocker instead of
omitting the evidence.

## Close Report

Create:

- `closing-report.md`

The close report must include:

- run label and framework/reference files used;
- implementation summary;
- files changed or added;
- exact validation commands and observed results;
- ledger row walk for S02-01 through S02-10;
- artifact inventory;
- explicit statement that this slice did not perform the later audit;
- explicit statement that project ledger evidence is readiness evidence, not
  independent project closure;
- bubble-up to Arc 03, including whether CDC should proceed to formal Arc 03
  close and project-readiness assessment.

Leave the slice status as proposed-done pending CDC verification.

