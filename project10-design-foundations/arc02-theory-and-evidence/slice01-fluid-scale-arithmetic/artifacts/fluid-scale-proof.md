# Fluid-scale interpolation: proof and limits

## Scope and model

This proof addresses the mathematical claims in the nine bounded live-source
witness spans listed in the [slice plan](../slice-plan.md#pins-inputs-and-bounded-source-witnesses).
It establishes facts about a shared-parameter interpolation of positive geometric
sequences. It does not establish perceptual quality, source attribution, browser
behavior, accessibility, or the correctness of an empirical rationale.

Let endpoint bases `a,b > 0`, ratios `r,q > 0`, integer step `n`, and a common
interpolation parameter `t ∈ [0,1]` be given. Define

```text
u = (1-t)a
v = tb
s_n = u r^n + v q^n
```

The same `t` is used for every `n`. Expanding two adjacent products gives

```text
s_n s_(n+2) - s_(n+1)^2
= (u r^n + v q^n)(u r^(n+2) + v q^(n+2))
  - (u r^(n+1) + v q^(n+1))^2
= u v (r q)^n (r^2 + q^2 - 2 r q)
= u v (r q)^n (r-q)^2.
```

The pure `u²` and `v²` terms cancel. Since `u,v ≥ 0` and `r,q > 0`, the
right-hand side is nonnegative. At a genuine interior (`0<t<1`), `u,v>0`, so it
is strictly positive exactly when `r≠q`. A positive sequence is geometric at
steps `n,n+1,n+2` exactly when this determinant is zero. Therefore every
interior step triple is geometric when `r=q`; for different ratios it is not.
At `t=0` or `t=1`, one coefficient vanishes and the remaining endpoint
progression is geometric. For negative integer `n`, `(rq)^n` remains positive,
so the same condition and conclusion hold. This is an exact algebraic result,
not a perceptual result.

## Baseline midpoint and growth counterexample

For the source's declared endpoints, the audit's midpoint model is

```text
s_n(1/2) = (16(6/5)^n + 20(4/3)^n)/2.
```

At steps 0 through 3 the exact values are `18`, `344/15`, `6592/225`, and
`126656/3375`. Their three adjacent ratios are `172/135`, `824/645`, and
`1979/1545`; they are unequal. The steps-0-to-2 determinant is `64/45 > 0`.
This reproduces the DES-003 counterexample from the pinned audit and shows why
endpoint scales alone do not prove an interior geometric scale.

“Higher steps grow faster” is not a consequence of linear interpolation. For
the plan's counterexample endpoints `a=16,b=20,r=4/3,q=6/5`, the endpoint
changes `b q^n - a r^n` are `4` at step 0 and `8/3` at step 1. The higher step
has the smaller endpoint change. For a fixed step, its linear slope is governed
by that step's endpoint difference; ordering steps does not order those
differences without additional assumptions.

## Clamp behavior

For the adopted diagnostic, with inline extent `w` CSS px and root size `R` CSS
px, the common parameter is

```text
t(w,R) = max(0, min((w/R - 20)/60, 1)).
```

Each step interpolates linearly between its two declared endpoints while
`20R ≤ w ≤ 80R`. Below that interval it is fixed at the lower endpoint; above
it it is fixed at the upper endpoint. This finite, clamped function saturates
at the endpoints. It does not asymptotically approach an endpoint as width
increases. Each step has its own endpoint difference and hence its own slope.
The numerical interpretation used here is `1vi = w/100`; no browser or writing
mode execution is implied.

## Valid special cases and proof controls

- Equal endpoint ratios give determinant zero at every `t`, including a genuine
  interior. The sequence is `((1-t)a + tb) r^n`.
- At either interpolation endpoint, the determinant is zero even if `r≠q`.
- With positive coefficients, unequal positive ratios, and any integer step
  including `n=-2`, the determinant is strictly positive. The evaluated
  negative-step control agrees with the identity.
- The attempted universal geometric claim fails on the midpoint example above;
  the endpoint and equal-ratio controls still pass.

These results justify a mathematical correction to universal proportionality
claims. They do not establish that any scale is harmonious, equally noticeable,
readable, accessible, or appropriate for a project. Claims about Weber–Fechner,
musical harmony, source authorship, observed design outcomes, browser zoom,
reflow, CSS support, WCAG conformance, relationships, and competency-question
coverage require other evidence and remain unassessed here.
