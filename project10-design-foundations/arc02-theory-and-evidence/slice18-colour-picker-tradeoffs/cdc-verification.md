# Slice18 — CDC verification

## Initial independent review — 2026-10-17

CDC Sofie reviewed separate CC's source `7b20ccc3a7019cfad6f238522314ce8ab70e0a35`
and planning return `cc1f7ceb0f33528554f20256d66c88310c6f1318` against initial
issue `fe91602e2b732da71f29d2e790d25c7f85477da6`. Two contributors; Expedited
Mode. **Two rows accepted, two open. Slice18 remains open; no successor.**

The source candidate's actual parent is `c6a089ba8f0809d9147ea60d66e3d78f02bd4792`,
an external Fennel import. Its entire design tree matches assigned `4e635bb3`.
Current main `c9d98a3ec3d0a24c30a18431d7aeaa13f6451872` adds separate Fennel
delivery; its design tree matches the candidate. Planning review HEAD
`5d8f3a9ffed74dbf69255956e450b855a10a3ed6` preserves the CC Project10 bytes.
Neither external change is part of CC's Slice18 delta. No source edits by CDC.

### Independent checks

Read the active project then arc and slice plans/ledger criteria, issued prompt,
complete eleven revised cards, batch record and closing report. Compared the
prepared source passages, accepted Slice17 terminology and actual claim deltas.
Applied Concept Cards evidence-lifecycle/graph-CQ guidance and visual-design's
model-versus-rendered-perception boundary. Original captures and source figures
were not independently verified.

- Exact candidate scope: thirteen authorized source paths; planning three.
  Both candidate messages have both required trailers; `git show --check` passes.
  Initial prompt/plan and all four ledger criteria/statuses survive CC unchanged.
- All233 card paths/identities retained; eleven changed,222 byte-identical;
  all161 source files and all guides unchanged. Eleven literal Source References
  and complete heading sequences match the assigned baseline.
- Parsed all233 YAML headers with Ruby/Psych and checked raw representation.
  Only the authorized six Rosetta rating/note scalars and one CSS association
  removal differ. Nested data, order and null/empty distinctions survive.
  The first temporary raw-header predicate assumed two-space scalar indentation;
  inspecting the four-space source and correcting that predicate produced a pass.
- SKILL differs only in owning version1.0.14→1.0.15. Removing the newly inserted
  history entry restores the prior file exactly. An initial temporary check
  wrongly required literal end-appending; the actual history retains old bytes
  and inserts the entry beneath its title. No source repair was needed.
- Fresh sequential `make help`, `make check-skills`, `make check-skill-versions`,
  `make check-package-paths`, then separate `make design` all pass at current main.
  Version gate:25 source skills/25 packages/zero errors. Description check:19
  above the soft300-character target; design remains360. Paths:zero hard failures,
  596 warnings/594 locations,three exceptions,796 skipped external URLs. Counts
  include external Fennel integration; CC's earlier24-package counts are historical.
  All eight design ZIP Markdown members equal committed `7b20ccc3` bytes;
  SHA256 `716e3a3cea6073296a1ed961d25ac21c6c1a5841da83658c14ecf317d25befe8`.
- Independently replayed HSL/HSV via Python's separate `colorsys` implementation:
  RGB(.8,.2,.2) gives HSV(0,.75,.8), HSL(0,.6,.5); grey.2/.5,black/white give
  both S=0 and V=L=g. Stored hue0 is conventional, not a measured neutral hue.
  Toe/inverse at0,.125,.5,1 and synthetic rational map/inverse at s=0,.4,.8,.9,1
  reproduce the printed results within1e-9. Toe(.5)=.42114056260896976;
  inverse(.5)=.568838198942395. Rational C=.048/.12/.1488 at s=.4/.8/.9;
  C0 is the initial slope, not C(0). Okhwb(.4,.5) gives w=.3,b=.5 and inverse;
  black's inverse denominator is zero. These are arithmetic/source checks,
  not execution of omitted helpers or perceptual tests.
- All66 header-edge tuples match the pinned source exactly; table directions
  match the method. All65 predecessor row IDs and six newly labelled statements
  are enumerated; final bodies contain65 relationship-list statements. All15
  frozen CQ occurrences retain their9/4/2 membership. These structural checks
  do not repair the semantic problems below.
- Returned three planning records:14 local links/11 fragments resolved,LF/EOF
  passed. Eleven revised cards:LF/EOF passed,no local Markdown links to resolve.

### F01 — Residual HSV/Okhsv teaching contradictions

At `7b20ccc3`, `hsv.md:79` infers that an S=0 achromatic axis produces different
perceived hues from the source's deep-blue shift example. Prepared112–143 reports
a shift as saturation decreases; it does not assign hue to the neutral endpoint.
The card's own neutral rule correctly says hue is powerless. At line102 it
contrasts HSV V and HSL L on neutrals, although both equal g for RGB(g,g,g), as
the batch's own grey witness confirms. Use the actual chromatic distinction.

`hsv.md:75` still promises brightness adjustment while keeping hue consistent;
`okhsv.md:86` still speaks of adjusting brightness while preserving saturation
relative to maximum. Distinguish changing model V/v at fixed numeric H/h or S/s
from preserving perceived brightness, hue or CIE saturation. Also reconcile
HSV's Common Confusions description with its exact Δ/M formula: the source's
rough appearance description is not an exact universal saturation definition.
Do not remove the useful control application or attributed blue example.

### F02 — Repeated source error and lost positive definitions

- `colour-gamut.md:73` labels the figure's horizontal coordinate plain chroma.
  Prepared345–349 explicitly uses C·L_r/L; the corrected Okhsv card already
  recognizes this. Retain the triangular approximation/curved-top qualifications
  and disclose that the figure itself was not inspected. Its verification note
  also calls the frozen2026-10-09 CSS document an Editor's Draft; its identity is
  the [Candidate Recommendation Draft](https://www.w3.org/TR/2026/CRD-css-color-4-20261009/).
- `colour-picker-design-principles.md:61` attributes a Munsell comparison profile
  to the article's tables. Prepared284–297 compares HSV,HSL,HSLuv,Lab-like,NCS;
  749–758 compares Okhsv/Okhsl. Munsell is historical context, not a table column.
- `chroma-vs-saturation.md` replaced the accepted Slice17 positive distinction
  with unspecified “distinct reference relationships.” Restore what differs:
  [CIE saturation](https://cie.co.at/eilvterm/17-22-073) relates colourfulness to
  the area's own brightness; [CIE chroma](https://cie.co.at/eilvterm/17-22-074)
  uses the brightness of a similarly illuminated achromatic reference. Both
  primary entries were freshly inspected. Preserve model C/hypot and HSL/HSV
  distinctions and conditions; no universal C/L formula follows. The batch's
  chroma/saturation answer currently repeats that definitions differ without
  supplying this distinction, so its claimed adequacy needs correction too.

### F03 — Header warrants are templates, not connecting evidence

The66-row table enumerates edges but repeats generic statements and broad P1–P8
lists. For example row1 asserts a local colour-gamut Related statement connecting
HSL; that section contains only “Colour spaces.” Row42's HSL/CSS-syntax edge
gets the same generic all-premises list as unrelated historical comparisons.
These references neither identify the actual connecting claim nor explain it.

Replace generic warrants with actual endpoint premises and reasoning. Compact
groups with exact member row IDs are sufficient; no66-paragraph requirement or
new registry. Example: gamut↔HSL/HSV connects the card's bounded in-range RGB
parameterization to their specified RGB gamut; it is an editorial association,
not a nonexistent literal Related bullet. HSL↔hsl-css-syntax connects its classic
coordinate model to the accepted CSS notation/normalization rules, not numeric
interchangeability with Okhsl. Learning prerequisites remain useful background,
not strict mathematical requirements. Keep source/inference distinctions.

Update affected body joins, five-dimension outcomes and actual CQ component
answers after F01/F02. Preserve unaffected memberships and historical results.
P4 should include the actual345–425 Okhsv geometry premises when invoking them.

### Row dispositions and next action

| Row | CDC status | Basis |
|---|---|---|
| S18-01 | open | Useful model recipes and arithmetic pass; F01/F02 leave false or incomplete teaching. |
| S18-02 | open | Populations/directions preserved; F03 and the lost CQ definition remain substantive gaps. |
| S18-03 | done | Independent complete preservation/exception checks above. Renew after the body-only correction. |
| S18-04 | done | Owning integration, fresh native/package checks and bounded return independently checked. Changed semantic results still require review under01/02. |

[Iteration01](cc-prompt-iteration01.md) authorizes only five affected card bodies
and the existing three CC return paths. Keep1.0.15 and all metadata/citations/
headings fixed. Retain unaffected arithmetic and package results after checking
applicability; no complete converter, new inquiry, schema or receipt-only chain.
Routine refinement stays in this slice; project/arc plans and criterion states
need no change. P10-11 fidelity, full corpus/global/live review, browser/AT,
final hosted rendering, composition and release gates retain their owners.

## Iteration01 independent review — 2026-10-17

Reviewed CC source `7068045aacd6cb75b856786a1de070791f21c2a8` and planning
`0cf5991ea5465d89d4d6807f7c17cc255bd0a7e8` against Iteration01 issue
`c5670897d904c4d5dcb44902dd4928d6882cfe23`. **Current verdict: three done,
S18-02 open. Source teaching accepted; evidence corrections still required.**
This supersedes the initial two-done row accounting, not its recorded findings.

### Reproduced changes and retained evidence

Read all five revised bodies completely, their exact source diff, current
closing report, all66 header rows and19 warrant groups, affected body/CQ records
and iteration receipts. Compared F01/F02 repairs to the inspected prepared-source
and CIE definitions from the initial review. Source no longer attributes hue
to the neutral endpoint; the chromatic and grey examples agree with the formulas.
Numeric H/h,S/s controls are distinguished from appearance guarantees. The
scaled gamut axis, two actual comparison tables and positive CIE definitions
are repaired, including their repeats and CQ contribution. F01/F02 are resolved.

Independent `colorsys` replay reproduces RGB(.8,.2,.2)→HSV(0,.75,.8) versus
HSL(0,.6,.5), and greys.2/.5→both S=0,V=L=g within1e-9. Hue0 is merely stored
convention at the neutral. The six other cohort cards and accepted toe/rational/
Okhwb formulas/examples are byte-identical to the initial reviewed state, so
retain their initial independent results and source limits; not fresh reruns.

Exact source commit:five authorized card paths, parent
`c5e743abb40db2f14b9332cea635a30f8b8a8d5b`. That parent's only delta from
assignedc9d98a3e is a separately committed README deletion, outside this assignment.
Exact CC planning commit:three authorized return paths. Both commits carry both
trailers and pass `git show --check`. Issued prompts, plan, CDC record, ledger
criteria and all prior row statuses survived CC unchanged.

Reproduced233-card path/header identity preservation, all233 raw metadata prefixes,
five literal Source Reference/heading sequences,228 unchanged cards and161
unchanged source files. All other code/guides/skill/history/package inputs are
unchanged fromc9; only the unrelated README deletion lies outside the five
card-body differences. Source remains unmodified by CDC. Source has the same
untracked LFE directory; planning was clean before this review.

Retain initial CDC native gates atc9: the complete delta changes only five
unbundled card bodies and unrelated README, with no changed gate, dependency,
Make or packaged Markdown input. No implicated execution condition changed.
The existing archive still compares8/8 to committed source7068045a and retains
SHA256 `716e3a3cea6073296a1ed961d25ac21c6c1a5841da83658c14ecf317d25befe8`.
This is a current byte comparison of the prior build, not a fresh Make run.
Three CC planning records pass16 local-link/12 fragment checks and LF/EOF;
five edited cards pass LF/EOF and whitespace checks.

### F04 — Body dispositions were overwritten

In the current batch's “Body relationship statement joins,” **all65 rows** have
lost their retained/rephrased/removed dispositions and literal final joins.
Each now has four cells under a three-column header, with an empty disposition
cell and a header-warrant reference. Example: body row7 is HSV→HWB but now points
to W01, a gamut↔HSL/HSV association. Header and body row numbers are different
populations. This is a semantic join regression as well as malformed Markdown;
the report's claim that only body join11 changed is false for the returned bytes.

Restore the complete accepted predecessor table from planningc5670897, then
update only body row11's final text to the corrected HSV/HSL contrast. Preserve
the65 predecessor identities and six separately listed final additions. Verify
actual before/after dispositions and final source text, not row counts alone.

### F05 — One wrong endpoint and incomplete grouped premises

All66 header tuples occur exactly once in19 groups; the structural membership
check passes. It does not catch these content errors:

- Header row35 is `okhsl contrasts_with hsl`; W09 instead discusses **HSLuv**.
  Supply the HSL encoded-RGB versus Okhsl Oklab-derived construction comparison.
- W14's Okhsl mapping support cites345–425, which is the **Okhsv** construction.
  Use actual Okhsl513–531/659–758 with the HSL106–178 premises and endpoint text.
- W05 combines17 prerequisites with “HSL/HSV, gamut, or orthogonality” background
  but omits row21's actual `colour-picker` prerequisite and leaves the other
  target-specific connections implicit. State the small set of distinct reasons
  once with exact member IDs; no need for17 separate essays.

The iteration summary says W01–W23, but only19 groups are defined (IDs have gaps).
Correct the current summary to the actual membership; no cosmetic renumbering.
Keep the remaining sound groups and bounded CQ answers. F03 remains unresolved
through F04/F05; it is not fixed by the passing66-ID check.

### Current row dispositions and next action

| Row | CDC status | Current evidence |
|---|---|---|
| S18-01 | done | All eleven available-evidence teaching outcomes retained/reviewed; five repaired bodies and positive examples pass. Graph/CQ reconciliation is separately open under02. Original fidelity remains outside this bounded acceptance. |
| S18-02 | open | F04 body-join regression and F05 mismatched/incomplete header premises. |
| S18-03 | done | Renewed233/header/citation/heading and protected-file comparisons at7068045a. |
| S18-04 | done | Source/planning integrity reproduced; independent native/package results retained with explicit unchanged-input checks. Current semantic evidence defects belong to02. |

[Iteration02](cc-prompt-iteration02.md) is a **planning-record-only** repair of
the batch and closing report. Freeze every source file and retain1.0.15; no
further source commit or Make run is needed for those records. No new inquiry,
validator, source acquisition, schema or successor. Routine same-slice repair
does not change project/arc plans or any parent criterion. Existing P10-11,
full-corpus/global/live, actual browser/AT, hosted, composition and release
requirements remain open with their recorded owners. Slice18 is not closed.
