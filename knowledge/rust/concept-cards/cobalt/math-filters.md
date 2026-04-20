---
# === CORE IDENTIFICATION ===
concept: Math Filters
slug: math-filters

# === CLASSIFICATION ===
category: liquid-filters
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Cobalt Static Site Generator Documentation"
source_slug: cobalt
authors: "Cobalt contributors (cobalt-org)"
chapter: "Liquid Standard Library"
chapter_number: null
pdf_page: null
section: "Math Filters"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "numeric filters"
  - "arithmetic filters"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - output-tags
  - liquid-template-language
extends: []
related:
  - string-filters
  - array-filters
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Liquid filter?"
---

# Quick Definition

Math filters are Liquid filters that perform arithmetic and numeric operations on values. They include basic arithmetic (addition, subtraction, multiplication, division, modulo), rounding operations, and value clamping.

# Core Definition

Math filters are part of the Liquid standard library implemented in the `liquid_lib` crate (source: `stdlib/filters/math/`). They operate on numeric values and are applied using the pipe character in output tags. The liquid crate's own example demonstrates math filters: `"Liquid! {{num | minus: 2}}"` with `num: 4` produces `"Liquid! 2"`. Math filters handle both integer and floating-point values. (Source: liquid_lib stdlib math filters, liquid crate rustdoc)

# Prerequisites

- **[Output Tags](/concept-cards/cobalt/output-tags.md)** -- Filters are applied within output tags.
- **[Liquid Template Language](/concept-cards/cobalt/liquid-template-language.md)** -- Understanding the filter pipe syntax.

# Key Properties

The following math filters are available in the liquid_lib standard library:

**Basic Arithmetic:**
1. **`plus`**: Adds a number. `{{ 4 | plus: 2 }}` produces `6`.
2. **`minus`**: Subtracts a number. `{{ 4 | minus: 2 }}` produces `2`.
3. **`times`**: Multiplies by a number. `{{ 4 | times: 2 }}` produces `8`.
4. **`divided_by`**: Divides by a number. `{{ 10 | divided_by: 2 }}` produces `5`.
5. **`modulo`**: Returns the remainder of division. `{{ 10 | modulo: 3 }}` produces `1`.

**Rounding:**
6. **`ceil`**: Rounds up to the nearest integer. `{{ 4.1 | ceil }}` produces `5`.
7. **`floor`**: Rounds down to the nearest integer. `{{ 4.9 | floor }}` produces `4`.
8. **`round`**: Rounds to the nearest integer (or specified decimal places). `{{ 4.5 | round }}` produces `5`.

**Value Operations:**
9. **`abs`**: Returns the absolute value. `{{ -5 | abs }}` produces `5`.
10. **`at_least`**: Clamps to a minimum value. `{{ 3 | at_least: 5 }}` produces `5`.
11. **`at_most`**: Clamps to a maximum value. `{{ 10 | at_most: 5 }}` produces `5`.

# Construction / Recognition

## To Construct/Create:
1. Apply a math filter using the pipe after a numeric value: `{{ value | filter_name: parameter }}`.
2. Chain multiple math filters: `{{ value | plus: 10 | divided_by: 2 }}`.

## To Identify/Recognize:
1. Look for pipe characters followed by math filter names in output tags.
2. Math filters typically have numeric parameters.

# Context & Application

- **Typical contexts**: Performing calculations in templates, computing values for display.
- **Common applications**: Calculating reading time, computing percentages, adjusting values for display, clamping values to ranges.

# Examples

**Example 1** (source: liquid crate rustdoc): Basic arithmetic:
```liquid
Liquid! {{ num | minus: 2 }}
```
With `num: 4`, produces: `Liquid! 2`.

**Example 2** (source: Liquid Standard Library): Clamping a value:
```liquid
{{ page.data.rating | at_least: 1 | at_most: 5 }}
```
Ensures the rating is between 1 and 5.

**Example 3** (source: Liquid Standard Library): Chaining arithmetic:
```liquid
{{ page.data.word_count | divided_by: 200 | ceil }}
```
Estimates reading time in minutes (assuming 200 words per minute).

# Relationships

## Builds Upon
- **[Output Tags](/concept-cards/cobalt/output-tags.md)** -- Filters are applied within output tags.
- **[Liquid Template Language](/concept-cards/cobalt/liquid-template-language.md)** -- Filter pipe syntax.

## Enables
- Numeric computation in templates.

## Related
- **[String Filters](/concept-cards/cobalt/string-filters.md)** -- Filters for text operations.
- **[Array Filters](/concept-cards/cobalt/array-filters.md)** -- Filters for array operations.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Using `divided_by` with integer arguments and expecting a float result.
  **Correction**: Integer division may truncate. Use a float divisor (e.g., `divided_by: 2.0`) if a decimal result is needed.

# Common Confusions

- **Confusion**: Confusing `at_least` and `at_most`.
  **Clarification**: `at_least` sets a minimum (returns the greater of the two values). `at_most` sets a maximum (returns the lesser of the two values).

# Source Reference

Liquid Standard Library, math filter module. Source: liquid_lib rustdoc (stdlib/filters/math/); liquid crate example.

# Verification Notes

- Definition source: liquid_lib stdlib math filter structs and liquid crate example
- Confidence rationale: All filters verified in the liquid_lib stdlib struct list.
- Uncertainties: None for filter names; specific parameter details may vary.
- Cross-reference status: Verified against liquid_lib stdlib index and liquid crate example.
