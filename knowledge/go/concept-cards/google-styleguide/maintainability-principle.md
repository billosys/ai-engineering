---
# === CORE IDENTIFICATION ===
concept: Maintainability Principle
slug: maintainability-principle

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
  - "maintainable code"
  - "ease of modification"
  - "code maintainability"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - clarity-principle
extends: []
related:
  - simplicity-principle
  - concision-principle
  - consistency-principle
  - least-mechanism
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What makes Go code maintainable?"
  - "How should APIs be designed for future growth?"
  - "Why should Go code minimize dependencies?"
---

# Quick Definition

Maintainable code is easy to modify correctly. APIs grow gracefully, abstractions map to the problem structure, dependencies are minimized, and tests ensure promised behaviors are maintained with clear diagnostics on failure.

# Core Definition

Maintainability is the fourth-ranked style principle. Code is edited many more times than it is written, so readable code must serve both the reader trying to understand it and the programmer who needs to change it. Maintainable code: (1) is easy for a future programmer to modify correctly, (2) has APIs structured to grow gracefully, (3) chooses abstractions that map to the problem structure (not the code structure), (4) avoids unnecessary coupling and unused features, (5) has comprehensive tests with clear, actionable diagnostics. It also avoids hiding critical details in easy-to-overlook places and uses predictable names so maintainers can find what they need.

# Prerequisites

- **clarity-principle** -- Clarity is key to maintainability; code must be understandable before it can be modified correctly

# Key Properties

1. Easy for a future programmer to modify correctly
2. APIs structured so they can grow gracefully
3. Abstractions map to the problem structure, not the code structure
4. Avoids unnecessary coupling and features that are not used
5. Comprehensive test suite with clear, actionable failure diagnostics
6. Does not hide critical details in easy-to-overlook places
7. Uses predictable names for variables, methods, and functions
8. Minimizes implicit and explicit dependencies

# Construction / Recognition

## To Apply:
1. Design APIs that can evolve without breaking existing consumers
2. Choose abstractions that reflect the problem domain
3. Use predictable, consistent names for identical concepts across methods and functions
4. Write tests that provide clear diagnostics on failure
5. Avoid depending on internal or undocumented behavior
6. Make critical logic explicit rather than hiding it in helper functions or subtle syntax

## To Recognize:
1. Single-character differences that change behavior fundamentally (e.g., `=` vs `:=`)
2. Complex boolean expressions where a negation is easy to miss
3. Helper functions that hide edge cases critical to correctness

# Context & Application

The source provides specific examples of hidden critical details. Using `=` instead of `:=` in `if user, err = db.UserByID(userID); err != nil` completely changes whether `user` is a new local variable or an outer variable being reassigned. A negation buried in a complex leap year expression (`!(year%100 == 0)`) is easy to miss. Both should be rewritten more explicitly or annotated with comments. Interfaces are a powerful tool but impose a cost on maintainers who must understand the underlying implementation.

# Examples

**Example 1 -- Hidden critical detail, made explicit (from source)**:

```go
// Good:
u, err := db.UserByID(userID)
if err != nil {
    return fmt.Errorf("invalid origin user: %s", err)
}
user = u
```

Separating the assignment from the error check makes the reassignment of `user` explicit and visible.

**Example 2 -- Breaking down complex expressions (from source)**:

```go
// Good:
// Gregorian leap years aren't just year%4 == 0.
// See https://en.wikipedia.org/wiki/Leap_year#Algorithm.
var (
    leap4   = year%4 == 0
    leap100 = year%100 == 0
    leap400 = year%400 == 0
)
leap := leap4 && (!leap100 || leap400)
```

Breaking the expression into named components makes each condition visible and the overall logic easier to verify.

# Relationships

## Related
- **simplicity-principle** -- Simple code is easier to maintain
- **concision-principle** -- Concise code highlights what matters, aiding maintenance
- **consistency-principle** -- Consistent code is easier to modify because patterns are predictable
- **least-mechanism** -- Fewer dependencies reduce maintenance burden

# Common Errors

- **Error**: Using `:=` and `=` interchangeably without considering scope implications
  **Correction**: Make variable scoping explicit; separate declarations from error checks when reassignment is involved

- **Error**: Hiding edge-case logic inside helper functions without documentation
  **Correction**: Document edge cases at the call site or in the helper function's documentation

# Common Confusions

- **Confusion**: Thinking maintainability means avoiding all abstraction
  **Clarification**: Abstraction is fine when it maps to the problem structure and provides clear benefit. The concern is unnecessary or misleading abstraction.

- **Confusion**: Believing interfaces always improve maintainability
  **Clarification**: Interfaces remove context and require maintainers to understand underlying implementations. Use them when the abstraction provides sufficient benefit.

# Source Reference

Chapter 2: Guide, Section "Style principles" > "Maintainability".

# Verification Notes

- Definition source: Directly from the "Maintainability" section of the Style Guide
- Confidence rationale: HIGH -- explicitly defined with detailed bullet list and code examples
- Uncertainties: None
- Cross-reference status: Related slugs verified against planned extractions
