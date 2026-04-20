---
concept: Use Raw String Literals
slug: use-raw-string-literals
category: style
subcategory: string-handling
tier: foundational
source: "Uber Go Style Guide"
source_slug: uber-style
authors: "Prashant Varanasi, Simon Newton"
chapter: "Style"
chapter_number: 4
pdf_page: null
section: "Use Raw String Literals to Avoid Escaping"
extraction_confidence: high
aliases:
  - raw string literals
  - backtick strings
prerequisites: []
extends: []
related: []
contrasts_with: []
answers_questions:
  - "When should I use backtick strings in Go?"
  - "How do I avoid escape sequences in Go strings?"
---

# Quick Definition

Use raw string literals (backtick-delimited strings) to avoid hand-escaped characters. Raw strings can span multiple lines and include quotes without backslash escaping, making them significantly easier to read.

# Core Definition

Go supports raw string literals delimited by backticks (`` ` ``), which interpret no escape sequences. The Uber Go Style Guide recommends using these to avoid hand-escaped strings, which are harder to read and maintain.

Raw string literals can span multiple lines and include double quotes, single quotes, and most special characters without any escaping.

# Prerequisites

- Knowledge of Go's two string literal forms (interpreted `"..."` and raw `` `...` ``)

# Key Properties

1. **No escape sequences**: Raw strings interpret backslashes literally, eliminating `\"`, `\\`, `\n`, etc.
2. **Multi-line support**: Raw strings can span multiple lines without concatenation.
3. **Contains quotes directly**: Double quotes appear literally inside backtick strings.
4. **Cannot contain backticks**: The only character a raw string literal cannot contain is the backtick itself.

# Construction / Recognition

**Good -- raw string literal:**

```go
wantError := `unknown error:"test"`
```

**Bad -- escaped interpreted string:**

```go
wantError := "unknown name:\"test\""
```

# Context & Application

Raw string literals are particularly useful for test assertions containing quoted strings, regular expressions, SQL queries, JSON templates, and any string where escape sequences would reduce readability. Use interpreted strings when you need escape sequences like `\n` or `\t`, or when the string must contain a backtick.

# Examples

**Test assertion with quotes:**

```go
wantError := `unknown error:"test"`
```

**Multi-line string:**

```go
query := `
  SELECT *
  FROM users
  WHERE name = "test"
`
```

# Relationships

None directly referenced in the source for this section.

# Common Errors

1. Using interpreted strings with heavy escaping when a raw string would be clearer.
2. Attempting to include a backtick inside a raw string literal -- this is not possible; use string concatenation or an interpreted string instead.

# Common Confusions

- **Raw strings and newlines**: Raw strings preserve literal newlines. If you do not want a leading newline, start the content on the same line as the opening backtick.
- **Raw strings and `\n`**: The characters `\n` in a raw string are the literal backslash and `n`, not a newline.

# Source Reference

Uber Go Style Guide, "Style" chapter, "Use Raw String Literals to Avoid Escaping" section.

# Verification Notes

Confidence: high. The guideline and code example are directly from the source text with an explicit Bad/Good comparison.
