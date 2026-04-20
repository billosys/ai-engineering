---
concept: Format Suppression
slug: format-suppression
category: formatter
subcategory: inline directives
tier: intermediate
source: "Biome Documentation"
source_slug: biome
authors: "Biome Contributors"
chapter: "formatter/index.mdx"
chapter_number: null
pdf_page: null
section: "Ignore Code"
extraction_confidence: high
aliases:
  - biome-ignore format
  - biome-ignore-all format
  - formatter suppression comments
prerequisites:
  - biome-formatter
extends:
  - biome-formatter
related:
  - formatter-options
contrasts_with: []
answers_questions:
  - "How do I prevent the Biome formatter from reformatting specific code?"
  - "How do I suppress formatting for an entire file?"
---

# Quick Definition

Biome provides two suppression comment directives to skip formatting: `biome-ignore format` suppresses formatting for the next syntax node, and `biome-ignore-all format` (placed at the top of a file) suppresses formatting for the entire file.

# Core Definition

Format suppression allows developers to opt specific code or entire files out of Biome's automatic formatting. Two comment directives are available:

1. **Node-level suppression** — `// biome-ignore format: <reason>` placed immediately before a syntax node prevents the formatter from reformatting that node.
2. **File-level suppression** — `// biome-ignore-all format: <reason>` placed at the top of a file prevents the formatter from reformatting anything in that file.

Both directives require a reason after the colon, documenting why the code is excluded from formatting.

# Prerequisites

- biome-formatter — understanding the Biome formatter and when it runs

# Key Properties

1. **Two granularity levels** — node-level (`biome-ignore format`) and file-level (`biome-ignore-all format`)
2. **Reason required** — both forms use the syntax `biome-ignore[-all] format: reason`
3. **Comment-based** — uses standard language comments (e.g., `//` in JavaScript)
4. **File-level must be at the top** — `biome-ignore-all` must appear at the top of the file to take effect
5. **Preserves original formatting** — suppressed code is printed verbatim, exactly as written

# Construction / Recognition

To suppress formatting for a single node:
```js
const expr =
  // biome-ignore format: the array should not be formatted
  [
    (2 * n) / (r - l),
    0,
    (r + l) / (r - l),
    -1,
    0,
  ];
```

To suppress formatting for an entire file:
```js
// biome-ignore-all format: generated file

const expr1 =
  [
    (2 * n) / (r - l),
    0,
    (r + l) / (r - l),
    -1,
    0,
  ];
```

# Context & Application

Format suppression is useful when the formatted output is less readable than the hand-formatted original. Common use cases include:

- Matrix or tabular data expressed as arrays
- Generated files that should not be reformatted
- Code where specific alignment conveys meaning

# Examples

From `formatter/index.mdx`:

- File-level: `// biome-ignore-all format: generated file` placed at the top prevents the entire file's arrays from being reformatted.
- Node-level: `// biome-ignore format: the array should not be formatted` placed before an array literal keeps its manual formatting intact.

# Relationships

## Builds Upon
- biome-formatter

## Enables
Fine-grained control over which code the formatter modifies.

## Related
- formatter-options (global configuration as opposed to inline directives)

## Contrasts With
None directly, though this is analogous to `// prettier-ignore` in Prettier.

# Common Errors

1. **Missing reason** — the colon and reason text are required; `// biome-ignore format` alone (without `: reason`) may not work as expected.
2. **Wrong placement of `biome-ignore-all`** — file-level suppression must be at the top of the file; placing it mid-file will not suppress the entire file.
3. **Applying to the wrong node** — `biome-ignore format` applies to the immediately following syntax node, not the entire block or statement surrounding it.

# Common Confusions

1. **`biome-ignore format` vs. `biome-ignore lint`** — the `format` keyword specifically targets the formatter; `lint` targets the linter. They are separate suppression systems.
2. **Suppression is not configuration** — suppression comments are per-instance overrides, not project-wide settings. For project-wide exclusions, use the `ignore` array in `biome.json`.

# Source Reference

- `sources-md/biome/formatter/index.mdx` — "Ignore Code" section, "Ignore an entire file" subsection, "Ignore nodes" subsection

# Verification Notes

Both suppression forms and their examples are taken directly from the source text. The requirement for a reason and the placement constraint for file-level suppression are explicitly documented.
