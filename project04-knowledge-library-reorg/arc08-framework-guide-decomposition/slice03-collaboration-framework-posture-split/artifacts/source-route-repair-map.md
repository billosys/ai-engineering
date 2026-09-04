# Slice03 Source Route Repair Map

Date: 2026-09-04
Source checkout: `/Users/oubiwann/lab/billosys/ai-engineering`
Source commit: `e7ba785bf8c48ef061f69f9d90d176030b62dfc4`

## Source Files Repaired

| Source file | Repair |
|---|---|
| `Makefile` | Replaced the old collaboration-framework monolith in `CF_FILES` with `01-posture-and-ethics.md`, `02-structural-pulls.md`, `03-collaborative-rights.md`, `04-component-route-table.md`, and `knowledge/collaboration-framework/version-history.md`. |
| `docs/ORIGINS.md` | Updated the historical public route from the old supplement file to the posture guide set entrypoint. |
| `docs/collaboration-framework.md` | Replaced the single collaboration posture row with four explicit posture/component rows. |
| `knowledge/collaboration-framework/SKILL.md` | Bumped version to `1.5.0`, updated the foundation summary, route table, session-use instructions, and version-history route to the split posture guide set and sibling history file. |
| `knowledge/engineering-methods/guides/AI-ENGINEERING-METHODOLOGY.md` | Updated companion/provenance links from the old monolith path to the posture guide set entrypoint. |

## Old Reference Scan

After repair, no live Markdown link or route target points to `knowledge/collaboration-framework/guides/AI-CONSTITUTION-SUPPLEMENT.md`. The remaining filename mentions are explicitly provenance/disposition text:

```text
knowledge/collaboration-framework/guides/01-posture-and-ethics.md
knowledge/collaboration-framework/guides/02-structural-pulls.md
knowledge/collaboration-framework/guides/03-collaborative-rights.md
knowledge/collaboration-framework/version-history.md
```

## Expedited Mode Guardrail Preservation

The collaboration-framework route table still carries the Slice02 Expedited Mode guardrails in the project-management row:

```text
Expedited Mode only changes the explicit process behaviors listed there; it does not authorize shortcuts, skipped validation, weaker evidence or review, inferred source scope or scope reduction/change, timeline interpretation, or operator approval gate override.
```

The stricter Slice02 phrase remains visible in `knowledge/project-management/guides/PROJECT-MANAGEMENT.md`:

```text
no shortcuts; no skipped validation; no weaker evidence or review; no inferred source scope and no reduction or other change in scope; no timeline interpretation; operator approval gates are not overridden.
```
