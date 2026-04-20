---
# === CORE IDENTIFICATION ===
concept: Variable Declarations (Best Practices)
slug: variable-declarations-bp

# === CLASSIFICATION ===
category: language
subcategory: variable-declarations
tier: foundational

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Best Practices"
chapter_number: 4
pdf_page: null
section: "Variable declarations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "var vs :="
  - "zero value initialization"
  - "composite literal declarations"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - size-hints-bp
  - channel-direction
  - shadowing
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When should I use := vs var in Go?"
  - "How should I declare zero-value variables?"
  - "When should I use composite literals?"
  - "Should I use new() or &Type{} for pointer types?"
---

# Quick Definition

Use `:=` for non-zero initialization, `var` for zero values ready for later use, and composite literals when initial values are known. For pointers to zero values, both `new(T)` and `&T{}` are acceptable; `new` reminds readers that non-zero values require a constructor.

# Core Definition

Go offers three main variable declaration forms, each signaling intent. Short declarations (`:=`) are preferred for non-zero initialization: `i := 42`. The `var` keyword with no initializer signals an intentional zero value ready for later use: `var coords Point`. This is preferred over explicit zero-value composite literals like `Point{X: 0, Y: 0}`. Composite literals are for when initial elements or members are known: `primes := []int{2, 3, 5, 7, 11}`. For pointer types to zero values, both `new(T)` and `&T{}` are fine; `new` serves as a hint that non-zero initialization would require a constructor or field assignment. Map types must be explicitly initialized before modification, though reading from zero-value maps is safe. Protobuf messages should be declared as pointer types (`*pb.Message`) because only pointers satisfy `proto.Message`. When a struct contains uncopyable fields (like `sync.Mutex`), make it a value type to use zero-value initialization, but pass via pointer.

# Prerequisites

(none)

# Key Properties

1. `:=` for non-zero initialization (signals intent to initialize)
2. `var` for zero values (signals intent to use zero value)
3. Composite literals for known initial values
4. `new(T)` and `&T{}` both acceptable for pointer-to-zero-value
5. Maps must be initialized before modification; zero-value maps are read-safe
6. Protobuf messages should be pointer types (`*pb.Message`)
7. Structs with uncopyable fields (sync.Mutex) use value-type zero init, passed by pointer

# Construction / Recognition

## To Apply:
1. Non-zero value: use `:=` (`i := 42`)
2. Zero value for later: use `var` (`var coords Point`)
3. Known initial values: use composite literal (`primes := []int{2, 3, 5, 7}`)
4. Pointer to zero: use `new(T)` or `&T{}`
5. Proto messages: always use pointer type

## To Recognize:
1. Consistent `:=` for initialized variables, `var` for zero-value variables
2. No explicit zero-value composite literals like `Point{X: 0, Y: 0}`
3. Protobuf as `*pb.Message` not `pb.Message`

# Context & Application

The three forms serve as visual signals to readers about the author's intent. Using `var` for zero values is cleaner and communicates "this will be populated later" (e.g., before `json.Unmarshal`). Using `:=` signals "I am setting this to a specific value now." Composite literals with explicit zeros are clunky and obscure the intent. For protobuf, `*pb.Something` satisfies the `proto.Message` interface while `pb.Something` does not.

# Examples

**Example 1 -- Non-zero initialization**:

```go
// Good:
i := 42

// Bad:
var i = 42
```

**Example 2 -- Zero value declarations**:

```go
// Good:
var (
    coords Point
    magic  [4]byte
    primes []int
)

// Bad:
var (
    coords = Point{X: 0, Y: 0}
    magic  = [4]byte{0, 0, 0, 0}
    primes = []int(nil)
)
```

**Example 3 -- Composite literals with known values**:

```go
// Good:
var (
    coords   = Point{X: x, Y: y}
    magic    = [4]byte{'I', 'W', 'A', 'D'}
    primes   = []int{2, 3, 5, 7, 11}
    captains = map[string]string{"Kirk": "James Tiberius", "Picard": "Jean-Luc"}
)
```

**Example 4 -- Pointer to zero value**:

```go
// Good:
var (
    buf = new(bytes.Buffer)
    msg = new(pb.Message)
)
```

# Relationships

## Related
- **size-hints-bp** -- Preallocating capacity for maps and slices
- **channel-direction** -- Another variable declaration best practice
- **shadowing** -- Pitfalls with := in new scopes

## Contrasts With
(none)

# Common Errors

- **Error**: Using `var i = 42` for non-zero initialization
  **Correction**: Use `:= ` for non-zero: `i := 42`

- **Error**: Using explicit zero-value composite literals like `Point{X: 0, Y: 0}`
  **Correction**: Use `var coords Point` -- the zero value is implied

# Common Confusions

- **Confusion**: Thinking `new(T)` is always preferable to `&T{}`
  **Clarification**: Both are fine; `new` is a hint that non-zero values need a constructor

- **Confusion**: Declaring protobuf messages as value types
  **Clarification**: Always use `*pb.Message` because only pointer types satisfy `proto.Message`

# Source Reference

Chapter 4: Best Practices, Section "Variable declarations" (Initialization, Zero values, Composite literals subsections).

# Verification Notes

- Definition source: Directly from "Variable declarations" section with three subsections
- Confidence rationale: HIGH -- explicit guidance with examples for each form
- Uncertainties: None
- Cross-reference status: References decisions#copying, proto.Message documentation
