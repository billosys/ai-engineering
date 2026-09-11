---
id: 01KWWGS8HD25CQE3BX5FQEW84Q
number: 11
type: research
schema: research/v1.1
name: 'Research: A markdown/git-native, dependency-ordered planning system'
created: 2026-06-20
updated: 2026-07-26
tags:
- research
- planning
- dag
- markdown
- git-native
- dependency-order
- prior-art
component: All
author: opaque IDs
origin: planned
reserved: false
source:
  paths:
  - docs/design/06-final/0011-research-a-markdowngit-native-dependency-ordered-planning-system.md
  class: odd
  normalization: trim+lf
  migrated_by: odm-migrate/1.0.0
  migrated_on: 2026-07-29
status:
  accepted:
    reached: 2026-06-20
    evidence: asserted
    evidence_dates:
      asserted: 2026-06-20
  active:
    reached: 2026-06-20
    evidence: asserted
    evidence_dates:
      asserted: 2026-06-20
  draft:
    reached: 2026-06-20
    evidence: asserted
    evidence_dates:
      asserted: 2026-06-20
  final:
    reached: 2026-06-20
    evidence: asserted
    evidence_dates:
      asserted: 2026-06-20
  revised:
    reached: 2026-06-20
    evidence: asserted
    evidence_dates:
      asserted: 2026-06-20
  under-review:
    reached: 2026-06-20
    evidence: asserted
    evidence_dates:
      asserted: 2026-06-20
---

# Research: A markdown/git-native, dependency-ordered planning system

_Cited synthesis for the planning-process redesign. Compiled 2026-06-19 from
five parallel research streams (WBS/identity, dependency sequencing, build
systems, state reconciliation, docs-as-code/traceability/flow). Each claim is
tagged **[E]** empirical/formal/standard or **[P]** practitioner-lore. The
honesty calibration in §1 is load-bearing: much of "agile planning" is lore;
the durable parts are the formal ones._

---

## 0. The convergent finding (the one that matters)

Five separate literatures — project management (WBS/CPM), engineering design
(DSM), build systems, infrastructure reconciliation, and docs-as-code — **all
converge on the same architecture**, and it is the one your own substrate
already runs on:

> **Stable-identity nodes + an explicit dependency DAG + order *derived* by
> topological sort + per-edge staleness/reconciliation checks + a single
> *complete* graph as the source of truth.**

This is literally how `make`/Bazel work, and the formal backbone is the *Build
Systems à la Carte* correctness theorem: **a build is correct only if the
dependency set is complete; an incomplete graph silently permits running a step
before its inputs are satisfied** [E]. That is a precise description of our
failure — "prod DB provisioned + migrated, service never wired" was an edge
that no graph tracked, so nothing could flag it. The fix is not more discipline;
it is *making the dependency graph and the state explicit, complete, and
mechanically checkable.* The two halves of the system are therefore: **"a build
system for the plan"** (ordering + readiness) and **"a reconciler for the
state"** (desired-vs-actual drift).

---

## 1. Evidence strength — what to trust vs. what is lore

**Formally/empirically grounded (build on these):**
- WBS is *scope/hierarchy, not sequence* — ISO 21511:2018, PMI Practice Standard, MIL-STD-881C [E].
- Identity must be decoupled from order — protobuf field-number spec (normative: numbers permanent, declaration order irrelevant, never reused) [E]; peer-reviewed genomics evidence that position-derived IDs are unstable and must be replaced by opaque IDs [E].
- Topological sort: a valid order exists *iff* the graph is acyclic; Kahn's algorithm yields cycle detection for free [E].
- *Build Systems à la Carte* (ICFP'18 / JFP'20, Microsoft Research): scheduler × rebuilder are orthogonal axes; correctness requires a complete dependency set [E].
- Control theory: closed-loop (measure reality, correct error) is robust where open-loop drifts undetected [E].
- Little's Law (Lead Time = WIP ÷ Throughput) is a proven theorem [E] — though its transfer to knowledge work is an assumption [P].
- PERT's "merge bias" optimism is a documented empirical defect (Klingel, *Management Science*, 1966) [E].

**Peer-reviewed method, but descriptive not outcome-measured:**
- DSM (Steward 1981, IEEE TEM; Eppinger & Browning, MIT Press): dependency matrix, partitioning derives sequence, cycles surface as "coupled blocks," "tearing" makes the assume-this-dependency choice explicit [P-method]. Steward's pointed claim: **CPM cannot represent cycles; DSM can** [P].
- CPM: order is *derived* from the precedence network, not hand-assigned [P, historical].

**Lore — useful framing, weak/absent controlled evidence (adopt cautiously, don't let it drive structure):**
- Critical Chain / CCPM: reviews find *no controlled multi-project studies*; originality disputed. Weakest-supported item in the set [E-on-the-weakness].
- ADRs, RFC/RFD processes, Diátaxis, docs-as-code, Definition-of-Ready/Done, WSJF/Cost-of-Delay: influential convention, little controlled-study backing [P]. (SAFe's WSJF substitutes Fibonacci estimates for Reinertsen's real economic quantities — "precision traded for speed.")
- Contested even within DSM: *minimizing feedback/iteration does not always minimize project duration* [E] — so dependency-order is necessary but **not sufficient** for an optimal schedule.

---

## 2. Design principles, mapped to the seven requirements

**R1 — Preserve the hierarchy (project → arc → slice → step).** Use it for
*scope decomposition only*, per WBS doctrine: deliverable-oriented, obey the
**100% rule** (children sum to exactly the parent — no more, no less) [E], and
give every node a **dictionary entry** (ID + definition) [E]. Crucially, WBS
standards are explicit that the hierarchy carries **no ordering** — sequence is
a separate layer (R3). This resolves your "hierarchy vs ordering" worry directly:
hierarchy = containment, never sequence.

**R2 — Decouple identity from order.** Give each work unit a **stable, opaque
ID that never encodes position and is never reused or renumbered** (protobuf
field-number discipline [E]; surrogate-key discipline [P]; genomics stable-ID
evidence [E]). "Phase 9 / 8.5 / 10" fails precisely because the number is doing
double duty as name *and* claimed sequence. Order becomes a *derived* property
of the dependency graph, not a property of the ID.

**R3 — Dependency-ordered, with out-of-order detection.** Model dependencies
explicitly (a DSM/edge-list) and **derive** order by topological sort; cycles
are detected automatically (Kahn) and must be surfaced, then broken by an
*explicit* "tear" decision (which dependency we choose to assume) — never
silently [P-method, E-formal]. The "unsatisfied-dependency reminder" you want is
exactly a **build-system staleness check**: Make even separates *ordering* from
*staleness* via order-only prerequisites [P], proving the two are independent
concerns. The à-la-Carte theorem is the warrant: only a **complete** graph can
detect that a step ran before its inputs were ready [E].

**R4 — Single source of truth for state + drift detection.** Treat the plan as
**declared desired state** and diff it against **observed actual state** — the
Terraform `plan` / Kubernetes-reconciler model [P, primary docs]. Two hard
lessons transfer directly: (a) **you can only detect drift on what the source of
truth claims to manage** — Terraform "cannot detect drift of resources not
managed by Terraform" — so the SoT must explicitly track *integration-level*
facts like "prod service wired to its DB," or that gap stays invisible (exactly
what happened); (b) **run the diff on a schedule**, not at point-of-failure.
Control theory names the principle: a plan never diffed against reality is
**open-loop** and drifts undetected [E].

**R5 — Multi-dimensional status.** Replace binary done/open with a **status
vector across explicit gates** — e.g. `built / tested / deployed / verified-live
/ operator-confirmed` — generalizing the Definition-of-Ready (entry gate) +
Definition-of-Done (exit gate) multi-gate idea [P]. "Phase 11 store-layer: done"
masked "not wired in prod" precisely because one scalar can't express
"done-at-its-layer but not done-at-integration." Each gate is independently
reconcilable (R4).

**R6 — Machine-readable, graph-traversable relationships.** Put relationships in
**YAML front-matter** (`id`, `depends_on`, `supersedes`, `part_of`,
`verifies`) and/or wiki-style links that yield backlinks [P]; adopt ADR/RFC
linking discipline — **supersede, don't delete** (mark old, link to new) and
distinguish "Obsoletes" (replace) from "Updates" (amend) [P]. Pursue
**bidirectional traceability** (forward + backward catches orphans) **but only
for mission-critical links** — the RE literature is explicit that *complete*
traceability is economically infeasible [P/E-argument]. So: trace
dependency + verification edges rigorously; don't try to link everything.

**R7 — Keep global state cheap to load (the real prize).** The single complete
graph + a **generated rollup/index** is the cheap global view that can compete
with local task focus. The deepest transfer here is the Kubernetes
**level-triggered** reconciler: it "acts on the current state regardless of how
you got there," which is *why it survives missed events and controller
restarts* [P]. That is the direct antidote to an LLM collaborator's
context-reset tax — if the global state is a regenerable artifact derived from
the SoT, every session reloads it cheaply instead of reconstructing it by
archaeology (the mechanism behind "the vision got lost").

---

## 3. Tooling requirements (capabilities, not products)

The evidence implies a small set of mechanical capabilities. Stated as
requirements:

1. **Stable-ID allocator + link-integrity checker** — issue opaque IDs; forbid
   reuse/renumber; fail on dangling links; verify supersession chains. (R2, R6)
2. **DAG validator** — parse `depends_on` front-matter into a graph; **detect
   cycles** (Kahn) and require an explicit tear, not a silent loop. (R3)
3. **Topological-order / "what's-next" query** — derive a valid order; answer
   *what is ready* (all deps satisfied), *what is blocked and by what*, and
   *what's on the critical path*. (R3)
4. **Out-of-order / staleness guard** — when work proceeds against an unsatisfied
   dependency, emit a loud, near-automatic warning (the build-staleness
   analogue). This is the specific mechanism you asked for. (R3)
5. **State reconciler (`plan`-style diff)** — diff declared desired-state facts
   against actual/live state and report drift; **runnable on a schedule**; and
   honest only about *tracked* facts, so the SoT must enumerate integration-level
   facts. (R4)
6. **Rollup/index generator** — regenerate a single cheap global view (per-node
   status vectors across gates, blocked/ready sets, drift report) from the SoT,
   so global state is O(open-one-file), not O(archaeology). (R5, R7)
7. **Multi-gate status tracking** — status as a vector across named gates, each
   independently set and independently reconciled. (R5)

Notably, capabilities 2–4 are a **build system applied to the plan**, and
capability 5 is a **reconciler applied to the plan's state** — both paradigms
this team already operates fluently in their substrate. The markdown files are
the "source"; these checks are the "build."

---

## 4. What the evidence does NOT support (guardrails)

- Don't lean on CCPM buffer theory or WSJF scoring as *structural* drivers —
  they're weakly evidenced; use them, if at all, as advisory prioritization
  *on top of* the dependency order, never as the ordering itself.
- Dependency order alone ≠ optimal schedule (DSM duration result) — so "number
  by dependency" gives a *correct* order, not necessarily the *fastest* one;
  priority is a separate, softer layer.
- Full traceability is infeasible — scope the machine-readable links to
  dependencies + verifications, not everything.

---

## Sources

**WBS / identity:** ISO 21511:2018; PMI Practice Standard for WBS (pmi.org/learning/library/practice-standard-work-breakdown-structures-8063); MIL-STD-881C; Precedence Diagram Method (en.wikipedia.org/wiki/Precedence_diagram_method); Protocol Buffers proto3 spec (protobuf.dev/programming-guides/proto3/); genomics stable-ID paper (pmc.ncbi.nlm.nih.gov/articles/PMC4447347/); surrogate vs natural keys (baeldung.com/sql/keys-natural-vs-surrogate); magic-number anti-pattern (refactoring.guru).

**Dependency sequencing:** Steward, *The Design Structure System*, IEEE TEM 1981 (ieeexplore.ieee.org/document/6448589/); Browning, DSM review, IEEE TEM 2001 (axiomaticdesign.com/wp-content/uploads/4dsms.pdf); Eppinger & Browning, *DSM Methods and Applications*, MIT Press 2012; topological sort / Kahn (usaco.guide/gold/toposort); CPM origins (pmi.org/learning/library/origins-cpm-personal-history-3762); PERT merge bias (mba.tuck.dartmouth.edu/pss/Notes/ResearchNotes16.pdf); CCPM critique (sciencedirect.com/science/article/abs/pii/S187673541500015X).

**Build systems:** *Build Systems à la Carte* (microsoft.com/en-us/research/wp-content/uploads/2018/03/build-systems.pdf; JFP 2020 extended); GNU Make manual — Rules & Prerequisite Types (gnu.org/software/make/manual); Bazel hermeticity (bazel.build/basics/hermeticity); Ninja manual (ninja-build.org/manual.html).

**Reconciliation:** Terraform drift (hashicorp.com/en/blog/detecting-and-managing-drift-with-terraform; developer.hashicorp.com/terraform/tutorials/state/resource-drift); Kubernetes controllers (kubernetes.io/docs/concepts/architecture/controller/); controller-runtime reconcile (pkg.go.dev/sigs.k8s.io/controller-runtime/pkg/reconcile); level-triggered reconciliation (chainguard.dev/unchained/the-principle-of-reconciliation); closed-loop control (sciencedirect.com/topics/engineering/closed-loop-control).

**Docs-as-code / traceability / flow:** ADRs — Nygard (cognitect.com/blog/2011/11/15/documenting-architecture-decisions); IETF RFC process (ietf.org/process/rfcs/); Oxide RFD 1 (rfd.shared.oxide.computer/rfd/0001); ISO/IEC/IEEE 29148 traceability + bidirectional traceability (jamasoftware.com); traceability cost (arxiv.org/pdf/cs/0703012); Diátaxis (diataxis.fr); DoR/DoD (scrum.org); WSJF (framework.scaledagile.com/wsjf; blackswanfarming.com); Little's Law (kanbanzone.com).

_Source-quality caveats from the research pass: a few build-system claims were drawn from search extracts of the canonical GNU/Bazel pages rather than a full live re-fetch (fetch timeouts) — wording is consistent across sources but worth a 30-second confirmation before any formal citation. Control-theory definitions are textbook-standard; Åström & Murray, Feedback Systems (fbsbook.org) is the citable primary if needed._
