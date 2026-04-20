---
# === CORE IDENTIFICATION ===
concept: Concision Principle
slug: concision-principle

# === CLASSIFICATION ===
category: principles
subcategory: style-principles
tier: foundational

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Guide"
chapter_number: 2
pdf_page: null
section: "Style principles"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "conciseness in Go"
  - "signal-to-noise ratio"
  - "high signal code"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - clarity-principle
  - simplicity-principle
extends: []
related:
  - naming-principles
  - maintainability-principle
contrasts_with:
  - clarity-principle

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does concise Go code look like?"
  - "How do I improve the signal-to-noise ratio in my Go code?"
  - "What gets in the way of concise Go code?"
---

# Quick Definition

Concise Go code has a high signal-to-noise ratio. The relevant details are easy to discern, and naming and structure guide the reader through them. Repetitive code, extraneous syntax, opaque names, and unnecessary abstraction are noise to be minimized.

# Core Definition

Concision is the third-ranked style principle. Concise code surfaces the most salient details by removing noise: repetitive code, extraneous syntax, opaque names, unnecessary abstraction, and excessive whitespace. Table-driven testing is a good example of concisely factoring out common code while highlighting the important differences in each case. Understanding and using common Go idioms (like the `if err != nil` pattern) also maintains high signal-to-noise ratio, since readers can quickly recognize familiar patterns. When code subtly deviates from a common pattern, the signal should be "boosted" with a comment.

# Prerequisites

- **clarity-principle** -- Clarity is the higher-priority principle; concision must not sacrifice it
- **simplicity-principle** -- Simplicity is ranked above concision

# Key Properties

1. High signal-to-noise ratio
2. Relevant details are easy to discern
3. Naming and structure guide the reader
4. Noise sources: repetitive code, extraneous syntax, opaque names, unnecessary abstraction, whitespace
5. Common idioms maintain signal (e.g., `if err != nil`)
6. Subtle deviations from common patterns should be boosted with comments

# Construction / Recognition

## To Apply:
1. Factor out repetitive code (e.g., use table-driven tests)
2. Remove extraneous syntax that adds no meaning
3. Use clear, descriptive names rather than opaque abbreviations
4. Use common Go idioms so readers recognize patterns instantly
5. Boost signal with comments when deviating subtly from familiar patterns

## To Recognize:
1. Repetitive code blocks that differ in only small ways -- candidates for factoring
2. Boilerplate syntax that could be simplified
3. Subtle deviations from common patterns without explanatory comments

# Context & Application

Concision complements clarity but can conflict with it. Removing too much can make code cryptic. The goal is to make important details apparent, not to minimize line count. The choice of what to include in a table-driven test, for example, affects how easy the table is to understand -- include only the fields that differ meaningfully. When code looks like the common `err != nil` pattern but actually checks `err == nil`, a comment like `// if NO error` boosts the signal.

# Examples

**Example 1 -- Common error-handling idiom (from source)**:

```go
// Good:
if err := doSomething(); err != nil {
    // ...
}
```

This pattern is so familiar that readers process it instantly, maintaining high signal.

**Example 2 -- Boosting signal for a subtle difference (from source)**:

```go
// Good:
if err := doSomething(); err == nil { // if NO error
    // ...
}
```

The comment calls attention to the fact that this checks for the *absence* of an error, which is the opposite of the common pattern.

# Relationships

## Related
- **naming-principles** -- Good naming is key to high signal-to-noise ratio
- **maintainability-principle** -- Concise code is often easier to maintain

## Contrasts With
- **clarity-principle** -- Excessive concision can reduce clarity; clarity always takes priority

# Common Errors

- **Error**: Removing code to the point where the logic is unclear
  **Correction**: Concision serves clarity, not the other way around. If removing code makes intent ambiguous, keep it.

- **Error**: Not commenting subtle deviations from common idioms
  **Correction**: When code looks like a common pattern but differs subtly, add a comment to boost the signal

# Common Confusions

- **Confusion**: Thinking concision means minimizing lines of code
  **Clarification**: Concision means maximizing signal-to-noise ratio. Sometimes more lines (e.g., breaking up a complex expression) can be more concise in terms of clarity.

- **Confusion**: Believing concision is the top priority
  **Clarification**: Concision is ranked third, after clarity and simplicity. It must not override either.

# Source Reference

Chapter 2: Guide, Section "Style principles" > "Concision".

# Verification Notes

- Definition source: Directly from the "Concision" section of the Style Guide
- Confidence rationale: HIGH -- explicitly defined with examples
- Uncertainties: None
- Cross-reference status: Related slugs verified against planned extractions
