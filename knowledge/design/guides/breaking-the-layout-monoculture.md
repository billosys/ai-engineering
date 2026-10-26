:::: hero

Strategies for Post-Template Web Design

# Breaking the Layout Monoculture

[A synthesis of academic research, modern CSS capabilities, editorial
design traditions, and spatial cognition applied to the question every
designer is asking: How do we make websites that don\'t all look the
same?]{.subtitle}

::: tag-row
[Research]{.tag} [CSS]{.tag} [Layout]{.tag} [Intrinsic Design]{.tag}
[Wayfinding]{.tag} [March 2026]{.tag}
:::
::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: container
::: section-label
The Problem
:::

## Research on Layout Similarity

::: prose
The [CHI 2021 author project abstract](https://cv-web-history.neocities.org/)
reports computer-vision analysis of representative website screenshots from
2003–2019. It reports increased similarity since 2007, especially in layouts,
where average distances decreased by over 30%, and interviews with 11 experienced
web design professionals. The authors discuss shared source/libraries, colour
standardisation and mobile support as possible factors. This is a bounded
reported result, not 30% whole-web sameness, a monotonic sixteen-year trend or
proof that template use causes harm. The full paper was unavailable for this
review; the abstract does not settle its methods and limitations.
:::

::: epigraph
Every page consists of containers in containers in containers; sometimes
text, sometimes images. Nothing is truly designed, it\'s simply assumed.

--- Boris Müller, Professor of Interaction Design, FH Potsdam
:::

::: prose
One design critique is that familiar column systems can persist after the
constraints that motivated them change. Current CSS offers other compositions;
a familiar grid may still serve a task well. Treat this as a prompt to examine
a convention, not a claim that all former limitations have disappeared.

Banner-blindness and visual-search research are useful reading pointers for
attention in their tested settings. They do not establish that a recurring
hero/features/testimonials sequence makes every visitor ignore a page, or that
template predictability universally harms comprehension and engagement.
Measure the actual navigation or reading problem before claiming such effects.

Shared tools can encourage repetition, but also provide useful consistency.
Vasilis van Gemert's context-specific design stance offers a productive question:
what does this particular audience, content and task need? This guide argues for
intentional variety rather than novelty or a universal rejection of templates.
:::

------------------------------------------------------------------------

::: section-label
The Toolkit
:::

## The New CSS Toolkit Makes Intrinsic Layout Real

CSS offers two-dimensional and content-responsive tools that can reduce
manual layout work in suitable cases. Check target support and fallback behavior;
no portable adoption percentage or first-invention claim is implied here.

::::::: feature-grid
::: feature-card
#### CSS Subgrid

A nested grid can participate in its parent grid's tracks with `subgrid`,
helping align content across components. Track sizing, content and markup still
need review; it is a useful mapping to compound-grid design, not a historical
first or automatic recreation of a print system.
:::

::: feature-card
#### Container Queries

Size queries adapt descendants according to an eligible ancestor query
container with the appropriate containment, not arbitrary component self-size.
Choose thresholds from content. Container units such as `cqw`/`cqh` also depend
on eligible containers; when none is available for an axis, their specified
fallback uses the small viewport size. Declare a usable base and check both
queried and fallback cases. See [container queries](https://www.w3.org/TR/css-contain-3/#container-rule).
:::

::: feature-card
#### Scroll-Driven Animations

`animation-timeline: scroll()` maps progress to a scroll range;
`animation-timeline: view()` maps progress across an element's visibility range
in its nearest ancestor scrollport. It is not a one-shot entry trigger.
Keep essential content visible at rest, without feature support and with reduced
motion. Use animation as decoration and check actual target behavior; a CSS
timeline does not replace every animation library. See [view progress timelines](https://www.w3.org/TR/scroll-animations-1/#view-timelines).
:::

::: feature-card
#### View Transitions API

For eligible same-origin cross-document navigation, both pages must opt in
with `@view-transition { navigation: auto; }`. Same-document transitions start
with JavaScript `document.startViewTransition()`; that path is not CSS-only.
Use unique active `view-transition-name` values, preserve ordinary navigation
as the fallback, and provide a reduced-motion alternative. A transition can
suggest continuity, but does not establish wayfinding benefit. See [activation](https://www.w3.org/TR/css-view-transitions-2/#cross-doc-opt-in).
:::
:::::::

::: notes
### Other Capabilities Worth Noting

**CSS `:has()`** supports relational, content-conditional styling; inspect
selector matching and target support rather than assuming every layout needs it.

**Anchor positioning** supplies geometry relative to an anchor. It does not
supply a complete Floating UI replacement or widget roles, names, keyboard,
focus, dismissal and collision policies for every task. Use maintained native
patterns or [APG interaction guidance](https://www.w3.org/WAI/ARIA/apg/patterns/).

**CSS math functions** such as `round()` can quantize a value. Neither rounding
nor the `cap` unit alone guarantees baseline alignment: `cap` uses the first
available font's used cap height, with specified fallbacks. Check line boxes,
font metrics, fallback runs and actual alignment. See [font-relative units](https://www.w3.org/TR/css-values-4/#cap).

**Masonry/grid-lanes** remains an unverified reading pointer in this guide, not
a current implementation or product-history claim. Inspect the actual target
and current specification before adopting it.

**`@scope`, nesting and `@layer`** address selector scope, nested rule syntax and
cascade ordering respectively. They do not prevent every style leak, remove all
specificity/origin interactions or replace every JavaScript/preprocessor feature.

Choose progressive enhancements for a concrete purpose. Keep semantics,
interaction and a usable base separate from the geometry an enhancement offers.
:::

------------------------------------------------------------------------

::: section-label
The Stack
:::

## The Intrinsic Design Stack

One useful approach combines Every Layout\'s composable primitives with
project-supplied values. Utopia is an optional source of fluid values, not a
requirement or a ranking of all layout methods.

### Every Layout\'s Primitives

::: prose
Every Layout (Heydon Pickering and Andy Bell) describes 13 primitives:
Stack, Box, Center, Cluster, Sidebar, Switcher, Cover, Grid, Frame, Reel,
Imposter, Icon and Container. They suggest spatial relationships and intrinsic
constraints. Queries, fixed values and other structures remain available when
content or behavior calls for them; this is not a zero-query requirement or an
invention-priority claim.

Gap can express Stack spacing; subgrid can help nested Grid alignment;
container queries can clarify Switcher modes. Dynamic viewport units can help
some Cover sizing cases but do not fix every mobile viewport issue. A Reel's
overflow and an Imposter's position are geometry, not complete carousel/dialog/
tooltip behavior. Preserve reading order, focus and native interaction patterns.
:::

### Utopia\'s Fluid Mathematics {#utopias-fluid-mathematics style="margin-top: var(--space-l);"}

::: prose
Utopia offers methods for interpolating selected type or space values
between declared endpoints with CSS `clamp()`. The result depends on the
chosen roots, intervals, content and browser behavior; inspect it across the
conditions the project supports. Viewport-relative units describe different
axes, but no unit alone establishes zoom behavior or WCAG conformance.

A project may coordinate spacing and type with shared parameters, including a
ratio or musical interval, when that supports its hierarchy. These are
construction choices. Interpolation is calculated per value and does not
preserve a geometric relationship at every intermediate width.
:::

### The Full Stack at a Glance {#the-full-stack-at-a-glance style="margin-top: var(--space-l);"}

  Layer          Tool                                 Purpose
  -------------- ------------------------------------ ------------------------------------------
  Typography     Contextual sizes and optional interpolation   Review hierarchy and rendered text
  Spacing        Contextual values and relationships   Shared or independent as useful
  Colour         Supplied values and rendered pairs   Check actual states and context
  Layout         Every Layout primitives              Composable, intrinsically responsive
  Alignment      CSS Subgrid                          Nested content alignment
  Adaptation     Container queries                    Component-level responsiveness
  Transitions    View Transitions API                 Perceptual continuity between pages
  Scroll         Scroll-driven animations             Optional decorative pacing
  Architecture   \@scope + nesting + \@layer          Clean cascade management
  Methodology    CUBE CSS                             Composition-first CSS architecture

------------------------------------------------------------------------

::: section-label
Historical Roots
:::

## Editorial Design Principles in CSS

::: prose
CSS Grid provides explicit row and column track layout. It can express
some editorial relationships while respecting fluid content. Print traditions
are useful design references, not proof that CSS reproduces their context or
that no earlier web technology arranged content in two dimensions.
:::

::: {.notes style="margin-top: var(--space-m);"}
### Historical Principles as Design Analogies

**Tschichold\'s asymmetric typography** (1928) can suggest
`grid-template-columns: 2fr 5fr 3fr` instead of the ubiquitous
`1fr 1fr 1fr`. His principle that \"form must be created out of
function\" parallels intrinsic sizing (`min-content`, `max-content`,
`fit-content()`).

**Müller-Brockmann\'s modular grids** (1981) --- rows AND columns
creating discrete cells --- can suggest CSS Grid choices: `grid-template-columns`
plus `grid-template-rows`, with subgrid for compound grids and named
areas for hierarchical structures.

**Vignelli\'s systematic restraint** --- limited typefaces, strict
grids, spacing as syntax --- can suggest a design token and custom
property approach as an analogy, not identical semantics. Jon Yablonski\'s Swiss in CSS project
(swissincss.com) recreates iconic Swiss Style posters entirely in CSS
with animation.
:::

::: {.prose style="margin-top: var(--space-l);"}
**Techniques that now work in pure CSS:** named grid areas for layout
declared in ASCII-art syntax; named grid lines for editorial column
structures with full-bleed breakouts; overlapping elements via same-cell
grid placement with z-index; font-metric-relative sizes using `cap` (not automatic baseline grids);
editorial pacing through alternating dense and airy sections;
`shape-outside` for text wrapping; `clip-path` for non-rectangular
crops; and `initial-letter` for drop caps.
:::

------------------------------------------------------------------------

::: section-label
Spatial Cognition
:::

## Wayfinding Science and Spatial Navigation

::: prose
For hub pages, portal sites, and any page whose primary job is to help
visitors find their way to deeper content, one useful design analogy comes from **Kevin Lynch\'s** urban planning research,
translated to digital spaces by Mark Foltz\'s MIT thesis \"Designing
Navigable Information Spaces.\" Lynch identified five elements of
legible environments: **paths, landmarks, regions, edges, and nodes**. A
homepage is a node; each major section is a region; the visual
transitions between them are edges.
:::

::: {.notes style="margin-top: var(--space-m);"}
### Key Principles from Spatial Cognition Research

**Gestalt grouping:** proximity, similarity and common region can cue
relationships; dissimilarity may help distinguish sections. These cues work
together in context, not as guaranteed laws of every interface. Partial imagery
may suggest more to explore; keep essential labels and access visible.

**Spatial memory:** stable boundaries and landmarks may help return visits.
Review the actual information architecture and tasks; broad/shallow and narrow/
deep hierarchies have trade-offs, not a universal efficiency ranking.

**Information scent** (Pirolli & Card, PARC): users are \"informavores\"
following scent trails. Each section must emit strong, differentiated
signals --- unambiguous labels, visual context, and spatial grouping
that keeps each area\'s cues coherent.

**Tufte\'s data-ink ratio:** maximise the proportion of visual elements
that communicate useful information. Support both overview scanning and
detailed reading. Use \"small multiples\" --- consistent templates
across repeated content types.
:::

### Museum Wayfinding: Reported Inspiration {#museum-wayfinding-the-strongest-design-analogue style="margin-top: var(--space-xl);"}

Museum websites face the same challenge as any multi-section portal:
making diverse content discoverable while creating a sense of
exploration. The six sketches below are reported inspiration, not audited
current site facts, award verification or evidence of engagement/wayfinding
benefit. Treat adaptations as proposals to test with the task.

::::::::::::::: museum-grid
:::: museum-item
::: museum-name
Victoria & Albert Museum
:::

Reported inspiration: colour used for selected content as a
\"breadcrumb trail.\" A \"city wayfinding\" approach treating the museum
as neighbourhoods, encouraging exploration of lesser-known areas.
::::

:::: museum-item
::: museum-name
Whitney Museum
:::

Reported inspiration: a typographic grid related to the logo as a container
for directional information. Whether it supports navigation needs actual review.
::::

:::: museum-item
::: museum-name
Nordiska Museet
:::

Reported inspiration: exhibition-specific palettes within a shared system,
with scroll-responsive text. No award or current implementation is verified here.
::::

:::: museum-item
::: museum-name
MIT Museum
:::

Reported inspiration: geometric “peephole” imagery. CSS `clip-path` could
adapt that motif decoratively; engagement benefit has not been established.
::::

:::: museum-item
::: museum-name
British Museum
:::

Reported inspiration: content-derived exhibition colours and hover accents.
A proposed adaptation still needs visible labels without hover.
::::

:::: museum-item
::: museum-name
Van Gogh Museum
:::

Reported inspiration: a horizontal exploration sequence. A contained CSS
Reel with optional scroll snapping is one proposed adaptation, not proof that
page-wide horizontal reading is suitable.
::::
:::::::::::::::

------------------------------------------------------------------------

::: section-label
The Approaches
:::

## Seven Concrete Approaches for Breaking Out

These seven practical approaches are design proposals informed by the reading
pointers above. Pick one for a content/navigation need, preserve familiar usable
controls, and test the result; distinctiveness does not justify broken controls.

:::: {.approach-card num="1"}
### Spatial Zoning Over Card Grids

::: prose
Treat the page as a **spatial map with distinct zones** --- each
occupying defined territory on the viewport with a unique visual
identity when useful. CSS Grid with named areas, project-chosen per-section colour
via custom properties, and typographic micro-variations per zone. This
follows Lynch\'s \"regions\" principle and leverages Gestalt common
region and proximity. The page becomes a landscape to survey, not a menu
to read. Use visible labels, semantic sections and landmarks alongside the
visual zoning; check source order and keyboard navigation.
:::
::::

:::: {.approach-card num="2"}
### Thematic Colour Differentiation with Content-Derived Palettes

::: prose
Inspired by the reported museum sketches, a project can give sections
content-derived colours through custom properties. Preserve supplied tokens;
OKLCH and `color-mix()` are optional candidate tools, not contrast guarantees.
Pair colour with labels and landmarks so it is never the sole wayfinding signal.
Check the actual pair/state and theme results.
:::
::::

:::: {.approach-card num="3"}
### View Transitions as Threshold Design

::: prose
A transition can suggest a threshold between related pages. For eligible
same-origin cross-document navigation, opt in on both pages; same-document
changes require `document.startViewTransition()` JavaScript. Use unique active
names, preserve ordinary navigation, and respect reduced motion. Test whether
continuity actually helps this task rather than claiming a research-proven gain.
:::
::::

:::: {.approach-card num="4"}
### Editorial Pacing Through Varied Grid Configurations

::: prose
Instead of uniform sections, alternate between dense and airy
compositions. Use subgrid to maintain a macro typographic grid while
varying column structures section by section. Asymmetric `fr` ratios
(Tschichold) create visual interest; `auto-fit`/`auto-fill` with
`minmax()` creates intrinsically responsive columns. Implement baseline
relationships using actual font metrics and line boxes; `cap` alone is no
baseline guarantee. Check reflow, long content and text-spacing overrides.

For an image-led article or collection, use the [image-composition method](image-composition.md)
to decide which visual relationships need a crop, which images should retain
their full proportions, and how captions, alternatives and links support the
reading path.
:::
::::

:::: {.approach-card num="5"}
### Decorative Pacing with Scroll-Driven Animation

::: prose
Use optional CSS scroll-driven decoration for pacing. `view()` progresses
across the visibility range; `animation-range` selects a portion, not a one-shot
trigger. Essential content must be visible at rest, with no feature support and
under `prefers-reduced-motion: reduce`. Keep a static alternative and test it.
Content-conditional `:has()` styling may help, while a query remains appropriate
when the task needs a discrete layout change. For a finite cue attached to a
user-selected destination rather than scroll progress, see the [purposeful
motion method](motion.md).
:::
::::

:::: {.approach-card num="6"}
### Partial Revelation Using Clip-Path

::: prose
The reported “peephole” motif can inspire decorative `clip-path` imagery.
Keep its linked label always exposed, with a visible keyboard focus indicator;
hover may decorate but cannot be the only route to essential text or controls.
Check touch and no-hover conditions. Do not clip essential content or infer an
engagement benefit from the effect.
:::
::::

:::: {.approach-card num="7"}
### Horizontal or Lateral Exploration

::: prose
A contained Reel may suit an image or related-item sequence. Provide
keyboard access, visible focus, a meaningful region label and source order;
scroll snapping is optional. Offer an ordinary reading alternative, such as
wrapping into a list at narrow widths. Exercise keyboard scrolling where the
Reel actually overflows. Do not force ordinary page prose into horizontal
scrolling, and do not equate overflow with a complete accessible carousel.
:::
::::

------------------------------------------------------------------------

::: section-label
Synthesis
:::

## The Deeper Point

::: epigraph
The grid is not the enemy. It\'s our launchpad. Every audacious layout
choice must be a stepping stone, not a stumbling block, on the user\'s
path.

--- KOTA
:::

::: prose
Breaking a familiar composition needs a reason grounded in content and use.
The grid remains an instrument: chosen constraints, labels, rhythm and variation
can help a particular page, while familiar patterns can support navigation.
The museum sketches and historical analogies offer possibilities, not audited
proof that a new layout will be more engaging.

Subgrid, asymmetric tracks, custom properties and container queries give the
practitioner expressive tools. Their value depends on the actual composition,
reading order, interaction, support and fallback. Scroll decoration must leave
the information available with reduced motion and without the enhancement.

The bounded CHI result motivates discussion of similarity; it does not prove a
template-harm mechanism or prescribe novelty. Build with intention, inspect the
result, and let the task decide when the familiar or the unusual serves people.
:::

------------------------------------------------------------------------

::: section-label
Appendix
:::

## Key References and Resources

::: ref-section
#### Academic Research

- CHI 2021: *Investigating the Homogenization of Web Design: A
  Mixed-Methods Approach* (ACM)
- Czerwinski & Larson (2002): *Cognition and the Web*, Microsoft
  Research
- Pirolli & Card: Information scent / information foraging theory, Xerox
  PARC
- NN/g: *Banner Blindness Revisited*; *Spatial Memory: Why It Matters
  for UX Design*
- ACM TOCHI: *High-cost banner blindness: Ads increase perceived
  workload*
- ACM Interactions, May--June 2025: *Where Is \'Spatial\' in Spatial
  Design?*
- Foltz, M.: *Designing Navigable Information Spaces* (MIT thesis)
:::

::: ref-section
#### Books and Primary Sources

- Tschichold, J. (1928): *The New Typography*
- Müller-Brockmann, J. (1981): *Grid Systems in Graphic Design*
- Vignelli, M. (2010): *The Vignelli Canon* (free PDF)
- Lynch, K. (1960): *The Image of the City*
- Tufte, E.: *The Visual Display of Quantitative Information*;
  *Envisioning Information*
:::

::: ref-section
#### Online Resources

- Every Layout: every-layout.dev (Pickering & Bell)
- Utopia: utopia.fyi (Gilyead & Mudford)
- CUBE CSS: cube.fyi (Andy Bell)
- Swiss in CSS: swissincss.com (Jon Yablonski)
- Jen Simmons\' Layout Lab: labs.jensimmons.com
- Josh Comeau: joshwcomeau.com/css/subgrid/
- Make Type Work (baseline grids): maketypework.com
- MDN: Subgrid, Container Queries, View Transitions, Scroll-Driven
  Animations
- Smashing Magazine: *Editorial Design Patterns with CSS Grid* (Rachel
  Andrew)
- Boris Müller: *Why Do All Websites Look the Same?* (Medium)
:::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::: footer
::::: footer-inner
::: meta
Breaking the Layout Monoculture · Research · March 2026 · CC0 Public
Domain
:::
:::::
::::::
