:::: hero

A Philosophy of Spatial Composition

# The Layout Philosophy

On fluid composition, spatial relationships and letting the browser help
while checking the result against actual content.

::: tag-row
[Intrinsic Design]{.tag} [Every Layout]{.tag} [Utopia]{.tag} [CUBE
CSS]{.tag} [CC0 --- Public Domain]{.tag} [March 2026]{.tag}
:::
::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: container
[]{#preamble}

::: section-label
Preamble
:::

## Why This Document Exists

::: prose
This guide focuses on how content and interface elements are arranged. Colour
and type choices come from the adopting project and the task at hand.

Most layout documentation tells you which CSS properties to use. This
document does something different. It articulates a **philosophy of
spatial composition** that can generate an infinite variety of layouts
from a small set of principles. Intrinsic and fluid methods can suit many
layouts; use a breakpoint when content or behavior needs a discrete change.

The philosophy synthesises two bodies of work that represent the current
state of the art in CSS layout thinking: **Every Layout** by Heydon
Pickering and Andy Bell, which defines composable layout primitives; and
**Utopia** by James Gilyead and Trys Mudford, which defines fluid
responsive mathematics. It also draws from the Arts & Crafts tradition, Müller-Brockmann’s grid
systems and Vignelli’s systematic restraint.

The goal is not to create a new set of constraints in which to bind
ourselves. It is to provide the knowledge, the vocabulary, and the tools
with which anyone can build the layout that *their* project needs --- a
layout that is beautiful, functional, and makes people want to stay and
explore. And perhaps even inspires them to build their own.
:::

::: {.epigraph style="margin-top: var(--space-xs);"}
Think of yourself as the browser\'s mentor, rather than its
micro-manager.

--- Heydon Pickering & Andy Bell, Every Layout
:::

------------------------------------------------------------------------

[]{#part-i}

::: section-label
Part I
:::

## The Intellectual Foundations

Two independent projects, arriving at the same truth from different
directions. Understanding where they converge --- and where each one
picks up where the other leaves off --- is the key to the whole system.

### Every Layout: The Grammar of Spatial Relationships

::: prose
Every Layout begins with a radical premise: **the web is already
responsive**. Before any CSS is written, browsers know how to wrap text,
scroll content, and fit boxes to their containers. The vast majority of
layout problems arise not from CSS\'s limitations but from designers
fighting its built-in algorithms --- applying fixed widths where
flexible ones would do, using pixel values where proportional ones would
adapt, writing media queries to undo the damage of earlier rigid
declarations.

The project\'s six \"Rudiment\" chapters build up a complete
epistemology of CSS layout from first principles. It starts with
**Boxes** --- the insight that everything on the web occupies a
rectangular region, and that the dimensions of that region should be
*derived from content and context*, not prescribed. The crucial
technical point is the difference between `width: 100%` (which
prescribes a size and then adds padding on top of it) and `width: auto`
(which lets the box fit its context naturally). This is not pedantry. It
is the atomic distinction between fighting the browser and collaborating
with it.

From Boxes, Every Layout moves to **Composition** --- the explicit
application of the Gang of Four software engineering principle
\"composition over inheritance\" to CSS layout. Where a typical approach
might create a bespoke `.dialog` class with dedicated styles for header,
body, and footer, compositional thinking decomposes the same dialog into
a Stack (for vertical spacing), a Box (for padding), a Cluster (for the
button row), and a Center (for the content width). The dialog is not a
thing to be styled; it is a *composition* of simpler things, each with a
single, reusable responsibility.

CSS units describe different relationships. `ch` is based on the advance
measure of the zero glyph in the active font; a `ch` measure is a starting
point to review against actual text, language, typeface and reading conditions.
`rem` follows the root font size, and `em` follows the relevant font size.
Pixels may suit values tied to device or asset dimensions. Choose units for the
behavior needed, then inspect the rendered result and user settings.

Global styles, compositional classes and utilities are one way to organize
a stylesheet. Choose layers and selector scope to fit the project; broad rules
need review against every content type and component they affect. The cascade
can express intentional defaults and exceptions without requiring a fixed
number of layers.

The **Modular scale** chapter offers one way to generate proportional
values: `size(n) = base × r^n`. For an increasing perfect-fourth scale,
`r = 4/3`; `1.333` is a displayed approximation, not that exact ratio.
With a `1rem` base, steps 0–3 round to `1.000rem`, `1.333rem`,
`1.778rem`, and `2.370rem` at three decimal places. Compute with the
selected ratio before rounding the displayed result. These proportions
are a construction choice; arithmetic alone does not establish
perceptual harmony, readability or a requirement that all spacing be geometric.

Finally, **Axioms** introduces designing by constraint rather than by artifact.
A project may declare an invariant, such as a prose measure or minimum target
size, where it suits the content and task. Scope the rule to the elements it
serves, and inspect its effects rather than assuming one declaration is sound
everywhere. CSS generates rendered results that still need review.
:::

::: {.epigraph style="margin-top: var(--space-xs);"}
Instead of telling browsers what to do, we allow browsers to make their
own calculations, and draw their own conclusions, to best suit the user,
their screen, and device.

--- Every Layout, \"Boxes\"
:::

### Utopia: The Mathematics of Continuous Adaptation

::: prose
Utopia describes one way to interpolate between values chosen for two reference
conditions. Select the roots and interval for the adopting project, then
inspect each result with representative content. Each value is interpolated
separately; intermediate steps do not generally form the same geometric
progression as the endpoints.

Spacing may share parameters with type, or use independent values. Fluid space
pairs and grids are options for cases where their behavior helps; they do not
require every margin, gutter and component size to derive from one base or
ratio. Check wrapping and relationships across the intended container range.

:::

::: {.epigraph style="margin-top: var(--space-xs);"}
Instead of tightening our grip by loading up on breakpoints, we can let
go, embracing the ebb and flow with a more fluid and systematic approach
to our design foundations.

--- Utopia homepage
:::

### Where They Meet: The Interface Between Composition and Scale

::: prose
Every Layout and Utopia address different concerns that can work together.
Compositional patterns need values for gaps, gutters and padding; a project can
supply fixed, fluid or independently chosen values. Utopia offers methods for
interpolating selected values across a declared range. It is one possible
source, not a dependency for the primitives.

The shared philosophical commitments run deeper than the technical
interface. Both projects advocate: letting the browser resolve layout
rather than prescribing it; using constraints and tolerances rather than
fixed values; choosing CSS units that encode meaningful relationships;
treating the web as a fluid medium rather than a collection of fixed
canvases. Both projects were created by practitioners who had grown
tired of fighting CSS and decided to *listen to it instead*.

This is the foundation upon which our layout philosophy is built.
:::

------------------------------------------------------------------------

[]{#part-ii}

::: section-label
Part II
:::

## Principles for Fluid Composition

These principles draw on Every Layout\'s compositional thinking and Utopia\'s
fluid mathematics. They are prompts for judgment. Test choices against the
content and constraints; no principle generates a correct decision
automatically.

:::: {.principle-card numeral="I"}
### Start with Constraints

::: prose
Express the relationships and constraints the task needs, then choose
CSS values that support them. A project may set a maximum measure or
minimum target size when it serves the content or interaction. Intrinsic
sizing, `min-`, `max-`, `clamp()`, `auto`, `flex-basis` and fixed values
each have uses; select them for the required behavior.

The browser evaluates layout from its available space, used fonts and
CSS rules. It does not know the task or guarantee a good composition.
Check the result with representative content, user font preferences,
zoom and relevant viewport or container conditions. Constraints can
support adaptable design; they do not make good outcomes inevitable.

**The test:** inspect whether intrinsic behavior preserves the task.
Add a media or container query when content, interaction, user needs or
output conditions call for a discrete change. State the reason and test
the resulting modes, rather than treating query removal as a universal test.
:::
::::

:::: {.principle-card numeral="II"}
### Compose Reusable Relationships

::: prose
Use reusable spatial patterns where they make relationships clearer:
Stacks for vertical flow, Boxes for padding, Centers for inline-size
constraints, Clusters for horizontal groups, Sidebars for main-plus-aside
patterns, Switchers for column-to-stack arrangements, Covers for centered
content, Grids for repeating patterns, Frames for aspect ratios and Reels
for horizontal sequences. This vocabulary supports composition; it is
not a proof that every task must fit these patterns.

A card might be a Box containing a Stack; a page header might combine
Cover, Center and Stack. These examples describe spatial arrangement.
Choose appropriate markup and interaction behavior separately. Shared
patterns can support consistency, but token choices, exceptions and
interactions still need review. Composition is a design method, not a
ban on CSS inheritance or justified additional rules.

**The test:** describe the relationships that matter to the task and
check whether the chosen patterns express them. If the vocabulary is
insufficient, adapt or extend it with a reason; an unfamiliar pattern
does not by itself show that the designer used the wrong abstraction.
:::
::::

:::: {.principle-card numeral="III"}
### Let Dimensions Flow From Content

::: prose
Let content inform dimensions where the task permits. A paragraph may
use a font-relative measure such as `ch`, checked with the used fonts
and scripts; the unit does not count arbitrary characters. Let section
block-size follow content where appropriate, and choose gaps for grouping
and interaction. Fixed, fluid and shared spacing can each serve a task.
A grid may use `auto-fit` and `minmax()` when their track-sizing behavior
fits the content and available space; a fixed column count may also be justified.

A preferred or fixed size does not show that its author knows all future
content or viewport sizes. Depending on sizing and overflow rules,
content may exceed the box, clip or scroll. Review the used size and
content access. Explicit heights, pixel widths and column counts can
serve requirements when their consequences are checked; intrinsic sizing
and container queries are alternatives, not a ban on explicit values.

**The test:** expand real content, narrow the available space and check
the combined case. Inspect reflow, overflow, grouping and task operation,
including access to essential labels, controls and meaningful wide data.
These are diagnostics for the tested conditions, not proof across all
content, users or browsers. Record exceptions and untested cases.
:::
::::

:::: {.principle-card numeral="IV"}
### Use Ratios Where They Help

::: prose
Ratios can help coordinate sizes when proportional steps suit the task. A
geometric scale is one available construction, not a requirement for every
type or spacing value. Fluid interpolation evaluates each value between its
own endpoints; ratios at an intermediate width are not generally preserved.

Choose roots, ratios, steps, units and intervals for the actual project. A
value that departs from a scale may be justified by content, interaction,
script coverage or optical fit. Check rendered hierarchy and wrapping rather
than treating a formula as proof of a correct composition.

:::
::::

:::: {.principle-card numeral="V"}
### Encode Axioms, Not Artefacts

::: prose
A broad CSS rule can encode a real project invariant when its scope is clear.
The browser applies the rule literally; it does not decide whether the result
fits every script, content type, viewport or user setting. Inspect it against
representative content, then scope or override it where needed.

:::
::::

:::: {.principle-card numeral="VI"}
### Unify Type, Space, and Grid

::: prose
Type, spacing and grids can share parameters when that simplifies a project,
but need not use one mathematical base. A spacing value or gutter may have its
own constraints. Compare proportions in context and keep exceptions that better
serve the content or task.

:::
::::

:::: {.principle-card numeral="VII"}
### Design Systems, Not Pages

::: prose
A design system can combine principles with reusable parts. Spatial primitives
and fluid values can help describe how a page adapts, but the browser does not
supply a finished design or guarantee correctness. Check choices with the
project’s actual content, users and supported conditions.

William Morris’s repeating patterns are one historical example of combining
constraints with variation. A layout method should help people respond to their
own content and tasks, not make every result belong to an inherited visual
family.

:::
::::

------------------------------------------------------------------------

[]{#part-iii}

::: section-label
Part III
:::

## The Architecture in Practice

How the seven precepts materialise as CSS. This is the technical
layer --- the specific primitives, tokens, and patterns that implement
the philosophy.

### The Fluid Foundation: A Scoped Arithmetic Illustration

::: prose
This named exercise uses an accepted diagnostic configuration: minimum and
maximum bases of `1rem` and `1.125rem`, endpoint ratios of `1.2` and `1.25`,
and an interval of `20rem`–`80rem`. These are inputs to an arithmetic-only
illustration, not recommended type sizes, roles, spacing values or defaults.
The expression shows step zero only and assigns no font or accessibility
outcome; negative steps are arithmetic probes, not functional-text
recommendations.
:::

```css
--example-step-0: clamp(1.000000rem, calc(0.958333rem + 0.208333vi), 1.125000rem);
```

At a 16px root the 20rem–80rem interval is nominally 320–1280 CSS pixels. At a
20px root it moves to 400–1600 CSS pixels. The interval is root-relative;
treating it as fixed pixel endpoints changes the configuration. Interpolation
is linear per step, not generally a geometric progression at intermediate
widths. A calculation does not establish readability or zoom behavior; inspect
the actual interface.

### The Compositional Layer: Every Layout Primitives

::: prose
Layouts can be composed from a vocabulary of spatial primitives. Each primitive
has a single responsibility and can be implemented as a CSS class. Supply values
from the adopting project; fixed, fluid and independently chosen spacing are all
available. Utopia is one possible source of values, not a prerequisite.
:::

::::::::::::::::::::::::::::::::: concept-grid
::::::: concept-card
::::: {.card-head}
::: {.card-label}
Vertical Flow
:::

::: card-title
The Stack
:::
:::::

::: {.card-body}
**Responsibility:** vertical spacing between adjacent sibling elements.
The most frequently used primitive --- nearly every block of content
lives inside a Stack.

**Mechanism:** `display: flex; flex-direction: column;` with `gap` set
to a Utopia space token. The owl selector (`* + *`) variant is also
common.

**Key parameter:** `--space` (which Utopia token to use for the gap).
:::
:::::::

::::::: concept-card
::::: {.card-head}
::: {.card-label}
Padding & Containment
:::

::: {.card-title}
The Box
:::
:::::

::: {.card-body}
**Responsibility:** inset padding around content. A Box is any element
that needs uniform internal spacing.

**Mechanism:** `padding` set to a Utopia space token, with optional
`border` and `background`.

**Key parameter:** `--padding` (which Utopia token, typically a space
pair like `--space-s-m` for fluid component padding).
:::
:::::::

::::::: concept-card
::::: {.card-head}
::: {.card-label}
Width Constraint
:::

::: card-title
The Center
:::
:::::

::: {.card-body}
**Responsibility:** constraining content to a maximum width and centring
it horizontally. The measure axiom is typically enforced here.

**Mechanism:** `max-inline-size` with `margin-inline: auto`. Uses
`box-sizing: content-box` so that padding does not reduce the content
area.

**Key parameter:** `--measure`, chosen for the actual typeface, language, text
and reading conditions; review the rendered line length.
:::
:::::::

::::::: concept-card
::::: {.card-head}
::: {.card-label}
Horizontal Grouping
:::

::: card-title
The Cluster
:::
:::::

::: {.card-body}
**Responsibility:** grouping items horizontally with wrapping. Tags,
button rows, navigation links, metadata.

**Mechanism:** `display: flex; flex-wrap: wrap; gap` set to a Utopia
space token. Items wrap naturally when space runs out.

**Key parameter:** `--space` and `justify-content` for alignment.
:::
:::::::

::::::: concept-card
::::: {.card-head}
::: {.card-label}
Main + Aside
:::

::: card-title
The Sidebar
:::
:::::

::: {.card-body}
**Responsibility:** a two-element layout where one element has a
preferred width (the sidebar) and the other takes the remaining space.
Stacks vertically when the main element would become too narrow.

**Mechanism:** Flexbox with `flex-basis` on the sidebar and `flex-grow`
on the main content. A `clamp()`-based variant can avoid a media query for some uses.

**Key parameter:** `--sidebar-width` and `--content-min` (minimum main
content percentage before stacking).
:::
:::::::

::::::: concept-card
::::: {.card-head}
::: {.card-label}
Responsive Columns
:::

::: {.card-title style="font-weight: 500; font-size: var(--step-1);"}
The Switcher
:::
:::::

::: {.card-body}
**Responsibility:** switching between multi-column and single-column layouts
based on available space. Intrinsic wrapping may suit the task; a breakpoint
may be clearer when behavior changes discretely.

**Mechanism:** `flex-wrap: wrap` with a calculated `flex-basis` that
causes items to wrap at the threshold width. The threshold is defined by
the content, not the viewport.

**Key parameter:** `--threshold` (the container width at which items
stack).
:::
:::::::
:::::::::::::::::::::::::::::::::

:::: notes
#### The Remaining Primitives

::: prose
The **Cover** centres one child vertically within a minimum-height
container (hero sections, full-viewport panels). The **Grid** creates
repeating equal-width columns using `auto-fit` and `minmax()`, requiring
no column count declaration --- the number of columns is derived from
the minimum item width and the available space. The **Frame** locks
media to an aspect ratio. The **Reel** creates horizontal overflow
scrolling (carousels, image strips). The **Imposter** positions an
element outside normal flow (modals, tooltips). The **Icon** sizes an
inline SVG relative to its adjacent text. The **Container** provides the
outermost width constraint for page content.

Together, these thirteen primitives offer reusable ways to describe spatial
relationships. They can help compose cards, headers, navigation, forms and
footers; use other structures when they better fit the content.
:::
::::

### The Unified Stack

::: prose
A project may combine fluid values with compositional primitives. Keep type,
spacing, composition, methodology and progressive enhancement as useful areas
of concern; their implementation and relationship depend on the project.
:::

:::::::::::::::::: layer-stack
::::: {.layer}
::: {.layer-name}
Typography
:::

::: layer-desc
Choose type sizes and any fluid interpolation for the actual hierarchy;
review rendered text and use discrete changes where the content calls for them.
:::
:::::

::::: {.layer}
::: {.layer-name}
Spacing
:::

::: layer-desc
Choose spacing values for their roles and relationships. Shared parameters,
fluid pairs and independent values are all available constructions.
:::
:::::

::::: {.layer}
::: {.layer-name}
Composition
:::

::: layer-desc
Every Layout primitives (Stack, Box, Center, Cluster, Sidebar, Switcher,
Cover, Grid, Frame, Reel, Imposter, Icon, Container). Uses values supplied
by the adopting project.
:::
:::::

::::: {.layer}
::: {.layer-name}
Methodology
:::

::: layer-desc
CUBE CSS (Composition, Utility, Block, Exception). The organisational
principle that structures how primitives, utilities, and
component-specific styles interact.
:::
:::::

::::: {.layer}
::: {.layer-name}
Enhancement
:::

::: layer-desc
Modern CSS features (container queries, subgrid, `:has()`, scroll-driven
animations, view transitions) layered progressively on top of the
intrinsic base.
:::
:::::
::::::::::::::::::

------------------------------------------------------------------------

[]{#part-iv}

::: section-label
Part IV
:::

## The Deeper Current: Layout as Craft

Why this philosophy belongs to a tradition older than the web itself.

::: prose
William Morris, the founder of the Arts & Crafts movement, did not rail
against machines because he hated technology. He railed against machines
that produced *thoughtless work* --- objects that were identical,
characterless, and disconnected from the people who made or used them.
His response was not to reject industrialisation but to insist that even
industrially produced objects should be made with care, intention, and
respect for the craft.

The web design monoculture is our version of Morris\'s factory.
Bootstrap, WordPress themes, and Tailwind UI templates produce layouts
that are functional but characterless --- the metal folding chairs of
the digital world. The CHI 2021 research confirms this: web design has
measurably homogenised by 30% over sixteen years. Every SaaS landing
page follows the same hero-features-testimonials-CTA-footer pattern.
Users have learned to filter it out.

Our response mirrors Morris\'s: not to reject the tools, but to insist
on *craft within the tools*. Every Layout and Utopia are not
anti-framework; they are the intellectual infrastructure for building
layouts that *deserve to exist*. A layout composed from suitable
primitives and values is a considered response to specific content in a
specific context. Inspect it at the widths and settings the project supports.

The Arts & Crafts movement believed that beautiful, well-made objects
had moral force --- that they improved the lives of both their makers
and their users. We believe something similar about layout. A site whose
spatial relationships support their content, whose typography remains
usable across supported widths, and whose composition responds to its task
can be hospitable. It invites people in. It respects their time and their
attention. And it demonstrates, by example, that the web can be better
than it currently is.

This document is released under CC0 because we believe this knowledge
should be common property --- not locked behind a paywall or a
proprietary framework. The point is that people should be able to make layouts for their own
content, with care and respect for the medium. Mission chairs, not metal folding chairs.
But not *only* Mission chairs --- whatever chair *you* need, built
beautifully.
:::

:::: epigraph
> Have nothing in your houses that you do not know to be useful, or
> believe to be beautiful.

::: attr
--- William Morris, 1880
:::
::::

------------------------------------------------------------------------

[]{#part-v}

::: section-label
Part V
:::

## Applying the Philosophy: A Worked Example

To demonstrate how the principles can be applied, consider a book detail
page composed from the adopting project’s content and available components.

::: prose
Imagine a page displaying a single book: cover image, title, author,
description, publication details, and related titles. A template
approach would design this page once, pixel-perfect at 1440px, then add
breakpoints at 1024px, 768px, and 375px to adapt it. That is four
designs, four sets of spacing values, four column configurations, and a
maintenance burden that grows with every design change.

The intrinsic approach composes the page from primitives and lets the
mathematics handle responsiveness.
:::

::: code-block
[/\* Page composition illustration; evaluate queries from observed needs
\*/]{.comment} [/\* Page: Container → Stack \*/]{.comment} [.page]{.sel}
{ [/\* Container: max-width, centred \*/]{.comment}
[max-inline-size]{.prop}: [1200px]{.val}; [margin-inline]{.prop}:
[auto]{.val}; [padding-inline]{.prop}: [var(\--space-s-l)]{.val}; [/\*
Fluid side padding \*/]{.comment} } [/\* Hero: Sidebar (cover image +
title info) \*/]{.comment} [.book-hero]{.sel} { [/\* Sidebar primitive
\*/]{.comment} [display]{.prop}: [flex]{.val}; [flex-wrap]{.prop}:
[wrap]{.val}; [gap]{.prop}: [var(\--space-l-xl)]{.val}; [/\* Steep fluid
gap \*/]{.comment} } [.book-hero \> .cover]{.sel} { [/\* Frame:
aspect-ratio locked \*/]{.comment} [flex-basis]{.prop}: [clamp(200px,
30%, 400px)]{.val}; [flex-grow]{.prop}: [0]{.val}; } [.book-hero \>
.info]{.sel} { [/\* Stack: title, author, metadata \*/]{.comment}
[flex-basis]{.prop}: [0]{.val}; [flex-grow]{.prop}: [999]{.val};
[min-inline-size]{.prop}: [55%]{.val}; [/\* Stacks when too narrow
\*/]{.comment} } [/\* Description: Center (measure-constrained prose)
\*/]{.comment} [.book-description]{.sel} { [max-inline-size]{.prop}:
[var(\--prose-measure)]{.val}; [/\* supplied project value; review with actual text \*/]{.comment} } [/\* Related
titles: Grid (intrinsic column count) \*/]{.comment}
[.related-grid]{.sel} { [display]{.prop}: [grid]{.val};
[grid-template-columns]{.prop}: [repeat(auto-fit, minmax(min(100%,
180px), 1fr))]{.val}; [gap]{.prop}: [var(\--space-s-m)]{.val}; }
:::

::: prose
This stylesheet is an illustration to review with representative content and
container sizes. Intrinsic wrapping can handle some width changes; evaluate any
queries against observed behavior. The measure, card width, spacing and type
values are examples whose suitability depends on the adopting project. The
composition uses Container, Sidebar, Center and Grid relationships; adapt or
replace them when the content calls for it.
:::

------------------------------------------------------------------------

[]{#part-vi}

::: section-label
Part VI
:::

## Sources, Lineage, and Further Reading

This philosophy stands on the shoulders of extraordinary work. Here is
where to go deeper.

  Source                   What It Provides                                                                                                                                                                                                                                                                                                                                                                                                                              Where to Find It
  ------------------------ --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------
  Every Layout             The 13 compositional primitives, the Rudiments philosophy (Boxes, Composition, Units, Global/Local, Modular Scale, Axioms), and the EPUB/website.                                                                                                                                                                                                                                                                                             every-layout.dev --- paid, partially free
  Utopia                   Fluid type and space calculators, the philosophical blog posts, utopia-core (JS/TS), utopia-core-scss, postcss-utopia, Figma plugins.                                                                                                                                                                                                                                                                                                         utopia.fyi --- free tools, free blog
  CUBE CSS                 The organisational methodology (Composition, Utility, Block, Exception) that structures how primitives and utilities interact in a stylesheet.                                                                                                                                                                                                                                                                                                cube.fyi --- free
  Vignelli Canon           Systematic restraint, syntactical consistency, the discipline of working within a chosen set of proportions.                                                                                                                                                                                                                                                                                                                                  Free PDF from RIT
  Müller-Brockmann         Mathematical grid construction, compound grids, the Swiss typographic tradition that anticipated CSS Grid by 40 years.                                                                                                                                                                                                                                                                                                                        Grid Systems in Graphic Design
  Bringhurst               Typographic measure, proportional systems, the musical-interval ratios that Tim Brown brought into web typography.                                                                                                                                                                                                                                                                                                                            Elements of Typographic Style, v4.0
  Refactoring UI           Tactical, pattern-oriented design guidance for developers. Constrained spacing scales, the \"design in greyscale first\" heuristic.                                                                                                                                                                                                                                                                                                           refactoringui.com
  Dao of Web Design        John Allsopp\'s 2000 essay arguing that web designers must relinquish control to the medium --- the philosophical ancestor of everything in this document.                                                                                                                                                                                                                                                                                    alistapart.com/article/dao/
  Kaplan (ed.)             The definitive international survey of the Arts & Crafts movement. 260 objects from 13 countries --- Britain, Ireland, the US, France, Belgium, Germany, Austria, Hungary, Scandinavia, Finland --- covering furniture, ceramics, metalwork, textiles, and works on paper. Country-by-country essays on how each nation adapted the Ruskin/Morris ideals to its own social context. The philosophical backbone of Part IV of this document.   *The Arts and Crafts Movement in Europe and America: Design for the Modern World, 1880--1920* (Thames & Hudson, 2004). 327pp, 360 illustrations.
  V&A / Greenhalgh (ed.)   The V&A\'s landmark exhibition catalogue, extending the story beyond Europe and America to include Japan and the movement\'s later manifestations. Covers architecture, garden design, photography, painting, and sculpture alongside the decorative arts. Leading scholars explore regional, national, and international variants. The most comprehensive single volume on the global scope of the movement.                                 *International Arts and Crafts* (V&A Publishing, 2005). Lavishly illustrated.

:::: {.accent-block .books}
#### For the mathematically inclined

::: prose
With ordered finite bounds, `clamp(min, preferred, max)` limits its
preferred calculation to those bounds. When that calculation is linear
in the selected inline extent, the result changes linearly only inside
its unsaturated interval and is fixed at a bound outside it; there is
no asymptotic approach.

For positive endpoint bases `a`, `b`, positive ratios `r`, `q`, integer
step `n`, and a shared clamped parameter `t` in `[0,1]`, each interpolated
step is `s_n = (1-t)a r^n + t b q^n`. At an interior parameter (`0<t<1`)
this is geometric across steps only when `r = q`; either endpoint retains
its own geometric sequence. Each step's change depends on its own endpoint
difference, so higher steps need not grow faster.

`vi` is a logical inline viewport unit. It does not alone establish
browser text enlargement, reflow or WCAG conformance. Declare the roots
and interval, then test the actual interface and user settings.
:::
::::

:::: {.accent-block .art}
#### For the philosophically inclined

::: prose
Every Layout\'s concept of \"axioms\" derives from Euclid\'s
postulates --- simple, irreducible rules from which complex geometries
follow. The Utopian idea of \"declarative design\" maps to the same
distinction computer science draws between imperative and declarative
programming: specify *what* you want, not *how* to achieve it. The Arts
& Crafts connection runs through Morris\'s pattern mathematics: the 17
wallpaper symmetry groups are themselves a kind of generative design
system, producing infinite variation from finite rules. The throughline
is always the same: good design is not about making beautiful things; it
is about making systems that *produce* beautiful things.
:::
::::

:::: {.accent-block .home}
#### For the practically inclined

::: prose
Start with supplied components and content. Try intrinsic sizing and fluid
values where they help. Add a container or viewport query when content, task or
interaction needs a discrete change. Choose measures and spacing for their
actual roles, then check supported widths and relevant text settings.

:::
::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::: footer
::::: footer-inner
::: meta
Layout Philosophy · March 2026 · CC0 Public Domain
:::
:::::
::::::
