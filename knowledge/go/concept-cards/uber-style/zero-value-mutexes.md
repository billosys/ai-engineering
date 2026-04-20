---
# === CORE IDENTIFICATION ===
concept: Zero-Value Mutexes
slug: zero-value-mutexes

# === CLASSIFICATION ===
category: concurrency
subcategory: synchronization
tier: intermediate

# === PROVENANCE ===
source: "Uber Go Style Guide"
source_slug: uber-style
authors: "Prashant Varanasi, Simon Newton"
chapter: "Guidelines"
chapter_number: 2
pdf_page: null
section: "Zero-value Mutexes are Valid"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "zero value mutex"
  - "mutex best practices"
  - "don't embed mutexes"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - defer-to-clean-up
  - copy-slices-and-maps-at-boundaries
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a zero-value mutex?"
  - "Should I use a pointer to a mutex in Go?"
  - "Should I embed sync.Mutex in my struct?"
---

# Quick Definition

The zero-value of `sync.Mutex` and `sync.RWMutex` is valid and ready to use, so you almost never need a pointer to a mutex. Don't embed the mutex in your struct -- use a named unexported field instead.

# Core Definition

The Uber Go Style Guide states that the zero-value of `sync.Mutex` and `sync.RWMutex` is valid, so you almost never need a pointer to a mutex. When using a struct by pointer, the mutex should be a non-pointer field on it. The guide further advises against embedding the mutex on the struct, even if the struct is not exported, because embedding exposes the `Lock` and `Unlock` methods as part of the struct's API. Instead, use a named unexported field like `mu sync.Mutex` to keep the mutex as an implementation detail (Uber Go Style Guide, "Zero-value Mutexes are Valid").

# Prerequisites

- **sync.Mutex / sync.RWMutex** -- Understanding what mutexes are and how they provide mutual exclusion
- **Go zero values** -- Understanding that Go initializes variables to their zero value
- **Struct embedding** -- Understanding the difference between embedding a type and using a named field

# Key Properties

1. `sync.Mutex` and `sync.RWMutex` are ready to use without explicit initialization
2. Declaring `var mu sync.Mutex` is sufficient -- no `new(sync.Mutex)` or `&sync.Mutex{}` needed
3. Mutexes should be non-pointer fields in structs
4. Mutexes should NOT be embedded -- use a named unexported field (e.g., `mu sync.Mutex`)
5. Embedding a mutex exposes `Lock` and `Unlock` as part of the struct's exported API, which is undesirable

# Construction / Recognition

## To Apply:
1. Declare mutexes as `var mu sync.Mutex` or as struct fields `mu sync.Mutex`
2. Never use `new(sync.Mutex)` or `*sync.Mutex` fields
3. Never embed `sync.Mutex` directly -- always use a named field
4. Name the mutex field `mu` (conventional) and keep it unexported

## To Recognize:
1. Look for `new(sync.Mutex)` or `*sync.Mutex` -- these indicate unnecessary pointer usage
2. Look for `sync.Mutex` (without field name) embedded in a struct -- this is the anti-pattern
3. A struct with unexported `mu sync.Mutex` field follows the guideline correctly

# Context & Application

This guideline is important for struct design in concurrent Go programs. Embedding a mutex makes `Lock()` and `Unlock()` part of the struct's method set, which leaks implementation details to callers. Even for unexported structs, using a named field is preferred because it keeps the synchronization mechanism explicit and contained. The zero-value validity means there is no need for constructor logic to initialize the mutex.

# Examples

**Example 1** (Guidelines, "Zero-value Mutexes are Valid"): Pointer vs value mutex

Bad:
```go
mu := new(sync.Mutex)
mu.Lock()
```

Good:
```go
var mu sync.Mutex
mu.Lock()
```

**Example 2** (Guidelines, "Zero-value Mutexes are Valid"): Embedded vs named field

Bad -- mutex is embedded, exposing Lock/Unlock:
```go
type SMap struct {
  sync.Mutex

  data map[string]string
}

func (m *SMap) Get(k string) string {
  m.Lock()
  defer m.Unlock()

  return m.data[k]
}
```

Good -- mutex is a named unexported field:
```go
type SMap struct {
  mu sync.Mutex

  data map[string]string
}

func (m *SMap) Get(k string) string {
  m.mu.Lock()
  defer m.mu.Unlock()

  return m.data[k]
}
```

The bad example makes the `Mutex` field, `Lock`, and `Unlock` methods unintentionally part of the exported API of `SMap`. The good example keeps the mutex and its methods as implementation details hidden from callers.

# Relationships

## Builds Upon
- **Go zero values** -- The validity of zero-value mutexes follows from Go's zero-value design philosophy

## Enables
- Simple struct initialization without constructor boilerplate for mutex fields
- Clean encapsulation of synchronization as an implementation detail

## Related
- **defer-to-clean-up** -- Defer is commonly used with mutexes (`defer mu.Unlock()`)
- **copy-slices-and-maps-at-boundaries** -- Both address protecting internal state in concurrent or shared contexts

## Contrasts With
- Embedding `sync.Mutex` in structs (anti-pattern)
- Using pointer-to-mutex (unnecessary)

# Common Errors

- **Error**: Using `mu := new(sync.Mutex)` to create a mutex
  **Correction**: Use `var mu sync.Mutex` -- the zero value is valid and ready to use

- **Error**: Embedding `sync.Mutex` in a struct (`type Foo struct { sync.Mutex; ... }`)
  **Correction**: Use a named unexported field: `type Foo struct { mu sync.Mutex; ... }`

# Common Confusions

- **Confusion**: Thinking `sync.Mutex` needs to be initialized before use
  **Clarification**: The zero value of `sync.Mutex` is an unlocked mutex, ready to use immediately

- **Confusion**: Believing embedding is fine for unexported structs
  **Clarification**: The guide advises against embedding even for unexported structs, because it still adds Lock/Unlock to the struct's method set

# Source Reference

Chapter 2: Guidelines, Section "Zero-value Mutexes are Valid".

# Verification Notes

- Definition source: Directly from the "Zero-value Mutexes are Valid" section with Bad/Good code comparisons
- Confidence rationale: HIGH -- explicit guideline with detailed examples and rationale
- Uncertainties: None
- Cross-reference status: Related slugs verified against planned extractions
