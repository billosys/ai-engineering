---
concept: "CSS Custom Properties for Colour"
slug: "css-colour-custom-properties"
category: "design-systems"
subcategory: "colour-tokens"
tier: "intermediate"
layer: "3-implementation"
source: "Working With Colors Guide"
source_slug: "posts"
authors: "Sarah Drasner"
chapter: "Color values / Color Variables"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: "high"
aliases:
  -
    - "CSS variables for color"
    - "CSS custom properties"
    - "--color tokens"
prerequisites:
  - "rgb-colour-model"
  - "hex-colour-notation"
  - "hsl-css-syntax"
extends: []
related:
  - "hex-colour-notation"
  - "hsl-css-syntax"
contrasts_with: []
answers_questions:
  - "How do CSS custom properties enable systematic colour theming?"
rosetta_stone:
  -
    domain: "engineering"
    concept: "Dependency injection / inversion of control"
    rating: "structural"
    note: "Scoped CSS custom properties offer a structural analogy to substituting a value at a scope boundary. The analogy is limited: CSS cascade, inheritance and computed-value resolution are not dependency injection."
---

# Quick Definition

CSS custom properties hold author-defined values that participate in the cascade and inheritance; `var()` substitutes them into property values. They can support colour themes, while semantic aliases and multiple naming layers remain optional design choices.

# Core Definition

Drasner recommends storing colour variables and mapping them to semantic names. This is one optional architecture; preserve existing tokens and add aliases only when shared meaning or theme variation justifies the extra indirection. She illustrates the approach with CSS custom properties:

```css
:root {
  --brandColor: red;
}
body {
  background: var(--brandColor);
}
```

She also demonstrates a Sass equivalent using maps:

```scss
$colors: (
  mainBrand: #FA6ACC,
  secondaryBrand: #F02A52,
  highlight: #09A6E4
);
```

She notes the importance of abstract naming: "Abstract naming is sometimes useful so that if you change a variable that was representing a blue color to an orange color, you don't have to go through and rename all of your color values." She also covers `currentColor`, an inherited value that respects the cascade: "currentColor is an incredibly useful value. It respects the cascade, and is useful for extending a color value to things like box shadows, outlines, borders, or even backgrounds."

# Prerequisites

- **RGB / Hex / HSL syntax** — The values stored in custom properties use these formats
- **CSS cascade** — Custom properties inherit through the DOM tree and can be overridden per scope

# Key Properties

1. Defined with `--` prefix: `--brand-primary: #FA6ACC;`
2. Referenced with `var()`: `color: var(--brand-primary);`
3. Cascade-aware: a custom property defined on `:root` is available to all elements; overriding it on a child scope affects only that subtree
4. A project may separate palette values from semantic roles when that indirection supports real reuse or theming; a primitive value can also be used directly

At computed-value time, an inherited alias keeps the value computed on its
ancestor. For example, if `:root` sets `--ink: black` and `--alias: var(--ink)`,
a child overriding only `--ink: red` gets red from `color: var(--ink)` but
black from `color: var(--alias)`. Redeclare `--alias: var(--ink)` on that child
when its consumers should also resolve to red.

# Construction / Recognition

## To Construct/Create:
1. Define raw colour palette on `:root` with descriptive names
2. Define semantic roles referencing the palette variables
3. Apply semantic variables to component styles
4. Override on scoped selectors for theming (e.g. `[data-theme="dark"]`)

## To Identify/Recognise:
1. `var(--something)` in a CSS colour value
2. `:root { --property-name: value; }` at the top of a stylesheet

# Context & Application

- **Typical contexts**: Design systems, component libraries, dark mode theming, brand colour management
- **Common applications**: Centralising brand colour definitions; enabling dark mode by overriding a set of custom properties; propagating a component's colour context to child icons via `currentColor`

## Cross-Domain Connections

**Engineering → STRUCTURAL**: A scoped custom property can resemble supplying a different value at a scope boundary. The analogy has limits: CSS values follow cascade, inheritance and computed-value rules, rather than dependency-injection semantics.

# Examples

**Example 1** (from source): The `:root { --brandColor: red; }` / `body { background: var(--brandColor); }` pattern — the minimal demonstration of CSS custom properties for colour.

**Example 2** (from source): The Sass map equivalent — `$colors: (mainBrand: #FA6ACC, ...)` with a `color()` function — demonstrates the same semantic naming pattern in a preprocessor context.

**Example 3** (from source): `currentColor` — `div-external { color: orange; }` / `.div-internal { border: 1px solid currentColor; }` — the inherited colour keyword that propagates the cascade value automatically.

# Relationships

## Builds Upon
- **CSS cascade** — Custom properties work through the same inheritance and specificity rules as other CSS properties
- **HSL / hex / RGB syntax** — These are the value formats stored in custom properties

## Enables
- **Design token systems** — Custom properties can carry design-token values in CSS; token meaning and architecture are project-defined
- **Dark mode theming** — Override a set of custom properties on a `[data-theme="dark"]` selector
- **Component colour scoping** — A custom property override on a component root can affect inheriting descendants, subject to cascade and computed-value rules

## Related
- **CSS `currentColor`** — A keyword that resolves to the element’s `color` value for other colour properties; it is distinct from a custom property

# Common Errors

- **Error**: Assuming every palette needs semantic aliases or a fixed number of naming layers.
  **Correction**: Drasner recommends abstract names, which can help when values change meaning. Preserve established names; add aliases when shared meaning or theme variation justifies them.

# Common Confusions

- **Confusion**: CSS custom properties are the same as Sass variables.
  **Clarification**: Sass variables are resolved at compile time and produce static CSS. CSS custom properties are evaluated at runtime by the browser and can be changed dynamically via JavaScript or media queries, enabling true runtime theming.

# Source Reference

"Color Variables" section under "Color values," Working With Colors Guide (Sarah Drasner).

# Verification Notes

- Current behavior: [CSS Variables §§2–3.1](https://www.w3.org/TR/css-variables-1/) defines custom-property cascade/inheritance and computed-value substitution. A child override of a primitive does not re-evaluate an alias already inherited with its computed value; redeclare the alias at the child scope when required.

- Definition source: Direct quotes and code examples from Drasner
- Confidence rationale: High — full code examples provided; concept well-defined
- Uncertainties: Drasner's article notes (in 2016) that CSS variables "haven't made their way into Microsoft browsers" — this is now resolved; IE11 is the only holdout and is obsolete
- Cross-reference status: Not in Ottosson source
- Rosetta Stone check: Engineering/dependency-injection mapping added as rigorous
- OCR issues: None significant
