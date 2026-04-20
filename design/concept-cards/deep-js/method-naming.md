---
# === CORE IDENTIFICATION ===
concept: Method Naming
slug: method-naming

# === CLASSIFICATION ===
category: functions
subcategory: naming
tier: intermediate

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "The property .name of functions (bonus)"
chapter_number: 21
section: "21.2.6 Methods in object literals"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "method .name"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-name-property
extends: []
related:
  - getter-setter-naming
  - symbol-keyed-method-names
  - function-naming-rules
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes a named function expression from an anonymous function?"
---

# Quick Definition

Methods in object literals and class definitions get their `.name` from the property key, whether defined via method shorthand, property definition, computed key, or property value shorthand.

# Core Definition

From "Deep JavaScript" (Ch 21.2.6): "If a function is the value of a property, it gets its name from that property. It doesn't matter if that happens via a method definition (line A), a traditional property definition (line B), a property definition with a computed property key (line C) or a property value shorthand (line D)." The same applies to class methods (Ch 21.2.7): static methods, instance methods, and computed keys all follow the same pattern.

# Prerequisites

- **Function .name property** — Method naming sets `.name`

# Key Properties

1. Method definition: `{ methodDef() {} }` -- name is `'methodDef'`
2. Property definition: `{ propDef: function () {} }` -- name is `'propDef'`
3. Computed key: `{ ['computed' + 'Key']: function () {} }` -- name is `'computedKey'`
4. Property shorthand: `{ shortHand }` -- name preserved from original function
5. Static methods: named the same way as instance methods

# Construction / Recognition

## To Construct/Create:
1. Define methods in object literals or class definitions

## To Identify/Recognize:
1. Check `obj.method.name` or `Class.prototype.method.name`

# Context & Application

Method naming ensures stack traces show meaningful method names. All four ways of defining methods on objects produce correctly named functions.

# Examples

**Example 1** (Ch 21):
```js
const obj = {
  methodDef() {},           // (A)
  propDef: function () {},  // (B)
  ['computed' + 'Key']: function () {}, // (C)
};
assert.equal(obj.methodDef.name, 'methodDef');
assert.equal(obj.propDef.name, 'propDef');
assert.equal(obj.computedKey.name, 'computedKey');
```

**Example 2** (Ch 21): Class methods:
```js
class ClassDecl {
  methodDef() {}
  static staticMethod() {}
}
assert.equal(ClassDecl.prototype.methodDef.name, 'methodDef');
assert.equal(ClassDecl.staticMethod.name, 'staticMethod');
```

# Relationships

## Builds Upon
- **Function .name property** — Methods have named `.name` properties

## Related
- **Getter/setter naming** — Getters and setters have prefixed names
- **Symbol-keyed method names** — Symbol keys produce special name formats

# Common Confusions

- **Confusion**: Only method shorthand (`{ method() {} }`) sets `.name`
  **Clarification**: Traditional property definitions and computed keys also set `.name`

# Source Reference

Chapter 21: The property .name of functions (bonus), Sections 21.2.6-21.2.7, lines 11437+.

# Verification Notes

- Definition source: direct from source with assertions
- Confidence rationale: All four patterns demonstrated
- Cross-reference status: verified
