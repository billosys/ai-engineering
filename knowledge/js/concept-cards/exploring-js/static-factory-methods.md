---
concept: Static Factory Methods
slug: static-factory-methods
category: classes
subcategory: static
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Classes"
chapter_number: 31
pdf_page: null
section: "31.6.8 Static factory methods"
extraction_confidence: high
aliases:
  - "factory method"
prerequisites:
  - static-members
extends: []
related:
  - constructor-method
contrasts_with: []
answers_questions:
  - "How do I provide alternative construction patterns for a class?"
---

# Quick Definition

Static factory methods are descriptive static methods that create instances in alternative ways, offering clearer intent than constructor overloading.

# Core Definition

As described in "Exploring JavaScript" Ch. 31, when there are multiple ways to instantiate a class, static factory methods (e.g., `Point.fromPolar()`) provide descriptive names. JavaScript's standard library uses them too: `Array.from()`, `Object.create()`. The author prefers either no factory methods or only factory methods (making the constructor private via a secret token).

# Prerequisites

- Static members

# Key Properties

1. Descriptive names clarify construction intent.
2. Standard library examples: `Array.from()`, `Object.create()`.
3. Can make constructor private via a secret token pattern.

# Construction / Recognition

```js
class Point {
  static fromPolar(radius, angle) {
    return new Point(radius * Math.cos(angle), radius * Math.sin(angle));
  }
  constructor(x=0, y=0) { this.x = x; this.y = y; }
}
```

# Context & Application

Use when a class has multiple construction patterns or when the constructor needs to be restricted.

# Examples

From the source text (Ch. 31, section 31.6.8):

```js
assert.deepEqual(
  Point.fromPolar(13, 0.39479111969976155),
  new Point(12, 5)
);
```

# Relationships

## Builds Upon
- **Static Members** -- factory methods are static methods

## Related
- **Constructor Method** -- the standard construction entry point

# Source Reference

Chapter 31: Classes, Section 31.6.8, lines 2278-2349.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit pattern with standard library examples
- Cross-reference status: verified
