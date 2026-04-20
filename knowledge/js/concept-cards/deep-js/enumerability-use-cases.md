---
# === CORE IDENTIFICATION ===
concept: Enumerability Use Cases
slug: enumerability-use-cases

# === CLASSIFICATION ===
category: object-model
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Enumerability of properties"
chapter_number: 13
section: "13.3 Use cases for enumerability"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - enumerability
  - for-in-loop
extends: []
related:
  - object-assign-enumerability
  - json-stringify-enumerability
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is enumerability?"
---

# Quick Definition

Enumerability has three historical use cases: hiding inherited properties from `for-in`, marking properties as not-to-be-copied, and hiding properties from `JSON.stringify()`. However, each has caveats and better modern alternatives.

# Core Definition

As described in "Deep JavaScript" Ch 13, "Enumerability is an inconsistent feature. It does have use cases, but there is always some kind of caveat." The use cases are:

1. **Hiding from `for-in`**: The original motivation. Caveat: `for-in` itself is largely superseded by `Object.keys()` + `for-of`.
2. **Marking as not-to-be-copied**: Affects `Object.assign()`, spreading, and historical `extend()` functions. Caveat: usually better to ignore inherited properties outright rather than relying on enumerability.
3. **Hiding from `JSON.stringify()`**: Caveat: `.toJSON()` is a cleaner alternative.
4. **Marking as private**: "There are several problems with this approach" — not truly private, clashes with copying, and naming conventions are more discoverable.

The conclusion: "almost all applications for non-enumerability are work-arounds that now have other and better solutions."

# Prerequisites

- **Enumerability** — understanding the attribute
- **for-in Loop** — the original motivation

# Key Properties

1. Hiding from `for-in`: the original purpose (ECMAScript 1)
2. Marking not-to-be-copied: affects `Object.assign()`, spreading
3. Hiding from `JSON.stringify()`: better served by `.toJSON()`
4. Pseudo-privacy: not recommended (use private fields instead)
5. Modern code rarely needs to interact with enumerability directly

# Construction / Recognition

## To Construct/Create:
1. Not applicable — this describes use case analysis

## To Identify/Recognize:
1. When someone makes a property non-enumerable, check which use case motivates it

# Context & Application

The book argues that enumerability is mostly a legacy feature. In modern code, the defaults work well: own properties are enumerable, prototype methods are non-enumerable. Developers should "usually pretend that enumerability doesn't exist."

# Examples

**Example 1** (Ch 13): The downsides of enumerability-driven copying:
- "Which properties to copy often depends on the task at hand; it rarely makes sense to have a single flag for all use cases."
- "A better choice is to provide a copying operation with a *predicate* (a callback that returns a boolean) that tells it when to ignore properties."

# Relationships

## Builds Upon
- **enumerability** — analysis of the attribute's use cases
- **for-in-loop** — the original use case

## Enables
- Understanding why enumerability exists and when to care about it

## Related
- **object-assign-enumerability** — one of the affected operations
- **json-stringify-enumerability** — another affected operation

## Contrasts With
- None

# Common Errors

- **Error**: Using enumerability for pseudo-privacy.
  **Correction**: Use private class fields (`#prop`) for true privacy. Enumerability is not a security mechanism.

# Common Confusions

- **Confusion**: Thinking enumerability is essential to understand for daily coding.
  **Clarification**: The defaults handle most cases correctly. "For our own code, we can usually pretend that enumerability doesn't exist."

# Source Reference

Chapter 13: Enumerability of properties, Section 13.3, lines 365-703. Section 13.4, lines 705-718.

# Verification Notes

- Definition source: synthesized from multiple use case sections
- Confidence rationale: Directly from the source's analysis with direct quotes.
- Cross-reference status: verified
