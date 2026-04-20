---
# === CORE IDENTIFICATION ===
concept: Function Names
slug: function-names

# === CLASSIFICATION ===
category: style
subcategory: naming
tier: foundational

# === PROVENANCE ===
source: "Uber Go Style Guide"
source_slug: uber-style
authors: "Prashant Varanasi, Simon Newton"
chapter: "Style"
chapter_number: 4
pdf_page: null
section: "Function Names"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "MixedCaps convention"
  - "Go function naming"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - package-names
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How should I name functions in Go?"
  - "Can test functions contain underscores?"
  - "What is MixedCaps in Go?"
---

# Quick Definition

Use MixedCaps (PascalCase or camelCase) for function names. Test functions may contain underscores to group related test cases.

# Core Definition

Go function names follow the community convention of MixedCaps -- exported functions use PascalCase (e.g., `ProcessOrder`) and unexported functions use camelCase (e.g., `processOrder`). The one exception is test functions, which may contain underscores for the purpose of grouping related test cases, e.g., `TestMyFunction_WhatIsBeingTested` (Uber Go Style Guide, "Function Names").

# Prerequisites

- **Go exported/unexported identifiers** -- Understanding that an uppercase first letter makes a function exported (public)

# Key Properties

1. Follow the MixedCaps convention: no underscores in regular function names
2. Exported functions start with an uppercase letter (PascalCase)
3. Unexported functions start with a lowercase letter (camelCase)
4. Test functions are the exception: underscores are permitted to group related test cases
5. The underscore in test names separates the function being tested from the specific scenario

# Construction / Recognition

## To Apply:
1. Name exported functions with PascalCase: `ProcessOrder`, `NewClient`
2. Name unexported functions with camelCase: `processOrder`, `newClient`
3. Never use underscores in non-test function names
4. In test functions, use the pattern `TestFunctionName_Scenario`: `TestParse_InvalidInput`

## To Recognize:
1. Look for function names with underscores outside of test files -- this violates the guideline
2. Look for test functions that use underscores to describe scenarios -- this is the correct pattern

# Context & Application

This guideline follows the standard Go community convention documented in Effective Go under "MixedCaps". The Uber style guide reinforces this convention and explicitly notes the test function exception. Consistent naming makes code predictable and aligns with the broader Go ecosystem's expectations.

# Examples

**Example 1 -- Standard function names**:

```go
// Exported (PascalCase)
func ProcessOrder(o *Order) error { ... }
func NewClient(cfg Config) *Client { ... }

// Unexported (camelCase)
func processOrder(o *Order) error { ... }
func validateInput(s string) bool { ... }
```

**Example 2 -- Test function with underscores** (Style, "Function Names"):

```go
// Underscores allowed in test functions for grouping related cases
func TestMyFunction_WhatIsBeingTested(t *testing.T) { ... }
```

# Relationships

## Related
- **package-names** -- Package and function naming conventions work together since functions are called as `package.Function`

# Common Errors

- **Error**: Using underscores in non-test function names (e.g., `process_order`)
  **Correction**: Use MixedCaps: `processOrder` or `ProcessOrder`

- **Error**: Using ALL_CAPS for constants or function names (a habit from other languages)
  **Correction**: Go uses MixedCaps everywhere: `MaxRetries`, not `MAX_RETRIES`

# Common Confusions

- **Confusion**: Thinking underscores are never allowed in Go function names
  **Clarification**: Test functions are the explicit exception. `TestParse_EmptyInput` is idiomatic for grouping related test cases.

- **Confusion**: Wondering whether acronyms should be all-caps in function names
  **Clarification**: Go convention uses all-caps for acronyms in MixedCaps names: `ServeHTTP`, `parseJSON`, `NewHTTPClient`

# Source Reference

Chapter 4: Style, Section "Function Names".

# Verification Notes

- Definition source: Directly from the "Function Names" section of the Uber Go Style Guide
- Confidence rationale: HIGH -- the source explicitly states the MixedCaps convention and the test function exception
- Uncertainties: None
- Cross-reference status: Related slugs verified against planned extractions
