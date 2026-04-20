---
concept: Prettier Compatibility
slug: prettier-compatibility
category: compatibility
subcategory: migration
tier: intermediate
source: "Biome Documentation"
source_slug: biome
authors: "Biome Contributors"
chapter: "formatter/option-philosophy.md"
chapter_number: null
pdf_page: null
section: "Existing Options"
extraction_confidence: high
aliases:
  - Prettier Challenge
  - Prettier migration
prerequisites:
  - biome-formatter
  - opinionated-formatting
extends:
  - opinionated-formatting
related:
  - formatter-options
  - prettier-divergences
contrasts_with: []
answers_questions:
  - "How does the Biome formatter relate to Prettier?"
  - "What should I understand before migrating from Prettier?"
---

# Quick Definition

Biome aims for high compatibility with Prettier's formatting output, having achieved over 97% compatibility through the Prettier Challenge, making migration from Prettier to Biome straightforward with only a few intentional divergences.

# Core Definition

Biome's Prettier compatibility is a design goal where Biome aims to produce output that closely matches Prettier's. This was formalized through the Prettier Challenge (hosted on Algora), which required implementing all of Prettier's configuration options to achieve full compatibility. Biome is "proud to have reached such high compatibility with Prettier and make the migration path for users as painless as possible." The compatibility extends to both formatting output and the configuration option set.

# Prerequisites

- biome-formatter — understanding the Biome formatter
- opinionated-formatting — understanding why Biome limits configuration options

# Key Properties

1. **97%+ compatibility** — Biome's output matches Prettier's in the vast majority of cases
2. **Prettier Challenge** — a formal challenge that drove Biome to implement all Prettier options
3. **Options as legacy** — Prettier-compatibility options (e.g., `bracketSameLine`, `arrowParentheses`) are considered legacy, not baseline features
4. **Intentional divergences exist** — a small number of cases where Biome deliberately differs from Prettier
5. **Migration path** — designed to make switching from Prettier to Biome as painless as possible
6. **Shared philosophy** — both tools follow the same option philosophy of minimal configuration

# Construction / Recognition

When migrating from Prettier to Biome:
1. Biome supports all of Prettier's configuration options, so existing preferences can be carried over
2. Run `biome format` and compare output to identify any differences
3. Review the documented intentional divergences to understand expected differences
4. Be aware that TypeScript files formatted by Prettier's TypeScript parser may show differences that are actually Prettier bugs

# Context & Application

Prettier compatibility matters because Prettier is "by far the most popular code formatter" in the web ecosystem. Teams migrating to Biome need confidence that the switch will not cause massive diffs across their codebase. The high compatibility percentage means most code will format identically, with differences limited to documented edge cases.

# Examples

From `formatter/option-philosophy.md`:

Biome originally started with only three options: indent style, indent width, and semicolons. The Prettier Challenge prompted implementing the full set of Prettier options:

> "However, when the Prettier Challenge was announced, Biome decided to accept the challenge, which required implementing all of the configuration options that Prettier had to achieve full compatibility."

The source emphasizes that these additional options are not an endorsement of configurability: "Their existence does not indicate that more options will be added, nor should they be used as a rationale to support the existence of other options in the future."

# Relationships

## Builds Upon
- opinionated-formatting (both Biome and Prettier share this philosophy)

## Enables
- Smooth migration from Prettier to Biome
- Confidence that formatting output will be nearly identical

## Related
- formatter-options (the options that exist for Prettier compatibility)
- prettier-divergences (the intentional differences that remain)

## Contrasts With
None directly.

# Common Errors

1. **Expecting 100% identical output** — Biome has intentional divergences and will not match Prettier in every case.
2. **Assuming TypeScript formatting differences are Biome bugs** — differences that appear only with Prettier's `typescript` parser (but not `babel` or `babel-ts`) are considered Prettier bugs, not Biome incompatibilities.

# Common Confusions

1. **Compatibility vs. identity** — Biome aims to be compatible with Prettier, not a drop-in clone. It has its own parser and intentionally diverges in cases where it believes Prettier's behavior is inconsistent or incorrect.
2. **Legacy options vs. core features** — the full set of Prettier options exists in Biome, but many are considered legacy features for migration, not core Biome features.

# Source Reference

- `sources-md/biome/formatter/option-philosophy.md` — "Existing Options" section, paragraph on the Prettier Challenge
- `sources-md/biome/formatter/index.mdx` — opening paragraph on Prettier philosophy

# Verification Notes

The 97%+ compatibility figure is referenced via the Prettier Challenge blog post link in the source. The characterization of options as "legacy" and the migration emphasis are directly from the source text.
