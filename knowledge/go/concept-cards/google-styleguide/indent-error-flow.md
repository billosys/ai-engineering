---
concept: Indent Error Flow
slug: indent-error-flow
category: error-handling
subcategory: code-structure
tier: foundational
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Style Decisions"
chapter_number: 3
pdf_page: null
section: "Indent error flow"
extraction_confidence: high
aliases:
  - line of sight
  - happy path indentation
  - error-first flow
prerequisites:
  - returning-errors
  - handle-errors-decisions
related:
  - conditionals-and-loops
contrasts_with: []
answers_questions:
  - "Should error handling go in the if block or the else block in Go?"
  - "What is 'line of sight' reading in Go?"
  - "How should the happy path be indented in Go?"
---

# Quick Definition

Handle errors first in the `if` block (with `return`, `continue`, etc.), then let the happy path continue at minimal indentation without an `else` clause. This "line of sight" pattern makes normal code flow immediately visible.

# Core Definition

> "Handle errors before proceeding with the rest of your code. This improves the readability of the code by enabling the reader to find the normal path quickly. This same logic applies to any block which tests a condition then ends in a terminal condition (e.g., `return`, `panic`, `log.Fatal`)." -- Google Go Style Guide, "Indent error flow"

> "Code that runs if the terminal condition is not met should appear after the `if` block, and should not be indented in an `else` clause." -- Google Go Style Guide, "Indent error flow"

# Prerequisites

- Understanding of Go's `if` statement and early returns
- Familiarity with Go error handling conventions

# Key Properties

1. **Error first**: Handle the error case inside the `if` block with a terminal statement.
2. **No else for happy path**: The normal code follows the `if` block at the same indentation level.
3. **Line of sight**: A reader can scan the left edge of the code to follow the happy path.
4. **If-with-init caveat**: When a variable is used for many lines, prefer declaring it separately rather than using `if x, err := f(); err != nil` with an `else` block.

# Construction / Recognition

**Good -- error first, happy path unindented:**

```go
if err != nil {
    // error handling
    return // or continue, etc.
}
// normal code
```

**Bad -- happy path buried in else:**

```go
if err != nil {
    // error handling
} else {
    // normal code that looks abnormal due to indentation
}
```

**Good -- variable used across many lines, declared separately:**

```go
x, err := f()
if err != nil {
    // error handling
    return
}
// lots of code that uses x
// across multiple lines
```

**Bad -- if-with-init forcing else for variable scope:**

```go
if x, err := f(); err != nil {
    // error handling
    return
} else {
    // lots of code that uses x
    // across multiple lines
}
```

# Context & Application

The "line of sight" principle means that a reader scanning the leftmost indentation level of a function sees only the happy path. Error handling and edge cases are indented one level and terminate early. This dramatically improves readability in functions with multiple sequential operations that can each fail.

# Examples

See Construction / Recognition above for the complete set of source examples.

# Relationships

- **handle-errors-decisions**: The broader principle of deliberate error handling.
- **conditionals-and-loops**: Related formatting guidance for conditional statements.

# Common Errors

1. Putting the happy path inside an `else` block, increasing indentation.
2. Using `if-with-init` when the variable is needed across many lines, forcing an `else`.
3. Nesting multiple levels of error checks instead of returning early.

# Common Confusions

- **When to use if-with-init**: It is appropriate when the variable is only needed for a few lines within the `if` block itself. When the variable is used extensively afterward, declare it separately.
- **Applies beyond errors**: This pattern applies to any terminal condition check (`return`, `panic`, `log.Fatal`, `continue`), not just error handling.

# Source Reference

Google Go Style Guide, "Style Decisions" chapter, "Indent error flow" section. See also Go Tip #1: Line of Sight.

# Verification Notes

Confidence: high. All guidance and code examples are directly from the source text.
