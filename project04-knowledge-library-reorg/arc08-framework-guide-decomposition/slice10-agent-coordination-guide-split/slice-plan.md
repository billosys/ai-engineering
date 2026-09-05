# Slice 10: Agent-Coordination Guide Split

```yaml
project: project04-knowledge-library-reorg
arc: arc08-framework-guide-decomposition
slice: slice10-agent-coordination-guide-split
status: verified-closed
opened-by: CDC
opened-on: 2026-09-05
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source-files-edited: authorized-by-this-slice
operating-mode: expedited-without-scope-inference
```

## Purpose

Split the current agent-coordination monolith into the four operator-accepted
numbered guides:

1. `knowledge/agent-coordination/guides/01-when-to-delegate.md`
2. `knowledge/agent-coordination/guides/02-context-packets.md`
3. `knowledge/agent-coordination/guides/03-result-integration.md`
4. `knowledge/agent-coordination/guides/04-anti-patterns.md`

The split must preserve the current delegation boundary: thinking/edit/review
judgment stays in the main context; lookup/evidence enumeration may be
parallelized; subagent outputs are reintegrated by the main context. The
component entrypoint must preserve the CC/CDC/operator terminology and
route-level coordination contract.

## Source Authorization

Source edits are authorized only for the agent-coordination guide split and
directly necessary route, package, history, documentation, release-note, and
package-path repairs.

Expected source surfaces include:

- `knowledge/agent-coordination/SKILL.md`
- `knowledge/agent-coordination/guides/SUBAGENT-DELEGATION-POLICY.md`
- `knowledge/agent-coordination/version-history.md`
- `knowledge/collaboration-framework/SKILL.md`
- `knowledge/collaboration-framework/guides/04-component-route-table.md`
- `knowledge/collaboration-framework/version-history.md`
- `knowledge/engineering-methods/guides/04-operational-routing.md`
- `knowledge/engineering-methods/version-history.md`
- `Makefile`
- `docs/ORIGINS.md`
- `docs/collaboration-framework.md`
- `AGENTS.md`
- `workbench/release-notes/RELEASE-0.5.0.md`
- `assets/packaging/path-exceptions.tsv`, only if validation requires a
  package-path exception move or disposition

No generated `build/` or `target/skills/` artifacts are to be committed.

## Required Work

1. Inventory the current source, route, package, and history surfaces before
   editing.
2. Split `SUBAGENT-DELEGATION-POLICY.md` into the four accepted guides,
   preserving semantics while improving selective loading.
3. Use `git mv` for the old monolith when choosing the primary successor path
   so file history is preserved where Git similarity permits. If heavy semantic
   rewriting makes Git record delete/add, document that disposition.
4. Remove the old `SUBAGENT-DELEGATION-POLICY.md` path as a live route unless
   explicitly retained as a support/provenance asset with operator-consistent
   rationale.
5. Update route surfaces, package lists, histories, documentation, AGENTS, and
   release notes.
6. Validate source, links, generated package shape, and package paths.
7. Close the slice with artifacts, ledger update, and `closing-report.md`.

## Validation Expectations

Minimum validation:

- Source `git diff --check`.
- Focused local Markdown link validation for touched route files.
- `make check-skills`.
- `make collab-framework`.
- `make check-package-paths`.
- Generated `collaboration-framework.zip` inspection confirming the four new
  agent-coordination guides are present and the old monolith package path
  follows the recorded disposition.
- Final source and planning worktree status checks.

## Outputs

Required planning artifacts:

- `artifacts/current-agent-coordination-surface-map.md`
- `artifacts/agent-coordination-split-map.md`
- `artifacts/legacy-subagent-policy-disposition.md`
- `artifacts/source-route-repair-map.md`
- `artifacts/source-validation-results.md`
- `closing-report.md`

Do not create `cdc-verification.md`; CDC writes it after independent review.

## Closure

Slice10 is CDC-verified closed.

CDC verification:

- `cdc-verification.md`
- Source commit: `9e2d5d055712efb53028ef250091d70487a257a0`
- Planning close commits: `f447399e250b46e7bdb9659c9f5ff558752893ad`,
  `25273bb550aebec40d377157c1b7c78104d04398`

Bubble-up: Slice11 is opened for the contribution-style guide split. No Arc08
scope change is required.
