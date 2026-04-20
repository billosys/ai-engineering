---
# === CORE IDENTIFICATION ===
concept: Computed Regex Flags
slug: computed-regex-flags

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
section: "18.2.2 Details and advanced features"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - dynamic regex flags

# === TYPED RELATIONSHIPS ===
prerequisites:
  - re-template-tag
extends:
  - re-template-tag
related:
  - regex-composition
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I compose regular expressions using template tags?"
---

# Quick Definition

With the `re` template tag, regex flags can be computed at runtime by interpolating a string expression in the flags position, enabling dynamic flag selection.

# Core Definition

As demonstrated in "Deep JavaScript" (Ch 18, Section 18.2.2): "Regular expression flags (such as `/u` in the previous example) can also be computed." The flags portion of `` re`/pattern/flags` `` can contain a `${}` interpolation that evaluates to a string, enabling dynamic flag assembly at runtime.

# Prerequisites

- **`re` template tag** — The composition mechanism.

# Key Properties

1. Flags are placed after the closing `/` in `` re`/pattern/flags` ``.
2. Flags can be **interpolated**: `` re`/abc/${'g'+'u'}` ``.
3. The interpolation must evaluate to a **string** of valid flag characters.
4. The resulting RegExp has the computed flags.

# Construction / Recognition

## To Construct/Create:
1. Use the `re` template tag with flag interpolation: `` re`/pattern/${ flagString }` ``.
2. The flag string is assembled dynamically (e.g., `'g' + 'u'`).

## To Identify/Recognize:
1. A `re` template literal with `${}` in the flags position (after the closing `/`).
2. The interpolated value is a string of flag characters.

# Context & Application

Computed flags enable scenarios where flag selection depends on runtime conditions, such as case-sensitive vs. case-insensitive search based on user preferences, or adding the `u` flag only when Unicode support is needed.

# Examples

**Example 1** (Ch 18): Computed flags:
```js
const regexp = re`/abc/${'g'+'u'}`;
assert.ok(regexp instanceof RegExp);
assert.equal(regexp.source, 'abc');
assert.equal(regexp.flags, 'gu');
```

# Relationships

## Builds Upon
- **`re` template tag** — The composition mechanism.
- **RegExp flags** — `g`, `i`, `m`, `u`, `s`, `y` flag characters.

## Enables
- **Dynamic regex configuration** — Choose flags based on runtime conditions.

## Related
- **Regex composition** — Flags are part of the overall composition.

## Contrasts With
- **Static flag literals** — Standard regex literals (`/pattern/gu`) have fixed flags.

# Common Errors

- **Error**: Interpolating invalid flag characters.
  **Correction**: Only valid RegExp flag characters are allowed. Invalid flags will cause a SyntaxError when the RegExp is constructed.

# Common Confusions

- **Confusion**: Thinking fragment RegExp flags are merged with the composed pattern's flags.
  **Clarification**: Fragment flags are ignored. Only the flags specified on the composed `re` template (including computed ones) apply to the final RegExp.

# Source Reference

Chapter 18: Composing regular expressions via re-template-tag, Section 18.2.2, lines 8393-8411.

# Verification Notes

- Definition source: direct (from source code example)
- Confidence rationale: Explicitly demonstrated with assertion checks
- Cross-reference status: verified against Section 18.1 basic usage
