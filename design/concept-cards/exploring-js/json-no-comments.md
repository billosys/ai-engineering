---
concept: JSON Does Not Support Comments
slug: json-no-comments
category: standard-library
subcategory: json
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Creating and parsing JSON (JSON)"
chapter_number: 48
pdf_page: null
section: "48.5.1 Why doesn't JSON support comments?"
extraction_confidence: high
aliases: []
prerequisites:
  - json-format
extends: []
related: []
contrasts_with: []
answers_questions:
  - "How do I work with JSON (stringify and parse)?"
---

# Quick Definition

JSON intentionally does not support comments. Douglas Crockford removed them because people were using them as parsing directives, which would have destroyed interoperability. The grammar is frozen and will never add them.

# Core Definition

"Exploring JavaScript" Ch. 48 quotes Crockford: "I removed comments from JSON because I saw people were using them to hold parsing directives, a practice which would have destroyed interoperability." His suggestion for commented config files: "insert all the comments you like. Then pipe it through JSMin before handing it to your JSON parser."

# Prerequisites

- **JSON format** -- this is a design decision about JSON

# Key Properties

1. Comments were intentionally removed
2. JSON grammar is frozen -- comments will never be added
3. Workaround: use a preprocessor (JSMin) to strip comments before parsing
4. Alternative formats like JSONC or JSON5 support comments

# Construction / Recognition

Invalid JSON with comments:
```json
{
  // This is NOT valid JSON
  "key": "value"
}
```

# Context & Application

Understanding this limitation prevents frustration when working with JSON configuration files and informs the choice of alternative formats when comments are needed.

# Examples

From the source, Crockford's suggestion: use a minifier to strip comments before parsing.

(Ch. 48, Section 48.5.1, lines 546-557)

# Relationships

## Builds Upon
- **JSON format** -- a design constraint of the format

# Common Errors

- **Error**: Adding comments to JSON files and expecting them to parse
  **Correction**: Use JSONC, JSON5, or strip comments with a preprocessor

# Common Confusions

- **Confusion**: JSON and JavaScript object syntax are identical
  **Clarification**: JSON is a strict subset of JavaScript; it lacks comments, trailing commas, and unquoted keys

# Source Reference

Chapter 48: Creating and parsing JSON, Section 48.5.1, lines 544-557.

# Verification Notes

- Definition source: direct quotation from Crockford via source text
- Confidence rationale: explicit FAQ with Crockford quote
- Cross-reference status: verified
