---
# === CORE IDENTIFICATION ===
concept: Declarative Environment Record
slug: declarative-environment-record

# === CLASSIFICATION ===
category: language-mechanics
subcategory: environments
tier: intermediate

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "A detailed look at global variables"
chapter_number: 5
section: "5.5.2 Creating variables: declarative record vs. object record"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - declarative record

# === TYPED RELATIONSHIPS ===
prerequisites:
  - environment-record
  - global-environment
extends:
  - environment-record
related:
  - object-environment-record
  - script-scope
contrasts_with:
  - object-environment-record

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the global scope differ from module scope?"
---

# Quick Definition

A declarative environment record stores variable bindings in internal (engine-managed) storage, used for `const`, `let`, and `class` declarations at the global scope level.

# Core Definition

As described in "Deep JavaScript" (Ch 5, Section 5.5): "A normal (*declarative*) environment record that has its own storage for its bindings." In the global environment, "Top-level `const`, `let`, and `class` create bindings in the declarative environment record." These bindings are not accessible as properties of the global object, which protects modern declarations from interfering with built-in globals.

# Prerequisites

- **Environment record** — A declarative record is a type of environment record.
- **Global environment** — The global environment contains a declarative record.

# Key Properties

1. Uses **internal storage** for bindings (not backed by a JavaScript object).
2. Stores bindings for `const`, `let`, and `class` at the global level.
3. Bindings are **not** properties of the global object.
4. When both records have a binding, the **declarative record wins**.
5. Most non-global environments use declarative records exclusively.
6. Protects modern declarations from built-in global variable conflicts.

# Construction / Recognition

## To Construct/Create:
1. Declare variables with `const`, `let`, or `class` at the top level of a script.

## To Identify/Recognize:
1. Variables that are globally accessible but not properties of `globalThis`.

# Context & Application

The declarative environment record is why `let` and `const` at the top level of a script are globally visible to other scripts but do not appear on the global object. This is a deliberate design choice to avoid the problems of the global object (name collisions with built-in properties).

# Examples

**Example 1** (Ch 5): Declarative vs. object record:
```html
<script>
  const one = 1;  // declarative record
  var two = 2;    // object record (global object)
</script>
<script>
  console.log(one); // 1 (accessible)
  console.log(globalThis.one); // undefined (not on global object)
  console.log(globalThis.two); // 2 (on global object)
</script>
```

**Example 2** (Ch 5): Declarative record wins in conflict:
```html
<script>
  let myGlobalVariable = 1; // declarative record
  globalThis.myGlobalVariable = 2; // object record
  console.log(myGlobalVariable); // 1 (declarative wins)
</script>
```

# Relationships

## Builds Upon
- **Environment record** — Declarative record is a subtype.
- **Global environment** — Contains a declarative record.

## Enables
- **Safe global declarations** — `let`/`const`/`class` don't pollute the global object.

## Related
- **Script scope** — The declarative record is part of the script (global) scope.

## Contrasts With
- **Object environment record** — Backed by the global object; stores `var`/function declarations.

# Common Errors

- **Error**: Assuming `let` at top level creates a global object property.
  **Correction**: `let`/`const`/`class` at top level create bindings in the declarative record, not on the global object.

# Common Confusions

- **Confusion**: Declarative record variables are not truly global.
  **Clarification**: They are global (accessible from all scripts) but not properties of the global object. Global accessibility and global object membership are different things.

# Source Reference

Chapter 5: A detailed look at global variables, Section 5.5.2, lines 214-240.

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicit definition with examples
- Cross-reference status: verified
