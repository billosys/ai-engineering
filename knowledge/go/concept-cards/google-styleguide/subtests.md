---
# === CORE IDENTIFICATION ===
concept: Subtests
slug: subtests

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
section: "Subtests"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "t.Run"
  - "subtest naming"
  - "test grouping"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - table-driven-tests-decisions
  - test-failure-messages
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How should I use t.Run for subtests in Go?"
  - "How should I name subtests?"
  - "Can subtests depend on each other?"
  - "What characters should I avoid in subtest names?"
---

# Quick Definition

Use `t.Run` to define subtests for flexible setup/cleanup, parallelism control, and test filtering. Name subtests like function identifiers (not prose), avoid slashes and spaces, and ensure each subtest is independently runnable.

# Core Definition

Go's testing library provides `t.Run` to define subtests, enabling flexibility in setup, cleanup, parallelism control, and test filtering. Subtests should not depend on other subtests for success or initial state -- each must be runnable individually via `go test -run` or Bazel test filters. Subtest names should be treated like function identifiers rather than prose descriptions: keep them readable, concise, and useful on the command line. The test runner replaces spaces with underscores and escapes non-printing characters, so avoid these in names. Slashes are particularly problematic because they have special meaning in test filter expressions. Longer descriptions belong in a separate field printed via `t.Log` or alongside failure messages.

# Prerequisites

- **Go testing package** -- Familiarity with `t.Run`, `t.Parallel`, and test filtering
- **Table-driven tests** -- Subtests are commonly used with table-driven test patterns

# Key Properties

1. **Independent execution**: Each subtest must be runnable in isolation; no dependencies on other subtests
2. **Identifier-style names**: Names should be like function identifiers, not prose descriptions
3. **No slashes**: Slashes have special meaning in test filters and cause awkward matching
4. **No spaces**: The runner replaces spaces with underscores, which can cause confusion
5. **Descriptions elsewhere**: Long descriptions go in a separate struct field or `t.Log`
6. **Setup/cleanup scoping**: Subtests scope setup and cleanup operations
7. **Parallelism control**: `t.Parallel()` within subtests enables concurrent execution

# Construction / Recognition

## To Apply:
1. Use `t.Run("descriptive-name", func(t *testing.T) { ... })` to group test cases
2. Name subtests concisely with identifier-style names (e.g., `"hu=en_bug-1234"`)
3. Put long descriptions in a separate field, printed in failure messages
4. Ensure each subtest works independently

## To Recognize:
1. Subtests with prose names: `t.Run("check that there is no mention of...", ...)`
2. Subtests with slashes: `t.Run("AM/PM confusion", ...)`
3. Subtests that depend on execution order or shared mutable state from prior subtests

# Context & Application

Subtests are particularly useful with table-driven tests, where each table entry becomes a named subtest. They are also valuable when multiple related test cases share expensive setup (e.g., creating a database connection). The naming guidelines ensure that tests can be selected and filtered effectively from the command line and that test logs remain readable.

# Examples

**Example 1 -- Table-driven test with subtests**:

```go
func TestTranslate(t *testing.T) {
    data := []struct {
        name, desc, srcLang, dstLang, srcText, wantDstText string
    }{
        {
            name:    "hu=en_bug-1234",
            desc:    "regression test following bug 1234",
            srcLang: "hu",
            dstLang: "en",
            srcText: "cigarettat es egy ongyujtot kerek",
            wantDstText: "cigarettes and a lighter please",
        },
    }
    for _, d := range data {
        t.Run(d.name, func(t *testing.T) {
            got := Translate(d.srcLang, d.dstLang, d.srcText)
            if got != d.wantDstText {
                t.Errorf("%s\nTranslate(%q, %q, %q) = %q, want %q",
                    d.desc, d.srcLang, d.dstLang, d.srcText, got, d.wantDstText)
            }
        })
    }
}
```

**Example 2 -- Anti-patterns in subtest names**:

```go
// Bad: too wordy
t.Run("check that there is no mention of scratched records", ...)
// Bad: slashes cause problems
t.Run("AM/PM confusion", ...)
```

# Relationships

## Related
- **table-driven-tests-decisions** -- Subtests are the standard mechanism for naming table-driven test cases
- **test-failure-messages** -- Subtest names complement failure messages for diagnostic output

# Common Errors

- **Error**: Making subtests depend on execution order
  **Correction**: Each subtest must be independently runnable with `go test -run`.

- **Error**: Using slashes in subtest names
  **Correction**: Slashes have special meaning in test filters. Use hyphens or underscores instead.

# Common Confusions

- **Confusion**: Thinking subtest names should be descriptive sentences
  **Clarification**: Names should be identifier-style (concise, filterable). Put descriptions in a separate field.

# Source Reference

Chapter 3: Style Decisions, Sections "Subtests" and "Subtest names" under "Test structure".

# Verification Notes

- Definition source: Directly from the "Subtests" and "Subtest names" sections
- Confidence rationale: HIGH -- explicit guidance with examples and anti-patterns
- Uncertainties: None
- Cross-reference status: References GoTip #25 and #117, the Go blog post on subtests
