:::: hero

Colour theory, typography, & layout-composition

# Foundational Research for a Visual Design Knowledge Base

This guide is a working organization of visual-design topics, selected questions,
reading pointers and cross-domain connections. Some topics use formal models or
empirical findings; others are contextual design methods and aesthetic judgments.
The taxonomy and questions are proposals for organizing learning, not a validated
curriculum, a completed source survey or proof of first-principles coverage.

::: tag-row
[Research]{.tag} [Domain Taxonomy]{.tag} [Competency Questions]{.tag}
[Source Analysis]{.tag}
:::
::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::: container
::: section-label
Section 1
:::

## A Working Taxonomy with Foundational and Cross-Cutting Topics

::: prose
The working categories include colour, typography, layout-composition, visual
perception, interaction, accessibility, information architecture, design systems
and visual identity. Their boundaries overlap; they are a practical navigation
choice rather than a validated description of every school or textbook.
:::

::: finding-card
#### Include Visual Elements

Point, line, plane, shape, texture and value provide useful vocabulary before
more specialized topics. Lupton & Phillips's *Graphic Design: The New Basics*
and Lauer & Pentak's *Design Basics* are reading pointers, not evidence that
every foundation course follows the same sequence.
:::

::: notes
#### Consider Motion, Data Visualization and Imagery

**Motion** includes timing, easing and choreography, with interaction, preference
and accessibility consequences. **Data visualization** combines visual encoding
with data and task needs. **Imagery** includes photography, illustration and
iconography. Give them navigable homes if the intended work needs them; no vendor
or school survey establishes a mandatory category list here.
:::

::: {.prose style="margin-top: var(--space-m);"}
Visual perception and layout overlap: proximity and other grouping cues help
explain arrangements, without acting as universal layout laws. Accessibility
cross-cuts all categories; either model it as a facet or make its requirements
visible within each topic. Visual identity also supplies an application context,
so its granularity differs from an individual colour or type concept.

Hierarchy, contrast, rhythm, proportion and balance can connect several topics.
Cross-reference their uses while retaining the distinction between a definition,
a contextual design strategy, an empirical result and a theorem with assumptions.
:::

### How Design Systems Organize Their Documentation {#how-design-systems-organize-their-documentation style="margin-top: var(--space-xl);"}

Documentation can be compared by principles, visual styles, tokens, components,
patterns and platform guidance. These are useful comparison questions, not an
established shared six-layer architecture. Identify each product, generation,
page date and category before drawing a conclusion; vendor labels and omissions
can mean different things.

::: {.prose style="margin-top: var(--space-s);"}

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

## Selected Questions Connect Perception and Implementation

::: prose
These selected prompts span definition, relationship, diagnosis, procedure and
cross-domain reasoning. The tiers are a working teaching aid; no completed
55-question assessment, professional certification survey or validity study is
claimed. Answer the actual question, identify its assumptions and record what
requires source or rendered-behavior evidence.
:::

:::: tier-section
[Foundational Tier]{.tier-label .tier-foundational}

### Core Vocabulary and First Principles

::: prose
**Definitional.** What is visual hierarchy, and what visual properties
(size, colour, contrast, weight, spacing) establish it? What
distinguishes a spacing system from arbitrary padding values --- what
problem does constraint solve? What are the three components of HSL, and
when might its controls help a particular palette task compared with hex notation?
HSL is an sRGB parameterization, while hex encodes sRGB channel values; neither
notation is universally better or a perceptual/contrast guarantee.

**Relational.** How do font weight and colour work *together* with font
size to create typographic hierarchy --- why is size alone insufficient?
How does the relationship between inter-group and intra-group spacing
communicate which elements belong together?

**Diagnostic.** A card layout uses 16px padding inside cards, 16px
between cards, and 16px between card title and body. Which relationships, if any, are unclear? Equal spacing alone does not prove a
problem. Inspect content, headings, borders, alignment and intended grouping;
closer within-group spacing is one possible cue, not a mandatory inequality.
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
car.\" What actual problem does the task reveal? Many hues alone do not establish a
violation. Check meaning/role consistency, hierarchy, complete pair/state contrast
and signals beyond colour. Preserve justified distinctions and supplied identity;
propose changes for observed problems, not a prescribed number of hues.
:::
::::

:::: tier-section
[Advanced Tier]{.tier-label .tier-advanced}

### Systematic Thinking and Cross-Domain Integration

::: prose
**Relational.** How does a well-structured design token system map onto
CSS custom properties? Which design decisions map to implementation contracts, and where do the
analogies stop? A shared vocabulary is not an isomorphism. How does cognitive load theory (intrinsic,
extraneous, germane) relate to progressive disclosure and visual
hierarchy?

**Diagnostic.** An admin panel organises UI by database tables --- Users
page, Orders page, Products page, each showing all columns. Assess whether this arrangement supports the actual users' tasks. A task-focused
view such as processing orders or handling returns may help; a table-focused
administration view can also be justified. Inspect what information and actions
people need before prescribing reorganization.
:::
::::

::: {.finding-card style="margin-top: var(--space-m);"}
#### Six Useful Review Questions

Ask whether the interface has (1) useful hierarchy, (2) understandable grouping,
(3) coherent colour roles, (4) appropriate typography, (5) information and actions
that support tasks, and (6) distinguishable action priorities. These are review
prompts, not a measured ranking or an explanation of a majority of quality gaps.
Neither a geometric scale nor a fixed palette/typeface count is a prerequisite.
:::

------------------------------------------------------------------------

::: section-label
Section 3
:::

## Reading Pointers Across Design Topics

The following pointers connect perception, design methods, practical patterns,
architecture and CSS. This map does not establish a single intellectual lineage,
complete bibliography or independent verification of each book. Check editions,
source context and actual supporting passages before relying on a particular
attribution or historical claim.

### Colour Theory: From Albers\'s Relativity to OKLCH\'s Perceptual Uniformity

::: prose
**Josef Albers, *Interaction of Color* (1963).** A reading pointer for colour
relativity, simultaneous contrast, apparent transparency and the influence of
context. Exact passages, editions and demonstrations need source inspection;
no exclusive print/ebook availability is asserted.

**Johannes Itten, *The Art of Color* (1961), and *Elements of Color*.** Reading
pointers for classifications such as hue, light-dark, complementary, saturation
and extension/proportion contrasts. Historical balance ratios are attributed
design proposals, not universal physical mixture or harmony laws.

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
difference formulas include Euclidean ΔE*₇₆ in CIELAB and later fitted
corrections such as CIEDE2000. Their predictions have defined conditions and limits. For the target user: **linear colour-space conversion stages use 3×3 matrices** --- literal
linear algebra. Complete conversions can also include nonlinear decoding
and componentwise cube roots.
:::

### Typography: From Bringhurst\'s Proportions to Utopia\'s Fluid Interpolation {#typography-from-bringhursts-proportions-to-utopias-fluid-interpolation style="margin-top: var(--space-xl);"}

::: prose
**Robert Bringhurst, *The Elements of Typographic Style* (4.0, 2012).** A
reading pointer for rhythm, proportion and typographic craft, with print-focused
context. Brown quotes Bringhurst in his modular-scale discussion; this does not
establish every claimed historical influence or validate a universal type rule.

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
**Don Norman, *The Design of Everyday Things* (revised 2013).** A reading
pointer for affordances, signifiers, mapping, feedback, constraints and conceptual
models. Apply each term with its source context and the actual interaction.

**Laws of UX (Jon Yablonski).** An organized set of laws, principles and
heuristics to inspect individually; a label “law” does not give every UI claim
universal empirical support.

**Refactoring UI (Adam Wathan & Steve Schoger).** A pointer for practical
interface decisions, including hierarchy, spacing and palette exercises. Such
methods can support systematic work while retaining intuition and contextual
judgment. HSL construction or grayscale-first work are options, not requirements.

**Brad Frost, *Atomic Design*.** Atoms, molecules, organisms, templates and pages
provide a compositional vocabulary. It can inform component architecture;
React/Vue components do not automatically have identical semantics or require
those five layers.
:::

------------------------------------------------------------------------

::: section-label
Section 4
:::

## Use Mathematical Models Within Their Domains

Formal models can clarify selected tasks when their quantities, assumptions and
empirical parameters are identified. They do not turn aesthetic judgments or
all interface behavior into mathematical consequences.

### Quantitative UX Laws

::: formula
[Fitts's model (Shannon formulation)]{.label} MT = a + b ×
log₂(1 + D/W)
:::

::: prose
For a defined aimed-pointing task, MT is movement time, D the movement distance
and W target width along the movement direction; D/W must be dimensionless with
W>0. The index log₂(1+D/W) is conventionally expressed in bits. Fit a and b to the
device, participants and task; no portable throughput of 10 bits/s follows.
Throughput estimation requires an explicit method, including accuracy/effective
width and aggregation, rather than interpreting one nominal ID/MT as a universal
capacity. See [MacKenzie's model and measurement discussion](https://www.yorku.ca/mack/hhci2018.html).

For a constant-width steering path, a fitted model is T=a+b(A/W), where A is path
length and W>0 its constant width. A variable-width version may use
T=a+b∫ds/W(s), with positive local width, specified path/task assumptions and
empirically fitted coefficients. Neither formula by itself guarantees easier
menus, better performance or aesthetic quality.
:::

::: formula
[Hick\'s Law]{.label} RT = a + b × log₂(n + 1)
:::

::: prose
Here n is a defined positive number of alternatives and a,b are fitted task
parameters. The log₂(n+1) expression is a model form, not a universal law for menu
length. Under an appropriate probability/task model, entropy
H=−Σpᵢlog₂pᵢ can replace a simple count, with probabilities summing to one and
zero terms taken by their limit. Compatibility, practice, grouping and search
strategy affect applicability. Hick's original hypothesis must be read in its
experimental context; the primary scan was unavailable in this review, so no
exact +1-origin story or precise Leonard (1959) result is asserted.
:::

::: formula
[Stevens\'s Power Law]{.label} ψ = k × Iⁿ
:::

::: prose
For a specified stimulus, task and range, ψ denotes a measured perceptual
response, I a positive stimulus magnitude and k,n empirically fitted parameters.
This model supplies no portable visual-area exponent 0.7, brightness exponent
0.33 or requirement for geometric spacing/type scales. Display transfer curves
and Oklab's model nonlinearity serve distinct purposes.
:::

::: formula
[Weber relation]{.label} ΔI / I = k
:::

::: prose
Within a specified discrimination task/range, I>0 is stimulus magnitude, ΔI the
just-noticeable increment and k a fitted fraction. No universal 3% line-length
threshold or typography/spacing necessity is established. The full Fechner
logarithmic account is distinct and needs additional assumptions; ΔI/I=k alone
is Weber's relation.
:::

### Periodic Pattern Symmetry Has Precise Assumptions {#group-theory-classifies-all-possible-repeating-patterns style="margin-top: var(--space-xl);"}

::: prose
The **17 wallpaper groups** classify planar Euclidean symmetry types with two
independent translations; the **7 frieze groups** classify one-direction periodic
strip patterns. Under the lattice assumptions, nontrivial rotation orders are
2,3,4,6; identity order 1 is also allowed. A local five-fold motif can occur inside
a repeated cell without being a symmetry of the whole periodic pattern.
Finite crops, one-axis repeats, responsive layouts and aperiodic tilings do not
all satisfy doubly periodic plane assumptions. A CSS background can realize a
periodic tiling, but its actual whole-pattern symmetry must be identified before
applying a classification. See the [IUCr periodic-group tables](https://www.iucr.org/__data/assets/pdf_file/0015/16602/ite.pdf).
:::

### Gestalt Principles Have Computational Formalisations {#gestalt-principles-have-computational-formalisations style="margin-top: var(--space-xl);"}

::: prose
In controlled, briefly displayed dot-array experiments, the Pure Distance Law
relates grouping log-odds to relative interdot-distance ratios. One reported form
is ln[p(b)/p(a)]=−α(||b||/||a||−1), using the natural logarithm, defined
responses/distances and an empirically fitted α. It is not a universal attraction
constant or a law that only relative distance matters in every interface.
Other grouping cues combine with proximity; stimulus construction and task affect applicability. See
[Kubovy's scoped discussion](https://academic.oup.com/edited-volume/42044/chapter/497008788).
A Chen et al. (2024) persistent-homology connection is an unverified reading
pointer here; no precise technical result from that work was inspected or adopted.
:::

------------------------------------------------------------------------

::: section-label
Section 5
:::

## The Rosetta Stone: Cross-Domain Analogies

Where cross-domain analogies are rigorous versus merely metaphorical.

::: bridge-card
#### Software Engineering → Design Systems: Separate the Connections

**Abstraction.** Tokens can separate reusable visual decisions from consumers;
useful naming/layer boundaries depend on the adopting project.
**DRY.** A shared token can reduce duplication only for consumers whose references
actually resolve through it; literals and independent mappings remain.
**API design.** A component props interface is an actual software API, with its
own behavior/types/contracts; visual design choices are not all API semantics.
**Composition.** Composing layout patterns can be useful, without proving that
every CSS rule implements the same principle as object composition.
**Dependency injection.** Custom properties participate in CSS cascade,
inheritance and substitution. A root-scoped value can supply descendants; that
mechanism alone is not software dependency injection or an isomorphism.
:::

::: bridge-card
#### Music, Mathematics and Colour: Scoped Connections

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

**Colour harmony ↔ musical harmony (LOOSE).** A circular indexing analogy can
organize discussion, but the ten-family Munsell diagram and twelve pitch classes
have different cardinalities. 12TET ratios 2^(n/12) are a chosen construction;
colour calibration is a different problem. Neither a universal tritone tension
maximum nor colour harmony from musical ratios is established here.
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
and separate mappings need their own review. Where the target implements [relative colour syntax](https://www.w3.org/TR/css-color-5/#relative-colors),
`oklch(from var(--brand) calc(l + 0.1) c h)` illustrates a model-coordinate
candidate. The referenced custom property must resolve to a valid colour;
conversion, destination gamut and actual rendered-pair checks remain necessary.
Keeping channels as separate custom properties is another optional architecture.
:::

::: notes
#### Spacing Notation: Choose Project Units and Names

A project might choose spacing values in multiples of 4 CSS px, a ratio scale,
content-led values or a combination. This is a local choice, not demonstrated
industry convergence. CSS `pt` and `px` are different units: 1pt=4/3px by their
specified relation, not interchangeable shorthand for a grid unit. T-shirt
names, numeric labels and semantic names are options; preserve meaningful
existing conventions and explain any exceptions.
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

Breakpoint labels are project conventions; use names that express the actual
behavior. Fluid `clamp()` interpolation can coexist with justified discrete
changes. A size query requires an eligible ancestor query container with the
appropriate containment; it does not make a component independent of every
viewport or content condition. Cascade layers order parts of the cascade;
importance, origin, unlayered rules and specificity within a layer still matter.
No layer arrangement automatically solves all cascade conflicts.
:::

------------------------------------------------------------------------

::: section-label
Section 7
:::

## CSS Capabilities Need Their Own Conditions

::: prose
**Container queries** depend on the query type, eligible container and containment;
see [CSS Conditional5](https://www.w3.org/TR/css-conditional-5/#container-queries).
**`:has()`** is a relational selector that can inspect matching relatives; its
syntax and support need target checks. **Subgrid** participates in a parent
grid's track sizing. **Nesting** supplies CSS rule-nesting syntax; it does not
replace every preprocessor facility. **Scroll-driven animations** require the
appropriate timeline/property support, motion-preference behavior and testing;
they do not universally replace an animation library.

CSS colour functions define model-specific values and operations. Encoded sRGB,
linear-light and OKLCH interpolation differ; gamut mapping and actual pair/state
checks remain necessary. A Display P3 target is not guaranteed by an asset or
platform name. Variable fonts expose only the axes/ranges supported by the chosen
file; weight, width and optical size are not all present in every variable font.

Design-tool variables, token interchange and build transforms can assist a
workflow. Inspect the actual tool/version and exported values before claiming
DTCG import/export, component mapping or target-platform compatibility. No current
Figma/Style Dictionary survey, adoption metric or all-platform guarantee was
established for this guide.
:::

------------------------------------------------------------------------

::: section-label
Section 8
:::

## Reading List and Input Planning

These are reading pointers. Author/title/edition labels identify intended works;
exact source identity, relevant passages and availability must be checked before
use. This list supplies no prices, exclusive formats, current ebook claims or
purchase priority ranking.

| Topic | Reading pointers |
|---|---|
| Colour | Albers, *Interaction of Color*; Itten, *Elements of Color*; Gurney, *Color and Light* |
| Typography | Bringhurst, *The Elements of Typographic Style*; Lupton, *Thinking with Type* (3rd ed., 2024); Butterick, *Practical Typography* |
| Layout and identity | Müller-Brockmann, *Grid Systems*; Vignelli, *The Vignelli Canon*; *Every Layout* |
| Interaction | Norman, *The Design of Everyday Things*; Krug, *Don't Make Me Think*; Yablonski, *Laws of UX*; Wathan & Schoger, *Refactoring UI* |
| Systems and CSS | Frost, *Atomic Design*; Utopia; Comeau, *CSS for JS Developers*; Eckles, *ModernCSS.dev* |
| Perception and information | Arnheim, *Art and Visual Perception*; Ware, *Information Visualization* |

Choose a source for the actual unanswered question, access conditions and intended
use. Inspect its relevant evidence and context; a reading list is not proof that
its contents were reviewed, that acquisition is authorized or that one resource
is the most valuable for every developer.

------------------------------------------------------------------------

::: section-label
Conclusion
:::

## A Working Map for Learning and Implementation

::: {.prose style="margin-bottom: var(--space-l);"}
The following layers are one navigational map. They connect perception, design
judgment, domain vocabulary and implementation without claiming a validated
curriculum or reducing all design principles to mathematical theorems.
:::

::::::: layer-stack
::: {.layer-item}
[Layer 0 --- Perception Science]{.layer-name} [Gestalt laws,
preattentive processing, Stevens\'s Power Law,
Weber-Fechner]{.layer-desc}
:::

::: {.layer-item}
[Layer 1 --- Design Principles]{.layer-name} [Hierarchy, contrast,
rhythm, proportion and balance --- contextual concepts]{.layer-desc}
:::

::: {.layer-item}
[Layer 2 --- Domain Knowledge]{.layer-name} [Selected topics
with specific concepts and vocabulary]{.layer-desc}
:::

::: {.layer-item}
[Layer 3 --- Implementation]{.layer-name} [CSS capabilities, design
tokens, component architecture, fluid systems]{.layer-desc}
:::
:::::::

::: {.prose style="margin-top: var(--space-l);"}
Cross-domain connections can support learning when their shared construction
and limits are explicit. Repeated multiplication by a chosen ratio is shared
arithmetic; a musical interval does not guarantee visual harmony. Temperament is
a loose colour-calibration analogy, not a precise equivalence. Tokens can provide
abstraction in software without making every design choice a software theorem.

Mathematics, music and software experience can be useful starting points. Keep
room for learning the medium's own evidence, constraints, context and craft.
:::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::: footer
::::: footer-inner
::: meta
Foundations of Design · Research · March 2026 · CC0 Public Domain
:::
:::::
::::::
