---
slice: slice02-nonlinear-colour-pipeline
status: open
depends-on: [arc01-portable-contract Operator-accepted composition]
---

# Slice02 — Nonlinear Colour Pipeline

## Goal and authority

Establish the technical/mathematical correction basis for DES-007 and the bounded
colour-uniformity/temperament assertions overlapping DES-002. Inventory the exact
selected occurrences, prove which operations are linear, reproduce identified
conversion models, and supply occurrence-level proposed corrections. This is
T-family evidence work under the [arc plan](../arc-plan.md),
[project plan](../../project-plan.md) and [nine-row ledger](ledger.md).
Whole-card/guide acceptance, live edits, original fidelity, source acquisition,
empirical perception studies and browser/package implementation remain later work.

CDC Sofie authors and independently reviews; separate CC executes the
[initial prompt](cc-prompt.md) through Operator relay. Two contributors, Expedited
Mode; CC proposes results, keeps every row open and cannot accept/close/advance.
Arc01 contract packet is `38b66d0de7d5e8cba98e7d588075f5c6d4ede90f`;
Operator closure is `fb33d8cf43e8bb99d9dc9835ded134bd8268933f`.
Slice01 is independently closed at `c3d68d7d`, recorded in planning predecessor
`9a306c6f49d61b9350e6b84d454da449deca5891`. Its arithmetic is retained evidence,
not assigned for another replay here. No readiness waiver or new scope reduction.

## Pins and complete bounded population

SOURCE/main: `dffa504e851b03b8e4746f1941068e4cc850b612`, tracked/index clean at
opening. Preserve pre-existing untracked `knowledge/lfe/` and planning
`project12-chcd-protocol/` without inspection. Use current plans/prompt at the
issuing commit containing this open set; record it before work. Method is
`759ce2dd116a4cfe03b72d43fd2791f48486251c`; composition is `38b66d0d`; audit is
`795ac75b7d02536e0e95252457ac3282cd17d8d8`. Always consume pinned Git bytes.

Read all six live spans, totaling 89 lines across four files. Inventory every
colour-conversion, OKLCH perceptual-uniformity and colour/temperament analogy
assertion in them, including repetitions, qualifiers and accurate counterclaims.
Unrelated type/unit/neuroscience assertions in the same context are explicitly
not assessed and remain in the later complete L/T populations.

| SOURCE-relative file | Inclusive spans | Context/purpose |
|---|---|---|
| `knowledge/design/SKILL.md` | 360–368 | Matrix-only summary and temperament comparison, with surrounding epistemic claims. |
| `knowledge/design/guides/foundations-of-design.md` | 239–254; 432–455 | Full pipeline versus matrix collapse; exact-brightness claims; rigorous/analogy labels and nearby qualifications. |
| `knowledge/design/guides/design.md` | 130–155 | Complete Principle II context; best-space/equal-jump/all-hue assertions; unrelated units retained as unassessed. |
| `knowledge/design/guides/colour.md` | 9–11; 542–552 | Subtitle and rationale repetitions; existing C&B values/roles are studied inputs, never adopted defaults. |

Read `knowledge/design/concept-cards/posts/matrix-transformation-colour.md`
completely (147 lines) as a contextual counterwitness. Inventory its conversion
teaching claims and examples relevant to this concern, including input-space,
linearity, nonlinear/inverse steps, matrix-generation distinctions and exactness
qualifiers. Record historical/attributed claims separately from mathematical
truth. Relationships, CQ components, GPU/ICC application claims and other
unassigned assertions remain explicitly not assessed. Full reading does not
establish complete five-dimension card review or reduce the 233-card denominator.

Prepared model evidence: `knowledge/design/sources/md/posts/a-perceptual-colour-space.md`
75–113 and 115–163 (88 lines), SHA-256
`ffe5494da6f0d040fb341d8e1f03d3e396600f6787088b6d57e32613798375f4`.
Read every formula, code statement, four-row example table and generation/use-case
qualification in those ranges. Decorative heading anchors at 73/114 are
reference-only; record necessary context extensions. Prepared comparison proves
what these bytes contain, not fidelity to an original capture.

Read current primary technical evidence at the explicitly dated
[CSS Color 4 Candidate Recommendation Draft, 9 October 2026](https://www.w3.org/TR/2026/CRD-css-color-4-20261009/):
§9.2, §9.4's OKLCH chroma/powerless-hue definitions, complete §9.5–9.6,
§10.2–10.3, and §19's non-normative notice plus `lin_sRGB`, `gam_sRGB`,
`XYZ_to_OKLab` and `OKLab_to_XYZ` functions. Read the public
[Oklab article](https://bottosson.github.io/posts/oklab/), from “Converting from
XYZ to Oklab” through “Converting from linear sRGB to Oklab,” ending before
“Motivation and derivation of Oklab.” Record URL, version/date, retrieved section
extent and limitations. These are read-only technical inspections, not acquisition
of the missing archival originals, immutable capture manifests or fidelity lineage.
Other linked pages are reference-only unless actually relied upon.

## Binding model and scope distinctions

1. Use the pinned article's named 2021-01-25 **linear-sRGB** coefficient generation
   for its forward/inverse RGB code. Consume the actual coefficients, operators
   and matrix input spaces from bytes; transcribe and check all values. Use the
   separately printed XYZ M1 and M2 for the four XYZ examples. Do not silently
   substitute newer CSSWG matrices, confuse XYZ M1 with the combined RGB matrix,
   or require exact cross-generation equivalence. Explain the coefficient/date
   distinction, retaining the article's application-specific qualification.
2. Decode each encoded sRGB channel before the linear-sRGB matrix: for `|c| <=
   0.04045`, `d(c)=c/12.92`; otherwise
   `d(c)=sign(c)*((|c|+0.055)/1.055)^2.4`. Encode linear channels using threshold
   `|x| <= 0.0031308`: `e(x)=12.92*x`; otherwise
   `e(x)=sign(x)*(1.055*|x|^(1/2.4)-0.055)`. Retain negative roundoff/extended
   coordinates for calculations; no early clipping or hidden gamut mapping.
3. Write `F_linear(v)=B*cbrt(A*v)` with real componentwise signed cube roots.
   Encoded input is `F_encoded(c)=F_linear(d(c))`. A is the combined linear-sRGB
   to LMS matrix; B is the LMS-prime to Oklab matrix. XYZ input has its distinct
   M1, also followed by cube roots and M2. Inverse uses the published inverse
   operations and componentwise cubes, then encoding for encoded RGB outputs.
   Rounded published coefficients yield approximate numerical round trips;
   distinguish these from exact inverse algebra and CSS conformance.
4. For positive lambda derive `F_linear(lambda*v)=lambda^(1/3)*F_linear(v)`.
   A nonzero white witness at lambda=1/8 disproves a single constant 3x3 linear
   matrix for the whole conversion: output scales by 1/2, not 1/8. Adjacent
   linear stages may concatenate; the nonlinear stage cannot be crossed.
   Treat transfer decoding, signed roots and inverse cubes as essential stages.
5. Describe Oklab-to-OKLCH as a polar coordinate change: `C=hypot(a,b)`, hue in
   degrees from `atan2(b,a)` modulo 360, `a=C*cos(h)`, `b=C*sin(h)`. For this
   mathematical round-trip diagnostic, hue is undefined at exactly zero chroma;
   preserve small nonzero chroma from coefficient rounding and do not call its
   hue meaningful. Separately describe CSS's powerless-hue epsilon and missing
   hue treatment from the dated specification. Do not apply CSS epsilon while
   claiming exact polar preservation or conflate analytic conversion with CSS
   parsing, clamping, gamut mapping or missing-component interpolation.
6. Mathematical operations do not establish equal perceived brightness across
   every hue/person/context, a uniquely best design space, universal contrast,
   palette quality or an identical equal-temperament mechanism. Scope OKLCH as
   approximately perceptual under its identified model; keep design analogies
   as analogies unless the claimed equivalence is actually established. Identify
   unsupported absolutes and limits of inspected evidence; do not invent a new
   empirical study or treat an unavailable original as false.
7. Practical proposed guidance must name input space/white point, output gamut,
   alpha/background/compositing context and evaluation of actual foreground/
   background/state pairs. These are dependencies for later palette/accessibility
   implementation, not a gamut/compositing/contrast algorithm or certification
   delivered by this slice. Retain supplied project identity and no C&B defaults.

## Case protocol and discriminating oracles

Use a small Python standard-library calculation in execution notes; no maintained
script, new package/runtime or broad test framework. Name this slice/pins and
show coefficient extraction/grammar, signs and all intermediate stages. Binary64
with signed real cube roots is sufficient; exact Fraction arithmetic is unsuitable
for irrational roots. Compare unrounded values; print at least 12 decimal places.

- **13 encoded sRGB cases:** all eight binary cube corners; three neutral triples
  `(c,c,c)` with c=0.04044, 0.04045, 0.04046; middle grey (0.5,0.5,0.5); mixed
  (0.2,0.4,0.6). **Three linear-sRGB cases:** neutral triples at 1, 1/8 and -1/8.
  Evaluate forward/inverse for all 16, without clipping. Report every component
  error and maxima/argmax; absolute round-trip tolerances 2e-6 encoded and 1e-6
  linear per channel. Transfer-threshold discontinuity/rounding are not perceptual
  defects or a license to normalize inputs silently.
- **Four XYZ cases:** consume all four actual published XYZ/Oklab rows at
  prepared lines 107–110. Compare all 12 components to the printed three-decimal
  results with absolute tolerance 0.0005. The Z-basis produces a negative LMS
  component; these basis vectors need not lie inside display sRGB. Do not clip.
- **20 polar cases:** use every forward Oklab output from the 13+3+4 cases;
  mathematical rectangular/polar/rectangular component error <=1e-12. Explicit
  exact-zero chroma and near-neutral hue limits; no hue-equality demand at zero.
- Author-reproduced numeric witnesses: decoded 0.5 is 0.214041140482;
  correct middle-grey L is 0.598180726623; skipping decoding gives 0.793700520804.
  White L is 0.999999993474; one-eighth linear-white L is 0.499999996737.
  XYZ (0,0,1) gives (0.152602580040,-1.414996551012,-0.448927203560).
  Check these displayed witnesses within 5e-10, independently deriving your
  values from the actual coefficients, not copying expected output as computation.
- Opening author calculation observed maxima: encoded 1.683913e-6, linear
  2.612846e-7, XYZ printed component 0.000397420, polar 2.775558e-16.
  These are sanity oracles, not a prescribed CC receipt or fresh CDC acceptance.
  Report actual observations and meaningful deviations rather than forcing them.
- **Three contrary controls through the same positive checking route:** remove
  cube roots and concatenate matrices (must fail XYZ table predicate and white
  scaling witness); skip sRGB decoding (must fail middle-grey L predicate);
  replace signed real roots with naive `x**(1/3)` (must reject complex/error/
  mismatched Z-basis result). Preserve the valid positive cases. Black/white-only
  round trips or regeneration from the same corrupted model cannot prove truth.

## Results, outputs and preservation

Inventory bounded occurrences with stable local IDs; no semantic claim count is
invented before reading. Adapt the accepted procedure's `card` to `subject` with
full path, SOURCE hash, inclusive span and literal assertion. Keep evidence and
five separate dimension outcomes/reasons/references, actor/method revision,
subject history/dependencies, blockers/owner/re-entry, proposed disposition and
independent review pending. Every local proof/numeric/paired-context reference
resolves to exact artifact/source revision/hash and span/equation/case ID.

For external technical observations, record the dated URL or actual retrieved
page identity, section/version/date and read extent. Do not invent an original
snapshot hash; explicitly mark it unavailable and name the fidelity limitation.
Hash any locally recorded observation/formula separately as derived evidence,
not as original website bytes. Mathematical conclusions can use their exact
local proof/model evidence. Any external-dependent technical conclusion needs
adequate inspectable primary support and later independent CDC reinspection;
unavailable required technical access leaves that result partial/blocked.
Original-source faithfulness stays blocked where P10-11 inputs are missing, or
not assessed for a purely mathematical result. No full-card/CQ/relationship
acceptance or source fidelity follows from successful conversion comparisons.

CC may create/update exactly seven slice-relative paths:

1. `artifacts/colour-conversion-proof.md` — model, assumptions, stages,
   nonlinearity proof, inverse/polar distinctions and scope.
2. `artifacts/claim-results.jsonl` — complete bounded occurrence population,
   exact five-dimension evidence/results and explicit unassessed boundaries.
3. `artifacts/numerical-reconciliation.md` — actual coefficient generations,
   table/case/intermediate values, errors/maxima and the three controls.
4. `artifacts/correction-handoff.md` — occurrence-linked exact proposed
   replacements, DES-007/limited DES-002 accounting and later dependency owners.
5. `artifacts/execution-notes.md` — intake/readback, source/read receipts,
   calculation/replay code, results, failures/recoveries and unrun work.
6. `ledger.md` — evidence/notes and proposed dispositions only; every row open.
7. `closing-report.md` — nine-row proposed return, exact output inventory,
   silent-drop/bubble-up and limitations; no acceptance/closure/next assignment.

Artifacts directory is created as actual outputs are produced. This procedural
result adaptation is not a Project08/public card schema. All previous planning
records, current plans/prompt, entire SOURCE tree/index/main branch, original
sources, packaging and unrelated work are protected. Commit only seven named
outputs with both repository trailers. Required checks: exact pins/path scope,
strict JSONL/all subject and evidence joins, entire case/control population,
local links/fragments, final LF/no CRLF and `git diff --check`. Planning-only work
requires no Make/package/browser gate; record those as unrun/later scope.

## Assignment history and author readiness

Current assignment: initial `cc-prompt.md`, issued with this open set. No prior
CC return or acceptance; `cdc-verification.md` will be created by actual review.
CDC owns next review/decision; Operator retains original inputs and release gate.
All nine rows start open. Any new normative dependency or crossed qualification
boundary must be read before dependent work, with an actual receipt. Source drift,
contradictory required evidence/oracles, needed mutation or a scope decision
outside this plan stops the affected work; continue independent work honestly.

CDC author inspected all six live spans, the entire 147-line counterwitness,
prepared 75–113/115–163, the 83-line pinned procedure, relevant accepted contract/
handoff and DES-002/007 sections; primary public conversion/dated CSS sections
were browsed. Source file hashes/counts were measured from pinned blobs. Required
planning/framework/workflow guides were loaded with bounded truncation recovery.
Combined read outputs were truncated; required active plan/prompt/ledger and
contract portions were recovered in bounded reads. Two guidance lookup attempts used a
planning-relative path where SOURCE was required, then the canonical SOURCE
path was loaded; no missing guide was treated as read.

Author's incidental coefficient-consumption calculation initially rejected an
inverse-row width assumption, then found incorrect example-table bounds and a
header parse; widths/operator signs and exact numeric rows 107–110 were repaired.
The successful replay consumed actual coefficients and all 20 cases, checked
16 round trips/12 table components/20 polar returns and rejected all three
contrary variants. No pending author validation failure remains. Author sanity
checks do not accept CC's later work. The transcript/code is incidental, not a
new maintained source asset; CC records its own exact code and receipts.
A path-check helper initially treated a protected untracked name as a required
tracked blob; the failed Git lookup was corrected by limiting extraction to the
required manifest. The untracked directory itself was not inspected.
Final opening checks preserve all existing parent criteria/statuses and Slice01
bytes: exact seven CDC paths, three new slice documents and nine open rows;
47 local destinations/12 fragments, final LF and diff check pass. These are
opening consistency checks, not execution or independent acceptance of Slice02.

Sizing: one technical concern, six live spans/89 lines, one contextual card and
88 prepared lines, narrowly bounded primary sections and five durable artifacts.
Room remains for derivation, complete occurrence results, error controls and
corrective iteration; no whole 233-card/eight-file review is squeezed into this
slice. If actual qualifications require a larger technical assignment, bubble
it up for a concrete split before pretending this bounded slice completes it.

## Version History

- 1.0 (2026-10-09): Opened source-grounded T-family colour-pipeline evidence
  after independent Slice01 closure; complete corpus/readiness gates retained.
