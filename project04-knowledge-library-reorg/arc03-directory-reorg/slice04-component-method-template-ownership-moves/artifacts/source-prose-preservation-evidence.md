# Source-Prose Preservation Evidence

```yaml
project: project04-knowledge-library-reorg
arc: arc03-directory-reorg
slice: slice04-component-method-template-ownership-moves
artifact: source-prose preservation
source_commit: 873a5502acef9c087cefd78d468cf6d123a27341
source-files-edited: true
```

## Rename-Aware Evidence

`git show --name-status --find-renames --oneline HEAD` in the source checkout
reported the source commit as rename-aware moves:

```text
873a550 Complete Project04 Arc03 Slice04 source ownership moves
R100 knowledge/collaboration-framework/docs/SUBAGENT-DELEGATION-POLICY.md -> knowledge/agent-coordination/docs/SUBAGENT-DELEGATION-POLICY.md
R100 knowledge/collaboration-framework/docs/CODE-AUDIT.md -> knowledge/code-auditing/docs/CODE-AUDIT.md
R098 knowledge/collaboration-framework/docs/CONTRIBUTION-STYLE.md -> knowledge/contribution-style/docs/CONTRIBUTION-STYLE.md
R098 knowledge/collaboration-framework/templates/CONTRIBUTION-TICKET.md -> knowledge/contribution-style/templates/CONTRIBUTION-TICKET.md
R088 knowledge/collaboration-framework/docs/AI-ENGINEERING-METHODOLOGY.md -> knowledge/engineering-methods/docs/AI-ENGINEERING-METHODOLOGY.md
R096 knowledge/collaboration-framework/docs/PROJECT-MANAGEMENT.md -> knowledge/project-management/docs/PROJECT-MANAGEMENT.md
R098 knowledge/collaboration-framework/docs/pm/01-scales-of-work.md -> knowledge/project-management/docs/pm/01-scales-of-work.md
R096 knowledge/collaboration-framework/docs/pm/02-canonical-planning-worktree.md -> knowledge/project-management/docs/pm/02-canonical-planning-worktree.md
R096 knowledge/collaboration-framework/docs/pm/03-planning-top-down.md -> knowledge/project-management/docs/pm/03-planning-top-down.md
R097 knowledge/collaboration-framework/docs/pm/04-closing-slices.md -> knowledge/project-management/docs/pm/04-closing-slices.md
R098 knowledge/collaboration-framework/docs/pm/05-closing-arcs.md -> knowledge/project-management/docs/pm/05-closing-arcs.md
R100 knowledge/collaboration-framework/docs/pm/06-confirmation-protocol.md -> knowledge/project-management/docs/pm/06-confirmation-protocol.md
R100 knowledge/collaboration-framework/docs/pm/07-anti-patterns.md -> knowledge/project-management/docs/pm/07-anti-patterns.md
R086 knowledge/collaboration-framework/docs/pm/08-maintenance.md -> knowledge/project-management/docs/pm/08-maintenance.md
R100 knowledge/collaboration-framework/docs/pm/09-worked-example-odm.md -> knowledge/project-management/docs/pm/09-worked-example-odm.md
R096 knowledge/collaboration-framework/docs/pm/version-history.md -> knowledge/project-management/docs/pm/version-history.md
R099 knowledge/collaboration-framework/docs/CODE-COVERAGE.md -> knowledge/testing/docs/CODE-COVERAGE.md
R097 knowledge/collaboration-framework/templates/LEDGER-DISCIPLINE.md -> knowledge/work-verification/templates/LEDGER-DISCIPLINE.md
```

## Byte-For-Byte Pure Moves

The following `cmp` checks returned exit code `0`, proving byte-for-byte
preservation for pure move files:

```text
git show HEAD^:knowledge/collaboration-framework/docs/SUBAGENT-DELEGATION-POLICY.md | cmp - knowledge/agent-coordination/docs/SUBAGENT-DELEGATION-POLICY.md
git show HEAD^:knowledge/collaboration-framework/docs/CODE-AUDIT.md | cmp - knowledge/code-auditing/docs/CODE-AUDIT.md
git show HEAD^:knowledge/collaboration-framework/docs/pm/06-confirmation-protocol.md | cmp - knowledge/project-management/docs/pm/06-confirmation-protocol.md
git show HEAD^:knowledge/collaboration-framework/docs/pm/07-anti-patterns.md | cmp - knowledge/project-management/docs/pm/07-anti-patterns.md
git show HEAD^:knowledge/collaboration-framework/docs/pm/09-worked-example-odm.md | cmp - knowledge/project-management/docs/pm/09-worked-example-odm.md
```

## Route/Link Update Disclosure

Files below were not byte-for-byte pure moves because package-local route links
had to be updated after owner-root moves:

- `SKILL.md`: route links updated to the accepted owner roots; version bumped
  from `1.4.5` to `1.4.6`; Version History gained the Slice04 ownership-move
  entry.
- `AGENTS.md`: PM path updated from
  `knowledge/collaboration-framework/docs/PROJECT-MANAGEMENT.md` to
  `knowledge/project-management/docs/PROJECT-MANAGEMENT.md`.
- `Makefile`: `CF_FILES` updated to package the owner-root paths.
- `package-path-exceptions.tsv`: the existing code-audit source-clone
  placeholder exception path updated to
  `knowledge/code-auditing/docs/CODE-AUDIT.md`.
- Moved PM, methodology, coverage, ledger, contribution prose, and
  contribution template files: only package-local relative links were updated.

No source-prose rewrite, guide decomposition, README rewrite, Arc04 public docs
work, or Arc05 vocabulary work was performed.
