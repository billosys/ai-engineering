---
# === CORE IDENTIFICATION ===
concept: Clarity Principle
slug: clarity-principle

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
  - "readability principle"
  - "code clarity"
  - "clarity in Go"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - simplicity-principle
  - concision-principle
  - maintainability-principle
  - consistency-principle
  - naming-principles
contrasts_with:
  - concision-principle

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the most important style principle in the Google Go Style Guide?"
  - "Should code be optimized for the writer or the reader?"
  - "What are the two facets of clarity in Go code?"
---

# Quick Definition

Clarity is the core goal of readability: code's purpose and rationale must be clear to the reader, not the author. It is the highest-priority style principle, ranked above simplicity, concision, maintainability, and consistency.

# Core Definition

Clarity is the first and most important of the five style principles. It means producing code that is clear to the reader -- not the author. Clarity has two distinct facets: (1) what the code is actually doing, and (2) why the code is doing what it does. Clarity is achieved primarily through effective naming, helpful commentary, and efficient code organization. Comments should explain "why" rather than "what" when the code can speak for itself. Code that stands out from the uniform codebase should do so for a good reason (typically performance), and that reason should be documented.

# Prerequisites

- **go-style-document-hierarchy** -- Understanding that this principle comes from the canonical Style Guide

# Key Properties

1. Clarity is viewed through the lens of the **reader**, not the author
2. It is more important that code be easy to **read** than easy to **write**
3. Two facets: what the code does, and why it does it
4. Achieved through effective naming, helpful commentary, and efficient code organization
5. Ranked first among five style principles (clarity > simplicity > concision > maintainability > consistency)
6. Comments should explain why, not restate what the code already says

# Construction / Recognition

## To Apply:
1. Use descriptive variable names when the purpose is not immediately obvious
2. Add commentary explaining "why" when the rationale is not evident from the code
3. Break up complex code with whitespace, comments, or extraction into separate functions
4. Avoid redundant comments that merely restate what the code does
5. Document any code that deviates from common patterns, especially for performance

## To Recognize:
1. Code where a reader unfamiliar with the codebase can understand both what and why
2. Comments that add value by explaining rationale, not restating logic
3. Variable and function names that are self-describing

# Context & Application

Clarity is the top priority because Go is designed to be straightforward to read. When code is unclear, invest time to make the purpose clearer for future readers -- through better names, comments, whitespace, or refactoring into more modular functions. The standard library exemplifies this principle: `strings.Cut` is only four lines but dramatically improves clarity and correctness at call sites. Adding unnecessary commentary can actually obscure code, so balance is key.

# Examples

**Example 1 -- Explaining "why" for business logic**:

When code contains nuances a reader might not know (e.g., an access control check distinguishing actual users from impersonators), add commentary explaining the rationale rather than just restating the conditional logic.

**Example 2 -- Letting code speak for itself**:

Allow the code to be self-describing through good symbol names rather than adding redundant comments. A well-named function like `UserByID` needs less explanation than a comment saying "// gets a user by their ID".

**Example 3 -- Boosting signal for subtle differences (from source)**:

```go
// Good:
if err := doSomething(); err == nil { // if NO error
    // ...
}
```

When code looks similar to a common pattern but differs subtly (e.g., checking `err == nil` instead of `err != nil`), add a comment to draw attention to the difference.

# Relationships

## Related
- **simplicity-principle** -- Simplicity supports clarity; simple code is easier to understand
- **concision-principle** -- Concision supports clarity by raising signal-to-noise ratio
- **maintainability-principle** -- Clear code is easier to maintain correctly
- **consistency-principle** -- Consistent code is easier to read because patterns are familiar
- **naming-principles** -- Good naming is the primary mechanism for achieving clarity

## Contrasts With
- **concision-principle** -- Concision can conflict with clarity; brevity must not sacrifice understanding

# Common Errors

- **Error**: Writing code that is clear to the author but opaque to future readers
  **Correction**: Always evaluate clarity from the reader's perspective, not yours

- **Error**: Adding comments that restate what the code already says
  **Correction**: Let self-describing code speak for itself; add comments that explain why

# Common Confusions

- **Confusion**: Thinking clarity means more comments everywhere
  **Clarification**: Excessive commentary can obscure code. Clarity comes from good names, structure, and targeted comments explaining rationale.

- **Confusion**: Believing clever or compact code is clearer
  **Clarification**: Clarity prioritizes the reader's comprehension, which often means simpler, more explicit code over clever constructs.

# Source Reference

Chapter 2: Guide, Section "Style principles" > "Clarity".

# Verification Notes

- Definition source: Directly from the "Clarity" section of the Style Guide
- Confidence rationale: HIGH -- the source explicitly defines clarity as the core goal with detailed guidance
- Uncertainties: None
- Cross-reference status: Related slugs verified against planned extractions
