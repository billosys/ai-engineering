# CC Prompt: Arc03 Slice03 Mechanical Framework Source Moves

You are CC for Project04 Arc03 Slice03,
`slice03-mechanical-framework-source-moves`.

Project04 is in Expedited Mode. Commit your own changes before CDC review, and
use explicit file lists for every `git add` and `git commit -- <paths>` command.
Do not use broad staging.

## Read First

From the planning checkout:

- `project04-knowledge-library-reorg/project-plan.md`
- `project04-knowledge-library-reorg/arc03-directory-reorg/arc-plan.md`
- `project04-knowledge-library-reorg/arc03-directory-reorg/ledger.md`
- `project04-knowledge-library-reorg/arc03-directory-reorg/slice02-top-level-compatibility-decision/cdc-verification.md`
- `project04-knowledge-library-reorg/arc03-directory-reorg/slice03-mechanical-framework-source-moves/slice-plan.md`
- `project04-knowledge-library-reorg/arc03-directory-reorg/slice03-mechanical-framework-source-moves/ledger.md`

Use these Arc02 handoff artifacts as implementation constraints:

- `project04-knowledge-library-reorg/arc02-directory-contract/slice02-accepted-directory-contract/artifacts/accepted-target-directory-contract.md`
- `project04-knowledge-library-reorg/arc02-directory-contract/slice02-accepted-directory-contract/artifacts/source-package-root-contract.md`
- `project04-knowledge-library-reorg/arc02-directory-contract/slice03-migration-validation-plan/artifacts/migration-sequence-plan.md`
- `project04-knowledge-library-reorg/arc02-directory-contract/slice04-implementation-handoff/artifacts/source-edit-slice-roadmap.md`

Work in the source checkout:
`/Users/oubiwann/lab/billosys/ai-engineering`.

## Assignment

Mechanically move the current selected-file collaboration-framework package
payload into `knowledge/collaboration-framework/` as a transitional source
root. Preserve source prose and package behavior.

Move this current payload:

- `docs/AI-CONSTITUTION-SUPPLEMENT.md`
- `docs/AI-ENGINEERING-METHODOLOGY.md`
- `docs/PROJECT-MANAGEMENT.md`
- `docs/pm/01-scales-of-work.md`
- `docs/pm/02-canonical-planning-worktree.md`
- `docs/pm/03-planning-top-down.md`
- `docs/pm/04-closing-slices.md`
- `docs/pm/05-closing-arcs.md`
- `docs/pm/06-confirmation-protocol.md`
- `docs/pm/07-anti-patterns.md`
- `docs/pm/08-maintenance.md`
- `docs/pm/09-worked-example-odm.md`
- `docs/pm/version-history.md`
- `docs/CODE-AUDIT.md`
- `docs/CODE-COVERAGE.md`
- `docs/SUBAGENT-DELEGATION-POLICY.md`
- `docs/CONTRIBUTION-STYLE.md`
- `templates/LEDGER-DISCIPLINE.md`
- `templates/CONTRIBUTION-TICKET.md`

Target root:

- `knowledge/collaboration-framework/docs/...`
- `knowledge/collaboration-framework/templates/...`

Keep `docs/ORIGINS.md` and `templates/GUIDE.md` in place. Do not move
domain/tooling skills, Biome entrypoints, or `protocols/ccdp`.

## Compatibility Decision Re-Entry

Slice02 selected no-shim because the composer source target did not exist yet.
This slice creates that target, so you must re-enter the decision.

Default to preserving top-level `SKILL.md` as the authoritative no-shim
entrypoint if validation can stay green. Update top-level `SKILL.md` links only
as needed to point at the moved framework payload. If that cannot preserve
route and package behavior, stop and record whether a validated shim or
replacement route is required before continuing.

`CLAUDE.md` must remain compatible with `AGENTS.md`; preserve symlink behavior
unless you have explicit evidence that changing it is required.

## Source Edit Boundaries

Allowed source edits:

- the moved files listed above;
- `SKILL.md` route/link/version-history updates required by moved payload paths;
- `Makefile` `CF_FILES` and directly related collaboration-framework packaging
  route updates;
- `package-path-exceptions.tsv` only for exact maintenance of existing
  collaboration-framework exception document paths after file movement;
- `README.md` and `AGENTS.md` only if direct route compatibility requires a
  narrow path update.

Not allowed without operator approval:

- splitting into Project02 specialist component roots;
- moving `docs/ORIGINS.md` or `templates/GUIDE.md`;
- adding new package-path exception rows, broad exceptions, or accepted
  warnings;
- CCDP package-policy changes;
- public skill kind/topology language;
- deep README or docs prose rewrite;
- committing generated zips.

## Required Artifacts

Create these under this slice's `artifacts/` directory:

- `artifacts/mechanical-move-manifest.md`
- `artifacts/source-prose-preservation-evidence.md`
- `artifacts/compatibility-route-update-record.md`
- `artifacts/package-validation-evidence.md`

## Validation

Run and record:

- source `git status --short` before and after source edits;
- source `git diff --check`;
- source `git diff --name-status --find-renames`;
- source-prose preservation checks, using byte-for-byte comparison for moved
  files whose bodies did not need route/link edits and explicit line-level
  disclosure for any route/link/version edits;
- `make check-skills`;
- `make collab-framework`;
- `make check-package-paths`;
- generated package inspection for `collaboration-framework.zip`, including
  package root and `SKILL.md` entrypoint;
- planning checkout `git diff --check`.

If `make check-package-paths` requires a moved existing exception path, update
only that existing exception row and record why it is mechanical maintenance,
not a new exception. If validation requires a new persistent exception or
accepted warning, stop for operator approval.

## Ledger and Close

Update `ledger.md` row by row with attested evidence. Then write
`closing-report.md` with:

- capability verdict;
- source commit and exact source path list;
- artifact inventory;
- row-by-row ledger walk for all six rows;
- source checkout status;
- planning checkout status;
- silent-drop check;
- Bubble-Up to Arc03, including anything Slice04 must account for.

Do not create `cdc-verification.md`; CDC owns that.

## Source Commit Instructions

Commit source changes first from the source checkout. Use exact touched paths.
For the expected move set, the path list should include old paths, new paths,
and directly edited compatibility/package files. Adjust the list to match the
actual touched files exactly.

```sh
git -C /Users/oubiwann/lab/billosys/ai-engineering add \
  SKILL.md \
  Makefile \
  package-path-exceptions.tsv \
  docs/AI-CONSTITUTION-SUPPLEMENT.md \
  docs/AI-ENGINEERING-METHODOLOGY.md \
  docs/PROJECT-MANAGEMENT.md \
  docs/pm/01-scales-of-work.md \
  docs/pm/02-canonical-planning-worktree.md \
  docs/pm/03-planning-top-down.md \
  docs/pm/04-closing-slices.md \
  docs/pm/05-closing-arcs.md \
  docs/pm/06-confirmation-protocol.md \
  docs/pm/07-anti-patterns.md \
  docs/pm/08-maintenance.md \
  docs/pm/09-worked-example-odm.md \
  docs/pm/version-history.md \
  docs/CODE-AUDIT.md \
  docs/CODE-COVERAGE.md \
  docs/SUBAGENT-DELEGATION-POLICY.md \
  docs/CONTRIBUTION-STYLE.md \
  templates/LEDGER-DISCIPLINE.md \
  templates/CONTRIBUTION-TICKET.md \
  knowledge/collaboration-framework/docs/AI-CONSTITUTION-SUPPLEMENT.md \
  knowledge/collaboration-framework/docs/AI-ENGINEERING-METHODOLOGY.md \
  knowledge/collaboration-framework/docs/PROJECT-MANAGEMENT.md \
  knowledge/collaboration-framework/docs/pm/01-scales-of-work.md \
  knowledge/collaboration-framework/docs/pm/02-canonical-planning-worktree.md \
  knowledge/collaboration-framework/docs/pm/03-planning-top-down.md \
  knowledge/collaboration-framework/docs/pm/04-closing-slices.md \
  knowledge/collaboration-framework/docs/pm/05-closing-arcs.md \
  knowledge/collaboration-framework/docs/pm/06-confirmation-protocol.md \
  knowledge/collaboration-framework/docs/pm/07-anti-patterns.md \
  knowledge/collaboration-framework/docs/pm/08-maintenance.md \
  knowledge/collaboration-framework/docs/pm/09-worked-example-odm.md \
  knowledge/collaboration-framework/docs/pm/version-history.md \
  knowledge/collaboration-framework/docs/CODE-AUDIT.md \
  knowledge/collaboration-framework/docs/CODE-COVERAGE.md \
  knowledge/collaboration-framework/docs/SUBAGENT-DELEGATION-POLICY.md \
  knowledge/collaboration-framework/docs/CONTRIBUTION-STYLE.md \
  knowledge/collaboration-framework/templates/LEDGER-DISCIPLINE.md \
  knowledge/collaboration-framework/templates/CONTRIBUTION-TICKET.md

git -C /Users/oubiwann/lab/billosys/ai-engineering commit -m "Move collaboration-framework source payload under knowledge" \
  -m "Co-authored-by: Codex <noreply@openai.com>" \
  -m "Co-authored-by: Billo AI <ai-engineering@billo.systems>" \
  -- \
  SKILL.md \
  Makefile \
  package-path-exceptions.tsv \
  docs/AI-CONSTITUTION-SUPPLEMENT.md \
  docs/AI-ENGINEERING-METHODOLOGY.md \
  docs/PROJECT-MANAGEMENT.md \
  docs/pm/01-scales-of-work.md \
  docs/pm/02-canonical-planning-worktree.md \
  docs/pm/03-planning-top-down.md \
  docs/pm/04-closing-slices.md \
  docs/pm/05-closing-arcs.md \
  docs/pm/06-confirmation-protocol.md \
  docs/pm/07-anti-patterns.md \
  docs/pm/08-maintenance.md \
  docs/pm/09-worked-example-odm.md \
  docs/pm/version-history.md \
  docs/CODE-AUDIT.md \
  docs/CODE-COVERAGE.md \
  docs/SUBAGENT-DELEGATION-POLICY.md \
  docs/CONTRIBUTION-STYLE.md \
  templates/LEDGER-DISCIPLINE.md \
  templates/CONTRIBUTION-TICKET.md \
  knowledge/collaboration-framework/docs/AI-CONSTITUTION-SUPPLEMENT.md \
  knowledge/collaboration-framework/docs/AI-ENGINEERING-METHODOLOGY.md \
  knowledge/collaboration-framework/docs/PROJECT-MANAGEMENT.md \
  knowledge/collaboration-framework/docs/pm/01-scales-of-work.md \
  knowledge/collaboration-framework/docs/pm/02-canonical-planning-worktree.md \
  knowledge/collaboration-framework/docs/pm/03-planning-top-down.md \
  knowledge/collaboration-framework/docs/pm/04-closing-slices.md \
  knowledge/collaboration-framework/docs/pm/05-closing-arcs.md \
  knowledge/collaboration-framework/docs/pm/06-confirmation-protocol.md \
  knowledge/collaboration-framework/docs/pm/07-anti-patterns.md \
  knowledge/collaboration-framework/docs/pm/08-maintenance.md \
  knowledge/collaboration-framework/docs/pm/09-worked-example-odm.md \
  knowledge/collaboration-framework/docs/pm/version-history.md \
  knowledge/collaboration-framework/docs/CODE-AUDIT.md \
  knowledge/collaboration-framework/docs/CODE-COVERAGE.md \
  knowledge/collaboration-framework/docs/SUBAGENT-DELEGATION-POLICY.md \
  knowledge/collaboration-framework/docs/CONTRIBUTION-STYLE.md \
  knowledge/collaboration-framework/templates/LEDGER-DISCIPLINE.md \
  knowledge/collaboration-framework/templates/CONTRIBUTION-TICKET.md
```

If you also touch `README.md`, `AGENTS.md`, or another allowed source file,
add it explicitly to both path lists.

## Planning Commit Instructions

After the source commit, commit the planning close packet from the planning
checkout with this exact path scope:

```sh
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning add \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice03-mechanical-framework-source-moves/artifacts/mechanical-move-manifest.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice03-mechanical-framework-source-moves/artifacts/source-prose-preservation-evidence.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice03-mechanical-framework-source-moves/artifacts/compatibility-route-update-record.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice03-mechanical-framework-source-moves/artifacts/package-validation-evidence.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice03-mechanical-framework-source-moves/ledger.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice03-mechanical-framework-source-moves/closing-report.md

git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning commit -m "Complete Project04 Arc03 Slice03" \
  -m "Co-authored-by: Codex <noreply@openai.com>" \
  -m "Co-authored-by: Billo AI <ai-engineering@billo.systems>" \
  -- \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice03-mechanical-framework-source-moves/artifacts/mechanical-move-manifest.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice03-mechanical-framework-source-moves/artifacts/source-prose-preservation-evidence.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice03-mechanical-framework-source-moves/artifacts/compatibility-route-update-record.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice03-mechanical-framework-source-moves/artifacts/package-validation-evidence.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice03-mechanical-framework-source-moves/ledger.md \
  project04-knowledge-library-reorg/arc03-directory-reorg/slice03-mechanical-framework-source-moves/closing-report.md
```
