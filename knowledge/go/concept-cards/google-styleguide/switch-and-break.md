---
concept: Switch and Break
slug: switch-and-break
category: language
subcategory: control-flow
tier: foundational
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Style Decisions"
chapter_number: 3
pdf_page: null
section: "switch and break"
extraction_confidence: high
aliases:
  - break in switch
  - labeled break
  - implicit break
prerequisites:
  - go-control-flow-basics
related:
  - conditionals-and-loops
contrasts_with: []
answers_questions:
  - "Do Go switch cases need break statements?"
  - "How do you break out of a for loop from inside a switch in Go?"
  - "What is a labeled break in Go?"
---

# Quick Definition

In Go, `switch` cases break implicitly -- do not add redundant `break` statements. Use a comment to clarify the purpose of empty cases. When a `switch` is inside a `for` loop, use a labeled `break` to exit the loop, since an unlabeled `break` only exits the `switch`.

# Core Definition

> "Do not use `break` statements without target labels at the ends of `switch` clauses; they are redundant. Unlike in C and Java, `switch` clauses in Go automatically break, and a `fallthrough` statement is needed to achieve the C-style behavior." -- Google Go Style Guide, "switch and break"

# Prerequisites

- Understanding of Go's `switch` statement
- Knowledge of Go's `for` loop
- Familiarity with `fallthrough` keyword

# Key Properties

1. **Implicit break**: Go switch cases automatically break at the end; no explicit `break` is needed.
2. **`fallthrough` for C-style**: Use `fallthrough` to explicitly fall into the next case.
3. **Comment empty cases**: Use a comment rather than `break` to clarify an intentionally empty case.
4. **Labeled break for loops**: `break` inside a switch within a `for` loop only exits the switch. Use a label on the `for` to break out of the loop.

# Construction / Recognition

**Good -- no redundant break, comment for empty case:**

```go
switch x {
case "A", "B":
    buf.WriteString(x)
case "C":
    // handled outside of the switch statement
default:
    return fmt.Errorf("unknown value: %q", x)
}
```

**Bad -- redundant break statements:**

```go
switch x {
case "A", "B":
    buf.WriteString(x)
    break // this break is redundant
case "C":
    break // this break is redundant
default:
    return fmt.Errorf("unknown value: %q", x)
}
```

**Important -- break in switch does not exit enclosing loop:**

```go
for {
    switch x {
    case "A":
        break // exits the switch, not the loop
    }
}
```

**Good -- labeled break to exit the loop:**

```go
loop:
    for {
        switch x {
        case "A":
            break loop // exits the loop
        }
    }
```

# Context & Application

Developers coming from C or Java often add `break` to every switch case out of habit. In Go, this is unnecessary noise because implicit breaking is the language default. The labeled-break pattern is essential knowledge for any code that combines `switch` with `for` loops, since the unlabeled `break` only exits the innermost breakable statement (the switch), not the loop.

# Examples

See Construction / Recognition above for the complete set of source examples.

# Relationships

- **conditionals-and-loops**: Related formatting guidance for switch and loop statements.

# Common Errors

1. Adding redundant `break` at the end of switch cases.
2. Using `break` in a switch inside a loop, expecting to exit the loop.
3. Using an empty case without a comment explaining the intent.

# Common Confusions

- **`break` scope**: `break` exits the innermost `for`, `switch`, or `select` -- in a switch-inside-a-loop, that means the switch, not the loop.
- **`fallthrough` is explicit**: Unlike C, you must opt in to fallthrough behavior.

# Source Reference

Google Go Style Guide, "Style Decisions" chapter, "switch and break" section.

# Verification Notes

Confidence: high. All rules and code examples are directly from the source text.
