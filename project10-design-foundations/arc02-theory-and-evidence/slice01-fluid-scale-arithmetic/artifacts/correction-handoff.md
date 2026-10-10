# Proposed correction handoff for DES-003 / DES-004

This is a planning proposal from the bounded evidence in
[fluid-scale-proof.md](fluid-scale-proof.md) and
[configuration-reconciliation.md](configuration-reconciliation.md). It does not
edit the live skill or guides, resolve absent-source attribution, close DES-003/
DES-004, establish source readiness, or accept the complete card/guide corpus.
Every source occurrence remains pinned to `dffa504e851b03b8e4746f1941068e4cc850b612`.
The identifiers below are the local `claim_id` values in
[claim-results.jsonl](claim-results.jsonl).

## Replacement proposals

### 1. Replace universal interior-geometricity claims

**Occurrences:** `TY-05`, `LAY-01`, `LAY-02`, `LAY-03`, `LAY-06`, `LAY-07`,
`LAY-13`, `LAY-14`, `DES-01`, `FND-04`.

> For each integer step, fluid type is interpolated independently between its
> selected endpoint sizes using the same clamped linear parameter. The
> intermediate sizes form a geometric progression only when the endpoint ratios
> are equal or the interpolation is at an endpoint. With unequal endpoint
> ratios, an interior scale is not generally geometric. Each step's change
> across the viewport depends on its own endpoint difference; higher steps do
> not necessarily grow faster.

This replacement states the proved condition, not a perceptual rule. Keep
“harmonious,” “equally noticeable,” and historical/source-author claims only
with appropriate source and empirical evidence; the present arithmetic does not
support them.

### 2. State the finite clamp correctly

**Occurrences:** `LAY-02`, `LAY-12`, `LAY-13`, `LAY-14`, `FND-04`.

> A `clamp(min, preferred, max)` whose preferred term is linear in inline
> viewport size interpolates linearly only while that term lies between its
> bounds. Outside the declared interval the value saturates at the corresponding
> bound; it does not asymptotically approach an endpoint.

Keep `vi`'s unit definition separate from claims about writing modes, browser
zoom, reflow, or WCAG. Proposed replacement for the unsupported unit-to-
conformance sentence (`LAY-12`):

> `vi` expresses a size against the logical inline viewport. Its use alone does
> not establish text enlargement, reflow, or WCAG conformance; verify those
> behaviors with the applicable browser, content, and accessibility checks.

### 3. Make ratio notation and displayed precision explicit

**Occurrences:** `SK-01`, `SK-03`, `TY-01`, `TY-03`, `TY-04`, `TY-07`,
`FND-02`.

> When the larger size is divided by the smaller size, the exact perfect-fourth
> multiplier is `4/3 = 1.333…` (displayed approximately as `1.333`). Do not use
> the rounded decimal `1.333` as though it were exactly `4/3`. If a musical
> interval is written low-to-high as `3:4`, identify that orientation; the
> corresponding increasing size multiplier is its reciprocal, `4/3`.

For a sequence claimed to use exact `4/3`, propose the three-decimal values
`1.000, 1.333, 1.778, 2.370, 3.160, 4.214` for steps 0 through 5, and
`0.750, 0.563` for steps −1 and −2. The presently printed positive sequence
matches powers of decimal `1.333`, not exact `4/3`.

### 4. Reconcile the stated baseline endpoints and declarations

**Occurrences:** `SK-03`, `SK-04`, `SK-05`, `SK-07`, `TY-01`, `TY-05`,
`LAY-02`, `LAY-06`, `LAY-09`, `LAY-10`, `LAY-11`, `FND-04`.

For the baseline endpoint decisions assigned by the slice plan—360px/16px with
ratio `6/5`, and 1440px/20px with ratio `4/3`—the step 0–2 declarations at a
16px root are proposed as:

```css
--step-0: clamp(1rem, 0.9166667rem + 0.3703704vi, 1.25rem);
--step-1: clamp(1.2rem, 1.0444444rem + 0.6913580vi, 1.6666667rem);
--step-2: clamp(1.44rem, 1.1792593rem + 1.1588477vi, 2.2222222rem);
```

These coefficients are derived from the stated endpoint model, not from the
published declarations. Keep the genuine same-default narrow ratio conflict
visible: SKILL.md:156 and type.md:472–475 say 1.25 at 360px, while the declared
`@min` configuration at SKILL.md:185–187 and layout.md:496–500 says 1.2 there.
The pair in layout.md:179–181 is introduced as an example (“say”) and is not a
required default conflict; its universal geometricity claim is separately
covered in proposal 1. For the bounded calculation, use the plan's explicit
360/16/6/5 and 1440/20/4/3 oracle, without treating that choice as a live-source
resolution.

The `space-s`, `space-m`, `space-l` and space-pair declarations depend on the
base-scale correction. Preserve their current named roles only if the owner
confirms the visible multipliers; then regenerate all endpoint, intercept and
slope values from the accepted scale and token relationships. Do not carry
forward values derived from the incorrect step-0 maximum. `SK-07` is inventoried
as literal space-token configuration; dependent values remain conditional on
owner confirmation of those multipliers.

### 5. Keep advice and empirical claims qualified

**Occurrences:** `SK-02`, `SK-06`, `SK-08`, `SK-09`, `TY-02`, `TY-04`, `TY-06`,
`LAY-04`, `LAY-05`, `LAY-08`, `LAY-09`, `LAY-11`, `LAY-15`, `FND-01`,
`FND-03`.

**Additional numeric inventory:** `SK-09` records the three-site axis values at
SKILL.md:173–177 without evaluating typeface/axis semantics or site suitability.
`LAY-15` records the numbered principle marker and numeric size examples at
layout.md:353–360; both printed differences are `+4px`, while the perceptual
comparison and normative advice remain unassessed. `TY-07` is handled with the
ratio notation in proposal 3.

No correction to typeface/axis roles, the zero-breakpoint preference, grid
coupling, token architecture, Weber–Fechner/noticeability claims, musical or
historical attribution, bibliographic details, or layout-primitive inventory is
proposed from this arithmetic-only assignment. Keep those occurrences explicitly
pending their source/empirical/contextual review. A project convention can be
retained only as a locally chosen convention; do not present it as a universal
mathematical requirement.

## Result and later owners

- The proof supports replacing the DES-003 claim of universal intermediate
  geometricity and universal faster growth, subject to CDC review.
- The actual published step clamps and conflicting ratio descriptions support a
  DES-004 correction proposal. No live file, card, package or source is changed.
- CDC owns independent review of this packet and any follow-up source scope.
  Any eventual live mutation requires a distinct exact allowlist, new source
  revision, version/history treatment and independent verification.
- Original/edition/capture fidelity remains under Arc02 CDC + Operator/P10-11.
  No attributed author/source claim is certified here.
- Complete 233-card and eight-live-file claim/dimension review, repeated-claim
  reconciliation, relationship/CQ support and revision effects remain with
  later C/L/G work. DES-005 accessibility, rendering, browser zoom/reflow,
  perceptual, typography/font-role, package/runtime and release checks remain
  with their existing Arc03–05 / Project10 gates.

No finding, project criterion, source-readiness row, or higher-scale gate is
closed by this proposal.
