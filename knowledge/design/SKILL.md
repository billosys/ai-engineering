---
name: visual-design-system
description: |
  Visual design principles, colour, typography, layout, and spatial composition.
  Use when: designing pages or components, selecting or evaluating type and
  colour, setting up type scales, composing layouts, writing CSS, building
  design tokens, creating fluid designs, reviewing visual quality, designing
  wayfinding, theming, or answering a visual design question.
license: MIT
metadata:
  version: "1.0.5"
  hermes:
    tags: [design, css, color, typography, layout, oklch, cube-css, utopia]
    category: web-frontend
---

# Visual Design — Principles for Context-Led Web Work

This skill offers a compositional approach to visual design: make relationships
visible, let content and tasks shape the arrangement, and use browser layout
capabilities with care. The guides provide methods and examples; the adopting
project's brief and supplied identity remain authoritative.

## Begin with the project's brief

Before making consequential choices, identify the audience, task and content;
reading conditions; supplied name, logo, tokens, typefaces, imagery and fixed
decisions; platform, viewport and input needs; language and scripts; relevant
accessibility targets and user preferences; and any unresolved constraints.
This is a short context aid, not a required questionnaire. Ask only when an
answer could change the design or its behavior. Otherwise state the assumption,
mark unknowns, and offer a reversible proposal with its reason.

Keep existing identity and semantics where they fit. Do not infer colours,
fonts, token names, ratios, themes, sites or endpoints from this skill. A
project may choose any of them independently. If it supplies no direction,
develop candidates for the particular task and label them as proposals.

## Choose a guide

Load the guide that fits the question. Links are relative to this packaged
entrypoint.

| Guide | Method | Load it when |
|---|---|---|
| [Design as Engineering](guides/design.md) | Principles, relationships, constraints and trade-offs, with room for contextual exceptions. | Reviewing or explaining a design decision. |
| [Foundations of Design](guides/foundations-of-design.md) | Research context, source analysis, technical concepts and cross-domain discussion. | Looking for evidence or conceptual background; check each claim's scope. |
| [Colour](guides/colour.md) | Start from supplied identity and colour roles, then choose and check actual pairs. | Selecting colours, mapping existing tokens or reviewing states and themes. |
| [Type](guides/type.md) | Start from scripts, content and reading conditions, then assess roles, fonts, scale and axes. | Choosing typefaces, fallbacks, hierarchy or variable-font settings. |
| [Layout](guides/layout.md) | Compose from spatial relationships and intrinsic sizing; use fluid values or breakpoints as the content requires. | Structuring pages, spacing, containers or responsive behavior. |
| [Breaking the Layout Monoculture](guides/breaking-the-layout-monoculture.md) | Context-led ways to vary familiar patterns, plus wayfinding and interaction considerations. | A page needs a distinct composition, exploration or navigation. |

## Routes by task

| Task | Guides |
|---|---|
| Design a page | [Layout](guides/layout.md), [Colour](guides/colour.md), [Type](guides/type.md) |
| Design a homepage or portal | [Breaking the Layout Monoculture](guides/breaking-the-layout-monoculture.md), [Layout](guides/layout.md), then relevant colour and type guidance |
| Choose colours | [Colour](guides/colour.md), then the perception discussion in [Design as Engineering](guides/design.md) |
| Set up typography | [Type](guides/type.md), then relevant layout guidance |
| Build or revise tokens | [Colour](guides/colour.md), [Foundations](guides/foundations-of-design.md), and the adopting project's token contract |
| Review a page | [Design as Engineering](guides/design.md), then relevant layout, colour, type and accessibility checks |
| Add transitions or animation | [Breaking the Layout Monoculture](guides/breaking-the-layout-monoculture.md), with target support and preference checks |
| Design navigation or wayfinding | [Breaking the Layout Monoculture](guides/breaking-the-layout-monoculture.md) |
| Investigate a mathematical or historical claim | [Foundations of Design](guides/foundations-of-design.md) and its cited sources |

## Principles to guide judgment

These are useful questions, not universal laws. Apply them when they fit the
content, user needs and technical context; record a reason when an exception
better serves the task.

| Principle | Useful question |
|---|---|
| Proportion | Would a declared scale or relationship make hierarchy easier to maintain? A ratio is one option; optical and content-led adjustments are valid. |
| Perception | Which properties matter to the viewer, and what should be evaluated in the rendered result? No color model or unit guarantees the outcome. |
| Role | Would purpose-based names help maintain the existing token system? Preserve established names and mappings when they already express the project's semantics. |
| Constraint | Which local constraints make this task easier to use or maintain? Do not prescribe a number of fonts, hues or spacing values. |
| Coherence | What should remain consistent, and where should expression vary for audience, content, medium or task? |
| Proximity | Do spacing and grouping communicate the actual relationships between items? Adjust where content or interaction calls for it. |
| Invariants | Which relationships should remain stable across instances, and which values need contextual review? |

## A vocabulary for composition

Stack, Box, Center, Cluster, Sidebar, Switcher, Cover, Grid, Frame, Reel,
Imposter, Icon and Container are useful spatial patterns described in [Layout](guides/layout.md).
They are a vocabulary for composition, not a required inventory: use the
patterns that help the content and supplied components.

## CSS composition examples

These snippets illustrate reusable layout relationships. Review their numeric
values with actual content. Any referenced custom properties must be defined
by the adopting project; these examples prescribe no spacing system, palette,
font or token architecture.

### Stack Primitive

```css
.stack { display: flex; flex-direction: column; gap: var(--space-s); }
```

### Sidebar Primitive

```css
.with-sidebar {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-l);
}
.with-sidebar > .sidebar { flex-basis: 20rem; flex-grow: 1; }
.with-sidebar > .main { flex-basis: 0; flex-grow: 999; min-inline-size: 55%; }
```

### Intrinsic Grid (no column count)

```css
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 250px), 1fr));
  gap: var(--space-s-m);
}
```

## Colour and type at a glance

For colour, begin with supplied values and map the needed surface, text,
interaction, border and state roles. A primitive/semantic/component token
architecture is optional; it must not displace the adopting project's existing
semantics. Check complete rendered foreground/background pairs, including
states, compositing and gamut on the target.

**Colour-space conversions combine linear and nonlinear stages**. Linear stages use 3×3 matrices; a complete conversion can also include sRGB decoding and componentwise cube roots.

For type, begin with language, script, content and reading conditions. Assign
roles from the hierarchy the task needs, evaluate candidate families and
fallbacks against real text, then choose any scale or available axes. Inspect
optical fit and rendered behavior. The guides supply no named font roster or
required family count.

## Fluid values and layout

Fluid interpolation can reduce abrupt changes where the content benefits from
it. Choose and declare the values and interval for the project that uses them.
A geometric scale is optional and does not make line length, wrapping or layout
correct at every width. Start with intrinsic sizing, then use a container or
viewport query when measured content, user settings or interaction requires a
discrete change. Test the target sizes and preferences.

## Review

- Does the hierarchy reflect the task and content?
- Are supplied names, assets, tokens and fixed choices preserved?
- Do colour pairs and interaction states remain legible after rendering,
  transparency, overlays and gamut mapping?
- Do selected typefaces cover the actual scripts and content, and do fallbacks
  remain usable?
- Do grouping and measures fit the content?
- Are fluid and intrinsic behaviors checked where they will be used? Are
  breakpoints or optical exceptions explained by an observed need?
- Are motion, focus, keyboard use, reflow and user preferences addressed where
  they affect the interaction?

These questions support review; answering them does not by itself establish
accessibility conformance or fresh-context usability.
