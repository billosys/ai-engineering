# Migrate a Semantic Design System Between Owners

Use this method when a team must change, adopt or hand off semantic design
roles across components, modes, repositories or maintainers. Begin with the
actual source and its rendered consumers. A token table can make a decision
portable, but it does not replace the adopting system's source, build,
interaction checks or ownership.

## Map the contract before changing it

Record the current and proposed role names, types, values, aliases, scope and
owners. Trace each role through its aliases to actual consumers and states.
Keep source declarations distinct from resolved values. Include every mode in
which consumers resolve, and note component exceptions whose values happen to
match the changed role. Do not infer that identical colours, spacing or type
values have the same owner or purpose.

For each item, record:

| Item | Migration record |
|---|---|
| Role and type | User-facing purpose, consuming CSS property or other typed use, and expected value type. |
| Source and resolved value | Declaration, alias chain, resolved value and mode or component scope. |
| Owner and consumers | Team or component allowed to change it, with rendered consumers and relevant states. |
| Compatibility | Whether the established name remains, gains a compatible alias, or would break existing consumers. |
| Exception | Separate owner, reason, consumers and review condition for a value that must not follow the common change. |

Prefer preserving established public names when their meaning remains accurate.
A compatible alias can clarify ownership while letting current consumers
continue to resolve through the existing role. A rename or removal is breaking
when consumers must change or behavior can silently change; identify that
impact before editing. Do not label a role retired unless the change actually
removes its contract. For a real retirement, name its replacement or bridge,
check usage, identify an owner and review, communicate the transition, state a
condition for removal, and preserve a rollback path. Set a deadline only when
the owner has chosen one.

## Carry values across modes and implementations

For each required mode, show the old declaration and resolved value beside the
proposed declaration and resolved value. Define aliases in the scopes where
their consumers resolve them; do not assume that an inherited alias will
re-resolve against a descendant's changed primitive. Keep appearance modes
separate from language, writing direction, forced colours, contrast settings,
motion preferences, zoom and input modality. Preserve markup `lang` and `dir`
and use logical properties where layout follows writing direction.

Use a semantic table first, then show the smallest implementation projection
that helps the receiving owner verify the mapping. Compare the representation
with the actual source and check current and proposed values, including types
and aliases. Choose a stale-value check or a rollback demonstration when it is
appropriate to the artifact and risk; record what the check establishes. These
are contextual verification techniques, not required mechanics for every
migration. The [LFE handoff](examples/lfe-system-handoff.md) uses a deliberately
stale value and an in-memory reversal of its narrowly assigned CSS declarations
to verify its specific table and source projection; that does not execute a
rollback or write the source system.

Keep the handoff format proportionate and tool-neutral. A Markdown table and a
CSS excerpt can convey semantic roles and selected resolved values; they do not
encode a full cascade, generated selectors, all modes, assets, interaction
behavior or tool-specific semantics. They are not evidence of DTCG
compatibility, a converter, or lossless import/export. The receiving team must
compare the handoff with its own contract and use its existing tools to build
and inspect the result. Add a format, schema or converter only when the task
explicitly owns and validates that additional capability.

The LFE example uses Fluent 2's distinction between raw values and purpose
aliases as contextual input; it does not require Fluent's architecture or
adopt its tokens. For adoption depth, the existing [contextual adoption
route](patterns-and-adoption.md#what-the-source-comparisons-support) adapts
USWDS's distinction among principles, UX guidance and code without importing
its stylesheet or claiming its maturity or compliance.

## Apply and verify a bounded first change

Choose the smallest owned component or route for the first use. Preserve
content, URLs, assets and unrelated roles. Avoid broad literal replacement:
equal values can serve different components, states and owners. Build from the
assigned source with its existing tooling, inspect generated output where the
project consumes it, and compare the rendered states that resolve the changed
roles. Include the active mode, ordinary interaction states, keyboard focus,
and any component-specific exception. Record measured results and untested
conditions separately; source inspection or a pair calculation alone does not
prove rendered behavior.

Review the source diff, semantic table, build and rendered result together.
Confirm that public role names and consumers remain compatible, aliases
resolve in every required scope, exceptions stay intact, and no unrelated
values changed. Where source artifacts are pinned, retain their revisions and
hashes so a reviewer can reproduce the comparison. A local task-branch
integration does not imply main-branch integration, publication or deployment
authority.

## Hand off ownership and rollback

Name the source owner, receiving owner, next reviewer and the decision each is
responsible for. Make adoption reversible at the same scope as the change. A
rollback restores the prior role mappings while preserving later accepted
changes and component exceptions; it does not use broad replacement or reset
unrelated work. Rebuild and inspect the result after rollback. Treat a historic
baseline as comparison evidence, not permission to overwrite current work.

When another owner will continue the work, give them the pinned source state,
the role and consumer map, the implementation projection, checks and results,
known limits, the smallest next decision, and the rollback instructions. Do
not turn a handoff into a silent transfer of publication or service authority.
For data or recovery behavior, identify the service owner and explain how
already saved user work will be preserved, recovered, migrated, expired or
disposed before retiring its reader. A fictional example or local build cannot
choose a real service's retention policy.

The [LFE semantic mode handoff](examples/lfe-system-handoff.md) applies this
method to one accepted light/dark CSS change. It preserves the public link and
focus roles, records the separate code-component exception and limits its
claims to the pinned source and retained checks. Use [Semantic system
evolution](system-evolution.md) when the task is to trace owners, modes and
consumers before evolving an existing system.
