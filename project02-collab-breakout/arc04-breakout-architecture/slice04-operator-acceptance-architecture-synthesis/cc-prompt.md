# CC Prompt: Project02 Arc04 Slice04 Operator Acceptance And Architecture Synthesis

You are working in the planning worktree:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`

Source checkout for read-only grounding:

`/Users/oubiwann/lab/billosys/ai-engineering`

## Assignment

Complete Project02 Arc04 Slice04:

`project02-collab-breakout/arc04-breakout-architecture/slice04-operator-acceptance-architecture-synthesis`

This is a planning/analysis slice. Do not edit source files in the main
checkout. Do not create source `SKILL.md`, README, Makefile, package, or zip
changes. Do not edit planning artifacts outside Project02.

This slice owns the operator acceptance checkpoint, but you must not
manufacture acceptance. If explicit operator acceptance or change requests are
not available in your executing context, prepare the acceptance packet and
record acceptance as pending with concrete re-entry conditions.

## Required Reading

Read these Project02 files before writing artifacts:

- `project02-collab-breakout/project-plan.md`
- `project02-collab-breakout/ledger.md`
- `project02-collab-breakout/arc04-breakout-architecture/arc-plan.md`
- `project02-collab-breakout/arc04-breakout-architecture/ledger.md`
- `project02-collab-breakout/arc04-breakout-architecture/slice01-architecture-decision-instrument/cdc-verification.md`
- `project02-collab-breakout/arc04-breakout-architecture/slice01-architecture-decision-instrument/artifacts/architecture-decision-method.md`
- `project02-collab-breakout/arc04-breakout-architecture/slice01-architecture-decision-instrument/artifacts/component-contract-schema.md`
- `project02-collab-breakout/arc04-breakout-architecture/slice01-architecture-decision-instrument/artifacts/operator-decision-and-risk-register.md`
- `project02-collab-breakout/arc04-breakout-architecture/slice02-component-contract-evaluation/cdc-verification.md`
- `project02-collab-breakout/arc04-breakout-architecture/slice02-component-contract-evaluation/artifacts/component-contract-evaluation-matrix.md`
- `project02-collab-breakout/arc04-breakout-architecture/slice02-component-contract-evaluation/artifacts/candidate-component-contracts.md`
- `project02-collab-breakout/arc04-breakout-architecture/slice02-component-contract-evaluation/artifacts/support-adapter-constraint-dispositions.md`
- `project02-collab-breakout/arc04-breakout-architecture/slice02-component-contract-evaluation/artifacts/package-release-gate-dispositions.md`
- `project02-collab-breakout/arc04-breakout-architecture/slice02-component-contract-evaluation/artifacts/slice03-composition-inputs.md`
- `project02-collab-breakout/arc04-breakout-architecture/slice03-target-composition-package-architecture/cdc-verification.md`
- `project02-collab-breakout/arc04-breakout-architecture/slice03-target-composition-package-architecture/artifacts/target-component-architecture.md`
- `project02-collab-breakout/arc04-breakout-architecture/slice03-target-composition-package-architecture/artifacts/dependency-and-composition-order.md`
- `project02-collab-breakout/arc04-breakout-architecture/slice03-target-composition-package-architecture/artifacts/package-and-release-architecture.md`
- `project02-collab-breakout/arc04-breakout-architecture/slice03-target-composition-package-architecture/artifacts/wayfinding-adapter-and-support-plan.md`
- `project02-collab-breakout/arc04-breakout-architecture/slice03-target-composition-package-architecture/artifacts/slice04-operator-acceptance-inputs.md`
- `project02-collab-breakout/arc04-breakout-architecture/slice04-operator-acceptance-architecture-synthesis/slice-plan.md`
- `project02-collab-breakout/arc04-breakout-architecture/slice04-operator-acceptance-architecture-synthesis/ledger.md`

Read closed Arc02 and Arc03 outputs only as needed to resolve a concrete
evidence question. Do not reopen conceptual or functional analysis unless
you find a concrete input gap; if you do, record it as an Arc04 risk rather
than silently replanning.

You may inspect the current source checkout for factual grounding. Keep source
files read-only.

Suggested source grounding includes:

- `README.md`
- `SKILL.md`
- `docs/AI-CONSTITUTION-SUPPLEMENT.md`
- `docs/AI-ENGINEERING-METHODOLOGY.md`
- `docs/PROJECT-MANAGEMENT.md`
- `docs/pm/*.md`
- `templates/LEDGER-DISCIPLINE.md`
- `docs/CODE-AUDIT.md`
- `docs/CLAUDE-CODE-COVERAGE.md`
- `docs/SUBAGENT-DELEGATION-POLICY.md`
- `docs/CONTRIBUTION-STYLE.md`
- `templates/CONTRIBUTION-TICKET.md`
- `Makefile`
- `package-path-exceptions.tsv`

Treat any prior soft layout sketch as low-weight hypothesis evidence only.
Actual Slice04 acceptance recommendations must come from verified Project02
evidence and explicit operator acceptance if it is available.

## Deliverables

Create these durable artifacts under:

`project02-collab-breakout/arc04-breakout-architecture/slice04-operator-acceptance-architecture-synthesis/artifacts/`

- `operator-acceptance-packet.md`
- `architecture-synthesis.md`
- `decision-risk-disposition-record.md`
- `package-release-acceptance-record.md`
- `arc05-implementation-inputs.md`
- `arc04-close-readiness.md`

Then update:

- `project02-collab-breakout/arc04-breakout-architecture/slice04-operator-acceptance-architecture-synthesis/ledger.md`
- `project02-collab-breakout/arc04-breakout-architecture/slice04-operator-acceptance-architecture-synthesis/slice-plan.md`

At close, also write:

- `project02-collab-breakout/arc04-breakout-architecture/slice04-operator-acceptance-architecture-synthesis/closing-report.md`

Do not write `cdc-verification.md`; CDC writes that after independent
verification.

## Required Artifact Content

`operator-acceptance-packet.md` must be concise enough for the operator to
review. Include the proposed architecture, exact acceptance questions,
recommended defaults, meaningful alternatives, risks, and the consequences of
accepting or changing each decision.

`architecture-synthesis.md` must state the architecture status precisely:
accepted only if explicit operator evidence exists, otherwise proposed and
pending acceptance. It must include component names, contracts, dependencies,
package/source assumptions, support assets, adapters, deferred decisions, and
Arc05 implementation implications.

`decision-risk-disposition-record.md` must disposition D-01 through D-12,
OQ-01 through OQ-09, and ARG-01 through ARG-12. Preserve source IDs and mark
each row accepted, changed, rejected, deferred, or pending.

`package-release-acceptance-record.md` must record source/package,
package-local link, zip root, README, `SKILL.md`, Makefile, generated zip,
CCDP separation, validation, and release-surface decisions. It must preserve
Project01 gates and mark package paths accepted only if explicit operator
evidence exists.

`arc05-implementation-inputs.md` must prepare Arc05 without starting it:
source edits, README updates, `SKILL.md` entrypoints, packaging changes,
Makefile/package-list changes, validation gates, migration notes, and review
concerns.

`arc04-close-readiness.md` must state whether Arc04 is ready for formal close
after CDC verification. If operator acceptance is pending or changes are
requested, state that Arc04 is not ready, name the blocker, and provide the
re-entry condition.

## Verification

Run every Verify command in `ledger.md` from the slice directory. Also run:

```sh
git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning diff --check -- project02-collab-breakout/arc04-breakout-architecture/slice04-operator-acceptance-architecture-synthesis
```

If you stage files, stage only the Project02 Arc04 Slice04 subtree unless the
slice plan explicitly requires a Project02 parent update.

## Close Report

The close report must include:

- verdict;
- artifact inventory;
- verification summary;
- row-by-row ledger walk for F-1 through F-9;
- silent-drop diff against the slice plan;
- bubble-up to Arc04, including whether Arc04 can proceed to formal arc close
  or whether operator acceptance/remediation is still required;
- what worked;
- closure metadata.

Keep acceptance evidence explicit. Final Arc04 close belongs to the arc close
step after CDC verification and any required operator acceptance.
