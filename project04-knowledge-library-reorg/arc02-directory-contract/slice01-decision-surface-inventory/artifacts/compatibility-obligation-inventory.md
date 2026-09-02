# Compatibility Obligation Inventory

```yaml
project: project04-knowledge-library-reorg
arc: arc02-directory-contract
slice: slice01-decision-surface-inventory
artifact: compatibility-obligation-inventory
artifact-status: compatibility inventory
created-on: 2026-09-02
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
source-files-edited: false
```

## Purpose

This inventory records compatibility obligations Arc02 must preserve when it
later selects a directory contract and migration plan. It covers validation
commands, package/list surfaces, links, wrappers, compatibility files, package
exceptions, and re-entry conditions. It is not source-edit authorization.

## Validation Command Obligations

| Command | Required when | Obligation |
|---------|---------------|------------|
| `make check-skills` | Any `SKILL.md`, `SKILL*.md`, frontmatter, description, source root, or `ALL_SKILL_FILES` change. | Ensure every live or newly planned skill entrypoint is in the validation surface. |
| `make check-package-paths` | Any generated skill package, package-local link, `package-path-exceptions.tsv`, README route, or package root changes. | Verify generated packages, not only source paths. |
| `make all` | Aggregate package target, generated zip behavior, or `INSTALL_ZIPS` changes. | Confirm full skill package build after root/list changes. |
| `make collab-framework` | Composer source, `CF_FILES`, framework component package behavior, or composer package payload changes. | Preserve `collaboration-framework` daily-driver composer behavior. |
| `make ccdp-package` | CCDP source or package payload changes. | Build protocol package separately from skill packages. |
| `make check-ccdp-package` | CCDP paths, README links, package contents, assembler output, or source-only exclusions change. | Preserve CCDP package separation and package-local protocol links. |
| `git -C /Users/oubiwann/lab/billosys/ai-engineering diff --check` | Every source-edit slice. | Catch whitespace and patch hygiene errors before commit. |
| `git -C /Users/oubiwann/lab/billosys/ai-engineering status --short` | Every planning and source-edit slice. | Confirm source checkout remains untouched unless explicitly authorized. |

## Package And List Surfaces

| Surface | Compatibility obligation | Re-entry condition |
|---------|--------------------------|--------------------|
| `Makefile` | Keep `CF_FILES`, `ALL_SKILL_FILES`, `INSTALL_ZIPS`, skill package targets, component targets, `make collab-framework`, `make check-skills`, `make check-package-paths`, `make all`, and CCDP targets synchronized with accepted roots. | Re-enter migration plan if accepted roots cannot be represented without weakening validation. |
| `CF_FILES` | Keep composer payload explicit and package-local after framework moves. | Re-enter Project02 composer packaging if composer-only payload cannot preserve daily-driver route. |
| `ALL_SKILL_FILES` | Include every current and accepted new `SKILL.md` or `SKILL*.md`. | Re-enter if source roots are accepted but entrypoints cannot be validated by the current checker. |
| `INSTALL_ZIPS` | Include installable skill zips only. Do not include `ccdp.zip` unless protocol policy changes. | Re-enter CCDP policy if protocol packages must become installable skills. |
| Generated skill zips | Treat generated package roots as authoritative package evidence. | Re-enter package-root decisions if generated roots contradict the accepted source-root rule. |
| `package-path-exceptions.tsv` | Use narrow, reasoned, preferably expiring exceptions for intentional source-only, provenance, external URL, example-project, or checker false-positive cases. | Re-enter exception policy if broad exceptions are needed to pass. |

## Link And Wayfinding Obligations

| Surface | Link responsibility | Wrapper or migration-note need |
|---------|---------------------|--------------------------------|
| `README.md` | Orient users to source checkout, generated zip, unzipped/install, installed skill routes, focused docs, skill library, and CCDP protocol distribution. | Needs migration notes when old top-level or `docs/` source paths move. |
| `docs/` | Explain repository materials, packages, methods, protocols, and knowledge-library anatomy without becoming the substrate by default. | Needs wrapper pages where old public routes point to moved source material. |
| `SKILL.md` | Route load behavior, preserve `collaboration-framework` composer role, and use installed-skill route wording across package roots. | Needs top-level compatibility shim decision if the current entrypoint moves. |
| `AGENTS.md` | Preserve planning/source checkout distinction, validation commands, package paths, skill-loading instructions, CCDP paths, and commit trailer convention. | Needs update whenever accepted paths or validation commands change. |
| `CLAUDE.md` | Preserve symlink compatibility intent with `AGENTS.md`. | Needs explicit decision before replacing symlink behavior. |
| Package-local links | Prefer package-local relative links within generated packages. | Needs repair before package-path exceptions are added. |
| Installed-skill routes | Use route wording across package boundaries instead of brittle relative links. | Needs README and `SKILL.md` wording after package roots are stable. |

## Authority And Boundary Obligations

- accepted fact: `collaboration-framework` remains the daily-driver composer;
  CCDP remains a separate protocol distribution; Arc01 has delivered the
  source-backed inventory and classification base.
- working hypothesis: Project02 top-level component roots and package target
  details remain hypotheses until Arc02 accepts, adjusts, or rejects them.
- operator decision required: root placement, top-level compatibility shim,
  template cross-cutting exceptions, accepted package warnings, and any CCDP
  policy change.
- planned surface: Project02 components and Project03 `concept-card-method`
  are not live source until implementation lands.
- not live source: `concept-card-method` and specialist Project02 component
  roots should not be described as current packages.
- source-edit risk: every listed validation or compatibility obligation
  constrains future source edits but does not authorize them.
- source-files-edited: false for this slice.

## Kind And Topology Obligations

Arc02 must preserve skill kind and topology as independent axes:

- skill kind: domain/tooling, framework/operational, method,
  protocol/package, support/template, source/provenance;
- topology: atomic, composite, bridge/integration, application/task bundle.

Validation surfaces such as `Makefile`, `package-path-exceptions.tsv`,
`AGENTS.md`, and `CLAUDE.md` are compatibility surfaces, not skill kinds.
CCDP is a protocol/package bridge, not an installable skill package. Templates
are support surfaces unless accepted entrypoint and package behavior make them
loadable.

## Re-Entry Conditions

- Re-enter Project02 if no directory contract can preserve accepted component
  roles, composer behavior, component version histories, source/package/release
  gate ownership, and CCDP separation.
- Re-enter Project03 if the accepted contract cannot preserve
  `concept-card-method` as planned method skill input without claiming live
  source.
- Re-enter CCDP policy only with explicit protocol package decision evidence.
- Re-enter kind/topology classification if accepted source roots, package
  roots, entrypoint shape, generated package behavior, or validation behavior
  changes load reason or composition identity.
- Re-enter migration sequencing if package-local links cannot be repaired
  before exception rows are needed.

## Implementation-Gate Inventory

Later implementation slices should declare the touched surfaces and then select
the relevant gates from this inventory. At minimum:

- source layout moves require source status, diff check, source-prose
  preservation review, README/docs route review, and package-path impact
  review;
- `SKILL.md` moves or additions require `make check-skills` and package-local
  link review;
- package target/list changes require generated package inspection,
  `make check-package-paths`, and `make all`;
- composer changes require `make collab-framework`;
- CCDP changes require `make ccdp-package` and `make check-ccdp-package`;
- package-path exception changes require a reason, classification, source, and
  expiration or explicit no-expiration rationale.
