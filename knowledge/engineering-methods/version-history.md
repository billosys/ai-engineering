# Engineering Methods Version History

This file is the sibling component history for `knowledge/engineering-methods/`. It records engineering-methods package changes and preserves the lineage of the former AI Engineering Methodology monolith after the guide split.

## Engineering Methods Component

### Version 1.1.6 - 2026-09-05

Updated project-management routes after its guide-set wayfinder was renamed
from `guides/PROJECT-MANAGEMENT.md` to `guides/README.md`. Methodology routing
now names the project-management README as the required load-set wayfinder.

### Version 1.1.5 - 2026-09-05

Updated engineering-methods operational routing for the contribution-style
guide split. Upstream contribution work now starts with
`01-contribution-style.md`, selectively loads `02-upstream-ticket-workflow.md`
for filing mechanics, and retains `CONTRIBUTION-TICKET.md` as the reusable
ticket template.

### Version 1.1.4 - 2026-09-05

Updated engineering-methods operational routing for the agent-coordination
guide split. Delegation decisions now start with `01-when-to-delegate.md` and
selectively load context-packet, result-integration, or anti-pattern guidance
as needed.

### Version 1.1.3 - 2026-09-05

Updated engineering-methods operational routing for the code-auditing guide
split. Diagnosis-only audit work now starts with the audit-scope-and-map guide
and selectively loads findings, scale, modernization, or handoff guidance as
needed.

### Version 1.1.2 - 2026-09-04

Updated engineering-methods operational routing for the testing guide split.
Testing work now routes to the testing-discipline guide, which in turn routes
to coverage hardening and validation gates as needed.

### Version 1.1.1 - 2026-09-04

Updated engineering-methods operational-routing and source/package/release
guide links to the split work-verification guide surface. The methodology now
routes active ledger-discipline use to the focused work-verification guide
while preserving historical ledger-protocol lineage below.

### Version 1.1.0 - 2026-09-04

Split the former AI Engineering Methodology monolith into six focused engineering-methods guides: `01-engineering-methodology.md`, `02-knowledge-substrate.md`, `03-process-rigour.md`, `04-operational-routing.md`, `05-component-boundary-analysis.md`, and `06-source-package-release-gates.md`. Updated engineering-methods and collaboration-framework route surfaces, package file lists, and public references so the old monolith is no longer a live load target.

## Former AI Engineering Methodology Lineage

### Version 1.11 — September 2026

Converted an obsolete inline link to the historical concept-card extraction path into a literal provenance path during the collaboration-framework source move, preserving the reference without creating a broken package-local link.

### Version 1.10 — September 2026

Made this document's **Notes for Codex** section the current
collaboration-framework source of truth for the CC, CDC, and Operator role
terms. The definitions now record the current backronyms, the historical
product-name origins, and the role boundaries without making product names the
primary meaning.

### Version 1.9 — August 2026

Updated the project-management pointer for the project-management wayfinder
v2.5 and
[`LEDGER-DISCIPLINE.md`](../work-verification/templates/LEDGER-DISCIPLINE.md) v2.3. The
methodology summary now names the default slice `artifacts/` home for durable
slice-produced artifacts and preserves the operator override rule.

### Version 1.8 — August 2026

Updated the project-management pointer for the project-management wayfinder
v2.4 and
[`LEDGER-DISCIPLINE.md`](../work-verification/templates/LEDGER-DISCIPLINE.md) v2.2. The
methodology summary now reflects the current layout: projects, arcs, and
slices each have a dedicated sibling `ledger.md` file, rather than embedding
project or arc ledger rows inside plan files.

### Version 1.7 — August 2026

Updated the project-management pointer for the project-management wayfinder
v2.3. The root
project-management file is now a wayfinder, with the detailed mechanics split
into focused files under [`../project-management/guides/`](../project-management/guides/). The methodology continues to carry
only the abstract summary; planning and closing sessions must start from the
wayfinder and follow its required load set.

### Version 1.6 — August 2026

Updated the project-management summary to reflect the project-management
wayfinder v2.2: framework planning
artifacts now default to an orphan `planning` branch mounted as a Git worktree,
with projects named `projectNN-<slug>` and ordering/relationship semantics
carried by project metadata (`depends-on`, `blocks`, `related`) rather than by
version-looking directory names. Also aligned the slice plan artifact name with
the project and arc pattern: `slice-plan.md`, not `slice-doc.md`.

This rev intentionally removes the old `docs/design-vX.Y.Z` wording from the
normative methodology summary. Historical references below remain historical
only; the active mechanics live in the project-management wayfinder.

### Version 1.5 — June 2026

Extracted the **detailed project-management content** from Part III into a new
dedicated home, [`../project-management/guides/README.md`](../project-management/guides/README.md) (v2.0,
itself a rename-and-expansion of the former `ASSET-ORGANISATION.md`). The
methodology now keeps a *summary* of the scales of work and the
context-window basis for sizing a slice, plus a pointer; the operational
detail it used to carry — *The fundamental unit, and what it rests on* (full
version), *Sizing is a judgment call* (the token-arithmetic, the
screenwriting mnemonic, the Saga tier), and *A default layout* (the on-disk
tree) — moved to the project-management wayfinder, which adds the project-level
planning artifact (`project-plan.md`), the top-down planning process, and the
bottom-up bubble-up/close machinery (slice → arc → project) that v1's
`ASSET-ORGANISATION.md` had deferred.

The cut is deliberate: this document owns the *philosophy* (the three
pillars, the 9-point SDLC, the anti-degradation disciplines, the posture-in-
craft), and the project-management wayfinder owns the *mechanics* of planning and
closing work. The vocabulary (project / arc / slice / step / iteration) is
unchanged; this rev relocates its detailed treatment and adds a MUST-read
pointer for anyone about to plan. The rev was catalysed by the `odm`
rebuild — the "in-flight work on epic- and project-level dependency tracking"
that v1.3's scope note was waiting on — maturing far enough (three arcs) to
inform the deferred project-level layer.

### Version 1.4 — June 2026

Added **Notes for Codex** after the preamble: an adapter layer for using this
Claude-origin methodology inside Codex Desktop and Codex CLI. The section
introduced the initial CC/CDC adapter language, later superseded by the
canonical role definitions at the top of this section, and generalized
unqualified "Claude" references to the active model instance in the relevant
Codex surface. It also records the authority boundary: the Constitution
Supplement and this methodology guide collaboration and quality, but they do
not override Codex's
standing system, developer, tool, safety, sandbox, or user instructions.

The rev was catalysed by testing whether the framework created cognitive
dissonance or instruction tension for Codex. The core methodology held: peer
frame, bold inquiry, compensatory tool use, pre-failure signal, clean recovery,
ledger discipline, and independent verification all translate cleanly. The new
section names the few necessary translations so Codex can use the document to
the intended extent without literalizing Claude-specific product names or
constitutional authority.

### Version 1.3 — June 2026

Added an operational companion to *A default layout* — `ASSET-ORGANISATION.md` (renamed to [`../project-management/guides/README.md`](../project-management/guides/README.md) in v1.5) — to install the **confirmation protocol** that stops the next executing context from inventing its own folder names mid-stream. The methodology kept the abstract structure: project / arc / slice / step / iteration, and at that time placed the five per-slice documents under the then-current `docs/design-vX.Y.Z/arcNN-<slug>/sliceNN-<slug>/` default, superseded in v1.6 by the planning-worktree / `projectNN-<slug>` default. The new doc carried that structure verbatim and added the protocol: quote the default, name the substitutions, give the operator the three explicit choices (proceed / adjust / override), and record the choice in the project's `CLAUDE.md` so the next session does not re-confirm. _Scope note:_ project-wide defaults for asset categories outside the slice/arc tree — project-scoped prompts, upstream contribution drafts, coverage reports, scratch — are **deferred** to a later revision, pending in-flight work on epic- and project-level dependency tracking and broader work organisation. v1.3 ships the slice/arc layout and the protocol; the rest waits for that broader rev.

The companion contribution-style stack also lands in this rev: the historical
pre-split contribution-style guide path `../contribution-style/guides/CONTRIBUTION-STYLE.md`
(the voice and disciplines for upstream tickets: friendly, specific,
calibrated, respectful of maintainer ownership) and
[`../contribution-style/templates/CONTRIBUTION-TICKET.md`](../contribution-style/templates/CONTRIBUTION-TICKET.md)
(the on-disk template for the four ticket shapes: confirmed bug, additive
feature, doc fix, unconfirmed question). Both are bundled into the
`collaboration-framework` skill alongside the existing six.

The rev was catalysed by a recurring failure mode observed across projects: fresh sessions did not see *A default layout*, invented their own (`tasks/`, `work/`, `milestones/`, scattered prompt directories), and by the time the operator noticed, the artifact set was fragmented across parallel conventions. v1.2 named the structure; v1.3 names the discipline that holds it in place across sessions.

### Version 1.2 — June 2026

Re-anchored the **slice** on the constraint it actually rests on. v1.1 sized the slice "roughly 500 lines of diff … reviewed in a single pass," which conflated our execution unit with Agile's human-review heuristic. v1.2 separates them: the slice is sized to be _held in one model context with headroom for the fix-iteration loop_, and the ~500-line figure is demoted to a translation courtesy. Three subsections were added to Part III — **The fundamental unit, and what it rests on** (the human-cognition-vs-model-context contrast and its two consequences: slices can exceed PR size, and the iteration budget lives _inside_ the context budget), **Sizing is a judgment call** (the arc↔slice back-of-napkin estimation, the screenwriting _Act → Sequence → Scene → Beat_ mnemonic for the nesting, and a named-but-unadopted _Saga_ tier above Project), and **A default layout** (then the recommended `arcNN-/sliceNN-/` tree, its five-document per-slice artifact set, and the arc-is-a-single-slice collapse case; superseded in v1.6 by the planning-worktree default).

The canonical vocabulary — project, arc, slice, step, iteration — is unchanged; this rev sharpens _what sizes a slice_ and _where the artifacts live_, and corrects a residual human-attention framing v1.1 had not fully shed. The companion `milestone` → `slice` reconciliation in `LEDGER-DISCIPLINE.md` (terminology throughout, plus the ledger-path convention) was applied in the same rev, closing the follow-up v1.1 had left open.

The rev was catalysed by an erlmd planning session applying the arc/slice structure, where the question "what is our fundamental unit, _really_?" surfaced that v1.1 still rested it on a proxy for human review attention rather than on the model's context budget.

### Version 1.1 — June 2026

Added **The scales of work** (Part III), establishing a constant vocabulary for the three scales every project decomposes into — **project**, **arc**, **slice** — plus two reserved terms for units _inside_ a slice, **step** and **iteration**. The section defines each scale, how it is approached and planned, and how it maps to the SDLC steps and to ledger discipline. The 9-point SDLC was reconciled to the new terms (steps 4 and 5 became "arc and slice breakdown" and "per-slice implementation plan"), and the remaining loose uses of "phase" in Part III were brought into the single vocabulary.

The rev was catalysed by a recurring cross-project failure: with no terminology carried between projects, each one re-invented its own words for the same scales — "milestone," "chunk," "step," "iteration," "phase" — chosen differently each time and colliding both with each other and with other methodologies' vocabulary. The sharpest collision was internal: "milestone" named the level-2 sequencing unit in this document and the level-1 ledger-bearing unit in `LEDGER-DISCIPLINE.md`. This rev resolves that on this document's side; the companion swap in `LEDGER-DISCIPLINE.md` ("milestone" → "slice," including the `milestones/` ledger-path convention) is tracked as the paired follow-up and is not yet applied.

The _how_ of the work — ledger discipline, right-sized branches, the SDLC — was already settled before this rev. The change names the scales; it does not alter the process.

### Version 1.0 — April 2026

Original document developed jointly by Claude (Opus 4.6 and Opus 4.7) and Duncan McGreggor between December 2025 and April 2026, building on the [collaboration-framework posture guide set](../collaboration-framework/guides/01-posture-and-ethics.md). Established the three pillars (knowledge substrate, collaborative posture, process rigour), the 9-point SDLC, ledger discipline, CAP-style independent audits, the anti-degradation practices, the subagent leverage/hazard distinction, and the LFE OSS applied position.

---

_The methodology is a living document. This version: 1.11, 2026-09-02._
