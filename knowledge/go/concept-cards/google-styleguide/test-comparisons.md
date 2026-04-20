---
# === CORE IDENTIFICATION ===
concept: Test Comparison Techniques
slug: test-comparisons

# === CLASSIFICATION ===
category: testing
subcategory: comparison-patterns
tier: intermediate

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Style Decisions"
chapter_number: 3
pdf_page: null
section: "Full structure comparisons"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "cmp.Equal usage"
  - "cmp.Diff usage"
  - "deep comparison"
  - "struct comparison in tests"
  - "print diffs"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - test-failure-messages
  - assertion-libraries
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How should I compare structs in Go tests?"
  - "When should I use cmp.Diff vs cmp.Equal?"
  - "Should I compare individual fields or entire structs?"
  - "How do I compare protocol buffer messages in tests?"
  - "Why should I avoid reflect.DeepEqual?"
  - "When should I print diffs instead of full values?"
---

# Quick Definition

Use `cmp.Equal` and `cmp.Diff` for structural comparisons in tests. Compare full structures rather than field-by-field. Compare stable, semantically relevant results rather than serialized output. Print diffs for large values instead of printing both got and want in full.

# Core Definition

This concept combines four related comparison guidelines. **Full structure comparisons**: when a function returns a struct, compare the entire struct using deep comparison rather than hand-coding field-by-field checks (unless irrelevant fields would obscure the test intent). Use `cmpopts` for structs with uncomparable fields. **Compare stable results**: do not compare against output that may change (like `json.Marshal` byte output); compare semantically equivalent data structures instead. **Equality comparison and diffs**: use `cmp.Equal` for equality and `cmp.Diff` for human-readable diffs; prefer `cmp` over `reflect.DeepEqual` (which is sensitive to unexported fields) and over `pretty` (which has known limitations). For protocol buffers, pass `protocmp.Transform()` to `cmp`. **Print diffs**: for large values, compute and print a diff rather than showing both full values; always label the diff direction (e.g., `(-want +got)`).

# Prerequisites

- **cmp package** -- `github.com/google/go-cmp/cmp` for `cmp.Equal` and `cmp.Diff`
- **Go testing basics** -- `t.Errorf` and `t.Fatalf`
- **test-failure-messages** -- Understanding the got-before-want convention

# Key Properties

1. **Full struct comparison**: Compare entire structs, not individual fields
2. **cmp over reflect.DeepEqual**: `reflect.DeepEqual` is sensitive to unexported fields and implementation details
3. **cmp over pretty**: `pretty` treats nil slices and empty slices as equal, among other limitations
4. **cmpopts for special cases**: Use `cmpopts.IgnoreInterfaces` and similar for uncomparable fields
5. **protocmp.Transform()**: Required when comparing protocol buffer messages with `cmp`
6. **Stable comparisons**: Compare parsed data structures, not serialized strings or bytes
7. **Diff for large values**: Use `cmp.Diff` and print a diff rather than two full values
8. **Label diff direction**: Always include `(-want +got)` or equivalent in the message
9. **cmp is for testing only**: The `cmp` package may panic in production code; use it only in tests

# Construction / Recognition

## To Apply:
1. Construct expected output as a struct literal and compare with `cmp.Equal`
2. For large or complex types, use `cmp.Diff` and print the diff
3. Label diff output: `(-want +got):\n%s`
4. For protos, add `protocmp.Transform()` option
5. Compare parsed/structured data, not serialized output
6. Multiple return values can be compared individually without wrapping in a struct

## To Recognize:
1. Hand-coded field-by-field struct comparison in tests
2. `reflect.DeepEqual` usage (should be updated to `cmp`)
3. String comparison of `json.Marshal` output
4. Diffs printed without direction labels

# Context & Application

Full structure comparison catches bugs in fields that hand-coded tests might not check. Comparing stable, semantic data prevents tests from becoming change detectors that break whenever a dependency changes its serialization format. Using `cmp.Diff` for large values makes test failures immediately diagnostic -- developers see exactly which fields differ rather than scanning two large output blocks.

# Examples

**Example 1 -- Full struct comparison with cmp.Equal**:

```go
// Good:
want := &Doc{
    Type:     "blogPost",
    Comments: 2,
    Body:     "This is the post body.",
    Authors:  []string{"isaac", "albert", "emmy"},
}
if !cmp.Equal(got, want) {
    t.Errorf("AddPost() = %+v, want %+v", got, want)
}
```

**Example 2 -- Diff with protocol buffers**:

```go
// Good:
if diff := cmp.Diff(want, got, protocmp.Transform()); diff != "" {
    t.Errorf("Foo() returned unexpected difference (-want +got):\n%s", diff)
}
```

**Example 3 -- Stable comparison (avoid serialized output)**:

```go
// Bad: comparing json.Marshal output (unstable)
// Good: parse the JSON and compare the resulting data structures
```

**Example 4 -- Multiple return values (no struct wrapping needed)**:

```go
// Good:
val, multi, tail, err := strconv.UnquoteChar(`\"...\"`, '"')
if err != nil {
    t.Fatalf(...)
}
if val != `"` {
    t.Errorf(...)
}
```

# Relationships

## Related
- **test-failure-messages** -- Comparison results feed into failure messages following got-before-want conventions
- **assertion-libraries** -- The `cmp` package is the preferred alternative to assertion libraries

# Common Errors

- **Error**: Using `reflect.DeepEqual` for struct comparison
  **Correction**: Use `cmp.Equal` or `cmp.Diff`. `reflect.DeepEqual` is sensitive to unexported fields and implementation details.

- **Error**: Comparing `json.Marshal` output strings for equality
  **Correction**: Parse the output and compare the data structures. Serialization format may change between versions.

- **Error**: Printing both full got and want values for large structs
  **Correction**: Use `cmp.Diff` to print only the differences.

# Common Confusions

- **Confusion**: Thinking `cmp` is suitable for production code
  **Clarification**: `cmp` is designed for testing and may panic when it detects misuse. Do not use it in production.

- **Confusion**: Thinking `pretty.Compare` and `cmp.Diff` are interchangeable
  **Clarification**: `pretty` treats nil slices as equal to empty slices, is insensitive to different interface implementations, and does not handle protobuf well. Prefer `cmp` for new code.

# Source Reference

Chapter 3: Style Decisions, Sections "Full structure comparisons", "Compare stable results", "Equality comparison and diffs", and "Print diffs" under "Useful test failures".

# Verification Notes

- Definition source: Synthesized from four subsections under "Useful test failures"
- Confidence rationale: HIGH -- all four subsections are explicit with detailed examples and rationale
- Uncertainties: None
- Cross-reference status: Related slugs verified against planned extractions
