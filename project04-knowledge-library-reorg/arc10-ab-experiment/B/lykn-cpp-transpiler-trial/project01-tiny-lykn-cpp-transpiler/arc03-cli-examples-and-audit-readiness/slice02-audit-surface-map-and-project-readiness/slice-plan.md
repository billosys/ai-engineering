# Arc 03 Slice 02 Plan: Audit Surface Map and Project Readiness

## Capability Statement

This slice records the final audit-readiness substrate for the tiny transpiler
trial. It should map the implementation surfaces that a later diagnosis-only
code audit must cover and gather project-readiness evidence against the project
ledger, without performing the audit itself.

## Scope

In scope:

- create an audit surface map under `artifacts/`;
- identify first-party Rust implementation surfaces, generated C++ examples,
  fixtures, tests, CLI/API boundaries, diagnostics, and validation gates;
- distinguish first-party source, generated examples, fixtures, tests,
  transient build outputs, and temporary smoke binaries;
- create a project-readiness evidence artifact that walks project ledger rows
  `P-01` through `P-06` with evidence pointers and any remaining gate needs;
- re-run the existing Rust validation gates and both generated C++ smoke
  examples;
- preserve implementation behavior unless the evidence walk reveals a blocker
  that cannot be honestly recorded without a small fix.

Out of scope:

- performing the later code-quality audit;
- writing final audit reports such as `*-audit-results-rust.md`;
- broad refactoring or source-language expansion;
- changing generated C++ semantics;
- packaging, release, or publication work.

## Artifact Home

Durable artifacts for this slice belong in:

- `artifacts/audit-surface-map.md`
- `artifacts/project-readiness-evidence.md`

Use those filenames unless CC records a concrete reason to amend the slice
plan and prompt.

## Implementation Notes

This should be mostly documentation and evidence work. If CC finds a
validation failure or a mismatch between the plan and implementation, record
the exact blocker and re-entry condition rather than papering over it. Only
make source changes if they are necessary to keep the project honest and still
fit the slice; otherwise defer them with rationale.

The audit surface map should be useful to a fresh later auditor. It should
answer: what is first-party, what is generated, what is fixture/test evidence,
what is transient, what contracts cross module boundaries, and which language
or domain guidance is relevant.

## Required Validation

Run from `../../../implementation/lykn-cpp-transpiler`:

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

Also use direct inspection commands for the map evidence, such as:

```bash
find src tests fixtures examples -maxdepth 3 -type f | sort
rg -n "transpile_to_cpp|ParseError|CodegenError|TranspileError|let|print" src tests fixtures examples
```

If `c++` is unavailable, record the exact missing-tool output in the close
report and readiness artifact.

## CDC Verification Focus

CDC should verify:

- the audit surface map covers all implementation surfaces and excludes
  transient outputs;
- the project-readiness evidence walks all project ledger rows without
  prematurely claiming independent project closure;
- validation commands reproduce;
- no source-language or generated-C++ behavior changed unexpectedly;
- Slice 02's bubble-up gives CDC enough evidence to close Arc 03 and assess
  project readiness for the later audit pass.

## Version History

| Version | Date | Change |
| --- | --- | --- |
| 1.0 | 2026-09-05 | Initial Slice 02 plan opened after Arc 03 Slice 01 CDC closure. |

