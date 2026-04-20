---
# === CORE IDENTIFICATION ===
concept: Inline Suppressions
slug: inline-suppressions

# === CLASSIFICATION ===
category: analyzer
subcategory: suppressions
tier: intermediate

# === PROVENANCE ===
source: "Biome Documentation"
source_slug: biome
authors: "Biome Contributors"
chapter: "analyzer/suppressions.mdx"
chapter_number: null
pdf_page: null
section: "Inline suppressions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - biome-ignore
  - next-line suppressions

# === TYPED RELATIONSHIPS ===
prerequisites:
  - suppression-comments
extends:
  - suppression-comments
related:
  - top-level-suppressions
  - range-suppressions
contrasts_with:
  - top-level-suppressions
  - range-suppressions

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I suppress a lint rule for a line, range, or file?"
  - "What distinguishes inline, top-level, and range suppressions?"
---

# Quick Definition
Inline suppressions use `biome-ignore` to disable a lint rule or assist action for the next line of code only.

# Core Definition
Inline suppressions disable a lint rule for the next line of code. The suppression comment uses the `biome-ignore` prefix and applies only to the immediately following line. Code beyond that line is unaffected and will still raise diagnostics if it violates the rule.

# Prerequisites
- suppression-comments (the suppression system and syntax)

# Key Properties
1. Uses the `biome-ignore` prefix
2. Applies only to the next line of code
3. The line after the suppressed line is not affected
4. Follows the standard suppression syntax: `biome-ignore <category>[/group[/rule]]: <explanation>`

# Construction / Recognition
Place a `biome-ignore` comment on the line immediately before the code to suppress:
```js
// biome-ignore lint/suspicious/noDebugger: reason
debugger;
```

# Context & Application
Used for one-off exceptions where a single line legitimately needs to bypass a rule. This is the most targeted and common form of suppression.

# Examples
From `analyzer/suppressions.mdx`:
```js
// biome-ignore lint/suspicious/noDebugger: reason
debugger;
debugger;
```
The first `debugger` at line 2 is suppressed; the second `debugger` at line 3 still raises a diagnostic.

# Relationships
## Builds Upon
- suppression-comments (shared suppression syntax and engine)

## Enables
- Fine-grained, per-line control over rule enforcement

## Related
- top-level-suppressions (file-wide suppression)
- range-suppressions (multi-line suppression)

## Contrasts With
- top-level-suppressions: suppress an entire file, not just one line
- range-suppressions: suppress a range of lines between start/end markers

# Common Errors
1. Placing the suppression comment two or more lines above the target — it only applies to the very next line
2. Expecting it to suppress multiple consecutive lines

# Common Confusions
1. Thinking inline suppression covers a block or scope — it only covers the next line

# Source Reference
- `sources-md/biome/analyzer/suppressions.mdx`, section "Inline suppressions"

# Verification Notes
Directly extracted from the inline suppressions section. The next-line-only behavior is explicitly documented.
