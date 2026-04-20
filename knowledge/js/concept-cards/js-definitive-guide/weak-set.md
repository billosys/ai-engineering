---
concept: WeakSet
slug: weak-set
category: standard-library
subcategory: collections
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "The JavaScript Standard Library"
chapter_number: 11
pdf_page: 292
section: "11.1.3 WeakMap and WeakSet"
extraction_confidence: high
aliases: []
prerequisites:
  - set-class
extends: []
related:
  - weak-map
contrasts_with:
  - set-class
answers_questions: []
---

# Quick Definition

A variant of Set that holds weak references to its object members, allowing garbage collection of those objects when no other references exist.

# Core Definition

"WeakSet implements a set of objects that does not prevent those objects from being garbage collected" (p. 292). Like WeakMap, it only allows objects as members, supports only `add()`, `has()`, and `delete()`, is not iterable, and has no `size` property.

# Prerequisites

- **set-class** — WeakSet is a restricted variant of Set

# Key Properties

1. Members must be objects — no primitive values
2. Holds weak references to members
3. Only `add()`, `has()`, `delete()` methods
4. Not iterable; no `size` property

# Construction / Recognition

```js
let branded = new WeakSet();
branded.add(someObject);
branded.has(someObject); // => true
```

# Context & Application

Used to "brand" or mark objects as having a special property or type without preventing garbage collection. Check membership with `has()` without keeping objects alive.

# Examples

From the source text (p. 292): Marking objects with a special property by adding them to a WeakSet, then testing for that property by checking membership. Unlike a regular Set, this does not prevent the marked objects from being garbage collected.

# Relationships

## Builds Upon
- **Set Class** — WeakSet is a restricted variant of Set

## Related
- **WeakMap** — The Map equivalent with weak references

## Contrasts With
- **Set Class** — Set holds strong references and is iterable; WeakSet holds weak references and is not

# Common Errors

- **Error**: Trying to add a primitive value to a WeakSet.
  **Correction**: Only objects can be WeakSet members.

# Common Confusions

- **Confusion**: Expecting WeakSet to be iterable.
  **Clarification**: WeakSet cannot be iterated because its contents depend on garbage collection.

# Source Reference

Chapter 11: The JavaScript Standard Library, Section 11.1.3, page 292.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: High — clearly described
- Uncertainties: None
- Cross-reference status: Verified
