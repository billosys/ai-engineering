# Agent-Coordination Split Map

```yaml
project: project04-knowledge-library-reorg
arc: arc08-framework-guide-decomposition
slice: slice10-agent-coordination-guide-split
artifact: agent-coordination-split-map
source_commit: 9e2d5d055712efb53028ef250091d70487a257a0
```

## Accepted Guide Set

Slice10 implemented the four accepted numbered agent-coordination guides:

- `knowledge/agent-coordination/guides/01-when-to-delegate.md`
- `knowledge/agent-coordination/guides/02-context-packets.md`
- `knowledge/agent-coordination/guides/03-result-integration.md`
- `knowledge/agent-coordination/guides/04-anti-patterns.md`

The split is semantic, not heading-only. Each guide is independently loadable
and routes to the companion guide needed for the next coordination stage.

## Semantic Preservation Map

| Former delegation-policy material | New owner | Preservation claim |
|-----------------------------------|-----------|--------------------|
| Do not delegate thinking/edit/review judgment | `01-when-to-delegate.md`, `04-anti-patterns.md` | Preserved as the core decision rule and thinking-delegation anti-pattern. |
| Lookup/evidence enumeration may be delegated or parallelized | `01-when-to-delegate.md`, `02-context-packets.md` | Preserved as the allowed delegation shape and packet design target. |
| Serial on thinking, parallel on lookup | `01-when-to-delegate.md` | Preserved as the operating rule. |
| Quality over elapsed time on the thinking path | `01-when-to-delegate.md`, `04-anti-patterns.md` | Preserved as a positive rule and speed-over-quality anti-pattern. |
| Context loss and skill loss failure modes | `01-when-to-delegate.md`, `04-anti-patterns.md` | Preserved as reasons for the boundary and context-starvation anti-pattern. |
| Self-contained prompt requirements | `02-context-packets.md` | Expanded into explicit context packet fields, good/bad packet shapes, and output contracts. |
| Returned summaries must be re-evaluated by the main context | `03-result-integration.md`, `04-anti-patterns.md` | Preserved as parent-context responsibility and summary-trust anti-pattern. |
| Codex adaptation: use parallel tools/subagents for lookup only | `01-when-to-delegate.md`, `03-result-integration.md` | Preserved in product-neutral form. |
| Verification that the policy is working | `03-result-integration.md`, `04-anti-patterns.md` | Preserved as result checking and anti-pattern detection. |
| Caveat for workloads where elapsed time matters more than depth | `01-when-to-delegate.md` | Preserved as a named caveat requiring an explicit different operating mode. |

## Selective Loading

The new load paths reduce required context for common tasks:

- Delegation decision: `01-when-to-delegate.md`.
- Lookup handoff preparation: `02-context-packets.md`.
- Parent-context result inspection and integration:
  `03-result-integration.md`.
- Failure-mode diagnosis: `04-anti-patterns.md`.

## Quality-Floor Preservation

The split preserves the required agent-coordination floor:

- thinking/edit/review judgment stays in the main context;
- lookup and evidence enumeration may be delegated or parallelized;
- the main or parent context independently inspects returned evidence;
- context packets are self-contained without smuggling design decisions into the
  delegated task;
- result integration remains a parent-context responsibility;
- anti-patterns include thinking delegation, vague handoffs, summary trust,
  speed-over-quality pressure, buried boundaries, context starvation, and
  acceptance by formatting;
- CC, CDC, and Operator role terms remain in the component entrypoint.
