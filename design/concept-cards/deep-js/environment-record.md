---
# === CORE IDENTIFICATION ===
concept: Environment Record
slug: environment-record

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
section: "5.2 Lexical environments"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - binding record

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lexical-environment
extends: []
related:
  - declarative-environment-record
  - object-environment-record
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a lexical environment?"
---

# Quick Definition

An environment record is the component of a lexical environment that maps variable names to their values, serving as the actual storage space for a scope's variables.

# Core Definition

As described in "Deep JavaScript" (Ch 5, Section 5.2): An environment record "maps variable names to variable values (think dictionary). This is the actual storage space for the variables of the scope. The name-value entries in the record are called *bindings*." There are two types relevant to global scope: declarative environment records (with internal storage) and object environment records (backed by a JavaScript object).

# Prerequisites

- **Lexical environment** — An environment record is one of the two components of a lexical environment.

# Key Properties

1. Maps variable names to values (a dictionary/map structure).
2. Entries are called **bindings**.
3. The "actual storage space" for a scope's variables.
4. Comes in subtypes: **declarative** (internal storage) and **object** (backed by a JS object).
5. The global environment record uniquely uses **both** types.

# Construction / Recognition

## To Construct/Create:
1. Every lexical environment contains an environment record.
2. The type of record depends on the context (function, block, global, etc.).

## To Identify/Recognize:
1. The component that holds name-value pairs in a lexical environment.

# Context & Application

Understanding environment records is key to understanding how the global environment works. The global environment uses two records: a declarative record for `let`/`const`/`class` declarations, and an object record (backed by the global object) for `var` and function declarations.

# Examples

**Example 1** (Ch 5): Environment record as a dictionary:
```
Environment Record:
  variableName1 → value1
  variableName2 → value2
  // Each entry is a "binding"
```

# Relationships

## Builds Upon
- **Lexical environment** — The environment record is one of its two components.

## Enables
- **Declarative environment record** — A subtype with internal storage.
- **Object environment record** — A subtype backed by a JavaScript object.

## Related
- **Global environment** — Uses both record types.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Assuming all environment records work the same way.
  **Correction**: The global environment has two kinds of records with different behaviors. Only the object record's bindings are accessible as global object properties.

# Common Confusions

- **Confusion**: Bindings and variables are different things.
  **Clarification**: A binding is the name-value entry in an environment record that represents a variable. The terms are closely related but "binding" refers specifically to the record entry.

# Source Reference

Chapter 5: A detailed look at global variables, Section 5.2, lines 69-72.

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicit definition provided
- Cross-reference status: verified
