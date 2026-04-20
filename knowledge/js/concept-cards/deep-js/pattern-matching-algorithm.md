---
# === CORE IDENTIFICATION ===
concept: Pattern Matching Algorithm
slug: pattern-matching-algorithm

# === CLASSIFICATION ===
category: language-mechanics
subcategory: destructuring
tier: intermediate

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "The destructuring algorithm"
chapter_number: 3
section: "3.2 The pattern matching algorithm"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - destructuring algorithm
  - matching algorithm

# === TYPED RELATIONSHIPS ===
prerequisites:
  - destructuring-assignment
extends: []
related:
  - object-pattern
  - array-pattern
  - default-values-in-destructuring
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is destructuring in JavaScript?"
---

# Quick Definition

The pattern matching algorithm is the formal recursive algorithm that specifies how JavaScript destructuring works, using declarative rules that process variable, object, and array patterns.

# Core Definition

As described in "Deep JavaScript" (Ch 3, Section 3.1-3.2): The destructuring algorithm is "known in functional programming as *pattern matching* (short: *matching*)." It uses the operator `←` ("match against") and "specifies the operator `←` that matches a `pattern` against a `value` and assigns to variables while doing so." The algorithm consists of declarative rules applied from top to bottom. Each rule has a head (pattern to match) and a body (actions to take). A pattern is either a variable (`x`), an object pattern (`{«properties»}`), or an Array pattern (`[«elements»]`).

# Prerequisites

- **Destructuring assignment** — The algorithm formalizes destructuring behavior.

# Key Properties

1. Specified via **declarative rules** applied top-to-bottom.
2. Each rule has a **head** (input pattern) and a **body** (side effects/actions).
3. Three types of patterns: variable, object pattern, array pattern.
4. Rules are recursive — patterns within patterns trigger nested matching.
5. Rules handle: normal matching, default values, rest elements, errors, and termination.

# Construction / Recognition

## To Construct/Create:
1. Identify the pattern type (variable, object, array).
2. Apply the appropriate rule from the algorithm.
3. Recurse into nested patterns as specified by the rule bodies.

## To Identify/Recognize:
1. Any destructuring expression follows this algorithm.
2. The algorithm explains the order of operations and error handling.

# Context & Application

Understanding the algorithm helps resolve ambiguous cases, particularly with default values. The chapter uses it to explain why `function move1({x=0, y=0} = {})` and `function move2({x, y} = {x: 0, y: 0})` behave differently.

# Examples

**Example 1** (Ch 3): Rule structure:
```
- (2c) {key: «pattern», «properties»} ← obj

  «pattern» ← obj.key
  {«properties»} ← obj
```
The head describes what input triggers the rule. The body describes what happens.

**Example 2** (Ch 3): Evaluating a match expression:
```
{first: f, last: l} ← obj
```
Rules are applied top-to-bottom: rule 2c matches, extracting `f ← obj.first`, then recursing with `{last: l} ← obj`, then rule 2c again for `l ← obj.last`, then rule 2e terminates.

# Relationships

## Builds Upon
- **Destructuring assignment** — The algorithm formalizes destructuring.

## Enables
- **Object pattern** — Rules 2a-2e handle object patterns.
- **Array pattern** — Rules 3a-3g handle array patterns.
- **Default values in destructuring** — Rules 2d and 3d handle defaults.

## Related
- **Variable pattern** — Rule 1 handles simple variable assignment.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Applying rules in the wrong order.
  **Correction**: Rules are always applied top-to-bottom; the first matching rule is used.

# Common Confusions

- **Confusion**: The algorithm is just "extracting properties."
  **Clarification**: It is a recursive process that handles nested patterns, defaults, rest elements, iterators, and error cases, not simple property access.

# Source Reference

Chapter 3: The destructuring algorithm, Sections 3.1-3.2, lines 1557-1680.

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Formal algorithm fully specified in source
- Cross-reference status: verified
