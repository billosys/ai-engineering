---
id: 01KZ321ERY0Y6PTRDQ83VF4BMX
number: 26
type: design
schema: design/v1.1
name: Store-as-source-of-truth & native authoring — authored planning nodes, the metadata/body channel split, and the JSON/TOML authoring contract
created: 2026-08-03
updated: 2026-08-03
tags:
- store-as-source
- native-authoring
- provenance
- source
- origin
- metadata
- toml
- json
- arc-store-as-source
component: odm-core; odm-migrate; odm-cli
author: Duncan McGreggor
version: '1.1'
origin: planned
reserved: false
source:
  paths:
  - docs/design/04-accepted/0026-store-as-source-model.md
  class: odd
  normalization: trim+lf
  migrated_by: odm-migrate/1.0.0
  migrated_on: 2026-08-03
status:
  accepted:
    reached: 2026-08-03
    evidence: asserted
    evidence_dates:
      asserted: 2026-08-03
  draft:
    reached: 2026-08-03
    evidence: asserted
    evidence_dates:
      asserted: 2026-08-03
  revised:
    reached: 2026-08-03
    evidence: asserted
    evidence_dates:
      asserted: 2026-08-03
  under-review:
    reached: 2026-08-03
    evidence: asserted
    evidence_dates:
      asserted: 2026-08-03
---

# Store-as-source-of-truth & native authoring — authored planning nodes, the metadata/body channel split, and the JSON/TOML authoring contract

> **Arc:** Store-as-source-of-truth & native authoring (`arc-store-as-source`), **slice 01 — the model**.
> This ODD **decides**; it writes no code and mints no nodes. Its decisions are the model the arc's
> implementation slices build against: **s02** self-sourced planning nodes, **s03** native authoring
> commands, **s04** cutover. Decisions were drawn and ratified in the CDC/operator decision session of
> **2026-08-02 / 2026-08-03** (forks A, B, D, E ratified; fork C recorded as already-settled).
>
> **State: Accepted (2026-08-03).** All five forks are ratified and recorded, and the operator reviewed
> and accepted this document. Slice 01's exit criterion (`ledger.md` D1-1) is met. The amendments this
> ODD specifies (sec. 3) are applied by later slices, not here.

## 1. Context

Migration Fidelity closed with the corpus faithfully in the store: odm's planning nodes live on the
orphan `odm` branch, byte-faithful to their `./docs` sources, `odm check` clean. But the store is not yet
*authoritative* — it is a **faithful mirror**. Today every planning node still carries a `source.paths`
pointing at a `./docs` file, and that file is where authoring actually happens: you edit the markdown in
`./docs`, run `migrate`, and odm projects the change into the store. The store copy and the `./docs` copy
exist **simultaneously** — the same planning document lives in two places at once (e.g. `project-plan.md`
is the `source.paths` of 52 store nodes; `CDC-SESSION-BOOTSTRAP.md` of 6). That double-bookkeeping is the
"training wheels": odm cannot yet author its own planning corpus, so the corpus is authored the old way
and mirrored in.

Two things follow. First, **odm has no command to author or edit a node body** — `node new` mints
frontmatter and a stub, not content; there is no `node edit`. The only real authoring surface is a text
editor on the `./docs` file. Second, because `./docs` is odm's *planning* home, it cannot also be odm's
*end-user documentation* home without conflating the two.

This ODD settles the model that removes the training wheels. **The single sentence it must make true:**
*a planning node's body is authored and owned in the store, and odm no longer depends on an external
`./docs` source to hold or verify it.* Once true, `./docs` is freed for conventional end-user
documentation, and odm authors every future arc, slice, and design doc in itself.

## 2. Decision

### 2.0 Frame — this extends ODD-0025's three axes, it does not depart from them

ODD-0025 §2.0 keeps three provenance-adjacent axes distinct, and this ODD works **entirely within that
frame**:

- **`origin`** — *why* a node exists (`planned` / `discovered` / `amendment`). A stored scalar.
- **`source`** — *where a migrated node's content came from* (path, class, normalization, migrating
  tool). Stored, because git cannot derive it after migration.
- **`provenance`** (ODD-0013) — *derived* git + supersede + gate lineage. Never stored.

An **authored node** — one born in the store, never pulled from an external file — is a new *point* in
this space, not a fourth axis and not the deletion of an axis. It is characterized by a new `origin`
value and a defined (empty-of-external-path) `source` shape. Everything below is the consequence of
placing authored nodes at that point.

### 2.1 Fork A — `source`/provenance is KEPT; "authored" is an `origin` value, not the absence of source

**Decision (ratified 2026-08-03): keep the `source` provenance record as a first-class, enduring field.
An authored node records `origin: authored` and a `source` block that carries no external `paths`.**

> **Correction, recorded deliberately (spec-keeping).** The slice-01 open set carried an earlier CDC
> *lean* to **drop external source entirely for authored nodes (A1)**. The operator overturned it:
> `source`/`source.paths` is **provenance metadata with significance and a lifetime beyond the initial
> migration** — it records where content that was *pulled into* odm came from, which stays true and
> useful long after the migration event. It is not migration scaffolding to discard. This ODD supersedes
> that lean. The root cause of the misread was an **under-specified schema** (the node-schema doc did not
> state that `source` is enduring provenance, nor that "authored" is a provenance *state*), so the fix is
> not only the decision but a schema clarification (§3) so the misread cannot recur.

Concretely:

- **Migrated / pulled-in nodes** — unchanged. `origin: planned` (etc.), full `source` record
  (`paths`, `class`, `normalization`, `migrated_by`, `migrated_on`) per ODD-0025 §2.2.
- **Authored nodes** — `origin: authored` (a **new `origin` value**, added to ODD-0013's set). The
  `source` record has **no external `paths`**; it carries `class: authored` to mark the provenance state
  explicitly (rather than an absent block, which reads as "unknown" rather than "authored in-store"). No
  `migrated_by` / `migrated_on` (there was no migration). The exact spelling is fixed in §3's amendment;
  the invariant is: *the provenance axis applies to authored nodes; its value is "authored," not "none."*

The load-bearing distinction: **`authored` is a value of provenance, never the absence of the concept.**
A future reader (human, CC, or a fresh context) must not be able to read "this node has no external
source" as "the `source` field is vestigial, drop it." §3 writes that into the schema.

### 2.2 Fork B — the body-hash gate is migration-scoped; N/A for authored nodes by construction

**Decision (ratified): the body-hash fidelity gate applies only to nodes with an external `source`
(migrated / end-user-imported / legacy). It is N/A for authored nodes — not by exception, but because an
authored node is never migrated, so the gate never fires.**

This is already consistent with ODD-0025 §2.1: the hash is a **migration-time gate only**, and **no hash
is stored** (content is allowed to change; a stored hash would be false drift). An authored node has no
migration event and no external body to prove faithfulness *against*, so there is nothing to hash and
nothing to gate. Git history on the orphan `odm` branch is the tamper record for authored content.

**No-regression clause (this is load-bearing):** for genuinely-migrated content the gate is
**unchanged** — B does not weaken migration fidelity. The gate keys off the presence of an external
`source.paths`; authored nodes simply do not present one. All *other* validation — schema, edges,
decomposition, derived order — **still applies to authored nodes in full**. "Self-sourced" removes the
migration fidelity check and nothing else.

### 2.3 Fork C — the design corpus (ODDs 0011–0025) is settled store-as-source (recorded, not decided)

The ODD corpus are design/planning artifacts **already migrated into the store** (repeatedly). They are
store-as-source like every other planning node. `docs/design/` (the ODD gate-ladder tree) and
`docs/design-v1.0.0/` (the planning tree) both delete in the **cutover (s04)**. Recorded here only so the
cutover's deletion scope is explicit — **no decision required**. (An earlier framing of this as an open
fork was a CDC error; "already in the store" settles it.)

### 2.4 Fork D — end-user `./docs` lives outside the odm planning store

**Decision (ratified): after cutover, `./docs` holds conventional end-user documentation, versioned with
the code on `release/1.0.x`, and is NOT tracked by the odm planning store.** odm tracks *planning*.
Freeing `./docs` from odm is the point of the arc. A future "docs coverage" capability, if ever wanted,
is a separate arc — not this one.

### 2.5 Fork E — the authoring/update contract: odm owns the seam; single-grammar surfaces

**Decision (ratified 2026-08-03).** The governing principle, from which the whole contract follows:

> **odm owns the seam.** Every surface odm hands an author is **single-grammar** — either pure-markdown
> **body** (no front-matter) or **structured metadata** — and odm is the *only* thing that ever fuses the
> two into the on-disk `---`-plus-body node file.

This is a direct extension of a stance odm already takes: you never write `id` / `number` / `path`,
because odm owns identity and placement. This adds "…and odm owns the YAML seam." The motivation is
concrete and empirical: **fused YAML-front-matter-plus-markdown files are where LLM authoring corrupts** —
clipped `---` fences, whitespace-significant YAML indentation drift, and wholesale rewrites that
reconstruct front-matter from memory and silently drop or reorder fields. Splitting the two channels
removes the exact surface where that corruption happens. The body (prose) and the metadata (explicitly
delimited structured data) are each individually safe to author; only their *seam* is fragile.

**The canonical metadata partial.** There is one in-memory **metadata partial** — the author-facing
fields of a node. The wire formats are I/O over it, not distinct concepts: odm accepts the partial as
**JSON *or* TOML**, dispatched on file extension (`--metadata=x.json` / `x.toml`), and **converts between
them internally** (trivial in Rust; a single canonical representation deserialized from either and
serialized to either). An LLM stubs JSON; a human writes TOML (matching odm's existing `odm.toml` /
`config.toml` idiom); the semantics are identical. odm may later emit metadata in either format
(`node show --meta`, `node edit --meta`) from the same canonical partial.

**The author-vs-odm field boundary.** The metadata partial carries **only author-owned fields** — title
/ `name`, `type`, `edges.part_of`, status intent, tags. odm **mints and owns** `id`, `number`,
placement/`path`, and the **`source`/provenance** record (per §2.1, authored provenance is odm-set, never
author-supplied). odm merges the author's partial over the odm-owned skeleton; a partial that tries to
set an odm-owned field is rejected (§ below). This boundary is part of the schema (§3) so it is not
re-derived per workflow.

**Validate-before-write (an asymmetry that is a feature).** odm validates the metadata partial against
the schema **before writing the node**, and fails loudly on a bad or forbidden field — so a malformed
authoring input can never produce a half-broken node on disk. The **body**, being pure prose, is never
parsed as structured data and so **cannot break node parsing at all**. Structured channel validated hard;
prose channel unvalidated; that asymmetry is the payoff of the split.

**The command surface (contract sketch — s03 specifies and builds the detail).** Two creation workflows
and a channel-addressed edit surface, all instances of the one principle:

- **Create, one-shot dual-source:** `odm node new <type> <name> --metadata=<file.json|.toml> --content=<file.md>`.
  You supply both channels separately; odm fuses, mints identity/placement/provenance, validates, writes.
- **Create, skeleton-then-grow:** `odm node new <type> <name>` mints a node with odm-owned front-matter
  and an empty/stub body, returning the ref. The body is then filled incrementally (below). Stub status
  tracks "body not finished yet" — this closes the `undeveloped-stub` gap.
- **Edit metadata, field-addressed:** `odm node set <ref> <field> <value>` (e.g. `status`,
  `edges.part_of`, `tags`). The author names a field; the `---` block is never in the editable surface.
- **Edit body, whole or sectioned:** `odm node set-body <ref> --from-file <md>` (or `--body`) replaces
  the whole body as pure markdown; `odm node edit <ref> --section "## Heading" --from-file <md>` replaces
  one heading-anchored section (robust for large docs — anchored on markdown headings, which LLMs handle
  natively, not on line numbers).
- **Interactive, split surfaces:** `odm node edit <ref> --body` opens **only** the stripped body in
  `$EDITOR` (odm re-attaches front-matter on save); `--meta` opens **only** the metadata as structured
  text. Even the interactive path never exposes the seam.
- **Always-works fallback:** hand-edit the store `.md` and `odm check`. Never removed; it is the floor
  under every command above.

The human ergonomics barely change (you still write markdown, and now write metadata in a clean
structured file instead of a fragile YAML header); the source of truth moves into the store.

## 3. Amendments required (specification only — applied by later slices/amendments, not here)

This ODD specifies the following changes; they are **applied** by the cited slice or by a dedicated ODD
amendment, not in this document.

- **ODD-0013 (Architecture & Design) — the node schema.** (a) Add **`origin: authored`** to the origin
  set. (b) Define the **authored `source` shape**: `source: { class: authored }`, no `paths`, no
  `migrated_by` / `migrated_on`. (c) State explicitly that **`source` is enduring provenance and
  "authored" is a provenance value, not the absence of the field** — the durable guard against the
  fork-A misread. (d) Record the **author-owned vs odm-owned field boundary** (§2.5). *(Applied by s02's
  schema work + an ODD-0013 amendment.)*
- **ODD-0025 (Migration Fidelity) — §2.0 / §2.1.** Note that the three axes now include an **authored
  origin** whose `source` carries no external path, and that the **body-hash migration gate is bypassed
  for authored nodes by construction** (they never migrate). Migration fidelity for genuinely-migrated
  content is unchanged. *(Applied by an ODD-0025 amendment alongside s02.)*
- **ODD-0013 §2.1 (names embed no metadata)** — unaffected in substance, cited to keep the naming rule
  visible: authored node names/titles carry no role metadata, same as migrated ones.

## 4. Consequences

- **The store becomes the sole home** of planning content; the `./docs` planning tree and the ODD
  gate-ladder tree both retire at cutover (s04). One copy, not two.
- **`./docs` is freed** for end-user documentation (fork D).
- **Authoring ergonomics change** for the better under LLM operation: the metadata/body channel split
  removes the fused-YAML corruption surface (§2.5). Humans gain a clean TOML metadata file; LLMs gain a
  JSON one.
- **Provenance stays first-class** (fork A): every node, authored or migrated, carries a meaningful
  `source`/`origin` record; nothing about provenance is weakened.
- **Migration fidelity is untouched** for genuinely-migrated content (fork B no-regression clause).
- **A new dependency chain:** s03's authoring commands depend on s02 having made self-sourced nodes
  legitimate, which depends on this ODD. s04 (cutover) depends on all three plus an explicit operator go.

## 5. Alternatives considered

- **A2 — repoint `source.paths` self-referentially at the store node's own file.** Rejected: it keeps a
  path that means nothing (a node pointing at itself) and a vacuous hash, and it obscures the genuine
  distinction between "pulled from elsewhere" and "born here." `origin: authored` + no external path
  states the truth directly.
- **B2 — keep a stored self-checksum on authored nodes for tamper detection.** Rejected: contradicts
  ODD-0025's "no stored hash" (content legitimately changes; a stored hash is false drift), and git on
  the orphan branch already is the tamper record.
- **Single-file YAML+markdown authoring surface** (edit the fused node file directly as the primary
  path). Rejected as the *primary* path (kept only as the always-works fallback): it is the exact
  corruption surface §2.5 exists to remove.
- **JSON-only or TOML-only metadata channel.** Rejected: JSON is best for LLM emission, TOML best for
  human authoring and consistent with odm's config idiom; supporting both over one canonical partial
  costs a trivial Rust conversion and serves both authors.

## 6. Resolutions (operator-ratified 2026-08-02 / 2026-08-03)

- **A — provenance kept.** `source` is enduring; authored nodes carry `origin: authored` + a
  no-external-path `source`; schema clarified so the earlier "drop it" lean cannot recur. *(Overturns the
  slice-01 A1 lean — recorded.)*
- **B — body-hash N/A for authored**, migration gate unchanged for migrated content.
- **C — design corpus settled** store-as-source; deletes in cutover.
- **D — end-user `./docs` outside** the planning store.
- **E — odm owns the seam; single-grammar surfaces**; canonical metadata partial with dual JSON/TOML
  I/O; author-vs-odm field boundary; validate-before-write; the create + channel-addressed-edit command
  surface (detail to s03).

## 7. Success criteria / downstream acceptance (arc ledger SS-rows made concrete)

The acceptance criteria the implementing slices inherit — these are the concrete tests the arc ledger's
SS-rows (`arc-plan.md`) now cite this ODD for:

- **SS-2 (s02):** a planning node with `origin: authored` and no external `source.paths` passes `check`
  with **no `undeveloped-stub` / missing-source / body-hash error**, while schema/edge/decomposition/order
  validation still applies. Fixture: an authored node, `check` clean.
- **SS-4 (s03):** a node body can be **created and updated via `./bin/odm`** with no hand-edit of store
  files — `node new --metadata=… --content=…`, `node set`, `node set-body`/`--section`, and
  `node edit --body/--meta` all demonstrated; the created/edited body reads back via `node show`.
- **SS-5 (no-regression):** the body-hash gate **still fails** on a genuinely-migrated node whose body
  diverges from its external source. Fork B does not weaken migration fidelity.
- **Metadata contract:** a metadata partial supplied as **either** JSON or TOML produces an identical
  node; a partial that sets an odm-owned field (`id`/`number`/`path`/`source`) is **rejected** before any
  write.
- **SS-6 (arc DoD, s04):** a fresh context authors a new arc + slice end-to-end using only `./bin/odm`,
  with no `./docs` planning tree and no hand-edited store files.

## 8. References

- **ODD-0025** — Migration Fidelity (source/origin/provenance axes; the body-hash gate). Most affected;
  amended per §3.
- **ODD-0013** — odm Architecture & Design (node schema; `origin`; names embed no metadata). Amended per §3.
- **ODD-0017** — Interop: projection out, reference-and-reconcile in. This arc is *authoring in* (the
  reverse direction); no conflict — projection-out is unaffected.
- **ODD-0022** — the odm store home (orphan branch; git as the store's tamper record — the basis for
  fork B's "git is the tamper record").
- `arc-store-as-source/arc-plan.md` (the arc); `arc-store-as-source/slice01-store-source-model/`
  (`slice-doc.md`, `ledger.md` — this ODD's open set).

## Version History

### v1.1 -- 2026-08-03 -- Accepted

Accepted by the operator. No substantive change from v1.0 Draft -- the five forks were already ratified in the 2026-08-02/03 decision session; this promotes the reviewed document from `01-draft/` to `04-accepted/` and closes slice 01 (ledger D1-1 -> reconciled). The amendments in sec. 3 (ODD-0013 schema: add `origin: authored` + the authored `source` shape + the author-vs-odm field boundary; ODD-0025: authored nodes bypass the migration body-hash gate by construction) are applied by slice 02 and dedicated ODD amendments, not here.

### v1.0 — 2026-08-03 — Draft

Authored from the CDC/operator decision session of 2026-08-02 / 2026-08-03. All five forks recorded:
A (provenance kept — **overturning the slice-01 A1 lean**, recorded as a spec-keeping correction), B
(body-hash N/A for authored, migration gate unchanged), C (design corpus settled), D (end-user `./docs`
outside), E (odm owns the seam; canonical metadata partial with dual JSON/TOML I/O; author-vs-odm field
boundary; validate-before-write; the create + channel-addressed-edit surface). Reconciled against
ODD-0025 (§2.0 axes, §2.1 gate) and ODD-0013 (schema); amendments to both specified in §3, to be applied
by s02 + amendments. **Decisions ratified; document pending operator acceptance (redline) → then promotes
to `04-accepted/` and slice-01 ledger D1-1 closes.** Surfaced by: `arc-store-as-source` slice 01.
