---
# === CORE IDENTIFICATION ===
concept: Global Environment
slug: global-environment

# === CLASSIFICATION ===
category: language-mechanics
subcategory: scoping
tier: intermediate

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "A detailed look at global variables"
chapter_number: 5
section: "5.5 The global environment"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - global environment record

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lexical-environment
  - environment-record
  - global-object
extends:
  - lexical-environment
related:
  - declarative-environment-record
  - object-environment-record
  - script-scope
  - module-scope
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the global scope differ from module scope?"
---

# Quick Definition

The global environment is the outermost lexical environment in JavaScript, uniquely composed of two environment records (object and declarative) that together manage global variables.

# Core Definition

As described in "Deep JavaScript" (Ch 5, Section 5.5): "The global scope is the 'outermost' scope -- it has no outer scope. Its environment is the *global environment*. Every environment is connected with the global environment via a chain of environments that are linked by outer environment references. The outer environment reference of the global environment is `null`." The global environment record uses two sub-records: "An *object environment record* has the same interface as a normal environment record, but keeps its bindings in a JavaScript object. In this case, the object is the global object." And "A normal (*declarative*) environment record that has its own storage for its bindings."

# Prerequisites

- **Lexical environment** — The global environment is a specialized lexical environment.
- **Environment record** — The global environment has two records.
- **Global object** — Backs the object environment record.

# Key Properties

1. The **outermost** environment — its `outer` reference is `null`.
2. All environments eventually chain to it via `outer` references.
3. Contains **two** environment records: object and declarative.
4. Object record: backed by the global object (for `var`/function declarations).
5. Declarative record: internal storage (for `let`/`const`/`class`).
6. When both records have a binding, the **declarative record wins** during lookup.

# Construction / Recognition

## To Construct/Create:
1. Created automatically when the JavaScript runtime initializes.

## To Identify/Recognize:
1. The environment with `null` outer reference.
2. The environment that contains built-in globals.

# Context & Application

The dual-record structure of the global environment explains the split behavior of global variables: `var` and function declarations become properties of the global object, while `let`/`const`/`class` declarations have internal storage. This design allows modern declarations to avoid polluting the global object while maintaining backward compatibility.

# Examples

**Example 1** (Ch 5): Declarative record wins when both have a binding:
```html
<script>
  let myGlobalVariable = 1; // declarative environment record
  globalThis.myGlobalVariable = 2; // object environment record

  console.log(myGlobalVariable); // 1 (declarative record wins)
  console.log(globalThis.myGlobalVariable); // 2
</script>
```

# Relationships

## Builds Upon
- **Lexical environment** — The global environment is a specialized lexical environment.
- **Global object** — Provides the backing store for the object record.

## Enables
- **Script scope** — The global scope is the scope of all scripts.
- **Module scope** — Module environments have the global environment as their outer environment.

## Related
- **Declarative environment record** — One of the two records.
- **Object environment record** — The other record, backed by the global object.

## Contrasts With
- None directly (it is unique).

# Common Errors

- **Error**: Assuming `let` declarations are accessible via `globalThis`.
  **Correction**: `let`/`const`/`class` at script top level are in the declarative record, not the object record. They are not properties of the global object.

# Common Confusions

- **Confusion**: The global environment has one environment record like other environments.
  **Clarification**: The global environment uniquely has **two** records. This dual-record structure is what creates the difference between `var` and `let` at the global level.

# Source Reference

Chapter 5: A detailed look at global variables, Section 5.5, lines 166-308.

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Detailed explanation with diagrams
- Cross-reference status: verified against ECMAScript spec references in source
