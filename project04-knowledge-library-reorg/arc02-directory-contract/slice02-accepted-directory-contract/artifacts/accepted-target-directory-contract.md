# Accepted Target Directory Contract

```yaml
project: project04-knowledge-library-reorg
arc: arc02-directory-contract
slice: slice02-accepted-directory-contract
artifact: accepted-target-directory-contract
artifact-status: accepted planning contract
created-on: 2026-09-02
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
source-files-edited: false
```

## Purpose

This artifact selects the accepted target directory contract for Project04
from the verified Arc02 Slice01 decision surface. It is a planning contract,
not source-edit authorization. Arc03 implementation slices own source moves,
and Slice03 owns the migration sequence, validation matrix, and package-path
exception policy that make this contract executable.

## Contract Summary

The accepted target directory contract is:

- `README.md` remains the top-level repository orientation and pointer map.
- `docs/` is user-facing explanation about repository materials, package
  behavior, protocols, methods, contribution paths, and knowledge-library
  anatomy.
- `knowledge/` is the default home for raw and derived knowledge-library
  substrate, including current domain/tooling skills and accepted future
  framework/operational or method skill source material.
- `templates/` remains top-level only for true cross-cutting support templates;
  owner-local templates move under the owning `knowledge/` or protocol root
  when an implementation arc can preserve package behavior.
- `protocols/ccdp/` remains the separate CCDP protocol and package surface.
- Top-level `SKILL.md`, `AGENTS.md`, and `CLAUDE.md` remain top-level
  compatibility surfaces unless a later implementation arc explicitly changes
  them with validation evidence.
- Wrappers and migration notes are required where old public or package-local
  paths point to moved substrate.
- Explicit exception rows are required for any accepted source-like material
  that remains outside its default root.

## Accepted Rules

| Surface | Accepted rule | Rationale | Later owner |
|---------|---------------|-----------|-------------|
| `README.md` | Keep top-level as concise orientation and route map. | Project04 requires users to start at README and branch into explanation, substrate, build/install, and protocol surfaces without ambiguity. | Arc04 public docs. |
| `docs/` | Keep as explanation about materials, not the default source substrate. | Arc01/Arc02 evidence distinguishes end-user explanation from reusable knowledge material. | Arc03 moves, Arc04 docs. |
| Source-like framework docs currently under `docs/` | Move to an owning `knowledge/` substrate root when preservation and package gates allow; leave wrapper or migration note in `docs/` if needed. | They are framework/operational material rather than reader-only docs. | Arc03, Slice03 plan. |
| `docs/dev/` extraction, provenance, and design material | Assign to owning method, framework, or provenance root under `knowledge/` unless a file is accepted as reader-facing explanation. | Folder placement alone is not decisive; owner and load reason decide. | Arc03, Slice03 plan. |
| `knowledge/` | Default substrate root for domain/tooling, framework/operational, method, source/provenance, and support material that functions as knowledge-library input. | Matches current domain/tooling roots and Project04 DoD. | Arc03 implementation. |
| Current domain/tooling skills | Preserve `knowledge/<slug>/` source roots unless a validated package defect requires a specific exception. | Current source already follows the desired substrate model. | Arc03 implementation. |
| Project02 framework/operational components | Accept `knowledge/<component>/` as the default source root family, with `knowledge/collaboration-framework/` for the composer when it moves from top-level selected-file packaging. | Keeps framework source in the substrate tree without adding an extra taxonomy directory before Arc05 public vocabulary. | Arc03 implementation, Project02 preservation gates. |
| `collaboration-framework` composer | Preserve as daily-driver composite composer; keep the package root named `collaboration-framework` even if source files move under `knowledge/collaboration-framework/`. | Project02 accepted the composer role, and Slice01 verified source root and package root must remain separate. | Arc03 implementation. |
| Planned `concept-card-method` | Reserve `knowledge/concept-card-method/` as the planned method-skill source root; do not claim live source or generated package availability before implementation. | Project03 makes it a planned method skill, not current source. | Project05/Arc03 coordination. |
| `knowledge/biome/` | Preserve as a single multi-entrypoint source root that may produce multiple package roots. | Slice01 verified Biome as a first-class edge case. | Arc03 validation. |
| `templates/` | Keep only cross-cutting support templates at top level; move owner-local templates with their owning component, method, skill, or protocol package when safe. | Prevents support payloads from becoming ambiguous source roots while preserving shared templates. | Slice03 policy, Arc03 moves. |
| `protocols/ccdp/` | Keep separate from installable skill packages; use docs or skill wrappers to point to it, not package absorption. | Project04 and Project02 preserve CCDP as a separate protocol distribution. | CCDP validation gates. |
| `SKILL.md` | Keep top-level until an implementation slice provides an accepted compatibility shim, replacement route, or no-shim operator decision. | Current composer packaging and installed-skill route behavior depend on this compatibility surface. | Slice03 policy, Arc03 implementation. |
| `AGENTS.md` and `CLAUDE.md` | Keep top-level; preserve the compatibility/symlink intent unless explicitly changed. | They are repository/session compatibility surfaces, not skill substrate roots. | Arc03 implementation if path language changes. |

## Wrapper And Migration Note Rules

- Add a wrapper when a stable human-facing route under `docs/` would otherwise
  disappear after moving source material.
- Add a migration note when a path has been documented, packaged, or cited and
  readers need a dated explanation of the new route.
- Prefer package-local link repair before adding package-path exceptions.
- A wrapper must explain where to go; it must not duplicate the moved source
  prose unless a later doc-rewrite slice explicitly authorizes that rewrite.
- A migration note must name whether the old path is deprecated, transitional,
  or retained as an explicit exception.

## Explicit Exception Rules

An explicit exception is required when:

- source-like or substrate-like material remains under `docs/`;
- owner-local support files remain in top-level `templates/`;
- top-level `SKILL.md` remains as a composer source after the composer source
  root moves;
- source root and package root intentionally diverge;
- a package-local link cannot be repaired and must use a path exception;
- a protocol package surface is linked from a skill package but remains outside
  the installable skill package set.

Each exception must record owner, reason, validation command, expiration or
no-expiration rationale, and re-entry condition.

## Boundary

This accepted target directory contract records planning decisions only.
It is not source-edit authorization, not final public vocabulary, and not a
migration sequence. Arc03 owns implementation, Arc05 owns public taxonomy
language, and Slice03 owns the migration sequence and validation matrix.
