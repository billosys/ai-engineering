---
concept: RegExp Match Objects
slug: regexp-match-objects
category: standard-library
subcategory: regexp
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Regular expressions (RegExp)"
chapter_number: 46
pdf_page: null
section: "46.14 Match objects"
extraction_confidence: high
aliases:
  - regex match result
prerequisites:
  - regular-expression-creation
  - regexp-capture-groups
extends: []
related:
  - regexp-methods
contrasts_with: []
answers_questions:
  - "How do I write and use regular expressions in JavaScript?"
---

# Quick Definition

A match object is the result of methods like `string.match()` (without `/g`) and `regExp.exec()`, containing the full match at index 0, capture group values at subsequent indices, a `.groups` property for named captures, and `.index` for the match position.

# Core Definition

"Exploring JavaScript" Ch. 46 describes match objects as array-like objects returned by regex matching methods. They contain: the full match (index 0), numbered capture groups (indices 1+), `.index` (where the match starts), `.input` (the input string), and `.groups` (named capture groups as an object). With flag `/d` (ES2022), `.indices` provides start/end positions for each group.

# Prerequisites

- **Regular expression creation** -- match objects are produced by regex methods
- **RegExp capture groups** -- groups populate match object entries

# Key Properties

1. Index 0: the full match
2. Indices 1+: numbered capture group values
3. `.index`: position of the match in the string
4. `.input`: the original input string
5. `.groups`: object of named capture groups (ES2018)
6. `.indices`: match start/end positions with flag `/d` (ES2022)

# Construction / Recognition

```js
const match = 'abc'.match(/a(b)(c)/);
// match[0] === 'abc' (full match)
// match[1] === 'b' (group 1)
// match[2] === 'c' (group 2)
// match.index === 0
```

# Context & Application

Match objects are the primary way to extract structured data from regex matches.

# Examples

Referenced throughout Ch. 46, Section 46.14 and the methods sections.

# Relationships

## Builds Upon
- **RegExp capture groups** -- groups appear in match objects

## Related
- **RegExp methods** -- methods that return match objects

# Common Errors

- **Error**: Expecting `match()` with `/g` to return match objects
  **Correction**: With `/g`, `match()` returns an Array of strings; use `matchAll()` for match objects

# Common Confusions

- **Confusion**: Match objects are regular Arrays
  **Clarification**: They are array-like objects with extra properties (`.index`, `.groups`)

# Source Reference

Chapter 46: Regular expressions (RegExp), Section 46.14.

# Verification Notes

- Definition source: synthesized from multiple sections
- Confidence rationale: high -- match objects described across multiple sections
- Cross-reference status: verified
