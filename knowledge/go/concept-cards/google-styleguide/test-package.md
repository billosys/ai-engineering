---
# === CORE IDENTIFICATION ===
concept: Test Package Organization
slug: test-package

# === CLASSIFICATION ===
category: testing
subcategory: test-organization
tier: intermediate

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Style Decisions"
chapter_number: 3
pdf_page: null
section: "Test package"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "_test package suffix"
  - "black box testing"
  - "white box testing"
  - "external test package"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - use-package-testing
  - subtests
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When should I use a _test package suffix in Go?"
  - "What is the difference between black box and white box testing in Go?"
  - "Can Go tests access unexported identifiers?"
  - "When should I use the same package for tests vs a different package?"
---

# Quick Definition

Tests can be in the same package (white box, accessing unexported identifiers) or in a `_test` suffixed package (black box, testing only the exported API). Use the `_test` package for integration tests without an obvious owning library and to break circular dependencies.

# Core Definition

Go supports two test package conventions. **Same-package tests** use `package foo` in the test file, giving access to unexported identifiers for thorough white-box testing. **Different-package tests** use `package foo_test`, testing only the exported API as a black-box consumer would. The `_test` suffix is the only permitted exception to the no-underscores rule for package names. Use the `_test` package when: an integration test does not belong to a single library, or when same-package tests would create circular import dependencies. Same-package tests enable better coverage and more concise tests but be aware that examples declared in them will not show the package name users need.

# Prerequisites

- **Go package system** -- Understanding of package visibility and import rules
- **Go test conventions** -- `*_test.go` files and the `go test` command

# Key Properties

1. **Same package (white box)**: `package foo` in `foo_test.go`; accesses unexported identifiers
2. **Different package (black box)**: `package foo_test` in `foo_test.go`; only exported API
3. **No explicit import needed**: Same-package tests do not import the package under test
4. **Circular dependency resolution**: Use `_test` package when same-package tests cause circular imports
5. **Integration tests**: Use `_test` package when the test does not belong to a single library
6. **Example visibility**: Examples in same-package tests lack the package qualifier users need

# Construction / Recognition

## To Apply:
1. For testing unexported internals: use `package foo` in `foo_test.go`
2. For testing exported API as a consumer: use `package foo_test` in `foo_test.go`
3. For integration tests spanning multiple packages: use `package integration_test`
4. For breaking circular dependencies: use the `_test` suffix

## To Recognize:
1. Tests that need unexported access but use a `_test` package (possibly over-constrained)
2. Tests in the same package that only exercise the exported API (could benefit from `_test`)
3. Circular dependency errors from test files (need to move to `_test` package)

# Context & Application

The choice between same-package and `_test` package testing depends on what you need to test and how the test relates to the package. Black-box testing with `_test` validates the public contract and catches API usability issues. White-box testing catches internal logic errors and enables testing of unexported helper functions. Both approaches are valid and can coexist for the same package.

# Examples

**Example 1 -- Same-package test (white box)**:

```go
// foo_test.go
package foo

func TestInternalHelper(t *testing.T) {
    // Can access unexported identifiers
    result := internalHelper("input")
    // ...
}
```

**Example 2 -- Different-package test (black box, integration)**:

```go
// integration_test.go
package gmailintegration_test

import "testing"
```

**Example 3 -- Breaking circular dependencies**:

```go
// fireworks_test.go
package fireworks_test

import (
    "fireworks"
    "fireworkstestutil" // also imports fireworks
)
```

# Relationships

## Related
- **use-package-testing** -- Both address test organization fundamentals
- **subtests** -- Subtests work the same in both package styles

# Common Errors

- **Error**: Using same-package tests when it creates circular import dependencies
  **Correction**: Switch to the `_test` package suffix to break the cycle.

- **Error**: Using `_test` package when you need to test unexported functions
  **Correction**: Use same-package tests for white-box access to internals.

# Common Confusions

- **Confusion**: Thinking `_test` suffix is just a convention, not a Go feature
  **Clarification**: The `_test` suffix is a special Go feature recognized by the build system. It creates an actual separate package that can only import the package under test.

- **Confusion**: Thinking you must choose one approach for all tests in a package
  **Clarification**: You can have both `package foo` and `package foo_test` test files in the same directory.

# Source Reference

Chapter 3: Style Decisions, Sections "Tests in the same package" and "Tests in a different package" under "Test package".

# Verification Notes

- Definition source: Directly from the "Test package" section and its subsections
- Confidence rationale: HIGH -- explicit guidance with clear examples for both approaches
- Uncertainties: None
- Cross-reference status: Verified against package naming conventions in the same chapter
