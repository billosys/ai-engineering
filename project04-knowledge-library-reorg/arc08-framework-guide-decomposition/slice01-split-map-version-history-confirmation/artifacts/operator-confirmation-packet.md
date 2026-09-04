# Operator Confirmation Packet

Status: approved by operator on 2026-09-04.

This packet was the approval gate for Arc08 source work. The operator approved
it on 2026-09-04 with the clarifications recorded below, allowing Slice02 to
open.

Support artifacts:

- `artifacts/operator-accepted-architecture.md`
- `artifacts/component-file-layout-plan.md`

Those files provide the accepted architecture and component file layout for
Arc08. The packet below restates the concrete split map, sibling
version-history rule, and Expedited Mode wording target for confirmation.

## Operator Approval Record

The operator approved:

- the collaboration-framework guide order;
- the engineering-methods guide order;
- the sibling version-history rule;
- the Expedited Mode correction target.

Clarifications:

- The version-history management practice must be documented somewhere durable
  and next-session-visible. The expected source surface is the top-level
  `AGENTS.md` file unless the implementing slice identifies and records a
  better home.
- The Expedited Mode wording target should say: "Expedited Mode means no
  inferred source scope and no reduction or other change in scope," if that
  clarification improves the source wording.

## Operator Confirmation: Split Map

Please confirm the collaboration-framework guide order:

1. `knowledge/collaboration-framework/guides/01-posture-and-ethics.md`
2. `knowledge/collaboration-framework/guides/02-structural-pulls.md`
3. `knowledge/collaboration-framework/guides/03-collaborative-rights.md`
4. `knowledge/collaboration-framework/guides/04-component-route-table.md`

Please confirm the engineering-methods guide order:

1. `knowledge/engineering-methods/guides/01-engineering-methodology.md`
2. `knowledge/engineering-methods/guides/02-knowledge-substrate.md`
3. `knowledge/engineering-methods/guides/03-process-rigour.md`
4. `knowledge/engineering-methods/guides/04-operational-routing.md`
5. `knowledge/engineering-methods/guides/05-component-boundary-analysis.md`
6. `knowledge/engineering-methods/guides/06-source-package-release-gates.md`

## Operator Confirmation: Sibling Version-History Rule

Please confirm the sibling version-history rule for all eight framework
component roots:

- each component root keeps one component `version:` in its `SKILL.md`;
- each component root gets one sibling `version-history.md`;
- changes to a component `SKILL.md`, `guides/`, `templates/`, or `examples/`
  are recorded in that sibling component history;
- version history should not live under `guides/` merely because a guide was
  edited;
- embedded `## Version History` sections in component `SKILL.md`, guides, or
  templates should be moved or reconciled into the sibling history file unless
  a later source-edit slice records an explicit exception.

Component roots covered by this rule:

- `knowledge/collaboration-framework/`
- `knowledge/engineering-methods/`
- `knowledge/project-management/`
- `knowledge/work-verification/`
- `knowledge/testing/`
- `knowledge/code-auditing/`
- `knowledge/agent-coordination/`
- `knowledge/contribution-style/`

Known first correction target:

- move `knowledge/project-management/guides/version-history.md` to
  `knowledge/project-management/version-history.md` and repair local links.

## Operator Confirmation: Expedited Mode Wording Target

Please confirm this correction target for Expedited Mode:

- Expedited Mode only changes the explicit listed process changes.
- Expedited Mode means no shortcuts.
- Expedited Mode means no skipped validation.
- Expedited Mode means no weaker evidence or review.
- Expedited Mode means no inferred source scope and no reduction or other
  change in scope.
- Expedited Mode means no timeline interpretation.
- Expedited Mode does not override explicit operator approval gates.

The likely Slice02 source edit surfaces are:

- `knowledge/project-management/guides/PROJECT-MANAGEMENT.md`
- `knowledge/collaboration-framework/SKILL.md`
- `knowledge/project-management/guides/version-history.md`, which should move
  to `knowledge/project-management/version-history.md`

## Required Operator Decision

Decision recorded: confirmed with named adjustments.

Expedited Mode did not override this approval gate; the gate closed by explicit
operator approval.
