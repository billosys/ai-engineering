---
id: 01KYP5H4YXRJ6315906KER3BGN
number: 25
type: design
schema: design/v1.1
name: Migration Fidelity — source provenance, synthesis, artifact nodes & frontmatter fidelity
created: 2026-07-27
updated: 2026-08-02
tags:
- migration
- source
- provenance
- synthesis
- fidelity
- artifact
- coverage
- arc-migration-fidelity
component: odm-migrate
author: Duncan McGreggor
version: '1.1'
origin: planned
reserved: false
source:
  paths:
  - docs/design/04-accepted/0025-migration-fidelity-model.md
  class: odd
  normalization: trim+lf
  migrated_by: odm-migrate/1.0.0
  migrated_on: 2026-08-03
status:
  accepted:
    reached: 2026-07-27
    evidence: asserted
    evidence_dates:
      asserted: 2026-07-27
  draft:
    reached: 2026-07-27
    evidence: asserted
    evidence_dates:
      asserted: 2026-07-27
  revised:
    reached: 2026-07-27
    evidence: asserted
    evidence_dates:
      asserted: 2026-07-27
  under-review:
    reached: 2026-07-27
    evidence: asserted
    evidence_dates:
      asserted: 2026-07-27
---

# Migration Fidelity — source provenance, synthesis, artifact nodes & frontmatter fidelity

> **Arc:** Migration Fidelity (`arc-migration-fidelity`), slice 02 (the model). This ODD is the
> single authoritative model the arc's implementation slices (s03 fidelity-core, s04
> scope+repair, s05 enforcement, s06 synthesis) build against. It **decides**; it writes no code
> and mints no nodes. Decisions are drawn from `arc-migration-fidelity/design-notes.md` §2–§3
> (forks F1–F10) and s01's exact inventory (`slice01-coverage-discovery/coverage-report.md`).
>
> **Accepted 2026-07-27** — all §7 open questions confirmed by the operator (F4 normalization; the
> `artifact` node type; F10 report coverage = mint-all; `author`/`version` preserved as typed
> fields; the `source`-not-`provenance` naming; provenance typed at creation in s03).

## 1. Context

The v1.0.x self-hosting migration brought documents into the store but not *faithfully*: s01's
coverage-discovery slice produced the exact inventory — **326 source docs, 266 uncovered across
10 classes; 6/12 arc dirs + 39/44 slice dirs represented; 44 stub bodies (6 arc + 38 slice);
60/60 nodes carrying no source record.** The arc's charter is to make migration *faithful and
verifiable* — four properties, each enforced by a check rather than trusted (arc-plan
"Capability"): 1:1 verbatim bodies hard-gated; a source record on every node; frontmatter fidelity
schema-mapped; and no file left behind. This ODD fixes the **model** those checks require. The
root causes are documented (`design-notes.md` §1): `selfhost.rs` mints a synthesized stub body
instead of importing the source; the source record was designed but never implemented (the
keystone hole); and `self_host` is create-or-skip, so re-running cannot repair existing nodes.

## 2. Decision

### 2.0 Three provenance-adjacent axes, kept distinct

0013 reserves the word **`provenance`** for **derived lineage** — git history + the `supersedes`
chain + gate-reached timestamps — *"never a stored scalar"*, and records a node's **`origin`**
(`planned`/`discovered`/`amendment` — *why* the node exists), not its provenance. This ODD adds a
third, genuinely-must-be-stored axis and names it to avoid collision:

- **`origin`** (existing) — *why* a node exists.
- **`source`** (new, this ODD) — *where a migrated node's content came from* (path, class,
  normalization, migrating tool). Stored, because git cannot derive it: after migration git blame
  returns the migrate commit, not the source. **This is the sub-map `design-notes.md` §2 called
  "provenance"; renamed `source` here to keep 0013's `provenance` = derived-only reservation
  intact.**
- **`provenance`** (0013, unchanged) — *derived* git + supersede + gate lineage; never stored.

> **An authored node (arc-store-as-source, ODD-0026) is a new *point* in this space, not a fourth
> axis.** It is characterized by `origin: authored` (a new value on the existing `origin` axis) and
> a `source` record whose shape carries no external path (`class: authored`). The three axes —
> `origin`, `source`, `provenance` — are unchanged in kind; "authored" is simply the value `origin`
> and `source` take together for a node that was never pulled from an external file. See the
> ODD-0013 amendment (arc-store-as-source slice02, F-8) for the exact schema shape.

### 2.1 Migration is strictly 1:1 and verbatim, hard-gated (F2, F3, F4, F5)

A migrated node's **body is its source body**. "Body" = the text after the frontmatter fence for
frontmatter docs; the whole file for the frontmatter-less planning corpus. The importer performs
**no body transformation** — it synthesizes no `# {name} (plan-of-record)` H1 and injects no
headers. *(That transform is the root cause of the 44 stubs; removing it is a fix — F3.)*

Migration computes `sha256(normalize(source_body))` and `sha256(normalize(node_body))` and
**hard-fails** on mismatch. The gate is a **migration-time gate only**; nothing is re-verified
later, and **no hash is stored** (content is allowed to change — Version-History sections do — so a
stored hash would be a false drift signal; F5).

**Normalization (F4, confirmed):** `normalize` = **trim leading/trailing whitespace + normalize
line endings CRLF→LF**, nothing else. Any *internal* change still fails the gate (the point); line
endings are a cross-platform checkout artifact, not content. `source.normalization: trim+lf` is
recorded so the comparison stays interpretable.

> **Scope clarified (arc-store-as-source slice02, ODD-0026 §2.2): the gate applies only to a node
> with an external `source` to verify against.** An authored node (`origin: authored`) has no
> migration event and no external body to prove faithfulness against — there is nothing to hash and
> nothing to gate, **by construction**, not a special-cased exemption. `verify_body_hash` is only
> ever called from the migration/reconcile paths (`self_host`/`repair`/`mapping::backfill_source`/
> `mapping::reconcile_source`), and every one now skips an `origin: authored` node before it would
> reach the gate — the same way they skip a synthesis or retired node. **No-regression clause
> (load-bearing):** for a node that *does* carry a migration `source`, the gate is entirely
> unchanged — a drifted non-stub body still hard-fails (arc-migration-fidelity s05 F-5;
> regression-fixtured at arc-store-as-source slice02, F-7). Fork B *narrows* the gate's
> applicability; it does not weaken it for the nodes it still applies to.
### 2.2 The `source` record + preserved `author` / `version` (F5 + fidelity findings)

Every migrated node carries a **`source` sub-map**, computed at migration time:

```yaml
source:
  paths:                             # a list (1+), so synthesis (many→one) fits the same shape
    - docs/design-v1.0.0/arc04-index-cache/slice07-early-cutoff/slice-doc.md
  class: slice-doc                   # the DocClass s01 assigns
  normalization: trim+lf             # what §2.1 stripped, so the gate stays interpretable
  migrated_by: odm-migrate/1.0.0     # tool + version → pre-fix imports become queryable
  migrated_on: 2026-07-27
```

> **An authored node also carries a `source` sub-map** (ODD-0026 §2.1 — provenance is kept, never
> dropped for having nothing to migrate), but a structurally different one: `class: authored`, no
> `paths`, no `normalization`/`migrated_by`/`migrated_on` (there was no migration to record). An
> optional `migrated_from` marker preserves a converted node's former `paths` without re-verifying
> against them (arc-store-as-source slice02 sub-decision (i)). See the ODD-0013 amendment for the
> full shape; this ODD's own concern — migration fidelity — simply does not apply to it.

Separately, two fields the source frontmatter carried that the node model **must preserve as
first-class metadata** (not derive, not drop):

- **`author`** — a new typed field. The node model deliberately omitted it because 0013 treated
  authorship as *git-derived* (0002 §2.2 "query git for author/dates"). But git-derivation is
  **wrong for migrated docs** — git returns the migrator, not the original author — so the source
  `author` must be captured explicitly or it is lost. `frontmatter.rs` already carries the legacy
  `author` in `extra` with a comment that "a later slice that types the key takes it over": **this
  arc is that slice.** Typed field, populated from source frontmatter.
- **`version`** — a new typed field. The doc's own content version is **source-of-truth
  quick-access** (you read the field, you do not parse the Version-History section to learn the
  current version). It is a *different axis* from the node's `schema:` marker (0020 §3). Typed
  field, populated from source frontmatter.

Both are **document-node fields**, validated per-type (0020's shared-core + per-type-validity
model) — a `check` finding if present on a work node. They land additively via `Frontmatter.extra`
until s03 types them (Q5, confirmed: typed at creation in s03).

### 2.3 Synthesis is a separate, superseding step — never migration (F1, F2)

Merging several docs into one is **not** migration; it is a later step that mints a **new** node
which **supersedes** its sources, keeping the §2.1 hash gate exception-free (1:1 always holds for
migration).

- **`edges.supersedes` becomes a list (`Vec`)** — a synthesized node may supersede many originals.
  The reverse (`superseded_by`) stays **derived, never stored** (consistent with 0013 §3), and the
  **bidirectional lineage must be guaranteed by the tooling on every synthesis** (+ a `check`
  rule) — never a hand-maintained back-edge.
- **Synthesis type sets the verification regime:** `concatenation` **stays hash-gated** against a
  **deterministic join** (fixed order, separator, per-source `normalize`); `editorial-merge` is
  verified by supersede lineage + explicit attestation; `other` as needed.
- **Two orthogonal axes kept:** synthesis-type = *how* merged; `SupersedesKind`
  {`obsoletes`/`updates`} = *what it does to the target*.

The synthesized node's `source` records `synthesis: <type>` and the multi-element `paths`.

**Amended v1.3 (arc-migration-fidelity s15, 2026-08-01 — the project vision is reversed out of this
mechanism):** s12/s13 applied synthesis to **the project specifically** — an editorial-merge node
(a curated `# Vision` body) superseding a separately-minted 1:1 `project-plan` node. s15 reverses
that one application: the operator judged the two-node split documentation over-engineering — it
was also the direct source of a reconcile gap (the 1:1 base was structurally unreachable by
reconcile, `#1001` in the live corpus) and a fragile "already a synthesis" idempotency check. **The
project is now always exactly one node**: a faithful 1:1 migration of `project-plan.md`, reconciled
like any other plan node (§2.9). The vision is a **rendered view** of that one node (`orient`
excerpts a heading/lead section from its body), never a stored synthesis body. The general
mechanism above is **not retracted** — `concatenation`/`editorial-merge`/`other`, the
`supersedes`-list model, and the bidirectional-lineage guarantee all remain available for a
**future, genuine** synthesis (several distinct sources merged into one new node); the project
vision was simply never a good fit for it once a single-source, in-place re-cast is what's wanted.
The collapse itself is `id`/`number`-preserving (the surviving node is the former synthesis, re-cast
in place, not re-minted) and retires the node it superseded rather than deleting it.

### 2.4 Frontmatter fidelity — a schema-mapping check over originally-present fields (F5)

A migration-time, versioned mapping-equivalence check over **only the fields the source had**:

| Legacy field | Node target | Notes |
|---|---|---|
| `number` | `number` | direct |
| `title` | `name` | direct |
| `created` / `updated` | `created` / `updated` | direct |
| `tags` | `tags` | direct |
| `component` | `component` | direct |
| `author` | **`author`** (new typed field, §2.2) | preserved, not git-derived (git returns the migrator) |
| `version` | **`version`** (new typed field, §2.2) | preserved — the SoT quick-access version, distinct from `schema:` |
| `state` (`DocState`) | cumulative **gate reach** | already faithful — `mapping.rs::reach_cumulative` |
| `supersedes` | `edges.supersedes` | now a list (§2.3) |
| `superseded-by` | *derived* | never stored (0013 §3) |

The frontmatter-less planning corpus has no such fields — its metadata is structural, already
handled by `selfhost.rs`. The mapping is itself schema-versioned so it can evolve (0020).

### 2.5 The `artifact` node type for supporting docs (F9, confirmed)

The ~211 uncovered supporting docs (`ledger`, `cc-prompt`, `cdc-verification`, `closing-report`,
ADR, amendment, UAT) get a new **`artifact`** document-family node type, distinct from work nodes
and from the governing/informing types (`design`/`research`/`adr`), for process-execution
artifacts. *(Spelling: `artifact`, matching the codebase's American-spelled type identifiers.)*

- **Containment:** an `artifact` is `part_of` its **nearest *modeled* scale** — per-slice → its
  slice; arc-level and **chunk-level** → its **arc**.
- **No "chunk" node scale.** A "chunk" (the Release-Hardening `cN-*` grouping) is not one of the
  project/arc/slice scales; a node scale for it would fracture the constant vocabulary
  (PROJECT-MANAGEMENT Part I). Chunk-level artifacts attach to the arc.

### 2.6 Report self-coverage — mint all reports (F10, confirmed: mint-all)

`odm migrate --coverage` renders to stdout, redirected into `coverage-report.md`; every slice
emits `closing-report.md` / `cdc-verification.md`. All are `.md` under the doc-coverage scan root,
so once s05 wires doc-coverage into `odm check` (MF-6) they must be accounted for. **Decision:
mint an `artifact` node for every report — authored *and* generated, `coverage-report.md`
included. No exemption, no ignore rule.** "No file left behind" stays literally true; a report
node's body simply updates on regeneration (fine — §2.1 stores no hash; §2.8 update-in-place is the
mechanism). Uniform treatment, zero special-casing.

### 2.7 Containment is optional for document nodes (F7)

Some `design`/`research`/`artifact` nodes are legitimately top-level; some are `part_of` an
arc/slice. Containment is **optional** for document-family nodes, and the doc-coverage / `orphan`
check **must not** flag a legitimately top-level document node as an orphan. (s01 confirmed the
"14 floaters" are mostly the intended shape.)

### 2.8 Repair is update-in-place, not re-migration (F8)

`self_host` is create-or-skip on `(type, number)`, so re-running **skips** the 44 stubs. Repair
needs an explicit **update-in-place** op: match each existing node → its source (by structural
coordinate, since the `source` record is absent *at repair time*), write the real body + `source`
into the **same** node, hard-fail the §2.1 gate, and **preserve `id` / `edges` / `status`**. A stub
is decidable by "the body is a lone H1." (s04 implements; bodyless nodes are
deleted-then-re-migrated where update-in-place will not serve — arc-plan s04.)

### 2.9 Reconcile re-establishes fidelity to a *changed* source (arc-migration-fidelity s12)

§2.8's repair is scoped to a **stub**: a node whose body was never faithfully migrated in the first
place. It deliberately **hard-fails** (never overwrites) a non-stub node whose body no longer matches
its source — drift on an already-faithful node was, until s12, a dead end: skipped and recorded
(design/research, s09/s10) or rejected outright (work-tree, §2.8's own wording), with no path back to
fidelity. **Reconcile** is the missing operation: given a node whose source has **legitimately
changed** since it was last snapshotted (the source file was edited, not the migration broken), it
**re-snapshots the body from the current source in place** — `id`/`edges`/`status` preserved, exactly
as §2.8 already requires for repair — rather than rejecting or skipping. The §2.1 gate stays
**migration-time-only**: reconcile does not turn it into a continuous check; it simply re-runs the
same "body came verbatim from source" verification against *whatever the source currently says*, so it
always trivially holds by construction.

**The living-plan-node policy (decided, s12 F-3):** a node whose source is a still-changing document
(the arc-migration-fidelity `arc-plan.md` node is the concrete, continuously-recurring case — s08's CDC
verification first surfaced it) reconciles the **same way** as any other drifted node: to current, with
**no special exclusion**. Two things make this safe rather than a moving target: (1) the gate is
migration-time-only, so inter-reconcile drift is *by design* invisible to `check` — there is no
continuously-enforced "must match" that a living document could ever violate; and (2) at arc-close the
source has stabilized, so the final reconcile pass leaves the node genuinely faithful.

**The reconcile exclusion (amended v1.3, s15 F-3):** the **sole** exclusion is a node carrying
`source.synthesis` — ODD-0020 v1.4's key, reused here rather than a second, node-type-based rule.
Before s15 this was expressed as "the project is excluded" (a `node_type == Project` check), because
the project was, at the time, always synthesis-shaped. Now that the project is collapsed to a plain
1:1 node by default (§2.3), that blanket exclusion would wrongly leave a faithful project
unreconciled forever — so the check is keyed on the actual reason a node must never be forced through
the 1:1 gate (it is a **merge**, not a migration), which generalizes correctly: a plain 1:1 project
reconciles like any other plan node; a node that genuinely does carry `source.synthesis` (project or
otherwise) still stays excluded, exactly as before.

Moved-source re-discovery is reconcile's other half: a node whose stored `source.paths` no longer
resolves, because its source file relocated (the concrete case: arc-migration-fidelity s11's L-8b
`01-draft/`→`04-accepted/` moves), is re-found by the corpus's own identity key for that family —
`number` for design/research, the structural `(type, number)` coordinate for work-tree nodes — the
same matching `self_host`/`backfill_source` already use, so a moved file is never invisible to it.

## 3. Disambiguation — three meanings of "research"

**`docs/dev/research/`** (a source directory, 5 files) ≠ **`docs/dev/`** generally (26) ≠ the
**`research` node *type*** (a document node whose legacy `tags` include `research`, 5). Three
things sharing one word.

## 4. Amendments required (specification only — applied by s03/s05, not here)

- **ODD-0013 §2.2 (Node types):** add **`artifact`** to the document family (§2.5); state its
  process-execution role and "nearest modeled scale" containment; affirm no `step`/`chunk` scale.
- **ODD-0013 §2.3 (Frontmatter schema, normative):** add the **`source`** sub-map (§2.2) and the
  typed **`author`** and **`version`** document-node fields (§2.2) to the normative list + canonical
  field order (all ride `extra` until s03 types them). Do **not** touch the `provenance`
  terminology block — `source` is deliberately distinct (§2.0).
- **ODD-0013 §3 (Edges):** change **`supersedes` from single-target to a list** (§2.3); note the
  tooling-guaranteed bidirectional `superseded_by` invariant.
- **ODD-0013 §9 (Migration):** replace the terse legacy-map with the §2.1 semantics — 1:1 verbatim,
  no-transform, hard body-hash gate, `source`-on-migration, and the §2.8 update-in-place repair.
- **ODD-0020 §2 (Decision) + §4 (upgrade path):** add an **`artifact`** schema marker — delivered as
  **`artifact/v1.1`**, not a fresh `v1.0` (the schema-minor bump is one global generation counter
  shared across every type, ODD-0020 §5, not a per-type axis — `artifact` is introduced already at
  the then-current minor); record that adding `source`/`author`/`version` bumps the affected types'
  schema minor when typed in s03.

## 5. Consequences

- The migration capability becomes **general and re-runnable**; "no file left behind" + the hard
  body-hash gate are its acceptance tests (arc MF-1, MF-2).
- odm's own corpus goes from skeleton to faithful — the P-12 self-host DoD becomes satisfiable
  against real content (arc MF-9).
- The `source` record makes coverage an **exact set-difference** rather than the heuristic match s01
  used.
- Preserving `author`/`version` closes the code's standing "carried in `extra` awaiting typing" TODO
  and keeps the doc's SoT metadata intact.
- The `artifact` type + mint-all reports make the doc-coverage `check` (MF-6) **stable** on the
  arc's own outputs.

## 6. Alternatives considered

- **Call the stored record `provenance`** (as design-notes did) + amend 0013. Rejected: 0013
  reserved `provenance` for derived lineage with a stated rationale; `source` is a distinct axis and
  keeps that reservation clean (§2.0).
- **Reuse the `note` type for supporting docs.** Rejected: `note` is free-form; ledgers/prompts/
  reports are a numerous, structured, `part_of`-contained, process-bound cohort with their own
  lifecycle — a distinct `artifact` type reads truer and versions independently.
- **Derive `author` from git** (the 0013 intent). Rejected for migrated docs: git returns the
  migrator, not the source author.
- **Exempt `coverage-report.md` from the coverage check** (an ignore rule). Rejected (§2.6): an
  exemption is a category of "files that don't count," which undercuts "no file left behind";
  minting a node is uniform and honest.
- **Store a body hash for later drift detection.** Rejected (F5): content is expected to change.
- **A `chunk` node scale.** Rejected (§2.5): it fractures the constant vocabulary.

## 7. Resolutions (operator-confirmed 2026-07-27)

All prior open questions are closed: F4 = `trim+lf`; F9 = new `artifact` type (American spelling);
F10 = mint-all (no exemption); `author` + `version` preserved as typed document-node fields; the
stored record named **`source`** (not `provenance`, §2.0); `source`/`author`/`version` typed at
creation in s03 (not deferred to a later schema bump).

## 8. Success criteria

s03–s06 implement the whole fidelity capability against this ODD without a further model decision;
the arc's composition check (MF-9) passes against a corpus with real bodies, full coverage, and a
`source` record; and `odm check` (MF-6 wired) is green and stays green on the arc's own artifacts.

## 9. References

- `arc-migration-fidelity/design-notes.md` §2–§3 (forks F1–F10, this ODD's source).
- `arc-migration-fidelity/arc-plan.md` (the four properties; the s02 row).
- `arc-migration-fidelity/slice01-coverage-discovery/coverage-report.md` (the exact inventory).
- ODD-0013 §2.2/§2.3/§3/§9 (amended) incl. its `provenance`=derived terminology (§2.0); ODD-0020
  §2/§4 (amended); ODD-0002 §2.2 (the git-derived-author intent); ODD-0024 (ULID retained).

## Version History

### v1.4 — 2026-08-03 — arc-store-as-source slice02: the gate is migration-scoped, not removed

Clarifies that the body-hash fidelity gate (§2.1) applies only to a node with an external `source`
to verify against — an authored node (ODD-0026, `origin: authored`) has no migration event and
nothing to hash, by construction. `origin`/`source`/`provenance` (§2.0) stay three axes; "authored"
is a new point in that space (an `origin` value + a source-less `source` shape), not a fourth axis.
No-regression clause: the gate is entirely unchanged for genuinely-migrated content — a drifted
non-stub body still hard-fails (regression-fixtured at arc-store-as-source slice02, F-7). Surfaced
by: ODD-0026 §2.2 (fork B) + §3 (design basis), implemented arc-store-as-source slice02.
### v1.3 — 2026-08-01 — Accepted

**§2.3 reversed for the project specifically (arc-migration-fidelity s15, operator decision
2026-08-01):** the project vision is no longer a synthesis-node instance. s12/s13's editorial-merge
split (a curated `# Vision` node superseding a separately-minted 1:1 `project-plan` node) is
collapsed back to **one faithful 1:1 project node** — the operator judged the split documentation
over-engineering, and it was also the direct cause of two defects this slice closes: (1) the 1:1 base
was structurally unreachable by reconcile (the live corpus's `#1001`, orphaned by the blanket
`node_type == Project` exclusion), and (2) the "already a synthesis" idempotency check was fragile.
The collapse is `id`/`number`-preserving — the surviving node is the former synthesis, re-cast in
place (never re-minted), so every `part_of` child (each arc) resolves unchanged — and retires the
node it superseded (supersede-don't-delete) rather than deleting it. The general synthesis mechanism
itself (§2.3's `concatenation`/`editorial-merge`/`other` regimes, the `supersedes`-list model, the
bidirectional-lineage guarantee) is **not retracted** — it remains available for a future, genuine
multi-source synthesis; only the project's own application of it is reversed. The vision becomes a
**rendered view** of the one node (`orient`), never a stored synthesis body — until a concise
vision-view lands (LLM-command-surface arc), `orient` renders the project's full body, an accepted
interim verbosity.

**§2.9's reconcile exclusion re-keyed on `source.synthesis` (s15 F-3):** replacing the blanket
`node_type == Project` check (three sites in `selfhost.rs`) with "excluded iff the node carries
`source.synthesis`" (reusing ODD-0020 v1.4's key) — post-collapse the project carries none, so it
reconciles like any other plan node; a node that genuinely is a synthesis (project or otherwise)
stays excluded exactly as before. Extends the same "everything ingested should reconcile" principle
to the artifact and note families (`mint_artifacts`/`mint_notes` become mint-or-reconcile, s15 F-4),
closing the parallel gap where a drifted-but-already-minted supporting doc had no path back to
fidelity.

### v1.2 — 2026-07-29 — Accepted

**New §2.9 (Reconcile re-establishes fidelity to a changed source, arc-migration-fidelity s12):**
records the reconcile capability §2.8 didn't cover — a non-stub node whose source **legitimately
changed** is re-snapshotted in place (id/edges/status preserved), not hard-failed or skipped; the §2.1
gate stays migration-time-only throughout. Decides the **living-plan-node policy** (s12 F-3): a
still-changing source (the arc-migration-fidelity `arc-plan.md` node, s08's CDC finding) reconciles the
same way as any other drifted node — reconcile-to-current, no special exclusion — safe because the gate
is migration-time-only (inter-reconcile drift is by design invisible to `check`) and because the source
stabilizes by arc-close. Also records moved-source re-discovery (the s11 L-8b moves' mechanism).

**§4 amendment reconciled:** the `artifact` schema-marker line now reads `artifact/v1.1` (the
then-current global minor), not a fresh per-type `artifact/v1.0` — the schema-minor bump is one
counter shared across every type (ODD-0020 §5), so a newly-introduced type is never at `v1.0` unless
introduced at the model's inception. Closes the s09 CDC LOW finding (spec/delivery divergence on this
one line); no behavioral change. Raised by arc-migration-fidelity s10 iteration 1 (initially deferred:
editing this ODD is itself node #25's source, and no reconcile mechanism existed yet to absorb the
resulting drift) and resolved here in **s12**, which built exactly that mechanism (§2.9,
`mapping::reconcile_source`) — this edit is now a disclosed, tracked re-snapshot target for **s13**'s
live reconcile run, not a dangling drift with no path back to fidelity.

### v1.1 — 2026-07-27 — Accepted

Operator confirmed all §7 questions. Renamed the stored migration record **`provenance` → `source`**
to respect 0013's `provenance`=derived-lineage reservation (new §2.0 names the three axes:
origin/source/provenance). Promoted **`author`** and **`version`** from mapping-orphans to
first-class typed document-node fields (§2.2/§2.4) — author because git-derivation is wrong for
migrated docs and the code already stages it in `extra` awaiting typing; version because it is SoT
quick-access. F10 resolved **mint-all** (no coverage-report exemption). `artifact` spelling fixed.
Amendments (§4) and alternatives (§6) updated accordingly.

### v1.0 — 2026-07-27 — Draft

Authored in the CDC seat from `design-notes.md` §3, formalizing the decided forks (F1/F2/F3/F5/F6/
F7/F8) and recording CDC-proposed rulings on the open ones (F4/F9/F10) plus the frontmatter-fidelity
mapping and the 0013/0020 amendment specification, with five calls flagged for operator sign-off.
