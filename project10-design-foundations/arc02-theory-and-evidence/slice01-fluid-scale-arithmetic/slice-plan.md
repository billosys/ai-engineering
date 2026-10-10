---
slice: slice01-fluid-scale-arithmetic
status: open
depends-on: [arc01-portable-contract Operator-accepted composition]
---

# Slice01 — Fluid Scale Arithmetic

## Goal and authority

Establish the mathematical correction basis for DES-003/004 and reconcile the
selected live witnesses with the adopted diagnostic configuration. This is a
bounded evidence assignment: general proof, actual-input numerical comparisons,
claim-level partial results and concrete later-edit instructions. It does not
rewrite the live skill, perform whole-card review or accept original fidelity.
The [arc plan](../arc-plan.md), [project plan](../../project-plan.md) and
[nine-row ledger](ledger.md) govern. Operator-approved Arc01 composition is
`38b66d0d`, closure `fb33d8cf43e8bb99d9dc9835ded134bd8268933f`.

Two contributors: CDC Sofie authors and independently reviews; separate CC
executes [cc-prompt.md](cc-prompt.md) through Operator relay. Expedited Mode
applies. All rows start open; CC proposes evidence, CDC accepts or returns it.
No close/verification file is created until real work/review occurs.

## Pins, inputs and bounded source witnesses

SOURCE: `dffa504e851b03b8e4746f1941068e4cc850b612` on main, current tracked/index
clean at authoring; pre-existing untracked `knowledge/lfe/` remains untouched.
Planning predecessor: `fb33d8cf43e8bb99d9dc9835ded134bd8268933f` (Arc01 closure).
Read current opening plans/prompt from the issuing commit containing this open
set; record that hash in intake. Use literal pinned Git bytes for source/evidence.
No replay may silently switch to a later HEAD or regenerated values.

Required live witnesses are these inclusive baseline ranges. Read all their
prose/code, keeping surrounding definitions and qualifiers. Their population is
five files / nine spans / 297 lines; this is bounded review, not whole-live coverage.

| SOURCE-relative path | Inclusive required ranges | Purpose |
|---|---|---|
| `knowledge/design/SKILL.md` | 144–210 | Conflicting ratio prose, endpoint declarations, published type/space/pair expressions and adjacent breakpoint claims. |
| `knowledge/design/guides/type.md` | 133–142; 456–488 | Scale definition and complete mathematical notes with empirical/attribution limits. |
| `knowledge/design/guides/layout.md` | 164–228; 350–380; 493–528; 933–948 | Interpolation/invariant claims, actual declarations and finite-clamp/asymptotic wording. |
| `knowledge/design/guides/design.md` | 363–369 | Repeated universal relationship/correctness claim. |
| `knowledge/design/guides/foundations-of-design.md` | 255–286 | Ratio notation, interpolation and growth claims in cited context. |

If a needed definition/qualification crosses a range boundary, read and record
the necessary extension, without claiming full-file completion. Any new finding
outside these ranges is a bubble-up for later C/L/T work, not silent scope growth.
The old skill's C&B defaults are studied inputs; the approved portable contract
supersedes them as behavior/authority for this assignment.

Other pinned inputs: Project09 DES-003/004 audit sections at `795ac75b7d02536e0e95252457ac3282cd17d8d8`;
Slice03 diagnostic example and contract at `38b66d0d`; Slice02 method at
`759ce2dd116a4cfe03b72d43fd2791f48486251c`. Historical audit/example checks are
context; perform the new assigned derivation and actual-byte comparisons.

## Binding mathematical model and investigation method

1. Inventory every mathematical/fluid-configuration assertion and numeric
   expression in the nine witness spans, with stable local claim ID, exact full
   path/hash/inclusive span/assertion. Repeated guide assertions are separate
   occurrences. Keep interleaved source, empirical and aesthetic assertions
   explicitly out of assessed scope or blocked; do not silently mark them true.
2. Define positive bases `a,b`, positive ratios `r,q`, integer `n` and common
   interpolation parameter `0 <= t <= 1`. Let `u=(1-t)a`, `v=tb`, and
   `s_n=u*r^n+v*q^n`. Derive
   `s_n*s_(n+2)-s_(n+1)^2 = u*v*(r*q)^n*(r-q)^2`.
   Explain when the consecutive sizes are geometric: equal ratios or an endpoint
   under these positive assumptions; a genuine interior with unequal ratios has
   positive determinant. Include negative steps. Do not infer perceptual quality.
3. Explain bounded clamped linear behavior and conditional growth. Outside the
   declared interval sizes saturate at endpoints; finite interpolation is not
   asymptotic approach. Step slopes depend on endpoint differences, not just
   step order. Probe `a=16,b=20,r=4/3,q=6/5`: step 0 difference is 4, step 1 is
   8/3, so universal faster higher-step growth is not established. These are
   analytic models, not browser or Utopia implementation/conformance claims.
4. Independently derive the published baseline audit midpoint and compare the
   actual printed step-0 declaration at root 16, extents 360/900/1440. Preserve
   declared small ratio 1.2 versus 1.25, 1.333 versus exact 4/3, base/endpoints and
   all numerical conflicts. Do not choose a hidden common configuration to make
   existing snippets agree. Explain ratio-orientation conventions before calling
   a written interval a numeric error. Attribution remains unassessed.
5. Reproduce the adopted diagnostic configuration by consuming its actual seven
   coefficient rows and actual step-0 expression from pinned bytes. Exact
   Fractions; six-place half-even serialization. Evaluate all seven steps at
   roots 16/20 and extents 160/320/800/1000/1280/1600: 84 exact-versus-printed cases.
   Compare table and CSS, negative steps, endpoints, saturation and interior
   widths. Record maximum error and all mismatches, not merely a bound.
6. Record five dimension results separately for the bounded claims; provide
   proof/counterexample and exact context for supported conclusions. Source
   fidelity is blocked for absent required originals or not assessed where the
   result is purely mathematical, never inferred from a successful computation.
   Relationship/CQ coverage and complete card/guide review remain unassessed.
7. Give occurrence-level proposed replacement text and later dependency owners
   in correction-handoff.md. Do not edit protected sources or accepted example.
   Reuse the adopted example as a diagnostic, with no house palette/fonts/roles,
   compulsory ratio or accessibility/beauty guarantee. Later implementation
   requires its own explicit source mutation scope and independent review.

## Discriminating oracles and proof limits

- Baseline midpoint at `t=1/2`, bases16/20 and ratios6/5,4/3: steps0–3 are
  `18, 344/15, 6592/225, 126656/3375`; adjacent ratios are
  `172/135, 824/645, 1979/1545`; determinant for steps0–2 is `64/45`.
  Equal-ratio and endpoint controls must still yield zero determinant.
- Printed baseline step 0 at root 16 and extents 360/900/1440 yields
  `16.19664,18.85560,21.33920` px, whereas the declared base model yields 16/18/20.
  These are author-reproduced rational oracles, not desired empirical conclusions.
- Adopted example: at root 16/extent 800 steps0–2 are17/20.85/25.5825 px;
  root 20/extent 800 step 0 is125/6 px; root 20/extent 1000 is21.25 px. The inherited
  84-case maximum is3/250000px; independently derive the new observed maximum.
- Reject an altered printed step 0 A coefficient (+1/10) through the same
  table-consuming numerical predicate used for the positive 84 cases. Reject
  fixed320–1280px endpoint reuse at root 20 (21.25 vs125/6 at extent 800). Reject
  universal interior geometricity with the unequal-ratio determinant/ratios;
  preserve valid equal-ratio/endpoint cases. These controls address real defects.
- Arithmetic model uses `max(lower,min(preferred,upper))` with ordered bounds
  and declared `1vi=w/100` numeric interpretation. No rendering, CSS parser,
  writing-mode/viewport behavior, root-preference/zoom, reflow, font, contrast,
  empirical science, AT or WCAG conclusion follows from this assignment.

An incidental Python standard-library calculation recorded in execution notes
is sufficient. Do not build a reusable validator/package/runtime, introduce a
maintained script or add a broad mutation framework. Every checker names its
new slice/pins/population; do not execute old checker code uninspected or count
predecessor-only assertions as this slice's verification.

## Output and preservation contract

Artifacts home: this slice's `artifacts/`, created as outputs are produced.
CC may create/update exactly seven paths relative to this slice:

1. `artifacts/fluid-scale-proof.md` — definitions, derivation, special/boundary
   cases and mathematical/perceptual/runtime scope.
2. `artifacts/claim-results.jsonl` — all bounded mathematical occurrences, exact
   source witnesses, evidence, five separate results and proposed disposition.
3. `artifacts/configuration-reconciliation.md` — declared/actual configurations,
   literal snippets, complete numeric comparisons and disagreements.
4. `artifacts/correction-handoff.md` — exact proposed replacements/dependencies,
   finding coverage, and explicit source/fidelity/remaining-review gates.
5. `artifacts/execution-notes.md` — intake/readback, actual queries/calculations,
   outputs/counts, failures/recoveries, negative controls and unrun scope.
6. `ledger.md` — evidence/proposed dispositions only; keep all rows open.
7. `closing-report.md` — CC proposed return with all nine rows, seven-output
   inventory, silent-drop walk and bubble-up; no acceptance or next-slice claim.

Reuse the accepted local result shape, adapting `card` to `subject` for live
file occurrences: path/hash/span/assertion. Retain claim_id, evidence, dimensions,
actor/method_revision, subject_history/dependencies, blocked input/owner/re-entry,
disposition and independent_review. This is a local procedural record, not a
Project08/public schema. Derivation evidence points to the exact proof artifact
revision/hash and section/equation; avoid dangling witness IDs or pretending an
analytic proof is an original source quotation. JSONL parse/referential checks
cover all emitted rows, without predeclaring a semantic claim count.

Protected: all earlier planning artifacts, prompts and acceptance records;
current project/arc/slice plans and issued prompt; entire SOURCE/design tree,
main index/branch, packaging, original sources and unrelated work. CC commits
only the seven named outputs with both repository trailers. SOURCE unchanged
means no Make/package gates are required here; record them as unrun/later scope.
Run exact path/pin checks, full JSONL/witness/evidence resolution, local links/
fragments, final LF/no CRLF and `git diff --check`. Independent CDC review remains.

## Assignment history

Current assignment: [Iteration02](cc-prompt-iteration02.md), issued 2026-10-09.
CC executes the focused correction and returns to CDC via the Operator.

- Initial [cc-prompt.md](cc-prompt.md), issue `3a18c51d`, returned as `e0f68c31`:
  historical partial acceptance; five done/four open. Preserved unchanged.
- [Iteration01](cc-prompt-iteration01.md), issue `24ae8a8b`, returned as
  `4e678b0b`: first executed refinement, independently partially accepted.
  F01/F02 and the corrected handoff accepted; six done/three open after residual
  F03 and new F04. Superseded for execution; prompt/return remain historical.
- [Iteration02](cc-prompt-iteration02.md): second refinement assignment, active.
  Repair TY-01's applicable conflict join and the current intake receipt;
  S01-01/02/09 remain open. No criterion/model/source-gate amendment.

### Iteration02 bounds and author readiness

Exactly four CC paths: artifacts/claim-results.jsonl, artifacts/execution-notes.md,
ledger.md Evidence/Notes only, and closing-report.md. Preserve the six-done/
three-open CDC statuses and criteria. Configuration, handoff, proof and all
numeric tables/deltas are protected. Change TY-01's evidence/affected references
and observation wording only; preserve subject and supported conclusions. The
prompt specifies configuration 50 as the conflict witness, preserves52 for
orientation, and requires a control rejecting the old 52-only conflict join.

CDC reloaded the governing project body, full Arc02 and slice plans, ledgers,
actual candidate delta, all 297 SOURCE witness lines, TY-01's complete record
and actual configuration witnesses. Prompt-authoring/intake/readiness,
iteration-preservation and correction-retention guidance determines the small
repair and exact four-path boundary. The issued 24ae Arc02 plan has137 lines at
the recorded SHA; no earlier loaded extent can be reconstructed from 131 alone.
Fresh pinned complete reading plus preserved historical discrepancy is the
required remedy. No new scientific claim, source acquisition or design choice
is assigned. Current prompt/plan/ledger and changed-data queries form a bounded
reading packet (approximately 12–18k tokens with correction/review headroom);
unchanged mathematical evidence is retained under the independent review rule.
Semantic applicability and honest receipts have distinct positive/negative
checks; counts/hashes alone do not prove either. Scope and partial-return gates
remain explicit, with no new maintained validator or reporting artifact.

### Historical Iteration01 bounds and author readiness

Original criteria/model/pins/populations remain binding. CC may update only
claim-results.jsonl, configuration-reconciliation.md, correction-handoff.md,
execution-notes.md (all under artifacts/), ledger.md evidence/notes and
closing-report.md: six paths. Proof, accepted example, sources, plans, prompts,
review and every other path are protected. Numerical tables/formulas/deltas
remain unchanged; evidence pointer SHA/blob/ranges may update to the actual
revised analysis artifact bytes. Preserve original 33 IDs and append omissions;
there is no final-count oracle. All done/open statuses are CDC-owned.

CDC freshly read all 297 witness lines and reviewed every emitted result's
context/dimensions/evidence; independently reproduced actual 84 cases and52
nonzero deltas. The review supplies exact source distinctions and repair shapes.
The prompt-authoring/iteration/row-closure rules support a focused evidence repair
with full source-to-output and semantic pointer inspection, not new tooling or
source acquisition. Checks distinguish valid alternative examples from actual
same-default conflicts and missing/irrelevant witnesses from valid ones. No
unresolved design choice is delegated; new contradictory evidence is reported.
Required reading budget is bounded to current contracts, changed outputs and
all nine spans, with unchanged proof/example retained for affected use.

## Author readiness — 2026-10-09

CDC read active project/arc inputs and required planning/prompt-authoring/ledger
routes; loaded knowledge/design/SKILL.md as the audited domain input and inspected
all nine source spans plus the adopted example. Source hashes/ranges are pinned;
main tracked/index clean. Author independently computed the baseline midpoint,
64/45 determinant, conflicting printed 16.19664/18.85560/21.33920 values and reversed
ratio growth 4 vs8/3. The old normative house defaults are superseded by the
Operator-approved composed contract; mathematical truth is kept separate from
its source-attribution and perceptual claims. testing's Proportionate Proof route
supports a small actual-artifact calculation and focused controls, with no new
maintained tooling. Required source-independent conclusions are resolved; actual
claim inventories/results are left to inspection. Partial and missing-input
behavior is explicit. Approximate input budget is 20–25k tokens with calculation/
review/iteration headroom; no full corpus/books or broad source acquisition is
assigned. No unresolved design choice is silently delegated to CC.

## Version History

- 1.2 (2026-10-09): Iteration01 independently reviewed at 4e678b0b; six done/three
  open, with current intake reopened. Issued four-path Iteration02 for residual
  F03 and F04; proof/numeric evidence retained and all wider gates unchanged.

- 1.1 (2026-10-09): Initial CDC review of e0f68c31 accepted five rows;
  issued focused Iteration01 for F01–F03. No scope/model/source-gate amendment.

- 1.0 (2026-10-09): Opened first Arc02 slice for bounded source-independent
  fluid-scale proof and numerical/correction evidence; all nine rows open.
