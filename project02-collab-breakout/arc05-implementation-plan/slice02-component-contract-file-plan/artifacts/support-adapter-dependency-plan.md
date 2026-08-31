# Support Adapter Dependency Plan

```yaml
project: project02-collab-breakout
arc: arc05-implementation-plan
slice: slice02-component-contract-file-plan
status: proposed-done
artifact-status: support adapter dependency plan
source-files-edited: false
```

## Grounding

This plan consumes the verified Slice01 cross-cutting map and the Arc04
operator-accepted architecture. It preserves support asset ownership, adapter
placement, dependency edge boundaries, `agent-coordination` scope,
CC/CDC/operator terminology, context-packet discipline, result integration,
component-boundary-analysis placement, source/package/release gates, memory
admission deferral, and CCDP separation.

## Support Asset Ownership

| support asset | Owner | Target placement | Package/source contract note |
|---------------|-------|------------------|------------------------------|
| Ledger discipline full template/protocol | `work-verification` | `work-verification/templates/LEDGER-DISCIPLINE.md`, with guide splits under `work-verification/guides/`. | Package-local links must resolve from the generated package. If both guide and template forms ship, Makefile content lists must include both intentionally. |
| Contribution ticket template | `contribution-style` | `contribution-style/templates/CONTRIBUTION-TICKET.md`. | Links from `contribution-style/SKILL.md` and guides should be package-local. |
| PM worked example | `project-management` | `project-management/examples/01-worked-example-odm.md`. | Example is package payload if PM ships standalone; cross-component links should not assume source checkout paths. |
| Component route table | `collaboration-framework` | `collaboration-framework/guides/component-route-table.md`. | The composer can route to installed skill names and source paths, but package-local links only cover composer-local files. |
| Generic guide skeleton | No accepted component owner in Slice02 | Deferred. | `templates/GUIDE.md` should not be silently bundled into one component without later rationale. |

## Adapter Placement

| adapter | Owner | Target placement | Boundary |
|---------|-------|------------------|----------|
| CC/CDC/operator terminology | `agent-coordination` | `agent-coordination/SKILL.md` and relevant guide intros. | Specialist components can reference the terminology but should route to `agent-coordination` rather than redefining it fully. |
| Legacy Claude/Codex wording | `agent-coordination` plus local notes where necessary | `agent-coordination/guides/04-anti-patterns.md` or component-local "Notes for Codex" sections. | Preserve functional translation, not cosmetic renaming churn. |
| Context-packet discipline | `agent-coordination` | `agent-coordination/guides/02-context-packets.md`. | Current delegation policy is insufficient; new prose is required. |
| Result integration | `agent-coordination` | `agent-coordination/guides/03-result-integration.md`. | Subagent output is evidence/input, not automatic closure. |
| Source/package/release gates adapter | `engineering-methods` | `engineering-methods/guides/06-source-package-release-gates.md`. | Shared gate semantics live here; every component still owns a local contract. |

## Dependency Edges

| dependency edge | Direction | Reason |
|-----------------|-----------|--------|
| Composer routes to specialists | `collaboration-framework` -> all accepted components | The composer remains the daily-driver entrypoint and should not inline all specialist bodies. |
| Methodology routes to operations | `engineering-methods` -> `project-management`, `work-verification`, `testing`, `code-auditing`, `agent-coordination`, `contribution-style` | Process practice needs operational components without absorbing their contracts. |
| PM closes through verification | `project-management` -> `work-verification` | PM owns lifecycle; work verification owns evidence and row closure. |
| Audit hardening handoff | `code-auditing` -> `testing` | Audit is diagnosis-only; hardening and coverage belong to testing. |
| Testing routes to domain skills | `testing` -> language/tooling skills | Tests must follow project language/tooling correctness rules. |
| Coordination supports role-bearing work | `agent-coordination` -> PM, verification, audit, implementation contexts | Delegation, context packets, and result integration cross several workflows. |
| Contribution consumes findings | `contribution-style` -> `code-auditing` and `collaboration-framework` | Upstream tickets may derive from audits and should keep the collaboration posture. |

## Deferred And Non-Component Boundaries

- `component-boundary-analysis` belongs at
  `engineering-methods/guides/05-component-boundary-analysis.md`. It is a guide,
  not a standalone component.
- `memory admission` remains deferred future research. No Project02 component,
  package root, source path, or generated zip is planned for it.
- CCDP separation is preserved. `protocols/ccdp/`, `ccdp.zip`, and
  CCDP-specific Make targets are adjacent protocol distribution surfaces, not
  collaboration-framework component payload.
- Component maintenance/version history is not a standalone support component.
  The accepted contract is per-component `SKILL.md` version plus sibling
  `version-history.md`.
