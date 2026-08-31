# Package Source Contract Register

```yaml
project: project02-collab-breakout
arc: arc05-implementation-plan
slice: slice02-component-contract-file-plan
status: proposed-done
artifact-status: package source contract register
source-files-edited: false
```

## Grounding

This register turns the verified Slice01 implementation surface and accepted
architecture into package/source contract fields. It is a Slice02 input to
Slice03. Package targets, README text, Makefile edits, generated zip contents,
and package-path exception rows are not final here.

## Register Rules

- `engineering-methods` owns the shared source/package/release gates.
- Every accepted component owns its local source path and package/source
  contract.
- Every accepted component must be validated through its `SKILL.md` description
  and package-local Markdown links once Slice03 defines the release surface.
- Component versioning contract is always `SKILL.md` version plus sibling
  `version-history.md`.

## Component Package/Source Contract Register

| Component | source path | package root | package-local link | installed skill | README route | SKILL route | Makefile impact | generated zip | validation command | owner | versioning contract | Slice03 / not final note |
|-----------|-------------|--------------|--------------------|-----------------|--------------|-------------|-----------------|---------------|--------------------|-------|---------------------|--------------------------|
| `collaboration-framework` | `collaboration-framework/` target source root, with compatibility migration from top-level `SKILL.md` and current docs. | `collaboration-framework/` package root is already the accepted composer root. | Links from composer `SKILL.md` should be package-local to `guides/` and component route table; links to other packages need explicit README/installed-skill wording. | Existing `/collaboration-framework` use path remains. | README should describe composer use plus route to individual components. | Composer `SKILL.md` should route to specialist component skill names without bundling their full bodies. | Existing `CF_FILES` must shrink or become composer-specific after Slice03 plan. | Existing `collaboration-framework.zip` remains, contents not final. | `make collab-framework`, `make check-skills`, `make check-package-paths`. | `collaboration-framework`, with gates defined by `engineering-methods`. | `SKILL.md` version plus sibling `version-history.md`; exact version bump is not final. |
| `engineering-methods` | `engineering-methods/`. | Likely `engineering-methods/`, pending Slice03 package naming confirmation. | Links stay package-local across methodology, substrate, process, routing, component-boundary-analysis, and source/package/release gates guides. | New installed skill route likely `/engineering-methods`, not final until Slice03. | README should present this as the process/gate component. | `engineering-methods/SKILL.md` routes to numbered guides and other components. | Add to skill file validation and package build lists if packaged standalone. | Likely new `engineering-methods.zip`, not final. | `make check-skills`, `make check-package-paths`; release gate text owns when to run `make all`. | `engineering-methods`. | `SKILL.md` version plus sibling `version-history.md`; seeds from methodology history. |
| `project-management` | `project-management/`. | Likely `project-management/`, pending Slice03. | PM guide links should be package-local under `guides/` and `examples/`; ledger links route to `work-verification` package/skill where needed. | New installed skill route likely `/project-management`. | README should distinguish lifecycle planning from the composed framework. | `project-management/SKILL.md` is the PM wayfinder and required-load router. | Add PM component to package build and validation lists if standalone. | Likely new `project-management.zip`, not final. | `make check-skills`, `make check-package-paths`. | `project-management`. | `SKILL.md` version plus sibling `version-history.md`; reconcile `docs/pm/version-history.md`. |
| `work-verification` | `work-verification/`. | Likely `work-verification/`, pending Slice03. | Guide links and `templates/LEDGER-DISCIPLINE.md` references must resolve inside package root; cross-component links should use README/install wording rather than fragile relative paths. | New installed skill route likely `/work-verification`. | README should present ledger/evidence/independent verification as a standalone load point. | `work-verification/SKILL.md` routes to evidence, row closure, silent-drop, and independent verification guides. | Add package target/list row and skill validation if standalone. | Likely new `work-verification.zip`, not final. | `make check-skills`, `make check-package-paths`. | `work-verification`. | `SKILL.md` version plus sibling `version-history.md`; seed from ledger discipline history. |
| `testing` | `testing/`. | Likely `testing/`, pending Slice03. | Coverage and validation guide links stay package-local; domain-specific testing links should route to source README or installed domain skills. | New installed skill route likely `/testing`. | README should explain that coverage hardening is one guide inside broader testing. | `testing/SKILL.md` routes to testing discipline, coverage hardening, validation gates, and domain-skill loading. | Add package target/list row and skill validation if standalone. | Likely new `testing.zip`, not final. | `make check-skills`, `make check-package-paths`; project tests are task-specific. | `testing`. | `SKILL.md` version plus sibling `version-history.md`; preserve old coverage prompt lineage. |
| `code-auditing` | `code-auditing/`. | Likely `code-auditing/`, pending Slice03. | Audit guide links stay package-local; domain skill references need source/installed route clarity. | New installed skill route likely `/code-auditing`. | README should present diagnosis-only audit separately from testing/remediation. | `code-auditing/SKILL.md` routes to audit scope, severity, scale, modernization, and hardening handoff. | Add package target/list row and skill validation if standalone. | Likely new `code-auditing.zip`, not final. | `make check-skills`, `make check-package-paths`. | `code-auditing`. | `SKILL.md` version plus sibling `version-history.md`; seed from audit source history. |
| `agent-coordination` | `agent-coordination/`. | Likely `agent-coordination/`, pending Slice03. | Coordination guide links stay package-local; external component route links should be documented as installed skill routes. | New installed skill route likely `/agent-coordination`. | README should describe role language, delegation, context packets, and result integration. | `agent-coordination/SKILL.md` carries CC/CDC/operator terminology directly and routes to guides. | Add package target/list row and skill validation if standalone. | Likely new `agent-coordination.zip`, not final. | `make check-skills`, `make check-package-paths`. | `agent-coordination`. | `SKILL.md` version plus sibling `version-history.md`; new prose version entry required. |
| `contribution-style` | `contribution-style/`. | Likely `contribution-style/`, pending Slice03. | Links from guides to `templates/CONTRIBUTION-TICKET.md` must be package-local. | New installed skill route likely `/contribution-style`. | README should route upstream-ticket work to this component and mention the template. | `contribution-style/SKILL.md` routes to guide and template use. | Add package target/list row and skill validation if standalone. | Likely new `contribution-style.zip`, not final. | `make check-skills`, `make check-package-paths`. | `contribution-style`. | `SKILL.md` version plus sibling `version-history.md`; preserve contribution guide provenance. |

## Slice03 Release-Surface Inputs

Slice03 must decide whether every likely package root becomes a generated zip,
which package roots are installed by default, how README route language handles
source checkout versus generated zip versus installed skill use, and how
package-path exception policy changes. This register is intentionally not
final on Makefile mechanics.
