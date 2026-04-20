---
# === CORE IDENTIFICATION ===
concept: Receivers and Interfaces
slug: receivers-and-interfaces

# === CLASSIFICATION ===
category: interfaces
subcategory: interface-satisfaction
tier: intermediate

# === PROVENANCE ===
source: "Uber Go Style Guide"
source_slug: uber-style
authors: "Prashant Varanasi, Simon Newton"
chapter: "Guidelines"
chapter_number: 2
pdf_page: null
section: "Receivers and Interfaces"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "value receivers vs pointer receivers"
  - "pointer receiver interface satisfaction"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - pointers-to-interfaces
  - verify-interface-compliance
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do value receivers and pointer receivers differ for interface satisfaction?"
  - "Can a value type satisfy an interface with pointer receiver methods?"
  - "Why can't I call a pointer receiver method on a map value?"
---

# Quick Definition

Methods with value receivers can be called on both pointers and values, but methods with pointer receivers can only be called on pointers or addressable values. This asymmetry determines which types can satisfy an interface.

# Core Definition

The Uber Go Style Guide explains that methods with value receivers can be called on pointers as well as values, while methods with pointer receivers can only be called on pointers or addressable values. For interface satisfaction, this means: if a type has value receivers for all interface methods, both the value type and its pointer can satisfy the interface. If any method has a pointer receiver, only the pointer type can satisfy the interface -- a plain value cannot (Uber Go Style Guide, "Receivers and Interfaces").

# Prerequisites

- **Go methods** -- Understanding method declarations with receivers
- **Go interfaces** -- Understanding how interface satisfaction works
- **Addressable values** -- Understanding which values in Go are addressable (variables, struct fields, array elements, but not map values)

# Key Properties

1. Value receiver methods can be called on both values and pointers
2. Pointer receiver methods can only be called on pointers or addressable values
3. Values stored in maps are not addressable, so pointer receiver methods cannot be called on them
4. A value type with all value receiver methods satisfies an interface for both `T` and `*T`
5. A type with any pointer receiver method satisfies the interface only for `*T`, not `T`
6. An interface can be satisfied by a pointer even if the method has a value receiver

# Construction / Recognition

## To Apply:
1. Decide whether methods need to mutate the receiver -- if yes, use pointer receivers
2. If all methods use value receivers, both `T` and `*T` will satisfy the interface
3. If any method uses a pointer receiver, only `*T` satisfies the interface
4. When storing values in maps, remember that map values are not addressable -- pointer receiver methods cannot be called on them
5. Store pointers in maps (`map[K]*T`) if you need to call pointer receiver methods

## To Recognize:
1. Look for compile errors like "cannot use value (type T) as type Interface" -- this indicates a pointer receiver mismatch
2. Look for `map[K]T` with pointer receiver methods -- the values won't be addressable

# Context & Application

This distinction is fundamental to Go's type system and affects API design decisions. When designing types that implement interfaces, the choice between value and pointer receivers has cascading effects on how the type can be used. The guideline is especially important when working with collections (maps, slices) and when deciding whether users of a type will work with values or pointers.

# Examples

**Example 1** (Guidelines, "Receivers and Interfaces"): Map addressability

```go
type S struct {
  data string
}

func (s S) Read() string {
  return s.data
}

func (s *S) Write(str string) {
  s.data = str
}

sVals := map[int]S{1: {"A"}}

// We can call Read on values stored in the map because Read
// has a value receiver, which does not require the value to
// be addressable.
sVals[1].Read()

// We cannot call Write on values stored in the map because Write
// has a pointer receiver, and it's not possible to get a pointer
// to a value stored in a map.
//
//  sVals[1].Write("test")

sPtrs := map[int]*S{1: {"A"}}

// You can call both Read and Write if the map stores pointers,
// because pointers are intrinsically addressable.
sPtrs[1].Read()
sPtrs[1].Write("test")
```

**Example 2** (Guidelines, "Receivers and Interfaces"): Interface satisfaction

```go
type F interface {
  f()
}

type S1 struct{}

func (s S1) f() {}

type S2 struct{}

func (s *S2) f() {}

s1Val := S1{}
s1Ptr := &S1{}
s2Val := S2{}
s2Ptr := &S2{}

var i F
i = s1Val  // works: S1 has value receiver
i = s1Ptr  // works: *S1 also satisfies F (value receiver)
i = s2Ptr  // works: *S2 has pointer receiver

// The following doesn't compile, since s2Val is a value,
// and there is no value receiver for f.
//   i = s2Val
```

# Relationships

## Builds Upon
- **Go method sets** -- The rules for value and pointer receiver methods define which types satisfy interfaces

## Enables
- Informed decisions about receiver types when designing interfaces
- Correct usage of types in maps and other non-addressable contexts

## Related
- **pointers-to-interfaces** -- Related to understanding how pointer and value types interact with interfaces
- **verify-interface-compliance** -- The compile-time check pattern depends on understanding receiver types

## Contrasts With
- Languages where all method calls use reference semantics by default

# Common Errors

- **Error**: Storing value types in a map and trying to call pointer receiver methods on them
  **Correction**: Store pointers in the map (`map[K]*T`) instead of values (`map[K]T`)

- **Error**: Trying to assign a value type to an interface when the type only has pointer receivers
  **Correction**: Use a pointer to the value (`&val`) when assigning to the interface

# Common Confusions

- **Confusion**: Believing that a value with pointer receiver methods can satisfy an interface
  **Clarification**: Only `*T` satisfies the interface when pointer receivers are used; a plain `T` value cannot

- **Confusion**: Thinking value receivers mean the method cannot be called on pointers
  **Clarification**: Value receiver methods can be called on both values and pointers -- Go automatically dereferences the pointer

- **Confusion**: Assuming all values are addressable in Go
  **Clarification**: Map values, constants, and some expression results are not addressable, which prevents calling pointer receiver methods on them

# Source Reference

Chapter 2: Guidelines, Section "Receivers and Interfaces". See also the reference to Effective Go's "Pointers vs. Values" section.

# Verification Notes

- Definition source: Directly from the "Receivers and Interfaces" section with two detailed code examples
- Confidence rationale: HIGH -- the source provides explicit code examples demonstrating both the map addressability issue and the interface satisfaction rules
- Uncertainties: None
- Cross-reference status: Related slugs verified against planned extractions
