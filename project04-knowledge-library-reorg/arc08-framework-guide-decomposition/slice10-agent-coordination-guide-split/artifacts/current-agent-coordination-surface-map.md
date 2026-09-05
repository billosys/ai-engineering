# Current Agent-Coordination Surface Map

```yaml
project: project04-knowledge-library-reorg
arc: arc08-framework-guide-decomposition
slice: slice10-agent-coordination-guide-split
artifact: current-agent-coordination-surface-map
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
source_basis_before_edit: 1eb10d789734d9cca5c2c0f7cdedb4257dfab1e6
```

## Current Surface Before Slice10

The agent-coordination component started Slice10 with this source shape:

- `knowledge/agent-coordination/SKILL.md`
- `knowledge/agent-coordination/guides/SUBAGENT-DELEGATION-POLICY.md`
- `knowledge/agent-coordination/version-history.md`

`SUBAGENT-DELEGATION-POLICY.md` was the only live agent-coordination guide
body. It carried the thinking-versus-lookup delegation boundary, the "serial
on thinking, parallel on lookup" rule, quality-over-elapsed-time pressure, tool
installation guidance, Codex adaptation, verification advice, and caveats about
task classes where looser delegation may be acceptable.

## Live Route References Before Edit

The pre-edit route scan found live references to the old delegation-policy guide
in:

- `knowledge/agent-coordination/SKILL.md`
- `knowledge/collaboration-framework/SKILL.md`
- `knowledge/collaboration-framework/guides/04-component-route-table.md`
- `knowledge/engineering-methods/guides/04-operational-routing.md`
- `docs/collaboration-framework.md`
- `docs/ORIGINS.md`
- `Makefile` `CF_FILES`

`workbench/release-notes/RELEASE-0.5.0.md` named the accepted
agent-coordination component but did not yet record the split guide routes.
`AGENTS.md` had work-verification, testing, and code-auditing route guidance
but no agent-coordination route guidance yet.

## Route Families Checked

The required source route families were checked before editing:

- `agent-coordination`: live owner of the monolith.
- `collaboration-framework`: composer route table and component route guide.
- `engineering-methods`: operational route table.
- public docs: old path present in the framework docs and origins sidebar.
- packaging: old path present in `Makefile` `CF_FILES`.
- package-path exceptions: no old agent-coordination exception was present
  before edit and no exception repair was required.

## Package Surface Before Edit

Before Slice10, `collaboration-framework.zip` included
`collaboration-framework/knowledge/agent-coordination/guides/SUBAGENT-DELEGATION-POLICY.md`
through the `CF_FILES` list. The accepted Arc08 target requires replacing that
package entry with the four numbered agent-coordination guides.
