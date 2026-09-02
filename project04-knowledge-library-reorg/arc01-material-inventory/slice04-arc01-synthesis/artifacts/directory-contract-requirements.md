# Directory Contract Requirements

```yaml
project: project04-knowledge-library-reorg
arc: arc01-material-inventory
slice: slice04-arc01-synthesis
artifact: directory-contract-requirements
artifact-status: slice synthesis evidence
created-on: 2026-09-02
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
source-files-edited: false
```

## Purpose

This artifact turns Arc01 evidence into requirements for Arc02's target
directory contract and migration plan. It does not choose the final layout and
does not authorize source edits.

## Contract-Level Requirements

| Area | Requirement | Evidence source | Arc02 output needed |
|------|-------------|-----------------|---------------------|
| `docs/` | Define `docs/` as user-facing documentation about repository materials, packages, methods, protocols, and the knowledge library. Do not leave source-like framework or method substrate in `docs/` without an explicit exception or wrapper policy. | Slice01 `material-role-classification.md`; Project04 plan. | A move/remain/wrapper table for every current `docs/` family. |
| `knowledge/` | Define whether `knowledge/` is the common source root for raw and derived knowledge-library substrate across domain/tooling, framework/operational, and method skill material. | Slice01 `current-source-surface-map.md`; Slice02 conflicts/questions; Slice03 classification matrix. | A source-root rule that covers current domain/tooling skills and planned framework/method surfaces. |
| Framework/operational components | Preserve Project02 accepted components and composer behavior while deciding whether component source roots live under `knowledge/`, at top level, under a framework family root, or through wrappers. | `operator-accepted-architecture.md`; Slice02 evidence map. | A component source root and package root contract for `collaboration-framework`, `engineering-methods`, `project-management`, `work-verification`, `testing`, `code-auditing`, `agent-coordination`, and `contribution-style`. |
| Method skill surfaces | Preserve planned `concept-card-method` as planned method skill input, not live source. Decide whether method skills live under `knowledge/` and whether thin `SKILL.md` plus focused `guides/` is the method-skill convention. | Project03 evidence summarized by Slice02; Slice03 matrix. | A planned-method source root rule and current/planned language rule. |
| `protocols/ccdp/` | Keep CCDP as a separate protocol/package surface with separate package validation unless a later protocol package decision reopens that policy. | Slice01 validation map; Slice02 accepted facts; Slice03 public-language implications. | A protocol contract for `protocols/ccdp/`, `ccdp.zip`, README links, and CCDP validation commands. |
| `templates/` | Decide which templates remain top-level cross-cutting support and which move under owning component, method, skill, or protocol roots. | Slice01 material roles; Slice03 template/support rows. | A template ownership table covering `templates/GUIDE.md`, `templates/LEDGER-DISCIPLINE.md`, and `templates/CONTRIBUTION-TICKET.md`. |
| `README` | Keep README as concise orientation and reader-mode wayfinding, not the complete source substrate. | Project04 plan; Project02 README wayfinding plan; Slice03 public-language implications. | A README responsibility boundary and handoff list to focused `docs/` pages. |
| `SKILL.md` | Preserve `collaboration-framework` daily-driver composer behavior and avoid cross-package brittle links. Decide top-level compatibility behavior before moving or replacing the current entrypoint. | Slice01 source map; Project02 skill-entrypoint validation plan. | A source checkout and installed-skill route policy for the current and future composer entrypoints. |
| Source root | State the source root rule separately from package root naming. Current `knowledge/*` source roots, top-level `SKILL.md`, and selected-file framework packaging do not all share one shape. | Slice01 validation map; Slice03 matrix. | A source-root rule for atomic, composite, bridge/integration, method, and support surfaces. |
| Package root | State whether generated package roots match source roots, frontmatter `name:`, component names, or selected-file package names. | Slice01 Makefile map; Project02 package target plan. | A package-root contract plus examples for domain/tooling skills, framework components, and Biome-style multiple entrypoints. |
| Package-local links | Prefer package-local links inside generated packages and installed-skill route wording across package roots. | Project02 package path/link exception plan; Slice01 validation map. | A link policy and migration gate before exception rows are added. |
| `Makefile` | Keep Makefile targets and lists synchronized with accepted roots: `CF_FILES`, `ALL_SKILL_FILES`, `INSTALL_ZIPS`, component package targets, `make collab-framework`, `make check-skills`, `make check-package-paths`, `make all`, and CCDP targets. | Slice01 source-validation-surface-map.md; Project02 package target plan. | A Makefile update matrix for every accepted source/package move. |
| `package-path-exceptions.tsv` | Use narrow package-path exceptions only for intentional source-only, provenance, external URL, example-project, or checker false-positive cases. | Slice01 validation map; Project02 package-path exception plan. | An exception policy with allowed classes, reasons, and expiration expectations. |
| `AGENTS.md` | Preserve source/planning checkout distinction, validation commands, domain skill routes, CCDP paths, and commit trailer rules as compatibility instructions change. | Slice01 validation map; repository instructions. | A compatibility update checklist for operator and assistant instructions. |
| `CLAUDE.md` | Preserve symlink compatibility intent. Do not replace a symlink with a copied file without an explicit compatibility decision. | Slice01 source map and CDC check. | A symlink preservation or migration rule. |

## Skill Kind and Topology Requirements

- The directory contract must record skill kind and topology as independent
  axes. It should not collapse domain/tooling into atomic or
  framework/operational into composite.
- Atomic source-root requirements should be based on one bounded load reason,
  entrypoint behavior, package behavior, and validation behavior.
- Composite source-root requirements should be based on identity-defining
  composition, routing, sequencing, or governing of multiple components.
- Bridge/integration layer requirements should cover protocol and connector
  surfaces without forcing them into skill package behavior.
- Application/task bundle requirements should permit workflow-specific
  arrangements without treating every recipe as a reusable method skill.
- The external ontology rubric remains tested input, not accepted taxonomy;
  public category language belongs to Arc05 after Arc02 settles the contract.

## Surface-Specific Migration Requirements

| Surface group | Move/remain/wrapper questions | Preservation requirements | Validation obligations |
|---------------|-------------------------------|---------------------------|------------------------|
| Current framework docs under `docs/` | Move into framework/operational component roots, remain as source docs, or become user-facing wrappers. | Preserve source prose, version history, Project02 component ownership, and package-local links. | `make collab-framework`, `make check-skills`, `make check-package-paths`, README/docs link checks. |
| Current `docs/dev/` extraction guidance | Move under method or knowledge substrate roots, keep as design/dev provenance, or expose through wrapper docs. | Preserve extraction provenance and avoid calling historical guidance current public docs unless updated. | Source path/link scan; future method-skill validation if packaged. |
| Current `knowledge/*` domain/tooling skills | Mostly remain source-backed skill substrate unless Arc02 identifies a specific contract problem. | Preserve `SKILL*.md`, guides, concept cards, sources, extraction metadata, tools, workbench boundaries, generated package roots, and frontmatter names. | `make check-skills`, per-package target, `make check-package-paths`, package exception review. |
| Planned Project02 components | Choose Project04-compatible source roots before implementation. | Preserve all accepted component names, daily-driver composer role, sibling `version-history.md`, and source/package/release gate ownership. | New entrypoint checks, generated component packages, aggregate package checks, source history review. |
| Planned Project03 `concept-card-method` | Decide whether `knowledge/concept-card-method/` remains the method skill source root. | Preserve planned status, thin entrypoint, focused guides, validation distinction, memory admission as lifecycle gate, and CCDP-adjacent boundary. | Future method package target, `make check-skills`, `make check-package-paths`, semantic/human validation gates where accepted. |
| `knowledge/biome/` | Decide whether one source root may own multiple package entrypoints. | Preserve current `biome-js-linter` and `biome-linter` package behavior or explicitly migrate both. | Both package checks, `ALL_SKILL_FILES`, generated root inspection, package-path exceptions. |
| `templates/` | Keep top-level, move under owners, or keep wrappers from top-level. | Preserve template provenance and owning component/method/package payload expectations. | Package-local link checks and `CF_FILES` or component payload checks. |
| `protocols/ccdp/` | Keep current root, add docs wrapper, cross-link from methods, or reopen package policy. | Preserve CCDP package separation, `ccdp.zip`, source-only exclusions, and protocol assembler behavior. | `make ccdp-package`, `make check-ccdp-package`, root README links, static site references when touched. |

## Required Arc02 Registers

Arc02 should open with these registers or equivalent sections:

- source-root register: current path, proposed target, kind, topology,
  authority level, source/provenance handling, and re-entry condition;
- package-root register: generated zip, package root, entrypoint, Makefile
  target, install behavior, and package-local link obligations;
- compatibility register: README, `SKILL.md`, `AGENTS.md`, `CLAUDE.md`,
  package-path exceptions, old source paths, wrapper docs, and migration notes;
- validation matrix: required source-checkout commands by touched surface;
- public-language deferral register: terms Arc05 may use only after source and
  package evidence exists.

## Minimum Later Validation Gate

Any later implementation slice that changes source layout, package roots, or
public routes must state which of these commands are mandatory and why:

- `git -C /Users/oubiwann/lab/billosys/ai-engineering diff --check`
- `git -C /Users/oubiwann/lab/billosys/ai-engineering status --short`
- `make check-skills`
- `make check-package-paths`
- `make all`
- `make collab-framework`
- `make ccdp-package`
- `make check-ccdp-package`

Generated package validation is stronger evidence than source-only link scans
for package behavior. Source-only planning artifacts are not enough to close
implementation rows.
