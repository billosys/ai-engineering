---
concept: RegExp test() and exec() Methods
slug: regexp-test-exec
category: standard-library
subcategory: pattern-matching
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "The JavaScript Standard Library"
chapter_number: 11
pdf_page: 314
section: "11.3.3 The RegExp Class"
extraction_confidence: high
aliases: []
prerequisites:
  - regexp-syntax
extends: []
related:
  - string-match-replace
contrasts_with: []
answers_questions: []
---

# Quick Definition

The RegExp instance methods `test()` (returns boolean) and `exec()` (returns detailed match object or null) for pattern matching, with behavior affected by the `lastIndex` property when using `g` or `y` flags.

# Core Definition

`test()` returns `true` if the string matches the pattern, `false` otherwise. `exec()` returns a match array (with `index`, `input`, and `groups` properties) or `null`. Both methods use and modify the `lastIndex` property when the `g` or `y` flag is set, enabling sequential matching through a string but also creating a significant source of bugs.

# Prerequisites

- **regexp-syntax** — Understanding RegExp patterns and flags

# Key Properties

1. `test()` — simple boolean match test
2. `exec()` — returns detailed match object with groups, index, and input properties
3. With `g`/`y` flags, `lastIndex` advances after each successful match
4. `lastIndex` resets to 0 after a failed match
5. `exec()` always returns one match at a time, even with `g` flag

# Construction / Recognition

```js
let pattern = /Java/g;
let text = "JavaScript > Java";
let match;
while((match = pattern.exec(text)) !== null) {
    console.log(`Matched ${match[0]} at ${match.index}`);
}
```

# Context & Application

`test()` is used for simple validation. `exec()` in a while loop was the traditional way to iterate all matches before `matchAll()` was introduced in ES2020. Use `matchAll()` instead of `exec()` loops when possible.

# Examples

From the source text (p. 315-317): `exec()` loop that runs twice for "JavaScript > Java". The `lastIndex` pitfall: reusing a RegExp literal in a while loop creates infinite loops because a new RegExp with `lastIndex=0` is created each iteration.

# Relationships

## Builds Upon
- **RegExp Syntax** — These are methods on RegExp objects

## Related
- **String match/replace** — The String-side equivalents

# Common Errors

- **Error**: Creating a RegExp literal inside a loop condition: `while((/pattern/g).exec(text))` causes infinite loops.
  **Correction**: Create the RegExp once outside the loop and reuse it.

- **Error**: Using a global RegExp with `test()` in a loop and getting inconsistent results due to `lastIndex`.
  **Correction**: Reset `lastIndex` to 0 before each `test()` call, or don't use the `g` flag if not needed.

# Common Confusions

- **Confusion**: Expecting `exec()` with `g` flag to return all matches at once like `match()` does.
  **Clarification**: `exec()` always returns one match at a time, advancing `lastIndex` for the next call.

# Source Reference

Chapter 11: The JavaScript Standard Library, Section 11.3.3, pages 314-317.

# Verification Notes

- Definition source: Synthesized from source text
- Confidence rationale: High — detailed treatment of `lastIndex` pitfalls
- Uncertainties: None
- Cross-reference status: Verified
