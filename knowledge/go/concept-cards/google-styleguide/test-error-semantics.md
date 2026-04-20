---
# === CORE IDENTIFICATION ===
concept: Test Error Semantics
slug: test-error-semantics

# === CLASSIFICATION ===
category: testing
subcategory: error-testing
tier: intermediate

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Style Decisions"
chapter_number: 3
pdf_page: null
section: "Test error semantics"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "error comparison in tests"
  - "testing error behavior"
  - "errors.Is in tests"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - test-failure-messages
  - test-comparisons
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Should I compare error strings in Go tests?"
  - "How should I test for specific errors in Go?"
  - "When should I use errors.Is vs string comparison for errors?"
  - "How do I test that a function returns any error?"
  - "What is a change detector test for errors?"
---

# Quick Definition

Test error behavior (using `errors.Is`, `errors.As`, or `cmpopts.EquateErrors`), not error message strings. Distinguish between tests that check for "any error" versus "a specific error". Avoid making tests brittle change detectors by relying on error wording.

# Core Definition

When testing errors, focus on semantic information rather than display strings. Error messages are intended for humans and are subject to change; testing against them creates change detector tests that break when messages are reworded. Use `errors.Is` or `cmp` with `cmpopts.EquateErrors` to test error semantics. When you only care whether an error occurred (not which error), test `err != nil` rather than matching a specific error. If an error lacks semantic information, consider filing a bug against the dependency to improve its API rather than parsing error strings. When all `wantErr` values are either `nil` or `cmpopts.AnyError`, simplify to a `bool` want field.

# Prerequisites

- **Go errors package** -- Familiarity with `errors.Is`, `errors.As`, and error wrapping
- **cmp and cmpopts** -- Understanding of `cmpopts.EquateErrors` and `cmpopts.AnyError`

# Key Properties

1. **No string comparison**: Do not compare error message strings
2. **Semantic testing**: Use `errors.Is` or `errors.As` to check error types and values
3. **cmpopts.EquateErrors**: Use with `cmp` for error comparison in table-driven tests
4. **Any-error vs specific-error**: Distinguish between "an error occurred" and "this specific error occurred"
5. **Simplify bool patterns**: When only checking error presence, use a `bool` want field instead of `cmpopts.AnyError`
6. **Exception for own package**: String comparisons are permissible to check that error messages from the package under test include certain properties like parameter names

# Construction / Recognition

## To Apply:
1. For specific error checks: `if !errors.Is(err, wantErr)`
2. For any-error checks: `if err != nil` compared against a bool
3. For table tests: use `cmpopts.EquateErrors` with `cmp`
4. Simplify to bool when all want values are nil or "any error"
5. Never match against error `.Error()` strings from external packages

## To Recognize:
1. Tests comparing `err.Error()` to a hardcoded string
2. Tests using `strings.Contains(err.Error(), ...)` for external errors
3. Table tests using `cmpopts.AnyError` when a simple bool would suffice

# Context & Application

Error messages evolve as code is maintained. Tests that match on error strings break whenever a message is improved or clarified, turning them into change detectors that slow development without catching real bugs. By testing semantic properties (error type, wrapped sentinel values), tests remain stable through cosmetic changes while still catching real behavioral regressions.

# Examples

**Example 1 -- Simplified bool error check**:

```go
// Good:
err := f(test.input)
if gotErr := err != nil; gotErr != test.wantErr {
    t.Errorf("f(%q) = %v, want error presence = %v", test.input, err, test.wantErr)
}
```

**Example 2 -- Semantic error check with errors.Is**:

```go
// Good:
if err := f(input); !errors.Is(err, fs.ErrNotExist) {
    t.Errorf("f(%q) = %v, want fs.ErrNotExist", input, err)
}
```

**Example 3 -- Anti-pattern with string comparison**:

```go
// Bad:
if err.Error() != "file not found" {
    t.Errorf(...)
}
```

# Relationships

## Related
- **test-failure-messages** -- Error test failures should follow the standard got-before-want format
- **test-comparisons** -- `cmpopts.EquateErrors` integrates with the `cmp` comparison approach

# Common Errors

- **Error**: Comparing error strings from external packages
  **Correction**: Use `errors.Is` or `errors.As` for semantic checking. If the error lacks semantic info, file a bug against the dependency.

- **Error**: Using `cmpopts.EquateErrors` when all want values are nil or AnyError
  **Correction**: Simplify to a `bool` wantErr field; the cmp machinery is unnecessary mechanism.

# Common Confusions

- **Confusion**: Thinking string comparison of errors from the package under test is also forbidden
  **Clarification**: It is permissible to check that error messages from your own package include certain properties (like parameter names). The prohibition targets testing exact error message wording, especially from external dependencies.

- **Confusion**: Conflating "any error" tests with "specific error" tests
  **Clarification**: When you only need to know if an error occurred, use a bool. When you need to know which error, use `errors.Is` or `errors.As`.

# Source Reference

Chapter 3: Style Decisions, Section "Test error semantics" under "Useful test failures".

# Verification Notes

- Definition source: Directly from the "Test error semantics" section
- Confidence rationale: HIGH -- explicit guidance with clear examples and rationale
- Uncertainties: None
- Cross-reference status: References best practices on error handling and GoTip #13
