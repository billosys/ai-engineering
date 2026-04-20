---
# === CORE IDENTIFICATION ===
concept: Garbage Collection
slug: garbage-collection

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: language-overview
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Types, Values, and Variables"
chapter_number: 3
pdf_page: 41
section: "3.1 Overview and Definitions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - automatic memory management
  - GC

# === TYPED RELATIONSHIPS ===
prerequisites:
  - primitive-vs-object-types
extends: []
related:
  - primitive-immutability-vs-object-mutability
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures?"
---

# Quick Definition

JavaScript performs automatic garbage collection, meaning the interpreter automatically reclaims memory occupied by values that are no longer reachable by the program.

# Core Definition

"The JavaScript interpreter performs automatic garbage collection for memory management. This means that a JavaScript programmer generally does not need to worry about destruction or deallocation of objects or other values. When a value is no longer reachable—when a program no longer has any way to refer to it—the interpreter knows it can never be used again and automatically reclaims the memory it was occupying." (p. 41)

# Prerequisites

- **primitive-vs-object-types** — Must understand that objects occupy memory

# Key Properties

1. Automatic — the interpreter handles memory management
2. Based on reachability — unreachable values are reclaimed
3. Programmers generally don't need to worry about deallocation
4. Caveat: programmers "do sometimes need to take care to ensure that values do not inadvertently remain reachable" longer than necessary (p. 41)

# Construction / Recognition

Garbage collection is invisible to the programmer. Values become garbage-collectable when no variable, property, or closure references them.

# Context & Application

Understanding garbage collection is important for avoiding memory leaks, especially with closures (which can inadvertently keep references to large objects alive), event listeners, and circular references.

# Examples

From the source text (p. 41): No code example given. The concept is described in prose.

Implicit example: when a function returns and its local variables go out of scope, the values they referenced become eligible for garbage collection (unless captured by a closure).

# Relationships

## Builds Upon
- **primitive-vs-object-types** — Objects are the primary targets of garbage collection

## Enables
- Understanding memory leaks (especially with closures)

## Related
- **primitive-immutability-vs-object-mutability** — Mutable objects may be shared via references

## Contrasts With
- Manual memory management in C/C++

# Common Errors

- **Error**: Assuming garbage collection prevents all memory leaks.
  **Correction**: Values that remain reachable (through closures, global variables, or event listeners) will not be collected even if no longer needed.

# Common Confusions

- **Confusion**: Setting a variable to `null` immediately frees the memory.
  **Clarification**: Setting to `null` removes the reference, making the value *eligible* for collection, but the actual collection happens at the interpreter's discretion.

# Source Reference

Chapter 3: Types, Values, and Variables, Section 3.1, page 41.

# Verification Notes

- Definition source: Direct quote from p. 41
- Confidence rationale: High — clearly stated
- Uncertainties: None
- Cross-reference status: Verified
