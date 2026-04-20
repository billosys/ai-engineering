---
concept: Biome Formatter
slug: biome-formatter
category: formatter
subcategory: null
tier: foundational
source: "Biome Documentation"
source_slug: biome
authors: "Biome Contributors"
chapter: "formatter/index.mdx"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - biome format
  - "biome format command"
prerequisites: []
extends: []
related:
  - formatter-options
  - opinionated-formatting
  - format-suppression
  - prettier-compatibility
contrasts_with:
  - prettier-divergences
answers_questions:
  - "What is the Biome formatter?"
  - "How do I format code with Biome?"
---

# Quick Definition

Biome is an opinionated code formatter that supports multiple languages and follows a minimal-options philosophy similar to Prettier, enforcing consistent style with very few configurable knobs.

# Core Definition

Biome's formatter is a tool that automatically reformats source code according to a fixed set of style rules. It supports multiple languages (JavaScript, TypeScript, JSX, JSON, CSS, and more) and is designed to eliminate debates over code style by providing very few configuration options. It follows the same option philosophy as Prettier: most formatting decisions are made by the tool, not the user.

# Prerequisites

Foundational concept with no prerequisites.

# Key Properties

1. **Opinionated** — enforces a single canonical style rather than being fully configurable
2. **Multi-language** — supports JavaScript, TypeScript, JSX, TSX, JSON, CSS, and other web languages
3. **Prettier-compatible** — aims for high compatibility with Prettier output (97%+)
4. **Minimal configuration** — deliberately limits the number of formatting options to avoid bike-shedding
5. **CLI and LSP** — usable from the command line and through editor integrations via the Language Server Protocol

# Construction / Recognition

To check formatting without modifying files:
```
biome format ./src
```

To apply formatting (write changes to disk):
```
biome format --write ./src
```

The command accepts a list of files and directories. When using shell globs, be aware that the shell expands them, which may have performance costs and compatibility differences across shells.

# Context & Application

The Biome formatter is used in JavaScript/TypeScript projects as a replacement for or alternative to Prettier. It is typically configured via a `biome.json` configuration file, which ensures consistency between CLI usage and LSP-based editor formatting. As of v1.9, Biome also supports loading `.editorconfig` files.

# Examples

From `formatter/index.mdx`, the CLI usage:
- `biome format ./src` — checks formatting and emits text differences
- `biome format --write ./src` — applies new formatting to files

The formatter separates language-agnostic options (indent style, indent width, line width) from language-specific options (semicolons, quote style, trailing commas) in the configuration file.

# Relationships

## Builds Upon
None (foundational concept).

## Enables
- formatter-options (configuring the formatter's behavior)
- format-suppression (selectively disabling formatting)
- opinionated-formatting (the philosophy behind the tool)

## Related
- prettier-compatibility (migration and compatibility goals)

## Contrasts With
- prettier-divergences (cases where Biome intentionally differs from Prettier)

# Common Errors

1. **Forgetting `--write`** — running `biome format ./src` only checks formatting; it does not modify files. Pass `--write` to apply changes.
2. **Shell glob expansion** — passing globs like `./src/**/*.test.{js,ts}` depends on the shell's expansion behavior; some shells do not support recursive globs or alternation.
3. **Config mismatch** — using CLI flags without a `biome.json` file can cause the CLI and LSP to apply different formatting rules.

# Common Confusions

1. **Biome is not just a formatter** — Biome is a broader toolchain that includes linting, but the `biome format` command specifically handles formatting.
2. **Not fully Prettier-identical** — while highly compatible, Biome has intentional divergences from Prettier's output in certain edge cases.

# Source Reference

- `sources-md/biome/formatter/index.mdx` — CLI section, Options section

# Verification Notes

Extracted directly from the formatter overview page. All CLI commands and configuration examples come from the source text.
