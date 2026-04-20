---
concept: Avoid Using Built-In Names
slug: avoid-using-built-in-names
category: code-safety
subcategory: naming
tier: foundational
source: "Uber Go Style Guide"
source_slug: uber-style
authors: "Prashant Varanasi, Simon Newton"
chapter: "Guidelines"
chapter_number: 2
pdf_page: null
section: "Avoid Using Built-In Names"
extraction_confidence: high
aliases:
  - don't shadow predeclared identifiers
  - avoid shadowing built-ins
prerequisites:
  - go-language-basics
related:
  - error-naming
  - avoid-embedding-types-in-public-structs
contrasts_with: []
answers_questions:
  - "What are predeclared identifiers in Go?"
  - "Why should you avoid using built-in names as variable or field names?"
---

# Quick Definition

Do not use Go's predeclared identifiers (like `error`, `string`, `len`, `copy`, `new`, etc.) as variable, field, or function names. Reusing these names shadows the original within the current scope, introducing confusing code and potentially latent bugs that are hard to detect with grep.

# Core Definition

> "The Go language specification outlines several built-in, predeclared identifiers that should not be used as names within Go programs." -- Uber Go Style Guide, "Avoid Using Built-In Names"

> "Depending on context, reusing these identifiers as names will either shadow the original within the current lexical scope (and any nested scopes) or make affected code confusing. In the best case, the compiler will complain; in the worst case, such code may introduce latent, hard-to-grep bugs." -- Uber Go Style Guide, "Avoid Using Built-In Names"

# Prerequisites

- Knowledge of Go's predeclared identifiers (types: `bool`, `int`, `string`, `error`; functions: `len`, `cap`, `make`, `new`, `copy`, `append`, `delete`, `close`, `panic`, `recover`; constants: `true`, `false`, `iota`; zero value: `nil`)
- Understanding of Go's lexical scoping rules

# Key Properties

1. **Compiler may not warn**: Go's compiler does not always produce errors for shadowing predeclared identifiers; the code may compile and run with subtle bugs.
2. **Scope-based shadowing**: The shadowed identifier is inaccessible within the current scope and all nested scopes.
3. **Grep ambiguity**: Using `error` as a field name makes searching for error-related code unreliable.
4. **Tooling support**: `go vet` and similar tools can detect shadowing of predeclared identifiers.

# Construction / Recognition

**Bad -- shadowing `error` and `string`:**

```go
var error string
// `error` shadows the builtin

// or

func handleErrorMessage(error string) {
    // `error` shadows the builtin
}
```

**Good -- using descriptive names:**

```go
var errorMessage string
// `error` refers to the builtin

// or

func handleErrorMessage(msg string) {
    // `error` refers to the builtin
}
```

**Bad -- field names matching built-in types:**

```go
type Foo struct {
    // While these fields technically don't
    // constitute shadowing, grepping for
    // `error` or `string` strings is now
    // ambiguous.
    error  error
    string string
}

func (f Foo) Error() error {
    // `error` and `f.error` are
    // visually similar
    return f.error
}

func (f Foo) String() string {
    // `string` and `f.string` are
    // visually similar
    return f.string
}
```

**Good -- descriptive field names:**

```go
type Foo struct {
    // `error` and `string` strings are
    // now unambiguous.
    err error
    str string
}

func (f Foo) Error() error {
    return f.err
}

func (f Foo) String() string {
    return f.str
}
```

# Context & Application

Go's predeclared identifiers are not reserved words -- the language allows them to be redeclared. This is a deliberate design choice for flexibility, but it creates a footgun. In practice, shadowing `error` as a parameter name is the most common violation. The resulting code compiles and runs, but the `error` type is no longer accessible in that scope, and the code becomes confusing to read and search.

# Examples

See Construction / Recognition above for the source examples.

# Relationships

- **error-naming**: Defines proper naming conventions for error values and types, which avoids collisions with the built-in `error` identifier.
- **avoid-embedding-types-in-public-structs**: Both address unintended API surface, though from different angles.

# Common Errors

1. Using `error` as a parameter name: `func foo(error string)` shadows the `error` type.
2. Using `string` as a field name in a struct, creating visual ambiguity with the built-in `string` type.
3. Using `copy` or `len` as local variable names, hiding the built-in functions.

# Common Confusions

- **Shadowing vs struct fields**: Struct fields named `error` or `string` do not technically shadow the built-in in the package scope, but they create grep ambiguity and visual confusion. The guide discourages both.
- **Compiler silence**: Developers may assume that if Go compiles the code, it is correct. The compiler does not treat predeclared identifier shadowing as an error.

# Source Reference

Uber Go Style Guide, "Guidelines" chapter, "Avoid Using Built-In Names" section.

# Verification Notes

Confidence: high. The guidance, the distinction between true shadowing and grep ambiguity, and all code examples are directly from the source. The note about `go vet` support is also from the source.
