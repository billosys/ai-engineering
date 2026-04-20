---
# === CORE IDENTIFICATION ===
concept: String Methods Overview
slug: string-methods-overview

# === CLASSIFICATION ===
category: primitive-types
subcategory: strings
tier: intermediate

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Strings"
chapter_number: 22
pdf_page: null
section: "String methods"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - string-type
extends: []
related:
  - string-concatenation
  - string-comparison
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

JavaScript strings provide methods for finding substrings (`.includes()`, `.indexOf()`), extracting parts (`.slice()`), splitting/joining (`.split()`, `.join()`), transforming (`.toUpperCase()`, `.trim()`, `.repeat()`, `.padStart()`), and more.

# Core Definition

JavaScript strings have a rich set of built-in methods organized into categories: finding/matching (`.includes()`, `.startsWith()`, `.endsWith()`, `.indexOf()`, `.lastIndexOf()`), extracting (`.slice()`, `.at()`), splitting/joining (`.split()` / `Array.join()`), padding/trimming (`.padStart()`, `.padEnd()`, `.trim()`, `.trimStart()`, `.trimEnd()`), and transforming (`.repeat()`, `.toUpperCase()`, `.toLowerCase()`) (Ch. 22, Section 22.1.3).

# Prerequisites

- **string-type** -- methods are called on strings

# Key Properties

1. Finding: `.includes()`, `.startsWith()`, `.endsWith()`, `.indexOf()`, `.lastIndexOf()`
2. Extracting: `.slice(start, end)`, `.at(index)` (supports negative indices)
3. Splitting: `.split(separator)` returns array
4. Joining: `Array.join(separator)` joins array into string
5. Padding: `.padStart(len, fillStr)`, `.padEnd(len, fillStr)`
6. Trimming: `.trim()`, `.trimStart()`, `.trimEnd()`
7. Case: `.toUpperCase()`, `.toLowerCase()`
8. Repeating: `.repeat(count)`
9. All methods return new strings (strings are immutable)

# Construction / Recognition

```js
'abca'.includes('a')     // true
'abca'.startsWith('ab')  // true
'abca'.indexOf('a')      // 0
'abc'.slice(0, 2)        // 'ab'
'7'.padStart(3, '0')     // '007'
'\t abc\n '.trim()       // 'abc'
'*'.repeat(5)            // '*****'
'ABC'.toLowerCase()      // 'abc'
```

# Context & Application

String methods are fundamental to text processing in JavaScript. Understanding the full API prevents reinventing common operations.

# Examples

From the source text:

```js
> 'abca'.includes('a')
true
> 'abca'.startsWith('ab')
true
> 'abca'.endsWith('ca')
true
> 'abca'.indexOf('a')
0
> 'abca'.lastIndexOf('a')
3

> '7'.padStart(3, '0')
'007'
> 'yes'.padEnd(6, '!')
'yes!!!'

> '\t abc\n '.trim()
'abc'
> '*'.repeat(5)
'*****'
> '= b2b ='.toUpperCase()
'= B2B ='

> 'a, b,c'.split(/, ?/)
['a', 'b', 'c']
> ['a', 'b', 'c'].join(', ')
'a, b, c'
```

# Relationships

## Builds Upon
- **string-type** — methods operate on strings

## Enables
- Text processing and manipulation

## Related
- **string-concatenation** — building strings
- **string-comparison** — comparing strings

## Contrasts With
- None

# Common Errors

- **Error**: Expecting string methods to modify the original string
  **Correction**: Strings are immutable. All methods return new strings.

# Common Confusions

- **Confusion**: Thinking `.slice()` and `.substring()` are identical
  **Clarification**: `.slice()` supports negative indices; `.substring()` does not. `.slice()` is generally preferred.

# Source Reference

Chapter 22: Strings, Sections 22.1.3 and 22.8, lines 192-257.

# Verification Notes

- Definition source: direct (cheat sheet in source)
- Confidence rationale: Comprehensive method listing
- Cross-reference status: verified
