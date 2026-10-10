# Bounded fluid-scale configuration reconciliation

## Inputs and method

Baseline SOURCE is `dffa504e851b03b8e4746f1941068e4cc850b612`; the accepted
Arc01 diagnostic example is `38b66d0d`, SHA-256
`996d047814bf174e0def2dea7f24f619c042dbd3bfa664bdaa3f4c4af4c2ea86`.
The source-file hashes and all nine witness ranges are receipted in
[execution notes](execution-notes.md#source-and-planning-intake-receipts).
The adopted example's actual table and step-0 declaration were parsed from the
pinned bytes; no regenerated table was used as the comparison input. All numeric
operations used Python `fractions.Fraction`, with integer half-even rounding to
six decimal places. The CSS arithmetic interpretation is `1vi = w/100`; clamp
bounds are ordered endpoint values. This does not execute a browser.

## Iteration01 source-to-result inventory

The table maps the complete nine-span population to every emitted subject.
Ranges are inclusive SOURCE line spans; the claim records carry the full exact
assertions and source hashes. Overlap is intentional where one passage contains
separate numeric and broader claims.

| Required witness | Covered result IDs and exact source spans | Inventory boundary |
|---|---|---|
| `knowledge/design/SKILL.md:144–210` | `SK-01:156`; `SK-02:158–167`; `SK-09:173–177`; `SK-03:185–187`; `SK-06:191`; `SK-04:195`; `SK-05:196`; `SK-07:199–203`; `SK-08:206–208` | Numeric step and per-site axis settings are recorded. Typeface/axis meaning, project branding, broader type/space/grid architecture and zero-breakpoint policy are not evaluated. |
| `knowledge/design/guides/type.md:133–142` | `TY-07:133`; `TY-01:135–140`; `TY-02:137–138` | The numeric heading and scale values are recorded. Musical/historical attribution and typographic or auditory harmony are not verified. |
| `knowledge/design/guides/type.md:456–488` | `TY-03:458–461`; `TY-04:463–470`; `TY-05:472–478`; `TY-06:480–485` | Printed ratios, percentages and fluid claims are separated from the perceptual, safety and source claims, which remain unassessed. |
| `knowledge/design/guides/layout.md:164–228` | `LAY-01:167–184`; `LAY-02:186–191`; `LAY-03:192–196`; `LAY-04:198–209`; `LAY-05:211–218` | The `say` pair at 179–181 is an illustrative alternative. Universal geometricity is assessed separately; spacing/grid behavior and attribution remain unassessed. |
| `knowledge/design/guides/layout.md:350–380` | `LAY-15:353–360`; `LAY-06:357–367`; `LAY-07:369–375`; `LAY-08:377–379` | The numbered heading and equal-absolute-difference examples are inventoried. Perceived magnitude and the normative “never by addition” advice are not tested. |
| `knowledge/design/guides/layout.md:493–528` | `LAY-09:496–505`; `LAY-10:509–517`; `LAY-11:518–527` | Declared defaults and literal type/space CSS are compared under the stated model; design suitability and space-token policy are not selected. |
| `knowledge/design/guides/layout.md:933–948` | `LAY-12:935–940`; `LAY-13:941–942`; `LAY-14:942–945` | Linear/clamp and scale claims are checked within the stated arithmetic model. Writing-mode, browser zoom, reflow and WCAG claims are not tested. |
| `knowledge/design/guides/design.md:363–369` | `DES-01:363–369` | The universal mathematical-correctness component is checked; overall design correctness is not established. |
| `knowledge/design/guides/foundations-of-design.md:255–286` | `FND-01:258–262`; `FND-02:264–270`; `FND-03:272–277`; `FND-04:279–284` | Bibliographic metadata, the primitive count, attribution and analogy are inventoried, not verified as facts. |

The three omissions from the initial return are now explicit subjects:
`TY-07` is the separate numeric heading at type.md:133; `SK-09` is the
per-site numeric axis table at SKILL.md:173–177; and `LAY-15` covers the
Roman-numeral principle marker and numeric examples at layout.md:353–360. The
two printed differences in LAY-15 are each `+4px`; the claim about their
perceived size and the rule in its heading are not arithmetic conclusions.
The `(v4.0, 2012, 398 pages)` metadata and “13 layout primitives” are carried
by FND-01/FND-03 as numeric mentions only. No bibliography, font or axis
semantics, historical attribution, empirical perception, media-query advice,
grid behavior, or general design-policy claim is accepted by this inventory.

## Ratio and claim relationships in the bounded live witnesses

| Witness | Actual bounded statement/configuration | Reconciliation |
|---|---|---|
| `knowledge/design/SKILL.md:156`, `:185–187`; `guides/type.md:139–140`, `:472–475`; `guides/layout.md:496–500` | Statements describing the same narrow/wide default give 1.25 at 360px in SKILL.md:156 and type.md, versus 1.2 at the `@min` 360px default in SKILL.md:186 and layout.md:498. Both give the wide endpoint as 4/3 displayed 1.333. | The narrow default is a genuine same-baseline conflict: keep 1.25 and 1.2 distinct. `1.333` is an approximate display of exact `4/3`; it is not a separate exact multiplier. The layout passage at 179–181 is handled in its own row because it explicitly introduces its 1.2-at-360/1.25-at-1240 pair with “say.” |
| `guides/layout.md:179–184` | “Say” 1.2 at 360px and a different scale “say” 1.25 at 1240px, followed by a claim that the interpolated results are always proportionally harmonious. | The pair is an illustrative alternative, not a required project default and not a conflict with the later 360/1440 default. Its unequal ratios still contradict a mathematical reading of “always proportionally harmonious” at interior widths; any perceptual meaning of “harmonious” remains unassessed. Preserve the geometricity finding without recasting the example as a configuration error. |
| `guides/type.md:133–140`; `foundations-of-design.md:264–270` | “4:3 = 1.333” and the interval list says “perfect fourth (3:4 ≈ 1.333).” | Under ordinary left:right numeric division, 4:3 is 4/3 while 3:4 is 3/4. The latter gives 1.333 only when the musical interval is oriented low-to-high and the scale multiplier is its reciprocal. State the orientation when using interval notation. The arithmetic resolves the ratio; it does not verify the historical attribution or musical analogy. |
| `guides/type.md:458–461` | The sequence is called powers of `4/3` but printed as `1.000, 1.333, 1.777, 2.369, 3.157, 4.209`. | Exact `4/3` powers rounded to three decimals are `1.000, 1.333, 1.778, 2.370, 3.160, 4.214`. The printed values instead match powers of decimal `1.333` rounded to three decimals. The two representations must not be conflated. Negative powers of exact `4/3` round to `0.750, 0.563` for steps −1 and −2. |
| `guides/layout.md:179–196`, `:362–375`; `guides/type.md:472–478`; `foundations-of-design.md:279–284`; `design.md:363–369` | Linear interpolation is said to preserve a modular/geometric scale and constant proportions at every interior width; higher steps are said to grow faster. | The determinant in [the proof](fluid-scale-proof.md#scope-and-model) is positive for a genuine interior with unequal endpoint ratios. Geometry is preserved for equal ratios or at an endpoint. Step slopes depend on their own endpoint differences; the assigned `4` versus `8/3` counterexample disproves the universal faster-higher-step rule. |
| `guides/layout.md:935–945` | A clamped linear function is described as asymptotically approaching a higher scale. | A finite clamp reaches and then holds its endpoint; it does not asymptotically approach it. The proof's clamp section gives the bounded behavior. The adjacent `vi`/zoom/WCAG claim is not established by this arithmetic and remains unassessed. |
| `guides/type.md:463–485` | Exact ratios and percentages are mixed with judgments about contrast, safety and equal noticeability. | Golden-ratio step increase is about 61.8% (rounded 62%); `4/3` is a 33⅓% increase (rounded 33%); 1.125, 1.25 and 1.5 are respectively 12.5%, 25% and 50% increases. “Too much,” “safe,” “hard to create,” and “equally noticeable” are empirical or contextual claims, not consequences of those calculations. They remain unassessed. |
| `knowledge/design/SKILL.md:191–203`; `guides/layout.md:198–218`, `:519–527` | Space is tied to type; token and pair values are presented as generated by a shared system. | The alias and printed token/pair declarations are configuration occurrences. Their displayed values follow the old printed step-0 endpoint, but they do not fix the type-scale inconsistencies above. A shared base or grid coupling does not establish the universal geometricity claim. Confirm the intended token multipliers before implementation. |

The numeric metadata `(v4.0, 2012, 398 pages)` in FND-01 and “13 layout
primitives” in FND-03 are inventoried as numeric mentions, not verified facts.
The numeric per-site axis table in SK-09 is likewise configuration inventory,
not validation of axis semantics or typeface/site suitability. The initial
return omitted these source occurrences; their inclusion here does not expand
this assignment into font, source-fidelity or design-policy review. Other
non-numeric typography, grid, zero-breakpoint, responsive-design, color,
perception and source-attribution material remains unassessed.

## Published baseline CSS at root 16px

The actual step-0 declaration is
`clamp(1rem, 0.9015rem + 0.4924vi, 1.3337rem)`. With `1vi=w/100`, its
clamped values do not match the stated 360px/16px and 1440px/20px endpoints.
The intended step-0 linearly interpolated value below is the plan's declared
baseline model, not an empirical result.

| Width | Published CSS result | Declared baseline result | Published − declared |
|---:|---:|---:|---:|
| 360px | 16.19664px | 16px | 0.19664px |
| 900px | 18.85560px | 18px | 0.85560px |
| 1440px | 21.33920px (upper clamp) | 20px | 1.33920px |

At the upper width, the unclamped preferred term is 21.51456px; the published
upper bound truncates it to 21.33920px. The exact source calculation is recorded
in execution notes. The audit's proposed step-0 expression for the stated
360/16 to 1440/20 endpoints is
`clamp(1rem, 0.9166667rem + 0.3703704vi, 1.25rem)`; the endpoints and slope
follow directly from those inputs.

The bounded code block also prints `--step-1` and `--step-2`. Under the same
stated baseline assumptions (small base 16px, ratio 6/5; large base 20px,
ratio 4/3; root 16px), their endpoint comparison is:

| Step | Published lower / upper clamp (rem) | Expected exact lower / upper (rem) | Published CSS result at 360px / 1440px (px) | Expected result at 360px / 1440px (px) |
|---:|---|---|---|---|
| 0 | 1 / 1.3337 | 1 / 1.25 | 16.19664 / 21.33920 | 16 / 20 |
| 1 | 1.2 / 1.7783 | 1.2 / 5/3 | 19.49356 / 27.41104 | 19.2 / 80/3 |
| 2 | 1.44 / 2.3706 | 1.44 / 20/9 | 23.46752 / 34.99328 | 23.04 / 320/9 |

If these endpoint assumptions are retained, exact per-step coefficients before
serialization are `A=a−(b−a)/3` and `B=(40/27)(b−a)` for the 360–1440 viewport
interval at a 16px root. The resulting (A,B) pairs are step 0 `(11/12,10/27)`,
step 1 `(47/45,56/81)`, and step 2 `(796/675,1408/1215)`. The displayed CSS
should be regenerated from confirmed endpoint decisions; numbers alone do not
resolve the source's contradictory 1.25/1.2/1.333 prose.

The space declarations include `--space-s: var(--step-0)`, a `space-m` clamp,
`space-l`, and `space-s-m`/`space-s-l` pairs. Their endpoints are literal
configuration values in the witness spans, not independently verified design
choices. If the apparent 1.5× and 2× endpoint multipliers are confirmed, the
chosen step-0 correction would require regenerating those dependent endpoints
and slopes from the same root/viewport model. This assignment does not authorize
selecting or installing a space-token policy.

## Adopted diagnostic example: emitted table and expression

The actual seven rows parsed from the pinned example are:

| n | a (rem) | b (rem) | A (rem) | B (vi) |
|---:|---:|---:|---:|---:|
| −2 | 0.694444 | 0.720000 | 0.685926 | 0.042593 |
| −1 | 0.833333 | 0.900000 | 0.811111 | 0.111111 |
| 0 | 1.000000 | 1.125000 | 0.958333 | 0.208333 |
| +1 | 1.200000 | 1.406250 | 1.131250 | 0.343750 |
| +2 | 1.440000 | 1.757812 | 1.334062 | 0.529688 |
| +3 | 1.728000 | 2.197266 | 1.571578 | 0.782109 |
| +4 | 2.073600 | 2.746582 | 1.849273 | 1.121637 |

All 28 emitted coefficients equal exact formula values rounded to six decimal
places using half-even rounding. The actual step-0 CSS expression's four values
join its actual table row exactly: lower `1.000000rem`, A `0.958333rem`, B
`0.208333vi`, upper `1.125000rem`. No regenerated expected table substitutes
for these emitted values.

For each of 7 steps × 2 roots (16px, 20px) × 6 inline extents
(160, 320, 800, 1000, 1280, 1600px), the exact root-relative model was compared
to the emitted six-decimal `clamp(a, A + B vi, b)` expression: **84 cases**.
There were **32 exact grid matches** and **52 nonzero serialization deltas**;
all 84 are below 0.001px. “Nonzero” here means the rounded expression differs
from the exact rational reference; it does not mean an oracle failure. The
maximum absolute delta is `3/250000px = 0.000012px` at `(R=20,w=1600,n=0)`.
Every nonzero delta (location and printed-minus-exact px) is listed so the bound
is not the only reported result:

| R (px) | w (px) | n | Printed − exact (px) |
|---:|---:|---:|---:|
| 16 | 160 | −2 | −1/140625 |
| 16 | 160 | −1 | −1/187500 |
| 16 | 320 | −2 | 7/2812500 |
| 16 | 320 | −1 | −1/468750 |
| 16 | 320 | +4 | 1/156250 |
| 16 | 800 | −2 | 1/225000 |
| 16 | 800 | −1 | −1/375000 |
| 16 | 800 | 0 | −1/125000 |
| 16 | 800 | +2 | −1/250000 |
| 16 | 800 | +3 | −1/200000 |
| 16 | 800 | +4 | 31/4000000 |
| 16 | 1000 | −2 | 71/13500000 |
| 16 | 1000 | −1 | −13/4500000 |
| 16 | 1000 | 0 | −13/1500000 |
| 16 | 1000 | +2 | −3/1000000 |
| 16 | 1000 | +3 | −23/4000000 |
| 16 | 1000 | +4 | 133/16000000 |
| 16 | 1280 | −1 | −1/312500 |
| 16 | 1280 | 0 | −3/312500 |
| 16 | 1280 | +2 | −1/125000 |
| 16 | 1280 | +3 | −17/2500000 |
| 16 | 1280 | +4 | −1/2000000 |
| 16 | 1600 | +2 | −1/125000 |
| 16 | 1600 | +3 | 3/500000 |
| 16 | 1600 | +4 | −1/2000000 |
| 20 | 160 | −2 | −1/112500 |
| 20 | 160 | −1 | −1/150000 |
| 20 | 320 | −2 | −1/112500 |
| 20 | 320 | −1 | −1/150000 |
| 20 | 800 | −2 | 2/421875 |
| 20 | 800 | −1 | −7/2250000 |
| 20 | 800 | 0 | −7/750000 |
| 20 | 800 | +2 | −3/500000 |
| 20 | 800 | +3 | −11/2000000 |
| 20 | 800 | +4 | 73/8000000 |
| 20 | 1000 | −2 | 1/180000 |
| 20 | 1000 | −1 | −1/300000 |
| 20 | 1000 | 0 | −1/100000 |
| 20 | 1000 | +2 | −1/200000 |
| 20 | 1000 | +3 | −1/160000 |
| 20 | 1000 | +4 | 31/3200000 |
| 20 | 1280 | −2 | 113/16875000 |
| 20 | 1280 | −1 | −41/11250000 |
| 20 | 1280 | 0 | −41/3750000 |
| 20 | 1280 | +2 | −9/2500000 |
| 20 | 1280 | +3 | −73/10000000 |
| 20 | 1280 | +4 | 419/40000000 |
| 20 | 1600 | −1 | −1/250000 |
| 20 | 1600 | 0 | −3/250000 |
| 20 | 1600 | +2 | −1/100000 |
| 20 | 1600 | +3 | −17/2000000 |
| 20 | 1600 | +4 | −1/1600000 |

At root 16px and `w=800px`, exact steps 0/1/2 are 17, 20.85 and
25.5825px; adjacent ratios are `417/340` and `3411/2780`, not equal. At root
20px, `w=800px`, step 0 is `125/6px`; reusing fixed 320–1280px endpoints gives
21.25px and is rejected. Root 20px moves the diagnostic interval to 400–1600px.

## Controls and bounded result

- A printed-table A coefficient corrupted by `+1/10` at step 0 fails the same
  exact coefficient comparison used for the seven positive rows.
- A step-0 CSS/table disagreement fails the emitted-value join.
- Fixed-pixel 320–1280px endpoint reuse at root 20px fails the exact 800px oracle.
- The unequal-ratio midpoint fails the universal geometricity claim; valid
  equal-ratio and endpoint cases remain geometric, including the negative-step
  determinant control.

All these calculations are mathematical evidence about the emitted source and
adopted diagnostic. The diagnostic remains an example, not a functional text
recommendation, design default, readability finding, or accessibility promise.
