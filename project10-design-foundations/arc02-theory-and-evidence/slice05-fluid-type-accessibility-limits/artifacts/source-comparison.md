# Slice05 source comparison and model evidence

SOURCE `dffa504e851b03b8e4746f1941068e4cc850b612`; values below are reproducible models, not browser observations. Current source identity and seven complete windows are in [occurrence inventory](occurrence-inventory.jsonl). Fifteen assigned atomic results are in [claim results](claim-results.jsonl).

## Primary source comparison

| ID | Source and exact inspected scope | Supports | Limit retained |
|---|---|---|---|
| CV | [CSS Values and Units Level 4, Working Draft 12 Mar 2024](https://www.w3.org/TR/2024/WD-css-values-4-20240312/): full §6.1.1 rem and user minimum-font notes; §6.1.2 intro and all §6.1.2.2 variants; complete §10.2 comparison functions. | `rem` equals computed `em` on root; minimum-font preference may affect used values without changing font-relative resolution; `vi` is 1% of the applicable viewport variant on the element inline axis; `clamp` clamps central value and favors minimum if bounds conflict. | Normative definitions do not predict browser/user setting outcomes for these pages or accessibility conformance. Draft is identified as work in progress. |
| WC | [WCAG 2.2 Recommendation 12 Dec 2024](https://www.w3.org/TR/2024/REC-WCAG22-20241212/): complete normative SC 1.4.4 and 1.4.10, including notes/exceptions. | AA SC 1.4.4 requires text (except captions/images of text) resizable to 200% without loss; AA SC 1.4.10 addresses no loss and no two-dimensional scroll at 320 CSS px width for vertical-scroll content or 256 CSS px height for horizontal-scroll content, except content requiring 2-D layout for use/meaning. | Neither criterion is satisfied by unit choice alone; requires content/functionality testing. |
| RT | [Understanding SC 1.4.4](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html): complete criterion/intent, all three intent notes and guidance through resize mechanisms. | Informative guidance says at least one supported user-agent text-scaling mechanism can suffice; intermediate offered steps must preserve content/functionality; page zoom, text-only, and text-size settings are distinct possible methods. | Understanding is informative, not the normative SC; not every mechanism is mandated. |
| RF | [Understanding SC 1.4.10](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html): criterion/notes/intent, full Basic text reflow and reflowing-site sections. | Horizontal languages reflow at width 320; vertical-language sections at height 256; 2-D-use exceptions remain, while table cells still need reflow. | Informative explanation and examples are not runtime evidence or conformance checks. |
| F94 | [Failure F94](https://www.w3.org/WAI/WCAG22/Techniques/failures/F94): complete technique body, examples, test procedure and expected result; page reports update 9 Mar 2026. | Viewport units used as primary text-size method are likely to fail 1.4.4; some uses may not prevent adjustment; media queries/author controls can be alternatives. | Failure technique has qualifications and alternatives; it does not show all mixed rem/vi clamps fail or ban viewport units. |
| UT | [Utopia calculator](https://utopia.fyi/type/calculator/): complete 66-line returned text, default inputs and complete generated CSS. | Current returned default displays min 360px / 18px / 1.2 and max 1240px / 20px / 1.25; generated CSS uses `vw`. | A live calculator state, not a historical capture, author attribution, universal configuration or evidence of accessibility. Dynamic UI not exercised. |

## Literal coefficient model: all 144 evaluations

`F(R,I)=clamp(mR, aR + bI/100, MR)`. Decimal coefficients below are parsed as exact base-10 Fractions from the four source declarations; no coefficient is rounded or repaired. For each baseline `F(R,I)`, each zoom column reports `z*F(R,I/z)` in assumed apparent units, then ratio to the unzoomed `F(R,I)`; branch is the inner value below/inside/above the bounds. Zoom is a stipulated model with root fixed. Changing R is separately represented by the R rows, not inferred from zoom. Every row evaluates one formula × root × inline extent × four zoom factors (=144 results).

| Formula | R px | I px | F(R,I) px | z=1 apparent (ratio;branch) | z=1.25 | z=2 | z=4 |
|---|---:|---:|---:|---|---|---|---|
| SK195 | 16 | 360 | 16.1966 | 16.1966 (1.000; inside) | 20.0000 (1.235; lower) | 32.0000 (1.976; lower) | 64.0000 (3.951; lower) |
| SK195 | 16 | 800 | 18.3632 | 18.3632 (1.000; inside) | 21.9692 (1.196; inside) | 32.7872 (1.785; inside) | 64.0000 (3.485; lower) |
| SK195 | 16 | 1440 | 21.3392 | 21.3392 (1.000; upper) | 25.1206 (1.177; inside) | 35.9386 (1.684; inside) | 64.7866 (3.036; inside) |
| SK195 | 20 | 360 | 20.0000 | 20.0000 (1.000; lower) | 25.0000 (1.250; lower) | 40.0000 (2.000; lower) | 80.0000 (4.000; lower) |
| SK195 | 20 | 800 | 21.9692 | 21.9692 (1.000; inside) | 26.4767 (1.205; inside) | 40.0000 (1.821; lower) | 80.0000 (3.641; lower) |
| SK195 | 20 | 1440 | 25.1206 | 25.1206 (1.000; inside) | 29.6281 (1.179; inside) | 43.1506 (1.718; inside) | 80.0000 (3.185; lower) |
| SK195 | 32 | 360 | 32.0000 | 32.0000 (1.000; lower) | 40.0000 (1.250; lower) | 64.0000 (2.000; lower) | 128.0000 (4.000; lower) |
| SK195 | 32 | 800 | 32.7872 | 32.7872 (1.000; inside) | 40.0000 (1.220; lower) | 64.0000 (1.952; lower) | 128.0000 (3.904; lower) |
| SK195 | 32 | 1440 | 35.9386 | 35.9386 (1.000; inside) | 43.1506 (1.201; inside) | 64.7866 (1.803; inside) | 128.0000 (3.562; lower) |
| SK196 | 16 | 360 | 19.4936 | 19.4936 (1.000; inside) | 24.0000 (1.231; lower) | 38.4000 (1.970; lower) | 76.8000 (3.940; lower) |
| SK196 | 16 | 800 | 22.7192 | 22.7192 (1.000; inside) | 26.9328 (1.185; inside) | 39.5736 (1.742; inside) | 76.8000 (3.380; lower) |
| SK196 | 16 | 1440 | 27.4110 | 27.4110 (1.000; inside) | 31.6246 (1.154; inside) | 44.2654 (1.615; inside) | 77.9742 (2.845; inside) |
| SK196 | 20 | 360 | 24.0000 | 24.0000 (1.000; lower) | 30.0000 (1.250; lower) | 48.0000 (2.000; lower) | 96.0000 (4.000; lower) |
| SK196 | 20 | 800 | 26.9328 | 26.9328 (1.000; inside) | 32.1998 (1.196; inside) | 48.0008 (1.782; inside) | 96.0000 (3.564; lower) |
| SK196 | 20 | 1440 | 31.6246 | 31.6246 (1.000; inside) | 36.8916 (1.167; inside) | 52.6926 (1.666; inside) | 96.0000 (3.036; lower) |
| SK196 | 32 | 360 | 38.4000 | 38.4000 (1.000; lower) | 48.0000 (1.250; lower) | 76.8000 (2.000; lower) | 153.6000 (4.000; lower) |
| SK196 | 32 | 800 | 39.5736 | 39.5736 (1.000; inside) | 48.0008 (1.213; inside) | 76.8000 (1.941; lower) | 153.6000 (3.881; lower) |
| SK196 | 32 | 1440 | 44.2654 | 44.2654 (1.000; inside) | 52.6926 (1.190; inside) | 77.9742 (1.762; inside) | 153.6000 (3.470; lower) |
| SK200 | 16 | 360 | 24.2954 | 24.2954 (1.000; inside) | 30.0000 (1.235; lower) | 48.0000 (1.976; lower) | 96.0000 (3.951; lower) |
| SK200 | 16 | 800 | 27.5448 | 27.5448 (1.000; inside) | 32.9540 (1.196; inside) | 49.1816 (1.786; inside) | 96.0000 (3.485; lower) |
| SK200 | 16 | 1440 | 32.0096 | 32.0096 (1.000; upper) | 37.6804 (1.177; inside) | 53.9080 (1.684; inside) | 97.1816 (3.036; inside) |
| SK200 | 20 | 360 | 30.0000 | 30.0000 (1.000; lower) | 37.5000 (1.250; lower) | 60.0000 (2.000; lower) | 120.0000 (4.000; lower) |
| SK200 | 20 | 800 | 32.9540 | 32.9540 (1.000; inside) | 39.7155 (1.205; inside) | 60.0000 (1.821; inside) | 120.0000 (3.641; lower) |
| SK200 | 20 | 1440 | 37.6804 | 37.6804 (1.000; inside) | 44.4419 (1.179; inside) | 64.7264 (1.718; inside) | 120.0000 (3.185; lower) |
| SK200 | 32 | 360 | 48.0000 | 48.0000 (1.000; lower) | 60.0000 (1.250; lower) | 96.0000 (2.000; lower) | 192.0000 (4.000; lower) |
| SK200 | 32 | 800 | 49.1816 | 49.1816 (1.000; inside) | 60.0000 (1.220; inside) | 96.0000 (1.952; lower) | 192.0000 (3.904; lower) |
| SK200 | 32 | 1440 | 53.9080 | 53.9080 (1.000; inside) | 64.7264 (1.201; inside) | 97.1816 (1.803; inside) | 192.0000 (3.562; lower) |
| SK203 | 16 | 360 | 16.9917 | 16.9917 (1.000; inside) | 20.0000 (1.177; lower) | 32.0000 (1.883; lower) | 64.0000 (3.767; lower) |
| SK203 | 16 | 800 | 27.9072 | 27.9072 (1.000; inside) | 29.9224 (1.072; inside) | 35.9680 (1.289; inside) | 64.0000 (2.293; lower) |
| SK203 | 16 | 1440 | 42.6784 | 42.6784 (1.000; upper) | 45.7995 (1.073; inside) | 51.8451 (1.215; inside) | 67.9667 (1.593; inside) |
| SK203 | 20 | 360 | 20.0000 | 20.0000 (1.000; lower) | 25.0000 (1.250; lower) | 40.0000 (2.000; lower) | 80.0000 (4.000; lower) |
| SK203 | 20 | 800 | 29.9224 | 29.9224 (1.000; inside) | 32.4414 (1.084; inside) | 40.0000 (1.337; lower) | 80.0000 (2.674; lower) |
| SK203 | 20 | 1440 | 45.7995 | 45.7995 (1.000; inside) | 48.3185 (1.055; inside) | 55.8755 (1.220; inside) | 80.0000 (1.747; lower) |
| SK203 | 32 | 360 | 32.0000 | 32.0000 (1.000; lower) | 40.0000 (1.250; lower) | 64.0000 (2.000; lower) | 128.0000 (4.000; lower) |
| SK203 | 32 | 800 | 35.9680 | 35.9680 (1.000; inside) | 40.0000 (1.112; lower) | 64.0000 (1.779; lower) | 128.0000 (3.559; lower) |
| SK203 | 32 | 1440 | 51.8451 | 51.8451 (1.000; inside) | 55.8755 (1.078; inside) | 67.9667 (1.311; inside) | 128.0000 (2.469; lower) |

| Formula | SOURCE line | min m | root coefficient a | viewport coefficient b | max M |
|---|---:|---:|---:|---:|---:|
| SK195 | 195 | 1 | 0.9015 | 0.4924 | 1.3337 |
| SK196 | 196 | 1.2 | 1.0534 | 0.7331 | 1.7783 |
| SK200 | 200 | 1.5 | 1.3523 | 0.7385 | 2.0006 |
| SK203 | 203 | 1 | 0.5038 | 2.4808 | 2.6674 |

The table is exact rational evaluation, formatted to four decimals (ratio to three); equality at a bound is labelled `inside`. It exposes model behavior at all requested inputs and is not an observation of browser zoom, text-only resizing, user root preferences or screen-reader behavior.

### Independent toy witnesses and axis selection

Toy `clamp(1rem, .5rem + 2vi, 2rem)`, 800px inline extent, R=16px: lower=16, preferred=24, upper=32, so F=24. Under the explicitly assumed 2× page-zoom model I/z=400, R fixed: preferred=16, F=16, apparent=32, ratio=4/3 to baseline 24 (not 2). Separately set R=32 with I=800: lower=32, preferred=32, upper=64, F=32. Pure `2vi` gives 16 at I=800 and apparent 16 under z=2 (8×2), showing cancellation only for that pure viewport model. Lower witness I=100 gives preferred=10 and F=16; upper witness I=2000 gives preferred=48 and F=32.

At an 800×600 CSS-px viewport, `vi` is width-based in horizontal writing: 8px; for vertical inline axis it is height-based: 6px. `vw` remains width-based: 8px. This checks axis selection only. It does not establish enlargement or reflow.

### Complete inventory and retained boundaries

Every window record retains all source lines, hashes and an independently declared membership projection. The following are outside the new technical verdict unless identified as C rows; full selected source text is still in the inventory. Boundary records give exact source wording, current disposition, reason and owner. Markup records preserve representation separately from substantive claims.

| ID | Exact original subject | Why not judged here / owner |
|---|---|---|
| B01 | SKILL.md:68 — All scales (type, space, colour lightness) must be geometric, not arithmetic. | Remaining Arc02 T/L; Slice01 assessed bounded arithmetic elsewhere, not this general principle. |
| B02 | SKILL.md:70 — “Never use `var(--brand-700)` in a component.” | Token-layer rule is Slice03/DES-008 territory; do not reopen with this accessibility pass. |
| B03 | SKILL.md:71 — Small palettes “produce better outcomes than infinite options.” | Outcome evidence and C&B/site context belong to remaining T/L. |
| B04 | SKILL.md:72 — “Same skeleton, different posture.” | Cross-site identity and design outcome remain T/L. |
| B05 | SKILL.md:73 — “Intra-group spacing < inter-group spacing. Always.” | General spatial/perceptual universal remains T/L. |
| B06 | SKILL.md:74 — “Define relationships (ratios, mappings, axioms), not individual values. The system generates instances.” | General method scope remains T/L. |
| B07 | layout.md:112–115 — “The Units chapter makes the case against pixels with precision. The value of `1px` is not what it seems—it varies across devices, zoom levels, and display densities. More importantly, pixels create no relationship between the value and the content it measures.” | This pixel/measure argument is a distinct T claim, not evidence that `rem` tracks preferences. Remaining Arc02 T/L. |
| B08 | layout.md:115–118 — “The `ch` unit, by contrast, is defined by the font’s own geometry: `60ch` is always roughly 60 characters wide, regardless of font size or screen density.” | Current CV definition is a glyph advance (used “0” glyph with fallback), not a guaranteed count of arbitrary characters; this slice does not judge local measure suitability. Remaining T/L. |
| B09 | layout.md:119–122 — “The `em` unit creates local proportional relationships, so that a child element scales with its parent. Each unit encodes a kind of relationship, and choosing the right unit is choosing the right relationship.” | Parent-relative mechanics and universal unit-selection advice are outside assigned rem/root question. Remaining T/L. |
| B10 | layout.md:941–945 — “The modular scale itself is a geometric progression: `size(n) = base × ratio^n`. Interpolating between two geometric progressions produces a family of curves, each asymptotically approaching the higher progression as the viewport widens. This is why the visual hierarchy intensifies on larger screens without any explicit instruction to do so.” | The bounded numeric progression/clamp witness is covered by accepted Slice01 LAY-13/14 and is not reopened here. C10 separately assesses the overlapping current claim that the family asymptotically approaches the higher progression; no whole family was recomputed here. The final visual/perceptual explanation remains T/L. |
| B11 | design.md:152 — “Every unit of measurement should describe the experience, not the mechanism.” | General design maxim remains T/L; C14 assesses only nearby vi/rem wording. |
| B12 | breaking-the-layout-monoculture.md:208–211 — “When the type scale is built on musical interval ratios (perfect fourth at 4:3, perfect fifth at 3:2, major third at 5:4), the space system inherits that proportional harmony automatically.” | Music attribution, orientation and perceived harmony are not proved by the CSS/accessibility primaries. Remaining T/L; no source lineage. |
| B13 | type.md:475–478 — “This means headings grow proportionally faster than body text as the viewport widens—Bringhurst’s principle that display type needs more air, and text type needs more density, implemented in pure CSS mathematics.” | Stepwise growth is input-dependent; attribution and perceptual explanation are outside this unit’s current evidence. C15 proposes qualification, but does not establish historic attribution or perception. Remaining T/L. |
| M01 | SKILL.md:66–74 — Markdown table pipes, separator row and cell boundaries. | Markup classification only; the cell assertion B01–B06/C01 remains substantive. |
| M02 | SKILL.md:189–204 — section heading and fenced CSS example. | Code fence/heading syntax retained; four literal formula lines C04–C07 are substantive model inputs. |
| M03 | layout.md:934 and :946 — `::: prose` open/close delimiters. | Markup only; adjacent technical sentences are C09/C10. |
| M04 | breaking-the-layout-monoculture.md:195–220 — heading anchor/style attribute, fenced prose delimiters, Markdown summary table and separator. | Markup only; C11–C13 assess relevant cell prose and summary claim separately. |

W02 remains completely inventoried; C02/C03 and literal formulas C04–C07 cover its in-scope configuration and shared-system statements. Its heading/code markup is M02. The W04 C10 literal span intersects a previously accepted Slice01 arithmetic range; its zoom/WCAG neighbor C09 is fresh assigned work. The W05 title, prose delimiters and summary table remain M04 rather than substantive evidence. Every source occurrence and line is retained; no whole-file, card or corpus review is inferred.

### Original pairs and relation boundary

C09 (layout.md:937–940) and C11 (breaking-the-layout-monoculture.md:198–204) are comparable originals: both infer zoom accessibility / WCAG satisfaction from `vi`. Their originals repeat the same unsupported inference, not contradictory content; each receives its own correction because each source occurrence remains independently assigned. C14 (design.md:148–152) overlaps the axis/root advice but does not assert a WCAG guarantee. C08 and C14 repeat the root-preference relationship; C14 is broader than the specification warrant. C15’s 1.25 narrow ratio conflicts with C02’s current Project10 1.2 baseline, while both display the wide ratio as approximate 1.333; this is a real input mismatch, not equivalent endpoints. No card graph/CQ or historic source lineage was inspected.
