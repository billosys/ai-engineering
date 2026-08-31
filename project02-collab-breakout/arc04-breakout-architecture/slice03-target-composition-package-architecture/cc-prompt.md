# CC Prompt: Project02 Arc04 Slice03 Target Composition And Package Architecture

You are working in the planning worktree:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`

Source checkout for read-only grounding:

`/Users/oubiwann/lab/billosys/ai-engineering`

## Assignment

Complete Project02 Arc04 Slice03:

`project02-collab-breakout/arc04-breakout-architecture/slice03-target-composition-package-architecture`

This is a planning/analysis slice. Do not edit source files in the main
checkout. Do not create source `SKILL.md`, README, Makefile, package, or zip
changes. Do not edit planning artifacts outside Project02.

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
- `project02-collab-breakout/arc04-breakout-architecture/slice03-target-composition-package-architecture/slice-plan.md`
- `project02-collab-breakout/arc04-breakout-architecture/slice03-target-composition-package-architecture/ledger.md`

Read closed Arc02 and Arc03 outputs as needed for evidence grounding. Do not
reopen conceptual or functional analysis unless you find a concrete input
gap; if you do, record it as an Arc04 risk rather than silently replanning.

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
Actual Slice03 architecture proposals must come from verified Project02
evidence, Slice01's decision method, and Slice02's evaluated contract inputs.

## Deliverables

Create these durable artifacts under:

`project02-collab-breakout/arc04-breakout-architecture/slice03-target-composition-package-architecture/artifacts/`

- `target-component-architecture.md`
- `dependency-and-composition-order.md`
- `package-and-release-architecture.md`
- `wayfinding-adapter-and-support-plan.md`
- `slice04-operator-acceptance-inputs.md`

Then update:

- `project02-collab-breakout/arc04-breakout-architecture/slice03-target-composition-package-architecture/ledger.md`
- `project02-collab-breakout/arc04-breakout-architecture/slice03-target-composition-package-architecture/slice-plan.md`

At close, also write:

- `project02-collab-breakout/arc04-breakout-architecture/slice03-target-composition-package-architecture/closing-report.md`

Do not write `cdc-verification.md`; CDC writes that after independent
verification.

## Required Artifact Content

`target-component-architecture.md` must propose the target component graph and
place every `CAW-01` through `CAW-26` row as a component, component family,
support asset, adapter, constraint, package/release gate, dependency edge,
non-component, or deferred question. It must preserve go / adjust / defer
posture and explain any adjusted placement.

`dependency-and-composition-order.md` must define load order and composition
paths for:

- standalone component use;
- composed `collaboration-framework` use;
- PM lifecycle and ledgered verification use;
- audit and coverage sibling use;
- delegation and contribution direct-load use;
- source clone, generated zip, installed skill, and CCDP-adjacent reader
  modes.

`package-and-release-architecture.md` must compose Project01 source/package
and release gates before package paths. Include package roots, source path
assumptions, package-local link behavior, README/`SKILL.md`/Makefile surface
changes, CCDP separation, generated zip behavior, validation commands, and
non-final package-path language.

`wayfinding-adapter-and-support-plan.md` must define:

- top-level `collaboration-framework` composer behavior, thin but not
  link-only;
- compact safety floor and route table expectations;
- PM wayfinder treatment;
- agent-adapter placement, preferably central plus local notes unless the
  evidence supports another shape;
- repository-orientation/source-package reader adapter placement;
- support-asset travel for templates, PM examples, anti-pattern guidance,
  audit examples, and protocol-distribution guidance;
- owners, citation edges, and re-entry conditions for non-component and
  deferred rows.

`slice04-operator-acceptance-inputs.md` must prepare Slice04's acceptance
packet. Include proposed decisions, open risks, rejected alternatives,
deferred questions, re-entry conditions, D/OQ/ARG source IDs, and Arc05
implementation-plan fields. It must clearly state that operator acceptance is
still pending and that source files remain untouched.

## Verification

Run every Verify command in `ledger.md` from the slice directory. Also run:

```sh
git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning diff --check -- project02-collab-breakout/arc04-breakout-architecture/slice03-target-composition-package-architecture
```

If you stage files, stage only the Project02 Arc04 Slice03 subtree unless the
slice plan explicitly requires a Project02 parent update.

## Close Report

The close report must include:

- verdict;
- artifact inventory;
- verification summary;
- row-by-row ledger walk for F-1 through F-9;
- silent-drop diff against the slice plan;
- bubble-up to Arc04, including whether Slice04 can open or whether the
  Arc04 plan needs adjustment first;
- what worked;
- closure metadata.

Keep outputs as proposed architecture inputs. Final operator acceptance
belongs to Slice04, and Arc05 implementation planning comes later.
