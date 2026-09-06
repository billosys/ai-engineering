# Arc 02: Expressions and Semantics

## Capability

Arc 02 extends the Arc 01 literal foundation into the full tiny expression
subset promised by the project: prefix arithmetic expressions with integer and
identifier leaves, expression-valued `let` initializers, expression-valued
`print` statements, deterministic C++ infix emission, and structured diagnostics
for malformed expressions and semantic mistakes. It should deepen the existing
parser/AST/codegen surface without turning the trial into a full compiler.

## Dependencies

- consumes: Arc 01 CDC closure, the Arc 01 parser/AST/codegen/error/CLI
  structure, and the project-plan v1.2 refinement that baseline let literals,
  simple identifiers, and unknown-identifier checks already landed in Arc 01
- leaves for Arc 03: representative fixture files, generated example coverage
  beyond one or two examples, optional C++ compiler execution, audit map, and
  final documentation polish
- keeps out of scope: full Lykn compatibility, JavaScript semantics, comments,
  strings, functions, conditionals, loops, arrays, objects, modules, source
  maps, build-system generation, optimization, and multi-file C++ output

## Slice Breakdown

| Slice | Scope | Load-bearing for | Status |
|-------|-------|------------------|--------|
| Slice 01: Recursive Arithmetic Core | Add recursive binary prefix arithmetic forms `(+ a b)`, `(- a b)`, `(* a b)`, and `(/ a b)` with integer and identifier leaves; allow expressions in `let` initializers and `print`; emit deterministic parenthesized C++ infix expressions; preserve Arc 01 behavior. | Slice 02 semantic closure and Arc 03 fixtures | closed |
| Slice 02: Semantic And Diagnostic Closure | Harden malformed-expression diagnostics, operator arity handling, nested identifier resolution edges, final full-subset acceptance coverage, and syntax documentation so Arc 02 closes the full tiny expression subset cleanly. | Arc 03 audit-readiness work | closed |

## Arc Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| A-1 | Slice 01 closes with recursive arithmetic expressions through the public API and CLI while preserving Arc 01 behavior. | Read `slice01-recursive-arithmetic-core/cdc-verification.md`. | correctness | arc-plan | done | attested: `slice01-recursive-arithmetic-core/cdc-verification.md` verifies 13 rows closed on 2026-09-05 | CDC-closed slice |
| A-2 | Slice 02 closes the remaining expression diagnostics and semantic edge cases for the full tiny subset. | Read `slice02-*/cdc-verification.md`. | correctness | arc-plan | done | attested: `slice02-semantic-diagnostic-closure/cdc-verification.md` verifies 13 rows closed on 2026-09-05 | CDC-closed slice |
| A-3 | Arc 02 slices compose into the full tiny expression subset. | From the trial workspace, run a valid nested arithmetic program and representative invalid expression programs through the CLI, then inspect generated C++ and diagnostics. | serious | arc-plan | done | attested: `closing-report.md` records valid full-subset CLI output plus unsupported-operator, extra-operand, before-bound identifier, and missing-close diagnostics on 2026-09-05 | reproduce at arc scale |
| A-4 | Slice bubble-up findings are dispositioned before Arc 03 starts. | Inspect this file's Version History and both slice close bubble-up sections. | serious | arc-plan | done | attested: `closing-report.md` records both slice bubble-ups inspected with no Arc 02 or project scope change required | required before next arc |

## Validation Approach

Arc 02 validation remains Rust-first and output-contract focused:

- targeted library tests for expression parsing, semantic validation, and
  generated C++ output
- targeted CLI tests for a valid arithmetic program and at least one expression
  diagnostic
- `cargo fmt --check`
- `cargo test`
- `cargo clippy -- -D warnings`
- text inspection of generated C++ to confirm stable parenthesized infix output

Arc 02 may add one generated C++ example, but broad fixture suites and optional
C++ compiler execution remain Arc 03 work unless Slice 02 discovers that Arc 02
cannot close honestly without a narrower supporting check.

## Version History

- v1.4, 2026-09-05: Closed Arc 02 after arc-level composition checking. Recorded A-3 and A-4 closure evidence. No project-plan scope change was required; Arc 03 is eligible to open.
- v1.3, 2026-09-05: Closed Slice 02 after CDC verification. Recorded A-2 child-close evidence. No Arc 02 scope or sequencing change was required; Arc 02 is ready for arc-level composition checking.
- v1.2, 2026-09-05: Opened Slice 02 after Slice 01 CDC verification. Kept Arc 02 scope unchanged, but made the Slice 02 breakdown explicit about final full-subset acceptance coverage in addition to diagnostic and semantic closure.
- v1.1, 2026-09-05: Closed Slice 01 after CDC verification. Recorded A-1 child-close evidence. No Arc 02 scope or sequencing change was required; Slice 02 remains planned for diagnostic and semantic closure.
- v1.0, 2026-09-05: Opened Arc 02 after Arc 01 CDC closure. Planned two slices:
  recursive arithmetic core first, then semantic and diagnostic closure.
