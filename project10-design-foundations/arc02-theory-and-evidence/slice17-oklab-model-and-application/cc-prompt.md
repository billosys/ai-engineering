# CC — Slice17 Oklab Model and Application

Execute Project10/Arc02/Slice17 and return to CDC Sofie through the Operator.
Two-Contributor Workflow; Expedited Mode. This is integrated source repair,
not an analysis-only handoff. No push, publication, self-acceptance or new inquiry.

SOURCE=/Users/oubiwann/lab/billosys/ai-engineering, main pin
`4acfec6d8fa17e1ecb869bda28a6e71d17ef771e`.
PLANNING=SOURCE/.worktrees/planning, predecessor
`bddbda7bbcce1955164c7bad4074c7cecdf90873`; issue is the commit adding this file.
S=project10-design-foundations/arc02-theory-and-evidence/slice17-oklab-model-and-application.
Confirm the [assignment](slice-plan.md#assignment-history), [ledger](ledger.md),
worktrees and drift. Preserve unrelated work and staging, including knowledge/lfe/.
All four rows start open. Missing historical captures remain P10-11, not a reason
to postpone technically supported corrections in these files.

## Implementation spine

Read each full card and actual source passage; repair the following statement
families throughout definitions, properties, procedures, examples, relationship/
question explanations and Verification Notes. Preserve the useful teaching.
Local prose is your discretion; the semantic boundaries and preservation rules
below are binding. Do not leave an opposite claim later in the same card.

| Card / family | Required resulting teaching |
|---|---|
| perceptual-uniformity; oklab; repeated lightness/chroma/interpolation claims | Distinguish ideal uniformity from Oklab's approximate fit under stated conditions. Independent coordinates are a modelling goal, not an appearance guarantee for every hue/context/display. Keep the article's examples attributed; do not infer uninspected image observations from prose-only preparation. Correct the impossible “constant hue ... across hues” recognition instruction to the actual constant-L/C hue sweep. |
| colour-space; xyz-colour-space | Scope a colour coordinate system to its model/observer/reference and representable domain; do not promise unique polar hue at zero chroma or every visible colour in every device gamut. XYZ is a linear tristimulus representation, not a requirement that all operations/conversions involving it are linear. X/Z are not standalone chrominance channels. XYZ is a useful route, not a mandatory intermediary for every conversion. Source's pure-X/Y/Z test coordinates are arithmetic fixtures, not verified visible display colours. |
| d65-whitepoint; oklab | D65 reference versus a rounded table vector; diffuse reference white is not an absolute display maximum. Shared D65 avoids that adaptation step, not gamut/encoding differences. CSS Lab/LCH and prophoto-rgb use D50; CSS Oklab/OkLCh use D65. Adapt differing reference whites rather than routinely re-deriving Oklab. Do not call every CSS space D65 or describe CIELAB generically as D65. |
| lms-cone-responses | Distinguish biological cone signals from Oklab's fitted cone-like intermediate. Lowercase l/m/s and uppercase Oklab L are different subjects. The source's approximate transform does not establish physiological accuracy or universal non-negative intermediates throughout every extended input domain. Use real signed cube roots for negative test intermediates. |
| oklab-conversion; matrix-transformation-colour; oklab | Encoded sRGB first decodes; linear-sRGB matrix→real cube roots→opponent matrix; inverse reverses the stages and re-encodes for encoded output. Keep XYZ M1 distinct from combined linear-sRGB coefficients. Adjacent linear stages compose, the complete nonlinear route does not. Use internally matched published coefficient sets; do not silently replace article coefficients with a different CSS family or demand exact identity from rounded numbers. The2021 update note applies to the linear-sRGB code; do not claim it dates every XYZ matrix. Distinguish linear (zero-bias) from general affine and exact algebra from finite numeric round trips. Fix “M1 takes [linear] RGB” where the actual printed M1 takes XYZ. Keep code examples accurately labelled as excerpts, not a verbatim pair when inverse code is absent. Neural-network similarity is an analogy, not a physiological/learned equivalence. |
| lightness-perceptual | Oklab L is not HSV V, CIELAB L*, XYZ Y or WCAG relative luminance. In particular it is not simply cbrt(Y) for arbitrary chromatic colours. Use the accepted rendered-sRGB pair method for WCAG; L-based palette candidates cannot certify contrast. Explain approximate grey/tonal construction, then gamut/render checks. |
| chroma-perceptual | C=hypot(a,b) is exact within stated coordinates. It is a model-specific chroma correlate, not universal absolute colourfulness or a guaranteed appearance step. Do not define all saturation as C/L, infer that rule from a Wikipedia link, or identify HSL/HSV S with perceptual saturation. CIE chroma refers colourfulness to similarly illuminated reference white/grey brightness; perceptual saturation relates it to the stimulus's own brightness. Keep coordinate units/model references explicit. CSS's0.4 percentage reference is not a hard maximum C. |
| gamut-srgb | The triangle is a chromaticity projection; bounded sRGB gamut is3D. A blue-fold constraint does not prove global convexity. Separate valid coordinates, mathematical conversion and destination representability; check target linear RGB in[0,1] with declared numeric tolerance. Wide gamut and HDR are distinct; P3/Rec2020 do not universally supersede sRGB. Pointer's dataset is a bounded empirical surface-colour dataset, not proof of every physically possible colour. |
| colour-interpolation-perceptual | Only t=0.5 is the arithmetic midpoint. Cartesian Oklab lerp and polar OkLCh interpolation trace different paths. State degrees/radians, shortest/longer hue choice, powerless hue at C=0 and alpha premultiplication where relevant. Encoded-sRGB interpolation is a valid selected/legacy method, not intrinsically an error; space choice changes results. It often darkens/grays mixes rather than universally producing light-grey dark-colour midpoints. Host syntax selects CSS interpolation; an endpoint written oklab() or a keyframe alone is not an explicit gradient-space instruction. Keep source Photoshop/browser adoption as its dated2025 report, not a tested current default. |
| colour-space-comparison and repeated table claims | Preserve literal numbers/quotes, scope rankings to the author's actual datasets/metric/scaling and note generated CAM16 lightness/chroma data is not independent human ground truth. The table contains HSV, not a quantitative HSL test. Describe the coordinate-swap method accurately, including per-pair minimum of the two colour differences before RMS. Do not turn source plots into universal superiority or dismiss CIELAB as categorically unusable. |

Music comparisons retain the skill's personality **as loose analogies**:
12-TET logarithmic frequency ratios and a fitted3D colour transform are not
identical mathematics or universal equal-appearance/equal-auditory-distance laws.
Answer the exact music CQ by correcting its false equivalence premise. Keep the
mathematical operation's literal rigor separately scoped. Do not add new music
history or a psychophysics literature investigation.

**Dependent consistency repair:** read complete posts/chroma-vs-saturation.md.
Correct only the chroma/perceptual-saturation/HSL/HSV-relative-chroma statement
family wherever repeated (including recognition, examples and notes). Preserve
the useful attributed HSL/HSLuv comparison, separate model parameters from CIE
appearance terms, and remove unproved pale-pastel/independent-of-lightness or
universal “max chroma around50%” tests. Its frozen header/citation stay intact.
This is a bounded endpoint repair, not full-card/Okhsv-family acceptance. Record
the exact supported and still-unreviewed scope instead of an extra full-card claim.

**Live reconciliation:** in foundations-of-design.md, only (a) the OKLCH/OKLAB
paragraph under Colour Theory and (b) the brightness→gamma/Oklab sentence in the
Stevens paragraph may change. Remove the ungrounded “most important” ranking and
undated support/default implications; use current syntax as a scoped method.
Replace the claimed universal brightness exponent explanation with the distinction
that a display transfer curve and Oklab's chosen cube-root stage have different
purposes/assumptions, rather than a derivation from one brightness exponent.
Preserve adjacent area/spacing claims as outside this assigned review, recording
their remaining Arc02 live-guidance warrant owner. Keep the already qualified
temperament/matrix paragraphs, optional tokens and portable identity unchanged;
read the colour/design guide perception statements for cross-file consistency.

## Existing-header exceptions and preservation

Exactly eleven existing scalar values may change, with YAML structure/order and
all other bytes/types/values frozen at the pin:

| Card | Existing field | Required change |
|---|---|---|
| perceptual-uniformity | related[2] | `cielab` → `colour-space-comparison`: no cielab card exists in the233 roster; the existing comparison card actually supplies this reading route. Record this one route replacement explicitly, not a new concept or hidden drop. |
| perceptual-uniformity | rosetta_stone[0].rating and .note | `rigorous` → `loose`; qualify music analogy as above. |
| perceptual-uniformity | rosetta_stone[1].note | Distinguish ideal metric/perception correspondence from an imperfect fitted model. |
| colour-interpolation-perceptual | rosetta_stone[0].rating and .note | `structural` → `loose`; remove auditory/visual guarantees and the just-intonation comparison asserted as explanation. |
| colour-interpolation-perceptual | css_implementation[0].property and .example | `background`; `background: linear-gradient(in oklab, red, blue);`. This explicitly selects a space; preserve its existing support value as predecessor metadata, not new browser evidence. |
| oklab-conversion | rosetta_stone[0].concept and .note | State linear transform→pointwise real cube root→linear transform for already-linear sRGB; encoded sRGB needs decoding first. Retain rigorous only for the literal stated composition. |
| xyz-colour-space | rosetta_stone[0].note | Bound linearity to the tristimulus representation/linear stages, not every operation or complete conversion. |

All14 literal Source Reference sections, original headings and remaining metadata
(including source identity, confidence, questions, aliases and other edges) stay
unchanged. Preserve quotes or label an explicit corrected paraphrase. In each
primary card, distinguish predecessor extraction/verification notes from current
technical support; do not relabel old confidence as a new grade, claim historical
capture fidelity or invent browser checks. Concise accurate notes suffice; no
project-process narrative or long boilerplate is needed in teaching prose.

## Focused proof and local semantic work

Use the article's literal coefficient family for its examples. Temporary numeric
work is enough; no reusable conversion library, new validator or mutation suite.
Retain accepted Slice02 numerical evidence only after checking actual formulas,
coefficients, claim scope and conditions; do not reconstruct that earlier audit.
Freshly check any newly printed/changed example. These discriminating cases guide
the correction (ordinary double precision; indicated approximations are not exact):

1. Input stage: linear RGB(.125,.125,.125) → L≈.5, a/b≈0; encoded RGB(.5,.5,.5)
   decodes to(.2140411405,...) → L≈.5981807266, versus≈.7937005208 if misread
   as linear. For the published rows, F(.5·white).L≈.79370052 but .5F(white).L≈.5:
   the whole route is not linear. Rounded reference-table values do not warrant
   exact equality. Preserve signed-root handling (e.g. XYZ(0,0,1) gives negative
   first LMS intermediate with the printed XYZ M1); do not label that test visible.
2. Polar: (a,b)=(.1,.1) gives C≈.1414213562 and h=45deg, with inverse using
   radians internally. Shorter hue350→10 at halfway is0deg modulo360; naive
   arithmetic180 is a different path. C=0 has no defined perceptual hue.
3. Gamut: using the article's inverse code, OkLCh(.7,.4,40deg) gives linear RGB
   about(1.84476948,-.14806871,-.12968581), outside sRGB. Fixed L/C is not a
   guarantee of displayable/constant-looking hue sweeps. Conversion is not mapping.
4. Data: preserve seven displayed non-CAM16 RMS columns and values; 1.70/.20=8.5
   is that table's L error ratio, not proof of8.5× perceptual quality. HSL gets no
   borrowed HSV row. Verify the source's metric/data caveats and attribution.
5. Method: a palette answer should choose contextual L/C/h candidates, check
   target gamut/rendering and actual WCAG pairs, then adjust as required; no
   default palette, universal equal appearance, C/L saturation law or exact
   colour/music equivalence. Reuse Slice16 colour guide's accepted pair procedure;
   it is read-only, not a new browser/conformance result.

Review all79 primary header occurrences with exact path/field/index, endpoint
revisions, direction/meaning, support and outcome. Repair the one dangling route
as authorized. All other header targets are in the13-card cohort. Walk all body
relationships (102 statements at the pin) and body questions as well; external
models can use the inspected prepared/spec premises without inventing cards or
claiming unreviewed endpoints. The dependent terminology card's affected claims
must agree; do not claim all of its other edge/CQ results accepted.

All20 primary answers_questions occurrences retain their exact five texts.
Map actual answer components and give the supported answer/limits for: uniformity
(8 occurrences), palette lightness across hues(5), conversion(5), chroma versus
saturation(1), and the colour/music mathematical-relationship question(1).
Counts/lookup arrows are not semantic direction or warrant. Group records only
when every member's claim and supporting premise remain recoverable. No blanket
“all reconciled” assertion; no automatic global deferral of available local work.

## Required reading and intake

Before dependent edits, load complete required extents, recover truncated output,
and record a concise source-cited readback/actual coverage in the batch. Confirm
stage/whitepoint/perception/contrast distinctions and the precise header exceptions.

- Standing SOURCE AGENTS/current collaboration-framework routes; current design
  and concept-cards entrypoints. Framework/PM wayfinder and focused planning/ledger
  guidance apply; engineering-methods guide07 Required reading and CC intake;
  work-verification guide05 Evidence During Correction Review; testing guide03
  Proportionate Proof and Package And Release Gates. Do not load irrelevant methods.
- Project plan active Release target, Scope/DoD/full-corpus, Evidence and workload
  economy, Operator deferral and Workflow/acceptance, then Arc02 Accepted inputs,
  Complete coverage, Findings/accessibility ownership and Workflow/current assignment.
  Project/arc ledgers: current criterion rows and source-readiness/amendment notes;
  historical narratives are reference-only. Full current slice plan, ledger and prompt.
- All13 primary cards and the complete dependent terminology card. Prepared
  a-perceptual-colour-space.md in full (504 lines; hash in plan), including data
  caveats and2025 introduction versus2020 publication. HTML icons may be omitted
  from display only; preserve source/math/line identity and do not claim absent
  plots were visually reviewed. Prepared okhsv-and-okhsl.md sections85–198 and
  234–277 at pin: picker-goal tradeoffs and HSV/HSL/HSLuv/appearance terminology.
- Complete foundations Colour Theory and Music Theory→Visual Design sections,
  plus Stevens paragraph; design.md's two OKLCH/perception paragraphs and current
  colour.md in full. Scope of mutation remains narrower than these reads.
- Concept-cards guide05 Identify The Subject And Its Evidence through Keep Rich
  Prose Attached To Its Warrant; guide06 Select Relationship Identity through
  Rich-Body Relationship And CQ Boundaries. Apply them to explicit claim/edge/CQ
  subjects; confidence/link resolution is not semantic verification.
- Primary technical support: Ottosson https://bottosson.github.io/posts/oklab/
  implementation, derivation/data limits, comparisons and blend discussion;
  CSS Color4 CRD2026-10-09 https://www.w3.org/TR/2026/CRD-css-color-4-20261009/
  §§2,9.1–9.6,10.9–12,13.1–13.5 and14.1.6 as applicable to actual changed claims;
  CIE e-ILV saturation17-22-073 and chroma17-22-074 at
  https://cie.co.at/eilvterm/17-22-073 and https://cie.co.at/eilvterm/17-22-074 .
  Read complete selected rules/definitions and record edition/status. W3C is a
  work-in-progress draft; current URLs do not satisfy missing immutable capture.
- Data scope: strict parse of all233 accepted Arc01/Slice01 card-source-index.jsonl
  rows at9cc203380aede19231b7c5119f0b43d9fe3d0e78; compare exact current path roster.
  Select the enumerated thirteen paths plus dependent path first, inspect their
  raw source identity/Source Reference records and current typed headers. Do not
  join by slug alone or compare literal raw titles/authors to unescaped display
  strings. Emit/inspect79 edge and20 CQ occurrences and body coverage in the
  existing batch, not a new copied index.
- Prior proof, selected only when reused: Slice02 cdc-verification.md final
  acceptance and numerical reconciliation's exact relevant matrix/vector/polar
  section, plus Slice16 cdc-verification.md accepted guide method/applicability.
  Old checker listings/history are reference-only; a new field fix does not
  require replaying previous extraction/normalization or every old negative.

## Exact mutation, validation and return

SOURCE maximum17 named paths (card bodies plus eleven explicit primary-header
scalars above; dependent header frozen):

```text
knowledge/design/concept-cards/posts/chroma-perceptual.md
knowledge/design/concept-cards/posts/colour-interpolation-perceptual.md
knowledge/design/concept-cards/posts/colour-space-comparison.md
knowledge/design/concept-cards/posts/colour-space.md
knowledge/design/concept-cards/posts/d65-whitepoint.md
knowledge/design/concept-cards/posts/gamut-srgb.md
knowledge/design/concept-cards/posts/lightness-perceptual.md
knowledge/design/concept-cards/posts/lms-cone-responses.md
knowledge/design/concept-cards/posts/matrix-transformation-colour.md
knowledge/design/concept-cards/posts/oklab-conversion.md
knowledge/design/concept-cards/posts/oklab.md
knowledge/design/concept-cards/posts/perceptual-uniformity.md
knowledge/design/concept-cards/posts/xyz-colour-space.md
knowledge/design/concept-cards/posts/chroma-vs-saturation.md
knowledge/design/guides/foundations-of-design.md
knowledge/design/SKILL.md
knowledge/design/version-history.md
```

Only the two specified guide passages may change. Owning metadata.version
**1.0.13→1.0.14** and matching sibling history entry change together; preserve
older entries and no duplicate skill-version labels. No other SKILL fields,
guides,219 other cards,161 source files, helpers, Makefile/lists or schema edits.
If source drift or an unlisted consequential defect requires more scope, report
the exact dependency and continue independent allowed repairs; no silent expansion.

PLANNING return maximum three paths:

```text
project10-design-foundations/arc02-theory-and-evidence/slice17-oklab-model-and-application/artifacts/batch-record.md
project10-design-foundations/arc02-theory-and-evidence/slice17-oklab-model-and-application/ledger.md
project10-design-foundations/arc02-theory-and-evidence/slice17-oklab-model-and-application/closing-report.md
```

Batch: intake,13 five-outcome rows, precise changed/unsupported/blocked claim
support and explicit sound-span coverage, dependent repair limits, local edges/CQs,
guide joins, focused calculations, before/after deltas and remaining owners.
Use concise grouped tables; no copied corpus or general verifier product.
Ledger Evidence/Notes only; all four statuses remain open. Plans/prompts/previous
accepted records are protected. Closing report is the per-row CC attestation,
sole supporting-artifact inventory and honest bubble-up; CDC independently closes.

Fresh checks: exact path/section/scalar mutations,233 identities, typed/raw ordered
metadata with only the11 exceptions, all14 literal citations/headings,219 other
cards and161 sources, protected guides and source/history scope, LF/EOF/local
links, whitespace and commit trailers. Inspect all substantive source deltas.
From SOURCE run **sequentially** `make help`, `make check-skills`,
`make check-skill-versions`, `make check-package-paths`, then separate fresh
`make design`; compare all8 packaged Markdown members to committed source and
record ZIP hash. Report warning counts and failures/recovery; ZIP does not check
unbundled cards or hosted rendering. No browser/AT/installed/hosted claim here.

Commit scoped source and planning work separately using explicit named paths
and `git commit --only`, preserving unrelated staging. Every commit includes:

```text
Co-authored-by: Codex <noreply@openai.com>

Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

Return final source/planning hashes, exact changed paths, actual fresh versus
retained evidence, four row proposals and limits. No receipt-only commit chain,
push, publication, original-fidelity/full-corpus or parent/release acceptance.
