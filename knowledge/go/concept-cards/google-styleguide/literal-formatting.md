---
concept: Literal Formatting
slug: literal-formatting
category: language
subcategory: composite-literals
tier: intermediate
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Style Decisions"
chapter_number: 3
pdf_page: null
section: "Literal formatting"
extraction_confidence: high
aliases:
  - composite literal style
  - struct literal formatting
  - field names in literals
prerequisites:
  - go-struct-basics
related:
  - nil-slices-decisions
  - function-formatting
contrasts_with: []
answers_questions:
  - "When must field names be used in Go struct literals?"
  - "What are the rules for matching braces in Go literals?"
  - "When can braces be cuddled in Go slice literals?"
  - "Should repeated type names be omitted in Go literals?"
  - "When should zero-value fields be omitted?"
---

# Quick Definition

Use composite literal syntax instead of building values field-by-field. Require field names for types from external packages; match closing braces to opening indentation; cuddle braces only when inner values are also literals and indentation matches; omit repeated type names in slices/maps; and omit zero-value fields when clarity is preserved.

# Core Definition

> "Where possible, this literal syntax should be used instead of building values field-by-field." -- Google Go Style Guide, "Literal formatting"

> "Struct literals must specify field names for types defined outside the current package." -- Google Go Style Guide, "Field names"

> "The closing half of a brace pair should always appear on a line with the same amount of indentation as the opening brace." -- Google Go Style Guide, "Matching braces"

> "Repeated type names may be omitted from slice and map literals." -- Google Go Style Guide, "Repeated type names"

> "Zero-value fields may be omitted from struct literals when clarity is not lost as a result." -- Google Go Style Guide, "Zero-value fields"

# Prerequisites

- Understanding of Go composite literal syntax
- Knowledge of Go struct, slice, and map types

# Key Properties

1. **Field names required for external types**: Struct literals for types from other packages must use field names; positional initialization couples to internal field ordering.
2. **Field names optional for local types**: Package-local types may omit field names, but use them for clarity with many fields.
3. **Matching braces**: Closing brace must be at the same indentation level as the opening brace. Do not put a closing brace on the same line as a value in a multi-line literal.
4. **Cuddled braces**: Dropping whitespace between braces is only allowed when indentation matches AND inner values are also literals (not variables).
5. **Omit repeated type names**: In slice and map literals, omit redundant type repetition (use `gofmt -s`).
6. **Omit zero-value fields**: Leave out fields set to their zero value when it does not hurt clarity. Table-driven test structs benefit from explicit field names so zero-value fields can be omitted entirely.

# Construction / Recognition

**Good -- field names for external package types:**

```go
r := csv.Reader{
    Comma:           ',',
    Comment:         '#',
    FieldsPerRecord: 4,
}
```

**Bad -- positional initialization of external type:**

```go
r := csv.Reader{',', '#', 4, false, false, false, false}
```

**Good -- matching braces in multi-line literal:**

```go
good := []*Type{
    {Key: "multi"},
    {Key: "line"},
}
```

**Bad -- closing brace on wrong line:**

```go
bad := []*Type{
    {Key: "multi"},
    {Key: "line"}}
```

**Good -- cuddled braces (inner values are literals, indentation matches):**

```go
good := []*Type{{
    Field: "value",
}, {
    Field: "value",
}}
```

**Good -- omit repeated type names:**

```go
good := []*Type{
    {A: 42},
    {A: 43},
}
```

**Bad -- repeated type names:**

```go
repetitive := []*Type{
    &Type{A: 42},
    &Type{A: 43},
}
```

**Good -- omit zero-value fields:**

```go
ldb := leveldb.Open("/my/table", &db.Options{
    BlockSize:       1<<16,
    ErrorIfDBExists: true,
})
```

**Bad -- specifying all zero-value fields:**

```go
ldb := leveldb.Open("/my/table", &db.Options{
    BlockSize:            1<<16,
    ErrorIfDBExists:      true,
    BlockRestartInterval: 0,
    Comparer:             nil,
    Compression:          nil,
    FileSystem:           nil,
    FilterPolicy:         nil,
    MaxOpenFiles:         0,
    WriteBufferSize:      0,
    VerifyChecksums:      false,
})
```

# Context & Application

These rules collectively ensure that composite literals are readable, maintainable, and resilient to refactoring. Requiring field names for external types prevents breakage when upstream packages reorder fields. Omitting zero-value fields and repeated type names reduces visual clutter. Matching-brace rules maintain scanability in deeply nested structures. In table-driven tests, explicit field names combined with zero-value omission make each test case clearly express only the fields it cares about.

# Examples

See Construction / Recognition above for the complete set of source examples.

# Relationships

- **nil-slices-decisions**: Related guidance on nil vs. empty slice initialization.
- **function-formatting**: Parallel formatting guidance for function signatures.

# Common Errors

1. Using positional initialization for types from external packages.
2. Placing the closing brace on the same line as the last value in a multi-line literal.
3. Cuddling braces when inner values are variables (not literals).
4. Explicitly specifying all zero-value fields, adding noise.
5. Repeating type names in slice/map literals when they can be inferred.

# Common Confusions

- **Cuddled vs. not cuddled**: Cuddling is only permitted when both conditions are met (indentation matches AND inner values are literals). When one element is a variable, cuddling is not allowed.
- **When to keep zero-value fields**: In table-driven tests where the zero value is part of the test (e.g., testing for `false` or `0`), explicitly specifying zero-value fields aids clarity.
- **`gofmt -s` helps**: Running `gofmt -s` automatically removes repeated type names in literals.

# Source Reference

Google Go Style Guide, "Style Decisions" chapter, "Literal formatting" section (including subsections: Field names, Matching braces, Cuddled braces, Repeated type names, Zero-value fields).

# Verification Notes

Confidence: high. All rules and code examples are directly from the source text, covering all five subsections as one unified concept.
