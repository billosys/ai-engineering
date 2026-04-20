---
# === CORE IDENTIFICATION ===
concept: Lexical Environment
slug: lexical-environment

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
  - lexical env

# === TYPED RELATIONSHIPS ===
prerequisites:
  - environment
  - lexical-scope
extends:
  - environment
related:
  - environment-record
  - outer-environment-reference
  - global-environment
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a lexical environment?"
  - "How do lexical environments relate to closures?"
---

# Quick Definition

A lexical environment is the ECMAScript specification's implementation of a scope, consisting of an environment record (variable storage) and a reference to the outer environment.

# Core Definition

As described in "Deep JavaScript" (Ch 5, Section 5.2): "In the JavaScript language specification, scopes are 'implemented' via *lexical environments*. They consist of two components: An *environment record* that maps variable names to variable values (think dictionary). This is the actual storage space for the variables of the scope. The name-value entries in the record are called *bindings*. A reference to the *outer environment* -- the environment for the outer scope."

# Prerequisites

- **Environment** — Lexical environment is the formal spec term for the concept introduced in Ch 4.
- **Lexical scope** — Lexical environments implement scopes.

# Key Properties

1. Two components: **environment record** and **outer environment reference**.
2. The environment record maps variable names to values; entries are called **bindings**.
3. The outer reference points to the environment of the enclosing scope.
4. Nested scopes form a **tree** of environments linked by outer references.
5. The formal ECMAScript specification term for the environment concept.

# Construction / Recognition

## To Construct/Create:
1. Every scope (function, block, global, module) has a corresponding lexical environment.

## To Identify/Recognize:
1. Any scope in JavaScript is backed by a lexical environment with a record and an outer reference.

# Context & Application

Lexical environments are the formal specification mechanism for all variable management in JavaScript. Understanding the two-component structure (record + outer reference) explains how variable lookup works, how closures retain access to variables, and how the global environment has special structure (two records instead of one).

# Examples

**Example 1** (Ch 5): The two components:
```
Lexical Environment = {
  environment record: { variableName: value, ... },
  outer: <reference to enclosing environment>
}
```
"The tree of nested scopes is therefore represented by a tree of environments linked by outer environment references."

# Relationships

## Builds Upon
- **Environment** — Lexical environment is the formal name for the concept.
- **Lexical scope** — Lexical environments implement scopes.

## Enables
- **Global environment** — A specialized lexical environment with two records.
- **Closure** — Lexical environments persist on the heap, enabling closures.

## Related
- **Environment record** — The variable storage component.
- **Outer environment reference** — The link to the enclosing environment.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Treating lexical environment and environment record as synonymous.
  **Correction**: A lexical environment contains an environment record *plus* an outer reference. The record is only one component.

# Common Confusions

- **Confusion**: "Environment" and "lexical environment" are different things.
  **Clarification**: In the ECMAScript spec, "lexical environment" is the formal term. The source uses "environment" informally in Ch 4 and introduces the full term in Ch 5. They refer to the same concept.

# Source Reference

Chapter 5: A detailed look at global variables, Section 5.2, lines 63-79.

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicit definition with components listed
- Cross-reference status: verified against ECMAScript specification link in source
