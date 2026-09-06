# Arc 02 Plan: Diagnostics and Negative Coverage

## Capability Statement

Arc 02 stabilizes the diagnostic surface left after Arc 01 by adding a small,
explicit negative-coverage matrix for the tiny language. It should make the
error boundary easier to audit without widening the accepted language or
turning the trial into a fuller compiler.

This arc is intentionally narrower than the original roadmap wording because
Arc 01 Slice 02 already delivered basic malformed-expression, unsupported-form,
unknown-identifier, duplicate-binding, C++-unsafe-identifier, invalid-CLI, and
direct literal divide-by-zero coverage.

## Dependencies

Consumes:

- Closed Arc 01 evidence from `../arc01-minimum-language-core/closing-report.md`.
- Slice 02 diagnostic structures in `implementation/lykn-cpp-transpiler/src/error.rs`.
- Existing fixture/test conventions under `implementation/lykn-cpp-transpiler`.

Leaves for later arcs:

- CLI comfort beyond current input-path behavior.
- Additional generated examples beyond the happy path.
- Audit surface map and code-audit pass.
- Any accepted-language expansion.

## Slice Breakdown

| Slice | Scope | Load-Bearing For |
| --- | --- | --- |
| Slice 01: Diagnostic Coverage Matrix | Add a compact invalid-fixture/test matrix for remaining parse/codegen boundary cases and preserve current accepted-language behavior. | Gives Arc 03 and the later audit pass a clearer negative-evidence surface. |

This slice uses the arc-local planning layout and is named Arc 02 Slice 01.

## Arc Validation Approach

Arc 02 closes when:

- the planned diagnostic matrix slice is independently verified;
- the accepted language has not widened;
- each invalid fixture maps to a structured diagnostic category;
- all standard validation gates still pass;
- the arc ledger rows are walked and composition is demonstrated at arc scale.

## Current Status

Slice 01 is CDC-verified. Arc 02 is formally closed as of 2026-09-05. No
additional Arc 02 slice is currently indicated by slice close evidence.

## Version History

| Version | Date | Change |
| --- | --- | --- |
| 1.2 | 2026-09-05 | Recorded formal Arc 02 close after arc-scale composition verification. |
| 1.1 | 2026-09-05 | Recorded Slice 01 CDC closure and Arc 02 eligibility for formal close; no slice breakdown change required. |
| 1.0 | 2026-09-05 | Initial Arc 02 plan, narrowed from the original roadmap after Arc 01 Slice 02 absorbed the basic diagnostic-hardening work. |
