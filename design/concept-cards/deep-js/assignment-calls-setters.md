---
# === CORE IDENTIFICATION ===
concept: Assignment Calls Setters
slug: assignment-calls-setters

# === CLASSIFICATION ===
category: object-model
subcategory: assignment
tier: intermediate

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Properties: assignment vs. definition"
chapter_number: 12
section: "12.3.3 Assignment calls setters, definition doesn't"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "setter invocation during assignment"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - property-assignment
  - property-definition
  - accessor-property
  - set-attribute
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does property assignment differ from property definition?"
---

# Quick Definition

When assigning to a property, JavaScript invokes any inherited setter for that property. When defining a property, inherited setters are ignored entirely. This is the key behavioral difference between assignment and definition.

# Core Definition

As described in "Deep JavaScript" Ch 12, "If we define, then our intention is to either create or change an own (non-inherited) property of `obj`. Therefore, definition ignores the inherited setter." Conversely, "If, instead, we assign to `.prop`, then our intention is often to change something that already exists and that change should be handled by the setter."

# Prerequisites

- **Property Assignment** — the operation that invokes setters
- **Property Definition** — the operation that ignores setters
- **Accessor Property** — setters are part of accessor properties
- **Set Attribute** — the setter function attribute

# Key Properties

1. Assignment invokes both own and inherited setters
2. Definition never invokes setters
3. This is the fundamental behavioral distinction between assignment and definition
4. Object literal properties use definition (do not invoke inherited setters)
5. The `=` operator always uses assignment (invokes setters)
6. Public class fields use definition (do not invoke inherited setters)

# Construction / Recognition

## To Construct/Create:
1. Assignment that triggers setter: `obj.prop = value` (when inherited setter exists)
2. Definition that bypasses setter: `Object.defineProperty(obj, 'prop', { value: v })`

## To Identify/Recognize:
1. If a setter is called, assignment was used
2. If a setter is not called when one exists in the prototype, definition was used

# Context & Application

This distinction is critical when working with prototype chains that contain accessor properties. If you want to override an inherited getter/setter with an own data property, you must use definition. If you want to trigger the setter's side effects, you must use assignment.

# Examples

**Example 1** (Ch 12): Definition ignores setter:
```js
let setterWasCalled = false;
const proto = {
  get prop() { return 'protoGetter'; },
  set prop(x) { setterWasCalled = true; },
};
const obj = Object.create(proto);
Object.defineProperty(obj, 'prop', { value: 'objData' });
assert.equal(setterWasCalled, false);
```

**Example 2** (Ch 12): Assignment invokes setter:
```js
let setterWasCalled = false;
const proto = {
  get prop() { return 'protoGetter'; },
  set prop(x) { setterWasCalled = true; },
};
const obj = Object.create(proto);
obj.prop = 'objData';
assert.equal(setterWasCalled, true);
assert.equal(obj.prop, 'protoGetter'); // getter still active
```

# Relationships

## Builds Upon
- **property-assignment** — assignment is the operation that calls setters
- **property-definition** — definition is the operation that ignores setters

## Enables
- Understanding how to correctly override inherited accessors

## Related
- None

## Contrasts With
- None

# Common Errors

- **Error**: Using assignment to create an own data property when an inherited setter exists.
  **Correction**: Assignment will trigger the setter instead of creating an own property. Use `Object.defineProperty()` to create an own property that overrides the accessor.

# Common Confusions

- **Confusion**: Expecting public class fields (which look like assignment) to trigger inherited setters.
  **Clarification**: Public class fields use definition, not assignment. They do not invoke inherited setters.

# Source Reference

Chapter 12: Properties: assignment vs. definition, Section 12.3.3, lines 426-484.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly demonstrated with parallel examples.
- Cross-reference status: verified
