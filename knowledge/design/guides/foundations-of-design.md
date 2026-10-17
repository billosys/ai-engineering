:::: hero

Colour theory, typography, & layout-composition

# Foundational Research for a Visual Design Knowledge Base

The field of visual design possesses formal structure, empirical
grounding, and mathematical depth fully comparable to graduate-level
mathematics or post-doctoral music theory. This research validates a
domain taxonomy, maps 55 competency questions across three tiers,
analyses 30+ foundational sources, and documents the mathematical
underpinnings that will give a technically sophisticated reader
first-principles access to the discipline.

::: tag-row
[Research]{.tag} [Domain Taxonomy]{.tag} [Competency Questions]{.tag}
[Source Analysis]{.tag}
:::
::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::: container
::: section-label
Section 1
:::

## The Taxonomy Is Strong but Needs a Foundational Layer and Three Additions

::: prose
The preliminary nine-category taxonomy maps well to how foundational
design education is structured at RISD, Parsons, and CMU. **Colour
theory, typography, and layout-composition receive universal standalone
treatment** across every program and textbook examined. Visual
perception, interaction design, and accessibility have strong support.
Information architecture, design systems, and brand identity have
moderate support but sit at different abstraction levels.
:::

::: finding-card
#### Critical Gap: Visual Elements

Every design foundations textbook --- Lupton & Phillips\'s *Graphic
Design: The New Basics*, Lauer & Pentak\'s *Design Basics* --- opens
with point, line, plane, shape, texture, and value. RISD teaches
\"form\" as a foundational principle co-equal with colour and
typography. These atomic building blocks are more fundamental than any
of the nine categories and must be added as a layer-zero category.
:::

::: notes
#### Three Categories to Add

**Motion design** --- RISD and Parsons both offer dedicated tracks;
Material Design 3, Carbon, Polaris, and Apple HIG all document motion as
a standalone visual style. Animation principles (easing, timing,
choreography) are distinct from interaction design.

**Data visualization** --- Carnegie Mellon offers it as a standalone
course; Carbon and Polaris document it as a top-level section. It
doesn\'t fit colour, typography, or layout alone.

**Imagery** --- RISD lists \"image\" as co-equal with colour and type.
Photography direction, iconography, and illustration selection are
fundamental design decisions with no current home in the taxonomy.
:::

::: {.prose style="margin-top: var(--space-m);"}
**Orthogonality issues to address.** An ontology engineer would flag
three concerns. First, visual-perception and layout-composition overlap
significantly --- gestalt principles *are* the perceptual laws governing
layout. Keep them separate but cross-reference heavily. Second,
accessibility operates as a cross-cutting quality attribute touching
every other category, not a peer domain. Model it as a facet dimension
or ensure each category has accessibility subconcepts. Third,
brand-identity sits at a higher abstraction level --- it\'s an
application context drawing on colour, typography, and design systems
rather than a knowledge domain of equal granularity. Consider renaming
it \"visual-identity-systems.\"

**Cross-cutting principles that span categories.** Hierarchy, contrast,
rhythm/repetition, scale/proportion, and balance appear in every
textbook and design system but belong to no single category. The
knowledge base should model these as cross-cutting concept cards that
reference multiple domains, similar to how mathematical theorems
reference multiple branches.
:::

### How Design Systems Organize Their Documentation {#how-design-systems-organize-their-documentation style="margin-top: var(--space-xl);"}

Analysis of five major systems reveals a convergent six-layer
architecture:

::: {style="overflow-x: auto;"}
  Layer           Material Design 3   Carbon              Polaris              Primer        Apple HIG
  --------------- ------------------- ------------------- -------------------- ------------- ------------------------
  Principles      Foundations         Guidelines          Foundations          Foundations   Foundations
  Visual styles   Styles              Elements            Design               Primitives    Foundations
  Tokens          Design tokens       Tokens (embedded)   Tokens (top-level)   Primitives    Implicit
  Components      Components          Components          Components           Components    Components
  Patterns        ---                 Patterns            Patterns             Guides        Patterns
  Platform        Develop             Developing          ---                  ---           Platforms/Technologies
:::

::: {.prose style="margin-top: var(--space-s);"}
**Universal visual style categories** across all five systems: colour,
typography, spacing/layout, motion, icons, and elevation/depth.
[The DTCG 2025.10 Format Module](https://www.designtokens.org/tr/2025.10/format/)
is a stable Final Community Group Report intended for implementation, not a
W3C Standard or Standards Track document. It specifies a JSON interchange
format with value types: `color`, `dimension`, `fontFamily`, `fontWeight`,
`duration`, `cubicBezier`, and `number`; composite types include `strokeStyle`,
`border`, `transition`, `shadow`, `gradient`, and `typography`. These type
categories describe value structure, not a required token-layer architecture.
:::

------------------------------------------------------------------------

::: section-label
Section 2
:::

## Fifty-Five Competency Questions Bridge Perception and Implementation

::: prose
Research into design education assessment, professional certification
criteria, senior designer interview processes, and developer knowledge
gaps produced 55 competency questions across five types and three tiers.
The questions specifically bridge \"I can see it\" and \"I can build
it\" --- connecting visual perception to systematic implementation.
:::

:::: tier-section
[Foundational Tier]{.tier-label .tier-foundational}

### Core Vocabulary and First Principles

::: prose
**Definitional.** What is visual hierarchy, and what visual properties
(size, colour, contrast, weight, spacing) establish it? What
distinguishes a spacing system from arbitrary padding values --- what
problem does constraint solve? What are the three components of HSL, and
why is it more useful than hex for palette construction?

**Relational.** How do font weight and colour work *together* with font
size to create typographic hierarchy --- why is size alone insufficient?
How does the relationship between inter-group and intra-group spacing
communicate which elements belong together?

**Diagnostic.** A card layout uses 16px padding inside cards, 16px
between cards, and 16px between card title and body. Why does everything
feel flat? *Answer: identical spacing erases the distinction between
containment and separation; intra-card spacing should be tighter than
inter-card spacing.*
:::
::::

:::: tier-section
[Intermediate Tier]{.tier-label .tier-intermediate}

### Applied Knowledge and Pattern Recognition

::: prose
**Procedural.** Given a data-rich card (title, status, three metrics,
timestamp, action button), how do you assign visual hierarchy: what gets
the most weight, what gets de-emphasised, and why? How do you ensure a
coloured status badge is accessible without relying solely on colour?

**Diagnostic.** A dashboard uses teal header, red errors, green success,
blue links, yellow warnings, purple badges. It looks like a \"clown
car.\" What principle was violated? *Answer: no constrained palette.
Define one primary, neutrals, and semantic colours with consistent
shades. Reduce total unique hues.*
:::
::::

:::: tier-section
[Advanced Tier]{.tier-label .tier-advanced}

### Systematic Thinking and Cross-Domain Integration

::: prose
**Relational.** How does a well-structured design token system map onto
CSS custom properties? What is the isomorphism between design decisions
and code architecture? How does cognitive load theory (intrinsic,
extraneous, germane) relate to progressive disclosure and visual
hierarchy?

**Diagnostic.** An admin panel organises UI by database tables --- Users
page, Orders page, Products page, each showing all columns. Diagnose the
fundamental mistake. *Answer: UI mirrors the data model instead of user
tasks. Reorganise around goals: \"Process orders,\" \"Handle returns.\"
Show relevant data from multiple tables on task-focused views.*
:::
::::

::: {.finding-card style="margin-top: var(--space-m);"}
#### The Six Most Consequential Developer Design Mistakes

Validated across multiple sources including Refactoring UI: (1) no
visual hierarchy --- everything has equal weight; (2) inconsistent
spacing --- no system; (3) unconstrained colour --- too many unrelated
hues; (4) no type scale --- random font sizes; (5) data-model-driven
information architecture instead of task-driven; (6) equal-weight
buttons --- no primary/secondary distinction. These six account for the
majority of the perceived quality gap between developer-built and
designer-built interfaces.
:::

------------------------------------------------------------------------

::: section-label
Section 3
:::

## Source Analysis Reveals a Clear Intellectual Lineage

The sources form a pipeline: perception science (Arnheim, Ware, gestalt
research) → design principles (Norman, Nielsen, Laws of UX) → practical
patterns (Krug, Refactoring UI) → system architecture (Frost, Curtis) →
CSS implementation (Comeau, Eckles, Every Layout, Utopia).

### Colour Theory: From Albers\'s Relativity to OKLCH\'s Perceptual Uniformity

::: prose
**Josef Albers, *Interaction of Color* (1963).** The canonical colour
education text. Central thesis: \"In visual perception a colour is
almost never seen as it really is.\" Key extractable concepts: colour
relativity, simultaneous contrast, one colour appearing as two (and vice
versa), vibrating boundaries, transparency illusion. 272 pages,
paperback, no ebook. Standing: universally canonical.

**Johannes Itten, *The Art of Color* (1961).** Complements Albers with a
classification-based approach. The seven colour contrasts (hue,
light-dark, cold-warm, complementary, simultaneous, saturation,
extension/proportion) are individually card-worthy concepts. The
contrast of extension is particularly mathematical: Goethe\'s balance
ratios (yellow:violet = 1:3, orange:blue = 1:2, red:green = 1:1).
Condensed version *Elements of Color* (\~96 pages, Wiley) is more
accessible.

**OKLCH/OKLAB (Björn Ottosson, 2020).** Oklab is a D65-referenced model
whose coordinates aim to approximate perceived lightness, chroma and hue;
its uniformity is a fitted approximation, not a guarantee across hues,
contexts, displays or destination gamuts. The linear-sRGB route uses a linear
transform, a pointwise real cube root and a second linear transform; encoded
sRGB must first be decoded. CSS supports explicit forms such as
`oklch(L C H)` and relative colour syntax such as
`oklch(from var(--base) calc(l + 0.15) c h)` where implemented. Select
candidates, inspect destination gamut/rendering and check actual colour pairs
when contrast matters; equal L does not certify appearance or accessibility.

**CIE colour science** provides the mathematical foundation. Colour
difference formulas progress from simple Euclidean distance in CIELAB
(ΔE\*₇₆) through the sophisticated CIEDE2000 with its five correction
terms. For the target user: **linear colour-space conversion stages use 3×3 matrices** --- literal
linear algebra. Complete conversions can also include nonlinear decoding
and componentwise cube roots.
:::

### Typography: From Bringhurst\'s Proportions to Utopia\'s Fluid Interpolation {#typography-from-bringhursts-proportions-to-utopias-fluid-interpolation style="margin-top: var(--space-xl);"}

::: prose
**Robert Bringhurst, *The Elements of Typographic Style* (v4.0, 2012,
398 pages).** The \"typographers\' bible.\" Organised around principles
(rhythm, proportion, harmony) rather than tutorials. Its mathematical
content on proportional systems directly inspired Tim Brown\'s modular
scale work. Standing: canonical but print-focused.

**Tim Brown\'s modular scale** connects typographic proportion with
web implementation. A modular scale generates values by repeated
multiplication by a selected ratio. Musical intervals can supply such
ratios: low-to-high pairs `15:16`, `4:5`, `3:4` and `2:3` correspond to
increasing multipliers `16/15 ≈ 1.067`, `5/4 = 1.250`, `4/3 ≈ 1.333`
and `3/2 = 1.500`, respectively. The pair notation names the smaller and
larger values; the multiplier is the larger divided by the smaller.
Brown quotes Bringhurst: \"A modular scale, like a musical scale, is a
prearranged set of harmonious proportions.\" This attributed description
does not prove that every constructed scale is visually harmonious,
readable or accessible; judge it with the project's content and conditions.

**Every Layout (Heydon Pickering & Andy Bell)** offers a vocabulary of
13 layout primitives: Stack, Box, Center, Cluster, Sidebar, Switcher,
Cover, Grid, Frame, Reel, Imposter, Icon and Container. Intrinsic sizing
and wrapping can make compositions adapt without a query where the task
permits; content or interaction may still require a discrete mode.
The emphasis on composing reusable parts has a useful parallel with
software design, rather than proving identical semantics or universal
coverage. Select the patterns that fit, retain appropriate markup and
interaction behavior, and check the result with actual content and conditions.

**Utopia (James Gilyead & Trys Mudford)** offers one approach to fluid
responsive design: choose endpoint bases, ratios and an interpolation
interval, then calculate each step independently. A linear preferred
expression supplies interpolation; `clamp()` bounds that expression.
With positive endpoint bases and ratios and a shared interior parameter,
the interpolated steps form a geometric sequence only when the endpoint
ratios are equal. Each step's slope depends on its own endpoint difference,
so higher headings do not necessarily grow faster than body text.
These calculations do not establish visual harmony or accessibility.
:::

### UI/UX: Norman\'s Affordances Through Laws of UX to Refactoring UI {#uiux-normans-affordances-through-laws-of-ux-to-refactoring-ui style="margin-top: var(--space-xl);"}

::: prose
**Don Norman, *The Design of Everyday Things* (revised 2013, 368
pages).** The foundational text of interaction design. Six concepts for
discoverability: affordances, signifiers, mapping, feedback,
constraints, conceptual models. The 2013 revision introduced
\"signifiers\" to resolve the widespread misuse of \"affordance.\"

**Laws of UX (Jon Yablonski, lawsofux.com)** compiles 30 laws organised
into heuristics (Fitts\'s Law, Hick\'s Law, Jakob\'s Law, Miller\'s Law,
Doherty Threshold), gestalt principles, cognitive biases, and
principles. Freely accessible, each law includes psychological
foundations and practical applications --- ideal for concept card
extraction.

**Refactoring UI (Adam Wathan & Steve Schoger, \~218 pages, PDF).** The
definitive developer-to-designer bridge. Core insight: **design is a set
of systematic, repeatable decisions, not artistic intuition.** Key
tactical patterns: constrained spacing scales, HSL-based palette
construction, \"start with too much whitespace,\" design in greyscale
first.

**Brad Frost, *Atomic Design* (free at atomicdesign.bradfrost.com).**
Five levels: atoms → molecules → organisms → templates → pages. Maps
directly to React/Vue component architecture.
:::

------------------------------------------------------------------------

::: section-label
Section 4
:::

## Design Has Rigorous Mathematical Structure

Not soft-discipline hand-waving --- precise formulations with empirical
grounding.

### Quantitative UX Laws

::: formula
[Fitts\'s Law (ISO 9241, Shannon formulation)]{.label} MT = a + b ×
log₂(1 + D/W)
:::

::: prose
Where MT is movement time, D is distance to target, W is target width,
and the Index of Difficulty ID = log₂(1 + D/W) is measured in bits.
Fitts drew directly from Shannon\'s channel capacity theorem.
**Throughput TP = ID/MT** ≈ 10 bits/s for mouse pointing. The Steering
Law for path-following is derived by integral calculus: T = a + b ×
(A/W).
:::

::: formula
[Hick\'s Law]{.label} RT = a + b × log₂(n + 1)
:::

::: prose
The +1 represents the null event (temporal uncertainty of stimulus
onset). General form uses Shannon entropy: RT = a + b × H where H = −Σ
pᵢ log₂(pᵢ). Breaks down critically when stimulus-response compatibility
is high (Leonard, 1959: NO set-size effect with highly compatible
mappings).
:::

::: formula
[Stevens\'s Power Law]{.label} ψ = k × Iⁿ
:::

::: prose
Explains why design systems use geometric spacing scales: visual area
has exponent n ≈ 0.7 (compressive), meaning doubling physical area does
NOT double perceived size --- you need \~2.7× the area. Brightness has n
≈ 0.33 in this account; that observation does not derive either a display
transfer curve or a colour-space nonlinearity. A display transfer curve and
Oklab's chosen cube-root stage have different purposes and assumptions.
:::

::: formula
[Weber-Fechner Law]{.label} ΔI / I = k
:::

::: prose
Just-noticeable differences are proportional to stimulus intensity. For
line length, k ≈ 0.03 (3%). This is why spacing scales must be geometric
(multiplicative) rather than arithmetic (additive) to create
perceptually equal steps.
:::

### Group Theory Classifies All Possible Repeating Patterns {#group-theory-classifies-all-possible-repeating-patterns style="margin-top: var(--space-xl);"}

::: prose
The **17 wallpaper groups** (proven by Fedorov, 1891) constitute a
complete mathematical classification of every possible two-dimensional
repeating pattern. The **7 frieze groups** do the same for border/strip
patterns. The crystallographic restriction theorem proves that only 2-,
3-, 4-, and 6-fold rotational symmetries are compatible with periodic
lattices --- which is why 5-fold symmetry (Penrose tilings) requires
aperiodic structures. This is not a heuristic but a mathematical
absolute: any CSS `background-repeat` pattern, textile, or tile design
must conform to one of these groups.
:::

### Gestalt Principles Have Computational Formalisations {#gestalt-principles-have-computational-formalisations style="margin-top: var(--space-xl);"}

::: prose
Kubovy & Wagemans (1995, 1998) established the **Pure Distance Law**:
grouping by proximity follows an exponential decay function of relative
inter-element distance --- log\[p(b)/p(a)\] = −α × (\|b\|/\|a\| − 1),
where α ≈ 3 is the attraction constant. Crucially, only *relative*
distances matter, not absolute ones. Recent work using persistent
homology (Chen et al., 2024) provides a unified computational framework
where proximity appears as 0-dimensional persistence and closure as
1-dimensional persistence in Vietoris-Rips filtrations.
:::

------------------------------------------------------------------------

::: section-label
Section 5
:::

## The Rosetta Stone: Cross-Domain Analogies

Where cross-domain analogies are rigorous versus merely metaphorical.

::: bridge-card
#### Software Engineering → Design Systems: Implementations, Not Analogies

Every major software engineering principle has a direct,
non-metaphorical implementation in design systems. **Abstraction** →
design tokens abstract visual decisions from implementation. **DRY** → a
centralised token repository is the single source of truth. **API
design** → a React component\'s props interface IS an API with types,
defaults, and contracts. **Composition over inheritance** → Every Layout
explicitly advocates this for CSS. **Dependency injection** → CSS custom
properties are injected at root scope and consumed by children. All
rated **RIGOROUS**: same concepts, not analogies.
:::

::: bridge-card
#### Music Theory → Visual Design: Three Connections

**Musical intervals → type scale ratios (SHARED CONSTRUCTION).** Brown's
modular-scale discussion uses musical ratios as one source of proportions.
An increasing perfect-fourth scale uses `4/3 ≈ 1.333`; a perfect-fifth
scale uses `3/2 = 1.500`. The common mathematics is repeated multiplication
by a chosen ratio. The golden ratio `φ = (1 + sqrt(5))/2 ≈ 1.618` is another
possible geometric multiplier, not a musical interval. Shared arithmetic
does not transfer auditory harmony into a guarantee of visual harmony,
readability or suitability for a project's content.

**Temperament → perceptual uniformity in colour spaces (LOOSE ANALOGY).**
Equal temperament divides an octave into equal frequency ratios, while
perceptual colour spaces aim to make coordinate differences more consistent
with perceived colour differences. The design goals are comparable, but the
mathematics and perceptual measurements differ; equal coordinate steps do
not guarantee equal appearance in every context.

**Linear algebra → colour space transformations (RIGOROUS).** Matrix
stages are literal linear algebra. To convert encoded sRGB to Oklab,
first decode to linear sRGB. Transform linear sRGB to XYZ and then LMS
using the D65 matrices, apply a componentwise real cube root, and use a
final matrix to obtain Oklab. Adjacent linear stages can be composed into
one matrix; the complete pipeline cannot be collapsed across its
nonlinear operations.

**Colour harmony ↔ musical harmony (LOOSE to STRUCTURAL).** The 12-hue
wheel / 12-semitone parallel is structurally suggestive, but colour
perception is trichromatic while auditory perception is
frequency-analytic. Empirical evidence for colour harmony based on
frequency ratios is weak. The structural parallel has practical value,
but mathematical equivalence is unsupported.
:::

------------------------------------------------------------------------

::: section-label
Section 6
:::

## Token Architecture Choices

::: notes
#### Colour Notation: Shifting from Hex to OKLCH

Hex is a widely used sRGB notation and remains useful for interchange. Other
CSS colour syntaxes, including OKLCH, serve different authoring and modelling
needs; adoption and suitability depend on the project and target environment.
One possible notation uses primitive values (`color.blue.500`),
semantic aliases (`color.primary`, `color.surface.default`), and
component bindings (`color.button.primary.background.hover`). This
example is not evidence that three tiers are the dominant industry
pattern. Choose reusable values when reuse helps, semantic aliases when
shared meaning or theme variation benefits, and component bindings when
local control warrants their maintenance. Additional layers add
indirection; fewer can couple consumers to shared values. A value change
reaches only consumers whose references resolve through it; local literals
and separate mappings need their own review. With CSS relative colour
syntax now baseline, teams can define `--brand-l`, `--brand-c`,
`--brand-h` as separate properties and generate tonal scales via
`calc()`.
:::

::: notes
#### Spacing Notation: 4-Point Base with 8-Point Primary Rhythm

The 4-point vs. 8-point grid debate has converged: modern teams use a
**4pt base** with 8pt as the primary structural rhythm. Component
padding at 4--16px, section margins at 24--64px. For token naming, the
dominant patterns are T-shirt sizing (`space-xs` through `space-3xl`),
numeric scales (`space.1` through `space.8`), and semantic aliases
(`spacing.inset.md`, `spacing.section.lg`).
:::

::: notes
#### Typography Tokens: Composite Structures

DTCG 2025.10 defines a typography composite with `fontFamily`, `fontSize`,
`fontWeight`, `lineHeight`, and `letterSpacing` values or appropriately typed
references. Composite value structure is separate from token naming and layers.
Utopia's calculator example uses numbered steps such as `--step--2` and
`--step-5`; its method and prefix are configurable. Choose names and scale
construction for the adopting project rather than treating an example as a
universal convention.
:::

::: notes
#### Responsive Notation: From Breakpoints to Fluid Ranges

Breakpoint naming universally uses T-shirt sizing (`sm`, `md`, `lg`,
`xl`), but Utopia\'s approach replaces discrete breakpoints with
continuous `clamp()` interpolation. Container queries (`@container`)
enable component-level responsiveness independent of viewport. Cascade
layers (`@layer`) solve specificity wars by defining explicit cascade
order.
:::

------------------------------------------------------------------------

::: section-label
Section 7
:::

## The 2024--2025 CSS Landscape: A Generational Capability Shift

::: prose
Modern CSS has undergone a transformation comparable to the introduction
of Flexbox. **Container queries** (96%+ global support) let components
respond to their own available space. **`:has()`** enables parent
selection based on children, previously requiring JavaScript.
**Subgrid** (97% support) solves nested alignment. **CSS Nesting**
eliminates the need for preprocessors. **Scroll-driven animations**
replace GSAP ScrollTrigger for parallax and reveal effects.

For colour: `oklch()`, `color-mix()`, relative colour syntax, and
`color(display-p3)` are all baseline. Wide-gamut displays (Display P3
covers \~50% more colours than sRGB) are standard on Apple devices and
OLED screens. Variable fonts provide continuous weight, width, and
optical size adjustment from a single file.

**Figma** has matured its variables system with multi-mode support
(light/dark, brand variants), native DTCG JSON import/export, and Code
Connect for mapping Figma components to production code. Style
Dictionary v4 provides first-class DTCG format support for transforming
tokens to any platform.
:::

------------------------------------------------------------------------

::: section-label
Section 8
:::

## Source Availability and Acquisition Summary

::: {style="overflow-x: auto;"}
  Source                                        Format                     Pages   Free?                 Priority
  --------------------------------------------- -------------------------- ------- --------------------- -------------------------
  Albers, *Interaction of Color*                Paperback (no ebook)       272     No                    [Essential]{.essential}
  Itten, *Elements of Color*                    Paperback                  96      No                    High
  Bringhurst, *Elements of Typographic Style*   Print only, v4.0           398     No                    [Essential]{.essential}
  Lupton, *Thinking with Type* (3rd ed, 2024)   Print, companion site      256     No                    [Essential]{.essential}
  Müller-Brockmann, *Grid Systems*              Print, bilingual           176     No                    High
  Vignelli, *The Vignelli Canon*                Free PDF from RIT          96      [Yes]{.free}          [Essential]{.essential}
  Norman, *Design of Everyday Things*           Ebook available            368     No                    [Essential]{.essential}
  Krug, *Don\'t Make Me Think*                  Print/ebook                200     No                    High
  Frost, *Atomic Design*                        Free online                \~200   [Yes]{.free}          High
  Refactoring UI                                PDF only                   \~218   No (\$79--149)        [Critical]{.essential}
  Laws of UX                                    Free website + book        ---     [Yes (site)]{.free}   [Essential]{.essential}
  Butterick, *Practical Typography*             Free web book              ---     [Yes]{.free}          High
  Every Layout                                  Paid website (some free)   ---     Partially             High
  Utopia                                        Free calculators + blog    ---     [Yes]{.free}          [Essential]{.essential}
  Comeau, CSS for JS Developers                 Paid course (blog free)    ---     Partially             High
  Eckles, ModernCSS.dev                         Free website               ---     [Yes]{.free}          High
  Gurney, *Color and Light*                     Print                      224     No                    Supplementary
  Arnheim, *Art and Visual Perception*          Print                      508     No                    Supplementary
  Ware, *Information Visualization*             Print (4th ed)             560     No                    Supplementary
:::

::: {.notes style="margin-top: var(--space-m);"}
#### Recommended Acquisition Priority

Start with the free resources (Vignelli Canon, Atomic Design, Laws of
UX, Butterick, Utopia, ModernCSS.dev), then acquire Refactoring UI (the
single most valuable resource for a developer), followed by Lupton and
Bringhurst for typography, Albers for colour, and Norman for interaction
design principles.
:::

------------------------------------------------------------------------

::: section-label
Conclusion
:::

## The Knowledge Base Should Mirror the Field\'s Layered Architecture

::: {.prose style="margin-bottom: var(--space-l);"}
This research reveals that visual design is not a flat collection of
tips but a **layered discipline** with formal mathematical structure at
its foundation.
:::

::::::: layer-stack
::: {.layer-item}
[Layer 0 --- Perception Science]{.layer-name} [Gestalt laws,
preattentive processing, Stevens\'s Power Law,
Weber-Fechner]{.layer-desc}
:::

::: {.layer-item}
[Layer 1 --- Design Principles]{.layer-name} [Hierarchy, contrast,
rhythm, proportion, balance --- the \"theorems\"]{.layer-desc}
:::

::: {.layer-item}
[Layer 2 --- Domain Knowledge]{.layer-name} [The ten-category taxonomy
with specific concepts and vocabulary]{.layer-desc}
:::

::: {.layer-item}
[Layer 3 --- Implementation]{.layer-name} [CSS capabilities, design
tokens, component architecture, fluid systems]{.layer-desc}
:::
:::::::

::: {.prose style="margin-top: var(--space-l);"}
The **cross-domain Rosetta Stone** should be woven throughout rather
than isolated in a separate section. When a concept card explains
modular type scales, it should note the identical mathematical structure
to musical intervals. When it explains OKLCH\'s perceptual uniformity,
it should reference the temperament analogy. When it explains design
tokens, it should map directly to software engineering abstraction.

The target user\'s existing expertise in mathematics, music theory, and
software engineering isn\'t a gap to be bridged --- **it\'s the
foundation on which the entire knowledge base should be built.**
:::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::: footer
::::: footer-inner
::: meta
Foundations of Design · Research · March 2026 · CC0 Public Domain
:::
:::::
::::::
