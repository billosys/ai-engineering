---
concept: Function Formatting
slug: function-formatting
category: language
subcategory: code-formatting
tier: intermediate
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Style Decisions"
chapter_number: 3
pdf_page: null
section: "Function formatting"
extraction_confidence: high
aliases:
  - function signature formatting
  - function argument formatting
prerequisites:
  - go-function-basics
related:
  - literal-formatting
  - conditionals-and-loops
contrasts_with: []
answers_questions:
  - "How should long Go function signatures be formatted?"
  - "Should Go function calls be broken across multiple lines?"
  - "How should long format strings with arguments be split?"
---

# Quick Definition

Keep function signatures on a single line to avoid indentation confusion. For call sites, prefer keeping arguments on one line or factoring out local variables. When wrapping is necessary, group arguments by semantic meaning rather than arbitrary column limits. Avoid inline comments on individual arguments.

# Core Definition

> "The signature of a function or method declaration should remain on a single line to avoid indentation confusion." -- Google Go Style Guide, "Function formatting"

> "Similarly, function and method calls should not be separated based solely on line length." -- Google Go Style Guide, "Function formatting"

# Prerequisites

- Understanding of Go function declarations and calls
- Familiarity with `gofmt` formatting conventions

# Key Properties

1. **Signatures on one line**: Function/method declarations should stay on a single line to prevent wrapped parameters from being confused with the function body.
2. **Factor out local variables**: Shorten long call sites by extracting parameters into named locals.
3. **No arbitrary line breaks**: Do not break function calls solely based on line length.
4. **Semantic grouping**: When wrapping is necessary, group arguments by meaning (e.g., coordinates together) rather than by column width.
5. **Avoid inline arg comments**: Use option structs or better documentation instead of comments on individual arguments.
6. **Format strings**: Keep the format string intact on one line; put arguments on subsequent lines grouped semantically.

# Construction / Recognition

**Bad -- signature wrapped causing indentation confusion:**

```go
func (r *SomeType) SomeLongFunctionName(foo1, foo2, foo3 string,
    foo4, foo5, foo6 int) {
    foo7 := bar(foo1)
    // ...
}
```

**Good -- factor out local variables:**

```go
local := helper(some, parameters, here)
good := foo.Call(list, of, parameters, local)
```

**Good -- long call on one line:**

```go
good := foo.Call(long, list, of, parameters, all, on, one, line)
```

**Bad -- arbitrary line breaks:**

```go
bad := foo.Call(long, list, of, parameters,
    with, arbitrary, line, breaks)
```

**Good -- use option struct instead of inline comments:**

```go
good := server.New(ctx, server.Options{Port: 42})
```

**Bad -- inline comment on argument:**

```go
bad := server.New(
    ctx,
    42, // Port
)
```

**Good -- semantic grouping when wrapping is needed:**

```go
canvas.RenderHeptagon(fillColor,
    x0, y0, vertexColor0,
    x1, y1, vertexColor1,
    x2, y2, vertexColor2,
)
```

**Good -- format string intact, arguments grouped semantically:**

```go
log.Warningf("Database key (%q, %d, %q) incompatible in transaction started by (%q, %d, %q)",
    currentCustomer, currentOffset, currentKey,
    txCustomer, txOffset, txKey)
```

**Bad -- broken format string with arbitrary wrapping:**

```go
log.Warningf("Database key (%q, %d, %q) incompatible in"+
    " transaction started by (%q, %d, %q)",
    currentCustomer, currentOffset, currentKey, txCustomer,
    txOffset, txKey)
```

# Context & Application

Long function signatures create indentation confusion because wrapped parameters align with the function body. This makes it hard to visually distinguish "where does the signature end and the body begin." Factoring parameters into local variables or using option structs solves the problem at the call site. For format strings, keeping the template intact on one line helps readers understand the output format at a glance.

# Examples

See Construction / Recognition above for the complete set of source examples.

# Relationships

- **literal-formatting**: Parallel formatting rules for composite literals.
- **conditionals-and-loops**: Formatting rules that share the indentation-confusion concern.

# Common Errors

1. Breaking function signatures across multiple lines, confusing parameters with body code.
2. Splitting function calls at arbitrary column boundaries instead of semantic boundaries.
3. Using inline comments on arguments instead of option structs.
4. Splitting format strings across lines with string concatenation.

# Common Confusions

- **When wrapping is allowed**: Wrapping is always permissible if it aids understanding, such as grouping coordinates. The rule is against arbitrary wrapping.
- **Long lines are okay**: A long single-line call is preferred over an artificially broken multi-line call.

# Source Reference

Google Go Style Guide, "Style Decisions" chapter, "Function formatting" section.

# Verification Notes

Confidence: high. All guidance and code examples are directly from the source text.
