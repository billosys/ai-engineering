---
concept: Lazy Evaluation with Iterators
slug: lazy-evaluation-iterators
category: iterators-generators
subcategory: iterator-protocol
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Iterators and Generators"
chapter_number: 12
pdf_page: 348
section: "12.2 Implementing Iterable Objects"
extraction_confidence: high
aliases:
  - "deferred computation"
  - "lazy iteration"
prerequisites:
  - iterator-protocol
  - custom-iterable-objects
extends: []
related:
  - generator-functions
  - infinite-sequences
contrasts_with: []
answers_questions: []
---

# Quick Definition

The property of iterators and generators where values are computed on demand rather than all at once, enabling memory-efficient processing of large or infinite data sets.

# Core Definition

"One key feature of iterable objects and iterators is that they are inherently lazy: when computation is required to compute the next value, that computation can be deferred until the value is actually needed" (p. 348). This allows processing data without loading everything into memory.

# Prerequisites

- **iterator-protocol** — Lazy evaluation is a property of iterators
- **custom-iterable-objects** — Understanding how to build iterables that defer computation

# Key Properties

1. Values computed only when `next()` is called
2. No need to store all values in memory simultaneously
3. Enables processing of infinite sequences
4. Iterable `map()` and `filter()` can be lazy (unlike Array methods)

# Construction / Recognition

```js
function words(s) {
    var r = /\s+|$/g;
    r.lastIndex = s.match(/[^ ]/).index;
    return {
        [Symbol.iterator]() { return this; },
        next() {
            let start = r.lastIndex;
            if (start < s.length) {
                let match = r.exec(s);
                if (match) { return { value: s.substring(start, match.index) }; }
            }
            return { done: true };
        }
    };
}
```

# Context & Application

Essential for processing large files, streams, or computed sequences where materializing all values would be impractical or impossible.

# Examples

From the source text (p. 348): The `words()` function lazily tokenizes a string: `[...words(" abc def ghi! ")]` returns `["abc", "def", "ghi!"]`. Unlike `split()`, it doesn't allocate the entire array upfront.

# Relationships

## Builds Upon
- **Iterator Protocol** — Lazy evaluation is inherent to the pull-based iterator model
- **Custom Iterable Objects** — Lazy iterables must be deliberately designed

## Related
- **Generator Functions** — Generators are naturally lazy
- **Infinite Sequences** — Lazy evaluation enables infinite sequences

# Common Errors

- **Error**: Using the spread operator `[...]` on an infinite lazy iterator.
  **Correction**: Spreading an infinite iterator will exhaust memory. Use `for/of` with a `break` condition, or a `take()` function to limit values.

# Common Confusions

- **Confusion**: Thinking Array's `map()` and `filter()` are lazy.
  **Clarification**: Array methods eagerly produce new arrays. Lazy `map()` and `filter()` must be implemented as iterator-returning functions.

# Source Reference

Chapter 12: Iterators and Generators, Section 12.2, page 348.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
