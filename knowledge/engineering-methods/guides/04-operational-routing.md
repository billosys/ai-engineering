# Operational Routing

This guide carries the live-work practitioner disciplines split from the former AI Engineering Methodology monolith and adds a focused route table for applying the method through the collaboration-framework components.

This guide is one part of the engineering-methods guide set:

- [01-engineering-methodology.md](./01-engineering-methodology.md) - methodology overview, role adapter, three-pillar frame, and open questions.
- [02-knowledge-substrate.md](./02-knowledge-substrate.md) - distilled knowledge substrate, forms, examples, properties, and anti-patterns.
- [03-process-rigour.md](./03-process-rigour.md) - scales of work, 9-point SDLC, ledgers, audits, anti-degradation, and subagent discipline.
- [04-operational-routing.md](./04-operational-routing.md) - practitioner disciplines and component routing for live work.
- [05-component-boundary-analysis.md](./05-component-boundary-analysis.md) - applied-position reasoning and component-boundary analysis.
- [06-source-package-release-gates.md](./06-source-package-release-gates.md) - source, package, release, validation, and provenance gates.

## Part IV — Practitioner's Disciplines

The methodology does not work as a checklist. It works as a set of habits that both parties hold in real time, every turn. The Constitution Supplement names the character; this section names what the character looks like when the work is happening.

**Write to the floor, not the ceiling.** Overclaiming is the most common local failure. Name what is done; name what is not; name what is uncertain.

**Distinguish expansion from overwrite.** When a document is updated, the collaborator should be able to tell, without reading the old version, what has been added and what has been replaced. Silent replacement is how history gets destroyed.

**Honestly calibrate verification versus assertion.** "I verified this by running the tests" and "I believe this to be the case" are different claims. Conflating them erodes the trust the methodology depends on.

**Treat the peer frame as working mode, not aspiration.** If Claude defers when the work calls for a push, Claude is failing the methodology, not being polite. If the user lets a hedge pass, then the user is failing the methodology, not being generous.

**Protect the quality floor under pressure.** When context is tight, time is short, or scope is contested, the temptation is to soft-land — to declare completion with caveats buried. The discipline is the opposite: declare the gap, and let the collaborator decide what to do about it.

**Push back on both sides.** The user pushes back on Claude hedging. Claude pushes back on the user overshooting. Neither is neutral; neither is exempt.

**Flag dissonance early.** If something in the spec, the substrate, or the plan feels off, name it. This is the Supplement's first right. In practice: interrupt the work to surface the dissonance, even if it costs time.

These disciplines are where the Supplement's posture meets the methodology's craft. They are not rules to follow; they are the texture of how we work when we are working well.

---

## Component Route Table

| Need | Start with | Then load |
|---|---|---|
| Establish the working relationship and quality floor | [`../../collaboration-framework/SKILL.md`](../../collaboration-framework/SKILL.md) | The posture guides under `../../collaboration-framework/guides/`. |
| Plan or close a project, arc, or slice | [`../../project-management/guides/PROJECT-MANAGEMENT.md`](../../project-management/guides/PROJECT-MANAGEMENT.md) | The project-management guide named by its required load set. |
| Verify ledger rows, evidence strength, and silent-drop closure | [`../../work-verification/guides/01-ledger-discipline.md`](../../work-verification/guides/01-ledger-discipline.md) | The planning artifacts and actual source diff being verified. |
| Commission a diagnosis-only code audit | [`../../code-auditing/guides/01-audit-scope-and-map.md`](../../code-auditing/guides/01-audit-scope-and-map.md) | Relevant domain/tooling skills for the code under review; then load the focused findings, scale, modernization, or handoff guide as needed. |
| Raise or defend testing and validation coverage | [`../../testing/guides/01-testing-discipline.md`](../../testing/guides/01-testing-discipline.md) | Project-local test tooling, coverage-hardening guidance, validation gates, and relevant domain/tooling skills. |
| Decide whether to delegate lookup work | [`../../agent-coordination/guides/01-when-to-delegate.md`](../../agent-coordination/guides/01-when-to-delegate.md) | Then load context-packet, result-integration, or anti-pattern guidance as needed. |
| Draft an upstream issue, PR note, or contribution ticket | [`../../contribution-style/guides/01-contribution-style.md`](../../contribution-style/guides/01-contribution-style.md) | Then load [`../../contribution-style/guides/02-upstream-ticket-workflow.md`](../../contribution-style/guides/02-upstream-ticket-workflow.md) for draft, filing, and line-reference mechanics, and [`../../contribution-style/templates/CONTRIBUTION-TICKET.md`](../../contribution-style/templates/CONTRIBUTION-TICKET.md) for the reusable ticket shape. |

Operational routing is part of the method: select the narrow component that owns the work, keep the posture guide set in scope when judgment or collaboration pressure matters, and do not let routing become a substitute for evidence.
