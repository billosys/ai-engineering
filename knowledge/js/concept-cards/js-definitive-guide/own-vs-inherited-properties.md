---
# === CORE IDENTIFICATION ===
concept: Own vs. Inherited Properties
slug: own-vs-inherited-properties

# === CLASSIFICATION ===
category: objects
subcategory: property-system
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Objects"
chapter_number: 6
pdf_page: 147
section: "6.1 Introduction to Objects"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - objects-as-property-collections
  - prototype-objects
extends: []
related:
  - prototype-chain
  - property-existence-testing
  - enumerating-properties
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the prototype chain?"
  - "What distinguishes Object.keys() from for/in?"
---

# Quick Definition

An *own property* is defined directly on an object; an *inherited property* is one obtained from the object's prototype chain. JavaScript uses the term "own property" to distinguish non-inherited properties.

# Core Definition

"It is sometimes important to be able to distinguish between properties defined directly on an object and those that are inherited from a prototype object. JavaScript uses the term *own property* to refer to non-inherited properties." (Ch. 6, §6.1)

# Prerequisites

- **objects-as-property-collections** — Properties are the elements being classified.
- **prototype-objects** — Inheritance is the mechanism that creates inherited properties.

# Key Properties

1. Own properties are defined directly on the object (e.g., via assignment or literal).
2. Inherited properties come from the prototype chain.
3. `hasOwnProperty()` returns `true` only for own properties.
4. `propertyIsEnumerable()` returns `true` only for own, enumerable properties.
5. `Object.keys()` returns only own enumerable properties.
6. `for/in` enumerates both own and inherited enumerable properties.
7. Setting a property always creates/modifies an own property, even if an inherited property with the same name exists.

# Construction / Recognition

```js
let o = {x: 1};                    // x is an own property
o.hasOwnProperty("x")             // => true
o.hasOwnProperty("toString")      // => false (inherited from Object.prototype)
```

# Context & Application

The own-vs-inherited distinction is fundamental to JavaScript's prototype-based inheritance model. It affects property enumeration, existence testing, and property assignment behavior.

# Examples

From the source text (§6.1, §6.3.2, §6.5):

```js
let o = { x: 1 };
"x" in o                        // => true (own property)
"toString" in o                  // => true (inherited property)
o.hasOwnProperty("x")           // => true
o.hasOwnProperty("toString")    // => false

// Setting overrides inherited property
let parent = { r: 1 };
let child = Object.create(parent);
child.r = 2;          // Creates own property, hides inherited one
parent.r              // => 1 (prototype unaffected)
```

# Relationships

## Builds Upon
- **objects-as-property-collections** — Properties being classified
- **prototype-objects** — Source of inherited properties

## Enables
- **property-existence-testing** — Different methods test own vs. any property
- **enumerating-properties** — Different tools enumerate own vs. all properties

## Related
- **prototype-chain** — The chain determines what is inherited

## Contrasts With
- No direct contrast — own and inherited are the two categories

# Common Errors

- **Error**: Using `for/in` when only own properties are desired.
  **Correction**: Use `Object.keys()` with `for/of`, or filter `for/in` with `hasOwnProperty()`.

# Common Confusions

- **Confusion**: Believing property assignment modifies the prototype.
  **Clarification**: Setting a property always creates or modifies an own property on the target object. The prototype chain is never modified by assignment.

# Source Reference

Chapter 6: Objects, Section 6.1 (p. 147), Section 6.3.2 (pp. 152-154).

# Verification Notes

- Definition source: Direct quote from §6.1
- Confidence rationale: High — foundational concept clearly stated
- Uncertainties: None
- Cross-reference status: Verified against §6.3.2, §6.5, §6.6
