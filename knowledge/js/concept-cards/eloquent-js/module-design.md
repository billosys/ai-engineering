---
# === CORE IDENTIFICATION ===
concept: Module Design
slug: module-design

# === CLASSIFICATION ===
category: modularity
subcategory: design-principles
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Modules"
chapter_number: 10
pdf_page: null
section: "Module design"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - module architecture

# === TYPED RELATIONSHIPS ===
prerequisites:
  - module
  - es-module
  - interface
extends: []
related:
  - package
  - dependency
  - encapsulation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How should I design modules?"
  - "What makes a good module interface?"
---

# Quick Definition
Module design principles include making interfaces simple and predictable, following existing conventions, focusing modules on single tasks, preferring functions over stateful objects, and using simple data structures.

# Core Definition
Haverbeke discusses multiple design principles: "if your interface is simple and predictable" it helps usability. Modules should follow "existing conventions" (like the `ini` package imitating JSON's `parse`/`stringify`). Focused modules that "compute values are applicable in a wider range of programs than bigger modules that perform complicated actions with side effects." He advises: "if something can be done with a function, use a function." (Ch 10, "Module design")

# Prerequisites
- **Modules**: Understanding module structure
- **ES modules**: Practical module system knowledge
- **Interfaces**: Understanding what makes a good interface

# Key Properties
1. Simple, predictable interfaces
2. Follow existing conventions
3. Single, focused responsibility
4. Prefer pure computation over side effects
5. Prefer functions over stateful objects
6. Use simple data structures when possible
7. Design for composability

# Construction / Recognition
Good module design is recognized by small interfaces, clear naming, focused purpose, and compatibility with common data structures.

# Context & Application
The chapter warns against the OOP tendency to create stateful objects where functions would suffice: "Instead of making a single function call and moving on, you have to perform the ritual of moving your object through its various states." (Ch 10)

# Examples
The `ini` package is cited as good design: "This module imitates the standard `JSON` object by providing `parse` and `stringify` functions, and, like `JSON`, converts between strings and plain objects. The interface is small and familiar." (Ch 10, "Module design", lines 551-556)

# Relationships
## Builds Upon
- module, es-module, interface
## Enables
- Better software architecture
## Related
- package, dependency, encapsulation
## Contrasts With
- N/A

# Common Errors
- **Error**: Creating modules that require multi-step setup via stateful objects
  **Correction**: Prefer modules that export simple functions operating on plain data structures

# Common Confusions
- **Confusion**: Good module design means getting it right from the start
  **Clarification**: "In the phase where you are still exploring the problem... you might want to not worry about it too much. Once you have something that feels solid, that's a good time to take a step back and organize it." (Ch 10)

# Source Reference
Chapter 10: Modules, Section "Module design", lines 527-655.

# Verification Notes
- Definition source: synthesized from design guidelines
- Confidence rationale: Extensive design discussion with practical examples
- Cross-reference status: verified
