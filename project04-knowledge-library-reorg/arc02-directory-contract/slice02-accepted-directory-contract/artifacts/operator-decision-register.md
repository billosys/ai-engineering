# Operator Decision Register

```yaml
project: project04-knowledge-library-reorg
arc: arc02-directory-contract
slice: slice02-accepted-directory-contract
artifact: operator-decision-register
artifact-status: accepted planning register
created-on: 2026-09-02
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
source-files-edited: false
```

## Purpose

This register dispositions every D-1 through D-12 decision from Arc02 Slice01
as accepted, adjusted, rejected, or operator decision required. There are no
unlabeled unresolved decisions. Choices that still need operator approval
before source edits are explicitly marked.

## Disposition Table

| ID | Slice01 decision | Disposition | Accepted/adjusted decision | Operator approval before source edits |
|----|------------------|-------------|----------------------------|---------------------------------------|
| D-1 | `docs/` versus `knowledge/` contract | accepted | `docs/` is explanation; `knowledge/` is default substrate for skill/framework/method/source material; wrappers or migration notes preserve human routes when source-like `docs/` material moves. | Required for the concrete file-by-file move list in Arc03. |
| D-2 | Project02 framework/operational component roots | adjusted | Use `knowledge/<component>/` as the default source root for Project02 components rather than top-level component roots or mandatory `knowledge/framework/<component>/` nesting. | Required if any component remains top-level or uses a family nesting exception. |
| D-3 | `collaboration-framework` composer | adjusted | Preserve the daily-driver composer and package root `collaboration-framework`; target source material under `knowledge/collaboration-framework/`; keep top-level `SKILL.md` compatibility until an implementation slice provides a shim, replacement route, or explicit no-shim decision. | Required for top-level `SKILL.md` shim/removal behavior. |
| D-4 | Planned `concept-card-method` method skill | accepted | Reserve `knowledge/concept-card-method/` as planned method root; do not claim live source or installed package availability before implementation. | Required before publishing availability language or adding package targets. |
| D-5 | Skill kind and topology language | adjusted | Preserve kind and topology as independent internal contract axes; defer final public vocabulary to Arc05. | Required only if Arc02 is asked to publish terminology before Arc05. |
| D-6 | Source root versus package root relationship | accepted | Source roots and package roots are separate contract axes; package identity may come from frontmatter, component names, selected-file package definitions, protocol rules, or multi-entrypoint rules. | Required for any new intentional divergence not covered by this contract. |
| D-7 | Biome multi-entrypoint root | accepted | Preserve `knowledge/biome/` as one multi-entrypoint source root with multiple package roots. | Not required unless implementation evidence favors splitting the root. |
| D-8 | Template ownership | adjusted | Keep top-level `templates/` only for cross-cutting support; move owner-local templates under their owning source or protocol root when package behavior can be preserved. | Required for top-level template exceptions after file-by-file classification. |
| D-9 | CCDP protocol/package surface | accepted | Keep `protocols/ccdp/` separate from installable skill packages; route through docs or skill references rather than absorbing it into `knowledge/`. | Required to reopen CCDP protocol package policy. |
| D-10 | README, `docs/`, and `SKILL.md` wayfinding | adjusted | README stays top-level orientation; `docs/` becomes focused explanation; `SKILL.md` files describe load behavior; top-level `SKILL.md` remains compatibility surface until implementation decides the shim/replacement. | Required for final public wording and top-level `SKILL.md` behavior. |
| D-11 | Migration sequencing and compatibility gates | adjusted | Accept mechanical moves before prose rewrites and validation after each source-edit slice; leave detailed migration sequence and validation matrix to Slice03. | Required before Arc03 source edits begin. |
| D-12 | Package-path exception policy | adjusted | Prefer package-local link repair first; allow only narrow, reasoned, preferably expiring explicit exceptions for intentional unresolved cases. | Required for any persistent no-expiration exception or accepted warning. |

## Accepted Facts

- Project02 accepted `collaboration-framework` as a daily-driver composer.
- Project03 planned `concept-card-method` as a method skill, but it is not
  live source.
- CCDP remains separate from installable skill packages.
- Biome is a real multi-entrypoint source-root/package-root edge case.
- Skill kind and topology remain independent: kind describes what the material
  is about; topology describes whether it is atomic, composite,
  bridge/integration, or another accepted structure.

## Rejected Options

- Rejected: treating current `docs/` as the default long-term home for
  framework/source substrate solely because that is where material lives today.
- Rejected: assuming one source root must produce exactly one package root.
- Rejected: making Project02 component roots live source before implementation.
- Rejected: making Project03 `concept-card-method` a current package before
  implementation.
- Rejected: folding CCDP into installable skill packages without explicit
  protocol-policy evidence.
- Rejected: using Arc02 internal contract language as final public vocabulary
  before Arc05.

## Re-Entry Conditions

- Re-enter Project02 if `knowledge/<component>/` cannot preserve accepted
  component roles, daily-driver composer behavior, independent loadability, or
  package validation.
- Re-enter Project03 if `knowledge/concept-card-method/` cannot preserve the
  planned method-skill architecture without claiming live source.
- Re-enter CCDP policy only if implementation evidence requires CCDP to behave
  as an installable skill package.
- Re-enter kind/topology classification if source roots, package roots,
  entrypoints, or generated package behavior change load reason or composition
  identity.
- Re-enter Arc02 Slice03 if the migration sequence cannot execute mechanical
  moves before prose rewrites or cannot repair package-local links before
  exceptions.

## No Unlabeled Unresolved Decisions

Every D-1 through D-12 decision has an accepted, adjusted, rejected, or
operator decision required disposition above. Remaining operator approvals are
source-edit gates, public-language gates, top-level compatibility gates, or
persistent-exception gates; none are unlabeled unresolved decisions.
