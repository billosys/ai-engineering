# Part II — The canonical planning worktree

In the absence of a project's own stated convention, planning artifacts live on
a dedicated Git worktree, not on the implementation branch and not under the
implementation branch's `docs/` tree. This is the canonical planning worktree.
It is the single source of truth for where planning artifacts live; the
[methodology](../AI-ENGINEERING-METHODOLOGY.md) used to carry an abridged copy
and now points here.

The default planning substrate is:

1. **Find the repository's worktree convention.** Inspect the repository before
   creating anything. If it already has a worktree directory convention, reuse
   it. Prefer an existing in-repo `.worktrees/` directory when present; otherwise
   use the convention already visible from `git worktree list`.
2. **If no convention exists, use `$PROJECT_DIR/.worktrees`.** This keeps the
   planning tree close to the repository while leaving it off the implementation
   branch.
3. **Use a `planning` branch and worktree by default.** If a suitable planning
   branch/worktree already exists, use it. If not, create a `planning` branch
   and a worktree directory of the same name under the worktree root.
4. **The `planning` branch is orphaned.** It shares the repository's Git object
   database and remotes, but it starts with no inherited implementation files.
   Its sole purpose is to house project plans, arc plans, per-scale ledgers,
   prompts, close reports, and CDC verification. The default branch is used to
   identify the repository and remote context, not to seed the planning files.

When a planning branch/worktree does not already exist, the safe creation
recipe is:

```sh
WORKTREE_ROOT="${PROJECT_DIR}/.worktrees" # or the repo's existing convention
git -C "$PROJECT_DIR" worktree add --detach --no-checkout "$WORKTREE_ROOT/planning"
git -C "$WORKTREE_ROOT/planning" switch --orphan planning
```

The resulting default shape is:

```
$PROJECT_DIR/.worktrees/planning/
  project01-<slug>/
    project-plan.md             ← the project's plan-of-record (the arc roadmap)
    ledger.md                   ← project-level DoD / composition ledger
    closing-report.md           ← project-level close + gate review, written at project close
    arcNN-<slug>/
      arc-plan.md               ← the arc's plan-of-record (the slice breakdown)
      ledger.md                 ← arc-level slice-close / composition ledger
      closing-report.md         ← arc-level close + bubble-up, written at arc close
      sliceNN-<slug>/
        slice-plan.md           ← plan-of-record for this slice
        ledger.md               ← grep-verifiable acceptance criteria (the steps)
        cc-prompt.md            ← the assignment the executing context receives
        closing-report.md       ← per-row walk + bubble-up, written at slice close
        cdc-verification.md     ← independent re-run + check, written at slice close
```

Three tiers of plan-of-record, one per scale: **`project-plan.md`** for the
project, **`arc-plan.md`** for each arc, and **`slice-plan.md`** for each
slice. Three tiers of ledger, one per scale: **`ledger.md`** beside each
project plan, arc plan, and slice plan. Three tiers of closing-report close the
same scales when they finish: project, arc, and slice. The per-slice
`cdc-verification.md` is the independent re-run that gates a slice closed.
Their full roles are defined in [`Planning, top-down`](./03-planning-top-down.md),
[`Closing slices`](./04-closing-slices.md), and
[`Closing arcs`](./05-closing-arcs.md); their on-disk shape is fixed here.

Each scale is also **verified by a ledger** — the recomposition discipline in
[`LEDGER-DISCIPLINE.md`](../../templates/LEDGER-DISCIPLINE.md). The ledger rows
for a scale live in that scale's own `ledger.md`: project rows in
`projectNN-<slug>/ledger.md`, arc rows in `arcNN-<slug>/ledger.md`, and slice
rows in `sliceNN-<slug>/ledger.md`. The plan-of-record names the capability,
roadmap, or slice scope; the ledger file carries the grep-verifiable rows that
prove the plan. `LEDGER-DISCIPLINE.md` owns the ledger mechanics at all three
scales; this file owns where the rows live.

### Naming rules

- **Projects use `projectNN-<slug>`**, matching the arc and slice convention.
  `project01-vault-split` is the shape; `docs/design-v0.1.0` is no longer the
  default. Version-looking directory names have repeatedly confused humans and
  LLMs into treating planning scope as release scope.
- **`NN` is two digits, zero-padded** (`project01`, `arc01`, `slice03`) — sorts
  cleanly, reads consistently, and survives projects that grow past nine arcs.
- **`<slug>` is short, kebab-case, and descriptive in isolation** —
  `project01-vault-split`, `arc01-discovery`, not `project01-thing`. Read aloud,
  the path should tell a reader what is in that directory without opening it.
- **Directory order is not dependency order.** Project metadata determines
  ordering and relationships: `depends-on`, `blocks`, `related`, current status,
  and any project-specific lineage fields. The numeric prefix is a stable,
  sortable local identifier, not the source of truth for dependency semantics.
- **When a body of work is one slice, not an arc**, skip the arc wrapper: the
  five per-slice documents live directly in one `sliceNN-<slug>/` directory
  under `projectNN-<slug>/`, with no `arc-plan.md` or arc-level
  `ledger.md` / `closing-report.md` above them. That collapse is not a third
  case to choose; it is what you discover when the sizing judgment comes back
  "one slice, not an arc." A project that is genuinely a single slice may keep a
  minimal `project-plan.md` and project-level `ledger.md`, but the moment a
  second arc is conceivable, write the full roadmap.

### Project metadata

Every `project-plan.md` begins with a short metadata block or equivalent header
section that makes relationships explicit. Minimum fields:

| Field | Meaning |
| --- | --- |
| `project` | Stable project id, matching `projectNN-<slug>`. |
| `status` | `planned`, `active`, `blocked`, `closed`, or project-specific status. |
| `depends-on` | Project ids or external prerequisites this project consumes. Empty is explicit. |
| `blocks` | Project ids or external outcomes blocked by this project. Empty is explicit. |
| `related` | Adjacent projects, tickets, repos, or evidence sources that are not hard dependencies. |

Use the same relationship vocabulary consistently across project plans. If a
project has a richer metadata schema, record it in the project instructions and
keep these meanings intact.

### The five per-slice documents

The five documents under each `sliceNN-<slug>/` are the artifact set that
attaches to one execution unit. They split into an **open set** (written when
the slice is planned, before any code) and a **close set** (written when the
slice finishes):

| Document | Set | Role |
|----------|-----|------|
| `slice-plan.md` | open | Plan-of-record: goal, scope (in/out), verification approach, exit criteria. |
| `ledger.md` | open | The acceptance criteria as grep-verifiable rows — the steps. Format and discipline in [`LEDGER-DISCIPLINE.md`](../../templates/LEDGER-DISCIPLINE.md). |
| `cc-prompt.md` | open | The assignment the implementing context (CC) receives. |
| `closing-report.md` | close | The per-row walk written at slice close, plus the **bubble-up to the arc** (see [`Closing slices`](./04-closing-slices.md)). |
| `cdc-verification.md` | close | The independent re-run that verifies the closing report against evidence, plus the **bubble-up check** (see [`Closing slices`](./04-closing-slices.md)). |

Opening the close-set documents at slice start, or leaving the open-set
documents unfinished when handing off to CC, are both spec-keeping failures.
Write the open set fully before CC starts; write the close set only once
there is something to close.

---
