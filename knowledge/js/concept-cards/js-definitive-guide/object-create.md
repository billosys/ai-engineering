---
# === CORE IDENTIFICATION ===
concept: Object.create()
slug: object-create

# === CLASSIFICATION ===
category: objects
subcategory: object-creation
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Objects"
chapter_number: 6
pdf_page: 149
section: "6.2.4 Object.create()"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - prototype-objects
  - prototype-chain
extends: []
related:
  - object-literals
  - constructor-functions
contrasts_with:
  - object-literals
  - constructor-functions

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the prototype chain?"
---

# Quick Definition

`Object.create()` creates a new object using its first argument as the prototype. Passing `null` creates a prototype-less object; passing `Object.prototype` is equivalent to `{}`.

# Core Definition

"Object.create() creates a new object, using its first argument as the prototype of that object." It also accepts an optional second argument for property descriptors. Passing `null` creates an object with no prototype that "will not inherit anything, not even basic methods like toString()." (Ch. 6, §6.2.4)

# Prerequisites

- **prototype-objects** — `Object.create()` explicitly sets the prototype.
- **prototype-chain** — The argument determines where the new object sits in the chain.

# Key Properties

1. `Object.create({x: 1, y: 2})` creates an object inheriting `x` and `y`.
2. `Object.create(null)` creates a prototypeless object — no inherited methods at all.
3. `Object.create(Object.prototype)` is equivalent to `{}` or `new Object()`.
4. Can be used as a defensive pattern: pass `Object.create(o)` to untrusted code to protect `o` from modification.

# Construction / Recognition

```js
let o = Object.create(prototypeObject);
let o = Object.create(null);
let o = Object.create(Object.prototype);
```

# Context & Application

`Object.create()` is powerful for creating objects with specific prototype chains, creating dictionary objects with no inherited properties (`Object.create(null)`), and guarding objects from modification.

# Examples

From the source text (§6.2.4, pp. 149-150):

```js
let o1 = Object.create({x: 1, y: 2});
o1.x + o1.y     // => 3

let o2 = Object.create(null);      // No prototype — no toString(), etc.
let o3 = Object.create(Object.prototype);  // Same as {} or new Object()

// Defensive pattern: protect original from modification
let o = { x: "don't change this value" };
library.function(Object.create(o));   // Library sees inherited values but can't modify o
```

# Relationships

## Builds Upon
- **prototype-objects** — Explicitly sets the new object's prototype
- **prototype-chain** — Determines the new object's position in the chain

## Enables
- Prototype-based inheritance without constructors
- Dictionary objects (null prototype)

## Related
- **object-literals** — `{}` always uses `Object.prototype`
- **constructor-functions** — `new` sets prototype from constructor's `prototype` property

## Contrasts With
- **object-literals** — Literals always inherit from `Object.prototype`; `Object.create()` can use any prototype
- **constructor-functions** — Constructors run initialization code; `Object.create()` just sets prototype

# Common Errors

- **Error**: Expecting `Object.create(null)` objects to work with `+` operator or `for/in`.
  **Correction**: Without `Object.prototype`, methods like `toString()` are missing. The `+` operator requires `toString()`.

# Common Confusions

- **Confusion**: Expecting `Object.create({x:1})` to create an object with an own property `x`.
  **Clarification**: The properties of the argument are *inherited*, not own. The new object starts with no own properties.

# Source Reference

Chapter 6: Objects, Section 6.2.4, pages 149-150.

# Verification Notes

- Definition source: Direct quote from §6.2.4
- Confidence rationale: High — clear explanation with examples
- Uncertainties: Optional second argument details in §14.1
- Cross-reference status: Verified
