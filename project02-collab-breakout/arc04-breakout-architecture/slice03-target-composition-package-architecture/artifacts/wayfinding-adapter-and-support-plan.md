# Wayfinding, Adapter, And Support Plan

```yaml
project: project02-collab-breakout
arc: arc04-breakout-architecture
slice: slice03-target-composition-package-architecture
status: proposed-done
artifact-status: proposed-wayfinding-input
operator-acceptance: pending
```

## Input Contract

This artifact consumes the verified Slice01 architecture decision method and
component-contract schema, plus the verified Slice02 support/adapter/
constraint dispositions and slice03 composition inputs. It complements
`target-component-architecture.md` and `package-and-release-architecture.md`.

The wayfinding, adapter placement, and support asset travel plan below is
proposed architecture only. Slice04 must still accept or change it.

## Top-Level Composer

The top-level composer remains the `collaboration-framework` entrypoint and is
thin but not link-only.

It should carry:

- a compact safety floor from `collaborative-posture-and-ethics`;
- a compact process floor from `engineering-methodology-and-process`;
- a route table for component selection;
- a short note for agent adapter role terms;
- a short repository orientation note for source/package reader modes;
- links or route names for direct-load components, the PM family, ledger,
  audit, coverage, delegation, contribution, and domain skills;
- package/release gate reminders only where needed for reader orientation.

It should not carry:

- full PM lifecycle mechanics;
- full ledger verification protocol;
- full audit, coverage, delegation, or contribution guide content;
- final package paths before operator acceptance;
- CCDP protocol distribution content.

This keeps the composer useful for broad session start while respecting the
breakout goal.

## Route Table

| Trigger | Route | Required Context |
|---------|-------|------------------|
| Broad or ambiguous substantial work | `collaboration-framework` top-level composer | Compact safety floor, route table, and adapter notes. |
| Collaboration posture, uncertainty, structural pulls, or peer frame | `collaborative-posture-and-ethics` | Methodology dependency link. |
| SDLC, sustained process, or quality floor | `engineering-methodology-and-process` | Posture prerequisite and routed component list. |
| Open, plan, close, or maintain project/arc/slice work | `project-management` PM wayfinder | Planning worktree note and ledger dependency. |
| Close, verify, or audit ledger evidence | `ledger-verification-protocol` | Evidence strength, row states, independent verification, silent-drop rules. |
| Code review, whole-repo diagnosis, modernization audit | `code-audit-discipline` | Diagnosis-only scope, domain skills, output-home convention. |
| Raise or repair coverage | `coverage-hardening-discipline` | Project tooling adapter and domain skills. |
| Decide whether to use subagents | `delegation-policy` | Thinking-vs-lookup rule and role adapter. |
| Draft upstream ticket or maintainer-facing proposal | `contribution-style-and-voice` | `CONTRIBUTION-TICKET.md` support asset and citation caveats. |
| Source clone, generated zip, installed skill, or CCDP-adjacent reading | `repository-orientation-and-distribution` adapter | Source/package reader modes and package-local link behavior. |

## PM Wayfinder

The PM wayfinder stays inside the `project-management` component family by
default.

It should:

- route to project, arc, and slice planning scales;
- route to canonical planning worktree guidance;
- route to top-down planning and open-set methods;
- route to slice and arc close mechanics;
- route to ledger-verification-protocol for ledgered verification;
- expose PM examples, planning anti-patterns, and provenance/version history
  notes as support assets;
- include local source/package reader notes so the family can be used from a
  source clone, generated zip, or installed skill.

It should not become a standalone component unless Slice04 records a concrete
package need.

## Agent Adapter

The proposed agent adapter placement is central plus local notes.

Central adapter owner:

- owns CC, CDC, Codex, Claude, Claude Code, Claude Desktop, Cowork, operator,
  planner, implementer, verifier, and main-context role mappings;
- owns drift-control language for role terms;
- owns the canonical short-note pattern that direct-load components can reuse.

Component owners:

- include a short local note wherever standalone use would otherwise be
  unclear;
- cite the central adapter when package-local links can resolve;
- avoid copying long role taxonomy into every package.

This is an adapter, not a standalone component by default. The local notes are
required because central-only role mapping can fail when a component is loaded
alone, while local-only mapping would drift.

## Repository Orientation Adapter

The repository orientation adapter owns source/package reader modes. It
separates explanatory reader orientation from hard package/release gates.

It should define:

- source clone behavior: source-relative links and source file paths;
- generated zip behavior: package-local links under a zip root;
- installed skill behavior: entrypoint and package-local support assets after
  unzip/install;
- CCDP-adjacent behavior: CCDP remains a separate protocol distribution;
- release-surface expectations: README, `SKILL.md`, Makefile, package list,
  generated zip behavior, and validation command coverage.

Each component should carry a short local source/package note and rely on the
central adapter for the full explanation.

## Support Asset Travel

| CAW Row | Support Asset Travel | Owning Component | Package Behavior |
|---------|----------------------|------------------|------------------|
| CAW-13 | `CONTRIBUTION-TICKET.md` travels with contribution guidance. | `contribution-style-and-voice`. | Package as a local template/support asset with resolving links. |
| CAW-14 | PM examples travel with the PM family. | `project-management`. | Package only if PM examples are accepted as family support. |
| CAW-15 | PM provenance and version history notes travel as PM and maintenance support. | `project-management` plus maintenance fields. | Keep version-history responsibility visible in source and package modes. |
| CAW-16 | Planning anti-patterns and repair guidance travel through the PM wayfinder. | `project-management`. | Package as PM support, not a direct-load component. |
| CAW-17 | Audit output examples travel with audit after adjustment. | `code-audit-discipline`. | Examples must use slice `artifacts/` for durable planning outputs or an explicit non-slice output home. |
| CAW-18 | Protocol distribution guidance travels as repository orientation / release-gate support. | Repository orientation and release gate owner. | Preserve CCDP separation; do not package CCDP inside a skill component. |

## Non-Component And Deferred Row Placement

These rows are not discarded. They retain owner, citation edge, and re-entry
condition.

| Row | Placement | Owner | Citation Edge | Re-entry Condition |
|-----|-----------|-------|---------------|--------------------|
| CAW-23 verification-methodology | Dependency edge / non-component; not standalone. | Ledger/methodology relationship. | Ledger owns evidence semantics; methodology cites process relation; PM close, audit, and coverage cite ledger as needed. | Reopen only if operator or later evidence proves direct-load workflow beyond ledger/methodology ownership. |
| CAW-24 ontology critique | Deferred question / non-component. | Project02 architecture method; possible Project03 or future component owner. | Architecture method cites it as a boundary-checking concern. | Reopen if operator requests a reusable abstraction-boundary method or Project03 produces component-ready method evidence. |
| CAW-25 component-maintenance discipline | Constraint and package/release gate; standalone component deferred. | Release gate owner plus every component owner. | Every component contract cites maintenance owner, source path, package path, support assets, version history responsibility, and release gates. | Reopen standalone status only if maintenance becomes a recurring direct-load workflow. |
| CAW-26 evidence strength and memory admission vocabulary | Non-component / dependency edge; not standalone. | Ledger/methodology relationship; possible future memory/evidence owner. | Ledger owns evidence strength; methodology owns broader process relation; memory admission remains cited vocabulary. | Reopen only in a future memory protocol or evidence ontology effort with direct-load evidence. |

## Local Note Requirements

Every accepted standalone component should include:

- a one-paragraph role-language note from the agent adapter;
- a one-paragraph source/package note from repository orientation;
- a dependency edge list naming required components and support assets;
- a package-local link checklist;
- owner and version-history responsibility from component-maintenance fields.

These notes are small enough to preserve standalone readability and specific
enough to avoid central-only ambiguity.
