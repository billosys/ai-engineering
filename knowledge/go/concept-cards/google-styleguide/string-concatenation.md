---
# === CORE IDENTIFICATION ===
concept: String Concatenation
slug: string-concatenation

# === CLASSIFICATION ===
category: language
subcategory: strings
tier: foundational

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Best Practices"
chapter_number: 4
pdf_page: null
section: "String concatenation"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "string building"
  - "strings.Builder"
  - "string formatting"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When should I use + vs fmt.Sprintf vs strings.Builder?"
  - "What is the performance difference between string concatenation methods?"
  - "How should I build multi-line constant strings?"
---

# Quick Definition

Use `+` for simple concatenation of a few strings, `fmt.Sprintf` when formatting is involved, and `strings.Builder` for piecemeal construction in loops. Use backtick literals for constant multi-line strings. Write directly to `io.Writer` with `fmt.Fprintf` instead of building intermediate strings.

# Core Definition

Go provides several string concatenation methods, each suited to different situations. The `+` operator is simplest for concatenating a few strings and requires no import. `fmt.Sprintf` is preferred when building complex formatted strings where many `+` operators would obscure the result. `strings.Builder` is preferred for piecemeal construction (building a string bit-by-bit, typically in a loop) because it runs in amortized linear time, whereas sequential `+` and `fmt.Sprintf` take quadratic time for building large strings. When the output destination is an `io.Writer`, use `fmt.Fprintf` directly instead of building a temporary string. For complex formatting beyond `fmt.Sprintf`, use `text/template` or `safehtml/template`. For constant multi-line string literals, prefer backtick (raw string) literals over concatenation with `+`.

# Prerequisites

(none)

# Key Properties

1. `+` operator: simplest, no import needed, for few strings
2. `fmt.Sprintf`: for formatted strings where `+` would obscure the result
3. `strings.Builder`: amortized O(n) for piecemeal construction; `+` is O(n^2) for large strings
4. `fmt.Fprintf`: write directly to `io.Writer` instead of building intermediate strings
5. Backtick literals: for constant multi-line strings
6. `text/template`: for complex formatting beyond `fmt.Sprintf`

# Construction / Recognition

## To Apply:
1. Simple joining: `key := "prefix: " + value`
2. Formatted string: `str := fmt.Sprintf("%s [%s:%d]-> %s", src, qos, mtu, dst)`
3. Loop building: use `strings.Builder` with `fmt.Fprintf(b, ...)`
4. Writing to io.Writer: use `fmt.Fprintf(w, ...)` directly
5. Multi-line constants: use backtick raw strings

## To Recognize:
1. `+` used only for simple cases with few operands
2. `fmt.Sprintf` for formatted output
3. `strings.Builder` in loops

# Context & Application

The quadratic performance of sequential `+` concatenation matters when building large strings in loops. Each `+` operation creates a new string, copying all previous content. `strings.Builder` avoids this by using an internal buffer that grows efficiently. For most code, the choice is a readability concern; for hot paths building large strings, it becomes a performance concern.

# Examples

**Example 1 -- Simple concatenation**:

```go
// Good:
key := "projectid: " + p
```

**Example 2 -- Formatted string**:

```go
// Good:
str := fmt.Sprintf("%s [%s:%d]-> %s", src, qos, mtu, dst)

// Bad:
bad := src.String() + " [" + qos.String() + ":" + strconv.Itoa(mtu) + "]-> " + dst.String()
```

**Example 3 -- Piecemeal construction**:

```go
// Good:
b := new(strings.Builder)
for i, d := range digitsOfPi {
    fmt.Fprintf(b, "the %d digit of pi is: %d\n", i, d)
}
str := b.String()
```

**Example 4 -- Multi-line constants**:

```go
// Good:
usage := `Usage:

custom_tool [args]`

// Bad:
usage := "" +
    "Usage:\n" +
    "\n" +
    "custom_tool [args]"
```

# Relationships

(none)

# Common Errors

- **Error**: Using `+` in a loop to build a large string
  **Correction**: Use `strings.Builder` for O(n) amortized performance

- **Error**: Building a string with `fmt.Sprintf` just to write it to an `io.Writer`
  **Correction**: Use `fmt.Fprintf(w, ...)` to write directly

# Common Confusions

- **Confusion**: Thinking `strings.Builder` is always necessary
  **Clarification**: For simple concatenation of a few strings, `+` is cleaner and sufficient

- **Confusion**: Using double-quoted strings with `\n` for multi-line constants
  **Clarification**: Backtick raw strings are cleaner for multi-line constants

# Source Reference

Chapter 4: Best Practices, Section "String concatenation".

# Verification Notes

- Definition source: Directly from "String concatenation" section with all subsections
- Confidence rationale: HIGH -- explicit guidance with examples for each method
- Uncertainties: None
- Cross-reference status: References GoTip #29: Building Strings Efficiently
