---
# === CORE IDENTIFICATION ===
concept: Suppression Comments
slug: suppression-comments

# === CLASSIFICATION ===
category: analyzer
subcategory: suppressions
tier: foundational

# === PROVENANCE ===
source: "Biome Documentation"
source_slug: biome
authors: "Biome Contributors"
chapter: "analyzer/suppressions.mdx"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - suppressions
  - biome-ignore comments

# === TYPED RELATIONSHIPS ===
prerequisites:
  - biome
extends: []
related:
  - biome-linter
  - biome-assist
  - inline-suppressions
  - top-level-suppressions
  - range-suppressions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a suppression comment?"
  - "How do I suppress a lint rule for a line, range, or file?"
---

# Quick Definition
Suppression comments are special code comments that disable Biome lint rules or assist actions for specific lines, ranges, or entire files.

# Core Definition
The Biome analyzer is the foundation of both the linter and assist tools, and they share the same suppression engine. Suppression comments allow turning off a lint rule or assist action for a specific line of code, a range, or an entire file. The suppression system uses three comment prefixes: `biome-ignore` (inline), `biome-ignore-all` (top-level/file-wide), and `biome-ignore-start`/`biome-ignore-end` (range).

# Prerequisites
Requires understanding of Biome as a toolchain and either the linter or assist tool.

# Key Properties
1. Shared by both the linter and assist tools via the analyzer engine
2. Three scope levels: inline (next line), top-level (entire file), and range (start to end)
3. Suppression comment format: `biome-ignore <category>[/group[/rule]]: <explanation>`
4. Categories include `lint`, `assist`, and `syntax`
5. Specificity increases with slashes: `lint` < `lint/suspicious` < `lint/suspicious/noDebugger`
6. Some rules support suppression with values in parentheses, e.g., `(foo)`
7. An explanation after the colon is required

# Construction / Recognition
The general syntax is:
```js
// biome-ignore lint: <explanation>
// biome-ignore lint/suspicious: <explanation>
// biome-ignore lint/suspicious/noDebugger: <explanation>
// biome-ignore-all lint: <explanation>
// biome-ignore-start lint: <explanation>
// biome-ignore-end lint: <explanation>
```

The category (`lint`, `assist`, `syntax`) follows the prefix, then optionally a group and rule name separated by slashes.

# Context & Application
Used when a specific rule or action should not apply to certain code — for example, generated files, intentional use of deprecated patterns, or code that legitimately violates a rule.

# Examples
From `analyzer/suppressions.mdx`:

Inline suppression disabling `noDebugger` for one line:
```js
// biome-ignore lint/suspicious/noDebugger: reason
debugger;
```

Top-level suppression for an entire file:
```js
// biome-ignore-all lint/suspicious/noDebugger: reason
debugger;
debugger;
```

Range suppression:
```js
// biome-ignore-start lint/suspicious/noDoubleEquals: reason
a == b;
c == d;
// biome-ignore-end lint/suspicious/noDoubleEquals: reason
f == g;
```

# Relationships
## Builds Upon
- biome (the shared analyzer engine)

## Enables
- inline-suppressions, top-level-suppressions, range-suppressions (the three suppression scopes)

## Related
- biome-linter (suppressions disable lint rules)
- biome-assist (suppressions disable assist actions)

## Contrasts With
None directly; suppression comments are the only mechanism for in-code rule disabling.

# Common Errors
1. Forgetting the explanation after the colon — it is required
2. Using the wrong category (e.g., `lint` when trying to suppress an `assist` action)
3. Not being specific enough — suppressing all of `lint` when only one rule should be suppressed

# Common Confusions
1. Thinking suppression comments only work for the linter — they work identically for assist actions
2. Not realizing the specificity hierarchy: `lint` suppresses everything, `lint/suspicious` suppresses a group, `lint/suspicious/noDebugger` suppresses one rule

# Source Reference
- `sources-md/biome/analyzer/suppressions.mdx`

# Verification Notes
All information directly from the suppressions documentation. The shared engine between linter and assist is explicitly stated.
