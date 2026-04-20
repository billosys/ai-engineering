---
concept: Initializing Structs
slug: initializing-structs
category: style
subcategory: initialization
tier: foundational
source: "Uber Go Style Guide"
source_slug: uber-style
authors: "Prashant Varanasi, Simon Newton"
chapter: "Style"
chapter_number: 4
pdf_page: null
section: "Initializing Structs"
extraction_confidence: high
aliases:
  - struct initialization
  - struct field names
  - struct references
prerequisites: []
extends: []
related:
  - local-variable-declarations
  - nil-is-a-valid-slice
  - initializing-maps
contrasts_with: []
answers_questions:
  - "How do I initialize structs idiomatically?"
  - "Should I use field names when initializing structs?"
  - "When should I use `var` for struct declarations?"
  - "Should I use `new(T)` or `&T{}` in Go?"
---

# Quick Definition

Initialize structs using field names (enforced by `go vet`), omit zero-value fields unless they provide meaningful context, use `var` for entirely zero-valued structs, and use `&T{}` instead of `new(T)` for struct references.

# Core Definition

The Uber Go Style Guide defines four sub-rules for struct initialization:

1. **Use field names**: Always specify field names when initializing structs. This is enforced by `go vet` and protects against breakage when struct fields are reordered.
2. **Omit zero-value fields**: When initializing with field names, omit fields that have zero values unless they provide meaningful context (e.g., in test tables).
3. **Use `var` for zero-value structs**: When all fields are omitted, use `var` instead of `T{}` to make the zero-value intent clear.
4. **Use `&T{}` not `new(T)`**: For struct references, use `&T{}` for consistency with non-pointer struct initialization.

# Prerequisites

- Understanding of Go's zero values for struct fields
- Knowledge of pointer vs value semantics for structs

# Key Properties

1. **Field names required**: Positional initialization (e.g., `User{"John", "Doe", true}`) is fragile and flagged by `go vet`.
2. **Zero-value omission reduces noise**: Only meaningful values should be specified; let Go handle defaults.
3. **Test table exception**: In test tables, zero values may be kept for clarity when field names provide context.
4. **`&T{}` consistency**: Using `&T{}` mirrors `T{}` syntax, while `new(T)` followed by field assignment is inconsistent.
5. **Field name exception**: Field names may be omitted in test tables with 3 or fewer fields.

# Construction / Recognition

**Use field names:**

```go
// Good
k := User{
    FirstName: "John",
    LastName: "Doe",
    Admin: true,
}

// Bad
k := User{"John", "Doe", true}
```

**Omit zero-value fields:**

```go
// Good
user := User{
  FirstName: "John",
  LastName: "Doe",
}

// Bad
user := User{
  FirstName: "John",
  LastName: "Doe",
  MiddleName: "",
  Admin: false,
}
```

**Use var for zero-value structs:**

```go
// Good
var user User

// Bad
user := User{}
```

**Use &T{} for struct references:**

```go
// Good
sval := T{Name: "foo"}
sptr := &T{Name: "bar"}

// Bad
sval := T{Name: "foo"}

// inconsistent
sptr := new(T)
sptr.Name = "bar"
```

# Context & Application

These rules apply to all struct initialization throughout a codebase. The zero-value omission is particularly important in production code where noisy zero values obscure the meaningful fields. In test code, the guidance is more relaxed -- test tables benefit from explicit field names even with zero values to make test expectations clear.

# Examples

**Test table with meaningful zero values:**

```go
tests := []struct{
  give string
  want int
}{
  {give: "0", want: 0},
  // ...
}
```

**Test table exception for small structs (3 or fewer fields):**

```go
tests := []struct{
  op Operation
  want string
}{
  {Add, "add"},
  {Subtract, "subtract"},
}
```

# Relationships

- **local-variable-declarations**: The `var` for zero-value structs mirrors the `var` for zero-value slices convention.
- **nil-is-a-valid-slice**: Both conventions use `var` to signal zero-value intent.
- **initializing-maps**: Maps follow a parallel convention with `make()` vs literal initialization.

# Common Errors

1. Using positional initialization -- breaks silently when fields are reordered or added.
2. Including zero-value fields in production struct literals -- adds noise without information.
3. Using `new(T)` instead of `&T{}` -- creates inconsistency between pointer and value initialization.
4. Using `User{}` instead of `var user User` for a fully zero-valued struct.

# Common Confusions

- **When to keep zero values**: Zero values should be kept when the field name provides meaningful context, such as in test tables where `want: 0` explicitly states the expected result.
- **`new(T)` vs `&T{}`**: Both produce `*T` pointing to a zero-value `T`, but `&T{}` is preferred because it allows inline field initialization and is visually consistent with `T{}`.

# Source Reference

Uber Go Style Guide, "Style" chapter, "Initializing Structs" section (including sub-sections: "Use Field Names to Initialize Structs," "Omit Zero Value Fields in Structs," "Use `var` for Zero Value Structs," "Initializing Struct References").

# Verification Notes

Confidence: high. All four sub-rules and their code examples are directly from the source text with explicit Bad/Good comparisons.
