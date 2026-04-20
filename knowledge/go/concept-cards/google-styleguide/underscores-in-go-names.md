---
# === CORE IDENTIFICATION ===
concept: Underscores in Go Names
slug: underscores-in-go-names

# === CLASSIFICATION ===
category: naming
subcategory: capitalization
tier: foundational

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Decisions"
chapter_number: 3
pdf_page: null
section: "Naming"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "underscore exceptions in Go"
  - "snake case exceptions"
  - "when underscores are allowed"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - mixedcaps-naming
extends:
  - mixedcaps-naming
related:
  - google-package-names
  - naming-principles
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Can Go names ever contain underscores?"
  - "What are the exceptions to the no-underscores rule?"
  - "Can Go filenames have underscores?"
---

# Quick Definition

Go names should not contain underscores, with exactly three exceptions: (1) package names only imported by generated code, (2) test/benchmark/example function names in `*_test.go` files, and (3) low-level libraries interoperating with the OS or cgo (e.g., `syscall`). Filenames are not identifiers and may contain underscores.

# Core Definition

Names in Go should generally not contain underscores. There are three exceptions: (1) Package names that are only imported by generated code may contain underscores. (2) Test, Benchmark, and Example function names within `*_test.go` files may include underscores (e.g., `TestMyFunction_EdgeCase`). (3) Low-level libraries that interoperate with the operating system or cgo may reuse identifiers as done in the `syscall` package, though this is expected to be very rare. Note that filenames (e.g., `my_file.go`, `my_file_test.go`) are not Go identifiers and are not subject to these conventions.

# Prerequisites

- **mixedcaps-naming** -- The base rule that Go uses MixedCaps, never underscores

# Key Properties

1. Go names should not contain underscores as a general rule
2. Exception 1: Package names imported only by generated code
3. Exception 2: Test, Benchmark, and Example function names in `*_test.go` files
4. Exception 3: Low-level OS/cgo interop libraries (e.g., `syscall`) -- very rare
5. Filenames are not Go identifiers and may contain underscores

# Construction / Recognition

## To Apply:
1. Default to MixedCaps for all Go identifiers
2. Only use underscores in test function names to separate the unit under test from the scenario
3. If writing generated code packages, underscores in the package name are acceptable
4. For syscall/cgo interop, match the OS identifier conventions as needed

## To Recognize:
1. Underscores in non-test function names indicate a violation
2. Underscores in variable or type names indicate a violation
3. Underscores in test function names (e.g., `TestParse_InvalidInput`) are expected and correct

# Context & Application

This rule clarifies the three narrow exceptions to Go's universal MixedCaps convention. The test function exception is the most commonly encountered: Go's testing framework uses underscores to separate the function or method being tested from the test scenario (e.g., `TestUserByID_NotFound`). The generated code exception accommodates machine-generated package names that may follow different conventions. The syscall exception is a pragmatic concession to interoperability needs.

# Examples

**Example 1 -- Test function names with underscores**:

```go
// Good: underscores allowed in test function names
func TestUserByID_NotFound(t *testing.T) { ... }
func BenchmarkSort_LargeSlice(b *testing.B) { ... }
```

**Example 2 -- Package names for generated code**:

```go
// Acceptable: package only imported by generated code
package foo_go_proto
```

**Example 3 -- Black box test packages (from source)**:

```go
// Good: black box test package uses _test suffix
package linkedlist_test  // not linked_list_test
```

# Relationships

## Related
- **google-package-names** -- Package naming rules, including the underscore exception for generated code
- **naming-principles** -- General naming philosophy that informs the no-underscores rule

## Extends
- **mixedcaps-naming** -- This card details the exceptions to the MixedCaps rule

# Common Errors

- **Error**: Using underscores in regular (non-test) function names
  **Correction**: Use MixedCaps for all non-test function names

- **Error**: Using underscores in black box test package names beyond the `_test` suffix (e.g., `linked_list_test` instead of `linkedlist_test`)
  **Correction**: The package name before `_test` should follow normal package naming (no underscores)

# Common Confusions

- **Confusion**: Thinking underscores are allowed in all identifiers within test files
  **Clarification**: Only test/benchmark/example *function names* may contain underscores. Variables and types within test files still use MixedCaps.

- **Confusion**: Believing Go filenames must also avoid underscores
  **Clarification**: Filenames are not Go identifiers. `my_handler_test.go` is perfectly fine.

# Source Reference

Chapter 3: Decisions, Section "Naming" > "Underscores".

# Verification Notes

- Definition source: Directly from the "Underscores" section of Style Decisions
- Confidence rationale: HIGH -- explicit three-exception rule from the source
- Uncertainties: None
- Cross-reference status: Related slugs verified against planned extractions
