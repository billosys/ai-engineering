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
technical reading: Ottosson, CSS Color 4 CRD dated 2026-10-09 §§2, 9.1–9.6,
10.9–12, 13.1–13.5, 14.1.6; CIE S 017:2020 terms 17-22-073 and 17-22-074.
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
passed. Source `main` is ahead six; no push.

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
79 header edges were counted, but their exact per-occurrence direction, endpoint
revision, premise, support and outcome have not all been recorded; the 102 body
relationship statements and body-question occurrences have not received a
complete occurrence-level reconciliation. The grouped CQ readback above is not
substitute evidence for exact answer-component mapping. Several old examples and
secondary statements may still need occurrence-by-occurrence review. This is why
S17-01 and S17-02 remain open. The exact path/typed-header preservation and native
package evidence support S17-03/S17-04 only as proposed checks, not CDC closure.
No parent, full-corpus, original-fidelity, hosted-rendering or release gate is
accepted here.
