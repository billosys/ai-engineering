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
This document argues for a principled approach to visual design: make
relationships explicit, choose useful constraints, inspect what can be measured,
and leave room for taste, context and craft. Software architecture and mathematics
can help organize decisions; they do not make aesthetic consistency provable or
turn every design system into a closed algebraic structure.

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

## Comparing Design Systems

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
### Use Proportion Where It Helps

::: {.epigraph style="margin-top: var(--space-xs);"}
Within a specified discrimination task and range, Weber's relation treats the
just-noticeable increment as a fitted fraction of positive stimulus intensity.

--- After Weber (model summary)
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
### Check Perception in Context

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
### Choose Constraints Deliberately

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
### Use Proximity to Support Meaning

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
These seven themes express a working commitment: make decisions and their
relationships inspectable while judging their effects in context. A declared
scale, a coherent role vocabulary or a repeated alignment can help a team reason
about a composition. Irregularity, asymmetry and deliberate exceptions can also
serve content and expression.

A feeling that something “looks off” can begin a useful discussion, but it does
not identify a mathematical violation or neural cause. Ask what the viewer is
trying to do, which relationship is unclear, and what concrete change might
help. Test the proposal with the content and intended audience. This manifesto
supplies no evidence that metabolic processing cost explains aesthetic pleasure
or that every permitted composition will look coherent.

Coherence is a design goal to evaluate. Shared structures can reduce accidental
variation, but they cannot make inappropriate combinations structurally
impossible without also imposing choices that may fail a particular task.

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
Rigour and creativity can support each other. A grid, ratio, type rhythm or
colour constraint can give a practitioner something productive to work with;
its value comes from the resulting composition and use, not from mathematical
regularity alone. The historical examples often invoked in this discussion ---
ancient buildings, manuscripts, paintings, posters and products --- do not prove
that every creator used the golden ratio or that one system explains enduring work.

A well-built design system can be an instrument. An instrument offers constraints
and expressive possibilities; the practitioner still chooses, listens, adjusts
and judges the result. A piano's finite keys illustrate that possibility, without
making colour and music obey the same perceptual or aesthetic laws.

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
