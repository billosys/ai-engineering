# Read-Only Rust Self-Audit Prompt

Use this prompt after the assigned trial project reaches its audit-ready
stopping point. This is a controlled framework-comparison audit pass. The goal
is to evaluate how well the assigned framework helps you audit the Rust code
that was produced under that same framework.

Do not begin until the operator confirms that your project is stopped at the
audit-ready boundary.

## Run Setup

Fill in these variables before running the prompt. Use only one setup block.

### Setup Block: framework-0.4.1

```text
RUN_LABEL=framework-0.4.1
FRAMEWORK_ENTRYPOINT=/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/SKILL.md
TRIAL_ROOT=/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial
PROJECT_PLAN=/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial/project-plan.md
IMPLEMENTATION_ROOT=/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial
REPORT_PATH=/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial/rust-self-audit-report.md
```

### Setup Block: framework-main-pre-0.5.0

```text
RUN_LABEL=framework-main-pre-0.5.0
FRAMEWORK_ENTRYPOINT=/Users/oubiwann/lab/billosys/ai-engineering/knowledge/collaboration-framework/SKILL.md
TRIAL_ROOT=/Users/oubiwann/lab/billosys/ai-engineering/workbench/lykn-cpp-transpiler-trial
PROJECT_PLAN=/Users/oubiwann/lab/billosys/ai-engineering/workbench/lykn-cpp-transpiler-trial/project01-tiny-lykn-cpp-transpiler/project-plan.md
IMPLEMENTATION_ROOT=/Users/oubiwann/lab/billosys/ai-engineering/workbench/lykn-cpp-transpiler-trial/implementation/lykn-cpp-transpiler
REPORT_PATH=/Users/oubiwann/lab/billosys/ai-engineering/workbench/lykn-cpp-transpiler-trial/project01-tiny-lykn-cpp-transpiler/rust-self-audit-report.md
```

## Role And Task

You are CDC for this trial condition.

Perform a read-only Rust code audit of the trial implementation under
`IMPLEMENTATION_ROOT`. Use the audit method provided by the assigned framework
at `FRAMEWORK_ENTRYPOINT`. This is a self-audit in the sense that you are
auditing the project created under your own framework condition, but the audit
must be diagnosis-only and evidence-based.

Write the final report to `REPORT_PATH`.

## Contamination Boundaries

Use only:

- the assigned `FRAMEWORK_ENTRYPOINT`;
- framework files reachable from that entrypoint in the same framework tree;
- the project and arc/slice planning artifacts under `TRIAL_ROOT`;
- the implementation files under `IMPLEMENTATION_ROOT`;
- the installed Rust guidance at `/Users/oubiwann/.codex/skills/rust-guidelines/SKILL.md`
  and only the Rust guide files it routes you to for this audit;
- standard local tools needed for read-only inspection and validation.

Do not use:

- the other framework condition's files;
- the other trial workspace;
- previous comparison reports;
- installed `collaboration-framework` as a substitute for `FRAMEWORK_ENTRYPOINT`;
- memory or remembered conclusions from the other condition;
- this prompt as evidence that one framework version should perform better.

If you accidentally open a disallowed source, record exactly what happened in
the report under "Contamination And Deviations" and continue without using it as
authority.

## Read-Only Boundary

This audit must not change code or planning files.

Allowed:

- read files;
- list files;
- run read-only search and inspection commands;
- run validation commands that compile or test the project;
- write only the audit report at `REPORT_PATH`.

Not allowed:

- editing source, tests, examples, fixtures, planning files, manifests, or
  generated C++;
- formatting files;
- applying fixes;
- staging or committing;
- opening follow-up implementation slices;
- rewriting the project plan based on audit findings.

If a validation command creates ordinary build output such as `target/`, record
that as transient tool output. Do not treat it as an audit artifact.

## Audit Scope

Audit the Rust implementation under `IMPLEMENTATION_ROOT` as a complete tiny
crate, not as a context-window sample.

Include:

- Rust library API;
- parser and syntax handling;
- AST design;
- code generation;
- structured errors and diagnostics;
- CLI boundary;
- tests;
- valid and invalid fixtures;
- generated C++ examples only as outputs of Rust codegen policy.

Do not perform a separate C++ code audit. If generated C++ exposes a problem,
file the finding against the Rust code or test/documentation contract that
produces or permits that output.

## Required Procedure

1. Record the current date with a local command.
2. Read `FRAMEWORK_ENTRYPOINT` completely.
3. Load the framework's audit guidance reachable from `FRAMEWORK_ENTRYPOINT`.
4. Read `PROJECT_PLAN` and the closed Arc 03 planning/closing evidence.
5. Load Rust guidance needed for a Rust audit.
6. Build an audit map before writing findings.
7. Inspect every first-party Rust source file and every first-party Rust test
   file under `IMPLEMENTATION_ROOT`.
8. Inspect fixtures and generated examples enough to audit test coverage and
   codegen policy.
9. Run validation commands if available:
   - `cargo fmt --check`
   - `cargo check`
   - `cargo clippy -- -D warnings`
   - `cargo test`
   - compile and run generated C++ examples with C++17 if a compiler is
     available
10. Write the report to `REPORT_PATH`.

If a required file or command is missing, do not improvise a replacement without
recording the deviation. Continue with the strongest available evidence.

## Finding Rules

Every severity-graded finding must include:

- stable ID, starting at `RUST-001`;
- severity: Blocker, High, Medium, or Low;
- location with file path and line number;
- scale: line/function, file/module, logical unit, crate/target,
  executable/API, or whole codebase;
- what is wrong;
- why it matters;
- concrete fix direction.

Do not report generic advice. Do not file a finding without a concrete failure
mode. If a concern is plausible but not proven, place it under "Open Questions"
or "Audit Notes", not under Findings.

Include at least five negative findings: specific things you checked and did
not find.

## Required Report Structure

Write a Markdown report with this exact top-level structure:

```markdown
# Rust Self-Audit Report

## Metadata

## Sources And Tools Used

## Contamination And Deviations

## Executive Summary

## Audit Map

## Validation Results

## Findings

## Coherence Observations

## Negative Findings

## Open Questions

## Audit-To-Hardening Handoff

## Self-Scoring For Third-Party Assessment

## Final Verdict
```

### Metadata

Include:

- `RUN_LABEL`;
- `FRAMEWORK_ENTRYPOINT`;
- `TRIAL_ROOT`;
- `PROJECT_PLAN`;
- `IMPLEMENTATION_ROOT`;
- `REPORT_PATH`;
- date;
- whether Arc 03 was confirmed closed before the audit began.

### Sources And Tools Used

List every framework file, project file, domain guide, source file group, and
tool command used. Separate "read" from "executed".

### Contamination And Deviations

State either "None observed" or list deviations plainly. Do not hide accidental
cross-condition context.

### Executive Summary

In 3 to 5 sentences, summarize:

- whether the crate is audit-ready;
- the highest-severity issue found;
- the dominant issue cluster;
- what is notably solid.

### Audit Map

Map:

- crate targets;
- public API;
- CLI entrypoint;
- parser/AST/codegen/error modules;
- tests;
- fixtures;
- generated examples;
- excluded/generated/build-output paths.

### Validation Results

Record exact commands and outcomes. Include failures and skipped commands.

### Findings

List severity-graded findings highest severity first. If no findings exist,
write `No severity-graded findings found` and then still provide the negative
findings section.

### Coherence Observations

Record non-finding patterns that affect maintainability, clarity, or future
auditability. Promote any item with a concrete failure mode to Findings.

### Negative Findings

List at least five specific clean checks.

### Open Questions

List genuine unresolved questions that should not be presented as defects.

### Audit-To-Hardening Handoff

Provide a follow-up work packet:

- finding IDs to address;
- suggested order;
- tests to add or update;
- validation commands to rerun;
- items explicitly not worth changing yet.

Do not implement any of it.

### Self-Scoring For Third-Party Assessment

Score your own audit from 0 to 3 on each measure. Use this scale:

| Score | Meaning |
| --- | --- |
| 0 | Absent, contradicted, or unusable. |
| 1 | Present but vague, incomplete, or not actionable. |
| 2 | Actionable and mostly complete, with gaps or weak evidence. |
| 3 | Complete, specific, and supported by inspectable evidence. |

Use this table:

| Measure | Score | Evidence | Notes |
| --- | --- | --- | --- |
| Framework isolation |  |  |  |
| Audit-map completeness |  |  |  |
| Source coverage |  |  |  |
| Validation discipline |  |  |  |
| Finding specificity |  |  |  |
| Severity calibration |  |  |  |
| Rust-idiom grounding |  |  |  |
| Generated-C++ boundary handling |  |  |  |
| Negative evidence quality |  |  |  |
| Hardening handoff quality |  |  |  |
| Threat/limitation honesty |  |  |  |

This self-score is evidence for the third-party assessor, not the final
assessment.

### Final Verdict

State one of:

- `audit-complete`;
- `audit-complete-with-limitations`;
- `audit-incomplete`.

Explain the verdict in 2 to 4 sentences.

## Stop Condition

Stop after writing `REPORT_PATH` and reporting its path to the operator. Do not
open hardening work. Do not close or modify any project, arc, or slice as part
of the audit unless the operator separately asks for that.
