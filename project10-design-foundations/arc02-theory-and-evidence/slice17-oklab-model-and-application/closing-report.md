# Slice17 Iteration01 CC return — proposed evidence, not CDC acceptance

This is the CC execution return for Iteration01, issued from planning
`de960367b73ac614619f3e7600436458eaa8c459` after planning predecessor
`61b3c427433f324a0933f7bcdccc507e6a03accb`. The implementation repair is
SOURCE `main` commit `c884b8f9ebc6c2c80385b8f1f3db9ecd63cb67fb`, based on
pin `485585efe99c2d2cf3b956356989664bc6ffa262`. The complete evidence and
occurrence-level review are in the [Iteration01 batch return](artifacts/batch-record.md#iteration01-current-cc-return--source-c884b8f9-planning-issue-de960367).

## Criterion readback

| Criterion | CC proposal | Evidence and limit |
|---|---|---|
| S17-01 | **Open** | All 13 primary card bodies were re-read after repair. Ten card bodies changed; three remain byte-identical. F01/F02 repairs, all 13 five-dimension available-evidence outcomes, and focused arithmetic are recorded. This does not restore unavailable historical source fidelity or constitute CDC review. |
| S17-02 | **Open** | The batch maps all 79 typed header occurrences with direction, both endpoint Core premises, reasoning and bounded outcome; all 102 predecessor body relationship occurrences map to current statements or explicit removals, and all 86 current statements are assessed. All 20 exact header CQ occurrences have component-level bounded answers. Inferred navigation remains identified as CC inference; CDC review is pending. |
| S17-03 | **Done at previously accepted scope** | CDC accepted this preservation criterion at SOURCE `485585ef` / planning `61b3c427`. Iteration01 is body-only: all 13 header/citation/heading projections remain unchanged, and the other 220 cards and 161 prepared sources remain unchanged. No metadata, card identity or representation correction was made. |
| S17-04 | **Open** | The source commit is exact-scope and has required trailers. Previously accepted native/version/package evidence remains applicable: the ten changed cards are unbundled and no package inputs changed. Iteration01 did not rerun native/package gates, as its contract permits retaining them after the input comparison. CDC should review that retained scope and this complete return. |

## Source repair and focused evidence

The source write set is exactly these ten authorized card bodies:
`chroma-perceptual.md`, `colour-interpolation-perceptual.md`,
`colour-space-comparison.md`, `d65-whitepoint.md`, `lightness-perceptual.md`,
`lms-cone-responses.md`, `matrix-transformation-colour.md`,
`oklab-conversion.md`, `oklab.md`, and `xyz-colour-space.md`. The three other
cards in the thirteen-card allowance were unchanged. Metadata prefixes,
citations, headings, the dependent card, guides, skills/history, all other
cards, prepared sources, helpers and package inputs were preserved.

The correction reconciles whole-card teaching, including fitted Oklab axes and
approximate uniformity; CIE chroma/saturation versus HSL/HSV parameters; Oklab L
versus XYZ Y, CIELAB L*, HSV V and WCAG relative luminance; D65 reference and
adaptation; XYZ M1 versus combined linear-sRGB coefficients; signed real cube
roots; complete forward/reverse conversion steps; rounded-coefficient error;
and CAM16-generated lightness/chroma data versus the distinct perceived-hue
dataset. The neural-network comparison is explicitly identified as CC card
author synthesis absent from the prepared article.

The prepared article was identified by SHA256
`ffe5494da6f0d040fb341d8e1f03d3e396600f6787088b6d57e32613798375f4` (504
lines). Fresh float64 calculations using its rounded coefficient family gave
Oklab `(0.728143374355, -0.025083383346, -0.099756334367)` for linear sRGB
`(0.2, 0.4, 0.8)`; the printed inverse returned approximately
`(0.200000025100, 0.399999998411, 0.799999860390)`, maximum absolute error
`1.40e-7`. Other recorded witnesses distinguish encoded from linear sRGB,
nonlinear scaling, negative intermediates, polar chroma/hue wrap, an
out-of-sRGB inverse result, and the article table's 8.5 L-RMS ratio from a
perceptual-quality multiplier. These are arithmetic/source-readback checks,
not browser rendering, psychophysical experiments or plot inspection.

## Scope and handoff

Planning changes are limited to the existing batch artifact, this closing
report, and Evidence/Notes cells in the slice ledger. The scoped commit remains
unpushed on SOURCE `main`. The pre-existing untracked
`knowledge/lfe/` was preserved. `git diff --check` passed for both worktrees;
the Iteration01 row counts reconcile to 79 edges, 102 predecessor body
relationships, 86 current body relationships, and 20 header CQ occurrences.

S17-01, S17-02 and S17-04 remain open for independent CDC review; S17-03
remains done at its accepted structural scope. This CC return does not close
Slice17 or Arc02, accept Project10, claim full-corpus fidelity or hosted
rendering, or authorize a push, publication or release. No successor slice is
opened here.
