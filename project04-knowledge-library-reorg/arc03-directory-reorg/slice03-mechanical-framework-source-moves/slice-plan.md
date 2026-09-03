# Slice 03: Mechanical Framework Source Moves

```yaml
project: project04-knowledge-library-reorg
arc: arc03-directory-reorg
slice: slice03-mechanical-framework-source-moves
status: verified-closed
opened-by: CDC
opened-on: 2026-09-02
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source-files-edited: true
operating-mode: expedited
artifact_home: artifacts/
```

## Goal

Mechanically move the current selected-file collaboration-framework payload
from top-level `docs/` and `templates/` source paths into the accepted
transitional substrate root `knowledge/collaboration-framework/`, while
preserving source prose, top-level route compatibility, and package behavior.

## Scope

In scope:

- Create `knowledge/collaboration-framework/` as the transitional source root
  for the current collaboration-framework package payload.
- Mechanically move the current collaboration-framework payload files:
  `docs/AI-CONSTITUTION-SUPPLEMENT.md`,
  `docs/AI-ENGINEERING-METHODOLOGY.md`,
  `docs/PROJECT-MANAGEMENT.md`, `docs/pm/*.md`,
  `docs/CODE-AUDIT.md`, `docs/CODE-COVERAGE.md`,
  `docs/SUBAGENT-DELEGATION-POLICY.md`, `docs/CONTRIBUTION-STYLE.md`,
  `templates/LEDGER-DISCIPLINE.md`, and
  `templates/CONTRIBUTION-TICKET.md`.
- Preserve top-level `SKILL.md` as the authoritative no-shim compatibility
  entrypoint unless route validation proves a shim or replacement route is
  required.
- Update only route links, `Makefile` collaboration-framework package payload
  paths, and exact existing package-path exception document paths required by
  the move.
- Validate package root and entrypoint behavior for
  `collaboration-framework.zip`.

Out of scope:

- Splitting the moved framework payload into Project02 specialist component
  roots; Slice04 owns component, method, and template ownership moves.
- Rewriting source prose beyond mechanical route/link updates needed because
  files moved.
- Deep README rewrite or end-user docs prose; Arc04 owns that work.
- Public skill kind/topology wording; Arc05 owns that work.
- Moving `docs/ORIGINS.md`, `templates/GUIDE.md`, domain/tooling skills,
  Biome entrypoints, or CCDP source.
- Adding new package-path exception rows, broad exceptions, or accepted
  warnings without operator approval.
- Committing generated zip artifacts.

## Expected Target Shape

The expected transitional source root is:

```text
knowledge/collaboration-framework/
  docs/
    AI-CONSTITUTION-SUPPLEMENT.md
    AI-ENGINEERING-METHODOLOGY.md
    PROJECT-MANAGEMENT.md
    CODE-AUDIT.md
    CODE-COVERAGE.md
    SUBAGENT-DELEGATION-POLICY.md
    CONTRIBUTION-STYLE.md
    pm/
      01-scales-of-work.md
      02-canonical-planning-worktree.md
      03-planning-top-down.md
      04-closing-slices.md
      05-closing-arcs.md
      06-confirmation-protocol.md
      07-anti-patterns.md
      08-maintenance.md
      09-worked-example-odm.md
      version-history.md
  templates/
    LEDGER-DISCIPLINE.md
    CONTRIBUTION-TICKET.md
```

Top-level `SKILL.md`, `README.md`, `AGENTS.md`, `CLAUDE.md`, `Makefile`, and
`package-path-exceptions.tsv` remain compatibility/package surfaces, not
default source-material homes.

## Expected Artifacts

- `artifacts/mechanical-move-manifest.md`
- `artifacts/source-prose-preservation-evidence.md`
- `artifacts/compatibility-route-update-record.md`
- `artifacts/package-validation-evidence.md`

## Verification Approach

CC will close the slice by committing source edits first, then committing the
planning close packet. CDC will independently reproduce the ledger rows before
closing the slice.

Required validation includes:

- source `git status --short`;
- source `git diff --check`;
- source move review with `git diff --name-status --find-renames`;
- source-prose preservation evidence, using byte comparison where route/link
  edits did not change file bodies and explicit line-level disclosure where
  route/link edits were required;
- `make check-skills`;
- `make collab-framework`;
- `make check-package-paths`;
- generated package inspection for `collaboration-framework.zip`;
- planning `git diff --check`.

## Exit Criteria

- The current selected-file collaboration-framework payload is mechanically
  moved under `knowledge/collaboration-framework/`.
- Top-level `SKILL.md` compatibility is re-entered and preserved with evidence
  under the selected no-shim path, or a validated shim/replacement route is
  implemented with evidence.
- `Makefile` collaboration-framework packaging points at the moved payload and
  generated package behavior remains valid.
- Existing package-path exception rows are either still valid or mechanically
  updated to the moved document paths; no new persistent exception or accepted
  warning is added without operator approval.
- Source prose preservation evidence distinguishes pure moves from required
  route/link updates.
- CC commits source edits separately with exact file lists, then commits the
  exact planning close packet.
- `closing-report.md` walks all six rows, records source/planning checkout
  status, and bubbles findings up to Arc03.
