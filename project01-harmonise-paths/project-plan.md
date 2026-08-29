# Project 01: Harmonise Paths

```yaml
project: project01-harmonise-paths
status: active
depends-on: []
blocks:
  - reliable source-clone use of ai-engineering skills
  - reliable zip/unzipped use of ai-engineering skills and protocol packages
related:
  - /Users/oubiwann/lab/billosys/ai-engineering
  - Makefile
  - SKILL.md
  - docs/PROJECT-MANAGEMENT.md
  - templates/LEDGER-DISCIPLINE.md
  - protocols/ccdp
```

## Planning Substrate

Planning artifacts live on orphan branch `planning`, worktree
`.worktrees/planning`, under `project01-harmonise-paths/`, per
`docs/PROJECT-MANAGEMENT.md`.

The implementation checkout is the source repository's `main` worktree at
`/Users/oubiwann/lab/billosys/ai-engineering`. Planning artifacts are written
here; implementation changes land separately in implementation branches or the
main worktree as directed by the operator.

Slice-generated analysis artifacts that are part of planning or verification
live in the slice directory where they are generated. The source checkout's
`workbench/` is no longer the default home for temporary planning reports now
that the planning branch is separate from the implementation branch.

## Definition of Done

The project is done when humans and LLMs can use the ai-engineering materials
from either the cloned source tree or the generated zip/unzipped bundles
without having to rediscover where referenced files actually live.

Specifically:

- Source-clone entry points continue to work for project management, SDLC
  planning/execution, language-specific best practices, and CCDP protocol
  processing.
- Packaged zip entry points resolve their bundled references from the package
  root or from the current document location.
- References to material intentionally not bundled are explicitly marked as
  repo-only, provenance-only, or example project paths.
- The Makefile packaging flow owns any required source-to-package path
  transforms and fails or warns through a repeatable package-path check.
- CCDP has a first-class distribution story alongside the skill bundles.

## Boundaries

In scope:

- Packaging path semantics for the collaboration-framework bundle, per-domain
  skill bundles, under-developed tooling skills, and CCDP materials.
- Make/Bash-friendly staging transforms where they reduce duplicate source
  prose.
- Validation that checks generated archives rather than only source files.
- README or release-facing documentation needed to teach both source and zip
  use.

Out of scope:

- Rewriting mature language guide content for style or substance.
- Moving highly developed language-pack directory trees without a separate
  operator-approved project.
- Changing the collaboration-framework planning methodology except where this
  project discovers a recurring packaging-path anti-pattern that should bubble
  up for later methodology maintenance.
- Implementing CCDP runtime behavior.

## Arc Roadmap

### Arc 01: Distribution Path Contract

Status: active.

Capability: establish a repeatable inventory of package path failures and a
written path semantics contract that later implementation slices can apply
without re-litigating source-root versus package-root behavior.

Slices:

- `slice01-package-path-audit`: inventory current package-invalid path
  references, classify them, and propose the source/package path contract.
- `slice02-contract-gate-design`: planned later after slice 01 closes. Expected
  focus: convert the accepted contract into Make/Bash-friendly validation
  requirements and decide warning versus hard-fail gates.

### Arc 02: Skill Bundle Harmonisation

Status: stub.

Expected capability: update packaged skill entry points and, where needed,
staging transforms so source-clone and zip/unzipped usage both resolve correctly
for the collaboration-framework and per-domain skills.

Detailed arc planning is deferred until Arc 01 closes.

### Arc 03: CCDP Distribution Package

Status: stub.

Expected capability: give CCDP a first-class package target and reader-facing
entry point so protocol users can consume the assembled spec, source chapters,
canonical JSON, and examples without repo-root path guessing.

Detailed arc planning is deferred until Arc 02 closes or Arc 01 explicitly
bubbles up a need to advance CCDP earlier.

### Arc 04: Release and Adoption Hardening

Status: stub.

Expected capability: update README/install/release guidance, run package-path
and packaging checks, and prepare the project for publication.

Detailed arc planning is deferred until the implementation arcs close.

## Current Status

Arc 01 is active. Slice 01 is opened and ready for implementation. Later arcs
are roadmap stubs only; their detailed plans should be written after the close
of the previous slice or arc, per the plan-late/plan-deep rule.

## Version History

### v1.0 - 2026-08-29

Initial roadmap opened from the packaging-path diagnosis. The project adopts
the canonical orphan `planning` branch and `.worktrees/planning` layout.
