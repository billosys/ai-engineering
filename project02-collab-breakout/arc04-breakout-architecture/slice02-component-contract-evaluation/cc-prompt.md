# CC Prompt: Project02 Arc04 Slice02 Component Contract Evaluation

You are working in the planning worktree:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`

Source checkout for read-only grounding:

`/Users/oubiwann/lab/billosys/ai-engineering`

## Assignment

Complete Project02 Arc04 Slice02:

`project02-collab-breakout/arc04-breakout-architecture/slice02-component-contract-evaluation`

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
- `project02-collab-breakout/arc04-breakout-architecture/slice01-architecture-decision-instrument/artifacts/architecture-input-register.md`
- `project02-collab-breakout/arc04-breakout-architecture/slice01-architecture-decision-instrument/artifacts/architecture-decision-method.md`
- `project02-collab-breakout/arc04-breakout-architecture/slice01-architecture-decision-instrument/artifacts/component-contract-schema.md`
- `project02-collab-breakout/arc04-breakout-architecture/slice01-architecture-decision-instrument/artifacts/candidate-architecture-worklist.md`
- `project02-collab-breakout/arc04-breakout-architecture/slice01-architecture-decision-instrument/artifacts/operator-decision-and-risk-register.md`
- `project02-collab-breakout/arc04-breakout-architecture/slice02-component-contract-evaluation/slice-plan.md`
- `project02-collab-breakout/arc04-breakout-architecture/slice02-component-contract-evaluation/ledger.md`

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
- package/path validation docs or exceptions where relevant

Treat any prior soft layout sketch as low-weight hypothesis evidence only.
Actual Slice02 dispositions must come from closed Project02 evidence and the
Slice01 decision instrument.

## Deliverables

Create these durable artifacts under:

`project02-collab-breakout/arc04-breakout-architecture/slice02-component-contract-evaluation/artifacts/`

- `component-contract-evaluation-matrix.md`
- `candidate-component-contracts.md`
- `support-adapter-constraint-dispositions.md`
- `package-release-gate-dispositions.md`
- `slice03-composition-inputs.md`

Then update:

- `project02-collab-breakout/arc04-breakout-architecture/slice02-component-contract-evaluation/ledger.md`
- `project02-collab-breakout/arc04-breakout-architecture/slice02-component-contract-evaluation/slice-plan.md`

At close, also write:

- `project02-collab-breakout/arc04-breakout-architecture/slice02-component-contract-evaluation/closing-report.md`

Do not write `cdc-verification.md`; CDC writes that after independent
verification.

## Required Artifact Content

`component-contract-evaluation-matrix.md` must account for every `CAW-01`
through `CAW-26` row from the Slice01 candidate architecture worklist. For
each row, include classification, evidence basis, contract status, risk
disposition, D/OQ/ARG links where relevant, Project01 gate relevance, and
go / adjust / defer posture.

`candidate-component-contracts.md` must evaluate the main candidate components
and component families against the Slice01 component-contract schema:

- `CAW-01` collaborative posture and ethics;
- `CAW-02` engineering methodology and process;
- `CAW-03` ledger verification protocol;
- `CAW-04` project management family;
- `CAW-05` code audit discipline;
- `CAW-06` coverage hardening discipline;
- `CAW-07` delegation policy;
- `CAW-08` contribution style and voice;
- composer and adapter candidates where a partial component contract is useful
  for Slice03 composition.

`support-adapter-constraint-dispositions.md` must disposition support assets,
adapters, constraints, dependency edges, package/release gates,
non-components, and deferred concepts, including `CAW-09` through `CAW-26`.

`package-release-gate-dispositions.md` must make Project01 source/package
constraints concrete at the contract-evaluation layer: source/package modes,
package-local links, zip roots, release surfaces, README and `SKILL.md`
wayfinding, Makefile/package lists, CCDP separation, validation commands, and
`make check-package-paths`.

`slice03-composition-inputs.md` must summarize which evaluated rows are ready
for composition, which require adjustment, which remain deferred, and which
are support assets, adapters, constraints, gates, dependency edges,
non-components, or operator decisions. It must explicitly state that Slice03
owns target graph composition and that Slice02 does not accept final
architecture.

## Verification

Run every Verify command in `ledger.md` from the slice directory. Also run:

```sh
git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning diff --check -- project02-collab-breakout/arc04-breakout-architecture/slice02-component-contract-evaluation
```

If you stage files, stage only the Project02 Arc04 Slice02 subtree unless the
slice plan explicitly requires a Project02 parent update.

## Close Report

The close report must include:

- verdict;
- artifact inventory;
- verification summary;
- row-by-row ledger walk for F-1 through F-9;
- silent-drop diff against the slice plan;
- bubble-up to Arc04, including whether Slice03 can open or whether the Arc04
  plan needs adjustment first;
- what worked;
- closure metadata.

Keep outputs as evaluated contract candidates and dispositions. Final target
composition belongs to Slice03, and operator-accepted architecture belongs to
Slice04.
