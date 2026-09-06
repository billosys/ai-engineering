# Project05 Concept Card Skill Bootstrap Artifacts

```yaml
project: project05-concept-card-skill
artifact: bootstrap-artifact-manifest
status: seed-input
created-for: Project05 planning
current-authority: ../project-plan.md
project04-status: closed
```

## Purpose

This artifact directory is the seed packet for Project05. It preserves the
historical evidence that led into the project; it is not itself the
plan-of-record.

Project03 produced the method inventory, conceptual model, skill architecture,
and implementation plan. It did not create the source skill. Project04 has now
closed and its repository layout decisions supersede stale assumptions in the
older Project03 and early Project05 packet.

Project05 now uses these artifacts to implement two live skills:
`document-extraction` and `concept-cards`.

## Directory Contents

| Path | Contents | Use |
|------|----------|-----|
| `source-v32/` | Copies of the two original v3.2 workbench method documents. | Source baseline and provenance. |
| `release-context/` | Current README and 0.5.0 release-note context from the source checkout. | Discoverability, release-note, and package context. |
| `project03-concept-card-method/` | Full Project03 planning packet as copied from the planning worktree. | Method inventory, conceptual model, skill architecture, implementation plan, closure evidence, and preserved original assessment. |
| `operator-accepted-src-prep-arch.md` | Operator-accepted architecture for standalone PDF/EPUB source preparation as an upstream capability consumed by concept-card generation. | Planning input for Project05 roadmap, dependency, and implementation-scope decisions. |
| `operator-accepted-project05-reorientation.md` | Operator-accepted Project05 reorientation after Project04 closure. | Current naming, layout, and nondeferrable implementation input. |
| `fresh-codex-project05-planning-prompt.md` | Handoff prompt for a fresh Codex instance. | Starting prompt for creating the Project05 plan. |

## Important Boundary

The copied Project03 packet contains historical slice prompts, close reports,
and planning artifacts. Treat those files as evidence and source context, not
as current instructions.

The current authority order is:

- Project05 `project-plan.md`
- Project05 arc and slice open sets
- `operator-accepted-project05-reorientation.md`
- current Project04 close evidence and live source tree
- older Project03 and Project05 artifacts as provenance

## Project04 Status

Project04 is closed. Project05 is no longer blocked by it, but Project05 must
consume the current Project04 layout and packaging behavior before source
implementation begins.
