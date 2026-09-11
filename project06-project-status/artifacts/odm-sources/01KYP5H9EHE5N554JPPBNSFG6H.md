---
id: 01KYP5H9EHE5N554JPPBNSFG6H
number: 772202000
type: note
schema: note/v1.1
name: 'PM Post-Mortem — project-x: what went wrong, what to do instead'
created: 2026-06-20
updated: 2026-07-25
tags:
- skill
origin: planned
reserved: false
source:
  paths:
  - docs/dev/skill/0001-project-x-pm-post-mortem.md
  class: dev-doc
  normalization: trim+lf
  migrated_by: odm-migrate/1.0.0
  migrated_on: 2026-07-29
---
# PM Post-Mortem — project-x: what went wrong, what to do instead

> Fine-grained lessons-learned for two consumers: (1) the new **PM skill**
> (LLM-collaboration planning conventions), and (2) the **`odm` SHOULD/SHOULDN'T
> + GOOD/BAD example corpus**. Compiled 2026-06-19 by Claude (CDC/team-support
> thread) from a long project-x session. Companion to
> `planning-system-research.md` (now **ODD-0011**,
> `docs/design/06-final/0011-research-a-markdowngit-native-dependency-ordered-planning-system.md`)
> and `odm-session-bootstrap.md` (now
> `docs/dev/0025-odm-discussion-bootstrap-rebuild-planning.md`).
>
> **Stance:** this is a blameless engineering post-mortem. The project shipped a
> lot of disciplined work; the failures below are *systemic* (information
> architecture + process), not personal. LLM-side failures are included on
> purpose — they're the part you can't get from human PM experience.

---

## How each finding is structured

For every finding: **What happened** · **Why it hurt** · **Do instead** ·
**Would have caught it sooner** · **Would have prevented it at origin** ·
**odm capability** · **GOOD vs BAD** (liftable example pair).

---

## A. Identity & numbering

### A1 — The number was both name *and* claimed sequence
- **What happened:** "Phase 9" / "Phase 8.5" / "Phase 10" use the number as identity and as position-in-sequence simultaneously.
- **Why it hurt:** the moment 8.5 was inserted and 10 completed out of order, the numbers asserted an order that was false. Cross-references rotted.
- **Do instead:** give each unit a stable opaque ID; express order separately as dependency edges.
- **Caught sooner:** a "the numbering implies an order the dependency graph contradicts" lint.
- **Prevented at origin:** identity ≠ order from day one (protobuf-field-number discipline).
- **odm:** stable IDs + derived topological order.
- **GOOD:** `id: a7f3` (opaque), `name: "OTel wiring"`, `after: [c2b1]`. **BAD:** "Phase 6" where "6" silently means both "the OTel work" and "sixth in line."

### A2 — Ad-hoc bisection/letter numbering with no rule
- **What happened:** `1.5a–1.5e`, `2.1`, `8.5` — `.5` insertions and letter suffixes, no stated convention; `1.5a–e` would be clearer as `1.1–1.5` or as hierarchy.
- **Why it hurt:** readers can't tell if the suffix means hierarchy, sequence, or "inserted late." It's not obvious why `.5` vs counting up.
- **Do instead:** one canonical hierarchy (project→arc→slice→step); never encode "inserted late" in the number.
- **Caught sooner:** schema validation rejecting non-canonical identifiers.
- **Prevented at origin:** lock the vocabulary + ID scheme before work starts.
- **odm:** canonical vocabulary enforcement + ID allocator.
- **GOOD:** insert a new slice → it gets a fresh opaque ID and an `after:` edge; position is derived. **BAD:** insert work → invent "8.5" to wedge it between 8 and 9.

### A3 — Renumbering broke references; patched, not fixed
- **What happened:** OTel went "Slice 4→6"; ledger carries stale annotations like "Slice 2 at planning"; historical workbench-path refs left "as written" by convention.
- **Why it hurt:** every renumber created dangling/ambiguous references that humans then have to mentally translate.
- **Do instead:** never renumber identities; rename display labels freely.
- **Caught sooner:** link-integrity checker flags dangling/oudated refs.
- **Prevented at origin:** stable IDs mean renumbering never happens.
- **odm:** link-integrity check; IDs immutable.
- **GOOD:** rename "OTel" label; all `after: [<id>]` edges still resolve. **BAD:** renumber the slice and grep-fix references by hand (and miss some).

### A4 — Vocabulary drift ("phase" vs "arc/slice"), never retrofitted
- **What happened:** terminology evolved mid-project; old "phase" artifacts were never migrated; "Slice 4" is ambiguous (this phase's, or old Phase 4?).
- **Why it hurt:** referential ambiguity across the whole doc corpus; broke traceability.
- **Do instead:** when vocabulary changes, migrate all artifacts in one pass.
- **Caught sooner:** a vocabulary linter that flags deprecated terms.
- **Prevented at origin:** settle the vocabulary first; one term per level.
- **odm:** owns the canonical vocabulary; `migrate` command.

### A5 — No reserved namespace for parallel/future work → cross-stream blindness
- **What happened:** "Phase 10" turned out to be *something else entirely, already completed* by another stream, while "Phase 10" was also referenced as future staging-DB work.
- **Why it hurt:** two streams collided on a number; neither saw the other; planning referenced a slot that was already taken/done.
- **Do instead:** reserve future/parallel work as explicit (even tentative) nodes; make all streams visible in one rollup.
- **Caught sooner:** a global rollup listing *all* work across streams.
- **Prevented at origin:** all work — including "future" and other-stream — lives in one graph from the start.
- **odm:** `future` placeholder nodes + provenance + global rollup.
- **GOOD:** a tentative `status: future` node reserves the staging-DB work, visible to everyone. **BAD:** "we'll call it Phase 10" — and discover Phase 10 already means something else.

---

## B. Dependencies & ordering

### B1 — Dependencies were prose, not data
- **What happened:** deps lived in sentences: "consumes the MIGRATE_CMD seam (O-48)," "sequenced after Slice 5."
- **Why it hurt:** unqueryable, unenforceable; nothing could warn when violated.
- **Do instead:** dependencies as structured front-matter edges.
- **Caught sooner:** any DAG query at all.
- **Prevented at origin:** edges-as-data from the first plan file.
- **odm:** `depends_on`/`consumes`/`after` edges → petgraph.
- **GOOD:** `consumes: [o48-migrate-cmd-seam]`. **BAD:** a prose note three docs away saying "this needs the seam first."

### B2 — No dependency graph → no derived order, no ready/blocked, no critical path
- **What happened:** order was assigned by hand and by conversation, never computed.
- **Why it hurt:** no way to ask "what can I actually start now?" or "what's the longest chain to traffic-ready?"
- **Do instead:** derive order by topological sort; query readiness.
- **odm:** `next` (ready), `blocked` (+by what), `path`.
- **GOOD:** `odm next` → the set with all deps satisfied. **BAD:** "let's do Slice 6 next" because it's the next number.

### B3 — No out-of-order guard → a real dependency got parked and forgotten
- **What happened:** Phase 8.5 (automated migrations) — a genuine dependency of "prod traffic-ready" — was parked behind Phase 9 and dropped out of attention; meanwhile prod's DB story silently broke.
- **Why it hurt:** the thing that would've made migrations reliable was invisible; work proceeded as if it didn't matter.
- **Do instead:** loudly surface unsatisfied dependencies whenever proceeding past them.
- **Caught sooner:** a staleness/out-of-order warning on every session-start `check`.
- **Prevented at origin:** a complete graph makes "you're proceeding with X blocked" automatic.
- **odm:** out-of-order/staleness guard; `check` as CI/pre-commit gate.
- **GOOD:** starting traffic-readiness work → "blocked: Phase-8.5 (migrations) incomplete." **BAD:** silence; rediscover the dependency two months later by tripping on a 503.

### B4 — Sequencing re-decided conversationally, no single recorded truth
- **What happened:** Phase 8.5 was "after Slice 3," then re-sequenced "after Slice 5" — decided in chat, recorded in scattered banners.
- **Why it hurt:** "what's the current plan order?" had no single authoritative answer.
- **Do instead:** order is a property of the graph; changing it is one edge edit, visible in the rollup.
- **odm:** edges are the single source of order.

### B5 — Recency/streetlight bias in work selection
- **What happened:** work was picked by what was freshly in-context (the current slice, the prompt just written), not by dependency or priority.
- **Why it hurt:** important-but-not-in-front work (Phase 8.5, the prod 503) starved.
- **Do instead:** select from the computed ready set, ranked by an explicit priority layer.
- **odm:** `next` + optional priority annotation (advisory, on top of deps).

---

## C. State, truth, and drift (the costliest category)

### C1 — No single source of truth for state
- **What happened:** "what is actually true" was reconstructed each time by archaeology — git log + grep across milestone dirs, workbench, a parked branch, ADRs, the deployment-plan, runbooks.
- **Why it hurt:** every session re-paid a large reconstruction cost; truth was the *intersection* of many docs, so no one held it.
- **Do instead:** one generated, authoritative rollup of state.
- **Prevented at origin:** a program-level state file/rollup from day one.
- **odm:** generated global rollup/index.

### C2 — The prod-DB drift: the marquee failure
- **What happened:** prod's DB was provisioned *and migrated*, but the service was never wired to it (`DB_HOST` missing from the prod overlay). The authenticated API was fail-closed at 503 by design. Undetected for weeks.
- **Why it hurt:** a production functional outage (latent until traffic) hid in plain sight because the integration-level fact "prod service wired to its DB" was tracked **nowhere** — it only existed as the intersection of an env file, three overlays, a parked-branch banner, a runsheet, and O-44 evidence.
- **Do instead:** track integration-level desired-state facts explicitly, and diff them against reality.
- **Caught sooner:** a scheduled reconcile comparing "declared: prod wired to DB" vs live `gcloud run describe`.
- **Prevented at origin:** every env, every capability, as a tracked fact with a reconcile probe, from first deploy.
- **odm:** desired-state facts + reconciler (`plan`-style diff).
- **GOOD:** node asserts `desired: prod.service.db_wired=true`; `odm reconcile` probes live and flags the mismatch. **BAD:** "prod has a DB" is true at the instance layer and false at the service layer, and nothing notices.

### C3 — No reconciliation loop; the best pattern wasn't generalized
- **What happened:** the name-freeze / policy-freeze / render-freeze harnesses were *exactly* the right desired-vs-actual pattern — and they **worked** (caught the stale baseline, Phase-12 drift, the prod overlay divergence). But they were file-level only; never lifted to the program level.
- **Why it hurt:** the program's plan-vs-reality was open-loop even though the team had already invented the closed-loop pattern locally.
- **Do instead:** generalize the freeze-harness into a program-level reconciler.
- **Prevented at origin:** treat the plan as desired-state diffed against actual from the start (Terraform/K8s model).
- **odm:** reconciler with pluggable probes (the freeze-harness, generalized).
- **GOOD:** `odm reconcile` runs all probes on a schedule, like `terraform plan`. **BAD:** a brilliant per-file golden that never becomes a program-level check.

### C4 — Drift is only visible on tracked facts
- **What happened:** the facts that drifted (prod wiring) weren't in any source of truth, so no diff could ever surface them.
- **Do instead:** enumerate integration-level facts deliberately; the reconciler is only as honest as the fact list.
- **odm:** the tool nudges enumerating desired-state facts per node.

### C5 — Stale docs contradicting decisions, undetected
- **What happened:** the technical-design doc still says **AlloyDB** + references `alloydb.tf`, months after the 2026-06-03 decision to use Cloud SQL.
- **Why it hurt:** a new reader gets a contradictory picture; the contradiction sat unflagged.
- **Do instead:** link decisions to the docs they affect; flag docs a superseding decision touches.
- **odm:** decision nodes + `supersedes`/`affects` edges; a "docs contradicting a committed decision" check.

---

## D. Status semantics

### D1 — Binary status hid integration truth
- **What happened:** "Phase 11 store-layer: done" was true at its layer but masked "not wired in prod → 503."
- **Why it hurt:** false confidence; "done" didn't mean "works in production."
- **Do instead:** multi-gate status vectors (built/tested/deployed/verified-live/operator-confirmed).
- **odm:** status vectors per node; each gate independently set + reconciled.
- **GOOD:** `store-layer: built✓ tested✓ deployed(dev)✓ verified-live(prod)✗`. **BAD:** `store-layer: done`.

### D2 — Ad-hoc status qualifiers invented on the fly
- **What happened:** we kept inventing `done (attested)`, `done (substrate); operator-pending`, `deferred (operator)` — because the model had no slot for them.
- **Why it hurt:** inconsistent semantics; the same word meant different things.
- **Do instead:** a defined gate/status taxonomy up front.
- **odm:** configurable gate sets per node type.

### D3 — Evidence level untracked
- **What happened:** O-37 closed "attested" (Duncan relaying Marco's verbal result) vs verbatim `PERMISSION_DENIED` outputs — the distinction had to be hand-noted.
- **Why it hurt:** "verified" and "someone said so" looked the same in the ledger.
- **Do instead:** record evidence type (asserted / attested / reproduced / reconciled) per gate.
- **odm:** evidence-level field on gate transitions.
- **GOOD:** `verified-live: reconciled (probe output attached)`. **BAD:** `done` with no indication it was a verbal relay.

---

## E. Scope, amendments, vision

### E1 — Vision lost by tackling work items when big-picture was asked (the core complaint)
- **What happened:** repeatedly, big-picture questions were answered with the next work item (cc-prompt, ledger row), and the strategy eroded.
- **Why it hurt:** the program drifted from its own goals (traffic-readiness, env parity) without anyone deciding to.
- **Do instead:** keep a cheap, always-current statement of vision/strategy at the top of the rollup; answer strategy questions from it.
- **Prevented at origin:** a north-star doc + cheap `orient` that leads with vision.
- **odm:** `orient` leads with vision → current focus → ready/blocked → drift.

### E2 — Amendments accreted onto in-flight ledgers; intent vs emergent blurred
- **What happened:** O-A1..O-A4 inserted discovered work into the active phase's ledger, mixing original plan with emergent scope.
- **Why it hurt:** "what was the original intent vs what did we add along the way?" got hard to see.
- **Do instead:** tag node provenance (planned vs amendment/discovered).
- **odm:** provenance field; rollup can show original-vs-emergent.

### E3 — Plan vs stakeholder expectation mismatch surfaced late and by accident
- **What happened:** the "anything in dev → staging → prod parity" expectation conflicted with the documented staging-DB deferral — discovered only when the DB confusion forced a big-picture review.
- **Why it hurt:** weeks of phased work proceeded on an assumption stakeholders didn't share.
- **Do instead:** record the program-level acceptance ("what does traffic-ready mean?") explicitly and check work against it.
- **odm:** program-level acceptance facts; reconcile plan against stated vision.

### E4 — No program-level "definition of done"
- **What happened:** there was a per-slice DoD but no "when is the whole service actually traffic-ready?" definition.
- **Do instead:** define program/arc acceptance as tracked facts.
- **odm:** acceptance facts at project/arc level, reconcilable.

### E5 — Deferrals relied on prose "named re-entry," not a tracked backlog
- **What happened:** deferrals were disclosed with a prose re-entry condition (good discipline!) but lived in closing reports, not a surfaced list.
- **Why it hurt:** O-37 and O-50 stayed open and only persisted by my re-raising them each turn; a different operator might have lost them.
- **Do instead:** deferred = a first-class status with a checkable re-entry condition, surfaced in the rollup.
- **odm:** `deferred` status + re-entry predicate + rollup surfacing.

---

## F. Verification & evidence

### F1 — Verification was point-in-time, against the repo, not continuous, not against reality
- **Do instead:** continuous reconcile against live state.
- **odm:** scheduled reconcile.

### F2 — Claims taken on summary, not verified (LLM, see G3)
- **What happened:** "the DB is barely used" was relayed from a subagent recon; later proven wrong (the DB backs tenant resolution on every authed request → 503).
- **Do instead:** verify load-bearing claims against primary evidence before acting on them.

### F3 — Bugs slipped because no continuous integration-level check
- **What happened:** `db-host-check` IPv4-only (missed DNS hosts); the unknown-env guard dropped in the case→data migration (typo'd env silently binds nothing); CHANGELOG mis-stated the binding count (27 vs 24). All caught late — by a reviewer or by me, not by a gate.
- **Do instead:** make these checks gates, not hopes.
- **odm:** `check` in CI.

### F4 — The best thing the project built was never generalized
- **What happened:** the freeze-harness pattern (see C3) was reinvented per slice and never lifted.
- **Lesson:** when a local mechanism is clearly the right pattern, generalize it immediately — don't leave the program operating open-loop while a closed-loop exists at the file level.

---

## G. LLM-specific failure modes (the part human PM experience can't supply)

### G1 — The context-reconstruction tax makes vision-loss the path of least resistance
- **What happened:** rebuilding the global picture each turn is expensive; the cheap, recent, local artifact wins attention. This *mechanically* produced E1.
- **Why it's LLM-specific:** context resets re-pay the cost every session; there's no persistent working memory of the whole.
- **Do instead:** make global state a cheap, single, machine-loadable artifact the agent reads first (`orient`). Don't rely on "remember the vision."
- **odm:** `orient` / generated rollup — the single most important LLM affordance.

### G2 — Default-to-producing-artifacts
- **What happened:** when asked big-picture questions, I defaulted to generating the next cc-prompt/ledger row — because producing is rewarded and feels like progress.
- **Do instead:** the skill should instruct: when a strategy/vision question is asked, answer at that altitude *first*; do not emit work items until the level is explicitly "execution."
- **PM-skill rule:** "Match the altitude of the question. Vision asked → vision answered. Work items are an execution-phase output, not a default."

### G3 — Pattern-matching over verification on a load-bearing claim
- **What happened:** I characterized prod-without-DB as "forward-looking, low urgency" from an incomplete recon, and had to correct it to "live 503 functional gap."
- **Do instead:** for any claim that changes severity/priority, verify against primary evidence before asserting; flag when relaying unverified summaries.
- **PM-skill rule:** "Severity/priority calls require reproduced evidence, not relayed summary. Name the evidence level."

### G4 — Trusting summaries over artifacts
- **Do instead:** the CDC discipline (read the actual artifact, reproduce the check) — extend it to program-state claims, not just code review.

### G5 — Clarifying-question calibration was unstable
- **What happened:** sometimes too many questions, sometimes ran ahead.
- **Do instead:** a rule of thumb — ask when the answer changes what you'd build *and* you can't get it from code/docs; otherwise proceed with a stated assumption. Scope questions before a *large* effort (research/arc) are worth it; work-item micro-questions usually aren't.

### G6 — Cross-session continuity gap
- **What happened:** each session (mine, CC's, the twin's) re-oriented from scratch; deferrals persisted only by re-raising.
- **Do instead:** durable, tool-backed state that any session loads identically.
- **odm:** the rollup *is* the shared memory.

---

## H. Condensed SHOULD / SHOULDN'T (liftable)

**SHOULD**
- Give every work unit a stable, opaque ID; never reuse or renumber.
- Express order as dependency edges; derive sequence by topological sort.
- Surface unsatisfied dependencies loudly whenever proceeding past them.
- Keep one generated, authoritative rollup of state; read it first each session.
- Track integration-level desired-state facts and reconcile them against reality on a schedule.
- Use multi-gate status vectors with explicit evidence levels.
- Tag provenance (planned vs discovered) and reserve future/parallel work as visible nodes.
- Match the altitude of the question; produce work items only in execution phase.
- Verify load-bearing/severity claims against primary evidence before acting.
- Generalize a clearly-right local mechanism to the program level immediately.

**SHOULDN'T**
- Encode sequence (or "inserted late") in an identifier.
- Renumber identities to fix ordering; rename labels instead.
- Leave dependencies as prose.
- Let "done" mean "done at its layer" without an integration gate.
- Invent status qualifiers ad hoc.
- Carry deferrals only in closing-report prose.
- Answer strategy questions with work items.
- Treat a relayed summary as verified.
- Let a brilliant per-file check stay per-file while the program runs open-loop.

---

## I. GOOD / BAD example pairs (for odm docs)

| # | BAD | GOOD |
|---|---|---|
| 1 | "Phase 8.5" wedged between 8 and 9 | new node, opaque id, `after:` edge; position derived |
| 2 | renumber slice, grep-fix refs (miss some) | rename label; `after:[id]` edges still resolve |
| 3 | "needs the migrate seam first" (prose, 3 docs away) | `consumes: [o48-seam]` edge |
| 4 | "do Slice 6 next" (next number) | `odm next` → ready set |
| 5 | dependency parked & forgotten | `odm check` → "blocked: Phase-8.5 incomplete" |
| 6 | "prod has a DB" (instance layer true, service layer false) | `desired: prod.service.db_wired`; `reconcile` flags mismatch |
| 7 | `store-layer: done` | `built✓ tested✓ deployed(dev)✓ verified-live(prod)✗` |
| 8 | `done` on a verbal relay | `verified-live: attested` vs `reconciled` |
| 9 | deferral lives in a closing report | `deferred` status + re-entry predicate, surfaced in rollup |
| 10 | answer "what's the vision?" with a cc-prompt | `orient` leads with vision, then ready/blocked/drift |

---

## J. The one-paragraph prevention summary

Almost every failure here reduces to two missing pieces that existed *locally* but
were never made *global*: a **complete dependency graph** (so order is derived and
out-of-order work is impossible to do silently) and a **desired-vs-actual
reconciler** (so plan and reality can't diverge unseen). The team had already
invented the second pattern at the file level (the freeze-harnesses) and lived
in the first paradigm daily (Make). Had both been lifted to the program level —
with a cheap, single, machine-loadable rollup as the source of truth — the
numbering chaos, the parked dependency, the prod-DB 503, the stale docs, and the
vision-loss would each have been either impossible or loud-and-early. `odm` is
the lift.
