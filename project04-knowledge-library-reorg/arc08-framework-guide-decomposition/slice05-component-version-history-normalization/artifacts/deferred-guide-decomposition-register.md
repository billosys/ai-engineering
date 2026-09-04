# Deferred Guide-Decomposition Register

Source commit: `657f156c7ad8048e60727275c2eed0d910de7f45`

Slice05 did not implement guide-body splits for the remaining components. The
items below are deferred re-entry candidates from the accepted component layout
plan and require later operator review before implementation.

| Component | Current source payload | Deferred target shape | Slice05 disposition |
|-----------|------------------------|-----------------------|---------------------|
| `work-verification` | `knowledge/work-verification/templates/LEDGER-DISCIPLINE.md` | Focused guides for ledger discipline, evidence strength, row closure, silent-drop checks, and independent verification, with the full protocol retained as template/support asset. | Not implemented in Slice05. Only history normalization was performed. |
| `testing` | `knowledge/testing/guides/CODE-COVERAGE.md` | `guides/01-testing-discipline.md`, `guides/02-coverage-hardening.md`, and `guides/03-validation-gates.md`. | Not implemented in Slice05. Current coverage guide remains intact. |
| `code-auditing` | `knowledge/code-auditing/guides/CODE-AUDIT.md` | Audit scope/map, findings/severity, scale-aware auditing, modernization synthesis, and audit-to-hardening handoff guides. | Not implemented in Slice05. Current audit guide remains intact. |
| `agent-coordination` | `knowledge/agent-coordination/guides/SUBAGENT-DELEGATION-POLICY.md` | Delegation, context packets, result integration, and anti-pattern guides. | Not implemented in Slice05. Current delegation policy remains intact. |
| `contribution-style` | `knowledge/contribution-style/guides/CONTRIBUTION-STYLE.md` and `knowledge/contribution-style/templates/CONTRIBUTION-TICKET.md` | Contribution style guide plus upstream ticket workflow guide, with the ticket template retained as template/support asset. | Not implemented in Slice05. Current guide/template pair remains intact. |

These are not silent drops because Slice05 scope explicitly excluded guide-body
splitting. They are preserved as future operator-review surfaces for a later
arc or slice.
