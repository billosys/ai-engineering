# Package And Release Gate Dispositions

```yaml
project: project02-collab-breakout
arc: arc04-breakout-architecture
slice: slice02-component-contract-evaluation
status: proposed-done
gate-status: evaluated-contract-inputs
architecture-decisions: none
```

## Input Contract

This artifact makes Project01 and `project01-harmonise-paths` source/package
constraints concrete at the component-contract evaluation layer. It consumes
the verified Slice01 architecture decision instrument, closed Arc02
package/release gate findings, closed Arc03 source/package risk findings, and
read-only source grounding in `README.md`, `SKILL.md`, `Makefile`,
`package-path-exceptions.tsv`, `docs/PROJECT-MANAGEMENT.md`, `docs/pm/*.md`,
`templates/LEDGER-DISCIPLINE.md`, and CCDP package guidance.

The dispositions below are package/release gate inputs for Slice03. They do
not accept final package paths or source moves.

## Gate Set

| Gate | Disposition | Contract Requirement | Evidence / Source Grounding |
|------|-------------|----------------------|-----------------------------|
| Project01 path-contract constraints | go as package/release gate. | Every accepted component contract must distinguish source path from package path and mark package paths non-final until operator acceptance. | Slice01 `component-contract schema`; Arc02 BNF-14; Arc03 FR-08/FR-10; Project01 carry-forward. |
| Source/package modes | go as contract requirement and adapter. | Each component must describe source clone, generated skill zip, unzipped installed skill, and any nearby CCDP package reading mode. | README building/installing section; Arc03 functional model; `CAW-20`. |
| Package-local links | go as gate. | Links inside generated or installed packages must resolve without source checkout assumptions. | `make check-package-paths`; Project01 path contract; `CAW-19`/`CAW-21`. |
| Zip root | go as gate. | Skill zips use a component-named root; the current composer uses `collaboration-framework/`; CCDP uses separate `ccdp/` root. | Makefile `CF_NAME`, `pack_skill`, `CCDP_NAME`; README package-use section. |
| Release surface synchronization | go as gate. | README, top-level `SKILL.md`, component `SKILL.md`, source docs, support assets, package lists, exceptions, and generated zip behavior must change together. | `CAW-21`; source Makefile lists `CF_FILES`, `INSTALL_ZIPS`, `ALL_SKILL_FILES`. |
| README wayfinding | go as release surface. | README must explain individual component use, composed framework use, and CCDP distinction after breakout. | README collaboration-framework, skill library, building/installing, and CCDP sections. |
| `SKILL.md` wayfinding | go as release surface. | The top-level composer `SKILL.md` must remain usable as `/collaboration-framework` and route to new components without retaining full monolith detail. | `SKILL.md`; Slice01 decision method; Arc03 S-13. |
| Makefile/package lists | go as package/release gate. | New or renamed components require Makefile targets/lists and generated zip expectations in the same implementation slice. | Makefile `CF_FILES`, `INSTALL_ZIPS`, `ALL_SKILL_FILES`, package targets. |
| CCDP separation | go as package/release gate. | CCDP remains a protocol distribution, not an installable skill bundle or collaboration-framework component. | README CCDP section; Makefile `ccdp-package`, `check-ccdp-package`; `CAW-22`. |
| Validation commands | go as gate. | Arc05 implementation slices must run relevant Make targets, including `make check-skills` for metadata/entrypoint changes and `make check-package-paths` after packaged Markdown link, bundle content, Makefile list, or exception changes. | AGENTS instructions, Makefile targets, Slice01 schema, Project01 gates. |

## Per-Contract Package Fields

Each accepted component or component family must include these fields before
Slice04 operator acceptance:

- source paths: current source evidence and likely implementation inputs.
- package paths: proposed package location, marked non-final before
  acceptance.
- package-local links: links that must resolve inside the generated package.
- zip root assumptions: component root and entrypoint behavior.
- README updates: source-clone, packaged-skill, and composed-framework route.
- `SKILL.md` entrypoints: top-level composer route and component entrypoint.
- Makefile/package list changes: targets, install lists, and packaged file
  lists.
- package-path exceptions: any accepted warning or exception must be explicit.
- CCDP separation: component contract states whether CCDP is irrelevant,
  cited, or adjacent but never bundled into a skill package.
- release gates and validation commands: `make check-skills`,
  `make check-package-paths`, package build target, and any component-specific
  check.
- component contract maintenance owner and version history responsibility.

## Component-Specific Gate Notes

| Candidate | Gate Disposition |
|-----------|------------------|
| `collaborative-posture-and-ethics` | If standalone, needs package-local links to methodology and contribution guidance; composer keeps compact summary. |
| `engineering-methodology-and-process` | Router contract must keep package-local links to PM, ledger, audit, coverage, delegation, contribution, and domain-skill routes. |
| `ledger-verification-protocol` | PM close guides depend on ledger evidence semantics; package-local links must work from both directions. |
| `project-management` | PM family requires internal guide links, artifact-home guidance, ledger dependency, and PM version-history route. |
| `code-audit-discipline` | Audit output conventions must distinguish ignored workbench drafts from durable slice `artifacts/`; examples must travel if cited. |
| `coverage-hardening-discipline` | Naming/alias decision affects package root, README route, and compatibility with historical `CLAUDE-CODE-COVERAGE.md`. |
| `delegation-policy` | Low package complexity; must retain role-language adapter link and standalone trigger. |
| `contribution-style-and-voice` | `CONTRIBUTION-TICKET.md` must package as support asset with package-local links. |
| top-level composer | Current `collaboration-framework.zip` remains the broad entrypoint until operator accepts a new composition; route table and compact floor are release-surface changes. |
| agent adapter | Central plus local notes require a drift-control check; every standalone package with role labels must link or embed the note. |
| repository orientation | Contract must route source clone and package readers without merging hard gate semantics into prose-only guidance. |
| PM wayfinder | Package-local links to PM internal guides and ledger must be checked. |

## CCDP Separation

The repository contains both installable skill bundles and the Composite
Cognition Dispatch Protocol. Source grounding shows:

- skill bundles are built by `make all`, `make skills`, and
  `make collab-framework`;
- installed skills use generated skill zips or unzipped package roots;
- CCDP is built separately with `make ccdp-package` and validated by
  `make check-ccdp-package`;
- README directs source readers to `protocols/ccdp/README.md` and package
  readers to `ccdp/README.md`.

Therefore `CAW-22` is go as a gate: any collaboration-framework component
contract that cites CCDP must state that CCDP is adjacent protocol
distribution material, not part of the installable skill component package.

## Slice03 Package Architecture Input

Slice03 should compose a target package strategy that includes:

- a thin `collaboration-framework` composer package;
- direct-load component packages only where the Slice02 contract status is go
  or adjust with clear re-entry;
- a PM family package strategy rather than unreviewed PM guide packages;
- explicit support-asset travel for templates and examples;
- central release gates plus per-component package fields;
- source/package reader-mode adapter behavior;
- validation commands anchored in Makefile targets and `make
  check-package-paths`.

This artifact is non-final. Operator acceptance remains required before Arc04
can close and before Arc05 can plan source/package implementation.
