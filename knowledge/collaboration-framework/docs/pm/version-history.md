# Version History

### Version 2.7 — September 2026

Routed CC, CDC, and Operator terminology to
[`../AI-ENGINEERING-METHODOLOGY.md#notes-for-codex`](../AI-ENGINEERING-METHODOLOGY.md#notes-for-codex)
as the current collaboration-framework source of truth. The
project-management wayfinder now avoids carrying partial local definitions
while preserving canonical filenames, artifact homes, and Expedited Mode
behavior.

### Version 2.6 — September 2026

Added **Expedited Mode** to the project-management wayfinder. When the
operator asks for this mode, CC commits the explicit file list after his close
packet, CDC commits verification and planning updates separately, slices close
as soon as evidence is reproduced, the next slice opens immediately after
slice close, and final-slice closure proceeds through formal arc close before
opening the next roadmap-provided arc and first slice.

This is a speed mode, not a weaker verification mode: it keeps explicit commit
scope, CDC reproduction of evidence, bottom-up slice/arc closure, and
operator-visible reports.

### Version 2.5 — August 2026

Added `sliceNN-<slug>/artifacts/` as the default home for durable artifacts
produced by a slice. The operator can override the location, but the override
must be explicit in `slice-plan.md`, repeated in `cc-prompt.md`, and verified at
slice close through the artifact inventory in `closing-report.md` and
`cdc-verification.md`.

Updated the canonical planning-worktree tree, top-down planning rules, slice
closing rules, confirmation-protocol example, anti-pattern list, and maintenance
notes. The change distinguishes the five per-slice Markdown documents from
slice-produced work artifacts so planning records and output evidence do not
compete for the same term.

### Version 2.4 — August 2026

Changed the canonical ledger layout so **every scale gets a dedicated
`ledger.md` file**. Project ledgers now live beside `project-plan.md`, arc
ledgers live beside `arc-plan.md`, and slice ledgers continue to live beside
`slice-plan.md`. This replaces the v2.1 transitional "ledger section inside the
plan file" arrangement for projects and arcs.

Updated the canonical planning-worktree tree, top-down planning rules,
confirmation-protocol example, and anti-pattern list to keep plan files focused
on scope/sequencing while ledger files carry acceptance and composition rows.

### Version 2.3 — August 2026

Split the long project-management monolith
([docs/PROJECT-MANAGEMENT.md](../PROJECT-MANAGEMENT.md)) into focused files under
`docs/pm/`, preserving the original part boundaries. The root file is now a
wayfinder with a required load set, a split-file index, and minimum-context
shortcuts for common operations. This keeps `PROJECT-MANAGEMENT.md` as the
entry point while reducing the context load for LLM sessions that only need one
piece of the project-management discipline.

- Refreshed the worked example after the v2.3 split so it teaches the general
  project-management flow rather than documenting the `odm` tool itself.

### Version 2.2 — August 2026

Changed the default project-planning substrate from an implementation-branch
`docs/design-vX.Y.Z` tree to a dedicated orphan `planning` branch mounted as a
Git worktree. The default project directory now follows the same convention as
arcs and slices: `projectNN-<slug>`. Added the planning worktree discovery and
creation rules, the `projectNN-<slug>` naming rule, project metadata fields for
`depends-on` / `blocks` / `related`, and confirmation-protocol language that
records the chosen planning branch, worktree, and project directory in local
instructions. Also renamed the slice plan-of-record from `slice-doc.md` to
`slice-plan.md`, matching `project-plan.md` and `arc-plan.md`.

This rev was catalysed by the `dns` / `vault` split planning work: the old
`docs/design-v0.1.0` default repeatedly caused humans and LLMs to confuse
planning scope with release scope and to reuse product-documentation trees for
planning records. The new default makes planning docs their own branch-backed
source of truth, while project metadata carries ordering and relationship
semantics.

### Version 2.1 — June 2026

Synchronised with `LEDGER-DISCIPLINE.md` v2.0, which extended ledger discipline
from slice-only to all three scales. Added the **ledger section** to the
required contents of `arc-plan.md` (the arc ledger's composition rows, Part III)
and `project-plan.md` (the project ledger's DoD rows, Part III); noted in the
canonical planning worktree (Part II) that the arc and project ledgers live as
sections in those plan docs and close in the matching `closing-report.md`
(Option A — no new files); and tied the arc composition check (Part V) to the
arc/project ledger closure. This embedded-section layout was superseded by
v2.4, which gives every scale its own sibling `ledger.md`. The
bubble-up/close machinery is unchanged; this rev names the
verification rigor that now backs it at each scale.

### Version 2.0 — June 2026

Renamed from `ASSET-ORGANISATION.md` (v1, which covered only the slice/arc
layout and the confirmation protocol) and substantially expanded into the
framework's full project-management home. v1's scope note had **deferred**
project- and epic-level organisation "pending in-flight work on epic- and
project-level dependency tracking" — that work is the `odm` rebuild, which has
now matured through three arcs and informs this revision. v2.0 lands the
deferred layer:

- **Absorbed the scales-of-work, fundamental-unit, sizing, and default-layout
  detail extracted from [`AI-ENGINEERING-METHODOLOGY.md`](../AI-ENGINEERING-METHODOLOGY.md)**
  (which now keeps a summary and points here). The vocabulary
  (project/arc/slice/step/iteration) and the context-window basis for sizing a
  slice now live in Part I; the canonical planning worktree in Part II.
- **Added `project-plan.md`** as the project-level plan-of-record (the arc
  roadmap), and formalized `arc-plan.md`'s required contents (Part III).
- **Added the top-down / bottom-up framing** and *plan late, plan deep*
  (Part III).
- **Added the slice bubble-up report and check** (Part IV), including the
  explicit slice-close arc-plan-update step, carried in the existing
  `closing-report.md` / `cdc-verification.md` rather than new files.
- **Added the formal arc-close process** (Part V): an arc-level
  `closing-report.md`, the composition check, the arc bubble-up report and
  check, and the project-plan-update decision it forces.
- **Added the plan-change discipline** (make-a-change + version-history,
  Part V) generalizing spec-keeping to the plan documents themselves.
- **Extended the anti-patterns** (Part VII) with closing-without-bubbling-up,
  closing-an-arc-by-fiat, never-changing plans, and far-ahead detailed plans.
- **Added a worked example** (Part IX, the `odm` rebuild).

The confirmation protocol (Part VI) and the anti-pattern core (Part VII) carry
forward from v1 with the layout references updated to this file and to the new
`project-plan.md` / arc-close artifacts.

### Version 1 — June 2026 (as `ASSET-ORGANISATION.md`)

Established the operational companion to the methodology's *A default layout*:
the slice/arc tree, the five per-slice documents, and the **confirmation
protocol** (quote the default, name the substitutions, give the operator
proceed / adjust / override, record the choice in the project's `CLAUDE.md`).
Broader project- and epic-level organisation was deferred. Shipped bundled in
the `collaboration-framework` skill.

---

_The project-management guide is a living spec. This version: 2.7, 2026-09-01._
