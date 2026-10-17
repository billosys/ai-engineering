# CC implementation — Slice18 Colour Picker Tradeoffs

Execute the source correction and return to CDC Sofie through the Operator.
Two contributors, Expedited Mode. No CRC, push, publication, closure or next slice.
SOURCE/main pin `4e635bb39b2c6151014b316f45f279d3682416d4`; planning predecessor
`a888e85710b18f031186b2bafde97d57bd8d0c02`. Record the actual issuing commit
(the commit adding this prompt) before implementation.

## Read and apply before editing

Read active [project plan](../../project-plan.md)1.73/project ledger, then
[arc plan](../arc-plan.md)1.54/arc ledger, [slice plan](slice-plan.md),
[ledger](ledger.md) and this complete prompt. Current AGENTS, framework/PM
wayfinder and relevant open/close routes, engineering-methods guide07 CC intake,
work-verification ledger/evidence-retention and native testing gates apply.
Use visual-design's contextual-perception/actual-pair guidance and Concept Cards
entrypoint/guides05–06 for source warrant, relationships and actual CQ components.
Retain unchanged guidance only with checked applicability; recover truncation
and record actual coverage/readback before dependent edits.

Read all eleven complete cards listed below, complete prepared picker article,
Drasner HSL97–124/native-control427–429, and the actual cited endpoint premises.
Read the external hsl-css-syntax card; use accepted Slice17 Oklab/lightness/
conversion/chroma and colour-guide methods read-only when they support a claim.
Inspect relevant primary sections linked below for current technical assertions.
Do not re-read unrelated project history or recreate accepted source inventories.

## Binding mutation and preservation

Only these eleven files under `knowledge/design/concept-cards/posts/` plus
`knowledge/design/SKILL.md` and `knowledge/design/version-history.md` may change:

- `colour-gamut.md`
- `hsv.md`
- `colour-picker.md`
- `chroma-vs-saturation.md`
- `colour-picker-design-principles.md`
- `okhsl.md`
- `munsell-colour-system.md`
- `hsl.md`
- `natural-colour-system.md`
- `orthogonal-colour-properties.md`
- `okhsv.md`

No guides/helpers/sources/package-list/schema or other222 cards. Preserve233
identities and all161 source files. Freeze literal Source Reference sections,
existing body headings and metadata representation except these exact changes:

1. In okhsl, okhsv and orthogonal-colour-properties, change existing
   `rosetta_stone[0].rating` from `rigorous` to `loose`. Replace only its existing
   note with the accurate limited analogy: numeric colour-model parameters and
   equal frequency ratios/Euclidean basis vectors do not establish equal visual
   or auditory differences or perceptual independence. Keep domain/concept fields.
   This authorizes exactly six scalar edits, not new fields or schema work.
2. In colour-picker, remove the sole `css_implementation[0]` association whose
   property is `input[type=color]` and example is HTML markup. Keep the existing
   field as an empty list `css_implementation: []`: a selector/HTML example is not
   a CSS-property mapping. Preserve its useful native-input illustration in the
   body, accurately labelled as HTML rather than literal recovered source code.

All other key/list order, nested alias arrays, types, null/empty distinctions,
source identities and extraction-confidence metadata remain frozen. Capture the
exact before/after exception values; no automatic metadata “cleanup.” Read the
owning metadata first; bump1.0.14→1.0.15 with append-only sibling history entry.
All card bodies require complete available-evidence review and supported repairs.

## Source basis and concrete repair recipe

Prepared `knowledge/design/sources/md/posts/okhsv-and-okhsl.md`:1136 lines,
SHA256 `227d62385a8ca4dfa77e9f5a10d55c9bd8d1c2f29d8964f59a1059bfb67d5d19`.
Full-card completeness is not inferred from the selected source spans below.
Current [Ottosson article](https://bottosson.github.io/posts/colorpicker/) is
technical support, not an immutable capture. Figures were not inspected by CDC;
attribute described visual examples, not fresh visual/empirical verification.

**Picker/principles/orthogonality (15–43,85–110,278–307,745–770):**
Keep all eight named goals, their conflict and both model profiles. These are the
author's proposed criteria and explicitly subjective tables, scoped to sRGB;
“yes” is not proof of exact perception or universal quality. Distinguish numeric
parameter independence, perpendicular vector bases, perception and smooth versus
even change. Both new models have Varies Evenly=no; Okhsv has Orthogonal
Lightness=no. HSL/HSV hue ratings are partial, not the same yes as Okhsv/Okhsl.
Fix all related examples/procedures/analogies, not just Core definitions.

The article prioritizes colour-space choice for its discussion; it does not
prove widget design/accessibility unimportant. Avoid universal drop-in/numeric
compatibility and current market-adoption claims. A usable choice procedure
names the task/gamut, desired control (e.g. lightness candidates versus locating
vivid hues), tradeoffs and output checks; it does not prescribe a new widget.
Native HTML input appearance/implementation is host-dependent. The prepared
Drasner native-input sentence has missing inline markup: a retained
`<input type="color" value="#ff0000">` is an illustrative HTML example, not a
verbatim recovered quote or evidence that the native widget uses Okhsl/HSV.
[HTML Color state](https://html.spec.whatwg.org/multipage/input.html#color-state-(type=color))
supports the control distinction; no current browser behavior test is claimed.

**HSL/HSV/chroma (106–198,234–297; accepted Slice17 terminology):**
Give the underlying RGB/encoding convention, normalized reference domain and
hue units. Classic picker formulas use encoded sRGB r,g,b∈[0,1], M=max, m=min,
Δ=M−m: HSV V=M and S=0 for M=0 else Δ/M; HSL L=(M+m)/2 and S=0 for Δ=0
else Δ/(1−|2L−1|). Hue is powerless at achromatic points. HSL S=0 gives grey
for every L, not only L=.5. HSV V is the maximum encoded component, not physical
brightness/lightness; mixtures at S<1 are not just fully saturated hue plus black.
Keep HSL/HSV saturation distinct from CIE appearance terms; correct repeated
absolute-chroma/maximum-lightness rules in Munsell/orthogonality too.

Align modern/legacy HSL syntax with accepted hsl-css-syntax and
[CSS Color4 §§7–7.2](https://www.w3.org/TR/2026/CRD-css-color-4-20261009/#the-hsl-notation):
modern numeric S/L use0–100, legacy requires percentages; hue wraps rather than
invalidating outside0–360. The normalized formulas above are a bounded numeric
example, not a restriction on all CSS syntax/extended values. Preserve useful
legacy examples and label Sass as source-era Sass, not standalone CSS.

**Gamut/Okhsv (89,240–276,301–425,461–511,840–940):**
Gamut is a representable set/volume, not just its boundary. sRGB is this article's
target, not a universal CSS/screen target or synonym for HDR. Distinguish gamut
conversion, mapping and component clipping; nearest-colour/component-clamp claims
are not a generic CSS rule ([CSS Color4 §14](https://www.w3.org/TR/2026/CRD-css-color-4-20261009/#gamut-mapping)).
Simple parameter boxes map to a bounded gamut with degenerate axes; they are not
a claim that the physical perceptual solid is cylindrical or uniformly spaced.
Correct the inverted colour-gamut Error/Correction pair into a real error.
The Okhsv figures use axes L_r and C·L_r/L, not plain C. Their triangular
construction is an approximation with a curved top and explicit compensation.
A constant-v band does not promise equal brightness. Retain cusp→(s=1,v=1),
relative model controls and source's qualified tradeoff. Retain Okhwb w=(1−s)v,
b=1−v, with inverse s=1−w/(1−b),v=1−b only when b≠1; black is degenerate.

**Toe/Okhsl/conversion (309–323,513–531,659–758,802–1117):**
Retain a usable recipe and explicit nonlinear stages. Do not call full Oklab
conversion a matrix transform. Source code uses normalized hue turns, not raw
atan2 radians: h=atan2(b,a)/(2π) modulo1; normalize a,b by C only when C>0.
Clearly handle C=0/black/white and zero divisors. For printed illustrative
coordinate recipes choose h=0 at powerless neutral hue as an explicit convention,
not a physical hue measurement. For exact neutral conversion, take s=0 and
l=toe(L) in Okhsl or v=toe(L) in Okhsv without normalizing by C or calling cusp
helpers. Canonical black is h=0,s=0,l/v=0; canonical white is h=0,s=0,l/v=1.
Degenerate coordinates are not uniquely invertible; these are explicit recipe
conventions, not a claim that the literal source handles every zero divisor.
Use a stated tolerance if classifying near-neutrals numerically. The code excerpts depend on omitted gamut helpers;
do not present them as a complete robust implementation or commission a library.

Use source constants k1=.206,k2=.03,k3=(1+k1)/(1+k2):
toe(L)=(k3L−k1+sqrt((k3L−k1)^2+4k2k3L))/2;
toe_inv(l)=l(l+k1)/(k3(l+k2)). Oklab's D65 chromaticity/relative normalization
is distinct from a fixed absolute reference luminance and this picker remapping;
do not repeat the source's “no reference white” phrase as a blanket denial of D65.
Keep appearance/context limits. No need to propagate the source's rounded half-
lightness Y comparison as an independently verified numerical claim.

For sRGB→Okhsl: decode→full Oklab→base L,C,h→get_Cs(**base Oklab L**,unit a/b)
→inverse piecewise C-to-s mapping→l=toe(L). Reverse l with toe_inv before
get_Cs and s-to-C. The existing card incorrectly supplies L_r to get_Cs.
Preserve the actual three-reference construction: C=0 and dC/ds=C0 at s=0,
C=Cmid at s=.8, C=Cmax at s=1. C0 is the initial slope, not C at s=0.
Use the source's rational piecewise mapping (1043–1060; inverse1097–1112), not
linear C=s·Cmax. Outline helper dependencies and domains, with one meaningful
worked mathematical example; avoid copying hundreds of implementation lines.

**Munsell/NCS (53–83,120–125,278–297):**
Preserve HVC ordering/notation, irregular solid and NCS resemblance/triangle
notation as useful context. Attribute historical overview and visual descriptions;
independence/uniformity are design goals, not all-context proofs or a chroma≈20
ceiling. Distinguish analogy/structural similarity from unsupported “first ever”
claims or direct HSL derivation. Munsell Chroma is not context-free absolute
colourfulness. NCS elementary colours are perceptual references, not RGB primaries;
its notation/system is not identical to a finite paint sample collection or one
RGB gamut. Do not assert every conversion requires a mapping table: specified
samples/measurement/conversion conditions are needed for defensible screen matches.
[Official NCS explanation](https://ncscolour.com/en-eu/pages/the-system) supports
notation/elementaries; retain 1050-Y90R as a notation example (10% blackness,
50% chromaticness,40% whiteness, hue toward red from yellow), not a screen RGB.
Munsell-owner full-page access failed for CDC; retain only supported bounded
HVC teaching/illustrative notation or inspect named primary support for added
claims, not new historical investigation. Keep limits and owners explicit.

## Semantic evidence, focused proof and return

One supporting artifact, `artifacts/batch-record.md`: eleven actual outcomes
for source agreement/fidelity limits, correctness, scope, consistency and edge/CQ
support. Cite claim-specific source/premise where needed; useful sound groups may
share a precise assessment. Record all66 header edges with actual meaning,
direction and support; prerequisites B→A support understanding A, extends A→B,
related/contrast symmetric. All65 predecessor body relationships need final
retained/rephrased/merged/removed-with-reason joins, plus final/new statements.
Read bodies for questions, not just question marks. Map all15 header occurrences
(three exact texts) to actual answer components and attempt bounded combined
answers. General/background cards can be partial. Counts and names are not warrant.

Worked edge: hsl→okhsl supports understanding a familiar picker convention;
prepared108/305–307 and the corrected two model definitions show familiar labels
but different coordinate constructions. This is an editorial learning route,
not interchangeable numeric values or strict mathematical necessity. Give such
connecting reasons with concise premises; no repeated full Core quotations,
new corpus IDs/schema or software validator. Reuse accepted233 index/source pins.

Fresh meaningful witnesses (use declared tolerances, e.g.1e-9 for these doubles):
- Encoded RGB(.8,.2,.2): HSV(h=0,S=.75,V=.8), HSL(h=0,S=.6,L=.5).
  Grey(.5,.5,.5) has both S=0 and powerless hue. This rejects same-saturation
  semantics and the “HSL grey only at L=.5” claim (also test another grey).
- toe(0)=0,toe(1)=1,toe(.5)≈.421140562609; toe_inv(.5)≈.568838198942.
  Round-trip at0,.125,.5,1. Do not confuse l with base L in get_Cs.
- Arithmetic-only synthetic fixture C0=.1,Cmid=.12,Cmax=.2 (not a measured
  hue/gamut): rational mapping gives C(0)=0,C(.4)=.048,C(.8)=.12,C(.9)=.1488,
  C(1)=.2; inverse recovers s. Linear C=sCmax fails at.8 (.16 versus.12).
- Check hue turns/degrees conversion, neutral/black/white denominators and Okhwb
  black boundary by direct algebra/source review; do not claim missing helpers
  were run or that printed reference code is robust at every boundary.

Read complete final cards again, including all repeated confusions/verification
notes. Scope current notes separately from inherited extraction confidence;
update chroma-vs-saturation's old bounded-review note to its actual new scope.
Compare233 paths, exact six scalar/one association exceptions, frozen metadata/
citations/headings, other222 cards/all161 sources/guides and changed-path scope.
Run local links, LF/EOF and whitespace checks. Begin with make help; sequentially
run make check-skills, make check-skill-versions, make check-package-paths, then
fresh make design; compare all8 Markdown ZIP members to committed source. Report
actual failures/recoveries and warnings, retaining unaffected prior evidence.

CC may create/update only `artifacts/batch-record.md`, first-class
`closing-report.md`, and ledger Evidence/Notes. Preserve criteria/statuses,
plans and prompt. The report names the issue/source/planning commits, all four
row proposals, sole artifact, scope-as-delivered and Bubble-up to the arc. Missing
capture fidelity, actual browser/AT/picker behavior, hosted233-view and full
corpus/global/release remain existing gates; do not defer available local review.
Commit exact changed SOURCE paths separately from these three planning outputs
(use git commit --only), with separate Codex <noreply@openai.com> and Billo AI
<ai-engineering@billo.systems> co-author trailers. No push or receipt-only chain;
return to Operator for CDC review, without independent acceptance or closure.
