# Arc 03 Slice 01 Plan: CLI and Example Surface

## Capability Statement

This slice gives the tiny transpiler a clearer executable surface for humans
and later auditors. It should add focused CLI coverage and one additional valid
fixture/generated C++ example while keeping the language subset, library API,
and existing diagnostics stable.

## Scope

In scope:

- preserve `transpile_to_cpp(source: &str) -> Result<String, TranspileError>`;
- add or harden focused CLI tests for successful transpilation and diagnostic
  failure output;
- add one additional valid fixture that uses only existing accepted forms;
- add the deterministic generated C++ counterpart for that fixture;
- compile and run all generated C++ examples when `c++` is available;
- keep Arc 01 and Arc 02 fixtures/tests passing.

Out of scope:

- new source-language forms;
- richer type checking;
- broad CLI framework adoption unless the current code already points that way;
- C++ build-system generation;
- the audit-readiness map, which is reserved for Arc 03 Slice 02.

## Implementation Notes

Prefer the existing crate structure and test style. The current CLI is expected
to remain thin; improvements should support testability and clear diagnostics
without turning the slice into a productized command-line tool.

The second valid example should exercise a different small expression shape
than `happy_path` while remaining easy to inspect. Good candidates include
nested arithmetic across existing bindings or a direct division case with a
non-zero literal denominator.

## Required Validation

Run from `../../../implementation/lykn-cpp-transpiler`:

```bash
cargo fmt --check
cargo check
cargo clippy -- -D warnings
cargo test
c++ -std=c++17 -Wall -Wextra -pedantic examples/generated/happy_path.cpp -o /private/tmp/lykn-cpp-transpiler-happy-path-arc03-slice01
/private/tmp/lykn-cpp-transpiler-happy-path-arc03-slice01
```

Also compile and run the new generated C++ example with an example-specific
output path under `/private/tmp`.

If `c++` is unavailable, record the exact missing-tool output in the close
report and leave C++ smoke evidence as blocked rather than silently dropping it.

## CDC Verification Focus

CDC should verify:

- CLI success and diagnostic failure behavior first;
- the second generated C++ example's deterministic output;
- that the source language did not widen;
- that existing Arc 01 and Arc 02 evidence still passes.

## Version History

| Version | Date | Change |
| --- | --- | --- |
| 1.0 | 2026-09-05 | Initial Slice 01 plan opened with Arc 03. |

