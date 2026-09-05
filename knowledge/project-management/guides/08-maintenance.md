# Part VIII — When to update this document

Treat updates to this document like methodology updates: dated, disclosed,
with the rationale preserved — *spec-keeping for the spec itself.* Update it
when:

- The scales of work, the canonical planning worktree, or the planning/closing
  process changes. The project-management guide owns all three now; keep the
  [methodology](../../engineering-methods/guides/01-engineering-methodology.md)'s summary in sync when the
  vocabulary itself moves.
- An anti-pattern recurs across more than one project. Add it to
  [`Anti-patterns to refuse`](./07-anti-patterns.md) with
  a name and a recognisable shape, so the next session refuses it on sight.
- A deferred asset category outside the settled slice-produced artifact default
  (project-scoped prompts, upstream contribution drafts, coverage reports,
  scratch) acquires a settled default. Add it with the same shape as the layout in
  [`Canonical planning worktree`](./02-canonical-planning-worktree.md).

Two cross-references that are settled today and should not be re-invented:
CAP-style audit reports are routed from
[`Audit Scope And Map`](../../code-auditing/guides/01-audit-scope-and-map.md)
(`workbench/<YYYY.MM.DD>-audit-results-<slug>.md` plus a top-level index and
modernization synthesis);
per-slice prompts live as `cc-prompt.md` inside the slice directory, not in a
separate prompts tree; durable artifacts produced by a slice default to
`artifacts/` inside that slice directory unless the operator records an
override.

---
