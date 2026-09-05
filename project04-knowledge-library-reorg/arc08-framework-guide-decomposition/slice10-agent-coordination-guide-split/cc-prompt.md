# CC Prompt: Project04 Arc08 Slice10 Agent-Coordination Guide Split

You are CC completing Project04 Arc08 Slice10 in Expedited Mode.

Expedited Mode changes only the explicit commit, close, and advance behaviors
already recorded in Project04. It does not authorize shortcuts, skipped
validation, weaker evidence or review, inferred source scope, reduction or
other change in scope, timeline interpretation, or override of operator
approval gates.

## Required Reading

Read before editing:

1. `project04-knowledge-library-reorg/project-plan.md`
2. `project04-knowledge-library-reorg/arc08-framework-guide-decomposition/arc-plan.md`
3. `project04-knowledge-library-reorg/arc08-framework-guide-decomposition/ledger.md`
4. `project04-knowledge-library-reorg/arc08-framework-guide-decomposition/slice10-agent-coordination-guide-split/slice-plan.md`
5. `project04-knowledge-library-reorg/arc08-framework-guide-decomposition/slice10-agent-coordination-guide-split/ledger.md`

Also read these source files before editing:

- `AGENTS.md`
- `Makefile`
- `knowledge/agent-coordination/SKILL.md`
- `knowledge/agent-coordination/guides/SUBAGENT-DELEGATION-POLICY.md`
- `knowledge/agent-coordination/version-history.md`
- `knowledge/collaboration-framework/SKILL.md`
- `knowledge/collaboration-framework/guides/04-component-route-table.md`
- `knowledge/collaboration-framework/version-history.md`
- `knowledge/engineering-methods/guides/04-operational-routing.md`
- `knowledge/engineering-methods/version-history.md`
- `docs/ORIGINS.md`
- `docs/collaboration-framework.md`
- `workbench/release-notes/RELEASE-0.5.0.md`
- `assets/packaging/path-exceptions.tsv`

## Task

Split the current agent-coordination monolith:

- `knowledge/agent-coordination/guides/SUBAGENT-DELEGATION-POLICY.md`

into:

- `knowledge/agent-coordination/guides/01-when-to-delegate.md`
- `knowledge/agent-coordination/guides/02-context-packets.md`
- `knowledge/agent-coordination/guides/03-result-integration.md`
- `knowledge/agent-coordination/guides/04-anti-patterns.md`

The split must be semantic, not just heading extraction. Each new guide should
be independently useful and selectively loadable. Preserve the current
agent-coordination contract:

- do not delegate thinking/edit/review judgment;
- lookup/evidence enumeration can be delegated or parallelized;
- the main context independently inspects and integrates returned evidence;
- context packets must be self-contained enough for lookup work without
  smuggling design decisions into the delegated task;
- result integration remains a parent-context responsibility;
- anti-patterns include thinking delegation, vague handoffs, summary trust,
  speed-over-quality pressure on the thinking path, and buried delegation
  boundaries;
- CC/CDC/operator terms remain routed clearly in the component entrypoint or
  adjacent framework route surfaces.

Use `git mv` for the old monolith when choosing the primary successor path so
history is preserved where Git similarity permits. If semantic extraction makes
Git record delete/add rather than a rename, record that in the legacy
disposition artifact and closing report.

Remove `SUBAGENT-DELEGATION-POLICY.md` as a live source/package route unless a
specific support/provenance retention decision is recorded. Do not leave stale
links or package paths.

## Source Scope

Authorized source edits are limited to the split and necessary repairs in:

- `knowledge/agent-coordination/**`
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
- `assets/packaging/path-exceptions.tsv`, only if route/package validation
  shows an exception repair is necessary

Do not commit generated zips, `build/`, or `target/skills/`.

## Required Planning Artifacts

Create:

- `artifacts/current-agent-coordination-surface-map.md`
- `artifacts/agent-coordination-split-map.md`
- `artifacts/legacy-subagent-policy-disposition.md`
- `artifacts/source-route-repair-map.md`
- `artifacts/source-validation-results.md`
- `closing-report.md`

Update:

- `ledger.md`

Do not create `cdc-verification.md`.

## Validation

Run and record at minimum:

- Source `git diff --check`.
- Focused local Markdown link validation for touched route files.
- `make check-skills`.
- `make collab-framework`.
- `make check-package-paths`.
- Generated `collaboration-framework.zip` inspection confirming all four new
  agent-coordination guides are present and the old
  `SUBAGENT-DELEGATION-POLICY.md` package path follows the recorded
  disposition.
- Final source and planning worktree status checks.

Package-path validation must have zero hard failures.

## Commit Instructions

Commit source changes after validation and before final planning close.
Because other work may share the branch, explicitly list every source file in
the commit command. Use a message such as:

```text
Split agent-coordination guide surface

Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

Then commit the Slice10 planning close packet, explicitly listing every
planning file changed or created. Use a message such as:

```text
Complete Project04 Arc08 Slice10

Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

If the closing report records a pending planning close hash, make a tiny
follow-up planning commit that records the actual close-packet commit hash,
again with explicit file paths and both trailers.

## Report Back

Report:

- source commit hash;
- planning commit hash or hashes;
- exact source and planning file lists;
- validation summary;
- `SUBAGENT-DELEGATION-POLICY.md` disposition;
- final source and planning statuses;
- Slice11 bubble-up.
