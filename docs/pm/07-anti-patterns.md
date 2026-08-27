# Part VII — Anti-patterns to refuse

The following layouts and habits are recognisable enough that a session should
refuse to adopt them on autopilot and propose the canonical structure instead,
via the confirmation protocol. If one is *already present* from earlier work,
name the dissonance to the operator before adopting or migrating it — silent
migration of an in-flight project's layout is its own failure mode.

- **`tasks/`, `work/`, `progress/`, or `reports/` at the project root.** The
  most common inventions; they conflict with the `project → arc → slice`
  vocabulary and route artifacts away from the scale they belong to.
- **`milestones/` for ledgers.** The level-1 ledger-bearing unit is **slice**,
  not milestone; the ledger lives inside the slice directory as `ledger.md`,
  not under a top-level `milestones/` tree.
- **A mega-file `PLAN.md` at the project root holding every arc, slice, and
  ledger.** The artifact set is per-scale for a reason: each document is a
  coherent unit that can be independently verified, closed, and re-read.
  Merging them across scales prevents all three. `project-plan.md` holds the
  *roadmap*, not the detail; each scale's acceptance/composition rows live in
  its own `ledger.md`.
- **Arc or project ledger sections embedded in plan files.** This was a
  transitional layout. Current projects, arcs, and slices all use a dedicated
  sibling `ledger.md`; plan files describe scope and sequencing, while ledger
  files carry acceptance/composition rows.
- **Per-author or per-session subdirectories** (`claude-a/`,
  `session-2026-06-18/`). The artifact is owned by the slice or arc it belongs
  to, not by who or when wrote it. Authorship belongs in the file header, not
  the path.
- **Closing a slice without bubbling up.** A `closing-report.md` with a per-row
  walk but no *Bubble-up to the arc* section is a half-closed slice — it
  verified the diff and skipped the question of what the diff did to the plan.
- **Closing an arc by fiat.** Declaring an arc done because its last slice
  merged, with no arc-level `closing-report.md` and no composition check, skips
  the one check the arc scale exists to provide.
- **A plan that never changes.** An `arc-plan.md` or `project-plan.md` whose
  Version History never grows while slices and arcs keep surfacing surprises is
  not stable — it is unmaintained, and the bubble-up checks are being skipped.
- **Detailed plans written far ahead.** Ten arc-plans authored on day one
  (see *Plan late, plan deep* in
  [`Planning, top-down`](./03-planning-top-down.md)). They are written against assumptions
  the earlier arcs will invalidate, and they rot.
- **Planning docs on the implementation branch by default.** Reusing the
  implementation branch's `docs/` tree for framework planning makes release
  docs, product docs, and LLM planning records compete for the same namespace.
  Use the planning worktree unless the operator explicitly overrides it.
- **Version-looking project directories** (`docs/design-v0.1.0/`,
  `project-v0.1.0/`). They invite readers to infer release scope from path
  shape. Use `projectNN-<slug>` and put ordering/relationships in project
  metadata.
- **Dependency semantics encoded only in directory names.** Numeric prefixes
  make paths sort; they do not define `depends-on`, `blocks`, or project
  lineage. If a relationship matters, write it in metadata where tools and
  reviewers can read it.

---
