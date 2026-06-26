# LEDGER-DISCIPLINE.md

> Per-slice verification discipline for CC (implementer) and CDC (reviewer).
> Load this skill at the start of any slice that has an associated ledger.
> This document describes the protocol; the ledger itself is per-slice and lives elsewhere.

## What this is

Ledger discipline is a per-slice verification practice adapted from the
defect-register and corrective-action traditions used in nuclear power,
surgery (WHO Surgical Safety Checklist), aviation, clinical trials, food
safety (HACCP), financial audit, and human spaceflight. The practice has a
century of precedent and decades of randomised-controlled evidence. See the
companion writeup and sourcebook for full citations.

The short version: every acceptance criterion for a slice is enumerated
as a ledger item with a grep-verifiable definition of done. CC works against
the ledger and reports a disposition for every item. CDC verifies every
disposition independently against the actual commit state. No slice
advances until the ledger is fully closed.

The practice exists because registers alone produce compliance theatre.
Paper compliance regularly overstates observed compliance by large,
reproducible margins (Pickering 2013, Levy 2012, Rydenfält 2013/2014). The
verification culture around the register — explicit closure criteria,
separation of identification from closure, effectiveness review distinct
from closure — is where the discipline actually lives.

## Notes for Codex

For Codex, read **CC** as Codex CLI in the IC implementation role and **CDC**
as Codex Desktop in the collaborative planning/review/QA role. The role split
matters more than the product names: implementation claims are proposed-done
until independently verified by a reviewing context or human.

If the same Codex surface performs both implementation and review, preserve
as much separation as the environment allows: re-read the ledger from the
opening state, rerun the Verify commands, inspect the actual diff, and treat
the closing report as evidence to check rather than as a summary to trust.
When possible, use a fresh context, a separate thread, or a human reviewer
for the CDC pass.

Codex must also respect its approval and sandbox model. A Verify command that
requires escalation, network access, GUI access, or writes outside the
workspace is still the right kind of evidence, but it must be run through the
available approval flow or recorded as blocked with a concrete reason and
re-entry condition.

## The ledger format

Each slice has a ledger. The ledger is a table with one row per
acceptance criterion. Minimum columns:

| Col         | Meaning                                                    |
|-------------|------------------------------------------------------------|
| ID          | Unique identifier (F-1, F-2, … or slice-specific).     |
| Criterion   | The acceptance criterion, as a single observable claim.    |
| Verify      | The command / grep / test that verifies it. Must be exec.  |
| Significance| serious / correctness-grade / polish.                      |
| Origin      | Where the criterion came from (audit doc, spec, review).   |
| Status      | open / done / deferred / no-op. Starts as `open`.          |
| Evidence    | Commit SHA + output of Verify command. Empty if open.      |
| Notes       | Free text. Used for deferred reasons, no-op rationales.    |

Rules:

1. **Every row must reach a final status before the slice advances.**
   Final status is one of: `done`, `deferred`, `no-op`. `open` is not a
   final status.

2. **`done` requires evidence.** The commit SHA where the change landed plus
   the output of the Verify command. A bare "done" without evidence is not
   an acceptable disposition.

3. **`deferred` requires a reason and a re-entry condition.** "Blocked on
   integration slice X" is acceptable. "Later" is not.

4. **`no-op` requires a rationale.** "Design decision: the invariant is
   documented rather than enforced because [specific reason]" is acceptable.
   "Not needed" is not.

5. **Missing rows are ledger bugs.** If the ledger has 24 rows at start of
   slice and 22 rows at close, the 2 missing rows are defects in the
   closing report, not omissions. Silent drops are the named failure mode
   this protocol prevents.

6. **Evidence must be independently reproducible.** The Verify command must
   be something CDC can run and observe the same result. Claims like
   "verified manually" are not evidence.

## CC protocol

When CC receives a slice prompt that references this skill:

1. **Read the ledger before writing any code.** The ledger is not a
   checklist to tick off at the end. It is the specification of what the
   slice means by "done." If a criterion is unclear, ask for
   clarification before implementing.

2. **Work against the ledger, not around it.** If during implementation you
   discover that a criterion is wrong, impossible, or supersedable, do not
   silently work around it. Raise it as an amendment request. The ledger
   can change; it cannot be quietly ignored.

3. **Update the ledger as you work.** Fill in the Evidence column at the
   commit where the criterion is met. Do not leave all evidence for the
   final report.

4. **In the closing report, walk the ledger item by item.** For every row,
   state the final status and the evidence. Do not summarise. Do not write
   "deviations: none" — write a disposition for each numbered item. If you
   find yourself writing a prose summary, stop and convert it to a per-row
   walk.

5. **Name any uncertainty.** If a criterion is marked `done` but you are
   not sure the evidence fully covers it, say so. The protocol rewards
   honest "done with caveat X" over confident "done" that turns out to
   be softpedalled.

6. **Expect the compliance-theatre failure mode.** The surgery literature
   (Pickering et al. 2013; Levy et al. 2012) documents that paper
   compliance regularly exceeds observed compliance by large margins. This
   is a property of humans and LLMs both. The countermeasure is the
   per-row walk with evidence. Trust the protocol over the instinct to
   report "deviations: none."

## CDC protocol

When CDC reviews a closed slice ledger:

1. **Count the rows.** The closing report's row count must match the
   opening ledger's row count. Missing rows are a ledger bug and must be
   corrected before any further review.

2. **For every `done` row, run the Verify command.** Do not take the
   evidence at face value. Execute the grep, run the test, read the diff.
   If the command does not reproduce the claimed result, the row is not
   done — it is softpedalled or mistaken.

3. **For every `deferred` row, check the reason and re-entry condition.**
   If the reason is thin ("later") or the re-entry condition is absent, the
   row is not validly deferred.

4. **For every `no-op` row, check the rationale.** A documented invariant
   that the code does not enforce is not a no-op — it is a softpedalled
   `done`. Watch for this specifically.

5. **Look for the silent-drop pattern.** If the opening ledger had N rows
   and the closing report addresses N-k rows with k > 0 rows not present,
   the missing k are silent drops. Do not accept a closing report with
   silent drops — return it for completion.

6. **Watch for spec-softening.** A row marked `done` where the evidence
   shows a weaker guarantee than the criterion stated is softpedalled, not
   done. Example from our case study: integration test required to pin
   end-to-end arithmetic to a specific value; evidence shows the test
   accepts a range that would pass even if half the ticks were dropped.
   That is softpedalling, not `done`.

7. **Watch for partial adoption.** A discipline (a helper function, a type
   invariant, an error-handling pattern) applied at some call sites and
   skipped at others within the same file is partial adoption, not `done`.
   Run workspace-wide greps to detect this.

8. **Record what worked.** At the end of the ledger, add a "What Worked"
   section capturing patterns or practices that made this slice close
   cleanly. This is the Safety-II complement to the defect ledger and
   prevents the protocol from becoming purely reactive.

## Iteration budget

Five iterations per slice. Not four, not ten. The cap is deliberate.

- If a slice closes in 1–3 iterations, that is normal and expected.
- If it takes 4–5, the slice was probably too large or under-specified,
  and the next slice's ledger should be tightened in response.
- If it reaches iteration 5 without convergence, stop. Do not iterate a
  sixth time on the same ledger in the same session. Options:
  a. Rework the slice scope (usually the right answer).
  b. Start a new CC session with fresh context (if context length is
     suspected as the problem).
  c. Escalate to a methodology review (if the same failure pattern is
     recurring across slices, which points at a structural rather
     than tactical issue).
- Some situations will dictate an override by the operator; in that event,
  keep an open mind, but provide feedback if it doesn't seem justified.

The empirical basis for this cap is both the self-debugging literature
(Chen et al. ICLR 2024: "successful debugging processes mostly end within
3 turns") and the Debugging Decay Index (Adnan & Kuhn 2025: 60–80% of
debugging capability is lost within 2–3 attempts). Past five iterations,
additional rounds usually make things worse rather than better.

## Known structural limitation

In this protocol, CC is both implementer and first-line self-assessor. This
is weaker than the mature-field discipline where the recorder of the defect
is structurally separate from the closer (aviation 14 CFR 121.563; CAFU
state machine; NRC inspector pattern). CDC's independent verification is
the protection against this weakness, but the protection depends on CDC's
discipline, not on structural enforcement.

Acceptable mitigations:

- CDC treats CC's `done` claim as "proposed done" until independently
  verified.
- CDC's review time is budgeted proportionally to the number of `done`
  rows, not the number of open issues (counter-intuitively, most of the
  review value is in checking the claims that look resolved, not in
  discussing the ones that are obviously still open).
- The iteration budget is per-slice, not per-CC-attempt — CDC's
  rejection of a softpedalled row counts as a new iteration.

## Failure modes this protocol prevents

1. **Silent drops.** Ledger items that are identified, not fixed, and not
   mentioned in the deferral list. The per-row walk and row-count check
   structurally prevent this.
2. **Spec-softening.** Criteria marked `done` with weaker-than-stated
   guarantees. The evidence-reproduction check in CDC protocol step 2
   catches this.
3. **Partial adoption.** A discipline applied inconsistently within a file
   or module. The workspace-wide grep in CDC protocol step 7 catches this.
4. **Vacuous tests.** Tests that compile but do not exercise the logic.
   Mitigated by requiring the Verify command to be a test that would fail
   if the criterion were violated, not just a test that compiles.
5. **Compliance theatre.** Paper compliance exceeding observed compliance.
   Mitigated by the independent reproduction step in CDC protocol.

## Failure modes this protocol does NOT prevent

1. **Wrong ledger.** If the ledger does not capture the true acceptance
   criteria of the slice, the protocol will faithfully verify against
   the wrong target. Ledger quality is upstream of protocol quality.
2. **Adversarial closure.** If CC or CDC deliberately falsifies evidence,
   the protocol assumes good faith. This is acceptable in the CC+CDC
   context; it is a real limitation when the discipline is extended to
   multi-human teams where audit-trail integrity matters.
3. **Systemic issues invisible to the ledger.** Hollnagel's Safety-II
   critique applies: the protocol tracks defects, not emergent success
   patterns. The "What Worked" section is a partial mitigation; genuine
   systemic issues may still require out-of-band review.

## Appendix: Per-slice ledger template

A new slice ledger starts as a minimal markdown table. Copy, fill in,
and commit it as the `ledger.md` in the slice's directory, per the canonical
layout in [`../docs/PROJECT-MANAGEMENT.md`](../docs/PROJECT-MANAGEMENT.md)
— e.g. `docs/design-vX.Y.Z/arcNN-<slug>/sliceNN-<slug>/ledger.md`:

    # Slice <N>: <name>

    ## Ledger

    | ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
    |----|-----------|--------|--------------|--------|--------|----------|-------|
    | F-1 | <criterion> | <grep/test> | serious/correctness/polish | <source> | open | | |
    | F-2 | ... | ... | ... | ... | open | | |

    ## What Worked

    _(Filled in at slice close. Patterns, practices, or decisions that
    made the slice close cleanly and should be preserved or
    generalised.)_

    ## Closure

    Closed at commit <SHA> on <date>. CDC verification: <name/session>.
    Total rows: <N>. Done: <n>. Deferred: <n>. No-op: <n>.

---

_Terminology aligned to [`../docs/AI-ENGINEERING-METHODOLOGY.md`](../docs/AI-ENGINEERING-METHODOLOGY.md) on 2026-06-08: the level-1 ledger-bearing unit is **slice**, not "milestone." This closes the paired follow-up flagged in the methodology's v1.1 and v1.2 version history (the `milestones/` ledger-path convention is now `arcNN-<slug>/sliceNN-<slug>/ledger.md`). The protocol itself — grep-verifiable rows, evidence-backed closure, CC/CDC separation, the five-iteration cap — is unchanged._
