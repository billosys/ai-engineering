---
concept: RegExp Global and Sticky Flags
slug: regexp-global-sticky-flags
category: standard-library
subcategory: regexp
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Regular expressions (RegExp)"
chapter_number: 46
pdf_page: null
section: "46.16 The flags /g and /y, and the property .lastIndex"
extraction_confidence: high
aliases:
  - "/g flag"
  - "/y flag"
  - lastIndex
prerequisites:
  - regexp-flags
extends: []
related:
  - regexp-methods
contrasts_with: []
answers_questions:
  - "How do I write and use regular expressions in JavaScript?"
---

# Quick Definition

Flag `/g` (global) makes regex methods consider all matches in a string rather than just the first. Flag `/y` (sticky, ES6) requires each match to start immediately after the previous one. Both use the `.lastIndex` property to track position.

# Core Definition

"Exploring JavaScript" Ch. 46: "/g (global) fundamentally changes how the following methods work: String.prototype.match(), RegExp.prototype.exec(), RegExp.prototype.test()." Flag `/y` (sticky): "When both [/g and /y] are switched on, any match must directly follow the previous one (that is, it must start at index .lastIndex of the regular expression object). Therefore, the first match must be at index 0."

# Prerequisites

- **RegExp flags** -- `/g` and `/y` are regex flags

# Key Properties

1. `/g`: match multiple times; methods iterate through matches
2. `/y` (ES6): matches must be consecutive (no gaps)
3. Both use `.lastIndex` to track current position
4. `/y` main use case: tokenization during parsing
5. `.lastIndex` is mutable and shared -- pitfall with reuse
6. `string.matchAll()` is preferred over `regExp.exec()` with `/g`

# Construction / Recognition

```js
> 'a1a2 a3'.match(/a./gy)   // sticky: stops at gap
[ 'a1', 'a2' ]
> 'a1a2 a3'.match(/a./g)    // global: matches all
[ 'a1', 'a2', 'a3' ]
```

(Ch. 46, Section 46.11, lines 1527-1537)

# Context & Application

`/g` is essential for finding all matches or performing global replacements. `/y` is specialized for tokenization.

# Examples

See construction example above. (Ch. 46, Section 46.11, lines 1527-1537)

# Relationships

## Builds Upon
- **RegExp flags** -- these are specific flag behaviors

## Related
- **RegExp methods** -- `/g` changes method behavior fundamentally

# Common Errors

- **Error**: Reusing a regex with `/g` without resetting `.lastIndex`
  **Correction**: Create a new regex or manually reset `.lastIndex = 0`

# Common Confusions

- **Confusion**: `/g` and `/y` together work like `/g` alone
  **Clarification**: Together, matches must be consecutive with no gaps between them

# Source Reference

Chapter 46: Regular expressions (RegExp), Sections 46.11, 46.16.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit sections on both flags
- Cross-reference status: verified
