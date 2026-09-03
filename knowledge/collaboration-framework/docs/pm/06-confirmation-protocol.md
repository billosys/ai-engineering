# Part VI — The confirmation protocol

The layout in [`Canonical planning worktree`](./02-canonical-planning-worktree.md)
is the *default*. The operator owns the actual layout for their project. This
protocol is the discipline that connects the two: the
executing context **confirms before adopting a layout and never invents one
mid-stream.** Apply it before creating any planning directory or filename.

### When the protocol triggers

At any of these moments, **stop and confirm with the operator before creating
directories or filenames**:

- Starting a new project that does not yet have a layout.
- Beginning the first arc or slice of a project where the layout was set up by
  prior work but is not obviously visible from an `ls`.
- Opening any artifact category not yet present in the repository and not
  covered by this document. Durable slice-produced artifacts are covered: their
  default home is `artifacts/` inside the owning slice directory.
- Resuming a project after long elapse, where the layout you remember may no
  longer match the layout on disk.

### How to confirm

A short, specific question with a concrete proposal — *not* an open-ended
"what would you like?", which throws the work back to the operator. Quote the
default verbatim, name where it comes from, and offer the choice to accept,
adjust, or override:

> I'm about to create the planning substrate for project 1. The default layout
> from [docs/PROJECT-MANAGEMENT.md](../PROJECT-MANAGEMENT.md) is a dedicated
> `planning` Git worktree:
>
> ```
> $PROJECT_DIR/.worktrees/planning/
>   project01-<slug>/
>     project-plan.md
>     ledger.md
>     closing-report.md
>     arc01-<slug>/
>       arc-plan.md
>       ledger.md
>       slice01-<slug>/
>         slice-plan.md
>         ledger.md
>         cc-prompt.md
>         artifacts/
>         closing-report.md
>         cdc-verification.md
> ```
>
> If no planning worktree exists, I will create an orphan `planning` branch and
> a worktree named `planning` under the existing worktree convention, or under
> `$PROJECT_DIR/.worktrees` if no convention exists. The project directory I
> would use is `project01-<slug>`. Want me to proceed with that, or adjust the
> branch / worktree / project slug?

That is it. The default is named, the substitutions are named, and the
operator's three options (proceed / adjust / override) are explicit.

For asset categories **not** covered by this document — project-scoped prompts
that outlive a slice, upstream contribution drafts, scratch notes — the same
protocol applies, but **without a default to quote**: name the category,
propose what you would otherwise have chosen on autopilot, and let the
operator pick. For durable artifacts produced by a slice, do quote the default:
`sliceNN-<slug>/artifacts/`, with an operator override recorded in the slice
plan if needed.

### What to do after the operator answers

- **"Proceed"** — record the chosen planning branch, worktree path, and project
  directory in the project's `CLAUDE.md`, `AGENTS.md`, or equivalent local
  instruction file so the next session does not re-confirm. One line is enough:
  *"Planning artifacts live on orphan branch `planning`, worktree
  `.worktrees/planning`, under `projectNN-<slug>/`, per
  [docs/PROJECT-MANAGEMENT.md](../PROJECT-MANAGEMENT.md); durable
  slice-produced artifacts default to
  the owning slice's `artifacts/` directory."* If no local instruction file
  exists, raise it as a follow-up — but do **not** silently start scattering
  files.
- **"Adjust"** — apply the adjustment, then record the adjusted layout in the
  project's `CLAUDE.md`, `AGENTS.md`, or equivalent local instruction file. If
  the adjustment diverges meaningfully from the default, briefly say *why* (team
  convention, prior tool output, a fork in scale) — spec-keeping for the layout
  itself.
- **"Override entirely"** — adopt the operator's layout verbatim, record it the
  same way, and add a one-line note that this project does not use the default.

### What this protocol prevents

It prevents the one failure mode this part exists to address: the next session
arriving and *inventing*. Once the protocol has been applied once per project,
the layout is written where the next session will see it, and no inventing is
necessary — or permitted.

---
