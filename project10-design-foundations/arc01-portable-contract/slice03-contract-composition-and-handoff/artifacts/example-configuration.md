# Diagnostic fluid-type configuration

**Status:** one CDC-selected diagnostic arithmetic/configuration case, not a
font, spacing, palette, token, role or accessibility default. No named font,
palette, spacing token or functional text role is assigned. Negative steps are
arithmetic probes, not recommendations for functional text.

## Equation and serialized expressions

Let integer step `n` range from -2 through 4. With small scale base `1rem` and
ratio `6/5`, and large scale base `9/8rem` and ratio `5/4`:

- `a(n) = (6/5)^n` rem
- `b(n) = (9/8) * (5/4)^n` rem
- For inline extent `w` CSS px and root size `R` CSS px,
  `t = clamp(0, (w/R - 20)/60, 1)`
- Exact per-step size is `R * ((1-t)*a(n) + t*b(n))` px; the
  endpoint interpolation is linear per step, not generally geometric at
  interior widths.
- `A = a - (b-a)/3`; `B = 100*(b-a)/60`.
- Serialize as `clamp(a rem, calc(A rem + B vi), b rem)` with each coefficient
  rounded to six decimal places.

| n | a (rem) | b (rem) | A (rem) | B (vi coefficient) |
|---:|---:|---:|---:|---:|
| -2 | 0.694444 | 0.720000 | 0.685926 | 0.042593 |
| -1 | 0.833333 | 0.900000 | 0.811111 | 0.111111 |
| +0 | 1.000000 | 1.125000 | 0.958333 | 0.208333 |
| +1 | 1.200000 | 1.406250 | 1.131250 | 0.343750 |
| +2 | 1.440000 | 1.757812 | 1.334062 | 0.529688 |
| +3 | 1.728000 | 2.197266 | 1.571578 | 0.782109 |
| +4 | 2.073600 | 2.746582 | 1.849273 | 1.121637 |

For step 0 the declaration is:

```css
--example-step-0: clamp(1.000000rem, calc(0.958333rem + 0.208333vi), 1.125000rem);
```

At reference root `R=16px`, endpoints are nominally 320–1280 CSS px; at
`R=20px`, the same `20rem–80rem` interval moves to 400–1600 CSS px. A root
change therefore moves the endpoints; retaining fixed 320–1280 px endpoints is
a different, incorrect interpretation of this selected config.

## Bounded numerical check

The inline rational checker compares all seven steps at both roots against six
inline extents: `w = 160, 320, 800, 1000, 1280, 1600` CSS px. It evaluates exact
rational endpoints/interpolation and the six-decimal `a/b/A/B` expressions,
including clamp saturation below/above range. This is 84 comparisons; observed
maximum absolute discrepancy is 0.000012 px at `R=20,
w=1600, n=0`, below the 0.001px bound.

At `R=16, w=800`, steps 0/1/2 are exactly 17, 20.85 and 25.5825 px. The adjacent
ratios are `417/340` and `3411/2780`, which differ; an interior result cannot be
claimed to preserve a geometric progression. At `R=20, w=800`, step 0 is
`125/6` px. Reusing the old fixed-pixel 320–1280 interval incorrectly produces
21.25 px there; the selected root-relative interval yields `125/6`. At
`R=20, w=1000`, step 0 is 21.25 px.

The arithmetic does not test a browser, font rendering, user text enlargement,
reflow, contrast, readable role selection, keyboard/AT behavior or WCAG
conformance. A `vi` coefficient does not prove enlargement compliance. Those
checks stay with later authorized Arc03/Arc04/Arc05 work.
