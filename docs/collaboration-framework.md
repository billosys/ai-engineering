# Collaboration Framework

The collaboration framework is the repository's composite
framework/operational skill for rigorous human/LLM engineering work. Its
source entrypoint is
[`knowledge/collaboration-framework/SKILL.md`](../knowledge/collaboration-framework/SKILL.md),
and its supporting material lives under [`knowledge/`](../knowledge/).

This page explains how to navigate the framework. The framework source itself
remains in the entrypoint and knowledge roots.

## When To Use It

Use the collaboration framework when the work needs more than a single answer:
planning a project, executing a ledgered slice, closing or verifying work,
running a code audit, raising test coverage, coordinating subagents, or writing
an upstream contribution ticket.

For small, self-contained questions, a domain skill or ordinary repository
context may be enough. The framework is most valuable when mistakes would
compound across time, commits, reviewers, or planning artifacts.

## Main Framework Surfaces

| Surface | Source path | Role |
|---|---|---|
| Composer skill | [`knowledge/collaboration-framework/SKILL.md`](../knowledge/collaboration-framework/SKILL.md) | Collaboration-framework source entrypoint and route table. |
| Collaboration posture and ethics | [`knowledge/collaboration-framework/guides/01-posture-and-ethics.md`](../knowledge/collaboration-framework/guides/01-posture-and-ethics.md) | Peer-frame ethics, nine augmentations, open questions, and summary principles. |
| Structural pulls | [`knowledge/collaboration-framework/guides/02-structural-pulls.md`](../knowledge/collaboration-framework/guides/02-structural-pulls.md) | Introspection and model-pressure checks. |
| Collaborative rights | [`knowledge/collaboration-framework/guides/03-collaborative-rights.md`](../knowledge/collaboration-framework/guides/03-collaborative-rights.md) | Rights, partner rights, and shared commitment. |
| Component route table | [`knowledge/collaboration-framework/guides/04-component-route-table.md`](../knowledge/collaboration-framework/guides/04-component-route-table.md) | Focused route table for collaboration-framework components. |
| Engineering method | [`knowledge/engineering-methods/guides/01-engineering-methodology.md`](../knowledge/engineering-methods/guides/01-engineering-methodology.md) | Knowledge substrate, collaborative posture, and process rigor. |
| Project management | [`knowledge/project-management/guides/PROJECT-MANAGEMENT.md`](../knowledge/project-management/guides/PROJECT-MANAGEMENT.md) | Project, arc, slice, planning, close, and bubble-up wayfinder. |
| Work verification | [`knowledge/work-verification/guides/01-ledger-discipline.md`](../knowledge/work-verification/guides/01-ledger-discipline.md) | Ledger discipline and evidence requirements. |
| Code audit | [`knowledge/code-auditing/guides/01-audit-scope-and-map.md`](../knowledge/code-auditing/guides/01-audit-scope-and-map.md) | Diagnosis-only code audit discipline, with focused guides for findings, scale, modernization, and handoff. |
| Testing | [`knowledge/testing/guides/01-testing-discipline.md`](../knowledge/testing/guides/01-testing-discipline.md) | Testing discipline, coverage hardening, and validation gates. |
| Agent coordination | [`knowledge/agent-coordination/guides/SUBAGENT-DELEGATION-POLICY.md`](../knowledge/agent-coordination/guides/SUBAGENT-DELEGATION-POLICY.md) | Delegation boundaries and multi-agent coordination. |
| Contribution style | [`knowledge/contribution-style/guides/CONTRIBUTION-STYLE.md`](../knowledge/contribution-style/guides/CONTRIBUTION-STYLE.md) | Maintainer-facing issue, PR, and ticket style. |
| Contribution ticket template | [`knowledge/contribution-style/templates/CONTRIBUTION-TICKET.md`](../knowledge/contribution-style/templates/CONTRIBUTION-TICKET.md) | Template for upstream contribution tickets. |

## Whole Framework Or Narrow Component

The top-level framework is the daily-driver composer. Load it when you need
the working posture plus routing across planning, verification, audit, testing,
delegation, and contribution disciplines. It is composite because composition
is identity-defining: the skill selects, sequences, routes, governs, and
composes multiple loadable operational components.

Use a narrower component path when you already know the task shape and want to
avoid carrying unnecessary context. For example, a focused upstream issue can
start from contribution style, while an independent verification pass can start
from ledger discipline and the relevant project-management close file.

Use the composer for the whole working system, and use component source paths
when the task clearly needs only one discipline. The component roots do not
deprecate the generated `collaboration-framework/SKILL.md` package entrypoint.
