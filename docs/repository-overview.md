# Repository Overview

AI Engineering is a source repository for assistant-facing knowledge material:
installable Markdown skill packages, supporting guides, support templates, and
the Composite Cognition Dispatch Protocol distribution. Start with the top-level
[`README.md`](../README.md) for the shortest route map, then use these focused
docs when you need more context.

## Top-Level Surfaces

| Path | Role |
|---|---|
| [`README.md`](../README.md) | Concise orientation, quick commands, and links to focused docs. |
| [`docs/`](./) | Human-facing explanation about the repository and how to navigate it. |
| [`knowledge/`](../knowledge/) | Source and derived knowledge-library substrate consumed by skills and packages. |
| [`SKILL.md`](../SKILL.md) | Top-level `collaboration-framework` composite framework/operational skill entrypoint. |
| [`protocols/`](../protocols/) | Protocol distributions, currently including CCDP. |
| [`templates/`](../templates/) | Cross-cutting support templates that are not owned by a single knowledge surface. |
| [`scripts/`](../scripts/) | Packaging and validation helpers used by the Makefile. |
| [`assets/`](../assets/) | Public assets such as README images. |

## How To Move Through The Repo

Use `docs/` to decide where to go next. These pages explain what exists, when
to use it, and which source path owns the detailed material. They are not the
source of truth for the skill content itself.

Use `knowledge/` when you need the actual material a skill loads or packages:
entrypoint `SKILL.md` files, topic guides, concept cards, extraction metadata,
source material, templates, and workbench notes where present.

Use `protocols/` for protocol distributions. CCDP has different packaging and
validation rules from installable skills, so it remains separate from the skill
library even though it is part of this repository.

Skill kind and topology are separate wayfinding axes. Kind names what a skill
is about, such as domain/tooling, framework/operational, or method work.
Topology names how it composes: Rust is the public example of an atomic
domain/tooling skill, while `collaboration-framework` is the public example of
a composite framework/operational skill.

## Common Entry Points

- Choosing a skill: [Skill library](./skill-library.md).
- Understanding the project-management and verification framework:
  [Collaboration framework](./collaboration-framework.md).
- Reading or maintaining the knowledge substrate:
  [Knowledge library anatomy](./knowledge-library-anatomy.md).
- Building, validating, or installing packages:
  [Building and installing](./building-and-installing.md).
- Reading CCDP: [Protocols](./protocols.md).
- Proposing changes: [Contributing](./contributing.md).
- Understanding the origin story: [Origins](./ORIGINS.md).

## Boundary To Keep In Mind

The repository deliberately separates explanation from substrate. `docs/`
helps humans find and understand the material. `knowledge/` stores the material
used by assistant skills and generated packages. If a page in `docs/` starts
duplicating a full guide, template, or source corpus, it should usually link to
the owning `knowledge/` path instead.
