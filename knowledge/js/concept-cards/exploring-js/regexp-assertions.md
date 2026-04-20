---
concept: RegExp Assertions
slug: regexp-assertions
category: standard-library
subcategory: regexp
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Regular expressions (RegExp)"
chapter_number: 46
pdf_page: null
section: "46.9 Syntax: assertions"
extraction_confidence: high
aliases:
  - regex assertions
  - lookahead
  - lookbehind
  - anchors
prerequisites:
  - regular-expression-creation
extends: []
related:
  - regexp-flags
contrasts_with: []
answers_questions:
  - "How do I write and use regular expressions in JavaScript?"
---

# Quick Definition

Assertions match positions rather than characters: `^` (start), `$` (end), `\b` (word boundary), and lookaround assertions -- positive/negative lookahead (`(?=...)`, `(?!...)`) since ES3, and positive/negative lookbehind (`(?<=...)`, `(?<!...)`) since ES2018.

# Core Definition

"Exploring JavaScript" Ch. 46 lists: "^ matches only at the beginning of the input. $ matches only at the end of the input. \b matches only at a word boundary." Plus four lookaround assertions: positive lookahead `(?=pattern)` (ES3), negative lookahead `(?!pattern)` (ES3), positive lookbehind `(?<=pattern)` (ES2018), negative lookbehind `(?<!pattern)` (ES2018).

# Prerequisites

- **Regular expression creation** -- assertions are pattern elements

# Key Properties

1. Anchors: `^` (start), `$` (end), `\b` (word boundary), `\B` (non-boundary)
2. Positive lookahead `(?=...)`: matches if pattern follows (ES3)
3. Negative lookahead `(?!...)`: matches if pattern does NOT follow (ES3)
4. Positive lookbehind `(?<=...)`: matches if pattern precedes (ES2018)
5. Negative lookbehind `(?<!...)`: matches if pattern does NOT precede (ES2018)
6. Assertions are zero-width: they don't consume characters

# Construction / Recognition

```js
> 'abcX def'.match(/[a-z]+(?=X)/g)      // positive lookahead
[ 'abc' ]
> 'Xabc def'.match(/(?<=X)[a-z]+/g)     // positive lookbehind
[ 'abc' ]
> 'Node.js: index.js'.replace(/(?<!Node)\.js/g, '.html')
'Node.js: index.html'
```

(Ch. 46, Section 46.9, lines 1057-1211)

# Context & Application

Assertions enable precise matching at specific positions. Lookarounds are essential for matching patterns adjacent to specific text without including that text in the match.

# Examples

Replace ".js" but not in "Node.js":
```js
> 'Node.js: index.js and main.js'.replace(/(?<!Node)\.js/g, '.html')
'Node.js: index.html and main.html'
```

(Ch. 46, Section 46.9.2, lines 1205-1210)

# Relationships

## Builds Upon
- **Regular expression creation** -- assertions are pattern syntax

## Related
- **RegExp flags** -- `/m` flag changes `^` and `$` to per-line matching

# Common Errors

- **Error**: Expecting lookaround patterns to consume characters
  **Correction**: Lookarounds are zero-width; the matched text does not include the lookaround pattern

# Common Confusions

- **Confusion**: `^` always means "start of string"
  **Clarification**: With flag `/m`, `^` matches the start of each line

# Source Reference

Chapter 46: Regular expressions (RegExp), Section 46.9, lines 1057-1211.

# Verification Notes

- Definition source: direct from source text with table
- Confidence rationale: explicit list with ES version annotations
- Cross-reference status: verified
