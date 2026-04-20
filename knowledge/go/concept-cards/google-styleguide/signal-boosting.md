---
# === CORE IDENTIFICATION ===
concept: Signal Boosting
slug: signal-boosting

# === CLASSIFICATION ===
category: commentary
subcategory: code-comments
tier: foundational

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Best Practices"
chapter_number: 4
pdf_page: null
section: "Signal boosting"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "signal boost"
  - "highlighting unusual patterns"
  - "err == nil comment"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - clarity-principle
extends: []
related:
  - documentation-conventions
  - godoc-formatting
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When should I add a comment to highlight an unusual pattern?"
  - "How do I draw attention to code that looks like a common pattern but differs subtly?"
---

# Quick Definition

Add a comment to "boost the signal" when code looks like a common pattern but actually differs subtly. The canonical example is `err == nil` (instead of the much more common `err != nil`), where a `// if NO error` comment draws attention to the difference.

# Core Definition

Sometimes code looks like something common but actually is not. A comment can "boost the signal" to draw the reader's attention to the subtle difference. The most prominent example is checking `err == nil` (success case) versus the much more common `err != nil` (error case). These two conditionals are visually hard to distinguish at a glance. Adding `// if NO error` as an inline comment immediately alerts the reader that this is the uncommon pattern.

# Prerequisites

- **clarity-principle** -- Signal boosting serves the reader's comprehension

# Key Properties

1. Add comments when code looks like a common pattern but differs subtly
2. The canonical example: `err == nil` with `// if NO error`
3. The comment draws attention to the difference, not explaining what the code does
4. This is a targeted use of comments for visual disambiguation

# Construction / Recognition

## To Apply:
1. Identify code that looks similar to a very common pattern but differs
2. Add a short inline comment highlighting the difference
3. Keep the comment minimal -- just enough to draw attention

## To Recognize:
1. Inline comments next to conditionals or expressions that look standard but are inverted or unusual
2. Comments that say what might be overlooked, not what is obvious

# Context & Application

This technique is valuable because code review and casual reading often rely on pattern recognition. When code superficially matches a common pattern but has a critical difference, readers may not notice. Signal boosting is a minimal-effort, high-value practice that prevents subtle bugs from being introduced during maintenance.

# Examples

**Example 1 -- err == nil signal boost**:

```go
// Good:
if err := doSomething(); err == nil { // if NO error
    // ...
}
```

Without the comment, this is easy to confuse with the common pattern:

```go
if err := doSomething(); err != nil {
    // ...
}
```

# Relationships

## Related
- **documentation-conventions** -- Broader documentation guidance
- **godoc-formatting** -- Formatting for larger documentation blocks
- **clarity-principle** -- Signal boosting is a direct application of clarity for the reader

## Contrasts With
(none)

# Common Errors

- **Error**: Omitting a signal-boosting comment on subtle pattern inversions
  **Correction**: Add a brief comment when code looks like a common pattern but behaves differently

- **Error**: Over-commenting obvious code as "signal boosting"
  **Correction**: Signal boosting is for subtle differences, not for restating what code clearly does

# Common Confusions

- **Confusion**: Thinking every conditional needs a comment
  **Clarification**: Only add signal-boosting comments when the code visually resembles a common pattern but differs

# Source Reference

Chapter 4: Best Practices, Section "Documentation" > "Signal boosting".

# Verification Notes

- Definition source: Directly from the "Signal boosting" section of Best Practices
- Confidence rationale: HIGH -- explicit guidance with canonical example
- Uncertainties: None
- Cross-reference status: Also referenced in the clarity-principle card's example 3
