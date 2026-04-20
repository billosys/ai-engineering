---
# === CORE IDENTIFICATION ===
concept: Pointers to Interfaces
slug: pointers-to-interfaces

# === CLASSIFICATION ===
category: interfaces
subcategory: interface-usage
tier: intermediate

# === PROVENANCE ===
source: "Uber Go Style Guide"
source_slug: uber-style
authors: "Prashant Varanasi, Simon Newton"
chapter: "Guidelines"
chapter_number: 2
pdf_page: null
section: "Pointers to Interfaces"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "interface pointer anti-pattern"
  - "don't use pointer to interface"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - verify-interface-compliance
extends: []
related:
  - receivers-and-interfaces
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Should I use a pointer to an interface in Go?"
  - "Why are interfaces already reference-like values in Go?"
---

# Quick Definition

You almost never need a pointer to an interface. Pass interfaces as values -- the underlying data can still be a pointer.

# Core Definition

An interface in Go is internally represented as two fields: a pointer to type-specific information ("type") and a data pointer. If the stored data is a pointer, it is stored directly; if the stored data is a value, then a pointer to the value is stored. Because the interface value itself already contains a pointer to the underlying data, passing a pointer to the interface is almost always unnecessary. If you want interface methods to modify the underlying data, the concrete type stored in the interface should be a pointer (Uber Go Style Guide, "Pointers to Interfaces").

# Prerequisites

- **Go interfaces** -- Understanding how interfaces work in Go is essential to grasping why a pointer to an interface is redundant
- **Pointers in Go** -- Understanding the difference between values and pointers is necessary to see why the interface's internal representation makes a pointer-to-interface unnecessary

# Key Properties

1. An interface value contains two internal fields: a type pointer and a data pointer
2. If the concrete value stored in the interface is a pointer, it is stored directly in the interface's data field
3. If the concrete value stored is a non-pointer, the interface stores a pointer to a copy of that value
4. Passing a pointer to an interface is almost never needed because the interface itself is already a lightweight reference type
5. To allow interface methods to modify the underlying data, use a pointer as the concrete type stored in the interface

# Construction / Recognition

## To Apply:
1. Declare function parameters and return types as interface values, not pointers to interfaces
2. If you need interface methods to mutate underlying data, ensure the concrete type stored in the interface is a pointer
3. Never use `*InterfaceName` as a parameter type unless you have a very specific reason

## To Recognize:
1. Look for function signatures with `*SomeInterface` as parameter types -- this is the anti-pattern
2. Look for variables declared as `var x *SomeInterface` -- this is almost always wrong

# Context & Application

This guideline applies whenever you are defining function signatures, struct fields, or variable declarations that involve interfaces. Because Go's interface values already act as lightweight containers holding a reference to the underlying data, adding another level of indirection via a pointer is redundant and can cause confusion. The rare exception is when you need to distinguish between "no interface value" (nil pointer) and "interface value holding nil" -- but this is an uncommon need.

# Examples

**Example 1** (Guidelines, "Pointers to Interfaces"):

The interface itself is two fields internally:

```go
// An interface is two fields:
// 1. A pointer to some type-specific information ("type")
// 2. Data pointer -- if the data stored is a pointer, it's stored directly.
//    If the data stored is a value, then a pointer to the value is stored.
```

If you want interface methods to modify the underlying data, use a pointer as the concrete type:

```go
type Writer interface {
    Write([]byte) (int, error)
}

// Pass the interface as a value, but the concrete type is a pointer
func process(w Writer) {
    // w can modify underlying data because the concrete type is a pointer
}
```

# Relationships

## Builds Upon
- **Go interface internals** -- Understanding the two-field representation explains why pointer-to-interface is unnecessary

## Enables
- Clean API design with proper interface usage

## Related
- **receivers-and-interfaces** -- Value vs pointer receivers determine whether the concrete type stored in an interface can modify data

## Contrasts With
- Using pointer-to-interface (`*InterfaceName`) as a parameter type

# Common Errors

- **Error**: Declaring function parameters as `*io.Reader` or `*io.Writer`
  **Correction**: Use `io.Reader` or `io.Writer` directly as the parameter type

- **Error**: Storing `*InterfaceName` in struct fields
  **Correction**: Store `InterfaceName` directly; if mutation is needed, ensure the concrete type is a pointer

# Common Confusions

- **Confusion**: Believing that passing an interface by value copies the underlying data
  **Clarification**: The interface value itself is small (two pointers). Passing it by value copies only the interface header, not the underlying data. The data pointer still refers to the original data.

- **Confusion**: Thinking you need a pointer to an interface to allow methods to modify data
  **Clarification**: You need the *concrete type stored in the interface* to be a pointer, not a pointer to the interface itself

# Source Reference

Chapter 2: Guidelines, Section "Pointers to Interfaces".

# Verification Notes

- Definition source: Directly from the "Pointers to Interfaces" section of the Uber Go Style Guide
- Confidence rationale: HIGH -- the source explicitly states this guideline with clear technical explanation of interface internals
- Uncertainties: None
- Cross-reference status: Related slugs verified against planned extractions
