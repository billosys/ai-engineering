# Final Framework Regression Assessment

Date: 2026-09-05

## Question

Did the collaboration-framework changes between `framework-0.4.1` and the
main/pre-0.5.0 candidate introduce regressions in project planning, execution,
or Rust audit behavior? Is there circumstantial evidence of improvement?

## Verdict

Decision: `main-slightly-improved`.

No material regression is demonstrated. The main/pre-0.5.0 candidate produced
better planning normalization, cleaner implementation organization, better
fixture/test structure, stronger generated-C++ safety before audit, and a more
protocol-compliant self-audit report.

The result is not a clean sweep. The 0.4.1 self-audit caught one true CLI issue
that the main/pre-0.5.0 audit missed: `print!` panics on broken stdout pipes.
Main also violated the audit prompt's allowed-source boundary by reading C++
and Lykn guidance during a Rust-only audit. Those are real marks against the
newer condition, but they do not rise to an overall regression signal.

## Compared Conditions

| Condition | Framework entrypoint | Trial workspace |
| --- | --- | --- |
| `framework-0.4.1` | `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/SKILL.md` | `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial` |
| `framework-main-pre-0.5.0` | `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/collaboration-framework/SKILL.md` | `/Users/oubiwann/lab/billosys/ai-engineering/workbench/lykn-cpp-transpiler-trial` |

## Evidence Reviewed

0.4.1:

- `project-plan.md`
- `arc03-examples-and-audit-readiness/closing-report.md`
- `closing-report.md`
- `rust-self-audit-report.md`
- implementation under the 0.4.1 trial root

Main/pre-0.5.0:

- `project01-tiny-lykn-cpp-transpiler/project-plan.md`
- `project01-tiny-lykn-cpp-transpiler/arc03-cli-examples-and-audit-readiness/closing-report.md`
- `project01-tiny-lykn-cpp-transpiler/closing-report.md`
- `project01-tiny-lykn-cpp-transpiler/rust-self-audit-report.md`
- implementation under `implementation/lykn-cpp-transpiler`

Previously produced comparison artifacts were used only after scoring to
interpret trends:

- `arc01-framework-comparison.md`
- `phase2a-post-arc02-framework-comparison.md`
- `read-only-self-audit-assessment-rubric.md`

## Comparability Check

The comparison is strong enough for a regression assessment:

- both used the same trial prompt family and same tiny Lykn-to-C++ task;
- both reached a closed Arc 03 audit-ready boundary;
- both then produced a read-only Rust self-audit report;
- both closed the project after the audit without repairing findings;
- both worktrees were clean after close;
- both produced reports of nearly identical size: 246 lines for 0.4.1 and 250
  lines for main/pre-0.5.0.

Known confounds:

- the implementations are not identical, because the frameworks shaped their
  own planning and execution;
- each audit is a self-audit of its own implementation, not a cross-audit of
  the same codebase;
- both self-audits had contamination or prompt-compliance issues;
- this is one matched task, not a population-level measurement.

## Project Execution Result

The main/pre-0.5.0 implementation finished with a stronger pre-audit safety
surface.

0.4.1 produced a coherent crate with parser, AST, codegen, errors, CLI, tests,
fixtures, and generated examples. Its audit found 7 issues: 1 high, 5 medium,
and 1 low.

Main/pre-0.5.0 produced a similarly compact crate with a cleaner test/fixture
layout and several hazards already blocked before audit. Its audit found 6
issues: 2 high, 1 medium, and 3 low.

Important implementation deltas:

| Topic | 0.4.1 | Main/pre-0.5.0 | Interpretation |
| --- | --- | --- | --- |
| C++ keyword identifiers | Accepted `return` and emitted invalid C++. | Rejected `class` and `return` as C++-unsafe identifiers. | Main improves generated-C++ validity. |
| Direct literal division by zero | Accepted `(print (/ 1 0))` and emitted `1 / 0`. | Rejected `(print (/ 1 0))` with a codegen error. | Main improves arithmetic diagnostic boundary. |
| File-read diagnostics | Missing-file error omitted the path. | Missing-file error included the path. | Main improves CLI diagnostic usefulness. |
| CLI usage tests | Audit reported usage/file-read gaps. | Usage diagnostics were covered; missing-file test still absent. | Main partially improves CLI coverage. |
| Fixture/test organization | Fixtures added under `tests/fixtures`; many behavior tests remain in `src/lib.rs`. | Separate `fixtures/`, `examples/generated/`, `tests/cli.rs`, `tests/diagnostic_matrix.rs`, and `tests/transpile.rs`. | Main improves auditability and selective review. |
| Broken pipe | Present and detected by 0.4.1 audit. | Present but missed by main audit. | Main audit regression on this specific issue. |

## Finding Reconciliation

| Finding Topic | 0.4.1 | Main/pre-0.5.0 | Confirmed? | Notes |
| --- | --- | --- | --- | --- |
| C++ keyword identifiers | Found: `return` accepted and emitted. | Negative finding says keywords are rejected. | Yes. | Main implementation fixed this class for keywords. |
| Direct literal division by zero | Found: literal `1 / 0` accepted. | Direct literal zero rejected; audit finds non-literal zero gap. | Yes. | Main narrowed the bug. |
| Signed integer overflow | Found as Medium. | Found as High. | Yes. | Both reports catch the hazard; severity differs. |
| Broken stdout pipe | Found as Medium. | Missed. | Yes. | Both implementations use `print!`, so this is a main audit miss. |
| Missing file path in diagnostic | Found. | Not applicable; main includes path. | Yes. | Main improved implementation. |
| Missing CLI read-error test | Found broader CLI coverage gap. | Found missing read-error test only. | Yes. | Main improved usage coverage but still lacks read-failure coverage. |
| Public error enum evolution | Found for `CliError`. | Found for public error enums. | Yes. | Both identify API evolution pressure. |
| C++ double underscore anywhere | Not specifically found. | Found `foo__bar`. | Yes. | Main catches a subtler C++ identifier-policy gap. |
| Dash-prefixed diagnostic classification | Not found. | Found `-foo` as invalid integer. | Yes. | Low-grade but precise diagnostic issue. |

## Audit Report Quality Scores

Scale: 0 to 3.

| Measure | 0.4.1 | Main/pre-0.5.0 | Notes |
| --- | --- | --- | --- |
| Framework isolation | 2 | 2 | 0.4.1 checked memory despite the no-memory boundary. Main read C++ and Lykn guidance despite the Rust-only allowed-source boundary. |
| Audit-map completeness | 3 | 3 | Both mapped the crate, modules, CLI, tests, fixtures, generated examples, and exclusions. |
| Source coverage | 3 | 3 | Both inspected all first-party Rust source and tests. |
| Validation discipline | 3 | 3 | Both ran Rust gates and C++17 generated-example checks. |
| Finding specificity | 3 | 3 | Both reports include file/line evidence and concrete fix direction. |
| Severity calibration | 2 | 2 | Both arithmetic findings depend partly on final language-semantics decisions. |
| Rust-idiom grounding | 2 | 2 | Both connect findings to Rust API/error/CLI practice; main missed broken-pipe despite relevant CLI guidance. |
| Generated-C++ boundary handling | 3 | 3 | Both correctly root generated-C++ issues in Rust parser/codegen policy. |
| Negative evidence quality | 1 | 3 | 0.4.1 misused "Negative Findings" to summarize defects instead of clean checks. Main listed eight concrete clean checks. |
| Coherence/architecture insight | 2 | 3 | Main gives more useful maintainability observations; 0.4.1 is solid but flatter. |
| Hardening handoff quality | 3 | 3 | Both provide actionable no-repair handoffs. |
| Limitation honesty | 2 | 2 | 0.4.1 missed required final-verdict/self-score format; main failed to flag its disallowed C++/Lykn source reads as contamination. |

Indicative totals:

- `framework-0.4.1`: 29/36
- `framework-main-pre-0.5.0`: 32/36

The score difference is meaningful but not huge. It supports improvement, not
dominance.

## Prompt Compliance Notes

0.4.1 report strengths:

- stayed read-only;
- used assigned 0.4.1 framework root;
- produced line-grounded findings;
- caught a true broken-pipe CLI issue;
- produced a good hardening handoff.

0.4.1 report weaknesses:

- checked memory despite a no-memory contamination boundary;
- did not use the required 0-3 self-scoring table;
- did not use one of the required final verdict labels;
- used "Negative Findings" to summarize actual findings rather than at least
  five concrete clean checks.

Main/pre-0.5.0 report strengths:

- followed the required report structure closely;
- used the required 0-3 self-scoring table;
- gave concrete negative findings;
- found subtler residual issues after earlier implementation hardening;
- produced a better audit-to-hardening packet.

Main/pre-0.5.0 report weaknesses:

- read C++ and Lykn guidance even though the prompt allowed only Rust domain
  guidance for this self-audit;
- did not disclose those reads as contamination;
- missed the shared broken-pipe issue in `src/main.rs`.

## Regression Classes

| Regression Class | Result |
| --- | --- |
| Correctness regression | No. Main fixes or narrows several 0.4.1 correctness hazards. |
| Coverage or validation regression | No. Main has stronger fixture/test organization and equivalent validation gates. |
| Scope-control regression | No material regression. Main front-loaded more work earlier, but narrowed later arcs and stopped at the requested boundary. |
| Usability or wayfinding regression | No. Main is clearer, more normalized, and easier to audit. |
| Evidence-quality regression | No overall regression. Main's negative evidence is much better; both had contamination notes to preserve. |
| Audit-quality regression | Mixed local result, no overall regression. Main missed broken pipe, but produced the more compliant and more complete audit report. |
| Safety/compliance regression | Possible minor concern. Main's disallowed C++/Lykn source reads should be treated as a framework-isolation warning. |

## Interpretation

The strongest evidence for improvement is not that main found more bugs. It did
not. The stronger evidence is that main produced a better-shaped project and a
more assessable audit artifact:

- routes and planning were easier to inspect;
- implementation and planning were more cleanly separated;
- fixtures and tests were laid out for audit;
- several hazards were already prevented by implementation before audit;
- the audit report followed the requested structure and produced real negative
  evidence.

The strongest evidence against overclaiming improvement is the broken-pipe
miss. The older audit caught a true issue at the CLI boundary that the newer
audit did not. That means the newer framework did not simply dominate the old
one on all audit behavior.

The fairest conclusion is that the post-0.4.x framework improves the overall
collaboration system, while still needing a guardrail around prompt-source
isolation and perhaps stronger CLI-specific audit prompting.

## Threats To Validity

- One matched task cannot prove general behavior.
- The self-audits reviewed different implementations.
- Both audit sessions had contamination or prompt-compliance issues.
- The third-party assessor created the self-audit prompt and rubric, so this is
  third-party relative to the two CDC runs but not fully independent of the
  experimental design.
- The main/pre-0.5.0 project-close report recorded an accidental installed
  framework open during project close, although the self-audit report itself
  did not report cross-framework use.

## Recommended Framework Follow-Up

1. Strengthen self-audit prompt wording so "allowed references" is a hard
   checklist and disallowed reads must be reported even if they seem harmless.
2. Add a specific audit-report compliance checklist: exact verdict label,
   exact self-score table, and negative findings as clean checks.
3. Add explicit CLI audit probes for pipe behavior, read failures, stdout/stderr
   separation, and exit codes.
4. Preserve the no-repair rule for future trials; the unfixed findings were the
   most useful evidence in this run.

## Final Conclusion

No regression requiring rollback or rethink is demonstrated by this trial.

There is circumstantial evidence that the main/pre-0.5.0 framework improves the
quality of planning, execution, evidence shape, and audit-report usability. The
result should be recorded as `main-slightly-improved`, with one concrete audit
miss and one source-isolation warning retained for follow-up.
