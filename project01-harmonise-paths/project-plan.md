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

Status: closed.

Capability: establish a repeatable inventory of package path failures and a
written path semantics contract that later implementation slices can apply
without re-litigating source-root versus package-root behavior.

Slices:

- `slice01-package-path-audit`: inventory current package-invalid path
  references, classify them, and propose the source/package path contract.
- `slice02-contract-gate-design`: convert the accepted contract into
  Make/Bash-friendly validation requirements and decide warning versus
  hard-fail gates.
- `slice03-package-path-gate-implementation`: stubbed for later implementation
  after Slice 02 closes.

### Arc 02: Skill Bundle Harmonisation

Status: active.

Capability: update packaged skill entry points and, where needed, staging
transforms so source-clone and zip/unzipped usage both resolve correctly for
the collaboration-framework and per-domain skills.

Slices:

- `slice01-tooling-entrypoint-links`: harmonise small tooling/simple skill
  entrypoint guide references where one `guides/...` spelling works in both
  source and package contexts.
- `slice02-collaboration-framework-links`: opened after Slice 01 closed.
  Focus: framework and project-management bundle links where source edits or
  narrow staging transforms resolve package warnings without changing
  methodology content.
- `slice03-mature-entrypoint-staging-transforms`: stub. Expected focus:
  package-stage transforms for mature language skill entrypoints where source
  root prose should not churn.
- `slice04-warning-policy-tightening`: stub. Expected focus: retire
  transitional exceptions that Arc 02 resolves and decide which remaining
  warnings belong to later arcs.

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

Arc 01 is closed. Arc 02 is active: Slice 01 is verified/closed and Slice 02 is
opened. Arc 03 and Arc 04 remain roadmap stubs only; their detailed plans
should be written after the close of the previous slice or arc, per the
plan-late/plan-deep rule.

## Version History

### v1.0 - 2026-08-29

Initial roadmap opened from the packaging-path diagnosis. The project adopts
the canonical orphan `planning` branch and `.worktrees/planning` layout.

### v1.1 - 2026-08-29

Slice 01 marked verified/closed and Slice 02 opened under Arc 01. The project
now records slice-local generated planning artifacts as the default pattern for
audit/design outputs.

### v1.2 - 2026-08-29

Slice 02 marked verified/closed under Arc 01. Slice 03 is ready to open from
the accepted contract gate design.

### v1.3 - 2026-08-29

Slice 03 opened under Arc 01. Its open set adopts the framework's default
`artifacts/` home for durable slice-produced evidence.

### v1.4 - 2026-08-29

Slice 03 marked verified/closed. Arc 01 is ready for formal close before Arc
02 is planned in detail.

### v1.5 - 2026-08-29

Arc 01 closed with composition verdict delivered. Arc 02 opened from Arc 01
bubble-up, and Slice 01 opened for tooling/simple skill entrypoint link
harmonisation.

### v1.6 - 2026-08-29

Arc 02 Slice 01 marked verified/closed. The slice burned the targeted
tooling/simple skill entrypoint bundled-reference warning class from 20 to 0
without new package-path hard failures. No project-plan change is required
before Arc 02 Slice 02.

### v1.7 - 2026-08-29

Arc 02 Slice 02 opened on collaboration-framework links. The slice follows
Slice 01's package-warning burn-down pattern but adds a required classification
step because the framework bundle contains both true package-internal links and
intentional source/provenance examples.
