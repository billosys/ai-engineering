# Operator-Accepted Architecture

```yaml
project: project02-collab-breakout
arc: arc04-breakout-architecture
slice: slice04-operator-acceptance-architecture-synthesis
status: accepted-architecture
operator-acceptance: accepted
accepted-on: 2026-08-31
explicit-operator-acceptance-evidence: recorded
source-files-edited: false
```

## Acceptance Evidence

The operator accepted the revised Project02 Arc04 architecture on 2026-08-31
after reviewing the acceptance packet and supplemental layout scenarios.

Operator acceptance incorporated the following explicit decisions:

- Keep `collaboration-framework` as the daily-driver composer and the home for
  the collaboration/posture floor.
- Rename the process/router component to `engineering-methods`.
- Keep `project-management` as its own component family.
- Rename the ledger/evidence component to `work-verification`.
- Use `testing` as the broader component that currently contains coverage
  hardening and can later receive TDD guidance.
- Rename the audit component to `code-auditing` and split its guide surface by
  stage/scale during implementation planning.
- Promote the old delegation policy into a broader `agent-coordination`
  component.
- Rename `contribution-style-and-voice` to `contribution-style`.
- Put source/package/release gates under `engineering-methods`, while every
  component keeps its own package/source contract.
- Version each component as a whole through its `SKILL.md`, with a sibling
  `version-history.md` so the entrypoint stays lean.
- Place ontology critique as
  `engineering-methods/guides/05-component-boundary-analysis.md`, not as a
  standalone component.
- Defer memory admission as future research, not a Project02 component.

## Accepted Component Map

| Accepted component | Purpose | Contract summary | Key dependencies and routes |
|--------------------|---------|------------------|-----------------------------|
| `collaboration-framework` | Daily-driver composer for science, engineering, research, pedagogy, technical writing, and large sustained work. | Carries the compact collaboration/posture floor and routes to all specialized components. | Routes to `engineering-methods`, `project-management`, `work-verification`, `testing`, `code-auditing`, `agent-coordination`, and `contribution-style`. |
| `engineering-methods` | LLM-centric SDLC, process practice, operational routing, component-boundary analysis, and source/package/release gates. | Owns the methodology/process layer without absorbing the specialized operational components. | Depends on `collaboration-framework` posture floor; routes to PM, verification, testing, auditing, agent coordination, contribution, and domain skills. |
| `project-management` | Project/arc/slice planning and close lifecycle. | Owns planning layout, top-down planning, bottom-up closure, confirmation protocol, anti-patterns, and examples. | Depends on `work-verification` for evidence closure. |
| `work-verification` | Evidence, ledgers, row closure, independent verification, and silent-drop prevention. | Replaces the narrower `ledger-verification-protocol` name while retaining ledger discipline as the core mechanism. | Used by PM, auditing, testing, and the composer. |
| `testing` | Testing discipline surface, starting with coverage hardening and validation gates. | Future-compatible with TDD guidance; coverage hardening is one guide, not the whole component identity. | Routes to domain skills and project-local test tooling. |
| `code-auditing` | Diagnosis-only audit discipline. | Preserves audit as diagnosis rather than remediation, with stage/scale-aware guidance and audit-to-hardening handoff. | May hand off to `testing` after diagnosis; uses domain skills as needed. |
| `agent-coordination` | Agent role language, delegation decisions, context-packet discipline, and result integration. | Replaces narrow delegation policy with coordination guidance for high-quality multi-agent work. | Routes to PM, verification, auditing, and implementation contexts when subagents or multiple LLM surfaces are involved. |
| `contribution-style` | Upstream contribution style and ticket preparation. | Keeps contribution guidance and `CONTRIBUTION-TICKET.md` together while shortening the component name. | Uses collaboration posture and may consume audit findings as input. |

## Accepted Layout Sketch

```text
collaboration-framework/
  SKILL.md
  version-history.md
  guides/
    posture-and-ethics.md
    structural-pulls.md
    collaborative-rights.md
    component-route-table.md

engineering-methods/
  SKILL.md
  version-history.md
  guides/
    01-engineering-methodology.md
    02-knowledge-substrate.md
    03-process-rigour.md
    04-operational-routing.md
    05-component-boundary-analysis.md
    06-source-package-release-gates.md

project-management/
  SKILL.md
  version-history.md
  guides/
    01-scales-of-work.md
    02-canonical-planning-worktree.md
    03-planning-top-down.md
    04-closing-slices.md
    05-closing-arcs.md
    06-confirmation-protocol.md
    07-anti-patterns.md
    08-maintenance.md
  examples/
    01-worked-example-odm.md

work-verification/
  SKILL.md
  version-history.md
  guides/
    01-ledger-discipline.md
    02-evidence-strength.md
    03-row-closure.md
    04-silent-drop-checks.md
    05-independent-verification.md
  templates/
    LEDGER-DISCIPLINE.md

testing/
  SKILL.md
  version-history.md
  guides/
    01-testing-discipline.md
    02-coverage-hardening.md
    03-validation-gates.md

code-auditing/
  SKILL.md
  version-history.md
  guides/
    01-audit-scope-and-map.md
    02-findings-and-severity.md
    03-scale-aware-auditing.md
    04-modernization-synthesis.md
    05-audit-to-hardening-handoff.md

agent-coordination/
  SKILL.md
  version-history.md
  guides/
    01-when-to-delegate.md
    02-context-packets.md
    03-result-integration.md
    04-anti-patterns.md

contribution-style/
  SKILL.md
  version-history.md
  guides/
    01-contribution-style.md
    02-upstream-ticket-workflow.md
  templates/
    CONTRIBUTION-TICKET.md
```

## Agent Coordination Terminology

`agent-coordination/SKILL.md` should carry the core terminology directly:

- `CC`: the code writer. Current backronym: CLI Contributor. Historically
  meant Claude Code or Codex CLI.
- `CDC`: the co-architect and co-planner, peer to the operator. Current
  backronym: Coordinating/Design Contributor. Historically meant Claude
  Desktop Cowork or Codex Desktop Contributor.
- `Operator`: the human in the loop, co-architect, and co-planner.

The component should also soften the old hard line against delegation:

- Prefer keeping humans tightly in the loop.
- Avoid telephone games and indiscriminate delegation to subagents.
- Use subagents when the task is a good fit, but give them a generous context
  packet: intent, constraints, relevant evidence, accepted architecture,
  quality bar, output contract, and integration expectations.
- Treat context starvation as a first-class delegation failure mode.
- Reintegrate subagent outputs through the main context before closure.

## Accepted Non-Component Decisions

| Topic | Accepted placement | Re-entry condition |
|-------|--------------------|--------------------|
| Source/package/release gates | `engineering-methods`, plus mandatory per-component package/source contract fields. | Reopen if Arc05 cannot map gates cleanly to README, `SKILL.md`, Makefile, generated zip, and validation behavior. |
| Component maintenance/version history | Component-level contract: version in each `SKILL.md`, sibling `version-history.md`. | Reopen only if maintenance becomes independent direct-load work. |
| Ontology critique | `engineering-methods/guides/05-component-boundary-analysis.md`. | Reopen standalone status only with evidence of direct-load reuse beyond Project02. |
| Memory admission | Deferred future research. | Reopen in a future memory protocol or collaboration-framework v0.6 effort. |
| CCDP | Separate protocol distribution, not a collaboration-framework skill component. | Reopen only if CCDP packaging policy changes outside Project02. |

## Arc05 Carry-Forward

Arc05 can plan implementation from this accepted architecture. It must still
produce a detailed implementation plan before source edits begin. That plan
must preserve Project01 source/package path constraints, package-local link
behavior, zip roots, README routes, `SKILL.md` routes, Makefile package lists,
generated zip behavior, validation commands, compatibility notes, and CCDP
separation.
