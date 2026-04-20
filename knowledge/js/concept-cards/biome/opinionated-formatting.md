---
concept: Opinionated Formatting
slug: opinionated-formatting
category: formatter
subcategory: philosophy
tier: intermediate
source: "Biome Documentation"
source_slug: biome
authors: "Biome Contributors"
chapter: "formatter/option-philosophy.md"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - formatter option philosophy
  - automatic style guide
prerequisites:
  - biome-formatter
extends:
  - biome-formatter
related:
  - formatter-options
  - prettier-compatibility
contrasts_with: []
answers_questions:
  - "What distinguishes the formatter's opinionated approach from configurable formatters?"
  - "Why does Biome have so few formatting options?"
---

# Quick Definition

Biome's opinionated formatting philosophy holds that there is one correct way to format code, and the formatter should enforce that style universally with minimal configuration, eliminating debates over style so teams can focus on substance.

# Core Definition

Biome is an opinionated formatter that "assumes there is only one correct way to format things and will enforce that style at all times." From this perspective, Biome functions as "its own automatic style guide, not a tool for implementing other style guides." The philosophy deliberately resists adding new configuration options to prevent trivial bike-shedding discussions about formatting preferences. The existing option set is considered stable and not open for additions.

# Prerequisites

- biome-formatter — understanding what the Biome formatter is

# Key Properties

1. **Single canonical style** — no matter the project or setup, Biome-formatted code always looks the same
2. **Bike-shedding elimination** — by refusing to make style configurable, debates over formatting vanish from code reviews
3. **Ecosystem-wide benefit** — consistent formatting across projects makes it easier to move between codebases and helps newcomers recognize patterns
4. **Options are legacy, not baseline** — options like `bracketSameLine` and `arrowParentheses` exist for Prettier compatibility, not because Biome endorses configurable style
5. **Style is stable** — the formatting output is considered stable; changes may occur but will be applied universally, not made configurable
6. **Shared with Prettier** — Biome explicitly follows Prettier's Option Philosophy

# Construction / Recognition

The opinionated approach is recognized by:
- Very few configuration options in `biome.json`
- Feature requests for new formatting options being closed without discussion
- The formatter producing identical output regardless of who runs it (given the same version)

# Context & Application

The opinionated philosophy is the conceptual foundation of Biome's formatter design. It shapes every decision about what to make configurable and what to hardcode. Teams adopting Biome accept the tool's style in exchange for eliminating all formatting-related discussion.

The benefits described in the source:
- "All of the discussions about where spaces should go, whether a line should be broken out, whether a line should be indented, and so many more simply vanish."
- "Code reviews become free of re-formatting requests and cyclical debates."
- "All it takes is trust that Biome does its best to format code cleanly, legibly, and consistently."

# Examples

From `formatter/option-philosophy.md`:

Biome started with a strict subset of options targeting the most contentious style guidelines: indent styles (tabs vs. spaces), indent widths (2 or 4), and enforced semicolons. This was "considered sufficient enough to address most people's needs."

When the Prettier Challenge was announced, Biome implemented all of Prettier's configuration options to achieve full compatibility. However, "Biome still shares Prettier's philosophy about these options and considers them a legacy feature for compatibility rather than a baseline feature set."

Prettier's own documentation on legacy options: "[these] are not the type of options we're happy to have. They cause a lot of bike-shedding in teams, and we're sorry for that."

# Relationships

## Builds Upon
- biome-formatter

## Enables
- The minimal option set in formatter-options
- Consistent behavior across projects

## Related
- formatter-options (the concrete options that exist)
- prettier-compatibility (the compatibility goal that forced additional options)

## Contrasts With
Fully configurable formatters (e.g., ESLint's stylistic rules) where every aspect of formatting can be individually controlled.

# Common Errors

1. **Requesting new options** — the source explicitly states that "requests for additional configuration options are not likely to be considered and may be closed without discussion."
2. **Using legacy options as justification** — the existence of options like `bracketSameLine` does not indicate that more options will be added; they exist only for Prettier migration.

# Common Confusions

1. **Opinionated does not mean unconfigurable** — a few options exist (indent style, line width, semicolons), but they are deliberately limited.
2. **Style changes vs. new options** — Biome may change its formatting output in future versions, but these changes are applied universally rather than exposed as new options.
3. **Biome's style vs. Prettier's style** — Biome aims to match Prettier's output closely, with only a few intentional divergences.

# Source Reference

- `sources-md/biome/formatter/option-philosophy.md` — entire document, especially "Existing Options" and "New Options" sections

# Verification Notes

All quoted passages are taken directly from the source text. The philosophy is explicitly and thoroughly documented in the option-philosophy page.
