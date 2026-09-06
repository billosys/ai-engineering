# Arc 03 Plan: CLI, Examples, and Audit Readiness

## Capability Statement

Arc 03 prepares the completed tiny transpiler for the later code-audit pass by
making its executable surface easier to verify, adding one more valid generated
C++ example, and recording a compact audit-readiness map.

This arc should not expand the accepted language. Its purpose is polish,
evidence, and auditability around the parser/API/codegen/error/CLI/test surface
already created by Arcs 01 and 02.

## Dependencies

Consumes:

- Arc 01 close evidence from `../arc01-minimum-language-core/closing-report.md`.
- Arc 02 close evidence from `../arc02-diagnostics-and-negative-coverage/closing-report.md`.
- Existing implementation under `../../implementation/lykn-cpp-transpiler`.

Leaves for later work:

- The actual framework-effectiveness code audit.
- Any language expansion beyond the tiny integer S-expression subset.
- Packaging, release, or publication work for the trial crate.

## Slice Breakdown

| Slice | Scope | Load-Bearing For |
| --- | --- | --- |
| Slice 01: CLI and Example Surface | Add focused CLI behavior coverage and a second valid fixture/generated C++ example while preserving the existing API and diagnostics. | Gives users and later auditors clearer executable evidence beyond the first happy path. |
| Slice 02: Audit Surface Map and Project Readiness | Record a concise audit surface map, walk project-level evidence, and close the project as ready for the later audit. | Provides the handoff substrate for the later framework-effectiveness audit pass. |

## Arc Validation Approach

Arc 03 closes when:

- CLI behavior has focused tests for success and diagnostic failure paths;
- at least two valid generated C++ examples exist and are deterministic;
- available generated C++ examples compile and run under C++17, or the exact
  missing-tool blocker is recorded;
- the audit-readiness map identifies parser/API/error/codegen/CLI/test surfaces;
- project and arc ledger rows are walked with reproduced evidence;
- no accepted-language expansion occurs without an explicit scope-change note.

## Current Status

Arc 03 is formally closed as of 2026-09-05. Slice 01 and Slice 02 are both
CDC-verified and closed. No additional Arc 03 slice is indicated by current
evidence.

## Version History

| Version | Date | Change |
| --- | --- | --- |
| 1.3 | 2026-09-05 | Recorded formal Arc 03 close after Slice 02 CDC verification and arc-scale composition verification. |
| 1.2 | 2026-09-05 | Opened Slice 02 after Slice 01 CDC closure; artifact home is `slice02-audit-surface-map-and-project-readiness/artifacts/`. |
| 1.1 | 2026-09-05 | Recorded Slice 01 CDC closure; no arc scope or sequencing change required. |
| 1.0 | 2026-09-05 | Initial Arc 03 plan opened after formal Arc 02 close. |
