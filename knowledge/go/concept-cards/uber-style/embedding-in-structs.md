---
# === CORE IDENTIFICATION ===
concept: Embedding in Structs
slug: embedding-in-structs

# === CLASSIFICATION ===
category: style
subcategory: type-design
tier: intermediate

# === PROVENANCE ===
source: "Uber Go Style Guide"
source_slug: uber-style
authors: "Prashant Varanasi, Simon Newton"
chapter: "Style"
chapter_number: 4
pdf_page: null
section: "Embedding in Structs"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "struct embedding"
  - "type embedding"
  - "embedded types"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - function-grouping-and-ordering
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes embedding from composition via fields?"
  - "Where should embedded fields appear in a struct definition?"
  - "When should I embed a type vs use a named field?"
---

# Quick Definition

Place embedded types at the top of a struct's field list, separated from regular fields by a blank line. Embed only when it provides tangible benefit -- if you would not expose all the embedded type's methods, use a named field instead.

# Core Definition

Embedded types should be placed at the top of the field list of a struct, with an empty line separating embedded fields from regular fields. Embedding should provide tangible benefit, such as adding or augmenting functionality in a semantically appropriate way, with zero adverse user-facing effects. The litmus test is: "would all of these exported inner methods/fields be added directly to the outer type?" If the answer is "some" or "no", do not embed -- use a named field instead. Mutexes should never be embedded, even on unexported types (Uber Go Style Guide, "Embedding in Structs").

# Prerequisites

- **Go struct types** -- Understanding struct field declarations and type composition
- **Go method sets** -- Understanding that embedding promotes the inner type's methods to the outer type
- **Go exported/unexported identifiers** -- Understanding visibility implications of embedding

# Key Properties

1. Embedded types go at the top of the field list, before regular fields
2. A blank line separates embedded fields from regular fields
3. Embedding promotes all of the inner type's methods to the outer type
4. Only embed when all promoted methods are appropriate for the outer type
5. Mutexes (`sync.Mutex`) should never be embedded -- use a named field
6. Embedding should not affect the outer type's zero value usefulness
7. Embedding should not expose implementation details or unrelated methods
8. Embedding should not change the outer type's API semantics or copy semantics

# Construction / Recognition

## To Apply:
1. Ask: "Would all exported methods of the inner type be appropriate on the outer type?"
2. If yes, embed the type and place it at the top of the field list
3. If no (or "some"), use a named field instead
4. Separate embedded fields from regular fields with a blank line
5. Never embed `sync.Mutex` -- always use a named field like `mu sync.Mutex`
6. Verify that embedding does not break the outer type's zero value

## To Recognize:
1. Look for `sync.Mutex` or `sync.WaitGroup` embedded in structs -- these should be named fields
2. Look for embedded types that expose methods irrelevant to the outer type
3. Look for embedded pointer types that break zero value usefulness (nil pointer panics)
4. Look for embedded fields placed after regular fields -- they should be at the top

# Context & Application

Embedding is Go's mechanism for composition that promotes an inner type's methods to the outer type. Unlike inheritance in other languages, embedding does not create an "is-a" relationship -- it is purely method and field promotion. The key decision is whether the promoted API is appropriate for the outer type. When `sync.Mutex` is embedded, `Lock()` and `Unlock()` become part of the outer type's API, which is almost never desirable. Similarly, embedding `io.ReadWriter` as a pointer in a struct breaks the zero value because calling `Read()` on the zero value panics with a nil pointer dereference.

# Examples

**Example 1 -- Bad: embedded field not at top** (Style, "Embedding in Structs"):

```go
type Client struct {
  version int
  http.Client
}
```

**Example 2 -- Good: embedded field at top with blank line** (Style, "Embedding in Structs"):

```go
type Client struct {
  http.Client

  version int
}
```

**Example 3 -- Good: purposeful embedding** (Style, "Embedding in Structs"):

```go
type countingWriteCloser struct {
    // Good: Write() is provided at this
    //       outer layer for a specific
    //       purpose, and delegates work
    //       to the inner type's Write().
    io.WriteCloser

    count int
}

func (w *countingWriteCloser) Write(bs []byte) (int, error) {
    w.count += len(bs)
    return w.WriteCloser.Write(bs)
}
```

**Example 4 -- Bad: embedding breaks zero value** (Style, "Embedding in Structs"):

```go
type Book struct {
    // Bad: pointer changes zero value usefulness
    io.ReadWriter

    // other fields
}

// later
var b Book
b.Read(...)  // panic: nil pointer
b.String()   // panic: nil pointer
b.Write(...) // panic: nil pointer
```

**Example 5 -- Good: zero value works** (Style, "Embedding in Structs"):

```go
type Book struct {
    // Good: has useful zero value
    bytes.Buffer

    // other fields
}

// later
var b Book
b.Read(...)  // ok
b.String()   // ok
b.Write(...) // ok
```

**Example 6 -- Bad vs Good: named fields for unrelated types** (Style, "Embedding in Structs"):

```go
// Bad: exposes Lock/Unlock, WaitGroup methods, Buffer, URL on Client
type Client struct {
    sync.Mutex
    sync.WaitGroup
    bytes.Buffer
    url.URL
}

// Good: named fields keep internals private
type Client struct {
    mtx sync.Mutex
    wg  sync.WaitGroup
    buf bytes.Buffer
    url url.URL
}
```

# Relationships

## Related
- **function-grouping-and-ordering** -- Embedded types affect method sets, which influences how methods should be organized

## Contrasts With
- Composition via named fields -- when not all promoted methods are appropriate, use a named field instead of embedding

# Common Errors

- **Error**: Embedding `sync.Mutex` in a struct, exposing `Lock()` and `Unlock()` to users
  **Correction**: Use a named field: `mu sync.Mutex`

- **Error**: Embedding an interface as a pointer type, breaking the zero value
  **Correction**: Either embed a concrete type with a useful zero value, or use a named field

- **Error**: Placing embedded fields after regular fields in the struct definition
  **Correction**: Move embedded fields to the top of the struct, separated by a blank line from regular fields

# Common Confusions

- **Confusion**: Thinking embedding creates an inheritance ("is-a") relationship
  **Clarification**: Embedding is composition with method promotion. The outer type "has-a" inner type and promotes its methods. There is no polymorphic inheritance.

- **Confusion**: Believing all embedding is bad because it can expose internals
  **Clarification**: Embedding is beneficial when all promoted methods genuinely belong on the outer type. The guideline is "embed consciously and intentionally", not "never embed".

- **Confusion**: Not understanding why mutexes specifically should never be embedded
  **Clarification**: Embedding a mutex exposes `Lock()` and `Unlock()` as part of the type's public API, allowing callers to interfere with the type's internal synchronization -- a serious encapsulation violation.

# Source Reference

Chapter 4: Style, Section "Embedding in Structs".

# Verification Notes

- Definition source: Directly from the "Embedding in Structs" section of the Uber Go Style Guide
- Confidence rationale: HIGH -- the source provides extensive guidance with multiple bad/good examples and a detailed list of what embedding should not do
- Uncertainties: None
- Cross-reference status: Related slugs verified against planned extractions
