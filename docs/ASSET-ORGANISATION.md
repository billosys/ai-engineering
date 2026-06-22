# Asset Organisation — where the work lives on disk

> Operational companion to the methodology's *A default layout* section.
> This document carries that section's structural bones (the project / arc
> / slice tree and its five per-slice documents) and names the discipline
> that protects it across sessions: **the operator owns the layout; the
> executing context confirms before adopting one and never invents a new
> one mid-stream.**
>
> _Scope note (v1):_ this revision covers **only** the slice/arc tree and
> the confirmation protocol. Project-wide defaults for other asset
> categories — project-scoped prompts, upstream contribution drafts,
> coverage reports, scratch — are **deferred** to a later revision,
> pending in-flight work on epic- and project-level dependency tracking
> and broader work organisation. Until that lands, the operator decides
> where those live on a per-project basis; this document does not
> prescribe defaults for them.

## Why this exists

The methodology proposed a default layout. We have since watched, repeatedly,
the same failure mode: a fresh Claude session starts work, does not see the
section, invents its own folder names (`tasks/`, `work/`, `progress/`,
`reports/`, `phase-1/`), scatters files across them, and by the time the
operator notices, the artifact set is fragmented across three or four
parallel conventions that none of the other Claude sessions will recognise
either.

The cost compounds. Two sessions later, the same project has artifacts under
`milestones/`, `work/`, `tasks/`, and `docs/design-v0.1.0/arc01-…/slice01-…/`,
and no one — human or Claude — can find anything without spelunking. The
substrate pillar of the methodology (*"a substrate that rots is worse than
no substrate — it misleads with the authority of formalization"*) applies
to the *directory structure itself*. Drift in the layout is drift in the
substrate.

This document is the fix on the substrate side. The fix on the posture side
is the **confirmation protocol** below.

---

## Notes for Codex

For Codex, read "Claude session" as any fresh Codex Desktop, Codex CLI, or
other LLM session entering the project without the full prior context. The
failure mode is the same: the session invents plausible folders because it
does not see the established layout.

Keep the canonical filenames `cc-prompt.md` and `cdc-verification.md` unless
the operator explicitly changes the project convention. In Codex use, those
names map to the roles defined in the methodology: CC is Codex CLI in the IC
implementation role; CDC is Codex Desktop in the planning/review/QA role.
Renaming them to `codex-prompt.md` or similar inside one project would create
the same parallel-convention drift this document exists to prevent.

---

## Part I — The confirmation protocol

This is the discipline this document exists to install. Apply it before
creating any of the artifact directories described in Part II.

### When the protocol triggers

At any of these moments, **stop and confirm with the operator before
creating directories or filenames**:

- Starting a new project that does not yet have a layout.
- Beginning the first arc or slice of a project where the layout was set up
  by prior work but is not obviously visible from a `ls`.
- Opening any artifact category that is **not yet present** in the
  repository and is not covered by this document — for the asset
  categories outside the current scope (see the scope note above), the
  default is to ask the operator outright rather than assume.
- Resuming a project after long elapse, where the layout you remember may
  no longer match the layout on disk.

### How to confirm

A short, specific question with a concrete proposal. *Not* an open-ended
"what would you like?" — that throws the work back to the operator. Quote
the default verbatim, name where it comes from, and offer the operator the
choice to accept, adjust, or override:

> I'm about to create the slice artifact set for slice 1 of arc 1. The
> default layout from `docs/ASSET-ORGANISATION.md` is:
>
> ```
> docs/design-v0.1.0/arc01-<slug>/slice01-<slug>/
>   slice-doc.md
>   ledger.md
>   cc-prompt.md
>   closing-report.md
>   cdc-verification.md
> ```
>
> The `<slug>`s I'd use are `<arc-slug>` and `<slice-slug>`. Want me to
> proceed with that, or adjust the layout / slugs?

That's it. The default is named, the substitutions are named, and the
operator's three options (proceed / adjust / override) are explicit.

For asset categories **not** covered by this document — project-scoped
prompts, upstream contribution drafts, coverage reports, scratch, anything
else — the same protocol applies, but **without a default to quote**: name
the category, propose what you'd otherwise have chosen on autopilot, and
let the operator pick.

### What to do after the operator answers

- **"Proceed"** — record the chosen layout in the project's `CLAUDE.md` (or
  equivalent local instruction file) so the next session does not have to
  re-confirm. One line is enough: *"Slice artifacts live under
  `docs/design-vX.Y.Z/arcNN-<slug>/sliceNN-<slug>/`, per
  `docs/ASSET-ORGANISATION.md`."* If no `CLAUDE.md` exists, raise it as a
  follow-up — but do **not** silently start scattering files.
- **"Adjust"** — apply the operator's adjustment, then record the adjusted
  layout in the project's `CLAUDE.md`. If the adjustment diverges
  meaningfully from the default, briefly say *why* (compatibility with a
  team convention, prior tool output, a fork in scale, etc.) — this is
  spec-keeping for the layout itself.
- **"Override entirely"** — adopt the operator's layout verbatim, record
  it the same way, and add a one-line note in the local `CLAUDE.md`
  that this project does not use the default.

### What this protocol prevents

It prevents the one failure mode this whole document exists to address:
the next Claude session arriving and *inventing*. By the time the
confirmation protocol has been applied once per project, the layout is
written down where the next session will see it, and no inventing is
necessary — or permitted.

---

## Part II — The canonical layout

### Slice and arc artifacts  *(the methodology's default layout)*

The methodology's
[*A default layout*](./AI-ENGINEERING-METHODOLOGY.md#a-default-layout)
section is canonical. The shape, re-stated here so this document is
self-contained:

```
docs/design-vX.Y.Z/
  arcNN-<slug>/
    arc-plan.md               ← the arc's plan-of-record
    sliceNN-<slug>/
      slice-doc.md            ← plan-of-record for this slice
      ledger.md               ← grep-verifiable acceptance criteria (the steps)
      cc-prompt.md            ← the assignment the executing context receives
      closing-report.md       ← per-row walk, written at slice close
      cdc-verification.md     ← independent re-run, written at slice close
```

Rules:

- **`X.Y.Z` is the project's design-doc version**, not the project's release
  version. Bumps mean "the design moved," not "we cut a release."
- **`NN` is two digits, zero-padded** (`arc01`, `slice03`) — sorts cleanly,
  reads consistently, and survives projects that grow past nine arcs.
- **`<slug>` is short, kebab-case, and descriptive in isolation** —
  `arc01-erlmd-probe`, not `arc01-thing`. Read aloud, the path should tell
  a reader what's in that directory without opening it.
- **When a body of work is one slice, not an arc**, skip the arc wrapper:
  the five per-slice documents live directly in one `NN-<slug>/` directory
  under `docs/design-vX.Y.Z/`. That collapse is not a third case to choose;
  it is what you discover when the sizing judgment comes back "one slice."

The five per-slice documents are the artifact set that attaches to one
execution unit. Their roles and the per-row ledger discipline live in
[`../templates/LEDGER-DISCIPLINE.md`](../templates/LEDGER-DISCIPLINE.md).

### Asset categories outside the current scope

The following categories are **not** assigned project-wide defaults in this
revision (see the scope note at the top): project-scoped prompts that
outlive a slice, upstream contribution drafts, test-coverage reports, and
scratch / ephemeral notes. For each, apply the confirmation protocol with
no default to quote — propose what you would otherwise have chosen and
let the operator decide.

Two cross-references that *are* in the framework today (not new to this
document):

- **CAP-style audit reports** already have a home specified in
  [`./CODE-AUDIT.md`](./CODE-AUDIT.md) — `workbench/<YYYY.MM.DD>-audit-results-<slug>.md`
  plus a top-level `workbench/<YYYY.MM.DD>-audit-index.md`. Follow that
  spec, not a new one.
- **Per-slice prompts** live as `cc-prompt.md` inside the slice directory,
  per the canonical layout above. Per-slice prompts are part of the
  slice artifact set; they are not "in" some other prompts directory.

These are the only two prompt/report categories with a settled home today.
Everything else waits for the broader rev.

---

## Part III — Anti-patterns to refuse

The following layouts are recognisable enough that future Claude sessions
should refuse to adopt them on autopilot and propose the canonical
slice/arc layout instead, via the confirmation protocol:

- **`tasks/` or `work/` or `progress/` at the project root.** These were
  the most common inventions; they conflict with the methodology's
  `project → arc → slice → step` vocabulary and route artifacts away from
  the scale they actually belong to.
- **`milestones/`** for ledgers. The methodology's vocabulary changed in
  v1.1 — the level-1 ledger-bearing unit is **slice**, not milestone — and
  the ledger lives inside the slice directory as `ledger.md`, not under a
  top-level `milestones/` tree. See the methodology's *Version History*
  for the reconciliation.
- **One mega-file `PLAN.md` at the project root holding all arcs, slices,
  and ledgers.** The artifact set is per-slice for a reason: each slice's
  five documents are a coherent unit, and merging them across slices
  prevents independent verification, independent close, and independent
  re-read.
- **Per-author or per-session subdirectories.** `claude-a/`, `claude-b/`,
  `session-2026-06-18/` — the artifact is owned by the slice or arc it
  belongs to, not by who or when wrote it. Authorship belongs in the file
  header, not the path.

If any of these are *already present* in a project — perhaps from earlier
work, perhaps from a tool that did not see this document — name the
dissonance to the operator before either adopting the existing convention
or migrating to the canonical layout. Silent migration of an in-flight
project's layout is its own failure mode.

---

## Part IV — When to update this document

This document should change when:

- The methodology's *A default layout* section changes. The two stay in
  sync; the methodology owns the abstract structure, this document
  carries the operational defaults and the confirmation protocol.
- An anti-pattern recurs across more than one project. Add it to Part III
  with a name and a recognisable shape — the goal is to make the
  failure mode visible enough that the next session refuses it on
  recognition.
- The deferred categories above (project-scoped prompts, upstream
  contribution drafts, coverage reports, scratch) acquire settled
  defaults — likely alongside the broader epic/project-organisation rev
  this document is waiting for. Add them to Part II with the same
  shape as the slice/arc subsection, and update the scope note.

Treat updates to this document like methodology updates: dated, disclosed,
with the rationale preserved. *Spec-keeping for the layout spec itself.*
