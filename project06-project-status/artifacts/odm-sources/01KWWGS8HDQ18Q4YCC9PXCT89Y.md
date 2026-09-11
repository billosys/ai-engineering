---
id: 01KWWGS8HDQ18Q4YCC9PXCT89Y
number: 13
type: design
schema: design/v1.1
name: odm — Architecture & Design (v-major rebuild)
created: 2026-06-20
updated: 2026-08-02
tags:
- architecture
- design
- node-graph
- dag
- reconciliation
component: All
author: topological sort
origin: planned
reserved: false
source:
  paths:
  - docs/design/04-accepted/0013-odm-architecture-design.md
  class: odd
  normalization: trim+lf
  migrated_by: odm-migrate/1.0.0
  migrated_on: 2026-08-03
status:
  draft:
    reached: 2026-06-26
    evidence: asserted
    evidence_dates:
      asserted: 2026-06-26
---

# odm — Architecture & Design (v-major rebuild)

> SDLC step 3 output. The *how* for the rebuild whose *what/why* is fixed in
> ODD-0012 (Project Definition) and grounded in ODD-0011 (Research). Where this
> doc and 0012 disagree, 0012 wins on scope and 0011 wins on evidence; raise the
> conflict rather than silently reconciling. Authored 2026-06-20 by Claude +
> Duncan.

## 1. Thesis

`odm` is **one graph of typed nodes** persisted as markdown-with-frontmatter in
git, plus two engines that operate on it:

1. a **build system for the plan** — derive order from dependencies, answer
   *what's ready / blocked / next*, and warn on out-of-order work; and
2. a **reconciler for the state** — diff each node's *declared desired facts*
   against *observed reality* and report drift.

There is no separate "doc system" and "plan system": a design document (ODD), a
decision record (ADR), and a unit of work (slice) are all **nodes** that differ
only by `type` and by which **gate-set** governs their status. This is what makes
the tool simultaneously self-documenting and self-tracking — both fall out of one
mechanism.

The single source of truth is the **complete set of node files**. Everything else
— the rollup, any caches, the directory layout — is *derived* and regenerable.
The cardinal rule (from ODD-0011's à-la-Carte result): **a fact that is not an
edge cannot be checked.** Bias toward over-declaring edges.

## 2. The node

Every node is one markdown file: YAML frontmatter (managed, queryable metadata) +
a markdown body (the human content / way-finding text).

### 2.1 Identity

- `id` — a **ULID** (via the `ulid` crate), assigned once at creation, **never
  reused, never renumbered**. This is the only identity. All edges reference ids.
- `number` — a human-friendly integer, **metadata, not identity**. Stable, never
  reused, but carries *no ordering claim* (the lesson of "Phase 8.5"). Used for
  display and as a CLI handle.
- `name` / `title` — human label; freely editable; never affects identity or
  file location. **Names embed no metadata** (v2.2, generalizing v2.1). A name
  labels *the thing itself* — never its coordinates, nor the role of the
  document it was derived from. Specifically, names carry:
  - **no numbers or positional references** — `"Workspace scaffolding"`, not
    `"Slice 01 — Workspace scaffolding"` or `"… (Arc 06)"`; that is `number`
    plus the `part_of` tree;
  - **no document-role labels** — not `"… (plan-of-record)"`, `"… (build
    plan)"`; that is `type`, plus which plan document it came from.

  Everything in that list is *already* carried by `number`, the containment
  tree, and `type`/gates. Embedding it in the name duplicates it and goes stale
  on any renumber or re-role. **Enforcement is at mint time:** the
  `migrate`/`self-host` importer **normalizes** a derived name to this rule
  rather than copying a plan-doc heading verbatim; `odm list`'s display
  stripping is then belt-and-braces, not the mechanism.

  *Scope note:* the normalizer targets the **mechanical, unambiguous** cases —
  a leading `"<Type> NN —"` or `"… (Arc NN)"`, and the known role-suffixes
  `(plan-of-record)`, `(build plan)`. Genuinely descriptive parentheticals that
  carry meaning (e.g. `"(v-major rebuild)"`) are left to human judgment: the
  rule prohibits *metadata*, not *qualifiers*.

Commands accept a `number`, a unique `name` prefix, or a full `id` and resolve to
the `id`. The id is what appears in frontmatter and git diffs.

### 2.2 Node types

Two families, one substrate:

- **Work nodes:** `project`, `arc`, `slice`. Scope decomposition only (WBS
  100%-rule: a parent's children sum to exactly the parent — no more, no less).
  Containment is the `part_of` tree, **not** sequence. There is deliberately **no
  `step` node**: a step is a single operation, always too small to deserve a
  node/document; the urge to drill into steps is funnelled into *breadth* (more
  slices/arcs), not depth. (Supersedes the parenthetical leaf-`step` note in
  0025-§4a.)
- **Document nodes:** `design` (a design document — formerly `odd`), `research`
  (a research / literature-survey / investigation doc that *informs* decisions
  but does not govern like a design doc), `adr`/`rfc` (decision record), `note`,
  **`artifact`** (v2.4 — ODD-0025 §2.5). Long-form content; same id/edge/gate
  machinery; supersede-don't-delete. A document node is **`research` iff its
  source frontmatter `tags` include `research`**, else `design` — self-documenting,
  and robust where a title-prefix or filename rule would not be (v2.0).
  - **`artifact` (v2.4, named here; the `NodeType` enum variant + minting land in
    arc-migration-fidelity slice05):** a process-execution supporting doc
    (`ledger`, `cc-prompt`, `cdc-verification`, `closing-report`, ADR, amendment,
    UAT) — distinct from work nodes and from the governing/informing types
    (`design`/`research`/`adr`), because it carries no work-gates or ordering and
    is not itself consulted-and-decided-by like a design doc. **Containment:** an
    `artifact` is `part_of` its **nearest *modeled* scale** — a per-slice artifact
    → its slice; an arc-level or **chunk-level** artifact → its **arc**. There is
    **no `step`/`chunk` node scale** — a "chunk" (the Release-Hardening `cN-*`
    grouping) is not one of the project/arc/slice scales, and a node scale for it
    would fracture the constant vocabulary (PROJECT-MANAGEMENT Part I) this
    section already commits to for `step` (§2.2 above). ODD-0025 §2.5/§2.6.

**Display names for the two families (v2.2).** The CLI names them **`plan`**
(the work nodes — what is being built) and **`reference`** (the document nodes —
what the plan is grounded in and decided by; consulted, not executed), as in
`odm list --group plan|reference`. The *model's* terms remain **work** and
**document** (`NodeType::is_work`/`is_document`); these are the reader-facing
labels, recorded here so the two vocabularies stay explicitly paired rather than
drifting apart the way `odd` did (F-2).

`type` is fixed at creation. New types are config + a gate-set; the engine is
type-agnostic. (Open Q-1: is `type` ever mutable? Current answer: no — model a
type change as supersede-by-a-new-node.)

### 2.3 Frontmatter schema (normative)

```yaml
id: 01J9Z3K7Q2V8M4N0XF7B5C3A1D     # ULID, immutable
number: 7                           # human handle, metadata
type: slice
name: "Store layer"
created: 2026-06-20                  # also encoded in the ULID; this is the human copy
updated: 2026-06-20
tags: [store, persistence]          # optional; free-form filter labels (carried from legacy)
component: odm-store                # optional; subsystem filter (carried from legacy)
author: "Katherine Johnson"         # optional; document-node only (v2.4, ODD-0025 §2.2) — the
                                     #   source doc's original author, preserved explicitly on
                                     #   migration (not git-derived: git blame on a migrated node
                                     #   returns the migrator, not the source author)
version: "2.3"                      # optional; document-node only (v2.4, ODD-0025 §2.2) — the
                                     #   doc's own content-version marker; distinct from `schema:`
                                     #   (ODD-0020 §3), which versions the frontmatter shape
origin: planned                     # how this node AROSE: planned | discovered | amendment | authored
reserved: false                     # tentative future-work placeholder (not yet real work)
source:                             # optional; every MIGRATED node carries one (v2.4, ODD-0025
                                     #   §2.0/§2.2) — work and document nodes alike; absent on a
                                     #   hand-created node. Distinct from `origin` (why a node
                                     #   exists) and from *provenance* below (derived, never
                                     #   stored) — `source` is stored because git cannot derive it.
  paths: [docs/design-v1.0.0/arc04-index-cache/slice07-early-cutoff/slice-doc.md]
  class: slice-doc                  #   the source doc's class
  normalization: trim+lf            #   what the body-hash gate stripped before comparing
  migrated_by: odm-migrate/1.0.0    #   tool + version
  migrated_on: 2026-07-27
  # --- authored shape (origin: authored) — ODD-0026 §2.1 ---
  # class: authored                 #   marks the provenance state explicitly (never an absent block)
  # paths: []                       #   no external path — the store IS the source
  # normalization: (absent)         #   nothing to hash-normalize; there was no migration
  # migrated_by: (absent)           #   no migrating tool
  # migrated_on: (absent)           #   no migration date
  # migrated_from: []               #   OPTIONAL marker (slice02 sub-decision (i)): former
  #                                 #     source.paths, preserved on conversion — provenance kept,
  #                                 #     just no longer re-verified against
edges:
  part_of: 01J9...ARC               # single parent (containment tree)
  depends_on:
    - 01J9...AAA                     # bare id → satisfied at target's terminal gate
    - { node: 01J9...BBB, satisfied_at: tested }
  blocked_by: []
  verifies: [01J9...DOC]
  consumes: [01J9...OUT]
  affects: []                        # decision/doc → the docs it touches (0001-C5)
  supersedes: []                     # a LIST (v2.4, ODD-0025 §2.3) — { node: 01J9...OLD, kind: updates } entries; kind ∈ {obsoletes (replace), updates (amend)}; empty when none. A synthesized node may supersede many originals (many-to-one); reverse (superseded_by) stays derived, never stored, and the tooling GUARANTEES the bidirectional lineage on every synthesis (never a hand-maintained back-edge) — enforced by a `check` rule.
  tears:                             # explicitly-broken dependency edges (see §4.3); omitted when empty
    - edge: 01J9...TORN              #   the assumed `depends_on` (bare id or { node, satisfied_at })
      because: "B is assumed to ship first"   # required rationale (audited; never dropped)
status:                              # multi-gate vector; absent gate = not reached
  built:  { reached: 2026-06-12, by: "duncan", evidence: reproduced }
  tested: { reached: 2026-06-13, evidence: reconciled }
  # evidence ∈ asserted | attested | reproduced | reconciled  (0001-D3)
decomposed:                          # a parent's guarded "complete" assertion (§4.5); typed, drift-guarded
  on: 2026-06-20                     #   when the child set was affirmed complete
  children: [01J9...AAA, 01J9...BBB] #   the affirmed child ids (a later add/remove is drift)
desired_facts:                       # for the reconciler (§5)
  - id: db-wired
    describe: "prod service has DB_HOST and connects"
    probe: { kind: shell, run: "scripts/check-db.sh", expect_exit: 0 }
```

**The authored `source` shape (ODD-0026 §2.1, arc-store-as-source slice02).** `source` is never
dropped for having "nothing to migrate": an authored node (`origin: authored`) carries
`source: { class: "authored" }` with no `paths`/`migrated_by`/`migrated_on`, plus an optional
`migrated_from` marker preserving a converted node's former `paths`. `check`
(`Violation::InconsistentAuthoredSource`) enforces both directions of the agreement — `origin:
authored` requires `source.class == "authored"`, and `source.class == "authored"` requires
`origin: authored` — so neither reading drifts from the other silently. "Authored" is a provenance
*value*, never the absence of the field.

**The author-owned vs odm-owned field boundary** (ODD-0026 §2.5). The metadata an author supplies
when creating or editing a node is a strict subset of the schema: `name`/title, `type`,
`edges.part_of`, status intent, and `tags`. Everything else is **odm-owned** and never
author-settable: `id` (mint-time only), `number` (mint-time only), placement/path (derived from
type + containment), and the entire `source`/provenance record (odm-set from the migration or
authoring event, never hand-supplied). A future authoring surface (slice03) validates this boundary
before any write — a partial that tries to set an odm-owned field is rejected, not silently accepted.

Frontmatter is **emitted in a canonical field order** (round-trip stable;
`parse ∘ emit = identity` is a proptest invariant): `id, number, type, schema,
name, created, updated, tags, component, author, version, origin, reserved,
retired, source, edges, status, decomposed, desired_facts, deferred` (v2.4 adds
`author`/`version`/`source`, ODD-0025 §4) — including the edge sub-keys in the
order shown above (`part_of, depends_on, blocked_by, verifies, consumes,
affects, supersedes, tears`), which §3's table mirrors. Unknown keys are preserved,
not dropped (forward-compat).

A node may also carry an optional **`retired: { reason, on }`** marker, set by
`odm retire` — the node is withdrawn but its file is *kept* (supersede-don't-delete;
git preserves history), absent until retired. (Added in build slice A1.5; Arc 02
may fold retirement into the gate model — see Q-10.)

## 3. Edges

Edges are first-class data, stored on the **source** node's frontmatter; reverse
edges (`superseded_by`, "depended-on-by", "part-of's children") are **derived**,
never stored, so there is exactly one place to edit.

| Edge | Meaning | Forms which graph |
|---|---|---|
| `part_of` | containment; single parent | the **hierarchy tree** |
| `depends_on` | needs target satisfied before this is ready | the **ordering DAG** |
| `blocked_by` | hard external block, not a scope dependency; **withholds from `next`** | ordering gate |
| `verifies` | this node (often a doc/test) verifies target | traceability |
| `consumes` | uses a concrete output/artifact of target | ordering DAG |
| `affects` | a decision/doc affects target docs; powers the stale-doc-vs-decision check (0001-C5) | traceability |
| `supersedes` | lineage; a **list** (v2.4, ODD-0025 §2.3) of `{ node, kind: obsoletes\|updates }` entries — a synthesized node may supersede many originals; old node(s) stay | lineage chain |
| `tears` | a `depends_on` we have *deliberately* assumed (cycle break) | annotation |

**Bidirectional lineage is tooling-guaranteed, never hand-maintained (v2.4).**
`superseded_by` stays **derived**, never stored (unchanged) — but the *tooling*
(the synthesis command) must guarantee, on every synthesis, that every
`supersedes` target is reachable in reverse, and a `check` rule verifies it. A
hand-maintained back-edge is exactly the kind of thing that drifts silently;
this closes that gap for the many-to-one case `supersedes`→list introduces.

The **ordering DAG** = `depends_on` ∪ `consumes` (∪ `blocked_by` as a soft gate).
`part_of` is a separate tree (containment ≠ sequence). `supersedes`/`verifies`
are tracked but don't drive ordering.

## 4. The graph engine (`odm-graph`)

Pure algorithms over abstract `(NodeId, EdgeKind)` — **zero domain knowledge**, so
it is independently testable. `odm-core` translates the domain model into it.

### 4.1 Derived-order queries
- `next` — nodes whose every `depends_on`/`consumes` edge is **satisfied** (§4.4),
  which have no active `blocked_by`, and which are not themselves complete: the
  ready frontier. (A `blocked_by` withholds a node from `next`; its reason surfaces
  under `blocked` — so `next` never overstates what is actionable. Q-3.)
- `blocked X` — the unsatisfied edges holding `X`, named.
- `path X [Y]` — dependency chain to `X` (or between `X` and `Y`); critical path.
- topological listing (Kahn).

### 4.2 Cycle detection
Kahn's algorithm yields cycle detection for free. Any cycle is surfaced **loudly**
and must be resolved by an explicit **tear**, never silently tolerated.

### 4.3 Tears
A tear marks one `depends_on` edge as *deliberately assumed* (DSM "tearing"). It
is recorded in `tears:` on the source node as a typed entry `{ edge, because }`
— the assumed edge **and** its required `because` rationale (the rationale is
persisted, not merely validated). `check` fails on a cycle that has no tear;
passes once a tear is declared; and lists all active tears **with their
rationale** so assumed dependencies stay visible.

### 4.4 Satisfaction & the staleness guard
An edge `A depends_on B` is **satisfied** when `B` has reached the gate named by
the edge's `satisfied_at` (default: `B`'s type's **terminal** gate). `A` is
**ready** when all its incoming dependency edges are satisfied.

**Evidence-leveled satisfaction.** Satisfaction carries not only *whether* the
satisfying gate was reached but *how well that is known* — the gate's evidence
level (§5.1 / 0001-D3): `asserted < attested < reproduced < reconciled`. The graph
**min-propagates** evidence along dependency chains: a node's effective confidence
is the *minimum* evidence level across its transitive dependency path, so a chain
is only as verified as its weakest link. A configurable **threshold** (default
`reproduced`) defines trustworthy satisfaction; a dependency satisfied only *below*
threshold is **soft-satisfied**:

- `next` still lists the node but flags it (`⚠ dep X satisfied at evidence=attested`);
- `blocked X` names the low-evidence dependency and how to raise it;
- `check` warns on below-threshold satisfaction (and fails it in strict/CI mode).

This never *blocks* proceeding on low evidence — it refuses to let the low
confidence be *invisible*. It is the direct antidote to 0001 F2/G3 (building
load-bearing work on a *relayed belief* — the prod-DB 503) and the internal
counterpart of the cross-team guard in ODD-0017 §3.3.

The **staleness guard**: advancing a node's gates (or editing it as "work") while
any `depends_on` is unsatisfied emits a loud out-of-order warning (build-staleness
applied to the plan). Non-fatal by default; `check` can make it fatal in CI.

### 4.5 Decomposition & recomposition integrity

A leading cause of the failures behind this rebuild was the inability to *see* how
a parent decomposed into children and to *recompose* the whole from the parts.
With the single-parent `part_of` tree (Q-4) the engine has the data to make this
structural and checkable — so this is **built, not deferred** (Q-7):

- **Recomposition is total and unambiguous:** reverse-`part_of` enumerates a
  parent's complete child set; every non-root node resolves to exactly one parent;
  no orphans, no dangling parents. `show <parent>` renders the full decomposition.
- **No undeveloped stubs:** a parent-capable node (`project`, `arc`) driven into a
  working/complete gate while it has zero children is flagged.
- **Guarded completeness assertion:** a parent may affirm a typed
  `decomposed: Decomposition { on, children }` ("these children fully account for
  my scope — no missing, no extra"). The affirmed child set is recorded (an
  enrichment of the bare `decomposed: complete` scalar, realized in arc02
  slice05) so a later add/remove is detectable as drift. `check` then guards it:
  children added/removed afterward, or a parent advanced toward done without the
  assertion, flags for re-affirmation.

What the tool deliberately does **not** attempt: *automatically* detecting
semantically missing or excess scope ("did you forget a slice?"). That is a human
judgement; faking it would be confabulation. The design makes the decomposition
cheap to review and turns "100% coverage" into an explicit, drift-guarded
assertion — the cheap global review the failures needed.

## 5. Status, gates, and reconciliation

### 5.1 Multi-gate status (fully configurable)
Status is a **vector over named, ordered gates**, not a scalar. Gate-sets are
defined **per node type in `odm.toml`** (decision: configurable from day one):

```toml
[gates.slice]   # the leaf work node carries the integration gates (0011-R5)
sequence = ["planned","built","tested","deployed","verified-live","operator-confirmed"]

[gates.arc]
sequence = ["planned","in-progress","complete","verified"]

[gates.design]
sequence = ["draft","under-review","revised","accepted","active","final"]

[gates.research]
sequence = ["draft","under-review","revised","accepted","active","final"]
```

`research` **mirrors `design`** initially (operator decision, 2026-07-26). The
migrate importer maps a source doc's state directory (`01-draft`…`06-final`)
onto a gate reach, so a shared full sequence means research docs in any state
dir map with zero special-casing. A semantically tighter research lifecycle
(research docs don't really go "active") is defensible, but it would also
require constraining which state dirs research docs may occupy — tighten later
if research proves it needs its own lifecycle.

A node records which gates it has reached (with date + actor); gates are ordered
so "terminal gate" and "advance/regress" are well-defined. The old single
`DocState` becomes simply the `design` gate-set — *one* configuration, not a
privileged concept. Binary done/open is gone: "done at its layer" vs "verified
live" are now distinct gates, which is precisely the distinction that hid the
prod-DB failure.

### 5.2 Desired-state facts + probes (`odm-reconcile`)
A node may declare `desired_facts`. A `Probe` is a trait; the first impl is
`shell` (run a command, compare exit/stdout) — the freeze-harness pattern lifted
to the program level. The legacy checksum/mtime detector becomes a `file` probe.

`reconcile` diffs declared desired facts against probe results and reports
**drift**, on demand and on a schedule. It is honest **only about tracked facts**
(Terraform's lesson: you can't detect drift on what the SoT doesn't claim to
manage) — so the tool nudges enumerating integration-level facts. Drift is folded
into the rollup.

## 6. Storage & layout (`odm-store`)

- **Files are the source; `odm` is the build.** Markdown + frontmatter, git-native.
- **Path = pure function of the id:** `nodes/YYYY/MM/<ULID>.md`, where `YYYY/MM`
  is the node's **creation** month read from the ULID timestamp. Files therefore
  **never move** on retitle, reparent, or gate change → minimal git churn, O(1)
  locate from id alone (no lookup index needed). Side benefit: `find ./nodes`
  gives an at-a-glance creation/activity history across machines.
- Filenames **are** the id; humans never navigate the tree by hand (`odm list` is
  our `ls`). Hierarchy and state live in frontmatter, never in the path — we do
  **not** repeat the legacy mistake of encoding truth in directory structure.
- **Atomic writes** (write-temp-rename, carried over from the legacy state code).
- **Config:** per-repo `odm.toml` via layered search (confyg), carried over.
- **Generated rollup:** a regenerable `ROLLUP.md` (+ `--json`) — way-finding tree,
  per-node status vectors, ready/blocked sets, active tears, drift, and **deferred
  nodes with their checkable re-entry predicate** (0001-E5; *deferred surfacing lands
  in A5 — Q-A3-1: no `deferred` representation exists yet, so A3 leaves a
  defined-but-empty slot*). Never hand-edited; `odm orient` reads/produces it. Any
  on-disk cache is derived and rebuildable from the node files alone.

### 6.1 Index & cache (`odm-index`) — the read-acceleration mini-infra

Distinct from storage (which reads/writes individual node files) **and** from the
rollup (a human-facing *view*): `odm-index` is the machine-facing **mini-infra**
that makes "which files define projects / arcs / slices?" and metadata filtering
fast at scale — built on the OS filesystem and nothing else (no database, no FTS
library, no daemon). This is the "as little infra as possible — i.e. none" line.

- **First run** blocks on a full scan: walk `nodes/`, parse frontmatter, build the
  index, persist it under `.odm/` (gitignored — it is derived, never truth).
- **Subsequent runs** are incremental: load the index, then a stat-walk detects
  only *changed / new / deleted* files (mtime+size fingerprint, content-hash as
  tiebreak); re-parse only those; update and persist. Cost scales with the
  *delta*, not the corpus.
- **Self-healing:** a missing or corrupt index is rebuilt from the node files — it
  carries no authority.
- **Consumers** (`list`, search/filter, `orient`, the graph build) read the index;
  they never re-walk the tree themselves.

Deliberately **research-gated** (Q-9): change-detection correctness (git's
stat-cache and the "racy-timestamp" problem), the DB-free persistent format, and
dependency-aware invalidation of derived views each deserve a proper research pass
before code. Its own crate keeps this infra isolated and swappable.

## 7. Command surface (`odm-cli`)

Commands named after the **question**, not the mechanism. `--json` on every query
(stable, documented schemas). `--dry-run` and `--yes` on every mutator. Errors
name the exact fix (errors-as-affordances). Bare `odm` **orients** (never bare-errors).

- **Orient/read:** `orient`/`brief`, `list` (filters: type, gate, ready, blocked,
  drift), `show X` (node + edges + status vector + way-finding, one call),
  `next`, `blocked X`, `path X [Y]`.
- **Context:** `use [project|arc] X` sets the current project/arc (so
  `--project`/`--arc` need not be repeated on every call); `context` shows the
  current selection. (closes 0025-§4a gap)
- **Mutate:** `new <type> <name>` (**idempotent** describe-or-create — re-running
  describes rather than duplicating), `rename`, `set-gate X <gate>`,
  `link X <edge> Y` / `unlink`, `tear X depends_on Y --because …`,
  `supersede X --with Y`, `retire X --because …` (mark withdrawn/removed; git
  preserves history — never a destructive delete of a tracked file).
- **Integrity:** `check` (schema, link-integrity, cycles-without-tears,
  out-of-order, decomposition/recomposition integrity (§4.5), stale docs vs
  committed decisions (0001-C5, via `affects`), unreconciled drift; CI/pre-commit
  gate, exit codes), `reconcile [--schedule]`, `rollup` (regenerate).
- **Migration:** `migrate <legacy-path>` (§9).

`check` is the lynchpin: it is the framework's mechanical disciplines made
executable, so the prose rules they replace can be retired.

### 7.1 JSON output schemas (canonical)

`--json` is the machine contract the ODD-0017 export projection targets. Each
query envelope carries an additive top-level **`schema`** marker
(`"<command>/v1"`) so consumers can pin a version and detect future evolution;
the marker versions the contract **from its introduction (arc03 slice04)
forward** — the `check` envelope's two earlier unmarked evolutions (severity/code
in slice06, the `tears` array in arc02 cleanup) are pre-history. The envelopes
are serialized from the in-memory model the human renders consume (no second
derivation), and each is locked by a shape test so accidental drift fails CI.

- **`check` → `"schema": "check/v1"`.** `{ schema, ok: bool, errors: uint,
  warnings: uint, findings: [{ severity, code, node, number, name, detail, fix }],
  tears: [{ from, to, because }] }`. Additive over the prior v2 envelope — existing
  consumers are unaffected.
- **`rollup` → `"schema": "rollup/v1"`.** `{ schema, tree: [TreeNode], ready:
  [{ node, soft: [{ dep, evidence }] }], blocked: [{ node, reasons: [{ kind,
  … }] }], tears: [{ from, to, because }], provenance: { planned, discovered,
  amendment }, drift: { tracked: false }, deferred: [] }`. A `TreeNode` is
  `{ id, number, name, type, origin, status: [{ gate, evidence|null }], children:
  [TreeNode] }` (status in gate-sequence order, absent gates `null`). A blocked
  `reason` is internally tagged by `kind`: `unsatisfied` | `soft-satisfied`
  (with `evidence`, `threshold`) | `externally-blocked`. The `drift`/`deferred`
  slots are present but empty until A5 (Q-A3-1/Q-A3-2).
- **`orient` (and `brief`) → `"schema": "orient/v1"`.** `{ schema, project:
  NodeRef|null, vision: string|null, focus: { arc: NodeRef, status: [GateStatus] }
  |null, ready: […], blocked: […], integrity: [{ severity, code, who, detail }],
  drift: { tracked: false }, hint: string|null }`. `ready`/`blocked` mirror the
  rollup shapes; `integrity` carries the surfaced `check` **errors** only (the
  human view's set). In a no-current-project state `project`/`vision`/`focus` are
  `null` and `hint` names the exact fix command (never bare-errors); otherwise
  `hint` is `null`. The key set is fixed across all states.

The already-stable `list`/`show`/`context` schemas are unchanged (a `schema`
marker may be added for consistency when ODD-0017 lands).

## 8. Crate architecture

Dependency / publish order, top to bottom (mirrors the oxur umbrella pattern):

| Crate | Responsibility | Key deps |
|---|---|---|
| `odm-graph` | Pure DAG/tree engine over abstract ids: edges, topo-sort, Kahn cycles, tears, ready/blocked/path, staleness. | petgraph |
| `odm-core` | Domain model: node types, ULID identity, frontmatter schema (serde), edge & gate semantics, satisfaction, link-integrity, rollup model. | odm-graph, ulid, serde |
| `odm-store` | Persistence: layout, atomic writes, git, `odm.toml`, scan/load. | odm-core, gix, confyg |
| `odm-index` | Incremental index + cache mini-infra: stat-based change detection, DB-free persisted index, fast type/metadata lookup & filter acceleration. No FTS deps. (Research-gated — Q-9 / ODD-0014.) | odm-store, odm-core |
| `odm-reconcile` | Probe trait + shell/file probes, drift diff, schedule. | odm-core, odm-index |
| `odm-migrate` | Legacy importer → new model. | odm-store, odm-core |
| `odm-cli` | clap surface, `--json`, errors-as-affordances, output (oxur-cli/tabled). | all above |
| `oxur-odm` | Umbrella: publishes the `odm` binary; re-exports the library API. | odm-cli |

Errors carry source position where parsing frontmatter (`thiserror` in libs,
`anyhow` in the binary). 95%+ coverage target; `proptest` for invariants
(round-trip, id-uniqueness, topo-validity).

## 9. Migration (`odm-migrate`)

Map the legacy model onto the new one:

| Legacy | New |
|---|---|
| `number` (identity, reusable) | fresh **ULID** id; legacy number preserved as `number` metadata |
| `DocState` scalar | `design` gate-set position |
| state directory (`05-active/…`) | dropped (was redundant truth); state → gate |
| `supersedes`/`superseded_by` | `supersedes` edge (reverse derived) |
| dustbin / Removed / Overwritten | supersede-don't-delete + git history |
| flat doc | `design`/`research`/`adr`/`artifact` document node |
| `author` | typed `author` field (v2.4) |
| `version` | typed `version` field (v2.4) |

The importer is **idempotent** and `--dry-run`-able; it never deletes legacy
files (git preserves history). Once it can import odm's own `docs/`, `odm`
self-hosts and these design docs move under `nodes/` (the loop closes).

**Migration is strictly 1:1 and verbatim, hard-gated (v2.4, ODD-0025 §2.1 —
arc-migration-fidelity).** A migrated node's body **is** its source body: the
importer performs **no body transformation** — no synthesized `# {name}`
heading, no header injection (the transform that produced odm's own 44 stub
bodies at self-host cutover). Migration computes `sha256(normalize(source))`
and `sha256(normalize(node))` (`normalize` = trim + CRLF→LF) and **hard-fails**
on mismatch — a migration-time-only invariant; no hash is stored, since content
is allowed to change afterward (e.g. Version-History sections). Every migrated
node additionally carries a `source` sub-map (§2.3) recording where its content
came from, and re-running does not repair an already-migrated node
(create-or-skip on `(type, number)`) — a `check` finding on that node's staleness
is repaired by an explicit **update-in-place** operation (arc-migration-fidelity
s04), which matches an existing node to its source by structural coordinate,
rewrites body + `source` in place, and preserves `id`/`edges`/`status`.
**Synthesis** (merging several source docs into one node) is explicitly **not**
migration — it is a separate, later step that mints a new node **superseding**
its sources (§3), keeping this hash gate exception-free.

## 10. Decisions & open questions

**Decided** (rationale above): unified node graph · **no `step` node** (funnel to
breadth, not depth) · ULID via `ulid` crate · `nodes/YYYY/MM/<ULID>.md`
creation-time sharding · filenames are ids · configurable per-type gate-sets ·
edges on source + derived reverse · ordering DAG = depends_on ∪ consumes ·
explicit tears for cycles · `supersedes` carries `obsoletes`/`updates` kind
(0011-R6) · `tags`/`component` retained · `provenance` split into `origin` +
`reserved` · **git via a pure-Rust library, not shelling out** (Q-2) ·
**`odm-index` is its own crate** — incremental index/cache mini-infra (Q-9) ·
command surface adds current-context (`use`/`context`), `retire`, and idempotent
describe-or-create (closes 0025-§4a/§4c gaps) · git = `gix` (Q-2) · `blocked_by`
withholds from `next` (Q-3) · decomposition/recomposition integrity built (§4.5,
Q-7) · the framework's mechanical PM layer is extracted into a standalone skill
that defers to `odm` (§11) · evidence-level on gate transitions, an `affects` edge
+ stale-doc-vs-decision check, and a deferred re-entry predicate (from post-mortem
0001 — D3/C5/E5) · evidence-leveled satisfaction with a threshold + min-propagation
(§4.4) — the internal counterpart of ODD-0017 §3.3.

> **Terminology (v2.4 adds a third axis — ODD-0025 §2.0):** *provenance* is
> reserved for the **derived lineage** — git history + the `supersedes` chain +
> gate-reached timestamps — never a stored scalar. `origin` (§2.3) is *why* a
> node exists (`planned`/`discovered`/`amendment`). `source` (§2.3, new) is
> *where a migrated node's content came from* — stored, because git cannot
> derive it (after migration, git blame returns the migrate commit, not the
> original path or author). Three distinct axes; only `source` is stored
> alongside `origin` — `provenance` stays derived-only.

**Open / resolved:**
- **Q-1** `type` immutability — **agreed: immutable** (model changes via supersede).
- **Q-2** Git via a Rust library, no shelling out — **decided: `gix`** (pure-Rust
  gitoxide; no C/libgit2 dependency — fits the minimal-infra goal).
- **Q-3** **Decided:** a `blocked_by` edge **hides** a node from `next` (so `next`
  never overstates actionability); the reason surfaces under `blocked`.
- **Q-4** Multi-parent containment — **agreed: not needed**; `part_of` is a tree.
- **Q-5** Rollup granularity/perf at scale — **TBD by observed need + data.**
- **Q-6** Month-shard key — **agreed: creation-time**; update-time is metadata
  (`updated:`).
- **Q-7** WBS 100%-rule as a `check` — **reframed & adopted (not deferred):** the
  part that bit us — *seeing* the parent→children decomposition and *recomposing*
  the whole — is structural, and we have the data, so it's built (§4.5: total
  recomposition, no-orphan/no-stub checks, drift-guarded typed `decomposed:
  Decomposition { on, children }` assertion). Only *automatic semantic*
  missing/excess-scope detection stays out (a
  human judgement; faking it = confabulation).
- **Q-8** Explicit entry-gate (Definition-of-Ready) distinct from
  dependency-readiness — **agreed: deferred.**
- **Q-9** Index/cache mini-infra (`odm-index`) — **research-first.** Scope:
  stat-based incremental change detection (git stat-cache / "racy-git" lessons), a
  DB-free persistent index format, dependency-aware invalidation of derived views,
  and filter/sort acceleration with **no FTS dependency**. Forthcoming research ODD
  (proposed **0014**) before implementation.
- **Q-10** Retirement representation — currently an optional top-level `retired: {
  reason, on }` field (build slice A1.5, since gates don't exist yet). Arc 02 may
  fold it into the gate model (a `withdrawn`/`retired` gate). Decide when gates land.

## 11. Scope beyond the engine, and next SDLC step

Two workstreams ride alongside the engine:

- **`odm-index` research → ODD-0014** (Q-9), in parallel — the index/cache
  mini-infra's correctness (git stat-cache / "racy-timestamp", DB-free persistence,
  dependency-aware invalidation) deserves a cited research pass before code.
- **Project-management skill overhaul** (in `billosys/ai-engineering`): the
  collaboration-framework's *mechanical* PM convention is extracted into its own
  skill that the framework references and defers to. On odm's release, most of that
  prose becomes "when you need to X, run `odm <cmd>`" entries paired with BAD /
  DON'T-DO counter-examples, seeded by a compiled list of the prior project's
  missteps (the failures that triggered this effort). This is the concrete form of
  bootstrap §6 ("retire mechanical prose → `odm check`"); it depends on a stable
  command surface (A1–A3) and lands as/after the migration+retirement arc.

**Next SDLC step:** the arc/slice breakdown (its own ODD). MVP = Arcs A1–A3
(substrate + DAG/gates + rollup/orient). Build each slice with a ledger; self-host
once A1–A3 land.

## Version History

### v2.6 — 2026-08-03 — arc-store-as-source slice02: `origin: authored` + the author/odm boundary

Adds `authored` to the `origin` value set (§2.3): a node born in the store, never pulled from an
external file. `source` is reaffirmed as enduring provenance, kept for every node that has ever
carried one — "authored" is `source.class`'s explicit value for a store-born node (no `paths`, no
`migrated_by`/`migrated_on`), never the absence of the `source` block. An optional
`source.migrated_from` marker preserves a converted node's former `source.paths` without
re-verifying against it. `check` (`Violation::InconsistentAuthoredSource`) enforces the two-way
agreement between `origin` and `source.class`. Also records the author-owned vs odm-owned field
boundary (ODD-0026 §2.5) that a future native-authoring surface (slice03) validates before every
write. Surfaced by: ODD-0026 §3 (design basis), implemented arc-store-as-source slice02.

### v2.5 — 2026-07-29 — L-8b: `state` corrected to Accepted (release-gate housekeeping)

**`state: Draft` → `Accepted`.** L-8 (`arc-release-hardening/uat-coverage-audit.md` §L-8) flagged that
this document's `state:` frontmatter — its **authority**, per §9's own model (a design doc's authority
is its `state:`-derived gate reach, not its directory) — had drifted from what its own history already
shows: this doc's own amendments (0019/0020, both `Accepted`, both applied by real, shipped slices —
v2.4 above) already assume ODD-0013 itself is settled, normative architecture, not an open draft. A
`Draft`-labeled document cannot correctly be amended by `Accepted` documents; the amendment chain is
itself the evidence the label was stale. Corrected as a pre-release housekeeping item
(arc-migration-fidelity **s11**, L-8b — reconcile before v1.0.0 ships), folding in the 0019/0020
amendment context per L-8b's instruction. **Doc-tree only**: this file is relocated
`01-draft/` → `04-accepted/` in the same change (`git mv`, history preserved) so the browsable view
agrees with the corrected `state:`. The corresponding **node's** gate vector is not touched here — that
is **s12**'s reconcile, not this edit's.

### v2.4 — 2026-07-27 — Migration Fidelity amendments (ODD-0025 §4)

Applied by arc-migration-fidelity slice03 (fidelity-core), specified by ODD-0025
(slice02, Accepted). **§2.2:** names `artifact` for the document family (a
process-execution supporting-doc type — `ledger`/`cc-prompt`/`cdc-verification`/
`closing-report`/ADR/amendment/UAT; `part_of` its nearest *modeled* scale;
explicitly no `step`/`chunk` node scale). **§2.3:** adds typed `author`/`version`
(document-node only) and `source` (every migrated node, work and document alike)
to the normative frontmatter + canonical field order. **§3:** `supersedes`
becomes a list (many-to-one synthesis support); `superseded_by` stays derived
but its bidirectional reachability is now tooling-guaranteed + `check`-verified,
never hand-maintained. **§9:** replaces the terse legacy-map with the 1:1
verbatim, hard-body-hash-gated migration semantics, the `source` record, and the
update-in-place repair vector — the mechanism that fixes the 44 stub bodies
self-host cutover produced. **§10 Terminology** gains `source` as a third,
deliberately-distinct axis alongside `origin` and the unchanged derived-only
`provenance`. Documentation only in this amendment — the `artifact` `NodeType`
enum variant, its minting, and the `supersedes`-list's actual `Vec` type change
in code are arc-migration-fidelity s05/s06, not s03.

### v2.3 — 2026-07-26
**§2.1 naming rule generalized:** from "names don't embed numbers" (v2.1) to **"names embed no
metadata"** — names also carry no document-role labels (`(plan-of-record)`, `(build plan)`).
**Enforcement moves to mint time**: the `migrate`/`self-host` importer normalizes a derived name
instead of copying a plan-doc heading verbatim, so `odm list`'s display stripping (F-6) becomes
belt-and-braces rather than the mechanism. The scope note is deliberate — the normalizer handles
the mechanical cases only; a descriptive parenthetical like `"(v-major rebuild)"` is a
*qualifier*, not metadata, and stays. Surfaced by: RH UAT **F-18** (33 of 60 node names carried a
role-suffix inherited from a plan-doc H1). Realized in RH chunk **C-5** (which absorbed the
standalone C-7); amendment stub `C-7-amendment-ODD-0013.md`.

### v2.2 — 2026-07-26
Display names recorded for the two node families (§2.2): the CLI calls work
nodes **`plan`** and document nodes **`reference`** (`odm list --group`), while
the model keeps *work*/*document*. Paired explicitly so the UI vocabulary cannot
drift from the model unnoticed — the failure mode F-2 caught with `odd`.
Surfaced by: an operator request during RH C-3 review.

### v2.1 — 2026-07-26
Naming convention added (§2.1): **names do not embed numbers** — a
number-reference in a name goes stale on any renumber and duplicates `number`
plus the containment tree. `odm list` de-numbers on display (RH C-3 / F-6);
existing stored names are left alone until a re-`self-host` regenerates them.
Surfaced by: RH UAT **F-6**. Realized in RH chunk **C-3**.

### v2.0 — 2026-07-26
Node-type taxonomy: renamed document node `odd` → `design` (§2.2); added a
`research` document type for investigation / literature-survey docs. Gate-sets
(§5.1): `[gates.odd]` → `[gates.design]` (unchanged sequence); added
`[gates.research]`, mirroring `design` initially (operator decision — see the
rationale in §5.1). Classification: a document node is `research` iff its source
`tags` include `research`, else `design`. Migration table (§9) updated for both.
Surfaced by: RH UAT **F-2** (`odd`→`design`) + **F-3** (add `research`).
Realized in RH chunk **C-2**; amendment stub `C-2-amendment-ODD-0013.md`.

### v1.9 and earlier — 2026-06-20 … 2026-06-26
Authored and revised during the v-major rebuild's SDLC step 3 (no version-history
section existed before v2.0; earlier revisions are in git history).
