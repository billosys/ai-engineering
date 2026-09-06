# Arc 01 Plan: Minimum Language Core

## Capability Statement

Arc 01 establishes the smallest real transpiler: a Rust crate with a testable
library API, thin CLI, AST/parser/codegen modules, valid and invalid fixtures,
and deterministic C++17 output for a tiny Lykn-inspired language.

This arc should leave enough code for meaningful CDC verification and future
audit, while keeping the accepted syntax intentionally narrow.

## Dependencies

Consumes:

- The project plan's trial scope and target C++ subset.
- Lykn reference cues from `bind`, `console:log`, S-expression surface syntax,
  and number-oriented examples.
- Rust guidance for crate layout, library/binary separation, and structured
  errors.
- C++ guidance for scoped initialized locals, standard-library I/O, immutable
  data, explicit expression grouping, and excluded feature families.

Leaves for later arcs:

- Broader diagnostics and negative coverage.
- CLI polish beyond input-path to stdout.
- C++ compiler smoke if the first slice does not have a local C++17 compiler.
- Audit pass itself.

## Slice Breakdown

| Slice | Scope | Load-Bearing For |
| --- | --- | --- |
| Slice 01: Crate Scaffold and Happy Path | Create the Rust crate, AST/parser/codegen baseline, first valid fixture, first invalid fixture, library API, thin CLI, and initial tests. | Establishes all later code surfaces. |
| Slice 02: First Diagnostic Hardening | Add explicit unknown identifier, malformed expression, unsupported form, and divide-by-zero diagnostics with invalid fixtures. | Enables Arc 02 to expand negative behavior without redesigning errors. |

Slice 02 has CC closure and CDC verification. With both planned slices closed
and arc-scale composition verified, Arc 01 is formally closed.

## Arc Validation Approach

Arc 01 closes when:

- both planned slices are independently verified;
- valid fixture transpilation is deterministic;
- invalid fixture behavior is structured enough for later hardening;
- the crate layout has the expected audit surfaces;
- the arc ledger rows are walked and composition is demonstrated at arc scale.

## Current Status

Slice 01 and Slice 02 are CDC-verified. Arc 01 is formally closed. No
additional Arc 01 slice is currently indicated by slice close or arc close
evidence.

## Version History

| Version | Date | Change |
| --- | --- | --- |
| 1.3 | 2026-09-05 | Recorded formal Arc 01 close after arc-scale composition verification; no additional Arc 01 slice indicated. |
| 1.2 | 2026-09-05 | Recorded Slice 02 CDC closure and Arc 01 eligibility for formal close; no slice breakdown change required. |
| 1.1 | 2026-09-05 | Opened Slice 02 after Slice 01 CDC verification and recorded the diagnostic-hardening boundary. |
| 1.0 | 2026-09-05 | Initial Arc 01 plan. |
