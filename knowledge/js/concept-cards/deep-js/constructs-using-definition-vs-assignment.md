---
# === CORE IDENTIFICATION ===
concept: Constructs Using Definition vs. Assignment
slug: constructs-using-definition-vs-assignment

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
section: "12.4 Which language constructs use definition, which assignment?"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - property-assignment
  - property-definition
  - assignment-calls-setters
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does property assignment differ from property definition?"
---

# Quick Definition

Object literal properties and public class fields use definition (they do not invoke inherited setters). The assignment operator `=` always uses assignment (it invokes inherited setters). This distinction is important when prototypes have setters.

# Core Definition

As described in "Deep JavaScript" Ch 12:
- "The properties of an object literal are added via definition" — therefore they never invoke inherited setters
- "The assignment operator `=` always uses assignment" — including normal assignment and destructuring
- "Public class fields are added via definition" — "even though public class fields have the same syntax as assignment, they do *not* use assignment to create properties, they use definition"

# Prerequisites

- **Property Assignment** — need to understand what assignment means
- **Property Definition** — need to understand what definition means
- **Assignment Calls Setters** — the key behavioral difference

# Key Properties

1. Object literal properties: definition
2. `=` operator (including destructuring): assignment
3. Public class fields: definition (despite looking like assignment)
4. Constructor body `this.prop = value`: assignment
5. `Object.defineProperty()`: definition
6. `Object.assign()`: uses get (from source) + set (assignment to target)

# Construction / Recognition

## To Construct/Create:
1. Not applicable — this is a classification of existing constructs

## To Identify/Recognize:
1. Check whether inherited setters are invoked — if not, definition is used
2. Object literals and class fields: definition
3. `=` operator: assignment

# Context & Application

This classification is important when working with prototype chains that contain accessor properties. A common surprise is that public class fields do NOT trigger inherited setters, despite their syntax resembling assignment.

# Examples

**Example 1** (Ch 12): Class fields use definition, constructor uses assignment:
```js
class A {
  set prop1(x) { lastSetterArgument1 = x; }
  set prop2(x) { lastSetterArgument2 = x; }
}
class B extends A {
  prop1 = 'one';          // definition — setter NOT called
  constructor() {
    super();
    this.prop2 = 'two';   // assignment — setter IS called
  }
}
new B();
assert.equal(lastSetterArgument1, undefined); // definition
assert.equal(lastSetterArgument2, 'two');     // assignment
```

# Relationships

## Builds Upon
- **property-assignment** — one of the two operations
- **property-definition** — the other operation
- **assignment-calls-setters** — the distinguishing behavior

## Enables
- Correctly predicting property behavior in class hierarchies

## Related
- None

## Contrasts With
- None

# Common Errors

- **Error**: Assuming public class fields trigger inherited setters.
  **Correction**: Class fields use definition, not assignment. They ignore inherited setters.

# Common Confusions

- **Confusion**: Thinking object literal properties use assignment because they look like `key: value` pairs.
  **Clarification**: Object literal properties use definition. They do not invoke inherited setters.

# Source Reference

Chapter 12: Properties: assignment vs. definition, Section 12.4, lines 563-652.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly demonstrated with setter-detection pattern.
- Cross-reference status: verified
