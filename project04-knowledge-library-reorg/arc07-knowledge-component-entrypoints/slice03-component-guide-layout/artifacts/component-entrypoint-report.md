# Component Entrypoint Report

Source commit: `0b0f363a4070df09f1bcf7b225f4cd0db018baeb`

## Component Entrypoint Files

Slice03 added concise component-root `SKILL.md` wayfinder files for the
collaboration-framework dependency components:

| Component | Entrypoint | Primary routed material |
| --- | --- | --- |
| `agent-coordination` | `knowledge/agent-coordination/SKILL.md` | `guides/SUBAGENT-DELEGATION-POLICY.md` |
| `code-auditing` | `knowledge/code-auditing/SKILL.md` | `guides/CODE-AUDIT.md` |
| `contribution-style` | `knowledge/contribution-style/SKILL.md` | `guides/CONTRIBUTION-STYLE.md`, `templates/CONTRIBUTION-TICKET.md` |
| `engineering-methods` | `knowledge/engineering-methods/SKILL.md` | `guides/AI-ENGINEERING-METHODOLOGY.md` |
| `project-management` | `knowledge/project-management/SKILL.md` | `guides/PROJECT-MANAGEMENT.md` and focused `guides/*.md` files |
| `testing` | `knowledge/testing/SKILL.md` | `guides/CODE-COVERAGE.md` |
| `work-verification` | `knowledge/work-verification/SKILL.md` | `templates/LEDGER-DISCIPLINE.md` |

## Entrypoint Contract

Each component entrypoint is a wayfinder, not a replacement for the long guide
or template it routes to. The long-form operational content remains in
component-owned `guides/` or `templates/` files.

No separate installable packages were added for these component entrypoints.
They are packaged as dependency material inside `collaboration-framework.zip`
through the collaboration-framework `CF_FILES` list.
