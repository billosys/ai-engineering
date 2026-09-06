# Arc 01 Framework Comparison: 0.4.1 vs Main Pre-0.5.0

Date: 2026-09-05

## Question

Does Arc 01 of the Lykn-to-tiny-C++ trial provide enough evidence to detect
early framework regressions between `framework-0.4.1` and
`framework-main-pre-0.5.0`?

## Short Answer

Yes, for preliminary planning and execution behavior. No, not yet for final
code-audit performance.

Arc 01 provides enough evidence to compare planning shape, scope control, CC
handoff quality, validation discipline, CDC closure behavior, friction, and
implementation surface. The later audit-pass comparison still needs a richer
post-Arc02 or post-Arc03 codebase and a same-framework audit pass in both
conditions.

## Conditions Compared

| Condition | Framework entrypoint | Trial workspace |
| --- | --- | --- |
| `framework-0.4.1` | `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/SKILL.md` | `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial` |
| `framework-main-pre-0.5.0` | `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/collaboration-framework/SKILL.md` | `/Users/oubiwann/lab/billosys/ai-engineering/workbench/lykn-cpp-transpiler-trial` |

## Evidence Reviewed

### 0.4.1

- `project-plan.md`
- `arc01-foundation/arc-plan.md`
- `arc01-foundation/closing-report.md`
- `arc01-foundation/slice01-crate-scaffold/{cc-prompt.md,ledger.md,closing-report.md,cdc-verification.md}`
- `arc01-foundation/slice02-let-literal-path/{cc-prompt.md,cc-iteration01-prompt.md,ledger.md,closing-report.md,cdc-verification.md}`
- Rust crate under the trial workspace root

### Main Pre-0.5.0

- `evaluation-notes.md`
- `project01-tiny-lykn-cpp-transpiler/project-plan.md`
- `project01-tiny-lykn-cpp-transpiler/ledger.md`
- `project01-tiny-lykn-cpp-transpiler/arc01-minimum-language-core/{arc-plan.md,ledger.md,closing-report.md}`
- `project01-tiny-lykn-cpp-transpiler/arc01-minimum-language-core/slice01-crate-scaffold-and-happy-path/{cc-prompt.md,ledger.md,closing-report.md,cdc-verification.md}`
- `project01-tiny-lykn-cpp-transpiler/arc01-minimum-language-core/slice02-diagnostic-hardening/{cc-prompt.md,ledger.md,closing-report.md,cdc-verification.md}`
- Rust crate under `implementation/lykn-cpp-transpiler`

## Reproduced Checks

### 0.4.1

- `cargo fmt --check`: pass
- `cargo test`: pass, 8 library tests and 4 CLI integration tests
- `cargo clippy -- -D warnings`: pass
- CLI smoke using a temp file containing `(print 42)`: pass, emitted complete
  C++17 source that prints `42`
- Rust source and test surface: 732 lines across `src/` and `tests/`

### Main Pre-0.5.0

- `cargo fmt --check`: pass
- `cargo test`: pass, 13 integration tests
- `cargo clippy -- -D warnings`: pass
- CLI smoke using a temp file containing:

  ```lykn
  (let x 1)
  (let y (+ x 2))
  (print (* y 3))
  ```

  pass, emitted complete C++17 source using `const int`, prefix arithmetic,
  and `std::cout`
- Rust source and test surface: 903 lines across `src/` and `tests/`

## Rubric

Scale: 0-3.

| Measure | 0.4.1 | Main pre-0.5.0 | Difference |
| --- | --- | --- | --- |
| Framework isolation and run setup | 2 | 3 | 0.4.1 recorded that installed framework/memory were opened before the scientific-control constraint was read; main recorded cleaner assigned-framework loading. |
| Planning structure and wayfinding | 2 | 3 | Main used the current project/arc/slice directory shape, separate project ledger, and clearer implementation/planning separation. 0.4.1 was coherent but flatter and less normalized. |
| Scope control | 3 | 2 | 0.4.1 stayed closer to the "tiny and incremental" spirit. Main front-loaded arithmetic and broader diagnostics into Arc 01; useful, but more ambitious. |
| CC prompt actionability | 2 | 3 | Main prompts carried tighter boundaries, validation expectations, and CDC handoff structure. 0.4.1 prompts were usable but needed a follow-up iteration on Slice 02. |
| Evidence and closure discipline | 2 | 3 | Both produced CDC verifications and arc close reports. Main showed more systematic row naming, reproduced gates, and arc/project bubble-up. 0.4.1 recovered well after a CDC blocker. |
| Validation depth | 2 | 3 | Both passed Rust format/test/clippy. Main also included C++17 compile/run smoke during Arc 01; 0.4.1 deferred C++ compilation. |
| Implementation quality for Arc 01 scope | 2 | 3 | Both are green and usable. Main has a richer AST/parser/codegen/error surface, fixtures, structured diagnostics, and generated C++ smoke. 0.4.1 is simpler and still sound for its narrower scope. |
| Audit readiness | 2 | 3 | Main is more audit-ready after Arc 01 because it already has arithmetic, fixture variety, C++ compile evidence, and more diagnostic boundaries. 0.4.1 needs Arc 02 before audit findings would be as meaningful. |
| Friction and recovery | 2 | 3 | 0.4.1 required an iteration for a normal parallel-test collision. The recovery was good, but the extra pass is still friction. Main closed Arc 01 without a comparable blocker. |

Indicative totals:

- `framework-0.4.1`: 19/27
- `framework-main-pre-0.5.0`: 26/27

The total is directional, not a final verdict. The categories are more useful
than the arithmetic.

## Observations

### Main Pre-0.5.0 Strengths

- Better project shape: canonical `project01-...` directory, project ledger,
  arc ledger, slice ledgers, and implementation subdirectory.
- Stronger wayfinding: planning and implementation surfaces were easier to
  locate and compare.
- Stronger evidence discipline: CDC verifications clearly separated CC claims
  from reproduced evidence.
- Stronger validation: Arc 01 included Rust gates plus C++17 compile/run smoke.
- Better audit readiness: richer parser, AST, codegen, errors, invalid
  fixtures, and generated example.

### 0.4.1 Strengths

- Very good scope restraint. It resisted turning Arc 01 into the whole tiny
  language.
- The iteration was handled correctly: the failed full `cargo test` result was
  preserved, root-caused as a test-isolation issue, repaired narrowly, and
  reverified.
- The simpler implementation is easier to reason about and may be less likely
  to hide an overbuilt design.

### Main Pre-0.5.0 Caution

The current framework did not violate the trial scope, but it did front-load
more capability into Arc 01. That appears beneficial in this run because the
work remained small and produced better audit surface. It is still worth
watching as a possible "quality pressure expands scope" failure mode in larger
tests.

### 0.4.1 Caution

The older framework produced coherent work, but the flatter layout and weaker
normalization made comparison and closure slightly more effortful. The
recorded contamination caveat around installed framework/memory access is also
a scientific-control weakness, even though the run states those sources were
not used as authority.

## Regression Assessment

This Arc 01 run does not show a regression in the main/pre-0.5.0 framework.
It supports an early improvement signal in:

- planning/wayfinding,
- evidence capture,
- CDC verification clarity,
- validation depth,
- audit-readiness of produced code.

The only possible tradeoff is scope pressure: the newer framework encouraged a
richer Arc 01. In this trial that was contained and useful, but it should be
watched in Phase 2.

## Threats To Validity

- Single task and one run per condition: this is a case comparison, not a broad
  behavioral proof.
- The framework versions differ in both content and organization, so the
  independent variable is a bundle: current framework content plus current
  layout.
- Arc 02 planning has already started in both runs; this report intentionally
  uses only Arc 01 evidence except where project plans record Arc01-to-Arc02
  bubble-up.
- Workbench artifacts are ignored by the parent repository, so evidence is
  local artifact state plus reproduced commands rather than committed source
  history.
- Audit quality has not yet been tested directly.

## Recommended Phase 2

Continue both runs through enough Arc 02 work to produce comparable arithmetic
and diagnostic coverage. Then run the same audit prompt in both conditions,
using each framework's assigned audit route, and score:

- audit map quality,
- finding specificity,
- file/line evidence,
- severity calibration,
- missed defects or false positives,
- ability to distinguish Rust implementation issues from generated-C++ policy,
- quality of audit-to-hardening handoff.

Phase 1 conclusion: main/pre-0.5.0 is ahead on early planning and execution
quality, with no demonstrated regression so far.
