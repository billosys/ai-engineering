---
concept: "Array .flatMap() Method"
slug: array-flat-map
category: collections
subcategory: arrays
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Arrays (Array)"
chapter_number: 34
pdf_page: null
section: "34.14.3 .flatMap(): Each input element produces zero or more output elements"
extraction_confidence: high
aliases:
  - ".flatMap()"
  - "Array.prototype.flatMap"
prerequisites:
  - array-creation
  - array-map
extends: []
related:
  - array-filter
  - array-map
contrasts_with:
  - array-map
answers_questions:
  - "How do I use array methods like `.map()`, `.filter()`, and `.reduce()`?"
---

# Quick Definition

`.flatMap()` (ES2019) maps each input element to zero or more output elements by having the callback return arrays, then flattens the results into a single output Array -- enabling simultaneous filtering and mapping.

# Core Definition

With `.flatMap()`, each input Array element is translated to zero or more output elements. The callback returns an Array of values (or a single non-Array value). The resulting arrays are flattened one level. This enables filtering and mapping simultaneously: return `[]` to skip, `[value]` to keep, and `[v1, v2]` to expand.

# Prerequisites

- **array-creation** -- operates on arrays
- **array-map** -- builds on map concept

# Key Properties

1. Introduced in ES2019
2. Callback returns Array (or single value)
3. Results flattened one level
4. Can filter (return []), keep (return [value]), or expand (return [v1, v2])
5. Combines filter + map in one step

# Construction / Recognition

```js
['a', 'b', 'c'].flatMap(x => [x, x]); // ['a','a','b','b','c','c']
['a', 'b', 'c'].flatMap(x => []);      // []
```

# Context & Application

Use `.flatMap()` when each input element may produce a variable number of outputs, or when you need to filter and transform simultaneously.

# Examples

```js
// Filter and map simultaneously
const result = [
  { status: 'fulfilled', value: 'dog.jpg' },
  { status: 'rejected', reason: 'NOT FOUND' },
];
result.flatMap(r => r.status === 'fulfilled' ? [r.value] : []);
// ['dog.jpg']

// One input -> many outputs
function stringsToCodePoints(strs) {
  return strs.flatMap(str => Array.from(str));
}
stringsToCodePoints(['many', 'a']); // ['m','a','n','y','a']
```

(Chapter 34, Section 34.14.3, lines 1789-1921)

# Relationships

## Builds Upon
- **array-map** -- extends the mapping concept

## Enables
- Filter+map in one pass
- One-to-many transformations

## Related
- **array-filter** -- flatMap can replace filter+map chains

## Contrasts With
- **array-map** -- `.map()` is always 1:1; `.flatMap()` is 1:N

# Common Errors

- **Error**: Returning nested arrays expecting deep flattening.
  **Correction**: `.flatMap()` only flattens one level. For deeper flattening, use `.flat(depth)`.

# Common Confusions

- **Confusion**: `.flatMap()` and `.map().flat()` are different.
  **Clarification**: They produce the same result, but `.flatMap()` is more efficient (one pass).

# Source Reference

Chapter 34: Arrays (Array), Section 34.14.3, lines 1789-1921.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with ES2019 marker and use cases
- Cross-reference status: verified
