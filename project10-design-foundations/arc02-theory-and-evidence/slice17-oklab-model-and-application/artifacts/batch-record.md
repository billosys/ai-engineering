# Slice17 CC batch record — 2026-10-17

## Assignment and source state

Executed the issued Slice17 prompt against SOURCE `main` pinned at
`4acfec6d8fa17e1ecb869bda28a6e71d17ef771e`; planning issue predecessor is
`bddbda7bbcce1955164c7bad4074c7cecdf90873`. Initial source tracked state matched
the pin. Pre-existing untracked `knowledge/lfe/` was preserved. The accepted
Slice01 index parsed as 233 JSONL records across five collections. Its sorted
path roster exactly matches `git ls-files knowledge/design/concept-cards` (233).
The 13-card projection contains 79 header edge occurrences: 27 prerequisites,
7 extends, 44 related and 1 contrast. The 20 header CQ occurrences are exactly
five texts with counts 8/5/5/1/1. These counts and endpoint resolution are
structural evidence only.

Required intake loaded in the executing context: current source `AGENTS.md` and
skill-version contract; project/arc/slice active plans and ledgers; complete
assignment; design/concept-card skill entrypoints; Concept Cards guide05/06;
Engineering Methods guide07 CC intake; Work Verification guide05; Testing
validation-gate guidance; all 13 primary cards and the complete dependent
`chroma-vs-saturation.md`; prepared Ottosson article (504 lines, display-only
icon omission); prepared Okhsv/Okhsl sections 85–198 and 234–277; assigned
foundations passages, design guide OKLCH passages and colour guide. Primary
technical reading: [Ottosson, “A Perceptual Color Space for Image Processing”](https://bottosson.github.io/posts/oklab/); [CSS Color 4 CRD dated 2026-10-09](https://www.w3.org/TR/2026/CRD-css-color-4-20261009/) §§2, 9.1–9.6, 10.9–12, 13.1–13.5, 14.1.6; CIE S 017:2020 [saturation 17-22-073](https://cie.co.at/eilvterm/17-22-073) and [chroma 17-22-074](https://cie.co.at/eilvterm/17-22-074).
CSS Color 4 is a work-in-progress Candidate Recommendation Draft. Current web
access is not an immutable historical capture. Source plots were not visually
inspected; no original capture, browser, accessibility-tool or hosted behaviour
claim is made.

## Five-dimension card outcomes (CC status)

The following are bounded correction outcomes, not five completed independent
acceptance determinations. All cards retain predecessor confidence and source
identity; technical notes distinguish current support from historical extraction.

| Primary card | Supported correction made | Retained / useful teaching | Unsupported assertion removed or narrowed | Technical inference boundary | Still open for CRC |
|---|---|---|---|---|---|
| `chroma-perceptual.md` | Oklab C=`hypot(a,b)`; CIE chroma/saturation distinction | Coordinate construction and attributed Munsell/hue-sweep descriptions | C/L law, universal C range, guaranteed equal appearance | Perceptual interpretation remains model/context dependent | Reconcile all repeated procedure/relationship claims and CQ component support |
| `colour-interpolation-perceptual.md` | Cartesian vs polar path, arithmetic midpoint, hue wrap, powerless hue, host syntax | Selected attributed blend examples and explicit CSS example | Universal evenness, sRGB as error, current adoption/default claims | CSS behavior is specification-based; support metadata remains predecessor data | Audit all body relationship/error examples and reproduce all witnesses |
| `colour-space-comparison.md` | Dataset/metric scope, per-pair minimum-before-RMS method, CAM16 caveat | Seven non-CAM16 RMS columns and values | 8.5× quality interpretation; HSL borrowing | Table is article evidence, not independent experiment | Reconcile all remaining example and relationship statements |
| `colour-space.md` | Model/reference/domain, zero-chroma hue and nonmandatory XYZ route | General coordinate framing | Unique/full-visible-domain and universal XYZ route | Scoped to model and device | Check all residual body claims and endpoint warrants |
| `d65-whitepoint.md` | Reference vs display white, D50/D65 CSS distinction, adaptation | Rounded D65 example | All-CSS-D65 and direct-compatibility claims | CSS Color 4 draft support | Reconcile all repeated construction/example prose |
| `gamut-srgb.md` | 2D projection vs 3D gamut, conversion vs mapping, local/global convexity, HDR vs gamut | Attributed article design-history examples | Pointer dataset as universal physical boundary | Dataset is empirical and bounded | Verify all examples and full relationship/CQ coverage |
| `lightness-perceptual.md` | Oklab L vs XYZ Y/CIELAB L*/HSV V/WCAG luminance; rendered-pair method | Candidate tonal construction | cbrt(Y), exact equal steps, L as contrast test | Pair procedure retained from Slice16; no browser result | Answer all five palette CQs with occurrence-level component support |
| `lms-cone-responses.md` | XYZ M1 vs combined linear-sRGB coefficients; fitted intermediate and signed root | Article matrix/code values | Physiological accuracy and universal nonnegativity | Prepared article formulas | Reconcile all examples and relationship meanings |
| `matrix-transformation-colour.md` | Linear vs affine, nonlinear route, coefficient domains, finite precision | Literal matrix operation | Universal single-matrix route and exact round trip | Mathematical claim limited to stated stages | Verify remaining source examples and occurrence-level edges |
| `oklab-conversion.md` | Decode first; matched coefficient families; XYZ M1 vs combined RGB; real cube root; 2021 note scope | Formula and reverse-stage explanation | Complete-route linearity, incorrectly assigned matrix input/date, neural equivalence | Article coefficient family retained | Finish exact inverse/polar/gamut witness review and all five CQ mappings |
| `oklab.md` | Approximate fitted model; D65/reference; gamut/render boundaries | Coordinate definitions and attributed article examples | Uniformity guarantee, untested current support, categorical superiority | CSS syntax checked against WIP draft | Verify all repeated claims and answer its eight uniformity/five palette CQs by occurrence |
| `perceptual-uniformity.md` | Ideal vs approximate fit; actual constant-L/C hue sweep; loose music analogy | Literal coordinate operation distinguished from analogy | Equal-appearance law and impossible across-hues recognition test | Dataset/context dependent | Verify all eight uniformity answers and every body relationship occurrence |
| `xyz-colour-space.md` | Tristimulus scope, nonmandatory route, nonlinear complete conversion, arithmetic fixtures | Linear XYZ matrix stages | Universal linearity, XYZ chrominance channels and universal routing | Observer/reference must be stated | Check all body examples and exact conversion CQ support |

## Dependent terminology and live-guide scope

`chroma-vs-saturation.md` body changes are limited to the assigned chroma / CIE
appearance saturation / HSL / HSV relative-chroma family, including the unsupported
pale-pastel and universal maximum-chroma tests. Its full header and Source
Reference remain frozen. Attributed HSL/HSLuv picker-goal tradeoffs are retained.
This is not acceptance of the remaining Okhsl/Okhsv card family.

In `guides/foundations-of-design.md`, only the OKLCH/OKLAB Colour Theory
paragraph and the brightness-exponent sentence in the Stevens paragraph changed.
Adjacent visual-area/spacing claims remain outside this slice; Arc02 owns their
warrant review. Existing temperament/matrix paragraphs, `colour.md`, `design.md`,
portable identity and token material were not changed.

## Focused numerical witnesses

Fresh double-precision calculations used the article's literal linear-sRGB rows:

- linear RGB (.125,.125,.125) produced L=0.499999997, a≈0, b≈0.
- encoded sRGB 0.5 decodes to 0.21404114048; applying the neutral Oklab cube-root route gives L≈0.598180731. Misreading 0.5 as linear gives L≈0.793700526.
- F(0.5·white).L≈0.793700521 while 0.5F(white).L≈0.5: the complete route is not linear.
- Article XYZ M1 at XYZ(0,0,1) gives l=-0.1288597137, exercising a negative intermediate and real signed cube root.
- (a,b)=(0.1,0.1) gives C=0.1414213562, h=45°. Shorter-path 350°→10° halfway is 0° modulo 360; naive arithmetic gives 180°.
- Article inverse for OkLCh(.7,.4,40°) gives linear RGB approximately (1.844769479,-0.148068712,-0.129685808), outside sRGB.
- Table ratio 1.70/0.20=8.5 is only the source L-RMS ratio. No quality multiplier is inferred.

These calculations support the listed discriminations. They do not prove browser
rendering, gamut mapping, original capture fidelity, or universal appearance.

## Preservation, integration and commits

Three source commits, each with required co-author trailers:

- `c8b16c7e` — exact 17-path Slice17 source write set, including 14 cards,
  foundations guide, design entrypoint and history.
- `26320610` — additional substantive consistency repairs to seven of those
  named card paths; no path outside the issued set.
- `485585ef` — further body-relationship corrections to five named cards; no
  path outside the issued set.

The exact 233-card roster was reproduced; the 14 touched card headers parse as
ordered YAML and differ only at the 11 enumerated primary scalar values. All 14
literal Source Reference sections and heading sequences match the source pin.
The dependent header/citation remain frozen. No helpers, schema, Makefile,
packaging list, other cards or source files were changed. `git diff --check`
passed. Source `main` is ahead seven; no push.

Sequential source gates: `make help` passed; `make check-skills` passed (24
skills; 18 descriptions exceed the 300-character editorial target, none violate
the gate); `make check-skill-versions` exited 0; `make check-package-paths`
passed (24 skills/packages, 388 Markdown files scanned, 0 hard failures, 596
warnings, 3 explicit exceptions); a separate fresh `make design` completed after
rerunning with source-checkout write authorization. The generated ZIP has eight
Markdown members, each byte-identical to its committed source member. ZIP SHA256:
`0e5c2cfe4d14446e30035e833d62c3d6f39ee172e00a9e30868c3291f9b49c7d`.
The first `make design` attempt lacked source write authorization and logged a
staging `Operation not permitted` before archiving an old ZIP; the authorized
retry rebuilt the package and passed the 8/8 byte comparison. The ZIP covers only
its packaged files, not concept cards or hosted rendering.

## Outstanding semantic work / limits

The required complete occurrence-level review is not finished in this return:
79 header edges now have exact source field/index, direction and resolved endpoint
path/revision, but premise support and outcome have not been recorded for each.
The exact 102 body statements were counted by source card but have not been
cross-walked occurrence-by-occurrence to endpoint premises and outcomes. The CQ
groups account for all 20 header question texts and map answer components present
in the cards, but body-question occurrences and each occurrence-to-warrant join
remain incomplete. Several old examples and secondary statements may still need
occurrence-by-occurrence review. This is why
S17-01 and S17-02 remain open. The exact path/typed-header preservation and native
package evidence support S17-03/S17-04 only as proposed checks, not CDC closure.
No parent, full-corpus, original-fidelity, hosted-rendering or release gate is
accepted here.

## Exact primary header-edge occurrence inventory

The 79 entries below preserve each source card, field/index, endpoint path and typed direction. All endpoint paths are resolved in the current source candidate `485585ef`. “Target resolves” proves identity only; the table does not provide premise support/outcome for every relation. The corrected `perceptual-uniformity.related[2]` now targets the comparison card.

| Source card | Field[index] | Relationship meaning | Endpoint card | Occurrence outcome |
|---|---|---|---|---|
| `knowledge/design/concept-cards/posts/chroma-perceptual.md` | `prerequisites[0]` | requires `chroma-perceptual` ↔ `oklab` | `knowledge/design/concept-cards/posts/oklab.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/chroma-perceptual.md` | `prerequisites[1]` | requires `chroma-perceptual` ↔ `perceptual-uniformity` | `knowledge/design/concept-cards/posts/perceptual-uniformity.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/chroma-perceptual.md` | `related[0]` | related `chroma-perceptual` ↔ `lightness-perceptual` | `knowledge/design/concept-cards/posts/lightness-perceptual.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/chroma-perceptual.md` | `related[1]` | related `chroma-perceptual` ↔ `colour-space-comparison` | `knowledge/design/concept-cards/posts/colour-space-comparison.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/chroma-perceptual.md` | `related[2]` | related `chroma-perceptual` ↔ `colour-interpolation-perceptual` | `knowledge/design/concept-cards/posts/colour-interpolation-perceptual.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/colour-interpolation-perceptual.md` | `prerequisites[0]` | requires `colour-interpolation-perceptual` ↔ `oklab` | `knowledge/design/concept-cards/posts/oklab.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/colour-interpolation-perceptual.md` | `prerequisites[1]` | requires `colour-interpolation-perceptual` ↔ `perceptual-uniformity` | `knowledge/design/concept-cards/posts/perceptual-uniformity.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/colour-interpolation-perceptual.md` | `prerequisites[2]` | requires `colour-interpolation-perceptual` ↔ `oklab-conversion` | `knowledge/design/concept-cards/posts/oklab-conversion.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/colour-interpolation-perceptual.md` | `extends[0]` | extends `colour-interpolation-perceptual` ↔ `perceptual-uniformity` | `knowledge/design/concept-cards/posts/perceptual-uniformity.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/colour-interpolation-perceptual.md` | `related[0]` | related `colour-interpolation-perceptual` ↔ `chroma-perceptual` | `knowledge/design/concept-cards/posts/chroma-perceptual.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/colour-interpolation-perceptual.md` | `related[1]` | related `colour-interpolation-perceptual` ↔ `lightness-perceptual` | `knowledge/design/concept-cards/posts/lightness-perceptual.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/colour-interpolation-perceptual.md` | `related[2]` | related `colour-interpolation-perceptual` ↔ `colour-space-comparison` | `knowledge/design/concept-cards/posts/colour-space-comparison.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/colour-space-comparison.md` | `prerequisites[0]` | requires `colour-space-comparison` ↔ `perceptual-uniformity` | `knowledge/design/concept-cards/posts/perceptual-uniformity.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/colour-space-comparison.md` | `prerequisites[1]` | requires `colour-space-comparison` ↔ `oklab` | `knowledge/design/concept-cards/posts/oklab.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/colour-space-comparison.md` | `prerequisites[2]` | requires `colour-space-comparison` ↔ `colour-space` | `knowledge/design/concept-cards/posts/colour-space.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/colour-space-comparison.md` | `prerequisites[3]` | requires `colour-space-comparison` ↔ `chroma-perceptual` | `knowledge/design/concept-cards/posts/chroma-perceptual.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/colour-space-comparison.md` | `prerequisites[4]` | requires `colour-space-comparison` ↔ `lightness-perceptual` | `knowledge/design/concept-cards/posts/lightness-perceptual.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/colour-space-comparison.md` | `extends[0]` | extends `colour-space-comparison` ↔ `perceptual-uniformity` | `knowledge/design/concept-cards/posts/perceptual-uniformity.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/colour-space-comparison.md` | `related[0]` | related `colour-space-comparison` ↔ `colour-interpolation-perceptual` | `knowledge/design/concept-cards/posts/colour-interpolation-perceptual.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/colour-space-comparison.md` | `related[1]` | related `colour-space-comparison` ↔ `gamut-srgb` | `knowledge/design/concept-cards/posts/gamut-srgb.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/colour-space.md` | `related[0]` | related `colour-space` ↔ `oklab` | `knowledge/design/concept-cards/posts/oklab.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/colour-space.md` | `related[1]` | related `colour-space` ↔ `xyz-colour-space` | `knowledge/design/concept-cards/posts/xyz-colour-space.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/colour-space.md` | `related[2]` | related `colour-space` ↔ `lms-cone-responses` | `knowledge/design/concept-cards/posts/lms-cone-responses.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/colour-space.md` | `related[3]` | related `colour-space` ↔ `d65-whitepoint` | `knowledge/design/concept-cards/posts/d65-whitepoint.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/colour-space.md` | `related[4]` | related `colour-space` ↔ `gamut-srgb` | `knowledge/design/concept-cards/posts/gamut-srgb.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/d65-whitepoint.md` | `prerequisites[0]` | requires `d65-whitepoint` ↔ `colour-space` | `knowledge/design/concept-cards/posts/colour-space.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/d65-whitepoint.md` | `related[0]` | related `d65-whitepoint` ↔ `oklab` | `knowledge/design/concept-cards/posts/oklab.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/d65-whitepoint.md` | `related[1]` | related `d65-whitepoint` ↔ `xyz-colour-space` | `knowledge/design/concept-cards/posts/xyz-colour-space.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/d65-whitepoint.md` | `related[2]` | related `d65-whitepoint` ↔ `gamut-srgb` | `knowledge/design/concept-cards/posts/gamut-srgb.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/gamut-srgb.md` | `prerequisites[0]` | requires `gamut-srgb` ↔ `colour-space` | `knowledge/design/concept-cards/posts/colour-space.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/gamut-srgb.md` | `prerequisites[1]` | requires `gamut-srgb` ↔ `d65-whitepoint` | `knowledge/design/concept-cards/posts/d65-whitepoint.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/gamut-srgb.md` | `extends[0]` | extends `gamut-srgb` ↔ `colour-space` | `knowledge/design/concept-cards/posts/colour-space.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/gamut-srgb.md` | `related[0]` | related `gamut-srgb` ↔ `oklab` | `knowledge/design/concept-cards/posts/oklab.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/gamut-srgb.md` | `related[1]` | related `gamut-srgb` ↔ `xyz-colour-space` | `knowledge/design/concept-cards/posts/xyz-colour-space.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/gamut-srgb.md` | `related[2]` | related `gamut-srgb` ↔ `colour-space-comparison` | `knowledge/design/concept-cards/posts/colour-space-comparison.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/lightness-perceptual.md` | `prerequisites[0]` | requires `lightness-perceptual` ↔ `oklab` | `knowledge/design/concept-cards/posts/oklab.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/lightness-perceptual.md` | `prerequisites[1]` | requires `lightness-perceptual` ↔ `perceptual-uniformity` | `knowledge/design/concept-cards/posts/perceptual-uniformity.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/lightness-perceptual.md` | `related[0]` | related `lightness-perceptual` ↔ `chroma-perceptual` | `knowledge/design/concept-cards/posts/chroma-perceptual.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/lightness-perceptual.md` | `related[1]` | related `lightness-perceptual` ↔ `colour-space-comparison` | `knowledge/design/concept-cards/posts/colour-space-comparison.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/lightness-perceptual.md` | `related[2]` | related `lightness-perceptual` ↔ `colour-interpolation-perceptual` | `knowledge/design/concept-cards/posts/colour-interpolation-perceptual.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/lms-cone-responses.md` | `prerequisites[0]` | requires `lms-cone-responses` ↔ `colour-space` | `knowledge/design/concept-cards/posts/colour-space.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/lms-cone-responses.md` | `related[0]` | related `lms-cone-responses` ↔ `xyz-colour-space` | `knowledge/design/concept-cards/posts/xyz-colour-space.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/lms-cone-responses.md` | `related[1]` | related `lms-cone-responses` ↔ `oklab` | `knowledge/design/concept-cards/posts/oklab.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/lms-cone-responses.md` | `related[2]` | related `lms-cone-responses` ↔ `matrix-transformation-colour` | `knowledge/design/concept-cards/posts/matrix-transformation-colour.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/matrix-transformation-colour.md` | `prerequisites[0]` | requires `matrix-transformation-colour` ↔ `colour-space` | `knowledge/design/concept-cards/posts/colour-space.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/matrix-transformation-colour.md` | `prerequisites[1]` | requires `matrix-transformation-colour` ↔ `xyz-colour-space` | `knowledge/design/concept-cards/posts/xyz-colour-space.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/matrix-transformation-colour.md` | `extends[0]` | extends `matrix-transformation-colour` ↔ `oklab-conversion` | `knowledge/design/concept-cards/posts/oklab-conversion.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/matrix-transformation-colour.md` | `related[0]` | related `matrix-transformation-colour` ↔ `lms-cone-responses` | `knowledge/design/concept-cards/posts/lms-cone-responses.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/matrix-transformation-colour.md` | `related[1]` | related `matrix-transformation-colour` ↔ `oklab` | `knowledge/design/concept-cards/posts/oklab.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/matrix-transformation-colour.md` | `related[2]` | related `matrix-transformation-colour` ↔ `oklab-conversion` | `knowledge/design/concept-cards/posts/oklab-conversion.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/oklab-conversion.md` | `prerequisites[0]` | requires `oklab-conversion` ↔ `oklab` | `knowledge/design/concept-cards/posts/oklab.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/oklab-conversion.md` | `prerequisites[1]` | requires `oklab-conversion` ↔ `xyz-colour-space` | `knowledge/design/concept-cards/posts/xyz-colour-space.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/oklab-conversion.md` | `prerequisites[2]` | requires `oklab-conversion` ↔ `lms-cone-responses` | `knowledge/design/concept-cards/posts/lms-cone-responses.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/oklab-conversion.md` | `prerequisites[3]` | requires `oklab-conversion` ↔ `matrix-transformation-colour` | `knowledge/design/concept-cards/posts/matrix-transformation-colour.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/oklab-conversion.md` | `extends[0]` | extends `oklab-conversion` ↔ `oklab` | `knowledge/design/concept-cards/posts/oklab.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/oklab-conversion.md` | `related[0]` | related `oklab-conversion` ↔ `d65-whitepoint` | `knowledge/design/concept-cards/posts/d65-whitepoint.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/oklab-conversion.md` | `related[1]` | related `oklab-conversion` ↔ `gamut-srgb` | `knowledge/design/concept-cards/posts/gamut-srgb.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/oklab.md` | `prerequisites[0]` | requires `oklab` ↔ `perceptual-uniformity` | `knowledge/design/concept-cards/posts/perceptual-uniformity.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/oklab.md` | `prerequisites[1]` | requires `oklab` ↔ `colour-space` | `knowledge/design/concept-cards/posts/colour-space.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/oklab.md` | `prerequisites[2]` | requires `oklab` ↔ `xyz-colour-space` | `knowledge/design/concept-cards/posts/xyz-colour-space.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/oklab.md` | `extends[0]` | extends `oklab` ↔ `perceptual-uniformity` | `knowledge/design/concept-cards/posts/perceptual-uniformity.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/oklab.md` | `related[0]` | related `oklab` ↔ `lms-cone-responses` | `knowledge/design/concept-cards/posts/lms-cone-responses.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/oklab.md` | `related[1]` | related `oklab` ↔ `d65-whitepoint` | `knowledge/design/concept-cards/posts/d65-whitepoint.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/oklab.md` | `related[2]` | related `oklab` ↔ `chroma-perceptual` | `knowledge/design/concept-cards/posts/chroma-perceptual.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/oklab.md` | `related[3]` | related `oklab` ↔ `lightness-perceptual` | `knowledge/design/concept-cards/posts/lightness-perceptual.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/oklab.md` | `related[4]` | related `oklab` ↔ `colour-interpolation-perceptual` | `knowledge/design/concept-cards/posts/colour-interpolation-perceptual.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/oklab.md` | `related[5]` | related `oklab` ↔ `oklab-conversion` | `knowledge/design/concept-cards/posts/oklab-conversion.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/oklab.md` | `related[6]` | related `oklab` ↔ `colour-space-comparison` | `knowledge/design/concept-cards/posts/colour-space-comparison.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/oklab.md` | `contrasts_with[0]` | contrasts with `oklab` ↔ `colour-space-comparison` | `knowledge/design/concept-cards/posts/colour-space-comparison.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/perceptual-uniformity.md` | `related[0]` | related `perceptual-uniformity` ↔ `colour-space` | `knowledge/design/concept-cards/posts/colour-space.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/perceptual-uniformity.md` | `related[1]` | related `perceptual-uniformity` ↔ `oklab` | `knowledge/design/concept-cards/posts/oklab.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/perceptual-uniformity.md` | `related[2]` | related `perceptual-uniformity` ↔ `colour-space-comparison` | `knowledge/design/concept-cards/posts/colour-space-comparison.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/xyz-colour-space.md` | `prerequisites[0]` | requires `xyz-colour-space` ↔ `colour-space` | `knowledge/design/concept-cards/posts/colour-space.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/xyz-colour-space.md` | `prerequisites[1]` | requires `xyz-colour-space` ↔ `d65-whitepoint` | `knowledge/design/concept-cards/posts/d65-whitepoint.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/xyz-colour-space.md` | `extends[0]` | extends `xyz-colour-space` ↔ `colour-space` | `knowledge/design/concept-cards/posts/colour-space.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/xyz-colour-space.md` | `related[0]` | related `xyz-colour-space` ↔ `lms-cone-responses` | `knowledge/design/concept-cards/posts/lms-cone-responses.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/xyz-colour-space.md` | `related[1]` | related `xyz-colour-space` ↔ `oklab` | `knowledge/design/concept-cards/posts/oklab.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/xyz-colour-space.md` | `related[2]` | related `xyz-colour-space` ↔ `oklab-conversion` | `knowledge/design/concept-cards/posts/oklab-conversion.md` | Target resolves; warrant not independently accepted |
| `knowledge/design/concept-cards/posts/xyz-colour-space.md` | `related[3]` | related `xyz-colour-space` ↔ `matrix-transformation-colour` | `knowledge/design/concept-cards/posts/matrix-transformation-colour.md` | Target resolves; warrant not independently accepted |

## Frozen-prompt body-relationship denominator

The issued pin contains 102 relationship statements in the thirteen `# Relationships` sections. The source card occurrence counts are: `chroma-perceptual.md` 7; `colour-interpolation-perceptual.md` 9; `colour-space-comparison.md` 8; `colour-space.md` 6; `d65-whitepoint.md` 4; `gamut-srgb.md` 8; `lightness-perceptual.md` 10; `lms-cone-responses.md` 6; `matrix-transformation-colour.md` 8; `oklab-conversion.md` 7; `oklab.md` 14; `perceptual-uniformity.md` 7; `xyz-colour-space.md` 8. The prose relationship sections were revised in the named cards, but the 102 occurrence-by-occurrence endpoint-premise/outcome map is still incomplete; see outstanding-work boundary above.

## Exact primary CQ occurrence map

| Exact question | Primary occurrences | Answer component present in current card body | Support and limit |
|---|---|---|---|
| “What makes a colour space perceptually uniform, and why does it matter for design?” | `colour-interpolation-perceptual`, `colour-space-comparison`, `colour-space`, `d65-whitepoint`, `gamut-srgb`, `lightness-perceptual`, `oklab`, `perceptual-uniformity` (8) | Coordinate differences aim to correspond consistently to perceived differences under stated conditions; Oklab is fitted/approximate. This can inform candidate construction/interpolation; check gamut and rendering. | Ottosson model goals and CSS Color 4 §9.2; no all-context guarantee, and each card's remaining claim premises still need CDC review. |
| “How do you construct a palette that changes lightness uniformly across hues?” | `chroma-perceptual`, `colour-interpolation-perceptual`, `colour-space-comparison`, `lightness-perceptual`, `oklab` (5) | Choose contextual L/C/h candidates; vary hue as intended; check target gamut/rendering and actual rendered sRGB foreground/background pairs for contrast; adjust. | Current colour/design guide method and approximate Oklab model; L is not WCAG luminance and does not certify equal appearance. |
| “How do you convert between colour spaces for image processing?” | `lms-cone-responses`, `matrix-transformation-colour`, `oklab-conversion`, `oklab`, `xyz-colour-space` (5) | State input encoding/reference; decode encoded sRGB; use matching coefficients; compose compatible linear stages around a signed real cube-root stage; reverse for inverse; encode only when needed. XYZ is useful but not mandatory. | Ottosson's two formula forms; CSS Color 4 conversion distinctions. Coefficient family and finite-precision limits must stay explicit. |
| “What distinguishes chroma from saturation in perceptual colour models?” | `chroma-perceptual` (1) | Oklab C is `hypot(a,b)`; CIE chroma references a similarly illuminated achromatic field, while CIE saturation references the stimulus's own brightness. HSL/HSV parameters are model-specific; no universal C/L law. | CIE S 017:2020 17-22-073/074 and Ottosson picker discussion. No broader Okhsl/Okhsv family acceptance. |
| “What is the mathematical relationship between perceptual uniformity in colour and equal temperament in music?” | `perceptual-uniformity` (1) | There is no identity: a fitted colour transform and 12-TET frequency ratios are different mathematics. The literal coordinate operation can be rigorous while the perceptual correspondence remains approximate. | Corrected loose analogy and rosetta note; no music-history or psychophysics inquiry. |

These groups account for all 20 frozen header occurrences and their exact texts.
They do not establish complete body-question coverage: body question statements
and each occurrence's exact component/warrant joins remain for CRC to inspect.
