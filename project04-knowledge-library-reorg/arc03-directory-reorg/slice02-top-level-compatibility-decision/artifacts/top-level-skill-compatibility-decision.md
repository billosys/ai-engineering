# Top-Level SKILL.md Compatibility Decision

```yaml
project: project04-knowledge-library-reorg
arc: arc03-directory-reorg
slice: slice02-top-level-compatibility-decision
artifact: top-level-skill-compatibility-decision
created-on: 2026-09-02
selected path: no-shim
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
source-files-edited: false
```

## Decision

Selected path: no-shim.

The top-level SKILL.md remains authoritative for now. No source edit is
required in Slice02 because the current source checkout already preserves the
collaboration-framework composer entrypoint, package root, and package
load behavior:

- top-level `SKILL.md` declares `name: collaboration-framework`;
- `Makefile` packages top-level `SKILL.md` into `collaboration-framework.zip`;
- `make collab-framework` produces a zip rooted at `collaboration-framework/`;
- the generated package contains `collaboration-framework/SKILL.md` as the
  entrypoint;
- `README.md` documents `/collaboration-framework` as the daily-driver route;
- `AGENTS.md` preserves standing instructions for loading the current
  `collaboration-framework` skill;
- `CLAUDE.md` remains a symlink to `AGENTS.md`.

This is an explicit no-shim decision, not a rejection of the future accepted
`knowledge/collaboration-framework/` composer source root. It keeps the current
top-level route authoritative until the later composer move slice has concrete
files to route.

## Alternatives Considered

| Path | Disposition | Rationale |
|------|-------------|-----------|
| validated shim | not selected now | A shim would be premature because `knowledge/collaboration-framework/` composer source material has not moved yet. Creating a shim now would introduce routing text without a moved target to validate. |
| replacement route | not selected now | A replacement route would require package/list and possibly README/SKILL routing changes before the new authoritative source root exists. That would violate the accepted ordering. |
| no-shim | selected path | The current top-level `SKILL.md` is already the authoritative composer entrypoint and validates with the existing package route. This preserves compatibility before composer moves. |

## Rationale

Arc03 requires a top-level compatibility decision before composer source moves.
The least risky decision is to keep the current `SKILL.md` authoritative for
now because it is already the package entrypoint and daily-driver route. This
avoids source churn before the mechanical move slice and keeps source edits out
of Slice02.

The decision preserves the Arc02/Arc03 ordering:

- top-level compatibility is decided before composer moves;
- mechanical moves before prose rewrites;
- package-local link repair before exceptions;
- Arc04 owns end-user docs;
- Arc05 owns public vocabulary.

## Re-Entry Condition

Re-entry condition: when a later Arc03 slice moves collaboration-framework
composer source material toward `knowledge/collaboration-framework/`, that
slice must revisit this no-shim decision and either:

- keep top-level `SKILL.md` authoritative with evidence;
- replace it with a validated shim;
- implement a replacement route that preserves `collaboration-framework.zip`
  root and entrypoint behavior.

The later slice must validate `make check-skills`, `make collab-framework`,
package root behavior, and entrypoint behavior after any source route change.
