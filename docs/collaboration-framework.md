# Collaboration Framework

The collaboration framework is the repository's top-level skill for rigorous
human/LLM engineering work. Its entrypoint is [`SKILL.md`](../SKILL.md), and
its supporting material lives under [`knowledge/`](../knowledge/).

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
| Composer skill | [`SKILL.md`](../SKILL.md) | Top-level collaboration-framework entrypoint and route table. |
| Collaboration posture | [`knowledge/collaboration-framework/docs/AI-CONSTITUTION-SUPPLEMENT.md`](../knowledge/collaboration-framework/docs/AI-CONSTITUTION-SUPPLEMENT.md) | Peer-frame and quality-floor posture. |
| Engineering method | [`knowledge/engineering-methods/docs/AI-ENGINEERING-METHODOLOGY.md`](../knowledge/engineering-methods/docs/AI-ENGINEERING-METHODOLOGY.md) | Knowledge substrate, collaborative posture, and process rigor. |
| Project management | [`knowledge/project-management/docs/PROJECT-MANAGEMENT.md`](../knowledge/project-management/docs/PROJECT-MANAGEMENT.md) | Project, arc, slice, planning, close, and bubble-up wayfinder. |
| Work verification | [`knowledge/work-verification/templates/LEDGER-DISCIPLINE.md`](../knowledge/work-verification/templates/LEDGER-DISCIPLINE.md) | Ledger discipline and evidence requirements. |
| Code audit | [`knowledge/code-auditing/docs/CODE-AUDIT.md`](../knowledge/code-auditing/docs/CODE-AUDIT.md) | Diagnosis-only code audit discipline. |
| Testing | [`knowledge/testing/docs/CODE-COVERAGE.md`](../knowledge/testing/docs/CODE-COVERAGE.md) | Test coverage hardening guidance. |
| Agent coordination | [`knowledge/agent-coordination/docs/SUBAGENT-DELEGATION-POLICY.md`](../knowledge/agent-coordination/docs/SUBAGENT-DELEGATION-POLICY.md) | Delegation boundaries and multi-agent coordination. |
| Contribution style | [`knowledge/contribution-style/docs/CONTRIBUTION-STYLE.md`](../knowledge/contribution-style/docs/CONTRIBUTION-STYLE.md) | Maintainer-facing issue, PR, and ticket style. |
| Contribution ticket template | [`knowledge/contribution-style/templates/CONTRIBUTION-TICKET.md`](../knowledge/contribution-style/templates/CONTRIBUTION-TICKET.md) | Template for upstream contribution tickets. |

## Whole Framework Or Narrow Component

The top-level framework is the daily-driver composer. Load it when you need
the working posture plus routing across planning, verification, audit, testing,
delegation, and contribution disciplines.

Use a narrower component path when you already know the task shape and want to
avoid carrying unnecessary context. For example, a focused upstream issue can
start from contribution style, while an independent verification pass can start
from ledger discipline and the relevant project-management close file.

The exact public category language is still bounded for Arc05. For now, the
safe operating model is practical: use the composer for the whole working
system, and use component source paths when the task clearly needs only one
discipline.
