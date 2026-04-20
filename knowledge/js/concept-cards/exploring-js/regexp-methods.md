---
concept: RegExp Methods
slug: regexp-methods
category: standard-library
subcategory: regexp
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Regular expressions (RegExp)"
chapter_number: 46
pdf_page: null
section: "46.15 Methods for working with regular expressions"
extraction_confidence: high
aliases:
  - regex methods
  - string regex methods
prerequisites:
  - regular-expression-creation
  - regexp-flags
extends: []
related:
  - regexp-capture-groups
  - regexp-match-objects
contrasts_with: []
answers_questions:
  - "How do I write and use regular expressions in JavaScript?"
---

# Quick Definition

JavaScript provides regex methods on both String and RegExp: `string.match()`, `string.matchAll()` (ES2020), `string.replace()`/`replaceAll()`, `string.search()`, `string.split()`, `regExp.test()`, and `regExp.exec()` for matching, replacing, searching, and splitting.

# Core Definition

"Exploring JavaScript" Ch. 46 covers key methods: `string.match(regExp)` without `/g` returns a match object for the first match; with `/g` returns all group-0 captures. `string.matchAll(regExp)` (ES2020) returns an iterable over all match objects. `regExp.test(str)` returns boolean. `string.replace()` and `string.replaceAll()` perform substitutions. "By default, regular expressions match anywhere in a string."

# Prerequisites

- **Regular expression creation** -- methods operate on RegExp objects
- **RegExp flags** -- flags change method behavior (especially `/g`)

# Key Properties

1. `string.match(re)` without `/g`: first match object (ES3)
2. `string.match(re)` with `/g`: Array of all matches (ES3)
3. `string.matchAll(re)`: iterable of match objects, requires `/g` (ES2020)
4. `regExp.exec(str)`: match object, advances `.lastIndex` with `/g` (ES3)
5. `regExp.test(str)`: boolean (ES3)
6. `string.replace(re, replacement)`: first match or all with `/g` (ES3)
7. `string.replaceAll(re, replacement)`: all matches, requires `/g` (ES2021)
8. `string.search(re)`: index of first match (ES3)
9. `string.split(re)`: split by regex (ES3)

# Construction / Recognition

```js
> 'abcX def'.match(/[a-z]+/g)
[ 'abc', 'def' ]
> /abc/.test('xabcx')
true
> 'hello world'.replace(/world/, 'JS')
'hello JS'
```

(Ch. 46, Section 46.15, various lines)

# Context & Application

These methods are the primary interface for using regex in JavaScript. Choose based on need: test for existence, extract matches, replace text, or split strings.

# Examples

Using `matchAll` for all match objects:
```js
const str = 'test1 test2';
for (const match of str.matchAll(/test(\d)/g)) {
  console.log(match[0], match[1]); // 'test1' '1', 'test2' '2'
}
```

(Ch. 46, Section 46.15.4)

# Relationships

## Builds Upon
- **Regular expression creation** -- methods require RegExp objects
- **RegExp flags** -- `/g` fundamentally changes method behavior

## Related
- **RegExp capture groups** -- results appear in match objects

# Common Errors

- **Error**: Using `matchAll()` without the `/g` flag
  **Correction**: `matchAll()` requires the `/g` flag; otherwise it throws

# Common Confusions

- **Confusion**: `match()` with `/g` returns match objects
  **Clarification**: With `/g`, `match()` returns an Array of matched strings (group 0 only); use `matchAll()` for full match objects

# Source Reference

Chapter 46: Regular expressions (RegExp), Section 46.15, lines 1097-1541.

# Verification Notes

- Definition source: synthesized from multiple subsections
- Confidence rationale: all methods explicitly described
- Cross-reference status: verified
