# Skill Entrypoint Validation Plan

```yaml
project: project02-collab-breakout
arc: arc05-implementation-plan
slice: slice03-package-readme-validation-plan
status: proposed-done
artifact-status: skill entrypoint validation plan
source-files-edited: false
```

## Grounding

This plan uses verified Slice01 release validation evidence, verified Slice02
component contract and file layout evidence, and the Slice02 package/source
contract register. It plans `SKILL.md` entrypoint validation without writing
final entrypoint prose.

## Entrypoint Rules

- Every component entrypoint is a component-local `SKILL.md`.
- Every `SKILL.md` has YAML frontmatter with `name:`, `description:`,
  `version:`, `license:`, and useful metadata.
- Each frontmatter `name:` must match the generated package root and installed
  skill route.
- Each `description` must stay within the limit enforced by
  `scripts/check-skill-description.sh`; `make check-skills` is the aggregate
  check.
- Every component has sibling `version-history.md`; component versioning uses
  the `SKILL.md` version plus that sibling history.
- Route table entries should name when to load another component instead of
  linking across package roots with fragile relative paths.

## Composer Plan

`collaboration-framework/SKILL.md` remains the composer:

- Carries the compact collaboration/posture floor.
- Routes to all seven specialist component entrypoints through a route table.
- Keeps the daily-driver behavior and `/collaboration-framework` installed
  route.
- Removes full specialist bodies from the composer package unless Slice04
  records an offline-use reason to vendor them.
- Has package-local links only to composer-local files such as
  `guides/posture-and-ethics.md`, `guides/structural-pulls.md`,
  `guides/collaborative-rights.md`, `guides/component-route-table.md`, and
  `version-history.md`.

## Component Entrypoint Plan

| Component | component entrypoint | Route table responsibility | Validation note |
|-----------|----------------------|----------------------------|-----------------|
| `collaboration-framework` | `collaboration-framework/SKILL.md` | Route to every specialist component and preserve daily-driver composer use. | `make check-skills`, `make collab-framework`, `make check-package-paths`. |
| `engineering-methods` | `engineering-methods/SKILL.md` | Route to methodology guides, source/package/release gates, PM, verification, testing, auditing, coordination, contribution, and domain skills. | `make check-skills`, component package target, `make check-package-paths`. |
| `project-management` | `project-management/SKILL.md` | Route to PM guides, examples, and `work-verification` for ledger mechanics. | `make check-skills`, component package target, `make check-package-paths`. |
| `work-verification` | `work-verification/SKILL.md` | Route to evidence, row closure, silent-drop, independent verification guides, and `templates/LEDGER-DISCIPLINE.md`. | `make check-skills`, component package target, `make check-package-paths`. |
| `testing` | `testing/SKILL.md` | Route to testing discipline, coverage hardening, validation gates, and domain skills. | `make check-skills`, component package target, `make check-package-paths`. |
| `code-auditing` | `code-auditing/SKILL.md` | Route to audit scope, findings/severity, scale-aware auditing, modernization, and audit-to-hardening handoff. | `make check-skills`, component package target, `make check-package-paths`. |
| `agent-coordination` | `agent-coordination/SKILL.md` | Carry CC/CDC/operator terms directly and route to delegation, context-packet, result-integration, and anti-pattern guides. | `make check-skills`, component package target, `make check-package-paths`. |
| `contribution-style` | `contribution-style/SKILL.md` | Route to contribution style, upstream ticket workflow, and `templates/CONTRIBUTION-TICKET.md`. | `make check-skills`, component package target, `make check-package-paths`. |

## Validation Plan

- Update `ALL_SKILL_FILES` so `make check-skills` checks all eight component
  `SKILL.md` files.
- Keep `scripts/check-skill-description.sh` as the description/frontmatter
  guard. If the checker needs component-root path support, change the Makefile
  call site rather than weakening the script.
- Validate generated package links with `make check-package-paths` after
  package content lists and package-local links exist.
- Run `make all` as the aggregate build after component package targets are
  implemented.
- Run CCDP checks only when CCDP files or `ccdp.zip` packaging changes.

## Versioning Expectations

- Each component starts from the closest current source history and records the
  breakout as an expansion, not a silent overwrite.
- Sibling `version-history.md` files carry historical entries and future
  component changes.
- `SKILL.md` files carry current component versions only, keeping entrypoints
  lean enough for direct load.
