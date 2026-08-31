# Package And Release Acceptance Record

```yaml
project: project02-collab-breakout
arc: arc04-breakout-architecture
slice: slice04-operator-acceptance-architecture-synthesis
status: accepted-architecture-input
operator-acceptance: accepted
accepted-package-path: recorded-in-operator-accepted-architecture
source-files-edited: false
```

## Status

This package/release acceptance record preserves Project01 and
project01-harmonise-paths source/package gates for operator review. At
original CC close, every package path below was pending and non-final because
explicit operator evidence was absent.

Operator acceptance is now recorded in
`operator-accepted-architecture.md`. The accepted architecture sets the
component package-root names for Arc05 planning while preserving this record's
Project01 source/package, package-local link, zip root, README, `SKILL.md`,
Makefile, generated zip, validation, release-surface, and CCDP separation
gates.

## Source Grounding

Read-only source grounding shows the current release surface:

- `README.md` documents `collaboration-framework.zip`, framework use,
  package use, domain skill library use, and CCDP separation.
- Top-level `SKILL.md` is the current collaboration-framework entrypoint.
- `Makefile` defines `INSTALL_ZIPS`, `ALL_SKILL_FILES`, `CF_FILES`,
  `CF_NAME := collaboration-framework`, `CCDP_NAME := ccdp`, `make
  collab-framework`, `make all`, `make check-skills`, `make
  check-package-paths`, `make ccdp-package`, and `make check-ccdp-package`.
- `templates/LEDGER-DISCIPLINE.md` and `templates/CONTRIBUTION-TICKET.md`
  are current support assets.
- `package-path-exceptions.tsv` remains part of the package-local link gate.

## Project01 Gate Carry-Forward

| Gate | Required package/release decision | Acceptance status |
|------|-----------------------------------|-------------------|
| source/package contract | Every component contract states source path, package path, source/package reader modes, installed skill behavior, and adjacent CCDP behavior where relevant. | pending |
| package-local links | Links inside generated zip roots must resolve without relying on source checkout paths. | pending |
| zip root | Every component names its generated zip root before implementation. | pending |
| README and `SKILL.md` routing | README and entrypoints must route source clone, package, installed skill, and composed framework use coherently. | pending |
| Makefile package list | `INSTALL_ZIPS`, `ALL_SKILL_FILES`, package targets, and `CF_FILES` changes must match accepted component roots. | pending |
| generated zip behavior | Arc05 must build generated zip artifacts from accepted roots and verify paths. | pending |
| release surface synchronization | README, `SKILL.md`, Makefile, package list, package-path exceptions, generated zip expectations, and version history move together. | pending |
| CCDP separation | CCDP remains protocol distribution material with `ccdp.zip`, not an installable collaboration-framework skill package. | pending |

## Pending Package Paths

Accepted package path: none.

| Pending package path | Proposed purpose | Zip root assumption | Package-local link consequence |
|----------------------|------------------|---------------------|--------------------------------|
| `collaboration-framework/` | Composer package with compact safety floor and route table. | `collaboration-framework.zip` continues to unzip under `collaboration-framework/` unless Arc05 proposes migration. | Links route to accepted component packages or embedded composer docs. |
| `collaborative-posture-and-ethics/` | Posture component plus dependency edge. | New generated zip root if accepted. | Links to methodology and contribution must be local or explicit cross-package references. |
| `engineering-methodology-and-process/` | Methodology process component and router. | New generated zip root if accepted. | Routes to PM, ledger, audit, coverage, delegation, contribution, and domain skills. |
| `ledger-verification-protocol/` | Ledger evidence component. | New generated zip root if accepted. | PM close links to ledger must resolve in package mode. |
| `project-management/` | PM component family and PM wayfinder. | New generated zip root if accepted. | Internal PM guide, example, anti-pattern, and ledger links must resolve. |
| `code-audit-discipline/` | Diagnosis-only audit component. | New generated zip root if accepted. | Audit examples must be package-local and use the slice `artifacts/` durable-output default. |
| `coverage-hardening-discipline/` | Coverage hardening component with compatibility treatment. | New generated zip root if accepted. | Historical coverage guide routes must remain discoverable. |
| `delegation-policy/` | Delegation decision component. | New generated zip root if accepted. | Role-language adapter note must resolve locally or through accepted central route. |
| `contribution-style-and-voice/` | Contribution component plus `CONTRIBUTION-TICKET.md`. | New generated zip root if accepted. | Template links must resolve under the package root. |

## Non-Package Rows

No standalone package root is accepted for `agent-adapter-and-routing`,
`repository-orientation-and-distribution`, `project-management-wayfinder`,
verification-methodology, ontology critique, component-maintenance discipline,
or evidence strength/memory admission vocabulary. These remain adapter,
support asset, constraint, package/release gate, dependency edge,
non-component, or deferred rows unless the operator changes the decision.

## Validation Commands

Arc05 must map source edits to validation command coverage:

| Change type | Validation command |
|-------------|--------------------|
| Any `SKILL.md` description or frontmatter update | `make check-skills` |
| Packaged Markdown links, bundle contents, Makefile package list changes, package-path exceptions, or generated zip expectations | `make check-package-paths` |
| Composer package behavior | `make collab-framework` plus `make check-package-paths` |
| Full skill release surface | `make all` plus `make check-package-paths` |
| CCDP source or package changes, if separately touched | `make ccdp-package` plus `make check-ccdp-package` |

This slice performs no source/package implementation and does not run package
builds. It records the package/release gate and non-final acceptance state for
operator decision.
