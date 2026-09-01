# Project05 Concept Card Skill Bootstrap Artifacts

```yaml
project: project05-concept-card-skill
artifact: bootstrap-artifact-manifest
status: seed-input
created-for: fresh Project05 planning
blocked-by: project04-knowledge-library-reorg
```

## Purpose

This artifact directory is the seed packet for a future planning project that
will implement the v4.0 concept-card method as an actual repository skill.

Project03 produced the method inventory, conceptual model, skill architecture,
and implementation plan. It did not create the source skill. Project05 should
use these inputs to plan and then implement that source skill after the
Project04 knowledge-library reorganization determines the final destination
layout.

## Directory Contents

| Path | Contents | Use |
|------|----------|-----|
| `source-v32/` | Copies of the two original v3.2 workbench method documents. | Source baseline and provenance. |
| `release-context/` | Current README and 0.5.0 release-note context from the source checkout. | Discoverability, release-note, and package context. |
| `project03-concept-card-method/` | Full Project03 planning packet as copied from the planning worktree. | Method inventory, conceptual model, skill architecture, implementation plan, closure evidence, and preserved original assessment. |
| `fresh-codex-project05-planning-prompt.md` | Handoff prompt for a fresh Codex instance. | Starting prompt for creating the Project05 plan. |

## Important Boundary

The copied Project03 packet contains historical slice prompts, close reports,
and planning artifacts. Treat those files as evidence and source context, not
as current instructions. The only current handoff instruction in this directory
is `fresh-codex-project05-planning-prompt.md`.

## Blocker

Project05 is blocked on the Project04 knowledge-library reorganization for the
final source destination and package layout. A Project05 plan may be created
now, but source implementation should wait until Project04 closes or an
operator explicitly records a compatible interim layout decision.
