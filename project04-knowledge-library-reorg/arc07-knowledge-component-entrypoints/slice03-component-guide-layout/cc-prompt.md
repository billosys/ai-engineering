# CC Prompt: Arc07 Slice03 Component Guide Layout and Standalone Entrypoints

You are CC working in Expedited Mode for Project04 Arc07 Slice03.

Read first:

- `project04-knowledge-library-reorg/project-plan.md`
- `project04-knowledge-library-reorg/arc07-knowledge-component-entrypoints/arc-plan.md`
- `project04-knowledge-library-reorg/arc07-knowledge-component-entrypoints/ledger.md`
- `project04-knowledge-library-reorg/arc07-knowledge-component-entrypoints/slice03-component-guide-layout/slice-plan.md`
- `project04-knowledge-library-reorg/arc07-knowledge-component-entrypoints/slice03-component-guide-layout/ledger.md`
- Slice01 artifacts:
  - `slice01-component-entrypoint-contract/artifacts/component-entrypoint-decision-register.md`
  - `slice01-component-entrypoint-contract/artifacts/source-migration-impact-map.md`
  - `slice01-component-entrypoint-contract/artifacts/implementation-slice-roadmap.md`
- Slice02 artifacts:
  - `slice02-collaboration-framework-entrypoint-relocation/artifacts/source-reference-repair-report.md`
  - `slice02-collaboration-framework-entrypoint-relocation/artifacts/validation-report.md`
  - `slice02-collaboration-framework-entrypoint-relocation/cdc-verification.md`

## Assignment

Implement the accepted component-root entrypoint and guide-layout contract:

1. Move the long component documents from legacy `docs/` paths to `guides/`
   with explicit `git mv` path pairs.
2. Move `knowledge/project-management/docs/pm/*` directly to
   `knowledge/project-management/guides/`.
3. Add concise component-root `SKILL.md` wayfinders/contracts for:
   - `knowledge/agent-coordination/`;
   - `knowledge/code-auditing/`;
   - `knowledge/contribution-style/`;
   - `knowledge/engineering-methods/`;
   - `knowledge/project-management/`;
   - `knowledge/testing/`;
   - `knowledge/work-verification/`.
4. Update `knowledge/collaboration-framework/SKILL.md` to route to the new
   `guides/` paths and new component entrypoints.
5. Repair README/docs/AGENTS/component links and Makefile/package surfaces.
6. Update package-path exceptions only when an existing exception path moved or
   a narrow new exception is genuinely required.
7. Record implementation and validation evidence in the four expected
   artifacts, update the ledger, and write `closing-report.md`.

## Required Source Moves

Use explicit `git mv` operations for these tracked file moves:

```bash
git mv knowledge/collaboration-framework/docs/AI-CONSTITUTION-SUPPLEMENT.md knowledge/collaboration-framework/guides/AI-CONSTITUTION-SUPPLEMENT.md
git mv knowledge/agent-coordination/docs/SUBAGENT-DELEGATION-POLICY.md knowledge/agent-coordination/guides/SUBAGENT-DELEGATION-POLICY.md
git mv knowledge/code-auditing/docs/CODE-AUDIT.md knowledge/code-auditing/guides/CODE-AUDIT.md
git mv knowledge/contribution-style/docs/CONTRIBUTION-STYLE.md knowledge/contribution-style/guides/CONTRIBUTION-STYLE.md
git mv knowledge/engineering-methods/docs/AI-ENGINEERING-METHODOLOGY.md knowledge/engineering-methods/guides/AI-ENGINEERING-METHODOLOGY.md
git mv knowledge/project-management/docs/PROJECT-MANAGEMENT.md knowledge/project-management/guides/PROJECT-MANAGEMENT.md
git mv knowledge/project-management/docs/pm/01-scales-of-work.md knowledge/project-management/guides/01-scales-of-work.md
git mv knowledge/project-management/docs/pm/02-canonical-planning-worktree.md knowledge/project-management/guides/02-canonical-planning-worktree.md
git mv knowledge/project-management/docs/pm/03-planning-top-down.md knowledge/project-management/guides/03-planning-top-down.md
git mv knowledge/project-management/docs/pm/04-closing-slices.md knowledge/project-management/guides/04-closing-slices.md
git mv knowledge/project-management/docs/pm/05-closing-arcs.md knowledge/project-management/guides/05-closing-arcs.md
git mv knowledge/project-management/docs/pm/06-confirmation-protocol.md knowledge/project-management/guides/06-confirmation-protocol.md
git mv knowledge/project-management/docs/pm/07-anti-patterns.md knowledge/project-management/guides/07-anti-patterns.md
git mv knowledge/project-management/docs/pm/08-maintenance.md knowledge/project-management/guides/08-maintenance.md
git mv knowledge/project-management/docs/pm/09-worked-example-odm.md knowledge/project-management/guides/09-worked-example-odm.md
git mv knowledge/project-management/docs/pm/version-history.md knowledge/project-management/guides/version-history.md
git mv knowledge/testing/docs/CODE-COVERAGE.md knowledge/testing/guides/CODE-COVERAGE.md
```

Create destination `guides/` directories as needed before the moves.

After all tracked files are moved, remove emptied legacy directories with
`rmdir`:

```bash
rmdir knowledge/project-management/docs/pm
rmdir knowledge/agent-coordination/docs
rmdir knowledge/code-auditing/docs
rmdir knowledge/collaboration-framework/docs
rmdir knowledge/contribution-style/docs
rmdir knowledge/engineering-methods/docs
rmdir knowledge/project-management/docs
rmdir knowledge/testing/docs
```

Do not use `rm -rf`.

## Authorized Source Files

You may edit only these source surfaces unless a hard blocker requires a
bubble-up:

- `AGENTS.md`
- `Makefile`
- `README.md`
- `docs/ORIGINS.md`
- `docs/collaboration-framework.md`
- `docs/knowledge-library-anatomy.md`
- `docs/repository-overview.md`
- `docs/skill-library.md`
- `assets/packaging/path-exceptions.tsv`
- `knowledge/agent-coordination/**`
- `knowledge/code-auditing/**`
- `knowledge/collaboration-framework/**`
- `knowledge/contribution-style/**`
- `knowledge/engineering-methods/**`
- `knowledge/project-management/**`
- `knowledge/testing/**`
- `knowledge/work-verification/**`

Do not edit `CLAUDE.md` separately; it is the compatibility surface for
`AGENTS.md`. Do not edit release notes in this slice. Do not touch CCDP source.
Do not commit generated zips, `build/`, or ignored build outputs.

## Entrypoint Rules

- The new component-root `SKILL.md` files should be concise wayfinders:
  trigger/scope/routing, not copied long-form guides.
- Include useful metadata and descriptions compatible with
  `make check-skills`.
- Add the component-root `SKILL.md` files to `ALL_SKILL_FILES` so their
  descriptions are validated.
- Include the component-root `SKILL.md` files in the collaboration-framework
  package only as dependency files routed from the composite package.
- Do not add separate zip targets or install targets for these components.

## Required Repairs

- Repair the `../SKILL.md` reference surfaced by Slice02 in the moved
  engineering-methods guide.
- Update `knowledge/collaboration-framework/SKILL.md` route table and version
  history for the guide-path and component-entrypoint changes.
- Update project-management guide links after `docs/pm/` moves directly to
  `guides/`.
- Update `AGENTS.md` from the old project-management `docs/`/`docs/pm/`
  paths to the new component entrypoint and guide paths.
- Update README/docs source references from `knowledge/*/docs/...` to
  `knowledge/*/guides/...`, preserving package-entrypoint language where it
  refers to generated zip layout.
- Update `Makefile` `CF_FILES` paths and any staging logic required by the new
  package layout.

## Source Validation

Run, at minimum:

- source status before edits;
- source diff check;
- local README/docs/AGENTS/SKILL/component-guide link validation;
- `make check-skills`;
- `make collab-framework`;
- `make check-package-paths`;
- generated `collaboration-framework.zip` inspection confirming:
  - package root `collaboration-framework/`;
  - package entrypoint `collaboration-framework/SKILL.md`;
  - component `SKILL.md` files present under their package-local component
    paths;
  - moved long documents present under `guides/`, not legacy `docs/`;
- final source status.

## Commit Instructions

After source validation passes, commit the source changes before planning
closure. Stage only the authorized source paths with explicit pathspecs:

```bash
git add -A -- AGENTS.md Makefile README.md docs/ORIGINS.md docs/collaboration-framework.md docs/knowledge-library-anatomy.md docs/repository-overview.md docs/skill-library.md assets/packaging/path-exceptions.tsv knowledge/agent-coordination knowledge/code-auditing knowledge/collaboration-framework knowledge/contribution-style knowledge/engineering-methods knowledge/project-management knowledge/testing knowledge/work-verification
```

Use a source commit message like:

```text
Reshape collaboration framework component guides

Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

Then update and commit exactly the Slice03 planning packet:

- `arc07-knowledge-component-entrypoints/slice03-component-guide-layout/artifacts/component-guide-move-report.md`
- `arc07-knowledge-component-entrypoints/slice03-component-guide-layout/artifacts/component-entrypoint-report.md`
- `arc07-knowledge-component-entrypoints/slice03-component-guide-layout/artifacts/reference-and-package-repair-report.md`
- `arc07-knowledge-component-entrypoints/slice03-component-guide-layout/artifacts/validation-report.md`
- `arc07-knowledge-component-entrypoints/slice03-component-guide-layout/ledger.md`
- `arc07-knowledge-component-entrypoints/slice03-component-guide-layout/closing-report.md`

Use a planning commit message like:

```text
Complete Project04 Arc07 Slice03

Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

## Closure Output

Report:

- source commit hash;
- planning commit hash;
- files moved and component `SKILL.md` files added;
- validation commands and outcomes;
- confirmation that legacy tracked component `docs/` directories are gone;
- confirmation that templates remain under `templates/`;
- confirmation that package output uses `guides/` paths and contains no legacy
  component `docs/` holdovers;
- any bubble-up to Slice04 or Arc07.
