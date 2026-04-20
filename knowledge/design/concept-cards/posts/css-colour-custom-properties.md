---
concept: CSS Custom Properties for Colour
slug: css-colour-custom-properties
category: design-systems
subcategory: colour-tokens
tier: intermediate
layer: 3-implementation
source: "Working With Colors Guide"
source_slug: posts
authors: "Sarah Drasner"
chapter: "Color values / Color Variables"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - ["CSS variables for color", "CSS custom properties", "--color tokens"]
prerequisites:
  - rgb-colour-model
  - hex-colour-notation
  - hsl-css-syntax
extends:
  - []
related:
  - hex-colour-notation
  - hsl-css-syntax
contrasts_with:
  - []
answers_questions:
  - "How do CSS custom properties enable systematic colour theming?"
rosetta_stone:
  - domain: engineering
    concept: "Dependency injection / inversion of control"
    rating: rigorous
    note: "CSS custom properties cascade through the DOM in the same way injected dependencies propagate through a dependency graph. A custom property defined on :root is 'injected' into all descendants; overriding it on a child component changes all colour references within that subtree \u2014 analogous to injecting a different implementation at a scope boundary."
---

# Quick Definition

CSS custom properties (CSS variables) allow colour values to be defined once, given semantic names, and reused throughout a stylesheet \u2014 enabling systematic colour theming and centralised palette management.

# Core Definition

Drasner introduces CSS custom properties for colour: "A good practice is to store color variables and never use them directly, mapping them instead to other variables with more semantic naming schemes. CSS has native variables, like:" showing the example:

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

- **RGB / Hex / HSL syntax** \u2014 The values stored in custom properties use these formats
- **CSS cascade** \u2014 Custom properties inherit through the DOM tree and can be overridden per scope

# Key Properties

1. Defined with `--` prefix: `--brand-primary: #FA6ACC;`
2. Referenced with `var()`: `color: var(--brand-primary);`
3. Cascade-aware: a custom property defined on `:root` is available to all elements; overriding it on a child scope affects only that subtree
4. Separation of palette from semantic roles: define raw colours as `--color-blue-500: #3B82F6;` and semantic roles as `--color-text-link: var(--color-blue-500);`

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

**Engineering \u2192 RIGOROUS**: CSS custom properties implement a form of dependency injection through the cascade. A colour value defined at `:root` is "injected" into every element that references it via `var()`. Overriding the custom property on a parent element changes the injected value for the entire subtree, without requiring any change to the leaf components \u2014 identical to how dependency injection enables configuration changes at system boundaries without modifying dependent components.

# Examples

**Example 1** (from source): The `:root { --brandColor: red; }` / `body { background: var(--brandColor); }` pattern \u2014 the minimal demonstration of CSS custom properties for colour.

**Example 2** (from source): The Sass map equivalent \u2014 `$colors: (mainBrand: #FA6ACC, ...)` with a `color()` function \u2014 demonstrates the same semantic naming pattern in a preprocessor context.

**Example 3** (from source): `currentColor` \u2014 `div-external { color: orange; }` / `.div-internal { border: 1px solid currentColor; }` \u2014 the inherited colour keyword that propagates the cascade value automatically.

# Relationships

## Builds Upon
- **CSS cascade** \u2014 Custom properties work through the same inheritance and specificity rules as other CSS properties
- **HSL / hex / RGB syntax** \u2014 These are the value formats stored in custom properties

## Enables
- **Design token systems** \u2014 Custom properties are the native CSS implementation of design tokens
- **Dark mode theming** \u2014 Override a set of custom properties on a `[data-theme="dark"]` selector
- **Component colour scoping** \u2014 Override custom properties on a component root to re-theme a subtree

## Related
- **CSS currentColor** \u2014 The cascading colour keyword that further leverages the CSS custom property pattern

# Common Errors

- **Error**: Naming custom properties with literal colour names (e.g. `--blue: #3B82F6`).
  **Correction**: Drasner warns: "if you change a variable that was representing a blue color to an orange color, you don't have to go through and rename all of your color values" \u2014 use semantic names (`--color-primary`) or at least scale names (`--color-blue-500`) that don't encode the colour in the name.

# Common Confusions

- **Confusion**: CSS custom properties are the same as Sass variables.
  **Clarification**: Sass variables are resolved at compile time and produce static CSS. CSS custom properties are evaluated at runtime by the browser and can be changed dynamically via JavaScript or media queries, enabling true runtime theming.

# Source Reference

"Color Variables" section under "Color values," Working With Colors Guide (Sarah Drasner).

# Verification Notes

- Definition source: Direct quotes and code examples from Drasner
- Confidence rationale: High \u2014 full code examples provided; concept well-defined
- Uncertainties: Drasner's article notes (in 2016) that CSS variables "haven't made their way into Microsoft browsers" \u2014 this is now resolved; IE11 is the only holdout and is obsolete
- Cross-reference status: Not in Ottosson source
- Rosetta Stone check: Engineering/dependency-injection mapping added as rigorous
- OCR issues: None significant
