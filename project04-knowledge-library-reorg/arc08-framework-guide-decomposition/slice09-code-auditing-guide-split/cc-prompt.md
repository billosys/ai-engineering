# CC Prompt: Arc08 Slice09 Code-Auditing Guide Split

You are CC working in Project04 Arc08 Slice09.

## Required Reading

Read these before editing:

- `arc08-framework-guide-decomposition/arc-plan.md`
- `arc08-framework-guide-decomposition/ledger.md`
- `arc08-framework-guide-decomposition/slice09-code-auditing-guide-split/slice-plan.md`
- `arc08-framework-guide-decomposition/slice09-code-auditing-guide-split/ledger.md`
- `arc08-framework-guide-decomposition/slice08-testing-guide-split/cdc-verification.md`
- `arc08-framework-guide-decomposition/slice07-work-verification-guide-split/cdc-verification.md`
- `artifacts/operator-accepted-architecture.md`
- `artifacts/component-file-layout-plan.md`
- Source `AGENTS.md`
- Source `knowledge/collaboration-framework/SKILL.md`
- Source `knowledge/code-auditing/SKILL.md`
- Source `knowledge/code-auditing/guides/CODE-AUDIT.md`
- Source `knowledge/code-auditing/version-history.md`
- Source `knowledge/testing/SKILL.md`

## Assignment

Implement Slice09 exactly as scoped: split or extract the current code-auditing
material into the five accepted numbered guides:

- `knowledge/code-auditing/guides/01-audit-scope-and-map.md`
- `knowledge/code-auditing/guides/02-findings-and-severity.md`
- `knowledge/code-auditing/guides/03-scale-aware-auditing.md`
- `knowledge/code-auditing/guides/04-modernization-synthesis.md`
- `knowledge/code-auditing/guides/05-audit-to-hardening-handoff.md`

The existing `knowledge/code-auditing/guides/CODE-AUDIT.md` file is the
current source material. Prefer preserving Git history by moving it with an
explicit `git mv` if it becomes one of the accepted guide files, then extract
the remaining focused material into companion guides.

Do not perform a heading-only split. The resulting guides must be independently
useful, correctly cross-routed, and easier to load selectively than the current
single audit guide.

Preserve the current quality floor: diagnosis-only audit posture, language/tool
detection, audit-map construction, all-scale review, severity classes, finding
format with file:line evidence, per-language reports, top-level index,
modernization synthesis, negative findings, and final verification checklist.
Do not weaken the instruction that a full audit is not a context-window sampling
pass and does not make code changes.

Repair all affected routes, including code-auditing `SKILL.md`,
`version-history.md`, Makefile `CF_FILES`, collaboration-framework routes,
work-verification, testing, project-management and engineering-methods
references, public docs, AGENTS, release notes, staging scripts, and
package-path exceptions where needed.

Use explicit `git mv` path pairs for source moves. If an empty directory must
be removed, use `rmdir` as a precaution. Do not use `rm -rf`.

## Required Artifacts

Create these planning artifacts:

- `artifacts/current-code-auditing-surface-map.md`
- `artifacts/code-auditing-split-map.md`
- `artifacts/legacy-code-audit-disposition.md`
- `artifacts/source-route-repair-map.md`
- `artifacts/source-validation-results.md`

Update:

- `ledger.md`

Create:

- `closing-report.md`

Do not create `cdc-verification.md`.

## Validation

Run the slice ledger verifier commands and record results in
`artifacts/source-validation-results.md` and `closing-report.md`.

At minimum, source validation must include:

- source `git diff --check`
- focused local Markdown link validation for touched route surfaces
- `make check-skills`
- `make collab-framework`
- `make check-package-paths`
- generated `collaboration-framework.zip` inspection confirming the five new
  code-auditing guides are present and the old `CODE-AUDIT.md` path follows
  `artifacts/legacy-code-audit-disposition.md`

Run package builds sequentially. Do not commit generated zips, `build/`, or
`target/skills`.

## Commit Requirements

Use explicit file lists for commits.

If source files change, commit only the exact source files you changed with a
message like:

```text
Split code-auditing guide surface

Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

Then commit only the exact Slice09 planning files you changed with a message
like:

```text
Complete Project04 Arc08 Slice09

Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

Final report should include source commit hash if one was created, planning
commit hash, validation summary, `CODE-AUDIT.md` disposition, and final
source/planning cleanliness.
