# CC Prompt: Slice 01 Source Inventory

You are executing Project 02, Arc 01, Slice 01 for the ai-engineering repo.

Read, in order:

1. `project02-collab-breakout/project-plan.md`
2. `project02-collab-breakout/ledger.md`
3. `project02-collab-breakout/arc01-framework-inventory/arc-plan.md`
4. `project02-collab-breakout/arc01-framework-inventory/ledger.md`
5. `project02-collab-breakout/arc01-framework-inventory/slice01-source-inventory/slice-plan.md`
6. `project02-collab-breakout/arc01-framework-inventory/slice01-source-inventory/ledger.md`

## Hard Gate

Do not execute this slice until `project01-harmonise-paths` is closed and
completely verified. Verify that condition from the planning worktree and cite
the evidence in ledger row F-1. If the evidence is absent or ambiguous, stop
and report the blocker. Do not infer closure from conversation memory.

## Work

Create these analysis artifacts in this slice directory:

- `framework-source-inventory.md`
- `source-to-concept-map.md`
- `project01-path-contract-notes.md`

Use actual source files from
`/Users/oubiwann/lab/billosys/ai-engineering`. Do not edit source files.

Inventory these required sources:

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

For each source, record:

- Role
- Major sections
- Load moment
- Standalone usefulness
- Dependencies
- Path/package notes
- Concepts and disciplines contributed
- Candidate breakout label, explicitly marked non-final

For Project 01, consume the verified closing artifacts and summarize only the
path/package constraints relevant to Project 02.

## Do Not

- Do not edit source files.
- Do not create or modify packaged zip artifacts.
- Do not decide final component boundaries.
- Do not treat current file boundaries as authoritative component boundaries.
- Do not execute if the Project 01 completion gate is not satisfied.

## Close

Update the slice ledger row by row with evidence. Then write
`closing-report.md` with a per-row walk and bubble-up notes for Arc 01. The
slice remains proposed-done until CDC independently verifies it in
`cdc-verification.md`.
