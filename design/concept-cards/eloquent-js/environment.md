---
# === CORE IDENTIFICATION ===
concept: Environment
slug: environment

# === CLASSIFICATION ===
category: fundamentals
subcategory: program-structure
tier: foundational

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Program Structure"
chapter_number: 2
pdf_page: null
section: "The environment"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - binding
  - value
extends: []
related:
  - console-log
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a binding (variable)?"
  - "What must I know before understanding closures?"
---

# Quick Definition

The environment is the collection of bindings and their values that exist at a given time, including language-standard bindings and platform-specific bindings for interacting with the surrounding system.

# Core Definition

As defined in "Eloquent JavaScript" (Ch 2, lines 243-250 of 02-program-structure.md): "The collection of bindings and their values that exist at a given time is called the *environment*. When a program starts up, this environment is not empty. It always contains bindings that are part of the language standard, and most of the time, it also has bindings that provide ways to interact with the surrounding system."

# Prerequisites

- **Binding** -- The environment is a collection of bindings.
- **Value** -- Bindings in the environment hold values.

# Key Properties

1. The **collection of bindings and their values** at a given time (line 243-244).
2. **Not empty** when a program starts -- contains language-standard bindings (lines 245-246).
3. Includes **platform-specific bindings** for system interaction (lines 247-248).
4. In a browser, includes bindings for website interaction and input reading (lines 248-250).

# Construction / Recognition

## To Identify/Recognize:
1. The set of all available bindings at any point during program execution.
2. Includes both user-defined and built-in bindings.

# Context & Application

The environment concept is foundational for understanding scope, closures, and how JavaScript makes built-in functions available. Every execution context has an associated environment.

# Examples

**Example 1** (Ch 2, lines 243-250): "When a program starts up, this environment is not empty. It always contains bindings that are part of the language standard."

**Example 2** (Ch 2, summary lines 893-897): "Bindings can be used to file pieces of data under a name, and they are useful for tracking state in your program. The environment is the set of bindings that are defined. JavaScript systems always put a number of useful standard bindings into your environment."

# Relationships

## Builds Upon
- **Binding** -- Environments consist of bindings.
- **Value** -- Each binding in the environment holds a value.

## Enables
- **Closures** (later chapters) -- Closures capture their enclosing environment.
- Understanding scope.

## Related
- **Console.log** -- A binding available in the default environment.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Assuming the environment contains only user-defined bindings.
  **Correction**: The environment always includes language-standard bindings and platform-specific bindings.

# Common Confusions

- **Confusion**: The environment is static and fixed.
  **Clarification**: The environment changes as bindings are created, modified, or go out of scope during program execution.

# Source Reference

Chapter 2: Program Structure, Section "The environment", lines 240-250 of 02-program-structure.md (book.md line 1304).

# Verification Notes

- Definition source: direct (quoted from source)
- Confidence rationale: Explicit definition with italicized term in dedicated section
- Cross-reference status: verified with chapter summary
