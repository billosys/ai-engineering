# Package And Release Architecture

```yaml
project: project02-collab-breakout
arc: arc04-breakout-architecture
slice: slice03-target-composition-package-architecture
status: proposed-done
artifact-status: proposed-package-architecture-input
operator-acceptance: pending
source-files-edited: false
```

## Input Contract

This artifact consumes the verified Slice01 component-contract schema and the
verified Slice02 package/release gate dispositions. It composes Project01 and
`project01-harmonise-paths` source/package constraints before proposing any
package path. Source grounding comes from read-only inspection of `README.md`,
`SKILL.md`, `Makefile`, current collaboration-framework source documents,
templates, and CCDP package guidance.

All package paths in this artifact are a non-final package path proposal.
Slice04 operator acceptance is required before Arc05 can plan source edits,
README updates, `SKILL.md` entrypoints, packaging changes, validation gates,
migration notes, or review concerns.

## Gate-First Package Rule

Every accepted component, component family, support asset, adapter, and
composer must satisfy these package/release gate rows before package paths are
implemented:

| Gate Row | Contract Effect |
|----------|-----------------|
| `CAW-19` Project01 path-contract constraints | State source path, package path, package-local links, zip root, release surface, README route, `SKILL.md` route, Makefile package list impact, and validation command. |
| `CAW-20` source/package reader modes | Explain source clone, generated zip, installed skill, and CCDP-adjacent reader modes. |
| `CAW-21` release surface synchronization | Keep README, `SKILL.md`, component entrypoints, Makefile package list entries, generated zip behavior, exceptions, and validation together. |
| `CAW-22` CCDP separation | Keep CCDP as separate protocol distribution and `ccdp.zip`, not a collaboration-framework skill package. |
| `CAW-25` component-maintenance discipline | Name maintenance owner and version-history responsibility for every accepted component contract. |

## Current Source And Package Surface

Read-only source grounding shows:

- `README.md` documents the current `collaboration-framework` use surface, the
  broader skill library, build/install commands, and CCDP package distinction.
- Top-level `SKILL.md` is the current collaboration-framework entrypoint.
- `Makefile` packages `collaboration-framework.zip` from `CF_FILES` and
  package-root `collaboration-framework/`.
- `Makefile` lists installed skill zips in `INSTALL_ZIPS`, validates skill
  descriptions with `make check-skills`, validates generated skill package
  Markdown paths with `make check-package-paths`, and separately packages CCDP
  with `make ccdp-package` and `make check-ccdp-package`.
- `templates/CONTRIBUTION-TICKET.md` and `templates/LEDGER-DISCIPLINE.md`
  are support assets in the current source layout.
- Package-local behavior matters because generated zip roots differ from
  source checkout paths.

## Proposed Package Roots

The table below is proposed architecture only. It does not finalise source
moves or Makefile targets.

| Package Root | Proposed Entry Surface | Classification | Source Path Assumptions | Package-Local Link Behavior |
|--------------|------------------------|----------------|-------------------------|-----------------------------|
| `collaboration-framework/` | Top-level composer `SKILL.md` with compact safety floor and route table. | Composer package. | Current source starts at top-level `SKILL.md`, `README.md`, `docs/`, and `templates/`. | Links route to component packages or embedded composer guides according to accepted release shape. |
| `collaborative-posture-and-ethics/` | Component `SKILL.md` plus posture guide. | Direct-load component plus dependency edge. | Current source in `docs/AI-CONSTITUTION-SUPPLEMENT.md` and composer summary. | Links to methodology and contribution remain package-local or explicitly cross-package. |
| `engineering-methodology-and-process/` | Component `SKILL.md` plus process guide and route table. | Direct-load component / router. | Current source in `docs/AI-ENGINEERING-METHODOLOGY.md` and current composer. | Links route to PM, ledger, audit, coverage, delegation-policy, contribution-style, and domain skills. |
| `ledger-verification-protocol/` | Component `SKILL.md` plus ledger discipline guide/template. | Direct-load component. | Current source in `templates/LEDGER-DISCIPLINE.md` and PM close docs. | PM package links to ledger; ledger links back to PM lifecycle without source-only assumptions. |
| `project-management/` | PM family `SKILL.md` / PM wayfinder plus internal guides. | Component family. | Current source in `docs/PROJECT-MANAGEMENT.md`, `docs/pm/*.md`, and ledger template references. | Internal guide links and ledger links must resolve under package root or accepted cross-package form. |
| `code-audit-discipline/` | Component `SKILL.md` plus audit guide and examples. | Direct-load component. | Current source in `docs/CODE-AUDIT.md`; examples may need output-home update. | Domain skill routes and audit output examples must be package-local where shipped. |
| `coverage-hardening-discipline/` | Component `SKILL.md` plus coverage hardening guide. | Direct-load component with compatibility treatment. | Current source in `docs/CLAUDE-CODE-COVERAGE.md`. | Compatibility alias or note must make source/package route clear. |
| `delegation-policy/` | Component `SKILL.md` plus delegation guide. | Direct-load component. | Current source in `docs/SUBAGENT-DELEGATION-POLICY.md`. | Role-language adapter note must resolve locally or through accepted central adapter route. |
| `contribution-style-and-voice/` | Component `SKILL.md` plus contribution guide and template. | Direct-load component with support asset. | Current source in `docs/CONTRIBUTION-STYLE.md` and `templates/CONTRIBUTION-TICKET.md`. | Template link must resolve inside the package root. |

No standalone package root is proposed for `agent-adapter-and-routing`,
`repository-orientation-and-distribution`, `project-management-wayfinder`,
verification-methodology, ontology critique, component-maintenance discipline,
or evidence strength/memory admission vocabulary in Slice03. Those rows remain
adapter, constraint, package/release gate, dependency edge, non-component, or
deferred question rows unless Slice04 accepts a different shape.

## README, SKILL.md, And Makefile Surface Changes

Arc05 implementation planning should prepare these source/package release
surface changes after Slice04 acceptance:

| Surface | Required Change Type |
|---------|----------------------|
| `README.md` | Add routes for individual component use, composed framework use, generated zip use, installed skill use, PM family use, and CCDP separation. |
| Top-level `SKILL.md` | Convert the composer into a compact safety floor and route table while preserving `/collaboration-framework` usability. |
| Component `SKILL.md` entrypoints | Add frontmatter, trigger/scope descriptions, local adapter notes, dependency edges, support assets, package paths, maintenance owner, and version history responsibility. |
| `Makefile` `INSTALL_ZIPS` | Add accepted component zip names in one package list change. |
| `Makefile` `ALL_SKILL_FILES` | Add every accepted component `SKILL.md` so `make check-skills` validates descriptions. |
| `Makefile` package targets | Add or factor package build targets for accepted component roots; preserve current generated zip behavior. |
| `Makefile` `CF_FILES` | Reduce or recompose the composer package file list according to the accepted route design. |
| `package-path-exceptions.tsv` | Add only explicit, justified exceptions; prefer package-local link repair. |
| Release notes or generated zip expectations | State changed package names, zip root assumptions, and migration path from current `collaboration-framework.zip`. |

## CCDP Separation

CCDP separation is a hard package/release gate:

- CCDP source remains under `protocols/ccdp/`.
- CCDP package use starts at `ccdp/README.md` inside `ccdp.zip`.
- CCDP validation uses `make ccdp-package` and `make check-ccdp-package`.
- Collaboration-framework packages may cite CCDP as adjacent protocol
  distribution material, but they must not bundle CCDP source or present CCDP
  as an installable skill component.

This keeps protocol distribution guidance (`CAW-18`) as support/constraint
language owned by repository orientation and release gates.

## Validation Commands

Arc05 implementation slices should map each accepted source edit to a
validation command:

| Change Type | Validation Command |
|-------------|--------------------|
| Any `SKILL.md` frontmatter or description update | `make check-skills` |
| Packaged Markdown links, bundle contents, Makefile package list changes, or path exceptions | `make check-package-paths` |
| Composer package behavior | `make collab-framework` plus `make check-package-paths` |
| Full skill release surface | `make all` plus `make check-package-paths` |
| CCDP package changes, if ever separately touched | `make ccdp-package` and `make check-ccdp-package` |

The Slice03 packet does not run these commands because no source files,
generated zip artifacts, README, `SKILL.md`, Makefile, package list, or CCDP
files are edited in this planning slice.

## Release Architecture Risks

| Risk | Proposed Disposition |
|------|----------------------|
| Source/package drift | Make `CAW-19` and `CAW-20` mandatory fields in every accepted contract before Arc05 source work. |
| Broken package-local links | Require `make check-package-paths` after package list or Markdown link edits. |
| Release surface mismatch | Treat README, `SKILL.md`, Makefile, generated zip behavior, package-path exceptions, and version history as one release surface. |
| CCDP confusion | Keep CCDP separation explicit in README, package docs, and validation command selection. |
| Premature final paths | Mark every package path non-final until Slice04 operator acceptance. |
| Component-maintenance drift | Require owner and version-history fields for every accepted component and support asset. |
