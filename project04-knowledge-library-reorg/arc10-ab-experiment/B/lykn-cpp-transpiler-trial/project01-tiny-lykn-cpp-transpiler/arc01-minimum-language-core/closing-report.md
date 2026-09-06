# Closing Report: Arc 01

Metadata:

| Field | Value |
| --- | --- |
| project | project01-tiny-lykn-cpp-transpiler |
| arc | arc01-minimum-language-core |
| role | CDC |
| status | closed |
| run label | `framework-main-pre-0.5.0` |
| repository HEAD observed | `c97b4e42e441b9bdd0a29a37ac1be508696ab9c0` |
| source commit | not applicable; trial implementation lives under ignored `workbench/` |
| close date | 2026-09-05 |

## Capability Verdict

Arc 01 promised the smallest real transpiler: a Rust crate with a testable
library API, thin CLI, AST/parser/codegen modules, valid and invalid fixtures,
and deterministic C++17 output for a tiny Lykn-inspired language.

Verdict: delivered. The arc now has a working crate under
`implementation/lykn-cpp-transpiler`, CDC-verified Slice 01 and Slice 02 close
artifacts, structured parser/codegen errors, tests, fixtures, a generated C++
example, and a C++17 smoke run.

## Slice Walk

| Slice | Outcome | Evidence |
| --- | --- | --- |
| Slice 01: Crate Scaffold and Happy Path | delivered, CDC-verified | `slice01-crate-scaffold-and-happy-path/cdc-verification.md` |
| Slice 02: First Diagnostic Hardening | delivered, CDC-verified | `slice02-diagnostic-hardening/cdc-verification.md` |

The slice count matches the `arc-plan.md` slice breakdown. No Arc 01 slice is
missing, deferred, or dropped.

## Composition Check

Arc capability as specified:

- crate/API/parser/codegen/test surfaces exist;
- valid fixture transpilation is deterministic;
- invalid fixture behavior is structured enough for later hardening;
- generated C++ remains inside the tiny C++17 subset;
- both planned slices are independently verified.

Arc capability as delivered:

- `cargo test` passed with 13 integration tests;
- `target/debug/lykn-cpp-transpiler fixtures/valid/happy_path.lykn` emitted the
  expected deterministic C++ source;
- `examples/generated/happy_path.cpp` compiled under C++17 with warnings
  enabled;
- the compiled smoke binary printed `9`;
- generated examples contain none of the excluded C++ constructs searched in
  the arc composition pass;
- Slice 01 and Slice 02 CDC verification files close every slice ledger row.

Commands reproduced from `implementation/lykn-cpp-transpiler`:

| Command | Result |
| --- | --- |
| `cargo test` | pass: 13 integration tests, 0 unit tests, 0 doc tests |
| `target/debug/lykn-cpp-transpiler fixtures/valid/happy_path.lykn` | pass: emitted expected C++ source |
| `rg -n "\b(class|template|new|delete|throw|try|catch|#define|auto|std::vector|std::string|malloc|free|->|&)\b" examples/generated` | pass: no matches |
| `c++ -std=c++17 -Wall -Wextra -pedantic examples/generated/happy_path.cpp -o /private/tmp/lykn-cpp-transpiler-arc01-close` | pass |
| `/private/tmp/lykn-cpp-transpiler-arc01-close` | pass: printed `9` |

## Arc Ledger Walk

### A01-01

Status: done, reproduced.

Evidence: `slice01-crate-scaffold-and-happy-path/cdc-verification.md` closes
Slice 01 with reproduced evidence for the crate, API, parser, codegen, tests,
fixtures, CLI, and generated C++ example.

### A01-02

Status: done, reproduced.

Evidence: `slice02-diagnostic-hardening/cdc-verification.md` closes Slice 02
with reproduced evidence for first diagnostic hardening without widening the
accepted source language.

### A01-03

Status: done, reproduced.

Evidence: the arc composition commands above demonstrate that the two slices
compose into a minimum useful transpiler from tiny source to deterministic
C++17 output.

### A01-04

Status: done, reproduced.

Evidence: Slice 01 and Slice 02 bubble-ups were compared against
`arc-plan.md`. The only required changes were status updates and the recording
of close eligibility; no arc scope, sequencing, or slice breakdown change was
required.

## Accumulated Arc-Plan Change Log

`arc-plan.md` version history records:

- `1.1`, 2026-09-05: opened Slice 02 after Slice 01 CDC verification and
  recorded the diagnostic-hardening boundary.
- `1.2`, 2026-09-05: recorded Slice 02 CDC closure and Arc 01 eligibility for
  formal close.

This close adds the final Arc 01 status update; it does not change the slice
breakdown.

## Bubble-Up To Project

Arc 01 delivered the project-roadmap capability for Minimum Language Core. It
established the crate shape, parser/AST/codegen/error/CLI/test surfaces,
deterministic happy-path C++ output, first invalid fixtures, and initial
diagnostic hardening.

What Arc 01 revealed: the original Arc 02 roadmap item overlapped with work
that landed early in Arc 01 Slice 02. Arc 02 should therefore focus on a
diagnostic coverage matrix and remaining negative boundary cases, rather than
repeating the already-verified basic malformed/unsupported/unknown/divide-by-zero
coverage.

Project-plan impact: Arc 01 status was updated to closed, Arc 02 was marked
active, and the narrowed Arc 02 interpretation was recorded in the project plan
before opening Arc 02 Slice 01.

Silent-drop diff: no Arc 01 roadmap item is known to be missing.

## Verdict

Arc 01 is closed.

Next eligible work: plan Arc 02 in detail and open Arc 02 Slice 01.
