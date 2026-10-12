:::: hero

A Manifesto for Visual Systems

# Design as Engineering

[On the convergence of mathematical proportion, perceptual science, and
software architecture in the construction of visual
identity.]{.subtitle}

::: tag-row
[Manifesto]{.tag} [Design Systems]{.tag} [Perceptual Science]{.tag}
[March 2026]{.tag}
:::
::::

:::::::::::::::::::::::::::::::::::::: container
::: section-label
Preamble
:::

::: epigraph
The details are not the details. They make the design.

--- Charles Eames
:::

::: {.preamble style="margin-top: var(--space-m);"}
This document is a statement of principles. It describes an approach to
visual design that treats aesthetic decisions not as matters of taste
but as engineering problems --- constrained, measurable, and composable.
It argues that the best design systems are not collections of components
but algebraic structures: closed under composition, governed by
invariants, and provably consistent.

These principles were refined through practical work with a design system.
They are not specific to that project. They explore useful connections between
visual design and software engineering while leaving room for their different
materials, goals and forms of evidence.

This is not a style guide. Style guides describe what to do. This
describes why.
:::

::: dot-divider
• • •
:::

::: section-label
Section I
:::

## The Convergence Thesis

::: prose
Material Design, Carbon and Polaris name distinct products and generations.
Compare their token models only after identifying the product, generation,
page date and token category. The available examples do not establish that
these systems share one architecture.

[Material Web's theming documentation](https://material-web.dev/theming/material-theming/)
distinguishes reference, system and component tokens, and allows concrete
component values. [Fluent 2's token documentation](https://fluent2.microsoft.design/design-tokens)
presents global and alias layers. These are bounded documentation examples,
not evidence that every design system requires the same layer count.
All three use multiplicative type scales rather than arbitrary font
sizes. All three enforce spacing systems built on a base unit with
constrained multipliers. All three separate colour into tonal scales
with systematic lightness progressions.

Similar structures across systems can reveal useful approaches, but they do
not establish one mandatory architecture. Tokens, scales and color models are
choices whose value depends on the project’s needs. Convergence is evidence to
inspect, not proof that alternatives are wrong.
:::

::: dot-divider
• • •
:::

::: section-label
Section II
:::

## Seven Principles

::::: {.principle-card numeral="I"}
### Multiply, Never Add

::: {.epigraph style="margin-top: var(--space-xs);"}
Just-noticeable differences are proportional to the stimulus intensity.

--- Ernst Heinrich Weber, 1834
:::

::: prose
A geometric scale is useful when proportional steps support the hierarchy,
but not every type size, spacing value or colour choice needs to be geometric.
Content, function, fixed dimensions and optical judgment can justify other
values. If a ratio helps, declare it as a local construction choice and inspect
the resulting hierarchy; departures are not errors by definition.

:::
:::::

:::: {.principle-card numeral="II"}
### Perception Is the Only Coordinate System That Matters

::: prose
OKLCH is a useful perceptual color space for exploring lightness, chroma and
hue. Its coordinates can help construct candidates, but equal numeric lightness
steps are not an exact guarantee of equal appearance across hues, contexts or
displays. Check rendered colors and complete foreground/background pairs.

Units such as `rem`, `ch` and `vi` describe different relationships and can be
useful in different contexts. Choose them for the intended behavior; no unit
alone proves a layout accessible or correct.

:::
::::

:::: {.principle-card numeral="III"}
### Name the Role, Not the Value

::: prose
Purpose-based aliases can distinguish a supplied value from the role that uses
it. For example, a project might keep `--client-action` and add
`--interactive-primary` as an alias if that name matches its existing
semantics. This is optional architecture: preserve established token names,
and add layers only when they solve a real maintenance need. A role name does
not prove that its value is appropriate in every component or state.

:::
::::

::::: {.principle-card numeral="IV"}
### Constraint Liberates; Freedom Paralyses

::: {.epigraph style="margin-top: var(--space-xs);"}
Real freedom is not the absence of structure but the presence of the
right structure.

--- After Barry Schwartz
:::

::: prose
A small, coherent set of spacing choices can make a project easier to use and
maintain, just as a useful constraint can support creative work. The right
constraints depend on the task and existing system. There is no required number
of type families, palette hues, spacing tokens or scale ratios. Keep the choices
that help people make and review the work.

:::
:::::

:::: {.principle-card numeral="V"}
### Unity Is Not Uniformity

::: prose
A coherent system can support distinct expressions without requiring them to
look alike. Decide which principles, components or names should remain shared
and which should vary for the project’s audience, content, medium and task.
The useful boundary preserves meaning and makes work easier to maintain; it
does not require a fixed number of sites or a prescribed font/color scheme.

A variable font illustrates one way an asset can vary along supported axes;
its use depends on the selected file and typographic goal. Shared structure and
contextual expression can coexist without making every project look the same.

:::
::::

:::: {.principle-card numeral="VI"}
### Proximity Carries Meaning; Uniformity Erases It

::: prose
Proximity is one cue that can help viewers infer grouping; its effect depends
on other visual signals and the viewing task. Repeated spacing can obscure
some relationships, while consistent spacing can aid comparison or scanning.
Use distance to support the intended grouping and inspect it with the actual
content. Other cues can establish relationships without a numerically smaller
gap.

:::
::::

::::: {.principle-card numeral="VII"}
### Design the Invariants, Not the Instances

::: {.epigraph style="margin-top: var(--space-xs);"}
Show me your flowchart and conceal your tables, and I shall continue to
be mystified. Show me your tables, and I won\'t usually need your
flowchart.

--- Fred Brooks (paraphrased)
:::

::: prose
A design system can capture relationships that should remain stable across
screens or components, such as shared token meanings or a useful type
hierarchy. Which properties are invariants depends on the project. Screens
still need to be designed and checked against their content, viewport, users
and context; a system can guide decisions without determining every
composition in advance.

:::
:::::

::: dot-divider
• • •
:::

::: section-label
Section III
:::

## The Deeper Structure

::: prose
Underneath these seven principles lies a single insight that unifies all
of them: the visual properties that humans perceive as \"harmonious\" or
\"consistent\" or \"professional\" are, without exception, properties
that exhibit mathematical regularity. Geometric type scales.
Perceptually uniform colour spaces. Proportional spacing. Systematic
tonal progressions. Consistent axis ratios.

This is not a coincidence and it is not a cultural construction. It is a
consequence of how neural systems process sensory information. Pattern
recognition is metabolically expensive; regular patterns are cheap to
process and therefore experienced as pleasant. Irregular patterns demand
more processing and are experienced as effortful --- which the mind
interprets as \"something is wrong,\" even when it cannot identify what.

This is why \"it just looks off\" is a reliable design critique even
from non-designers. They are detecting a violation of mathematical
regularity that they cannot name. The purpose of a principled design
system is to make that violation structurally impossible --- to ensure
that every composition the system permits is one that the visual cortex
will process as coherent.

Comparisons between Material Design, Carbon and Polaris need an identified
product generation and token category. Their available examples do not
establish one shared token architecture. A token-model comparison also does
not establish a universal law of perception.
:::

::: dot-divider
• • •
:::

::: section-label
Section IV
:::

## On Tools and Technology

::: prose
**Variable fonts** can expose ranges of variation along documented axes.
Their practical value depends on the selected asset, supported axes, browser
behavior and typographic goal. Inspect the actual font and rendered samples;
not every value in an axis range is a designed or suitable style.

**OKLCH** is a useful CSS color space for exploring lightness, chroma and hue.
It does not make coordinates exact predictions of perceived color. Check
rendered values and complete pairs in their actual context.

**Fluid type and spacing via CSS `clamp()`** can interpolate values between
declared bounds. It can reduce abrupt changes for some content, while a
breakpoint or fixed value may fit other behavior better. Review the actual
interface across its supported conditions.

**Design tokens** can record shared values and roles. Their scope and semantics
come from the adopting project; a token name does not by itself guarantee a
particular value, behavior or cross-platform result.
:::

::: dot-divider
• • •
:::

::: section-label
Section V
:::

## Coda

::: prose
There is a persistent mythology that design and engineering are opposed
--- that rigour constrains creativity, that systems suppress expression,
that mathematics is the enemy of beauty. The evidence says otherwise.

The most enduring visual works in human history --- the Parthenon, the
illuminated manuscripts, the Renaissance canvases, the Swiss typographic
posters, the Braun products --- are without exception works of profound
mathematical regularity. Their creators did not experience the golden
ratio and the modular grid and the baseline rhythm as constraints on
their art. They experienced them as the medium through which their art
became possible.

A well-built design system is not a cage. It is an instrument. Like any
good instrument, it has constraints --- a piano has 88 keys, not
infinite frequencies --- and those constraints are precisely what allow
a skilled practitioner to produce music instead of noise.

**Build the instrument well. Tune it to human perception. Then play.**
:::

::: dot-divider
• • •
:::
::::::::::::::::::::::::::::::::::::::

:::::: footer
::::: footer-inner
::: meta
Design Manifesto · March 2026 · CC0 Public Domain
:::
:::::
::::::
