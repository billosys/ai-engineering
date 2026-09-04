# Current Remaining History Surface Map

Source checkout: `/Users/oubiwann/lab/billosys/ai-engineering`

Source commit after implementation: `657f156c7ad8048e60727275c2eed0d910de7f45`

## Scope

Slice05 inspected the five remaining framework component roots:

- `knowledge/work-verification/`
- `knowledge/testing/`
- `knowledge/code-auditing/`
- `knowledge/agent-coordination/`
- `knowledge/contribution-style/`

For each component, CC inspected the current `SKILL.md`, `guides/`,
`templates/`, and `examples/` surfaces where they existed before editing.

## Pre-Edit Surface Findings

| Component | `SKILL.md` version before edit | Source files inspected | Embedded history before edit | Sibling history before edit | Notes |
|-----------|--------------------------------|------------------------|------------------------------|-----------------------------|-------|
| `work-verification` | `1.0.0` | `SKILL.md`; `templates/LEDGER-DISCIPLINE.md` | `templates/LEDGER-DISCIPLINE.md` contained `## Version History` with protocol lineage v2.4, v2.3, v2.2, v2.1, v2.0, and v1. | absent | No `guides/` or `examples/` files were present in the current source surface. |
| `testing` | `1.0.0` | `SKILL.md`; `guides/CODE-COVERAGE.md` | absent | absent | Current guide is coverage-hardening only; broader testing guide split remains deferred. |
| `code-auditing` | `1.0.0` | `SKILL.md`; `guides/CODE-AUDIT.md` | `guides/CODE-AUDIT.md` contained `## Version History` with audit lineage v1.1 and v1.0. | absent | Current guide is diagnosis-only audit only; broader audit guide split remains deferred. |
| `agent-coordination` | `1.0.0` | `SKILL.md`; `guides/SUBAGENT-DELEGATION-POLICY.md` | absent | absent | Current guide remains the delegation policy; broader coordination split remains deferred. |
| `contribution-style` | `1.0.0` | `SKILL.md`; `guides/CONTRIBUTION-STYLE.md`; `templates/CONTRIBUTION-TICKET.md` | absent | absent | Current guide/template pair remains intact; broader contribution workflow split remains deferred. |

## Route Surfaces Inspected

- `Makefile` `CF_FILES`
- `knowledge/collaboration-framework/SKILL.md`
- `knowledge/collaboration-framework/version-history.md`
- source docs and release-note references discovered by `rg` for the five
  component names and legacy guide/template filenames

No guide-local `version-history.md` files existed in these five component roots
before the slice. No guide or template body split was performed.
