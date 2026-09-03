# Source-Prose Preservation Evidence

```yaml
project: project04-knowledge-library-reorg
arc: arc03-directory-reorg
slice: slice03-mechanical-framework-source-moves
artifact: source-prose-preservation-evidence
created-on: 2026-09-02
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
source_commit: 99cebae1e98004164e4ea6735c4a68bc60c233da
source-files-edited: true
```

## Preservation Summary

Source-prose preservation was checked with rename-aware Git evidence and
byte-for-byte comparison for files that were pure move candidates. No prose
rewrite was performed.

## Rename-Aware Diff Evidence

Command:

```sh
git -C /Users/oubiwann/lab/billosys/ai-engineering show --name-status --find-renames --oneline HEAD
```

Result summary:

- `git diff --name-status --find-renames` evidence records eighteen pure move
  payload files as `R100`.
- `docs/AI-ENGINEERING-METHODOLOGY.md` is recorded as `R098` because it moved
  and received route/link update plus version history edits.
- `SKILL.md`, `Makefile`, and `package-path-exceptions.tsv` were direct
  route/package maintenance edits.

## Byte-For-Byte Evidence

The following pure move files were checked with `cmp` against `HEAD^` old-path
content and returned `cmp OK`, proving byte-for-byte preservation:

- `docs/AI-CONSTITUTION-SUPPLEMENT.md`
- `docs/PROJECT-MANAGEMENT.md`
- `docs/CODE-AUDIT.md`
- `docs/CODE-COVERAGE.md`
- `docs/CONTRIBUTION-STYLE.md`
- `docs/SUBAGENT-DELEGATION-POLICY.md`
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
- `templates/CONTRIBUTION-TICKET.md`
- `templates/LEDGER-DISCIPLINE.md`

## Line-Level Disclosure

This section is the line-level disclosure for files that were not pure moves.

Route/link update disclosures:

- `SKILL.md`: bumped top-level entrypoint version from `1.4.4` to `1.4.5`,
  updated links from `./docs/...` and `./templates/...` to
  `./knowledge/collaboration-framework/docs/...` and
  `./knowledge/collaboration-framework/templates/...`, and added a Version
  History entry for the move.
- `Makefile`: updated `CF_FILES` from old `docs/` and `templates/` payload
  paths to `knowledge/collaboration-framework/docs/...` and
  `knowledge/collaboration-framework/templates/...`.
- `package-path-exceptions.tsv`: mechanically updated the existing
  `collaboration-framework.zip` exception document path from
  `docs/CODE-AUDIT.md` to
  `knowledge/collaboration-framework/docs/CODE-AUDIT.md`; no new exception row
  was added.
- `knowledge/collaboration-framework/docs/AI-ENGINEERING-METHODOLOGY.md`:
  converted one obsolete inline link to the historical
  `./dev/concept-cards/0009-howto-concept-card-extraction-with-claude-code-v3.2.md`
  path into a literal provenance path because the target is not present in the
  source checkout or package; added `Version 1.11` and updated the document
  footer from `1.10, 2026-09-01` to `1.11, 2026-09-02`.

These edits are route/link update and version history maintenance required by
the source move and package validation. They are not prose rewrites.
