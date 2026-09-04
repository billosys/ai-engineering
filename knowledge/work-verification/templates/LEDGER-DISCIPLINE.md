# LEDGER-DISCIPLINE.md

> Per-scale verification discipline for the doer / independent-reviewer pair.
> Load this skill at the start of any **slice, arc, or project that has a
> ledger** — before the work, not as an end-of-unit checklist. This document
> describes the protocol; the ledgers themselves live next to the
> plan-of-record at each scale as dedicated `ledger.md` files (see
> `../../project-management/guides/PROJECT-MANAGEMENT.md`).

## What this is

Ledger discipline is a verification practice adapted from the defect-register
and corrective-action traditions used in nuclear power, surgery (WHO Surgical
Safety Checklist), aviation, clinical trials, food safety (HACCP), financial
audit, and human spaceflight. The practice has a century of precedent and
decades of randomised-controlled evidence. See the companion writeup and
sourcebook for full citations.

The short version: every acceptance criterion for a unit of work is enumerated
as a ledger row with a verifiable definition of done. The doer works against
the ledger and reports a disposition for every row. An independent reviewer
verifies every disposition against the actual artifacts. No unit advances
until its ledger is fully closed.

**The ledger is one scale-free discipline with three instantiations.** It was
born at the **slice** — the unit of execution — and that is where it is most
mechanical. But the same discipline applies one and two scales up, to the
**arc** (do its slices compose into the promised capability?) and the
**project** (do its arcs compose into the definition of done?). Those higher
scales are the *recomposition* side of the decompose/recompose loop in
[`../../project-management/guides/PROJECT-MANAGEMENT.md`](../../project-management/guides/PROJECT-MANAGEMENT.md): planning lays
out a tree of claims top-down; the ledgers discharge that tree from the leaves
up, each scale's ledger being the gate that confirms its sub-tree composes
before the claim above it can rest on it. This is the assurance-case pattern
(see *Lineage*), realised as living ledgers.

This retained template/support asset states the **invariant spine** once, then
gives three sections — one per scale — describing only what *adapts*. Use it
when you need the complete protocol in one file or copyable ledger tables. For
selective loading, use the focused guides:

- [`../guides/01-ledger-discipline.md`](../guides/01-ledger-discipline.md)
- [`../guides/02-evidence-strength.md`](../guides/02-evidence-strength.md)
- [`../guides/03-row-closure.md`](../guides/03-row-closure.md)
- [`../guides/04-silent-drop-checks.md`](../guides/04-silent-drop-checks.md)
- [`../guides/05-independent-verification.md`](../guides/05-independent-verification.md)

Read the spine, then the section for the scale you are closing.

The practice exists because registers alone produce compliance theatre. Paper
compliance regularly overstates observed compliance by large, reproducible
margins (Pickering 2013, Levy 2012, Rydenfält 2013/2014). The verification
culture around the register — explicit closure criteria, separation of
identification from closure, effectiveness review distinct from closure — is
where the discipline actually lives.

## Notes for Codex

For the canonical **CC**, **CDC**, and **Operator** role definitions, read
[the methodology Notes for Codex](../../engineering-methods/guides/01-engineering-methodology.md#notes-for-codex)
in the collaboration-framework package. Those labels are the **slice-level
instance** of a scale-free principle: *the closer of a row is structurally
separate from its verifier.* At arc and project scale the labels shift (see
those sections), but the separation does not.

If the same Codex surface performs both roles, preserve as much separation as
the environment allows: re-read the ledger from the opening state, rerun the
Verify commands, inspect the actual diff, and treat the closing report as
evidence to check rather than a summary to trust. When possible, use a fresh
context, a separate thread, or a human reviewer for the verifying pass.

Codex must also respect its approval and sandbox model. A Verify command that
requires escalation, network access, GUI access, or writes outside the
workspace is still the right kind of evidence, but it must be run through the
available approval flow or recorded as blocked with a concrete reason and
re-entry condition.

---

## The invariant spine

These rules hold at every scale. The three scale sections below describe only
what changes.

### The ledger format

A ledger is a table with one row per acceptance criterion. Minimum columns:

| Col          | Meaning                                                     |
|--------------|-------------------------------------------------------------|
| ID           | Unique identifier (F-1, A-1, P-1, … or unit-specific).      |
| Criterion    | The acceptance criterion, as a single observable claim.     |
| Verify       | The command / grep / test / demonstration that verifies it. |
| Significance | serious / correctness-grade / polish.                       |
| Origin       | Where the criterion came from (plan, bubble-up, review).    |
| Status       | open / done / deferred / no-op. Starts as `open`.           |
| Evidence     | The evidence + its **strength** (see below). Empty if open. |
| Notes        | Free text. Deferred reasons, no-op rationales.              |

### The rules

1. **Every row must reach a final status before the unit advances.** Final
   status is one of `done`, `deferred`, `no-op`. `open` is not final.
2. **`done` requires evidence.** Where the change landed (a commit SHA, a
   pointer to a closed child ledger, a demonstration transcript) plus the
   output of the Verify. A bare "done" is not acceptable.
3. **`deferred` requires a reason and a re-entry condition.** "Blocked on
   slice X" is acceptable; "later" is not.
4. **`no-op` requires a rationale.** "Documented rather than enforced because
   [specific reason]" is acceptable; "not needed" is not.
5. **Missing rows are ledger bugs.** If the ledger opens with N rows and closes
   addressing N−k, the missing k are defects in the closing report, not
   omissions. Silent drops are the named failure mode this protocol prevents.
6. **Evidence must be independently reproducible.** The Verify must be
   something the reviewer can run (or a demonstration they can witness) and
   observe the same result. "Verified manually" is not evidence.
7. **The closer is structurally separate from the verifier.** The doer reports
   dispositions; an independent party verifies every one against the artifacts.

### Evidence strength

Every piece of evidence carries a strength, borrowed from odm's gate-evidence
levels because the fit is exact:

- **asserted** — claimed done, no evidence attached. Never a valid closure.
- **attested** — the doer supplied evidence (reported command output, a
  pointer), not independently re-run. Proposed-done.
- **reproduced** — an independent party re-ran the Verify (or witnessed the
  demonstration) and observed the same result at this scale.
- **reconciled** — the strongest: the claim has additionally been checked
  consistent with the broader state of truth (e.g. CI green across the whole
  workspace, or a reconciliation pass against an external source).

**A `done` row's evidence must reach at least `reproduced` at its own scale.**
`attested` is the holding state while the doer's claim awaits independent
reproduction. (This maps directly onto our sandbox/CI reality: the
implementer *attests* a test passes; CI *reproduces* it; "green across the
workspace" is *reconciled*.)

### The five axes that adapt up the scales

| Axis | Slice | Arc | Project |
|------|-------|-----|---------|
| **Rows assert** | acceptance criteria (the steps) | (a) slices closed · (b) slices **compose** into the capability · (c) bubble-up findings dispositioned | (a) arcs closed · (b) arcs **compose** into the DoD · (c) bubble-up findings dispositioned |
| **Evidence kind** | grep / unit test, *reproduced* | integration demo *reproduced*; children-closed *attested* (pointer to closed child ledger) | system/acceptance demo *reproduced*; children-closed *attested* via arc ledgers |
| **Doer / verifier** | CC implements / CDC verifies | CDC assembles / fresh context or operator gates | planner assembles / operator + fresh context gates |
| **Iteration** | five-iteration fix loop on the diff | failed composition → **remediation slice** (not a re-pass) | failed DoD → **remediation arc** (or roadmap re-scope) |
| **Cadence** | opens in slice `ledger.md`, next to `slice-plan.md`; closes at slice close | opens in arc `ledger.md`, next to `arc-plan.md`; closes in arc closing-report | opens in project `ledger.md`, next to `project-plan.md`; closes in project closing-report |

Three classes of row recur at every interior scale: **(a) children closed**,
**(b) children compose**, **(c) bubble-up findings dispositioned**. The
load-bearing rule across scales: **class-(b) composition rows are always
independently *reproduced* at their own scale — you actually run the
integration/system demonstration — never merely inherited as attestation from
the children.** Inheriting composition is exactly the "audit that only reads
the claim of completion" theatre, committed one scale up.

---

## Section A — Slice-level ledger protocol

The slice is the leaf and the origin of the discipline — the unit of execution
that lands as one mergeable diff. Here the ledger is most mechanical: rows are
acceptance criteria (the slice's *steps*), and Verify is a grep or a test.

### What the rows assert

The slice-plan's exit criteria, decomposed into single observable claims. Each
row is something a command can check: a function behaves, a test passes, an
invariant holds, an error path returns the right error.

### CC protocol

When CC receives a slice prompt that references this skill:

1. **Read the ledger before writing any code.** It is the specification of what
   the slice means by "done." If a criterion is unclear, ask before
   implementing.
2. **Work against the ledger, not around it.** If a criterion is wrong,
   impossible, or supersedable, raise it as an amendment request. The ledger
   can change; it cannot be quietly ignored.
3. **Update the ledger as you work.** Fill in Evidence at the commit where the
   criterion is met (strength `attested`). If the evidence is a durable artifact
   produced by the slice, point to `artifacts/` inside the slice directory by
   default, or to the operator-recorded override. Do not leave all evidence for
   the final report.
4. **In the closing report, walk the ledger row by row.** For every row, state
   the final status and the evidence. Do not summarise; do not write
   "deviations: none" — write a disposition for each numbered row. If you find
   yourself writing a prose summary, stop and convert it to a per-row walk.
5. **Name any uncertainty.** A `done` whose evidence you are unsure fully covers
   the criterion should say so. The protocol rewards honest "done with caveat X"
   over confident "done" that turns out softpedalled.
6. **Expect the compliance-theatre failure mode.** Paper compliance regularly
   exceeds observed compliance (Pickering 2013; Levy 2012). The countermeasure
   is the per-row walk with evidence. Trust the protocol over the instinct to
   report "deviations: none."

### CDC protocol

When CDC reviews a closed slice ledger:

1. **Count the rows.** The closing report's row count must match the opening
   ledger's. Missing rows are a ledger bug, corrected before any further review.
2. **For every `done` row, run the Verify.** Do not take evidence at face value
   — execute the grep, run the test, read the diff. If it does not reproduce the
   claimed result, the row is not done. (This is the `attested` → `reproduced`
   transition.)
3. **For every `deferred` row, check the reason and re-entry condition.** Thin
   reason ("later") or absent re-entry → not validly deferred.
4. **For every `no-op` row, check the rationale.** A documented invariant the
   code does not enforce is a softpedalled `done`, not a no-op.
5. **Look for the silent-drop pattern.** N opening rows, N−k addressed with
   k > 0 missing → the missing k are silent drops. Return for completion.
6. **Watch for spec-softening.** A `done` whose evidence shows a weaker
   guarantee than the criterion stated is softpedalled. (Case study: an
   integration test required to pin end-to-end arithmetic to a value, whose
   evidence shows it accepts a range that would pass even if half the ticks were
   dropped.)
7. **Watch for partial adoption.** A discipline applied at some call sites and
   skipped at others within the same file is partial adoption, not `done`. Run
   workspace-wide greps.
8. **Check artifact placement.** If a slice produced durable artifacts, confirm
   they live under the slice's `artifacts/` directory, or under the explicit
   override recorded in the slice plan and prompt. If the close says "none,"
   verify that against the diff and command outputs.
9. **Record what worked.** Add a "What Worked" section capturing patterns that
   made the slice close cleanly — the Safety-II complement to the defect ledger.

### Iteration budget

Five iterations per slice. Not four, not ten. The cap is deliberate and is a
**slice-scale** mechanism (its higher-scale analogue is remediation work, not a
re-pass — see Sections B and C).

- 1–3 iterations is normal and expected.
- 4–5 means the slice was probably too large or under-specified; tighten the
  next slice's ledger in response.
- Reaching 5 without convergence: stop. Do not iterate a sixth time on the same
  ledger in the same session. Options: (a) rework the slice scope (usually
  right); (b) start a fresh CC context (if context length is the suspect);
  (c) escalate to a methodology review (if the failure pattern recurs across
  slices — structural, not tactical).
- An operator may override; keep an open mind, but give feedback if the override
  doesn't seem justified.

The empirical basis is the self-debugging literature (Chen et al. ICLR 2024:
"successful debugging processes mostly end within 3 turns") and the Debugging
Decay Index (Adnan & Kuhn 2025: 60–80% of debugging capability lost within 2–3
attempts). Past five iterations, additional rounds usually make things worse.

### Known structural limitation

CC is both implementer and first-line self-assessor — weaker than the
mature-field discipline where the recorder of a defect is structurally separate
from the closer (aviation 14 CFR 121.563; NRC inspector pattern). CDC's
independent verification is the protection, but it depends on CDC's discipline,
not structural enforcement. Mitigations: CDC treats `done` as proposed-done
until reproduced; CDC budgets review time proportional to the number of `done`
rows (most review value is in checking claims that look resolved); the iteration
budget is per-slice, so CDC's rejection of a softpedalled row counts as a new
iteration.

### Per-slice ledger template

```
# Slice <N>: <name>

## Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| F-1 | <criterion> | <grep/test> | serious/correctness/polish | <source> | open | | |
| F-2 | ... | ... | ... | ... | open | | |

## What Worked

_(At slice close. Patterns that made the slice close cleanly.)_

## Closure

Closed at commit <SHA> on <date>. Verified by: <name/session>.
Rows: <N>. Done: <n>. Deferred: <n>. No-op: <n>.
```

The slice ledger lives as `ledger.md` in the slice directory, per the canonical
planning worktree in
[`../../project-management/guides/PROJECT-MANAGEMENT.md`](../../project-management/guides/PROJECT-MANAGEMENT.md) — e.g.
`$PROJECT_DIR/.worktrees/planning/projectNN-<slug>/arcNN-<slug>/sliceNN-<slug>/ledger.md`.
Durable artifacts produced by the slice default to the sibling
`artifacts/` directory in that same slice path, unless the operator records a
different artifact home in the slice plan.

---

## Section B — Arc-level ledger protocol

An arc is verified when its last slice closes. No one *implements* an arc — it
emerges from slices — so the arc ledger does not re-verify slice rows (those are
closed one scale down). It verifies that the slices **compose** into the
capability the arc promised, and that every finding the slices bubbled up has a
tracked disposition. This is the V-model's *integration* level: do the parts
work together, with no interface gaps?

### What the rows assert

Three classes (from the spine), derived from the arc-plan's capability
statement decomposed into "what must be true for this capability to exist":

- **(a) Slices closed.** One row per slice in the arc-plan's breakdown: this
  slice's ledger closed cleanly. Evidence: a pointer to its closed
  `cdc-verification.md` — strength `attested` (spot-check, don't re-run the
  whole slice).
- **(b) Slices compose.** The integration claims: the capability is
  demonstrably achievable end-to-end across the slices. Evidence: an
  integration demonstration **reproduced at the arc scale** — strength
  `reproduced` (mandatory; never inherited).
- **(c) Findings dispositioned.** One row per slice bubble-up finding: it was
  routed (a remediation slice, a re-slice, a deferral with re-entry, or a
  no-op with rationale). Evidence: the arc-plan change-log entry that records it.

### Evidence kinds

Composition rows are reproduced via an arc-scale demonstration (run the
capability end-to-end). Children-closed rows are attested by pointer to the
closed slice ledgers. The silent-drop check operates on the slice breakdown: the
arc ledger's class-(a) row count must equal the number of slices in the
arc-plan — a missing slice is an arc-scale silent drop.

### Roles

CDC — who ran the per-slice verifications and therefore knows the arc — assembles
the arc ledger and writes the arc closing-report. Independence is preserved by a
**fresh context, the operator, or a subagent** acting as the arc-gate reviewer
(the stage-gate's independent gatekeeper). The one who performed the composition
cannot be the one who signs it off.

### Remediation, not iteration

There is no five-iteration loop at arc scale — you do not re-implement an arc. A
failed composition row (the slices do not add up) spawns a **remediation slice**
or a re-slice, planned through the arc-plan via the plan-change discipline, and
the arc closes only once that slice closes. Trying to "iterate" an arc in place
— patching across slices without planning the work — is the bisection
anti-pattern (the `05.1` / `07.1` numbering odm refuses); it is iteration applied
at the wrong scale.

### Cadence

The arc ledger **opens** when the arc-plan is written: its class-(b) composition
rows are stated up front from the capability statement (you know what "composes"
means before the slices run). It lives in a dedicated `ledger.md` beside
`arc-plan.md`. It **accrues** class-(a) and class-(c) rows as slices close and
bubble up. It **closes** in the arc `closing-report.md` with the per-row walk and
the independent gate review.

### Cross-scale trending

A finding that recurs across **slices** within the arc is an arc-level systemic
signal — the arc has a hole, not just one slice. Note it in the arc
closing-report's "What Worked / What Recurred" so it informs the next arc rather
than re-surfacing slice by slice.

### Per-arc ledger template

```
## Arc Ledger  (in arcNN-<slug>/ledger.md)

Capability: <the one coherent thing this arc delivers>

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| A-1 | slice 01 closed | ptr: slice01 cdc-verification | correctness | arc-plan | open | | attested |
| A-2 | <capability> demonstrable end-to-end | <integration demo> | serious | arc-plan | open | | reproduce at arc scale |
| A-3 | <slice-NN bubble-up finding> routed | ptr: arc-plan change-log | <…> | bubble-up | open | | |

## Closure  (in closing-report.md)

Composition verdict: <delivered / gaps named>. Gate reviewed by: <independent>.
Slices: <N> (matches arc-plan breakdown). Findings dispositioned: <n>.
```

---

## Section C — Project-level ledger protocol  *(provisional)*

> **Provisional.** This tier is validated by analogy and established practice
> (assurance cases, the V-model's system/acceptance levels, stage-gate reviews),
> not yet by a closed project — odm has not closed an MVP as of this writing. It
> will be revised against experience when it does. Shipped now because the
> *structure* is the point; the honest register is "tested at slice and arc
> scale, reasoned at project scale."

A project is verified when its last arc closes. As with the arc, nothing is
re-verified that closed one scale down; the project ledger verifies that the
arcs **compose** into the definition of done, and that every arc bubble-up
finding is dispositioned. This is the V-model's *system + acceptance* level: the
complete integrated whole, against both the design and the actual need.

### What the rows assert

Derived from the project-plan's definition of done:

- **(a) Arcs closed.** One row per arc in the roadmap: its arc ledger closed and
  it composed. Evidence: pointer to the arc closing-report — `attested`.
- **(b) Arcs compose into the DoD.** The acceptance claims: the project's
  definition of done is demonstrably met. Evidence: a **project-level capability
  demonstration reproduced at project scale** — e.g. for odm, "a fresh session
  orients fully from `odm orient` alone." Never inherited.
- **(c) Findings dispositioned.** One row per arc bubble-up finding, routed via
  the project-plan change-log.

### Evidence kinds

Composition/acceptance rows reproduced via end-to-end project demonstrations
(the closest thing to acceptance testing against the DoD). Arc-closed rows
attested via the arc ledgers. The DoD is partly a *judgment* — "did we build the
right thing" is not fully grep-verifiable — so project composition rows will
include demonstrations *and* an explicit acceptance judgment by the operator,
recorded as such. Naming where the evidence is a judgment rather than a
reproduction is itself part of the honesty discipline.

### The project gate

The project close is a stage gate: go / adjust / kill against the DoD, reviewed
by the operator with an independent context. "Adjust" spawns remediation; "go"
closes the project (or the MVP boundary); "kill" is a legitimate, recorded
outcome.

### Remediation, not iteration

A failed DoD criterion spawns a **remediation arc** or a roadmap re-scope,
tracked through the project-plan via the plan-change discipline — never an
unbounded grind. The project closes only once that work closes.

### Cadence

Opens when the project-plan is written: DoD criteria become the class-(b)
composition rows up front. The project ledger lives in a dedicated `ledger.md`
beside `project-plan.md`. It accrues class-(a)/(c) rows as arcs close. It closes
in a project-level `closing-report.md` with the per-row walk and the gate review.

### Cross-scale trending

A finding that recurs across **arcs** is a project-level systemic signal — the
project's design or process has a hole. This is where the most expensive,
highest-altitude drift is caught (the SDLC's "audits catch system-level errors"
altitude).

### Per-project ledger template

```
## Project Ledger  (in projectNN-<slug>/ledger.md)

Definition of done: <what the project delivers; what it explicitly does not>

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|----|-----------|--------|--------------|--------|--------|----------|-------|
| P-1 | arc 01 closed + composed | ptr: arc01 closing-report | correctness | project-plan | open | | attested |
| P-2 | <DoD criterion> demonstrable | <acceptance demo> | serious | project-plan | open | | reproduce at project scale |
| P-3 | <arc-NN bubble-up finding> routed | ptr: project-plan change-log | <…> | bubble-up | open | | |

## Closure  (in projectNN-<slug>/closing-report.md)

DoD verdict: <met / gaps named>. Gate: go / adjust / kill. Reviewed by: <operator + independent>.
Arcs: <N> (matches roadmap). Findings dispositioned: <n>.
```

---

## Failure modes this protocol prevents

1. **Silent drops** — rows identified, not fixed, not mentioned in the deferral
   list. The per-row walk and row-count check prevent this *at every scale*
   (slice steps, arc slices, project arcs).
2. **Spec-softening** — criteria marked `done` with weaker-than-stated
   guarantees. The evidence-reproduction step catches it.
3. **Partial adoption** — a discipline applied inconsistently within a file or
   module. The workspace-wide grep catches it (slice scale).
4. **Vacuous tests** — tests that compile but do not exercise the logic. The
   Verify must be one that would fail if the criterion were violated.
5. **Compliance theatre** — paper compliance exceeding observed compliance.
   Independent reproduction is the mitigation.
6. **Inherited composition** — *(arc/project)* accepting that the children
   "compose" because each child closed, without an independent end-to-end
   demonstration at this scale. The class-(b)-must-be-reproduced rule prevents
   it.
7. **Iteration at the wrong scale** — *(arc/project)* grinding patches across
   slices/arcs instead of planning remediation work. The
   remediation-not-iteration rule prevents it.

## Failure modes this protocol does NOT prevent

1. **Wrong ledger.** If the ledger does not capture the true acceptance
   criteria, the protocol faithfully verifies the wrong target. Ledger quality
   is upstream of protocol quality — and this gets harder, not easier, up the
   scales, where "composes into the capability" is a judgment.
2. **Adversarial closure.** The protocol assumes good faith; it does not defend
   against deliberately falsified evidence. Acceptable in the CC+CDC context; a
   real limit when extended to multi-human teams where audit-trail integrity
   matters.
3. **Systemic issues invisible to the ledger.** Hollnagel's Safety-II critique:
   the protocol tracks defects, not emergent success. The "What Worked" sections
   and cross-scale trending are partial mitigations.

## Lineage

The **slice** tier descends from the defect-register and corrective-action
traditions (nuclear INPO, aviation NTSB, surgery's WHO checklist, clinical
trials, HACCP, financial audit, spaceflight), with the five-iteration cap
grounded in the self-debugging literature (Chen et al. ICLR 2024) and the
Debugging Decay Index (Adnan & Kuhn 2025).

The **multi-scale** structure descends from three further traditions, which is
why extending the ledger upward is recovery of an established shape rather than
invention:

- **Assurance cases / Goal Structuring Notation** — a top claim decomposed via
  *strategies* into sub-claims, bottoming out in *solutions* (evidence). The
  project → arc → slice → evidence ledger tree *is* an assurance case realised
  as living, gated registers.
- **The V-model** — verification at each decomposition level with a
  corresponding integration level: unit (slice) → integration (arc) →
  system/acceptance (project). The verify-ability gradient up the scales is the
  V-model's gradient.
- **Stage-gate / phase-gate reviews** — formal go/adjust/kill decision points
  with predefined exit criteria assessed by independent gatekeepers. Arc-close
  and project-close are stage gates; the exit criteria are the composition rows,
  set when the plan-of-record at that scale is written.

---

## Component History

The work-verification component history lives at
[`../version-history.md`](../version-history.md). Current ledger-discipline
protocol version: 2.4, 2026-09-01.
