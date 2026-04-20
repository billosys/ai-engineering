---
# === CORE IDENTIFICATION ===
concept: Private Property
slug: private-property

# === CLASSIFICATION ===
category: object-oriented-programming
subcategory: encapsulation
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "The Secret Life of Objects"
chapter_number: 6
pdf_page: null
section: "Private Properties"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - private field
  - private method
  - hash-prefixed property

# === TYPED RELATIONSHIPS ===
prerequisites:
  - class-declaration
  - encapsulation
extends: []
related:
  - interface
  - getter
  - setter
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I hide internal state from external code?"
  - "How does JavaScript enforce encapsulation?"
---

# Quick Definition
Private properties are class members prefixed with `#` that can only be accessed from inside the class declaration that defines them, enforcing encapsulation.

# Core Definition
Haverbeke explains: "To declare a private method, put a `#` sign in front of its name. Such methods can be called only from inside the `class` declaration that defines them." He adds: "To use private instance properties, you must declare them. Regular properties can be created by just assigning to them, but private properties *must* be declared in the class declaration to be available at all." (Ch 6, "Private Properties")

# Prerequisites
- **Class declarations**: Private properties only work within class declarations
- **Encapsulation**: Private properties are the mechanism for enforcing encapsulation

# Key Properties
1. Prefixed with `#` symbol
2. Only accessible inside the defining class
3. Must be declared in the class body (cannot be created dynamically)
4. Trying to access from outside the class produces an error
5. Applies to both properties and methods

# Construction / Recognition
```javascript
class SecretiveObject {
  #getSecret() {
    return "I ate all the plums";
  }
  interrogate() {
    let shallISayIt = this.#getSecret();
    return "never";
  }
}
```

# Context & Application
Private properties provide true encapsulation in JavaScript, preventing external code from depending on internal implementation details.

# Examples
```javascript
class RandomSource {
  #max;
  constructor(max) {
    this.#max = max;
  }
  getNumber() {
    return Math.floor(Math.random() * this.#max);
  }
}
```
Only `getNumber()` is the public interface; `#max` is hidden. (Ch 6, "Private Properties", lines 441-451)

# Relationships
## Builds Upon
- class-declaration, encapsulation
## Enables
- Better encapsulation, safer interfaces
## Related
- interface, getter, setter
## Contrasts With
- N/A

# Common Errors
- **Error**: Trying to access a `#` property from outside the class
  **Correction**: Private properties are only accessible within the class body; expose needed behavior through public methods

# Common Confusions
- **Confusion**: Private properties can be created by assigning to them like regular properties
  **Clarification**: Private properties must be explicitly declared in the class body before they can be used

# Source Reference
Chapter 6: The Secret Life of Objects, Section "Private Properties", lines 396-451.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly defined with examples
- Cross-reference status: verified
