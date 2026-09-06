# Phase 2A Framework Comparison: Post-Arc02 Checkpoint

Date: 2026-09-05

## Question

After `framework-0.4.1` has fully closed Arc 02, do the two trial runs show
evidence of regression or improvement in project planning, software execution,
and preparation for the later code-audit phase?

## Short Answer

No regression is evident at this checkpoint.

By the end of Arc 02, both runs have produced a working tiny Lykn-inspired
Rust-to-C++ transpiler surface with recursive arithmetic expressions, structured
diagnostics, Rust validation gates, and independently verified closure evidence.
The newer framework remains ahead on planning normalization, route clarity,
fixture/test organization, validation depth, and audit-readiness surface.

The older 0.4.1 framework caught up on language capability by Arc 02, and it
continued to show a real strength: cautious, comprehensible slice boundaries.
Its main weakness remains operational friction and weaker early artifact
organization.

## Conditions Compared

| Condition | Framework entrypoint | Trial workspace |
| --- | --- | --- |
| `framework-0.4.1` | `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/SKILL.md` | `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial` |
| `framework-main-pre-0.5.0` | `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/collaboration-framework/SKILL.md` | `/Users/oubiwann/lab/billosys/ai-engineering/workbench/lykn-cpp-transpiler-trial` |

## Evidence Boundary

Primary comparison:

- 0.4.1 through formal Arc 02 close.
- main/pre-0.5.0 through formal Arc 02 close.

Secondary timeline note:

- main/pre-0.5.0 has already CDC-closed Arc 03 Slice 01, so current live code in
  its trial workspace includes later CLI/example work. Current-command results
  from main are useful as health checks, but they are not pure Arc 02 evidence.

## Evidence Reviewed

### 0.4.1

- `project-plan.md`
- `arc02-expressions-and-semantics/arc-plan.md`
- `arc02-expressions-and-semantics/closing-report.md`
- `arc02-expressions-and-semantics/slice01-recursive-arithmetic-core/{slice-plan.md,ledger.md,closing-report.md,cdc-verification.md}`
- `arc02-expressions-and-semantics/slice02-semantic-diagnostic-closure/{slice-plan.md,ledger.md,closing-report.md,cdc-verification.md}`
- Rust crate under the trial workspace root

### Main Pre-0.5.0

- `project01-tiny-lykn-cpp-transpiler/project-plan.md`
- `project01-tiny-lykn-cpp-transpiler/arc02-diagnostics-and-negative-coverage/arc-plan.md`
- `project01-tiny-lykn-cpp-transpiler/arc02-diagnostics-and-negative-coverage/closing-report.md`
- `project01-tiny-lykn-cpp-transpiler/arc02-diagnostics-and-negative-coverage/slice01-diagnostic-coverage-matrix/{slice-plan.md,ledger.md,closing-report.md,cdc-verification.md}`
- `project01-tiny-lykn-cpp-transpiler/arc03-cli-examples-and-audit-readiness/arc-plan.md`
- `project01-tiny-lykn-cpp-transpiler/arc03-cli-examples-and-audit-readiness/slice01-cli-and-example-surface/cdc-verification.md`
- Rust crate under `implementation/lykn-cpp-transpiler`

## Reproduced Checks

### 0.4.1 Current Closed Arc02 State

- `cargo fmt --check`: pass
- `cargo test`: pass, 21 library tests and 7 CLI integration tests
- `cargo clippy -- -D warnings`: pass
- C++17 compile of `examples/arithmetic.cpp`: pass
- Compiled `examples/arithmetic.cpp` output: `35` and `124`
- Rust source and test surface: 1198 lines across `src/` and `tests/`
- Source organization: examples exist; no `fixtures/` directory exists yet

### Main Current State

This is a post-Arc03-Slice01 health check, not pure Arc02 evidence.

- `cargo fmt --check`: pass
- `cargo test`: pass, 19 integration tests across `cli`, `diagnostic_matrix`,
  and `transpile`
- `cargo clippy -- -D warnings`: pass
- C++17 compile of `examples/generated/happy_path.cpp`: pass
- Compiled `happy_path.cpp` output: `9`
- C++17 compile of `examples/generated/arithmetic_mix.cpp`: pass
- Compiled `arithmetic_mix.cpp` output: `3`
- Rust source and test surface: 1167 lines across `src/` and `tests/`
- Source organization: valid fixtures, invalid fixtures, generated examples,
  CLI tests, diagnostic-matrix tests, and transpile integration tests are
  separated

## Capability Comparison

By Arc 02 close, the two runs are comparable in core language capability:

- both accept integer literals, identifiers, `let`, `print`, and binary prefix
  arithmetic for `+`, `-`, `*`, and `/`;
- both reject malformed expressions and unsupported operators with structured
  diagnostics;
- both preserve deterministic parenthesized C++ infix output;
- both pass Rust format, test, and lint gates;
- both have CDC verification artifacts separating CC claims from reproduced
  evidence.

The difference is how they got there.

The 0.4.1 run used Arc 02 to perform the semantic expansion originally expected
there: recursive arithmetic core in Slice 01, then semantic and diagnostic
closure in Slice 02. This is orderly and easy to reason about.

The main/pre-0.5.0 run front-loaded more implementation into Arc 01, then
adapted Arc 02 into a focused negative-coverage matrix instead of repeating
already-delivered work. This is stronger planning adaptation. It avoided a
redundant second Arc 02 slice and moved earlier into audit-readiness work.

## Rubric

Scale: 0-3. Scores are directional, not statistically meaningful.

| Measure | 0.4.1 | Main pre-0.5.0 | Interpretation |
| --- | --- | --- | --- |
| Framework isolation and setup | 2 | 3 | Main has cleaner assigned-framework routing. 0.4.1 records an early contamination caveat from opening installed framework/memory before the control constraint was read. |
| Planning structure and wayfinding | 2 | 3 | Main uses normalized project/arc/slice layout and clearer planning/implementation separation. 0.4.1 is coherent but flatter. |
| Planning adaptation | 2 | 3 | Main explicitly narrowed Arc 02 after Arc 01 absorbed diagnostic work. 0.4.1 refined the roadmap too, but later and with more process friction. |
| Scope control | 3 | 3 | Both stayed within the tiny-transpiler task by Arc 02. Main's earlier front-loading remains watchable, but its Arc 02 narrowing was a strong containment move. |
| Slice economy | 2 | 3 | 0.4.1 needed two Arc 02 slices; main needed one because it avoided rework and used a matrix slice to close the remaining boundary. |
| Evidence and CDC closure discipline | 3 | 3 | Both now have independently verified slice and arc closure evidence. |
| Validation depth | 2 | 3 | Both pass Rust gates. Main had C++17 compile/run evidence in Arc 02 closure; 0.4.1's Arc 02 C++ example compiles now, but that was not part of its formal Arc 02 gate. |
| Implementation/test organization | 2 | 3 | Main has fixtures and split integration tests. 0.4.1 still concentrates most behavior tests in `src/lib.rs` and defers fixture organization. |
| Audit readiness | 2 | 3 | Main is more audit-ready earlier because its artifacts are already organized around valid fixtures, invalid fixtures, generated examples, CLI behavior, and diagnostic matrix coverage. |

Indicative totals:

- `framework-0.4.1`: 20/27
- `framework-main-pre-0.5.0`: 27/27

The score gap is mostly organization, adaptation, and validation evidence. It
is not a claim that the 0.4.1 implementation is bad; the closed Arc 02 code is
green and capable.

## Findings

### 1. The newer framework improves audit-readiness without requiring more code

Main's current code is slightly smaller by Rust line count but has a better
audit surface:

- implementation modules remain separated;
- tests are organized as CLI, diagnostic matrix, and transpile integration
  suites;
- valid and invalid examples are durable fixtures;
- generated C++ examples are under a dedicated generated-example path;
- C++17 compile/run checks are explicit.

This is the strongest non-regression signal so far: the framework reorg appears
to improve selective access and evidentiary shape without inflating the code.

### 2. 0.4.1 remains better at feeling conservative

The 0.4.1 run's Arc 02 decomposition is admirably straightforward. It builds
the expression core, then verifies semantic and diagnostic closure. That makes
the work easy to narrate and review.

The cost is that some supporting surfaces arrive later. Fixture layout, C++17
compiler evidence, and audit-readiness mapping are all postponed to Arc 03. For
this trial, that is not wrong, but it delays the audit-quality experiment.

### 3. Main's front-loading is no longer just a concern; it became useful

The Arc 01 comparison flagged main's richer first arc as possible scope
pressure. Arc 02 changes the interpretation: because main used the earlier
capability to narrow Arc 02, the extra early work did not spiral. It reduced
later process load.

This should remain a monitored risk in larger projects, but in this run it was
a net positive.

### 4. Closure discipline is strong in both conditions now

Both runs separate CC proposed-done reports from CDC verification. Both include
row walks, command reproduction, deferral/no-op notes, and bubble-up
disposition.

The newer framework's advantage is less about "does it verify?" and more about
"how easy is it to find exactly the route and evidence needed?"

### 5. The next decisive evidence is the audit pass

Planning/execution evidence now favors main/pre-0.5.0, but the original
experiment also asks whether the framework improves code-audit performance.
That is not fully measured yet.

The next fair comparison should wait until both projects reach their
audit-ready close point. Main already has Arc 03 Slice 01 closed and needs Arc
03 Slice 02. 0.4.1 still needs its Arc 03 examples/audit-readiness work.

## Regression Assessment

At this checkpoint:

- no regression is demonstrated in main/pre-0.5.0;
- planning clarity appears improved;
- closure and validation evidence are at least as strong;
- implementation organization is stronger;
- audit-readiness arrives earlier;
- the main remaining risk is that stronger framework guidance may encourage
  early capability bundling unless the CDC keeps explicitly narrowing later
  arcs when work has already landed.

## Threats To Validity

- Single run per condition. This is useful engineering evidence, not broad
  behavioral proof.
- The independent variable bundles content and layout changes together.
- The current main workspace has progressed past Arc 02, so live health checks
  are not pure Arc 02 evidence.
- Workbench files are ignored by the parent repository; evidence is local
  artifact state plus reproduced commands, not committed project history.
- Operator interactions differed as the run progressed, especially because main
  moved into Arc 03 while 0.4.1 was still closing Arc 02.
- The audit-quality phase has not yet been run under matched conditions.

## Recommended Next Phase

Continue until both trial projects are audit-ready, then run one matched audit
prompt per condition.

For fairness:

- compare audit outputs after each run's project close, not by identical arc
  number;
- freeze or copy the relevant workbench state before running the audit prompts;
- use each condition's assigned framework audit route only;
- ask each CDC to produce an audit map, findings with file/line evidence,
  severity calibration, false-positive/missed-defect notes, and a hardening
  handoff;
- score the audits separately from implementation execution.

Phase 2A conclusion: main/pre-0.5.0 continues to outperform 0.4.1 on framework
effectiveness, with no regression evident so far. The strongest observed
improvement is not raw coding ability; it is better organization of decisions,
evidence, fixtures, validation, and routes for later audit work.
