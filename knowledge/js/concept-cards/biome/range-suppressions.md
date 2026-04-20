---
# === CORE IDENTIFICATION ===
concept: Range Suppressions
slug: range-suppressions

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
section: "Range suppressions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - biome-ignore-start/end
  - block suppressions

# === TYPED RELATIONSHIPS ===
prerequisites:
  - suppression-comments
extends:
  - suppression-comments
related:
  - inline-suppressions
  - top-level-suppressions
contrasts_with:
  - inline-suppressions
  - top-level-suppressions

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I suppress a lint rule for a line, range, or file?"
  - "What distinguishes inline, top-level, and range suppressions?"
---

# Quick Definition
Range suppressions use `biome-ignore-start` and `biome-ignore-end` to disable a lint rule or assist action for a specific range of lines within a file.

# Core Definition
Range suppressions disable a lint rule from a particular range in the file, starting from the line with the `biome-ignore-start` comment until the line with the matching `biome-ignore-end` comment. Every start comment must have a matching end comment. Range suppressions can overlap, allowing multiple rules to be suppressed independently across intersecting ranges.

# Prerequisites
- suppression-comments (the suppression system and syntax)

# Key Properties
1. Uses `biome-ignore-start` to begin and `biome-ignore-end` to close the suppressed range
2. Every `biome-ignore-start` must have a matching `biome-ignore-end`
3. Lines before the start and after the end are not suppressed
4. Multiple range suppressions can overlap independently
5. Each overlapping range tracks its own rule independently

# Construction / Recognition
Wrap the target code in start/end comments:
```js
// biome-ignore-start lint/suspicious/noDoubleEquals: reason
a == b;
c == d;
// biome-ignore-end lint/suspicious/noDoubleEquals: reason
f == g;
```

# Context & Application
Used when multiple consecutive lines need suppression but a file-wide suppression is too broad. Common for blocks of generated code, legacy code, or intentional patterns that span several lines.

# Examples
From `analyzer/suppressions.mdx`, simple range:
```js
// biome-ignore-start lint/suspicious/noDoubleEquals: reason
a == b;
c == d;
// biome-ignore-end lint/suspicious/noDoubleEquals: reason
f == g;
```
Lines 2-3 are suppressed; line 5 (`f == g`) still raises a diagnostic.

Overlapping ranges from the source:
```js
debugger;
// biome-ignore-start lint/suspicious/noDebugger: reason
debugger;
// biome-ignore-start lint/suspicious/noDoubleEquals: reason
a == b;
c == d;
// biome-ignore-end lint/suspicious/noDoubleEquals: reason
debugger;
f == g;
// biome-ignore-end lint/suspicious/noDebugger: reason
```
The `noDebugger` suppression runs from line 2 to line 10. The `noDoubleEquals` suppression runs from line 4 to line 7. After line 7, `f == g` raises a diagnostic because `noDoubleEquals` is no longer suppressed, but `debugger` at line 8 is still suppressed.

# Relationships
## Builds Upon
- suppression-comments (shared suppression syntax and engine)

## Enables
- Targeted multi-line suppression without file-wide impact

## Related
- inline-suppressions (single-line suppression)
- top-level-suppressions (file-wide suppression)

## Contrasts With
- inline-suppressions: only suppress one line, no start/end markers needed
- top-level-suppressions: suppress the entire file, no end marker needed

# Common Errors
1. Forgetting the matching `biome-ignore-end` comment — every start must have an end
2. Using different rule names in start and end comments, causing a mismatch

# Common Confusions
1. Thinking overlapping ranges interfere with each other — each range tracks its rule independently
2. Assuming the end comment line itself is suppressed — the end comment terminates the range

# Source Reference
- `sources-md/biome/analyzer/suppressions.mdx`, section "Range suppressions"

# Verification Notes
Directly extracted including the overlapping ranges example. All behavior is explicitly documented in the source.
