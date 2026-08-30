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
- `slice03-package-path-gate-implementation`: implement the accepted package
  path gate and transitional exception policy.

### Arc 02: Skill Bundle Harmonisation

Status: closed.

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
- `slice03-mature-entrypoint-staging-transforms`: package-stage transforms for
  mature language skill entrypoints where source-root prose should not churn.
- `slice04-warning-policy-tightening`: retire stale Arc 02 transitional policy
  and decide which remaining warnings belong to later maintenance or arcs.

### Arc 03: CCDP Distribution Package

Status: closed.

Capability: give CCDP a first-class package target and reader-facing
entry point so protocol users can consume the assembled spec, source chapters,
canonical JSON, and examples without repo-root path guessing.

Arc 03 delivered `make ccdp-package`, `make check-ccdp-package`, `ccdp.zip`,
a CCDP-specific package validator, generated-output freshness checking,
source-clone entrypoint guidance, and package-local reader guidance.

### Arc 04: Release and Adoption Hardening

Status: stub.

Expected capability: update README/install/release guidance, run package-path
and packaging checks, and prepare the project for publication.

Detailed arc planning is deferred until the implementation arcs close.

## Current Status

Arc 01, Arc 02, and Arc 03 are closed. Arc 04 remains a roadmap stub and is
ready for detailed planning next, per the plan-late/plan-deep rule.

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

### v1.8 - 2026-08-29

Arc 02 Slice 02 marked verified/closed. The slice burned collaboration-framework
`bundled-reference` warnings from 4 to 0, moved total package-path warnings from
406 to 402, and preserved non-bundled framework examples as classified warnings
for later policy tightening.

### v1.9 - 2026-08-29

Arc 02 Slice 03 opened on mature language entrypoint staging transforms. The
slice targets generated-package path harmonisation for mature entrypoints while
keeping broad mature guide prose and directory restructuring out of scope.

### v1.10 - 2026-08-29

Arc 02 Slice 03 marked verified/closed. The slice burned targeted mature
entrypoint `bundled-reference` warnings from 107 to 0 and moved total
package-path warnings from 402 to 295 without mature guide prose rewrites.

### v1.11 - 2026-08-29

Arc 02 Slice 04 opened on warning policy tightening. The slice will classify
the remaining post-Slice-03 warnings, retire or convert transitional exception
rows, and preserve unresolved package usability issues as visible later-arc
work rather than broad exceptions.

### v1.12 - 2026-08-29

Arc 02 Slice 04 marked verified/closed, and Arc 02 closed with composition
verdict delivered. The final skill-bundle package-path gate scans 12 generated
zips with 0 hard failures, 295 visible warnings, and 3 explicit exceptions.

### v1.13 - 2026-08-29

Arc 03 opened on CCDP distribution packaging after Arc 02 close. Slice 01
starts with a CCDP distribution inventory so package contents, entrypoint, path
semantics, and validation are designed from the actual protocol surface.

### v1.14 - 2026-08-29

Arc 03 Slice 01 marked verified/closed. The CCDP distribution inventory found
that workbench/prompts should be excluded by default, the package likely needs
a `ccdp/` root and package-local entrypoint, and generated assembled-spec drift
needs an explicit contract decision.

### v1.15 - 2026-08-29

Arc 03 Slice 02 opened on CCDP package contract design. The slice will choose
archive identity, contents, entrypoint, read-only/rebuild-capable semantics,
path transforms, validation/checker policy, and generated-output freshness
before package implementation.

### v1.16 - 2026-08-29

Arc 03 Slice 02 marked verified/closed. The accepted CCDP package contract
selects `ccdp.zip`, root `ccdp/`, generated package-local `ccdp/README.md`,
one rebuild-capable/read-only usable package, and a CCDP-specific checker.

### v1.17 - 2026-08-29

Arc 03 Slice 03 opened on CCDP package implementation. The slice will implement
the package/check targets, package staging, generated README, required
contents/exclusions, zip/unzip validation, extracted-package assembly, and the
generated-output freshness gate required by the Slice 02 contract.

### v1.18 - 2026-08-29

Arc 03 Slice 03 marked verified/closed. CCDP now has `make ccdp-package`,
`make check-ccdp-package`, `ccdp.zip`, a package-local README, a
CCDP-specific validator, and a freshness gate that keeps the assembled spec
from drifting before packaging.

### v1.19 - 2026-08-29

Arc 03 Slice 04 opened on CCDP reader guidance. The slice will update
source-clone and package/unzipped instructions so humans and LLMs can find the
right CCDP entrypoints without repo-root guessing.

### v1.20 - 2026-08-29

Arc 03 Slice 04 marked verified/closed. CCDP reader guidance now points
source-clone users at `protocols/ccdp/README.md`, package users at
`ccdp/README.md`, distinguishes `ccdp.zip` from installable skill bundles, and
labels `workbench/` and `prompts/` as source-only excluded material.

### v1.21 - 2026-08-29

Arc 03 closed with composition verdict delivered. CCDP now has a first-class
protocol package, validator, generated-output freshness gate, zipped/unzipped
path validation, and reader guidance for both source and package contexts.
