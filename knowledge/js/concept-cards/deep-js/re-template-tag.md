---
# === CORE IDENTIFICATION ===
concept: "re Template Tag"
slug: re-template-tag

# === CLASSIFICATION ===
category: regular-expressions
subcategory: template-tags
tier: advanced

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Composing regular expressions via re-template-tag (bonus)"
chapter_number: 18
section: "18.1 The basics"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - re-template-tag
  - re tagged template

# === TYPED RELATIONSHIPS ===
prerequisites:
  - regular-expressions-basics
  - template-literals
extends: []
related:
  - regex-composition
  - regex-fragment-reuse
  - named-capture-groups-composition
  - computed-regex-flags
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I compose regular expressions using template tags?"
---

# Quick Definition

The `re` template tag is a function from the `re-template-tag` library that composes regular expressions from template literals, automatically extracting regex source from interpolated `RegExp` objects and escaping interpolated strings.

# Core Definition

As introduced in "Deep JavaScript" (Ch 18, Section 18.1): "The library implements the template tag `re` for regular expressions." Installed via `npm install re-template-tag` and imported as `import {re} from 're-template-tag';`. The basic usage is `` re`/pattern/flags` `` which produces a `RegExp` object. Interpolated RegExp objects contribute their `.source`; interpolated strings are escaped.

# Prerequisites

- **Regular expression basics** — Understanding regex syntax and flags.
- **Template literals** — JavaScript tagged template literal syntax.

# Key Properties

1. Import: `import {re} from 're-template-tag';`.
2. Syntax: `` re`/pattern/flags` `` — produces a RegExp.
3. Interpolated **RegExp objects** contribute their `.source` property.
4. Interpolated **strings** are properly escaped.
5. Supports **flag-less mode**: `` re`pattern` `` (no slashes, no flags).
6. Backslashes work as they would in regex literals.

# Construction / Recognition

## To Construct/Create:
1. Import: `import {re} from 're-template-tag';`.
2. Write: `` re`/pattern/flags` `` with interpolations `${...}`.
3. Interpolate RegExp objects for pattern fragments.
4. Interpolate strings for literal text (auto-escaped).

## To Identify/Recognize:
1. A template literal tagged with `re`.
2. The result is a `RegExp` instance.
3. Interpolations contain RegExp objects or strings.

# Context & Application

The `re` template tag makes complex regular expressions more readable and maintainable. The author notes that "the intent is to introduce the ideas behind the library (more than the library itself)." The underlying concept — composing regexes from documented fragments — is the main takeaway.

# Examples

**Example 1** (Ch 18): Basic usage equivalent to a literal:
```js
import {re} from 're-template-tag';

assert.deepEqual(
  re`/abc/gu`,
  /abc/gu);
```

**Example 2** (Ch 18): Composing from fragments:
```js
const RE_YEAR = /([0-9]{4})/;
const RE_MONTH = /([0-9]{2})/;
const RE_DAY = /([0-9]{2})/;
const RE_DATE = re`/^${RE_YEAR}-${RE_MONTH}-${RE_DAY}$/u`;
assert.equal(RE_DATE.source, '^([0-9]{4})-([0-9]{2})-([0-9]{2})$');
```

**Example 3** (Ch 18): String escaping:
```js
assert.equal(re`/-${'.'}-/u`.source, '-\\.-');
```

# Relationships

## Builds Upon
- **Template literals** — The JavaScript tagged template mechanism.
- **RegExp constructor** — The `re` tag ultimately creates a RegExp.

## Enables
- **Regex composition** — The primary purpose.
- **Fragment reuse** — Define once, compose many times.
- **Safe string insertion** — Automatic escaping prevents injection.

## Related
- **Computed regex flags** — Flags can be interpolated too.
- **Named capture groups composition** — Named groups work well with `re`.

## Contrasts With
- **`new RegExp(string)`** — Manual construction without automatic escaping or fragment support.
- **Regex literals** — No composition or interpolation support.

# Common Errors

- **Error**: Forgetting the slashes in `` re`/pattern/flags` ``.
  **Correction**: The slashes are part of the `re` tag syntax (mimicking regex literals). Without them, use the flag-less mode: `` re`pattern` ``.

# Common Confusions

- **Confusion**: Thinking `re` modifies the behavior of the regex engine.
  **Clarification**: `re` only constructs a standard `RegExp` object. The regex engine behavior is identical to any other RegExp.

# Source Reference

Chapter 18: Composing regular expressions via re-template-tag, Section 18.1, lines 8282-8355.

# Verification Notes

- Definition source: direct (from library introduction and examples)
- Confidence rationale: Explicitly described with install, import, and usage examples
- Cross-reference status: verified against Section 18.2 feature tour
