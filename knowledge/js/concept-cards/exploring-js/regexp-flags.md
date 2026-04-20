---
concept: RegExp Flags
slug: regexp-flags
category: standard-library
subcategory: regexp
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Regular expressions (RegExp)"
chapter_number: 46
pdf_page: null
section: "46.11 Regular expression flags"
extraction_confidence: high
aliases:
  - regex flags
  - regex modifiers
prerequisites:
  - regular-expression-creation
extends: []
related:
  - regexp-flag-v
  - regexp-global-sticky-flags
contrasts_with: []
answers_questions:
  - "How do I write and use regular expressions in JavaScript?"
---

# Quick Definition

JavaScript regular expressions support eight flags that modify matching behavior: `/d` (match indices, ES2022), `/g` (global), `/i` (case-insensitive), `/m` (multiline), `/s` (dotAll, ES2018), `/u` (Unicode, ES6), `/v` (Unicode sets, ES2024, recommended), and `/y` (sticky, ES6).

# Core Definition

"Exploring JavaScript" Ch. 46 provides a comprehensive table of all flags. Key flags: `/g` makes methods consider all matches; `/i` enables case-insensitive matching; `/m` makes `^` and `$` match per line; `/s` makes dot match line terminators; `/u` and `/v` enable Unicode support. The text recommends: "I recommend to use flag /v with all regular expressions."

# Prerequisites

- **Regular expression creation** -- flags modify regex behavior

# Key Properties

1. `/d` (`hasIndices`): match indices in match objects (ES2022)
2. `/g` (`global`): match multiple times (ES3)
3. `/i` (`ignoreCase`): case-insensitive matching (ES3)
4. `/m` (`multiline`): `^`/`$` match per line (ES3)
5. `/s` (`dotAll`): dot matches line terminators (ES2018)
6. `/u` (`unicode`): Unicode code point mode (ES6)
7. `/v` (`unicodeSets`): recommended, improves `/u` (ES2024)
8. `/y` (`sticky`): matches must be consecutive (ES6)
9. Order alphabetically; `/v` and `/u` are mutually exclusive

# Construction / Recognition

```js
/pattern/giv       // global, case-insensitive, Unicode sets
/a./gm             // global, multiline
```

(Ch. 46, Section 46.11, lines 1224-1542)

# Context & Application

Flags are essential for controlling regex behavior. Flag `/v` is recommended for all new regex patterns.

# Examples

```js
> /a/.test('A')     // false (case-sensitive)
> /a/i.test('A')    // true (case-insensitive)
> 'a1\na2\na3'.match(/^a./gm)  // [ 'a1', 'a2', 'a3' ]
> 'a1\na2\na3'.match(/^a./g)   // [ 'a1' ]
```

(Ch. 46, Section 46.11, lines 1462-1483)

# Relationships

## Builds Upon
- **Regular expression creation** -- flags are part of regex definition

## Related
- **RegExp flag /v** -- recommended Unicode sets flag
- **RegExp global and sticky flags** -- advanced flag behavior

# Common Errors

- **Error**: Using both `/u` and `/v` flags together
  **Correction**: They are mutually exclusive; prefer `/v`

# Common Confusions

- **Confusion**: Flags can be changed after creation
  **Clarification**: Flags are immutable; create a new RegExp with desired flags

# Source Reference

Chapter 46: Regular expressions (RegExp), Section 46.11, lines 1224-1542.

# Verification Notes

- Definition source: direct from source text with flag table
- Confidence rationale: explicit comprehensive table
- Cross-reference status: verified
