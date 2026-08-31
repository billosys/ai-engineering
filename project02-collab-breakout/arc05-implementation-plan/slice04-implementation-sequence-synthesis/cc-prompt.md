# CC Prompt: Arc05 Slice04 Implementation Sequence Synthesis

You are CC working in the planning worktree for Project02. Follow this prompt
exactly, keep the work planning-only, and commit only the explicit Slice04 file
list when complete.

## Context

Project: `project02-collab-breakout`

Arc: `arc05-implementation-plan`

Slice: `slice04-implementation-sequence-synthesis`

Planning worktree:
`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`

Source checkout:
`/Users/oubiwann/lab/billosys/ai-engineering`

Do not edit source checkout files. This slice synthesizes the final
implementation sequence; it does not start implementation.

## Read First

From the planning worktree, read:

- `project02-collab-breakout/project-plan.md`
- `project02-collab-breakout/ledger.md`
- `project02-collab-breakout/arc05-implementation-plan/arc-plan.md`
- `project02-collab-breakout/arc05-implementation-plan/ledger.md`
- `project02-collab-breakout/arc05-implementation-plan/slice04-implementation-sequence-synthesis/slice-plan.md`
- `project02-collab-breakout/arc05-implementation-plan/slice04-implementation-sequence-synthesis/ledger.md`
- `project02-collab-breakout/arc05-implementation-plan/slice01-implementation-surface-map/cdc-verification.md`
- `project02-collab-breakout/arc05-implementation-plan/slice01-implementation-surface-map/artifacts/implementation-surface-inventory.md`
- `project02-collab-breakout/arc05-implementation-plan/slice01-implementation-surface-map/artifacts/release-validation-surface-map.md`
- `project02-collab-breakout/arc05-implementation-plan/slice02-component-contract-file-plan/cdc-verification.md`
- `project02-collab-breakout/arc05-implementation-plan/slice02-component-contract-file-plan/artifacts/component-contract-matrix.md`
- `project02-collab-breakout/arc05-implementation-plan/slice02-component-contract-file-plan/artifacts/component-file-layout-plan.md`
- `project02-collab-breakout/arc05-implementation-plan/slice02-component-contract-file-plan/artifacts/source-to-component-migration-plan.md`
- `project02-collab-breakout/arc05-implementation-plan/slice02-component-contract-file-plan/artifacts/package-source-contract-register.md`
- `project02-collab-breakout/arc05-implementation-plan/slice02-component-contract-file-plan/artifacts/support-adapter-dependency-plan.md`
- `project02-collab-breakout/arc05-implementation-plan/slice03-package-readme-validation-plan/cdc-verification.md`
- `project02-collab-breakout/arc05-implementation-plan/slice03-package-readme-validation-plan/artifacts/package-target-plan.md`
- `project02-collab-breakout/arc05-implementation-plan/slice03-package-readme-validation-plan/artifacts/readme-wayfinding-plan.md`
- `project02-collab-breakout/arc05-implementation-plan/slice03-package-readme-validation-plan/artifacts/skill-entrypoint-validation-plan.md`
- `project02-collab-breakout/arc05-implementation-plan/slice03-package-readme-validation-plan/artifacts/package-path-link-exception-plan.md`
- `project02-collab-breakout/arc05-implementation-plan/slice03-package-readme-validation-plan/artifacts/migration-compatibility-plan.md`
- `project02-collab-breakout/arc05-implementation-plan/slice03-package-readme-validation-plan/artifacts/slice04-implementation-sequence-inputs.md`
- `project02-collab-breakout/arc04-breakout-architecture/slice04-operator-acceptance-architecture-synthesis/artifacts/operator-accepted-architecture.md`

## Required Outputs

Create `artifacts/` under the slice directory and produce:

- `artifacts/implementation-sequence-roadmap.md`
- `artifacts/source-edit-risk-register.md`
- `artifacts/validation-matrix.md`
- `artifacts/acceptance-gate-plan.md`
- `artifacts/implementation-prompt-packet.md`
- `artifacts/arc05-close-readiness.md`
- `closing-report.md`

Update:

- `slice-plan.md`
- `ledger.md`

## Artifact Requirements

`implementation-sequence-roadmap.md` must provide the ordered source-edit
slices for implementing all eight accepted components:
`collaboration-framework`, `engineering-methods`, `project-management`,
`work-verification`, `testing`, `code-auditing`, `agent-coordination`, and
`contribution-style`. Include dependency order, rationale, expected commit
boundaries, and validation checkpoints.

`source-edit-risk-register.md` must cover compatibility for top-level
`SKILL.md`, old source paths, old prompt names, package roots, package-local
links, installed-skill routes, package-path exceptions, generated zip behavior,
provenance, and CCDP separation.

`validation-matrix.md` must map validation commands to surfaces and failure
modes. Include `make check-skills`, `make check-package-paths`, `make all`,
`make collab-framework`, component package targets, `git diff --check`, source
checkout cleanliness, and conditional CCDP gates.

`acceptance-gate-plan.md` must state Arc05 close gates, source implementation
entry gates, operator decisions, required proof, and no-go conditions.

`implementation-prompt-packet.md` must be a compact handoff for future source
implementation. Include the source-edit sequence, required context packet,
explicit file-list commit rules, co-author trailers, and the reminder that this
slice itself made no source edits.

`arc05-close-readiness.md` must say whether Arc05 will be ready to close after
Slice04 CDC verification, what remains open or deferred, and what evidence
shows source files remain untouched.

## Ledger And Close

Run every Verify command in the local `ledger.md`. Mark rows F-1 through F-9
`done` only when the commands pass and the evidence is present.

Write `closing-report.md` with:

- verdict
- artifact inventory
- ledger row walk
- silent-drop diff
- bubble-up to Arc05
- what worked
- closure summary

Set `slice-plan.md` to `proposed-done` only after the artifacts and ledger are
complete.

## Verification Commands

In addition to the ledger commands, run:

- Count ledger rows: `rg -c '^| F-[0-9]+' ledger.md`
- Count close-report row entries: `rg -c '^- F-[0-9]+:' closing-report.md`
- Count required artifacts: `find artifacts -maxdepth 1 -type f -name '*.md'`
- Check source checkout cleanliness: `git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet`
- Check planning diff whitespace for this slice:
  `git diff --check -- project02-collab-breakout/arc05-implementation-plan/slice04-implementation-sequence-synthesis`
- Check staged diff whitespace after staging:
  `git diff --cached --check`

## Commit Rule

After verification passes, stage and commit only the Slice04 files explicitly.
Do not include unrelated planning work.

Commit exactly the relevant Slice04 file list, expected to be:

- `project02-collab-breakout/arc05-implementation-plan/slice04-implementation-sequence-synthesis/slice-plan.md`
- `project02-collab-breakout/arc05-implementation-plan/slice04-implementation-sequence-synthesis/ledger.md`
- `project02-collab-breakout/arc05-implementation-plan/slice04-implementation-sequence-synthesis/cc-prompt.md`
- `project02-collab-breakout/arc05-implementation-plan/slice04-implementation-sequence-synthesis/artifacts/implementation-sequence-roadmap.md`
- `project02-collab-breakout/arc05-implementation-plan/slice04-implementation-sequence-synthesis/artifacts/source-edit-risk-register.md`
- `project02-collab-breakout/arc05-implementation-plan/slice04-implementation-sequence-synthesis/artifacts/validation-matrix.md`
- `project02-collab-breakout/arc05-implementation-plan/slice04-implementation-sequence-synthesis/artifacts/acceptance-gate-plan.md`
- `project02-collab-breakout/arc05-implementation-plan/slice04-implementation-sequence-synthesis/artifacts/implementation-prompt-packet.md`
- `project02-collab-breakout/arc05-implementation-plan/slice04-implementation-sequence-synthesis/artifacts/arc05-close-readiness.md`
- `project02-collab-breakout/arc05-implementation-plan/slice04-implementation-sequence-synthesis/closing-report.md`

Use a commit message like:

```text
Plan Project02 Arc05 implementation sequence

Co-authored-by: Codex <noreply@openai.com>

Co-authored-by: Billo AI <ai-engineering@billo.systems>
```
