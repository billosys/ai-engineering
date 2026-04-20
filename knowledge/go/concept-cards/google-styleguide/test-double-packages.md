---
# === CORE IDENTIFICATION ===
concept: Test Double Packages
slug: test-double-packages

# === CLASSIFICATION ===
category: testing
subcategory: test-organization
tier: intermediate

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Best Practices"
chapter_number: 4
pdf_page: null
section: "Test double and helper packages"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "test double naming"
  - "test helper packages"
  - "stub package naming"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - package-names
extends: []
related:
  - naming-principles
  - package-size
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How should I name a package that provides test doubles?"
  - "How should I name stub types in a test helper package?"
  - "How do I name local variables that reference test doubles?"
---

# Quick Definition

Name test double packages by appending `test` to the production package name (e.g., `creditcardtest`). Name stub types concisely when there is only one type to double; use behavior-based or type-prefixed names when there are multiple.

# Core Definition

When creating a package of test doubles (stubs, fakes, mocks, or spies), append the word `test` to the original package name to form the test helper package name (e.g., `creditcard` becomes `creditcardtest`). For a single test double type, use a concise name like `Stub` since the package name already provides context (`creditcardtest.Stub`). When multiple behaviors are needed, name stubs by the behavior they emulate (e.g., `AlwaysCharges`, `AlwaysDeclines`). When doubling multiple types, prefix with the type name (e.g., `StubService`, `StubStoredValue`). In test code, prefix local variables referencing doubles to differentiate them from production types (e.g., `spyCC` rather than `cc`).

# Prerequisites

- **package-names** -- Understanding Go package naming conventions

# Key Properties

1. Test helper package name = production package name + `test` suffix
2. Single-type doubles use concise names (e.g., `Stub`, `Fake`, `Spy`)
3. Multiple behaviors use descriptive names (e.g., `AlwaysCharges`, `AlwaysDeclines`)
4. Multiple doubled types use type-prefixed names (e.g., `StubService`, `StubStoredValue`)
5. Test local variables should use prefixed names to distinguish doubles from production types
6. Mark Bazel `go_library` rules as `testonly` for test helper packages

# Construction / Recognition

## To Apply:
1. Create a new package named `<production>test`
2. If doubling one type, name the double `Stub` (or `Fake`, `Mock`, `Spy` as appropriate)
3. If multiple behaviors, name by the behavior (e.g., `AlwaysSucceeds`)
4. If multiple types, prefix with the type name (e.g., `StubService`)
5. In tests, prefix variables referencing doubles (e.g., `spyCC`)

## To Recognize:
1. Package names ending in `test` that contain types implementing production interfaces
2. Concise type names leveraging the package name for context

# Context & Application

This convention ensures test double packages are clearly associated with their production counterparts while keeping type names at call sites readable. The approach avoids redundant naming like `StubCreditCardService` by letting the package name carry context. The variable-naming guidance helps readers of test code quickly distinguish between real implementations and doubles.

# Examples

**Example 1 -- Simple single-type stub**:

```go
package creditcardtest

import (
    "path/to/creditcard"
    "path/to/money"
)

// Stub stubs creditcard.Service and provides no behavior of its own.
type Stub struct{}

func (Stub) Charge(*creditcard.Card, money.Money) error { return nil }
```

**Example 2 -- Multiple behaviors**:

```go
// AlwaysCharges stubs creditcard.Service and simulates success.
type AlwaysCharges struct{}

func (AlwaysCharges) Charge(*creditcard.Card, money.Money) error { return nil }

// AlwaysDeclines stubs creditcard.Service and simulates declined charges.
type AlwaysDeclines struct{}

func (AlwaysDeclines) Charge(*creditcard.Card, money.Money) error {
    return creditcard.ErrDeclined
}
```

**Example 3 -- Prefixed test variable**:

```go
// Good:
func TestProcessor(t *testing.T) {
    var spyCC creditcardtest.Spy
    proc := &Processor{CC: spyCC}
    // ...
}

// Bad:
func TestProcessor(t *testing.T) {
    var cc creditcardtest.Spy  // unclear it's a double
    proc := &Processor{CC: cc}
    // ...
}
```

# Relationships

## Related
- **naming-principles** -- General naming guidance applied to test code
- **package-size** -- Helps decide when test helpers warrant a separate package

## Contrasts With
(none)

# Common Errors

- **Error**: Naming the double `StubCreditCardService` with full qualification
  **Correction**: Use `Stub` or `StubService` -- the package name provides context

- **Error**: Using unprefixed variable names for doubles alongside production types
  **Correction**: Prefix double variables (e.g., `spyCC`) to improve clarity

# Common Confusions

- **Confusion**: Thinking every test needs a separate test double package
  **Clarification**: Only create a `*test` package when doubles will be shared across multiple test files or packages

- **Confusion**: Mixing double kinds (stub, fake, mock) in names inconsistently
  **Clarification**: Choose the double type name that matches the actual behavior provided

# Source Reference

Chapter 4: Best Practices, Section "Naming" > "Test double and helper packages".

# Verification Notes

- Definition source: Directly from the "Test double and helper packages" section with all subsections
- Confidence rationale: HIGH -- explicit guidance with detailed examples
- Uncertainties: None
- Cross-reference status: References guide#naming, decisions#package-names
