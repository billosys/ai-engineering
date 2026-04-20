---
concept: Reduce Scope of Variables
slug: reduce-scope-of-variables
category: style
subcategory: variable-scope
tier: foundational
source: "Uber Go Style Guide"
source_slug: uber-style
authors: "Prashant Varanasi, Simon Newton"
chapter: "Style"
chapter_number: 4
pdf_page: null
section: "Reduce Scope of Variables"
extraction_confidence: high
aliases:
  - minimize variable scope
  - if-init statement
prerequisites: []
extends: []
related:
  - local-variable-declarations
contrasts_with: []
answers_questions:
  - "How do I reduce variable scope in Go?"
  - "What is an if-init statement in Go?"
---

# Quick Definition

Minimize the scope of variables and constants by declaring them as close to their use as possible. Use if-init statements (e.g., `if err := f(); err != nil`) to confine variables to the block where they are needed, but do not reduce scope if it conflicts with reducing nesting.

# Core Definition

The Uber Go Style Guide recommends reducing the scope of variables and constants wherever possible. The primary mechanism is the if-init statement, which declares a variable within the `if` clause itself, limiting its lifetime to that block. However, this should not be applied when the result is needed outside the `if` block, as that leads to increased nesting and reduced readability.

Constants that are only used in a single function should be declared inside that function rather than at package scope.

# Prerequisites

- Understanding of Go's block scoping rules
- Familiarity with if-init statement syntax

# Key Properties

1. **If-init statements**: Use `if err := f(); err != nil { ... }` to scope `err` to the if block when it is not needed afterward.
2. **Do not over-scope-reduce**: If the variable is needed after the if block, declare it before the if statement to avoid nesting.
3. **Local constants**: Constants used only in one function should be declared inside that function, not at package level.
4. **Balance with nesting**: Scope reduction should not conflict with the "Reduce Nesting" guideline.

# Construction / Recognition

**Good -- if-init scopes err to the block:**

```go
if err := os.WriteFile(name, data, 0644); err != nil {
  return err
}
```

**Bad -- err declared in wider scope than needed:**

```go
err := os.WriteFile(name, data, 0644)
if err != nil {
  return err
}
```

**Good -- variable needed outside if, declared before:**

```go
data, err := os.ReadFile(name)
if err != nil {
  return err
}

if err := cfg.Decode(data); err != nil {
  return err
}

fmt.Println(cfg)
return nil
```

**Bad -- over-scoping forces nesting:**

```go
if data, err := os.ReadFile(name); err == nil {
  err = cfg.Decode(data)
  if err != nil {
    return err
  }

  fmt.Println(cfg)
  return nil
} else {
  return err
}
```

**Good -- local constants:**

```go
func Bar() {
  const (
    defaultPort = 8080
    defaultUser = "user"
  )
  fmt.Println("Default port", defaultPort)
}
```

# Context & Application

This principle applies throughout function bodies. It is particularly useful for error handling, where `err` variables are often only needed for a single check. The balance with nesting is critical: if reducing scope adds nesting levels, prefer the wider scope for readability.

# Examples

See Construction / Recognition above for complete examples from the source.

# Relationships

- **local-variable-declarations**: Scope reduction builds on the `:=` vs `var` conventions for declaring variables.

# Common Errors

1. Declaring variables at function scope when they are only used in a single if block.
2. Using if-init to reduce scope when the result is needed later, forcing awkward nesting with else blocks.
3. Declaring constants at package level when they are only used in one function.

# Common Confusions

- **Scope reduction vs nesting reduction**: These two guidelines can conflict. When they do, prefer reducing nesting over reducing scope.
- **If-init with multiple return values**: When a function returns both a result and an error, use if-init only if the result is not needed outside the if block.

# Source Reference

Uber Go Style Guide, "Style" chapter, "Reduce Scope of Variables" section.

# Verification Notes

Confidence: high. All rules and code examples are directly from the source text with explicit Bad/Good comparisons.
