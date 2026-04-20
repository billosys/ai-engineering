---
# === CORE IDENTIFICATION ===
concept: Script Scope
slug: script-scope

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
section: "5.5.1 Script scope and module scopes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - global scope

# === TYPED RELATIONSHIPS ===
prerequisites:
  - global-environment
  - lexical-scope
extends: []
related:
  - module-scope
  - declarative-environment-record
  - object-environment-record
contrasts_with:
  - module-scope

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the global scope differ from module scope?"
---

# Quick Definition

Script scope (global scope) is the outermost scope in JavaScript, shared by all scripts, and is the only scope where truly global variables can be created.

# Core Definition

As described in "Deep JavaScript" (Ch 5, Section 5.5.1): "In JavaScript, we are only in global scope at the top levels of scripts." The global scope is shared across all `<script>` tags. Module scopes are subscopes of the script scope. The structure can be visualized as nested blocks where the outermost block is the global scope containing all module scopes.

# Prerequisites

- **Global environment** — Script scope corresponds to the global environment.
- **Lexical scope** — Script scope is a type of scope.

# Key Properties

1. The **outermost** scope — contains all other scopes.
2. **Shared** across all `<script>` tags.
3. The only scope where truly global variables can be created.
4. Module scopes are **subscopes** of script scope.
5. Variables declared here are accessible everywhere (subject to shadowing).
6. Contains both declarative and object environment records.

# Construction / Recognition

## To Construct/Create:
1. Code at the top level of a `<script>` tag is in script scope.
2. Not inside any function, block, or module.

## To Identify/Recognize:
1. The top level of a `<script>` tag (not a `<script type="module">`).

# Context & Application

In modern JavaScript, most code lives in modules, which have their own scope. Script scope is primarily relevant for legacy code, library globals, and understanding how `var` declarations at the top level become global variables.

# Examples

**Example 1** (Ch 5): Script scope as container for module scopes:
```js
{ // Global scope (scope of *all* scripts)

  // (Global variables)

  { // Scope of module 1
    ···
  }
  { // Scope of module 2
    ···
  }
  // (More module scopes)
}
```

**Example 2** (Ch 5): Scripts share the same top-level scope:
```html
<script>
  const one = 1;
  var two = 2;
</script>
<script>
  // All scripts share the same top-level scope:
  console.log(one); // 1
  console.log(two); // 2
</script>
```

# Relationships

## Builds Upon
- **Global environment** — Script scope is implemented by the global environment.
- **Lexical scope** — Script scope is a type of scope.

## Enables
- **Cross-script variable sharing** — Variables declared in one script are visible in others.

## Related
- **Declarative environment record** — Stores `let`/`const`/`class` in script scope.
- **Object environment record** — Stores `var`/function declarations in script scope.

## Contrasts With
- **Module scope** — Module scope is a subscope of script scope; module code is not in global scope.

# Common Errors

- **Error**: Assuming module top-level code is in global scope.
  **Correction**: Modules have their own scope. Only script top-level code is in global scope.

# Common Confusions

- **Confusion**: Each `<script>` tag has its own scope.
  **Clarification**: All `<script>` tags share the same global (script) scope. A `const` declared in one script is visible in subsequent scripts.

# Source Reference

Chapter 5: A detailed look at global variables, Section 5.5.1, lines 187-212.

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicit definition with code visualization
- Cross-reference status: verified
