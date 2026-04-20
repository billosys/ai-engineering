---
# === CORE IDENTIFICATION ===
concept: Abstract Data Type
slug: abstract-data-type

# === CLASSIFICATION ===
category: object-oriented-programming
subcategory: encapsulation
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "The Secret Life of Objects"
chapter_number: 6
pdf_page: null
section: "Abstract Data Types"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - ADT
  - object class

# === TYPED RELATIONSHIPS ===
prerequisites:
  - object
  - function
extends: []
related:
  - encapsulation
  - interface
  - class-declaration
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an abstract data type?"
  - "How do abstract data types organize programs?"
---

# Quick Definition
An abstract data type (or object class) is a subprogram that may contain arbitrarily complicated code but exposes a limited set of methods and properties for external use.

# Core Definition
As Haverbeke explains: "an *abstract data type*, or *object class*, is a subprogram that may contain arbitrarily complicated code but exposes a limited set of methods and properties that people working with it are supposed to use. This allows large programs to be built up out of a number of appliance types, limiting the degree to which these different parts are entangled by requiring them to only interact with each other in specific ways." (Ch 6, "Abstract Data Types")

# Prerequisites
- **Objects**: ADTs are built on JavaScript objects as their foundation
- **Functions**: Methods within ADTs are functions that define the type's behavior

# Key Properties
1. Exposes a limited public interface of methods and properties
2. Hides internal complexity behind that interface
3. Can be repaired or rewritten without impacting the rest of the program
4. Can be reused across multiple programs

# Construction / Recognition
An ADT is recognized by its separation of interface from implementation. In JavaScript, ADTs are implemented using classes or constructor functions that define a clear set of public methods while keeping internal details private.

# Context & Application
ADTs are the central organizing principle of object-oriented programming. They allow large programs to be built from independent, loosely-coupled components. JavaScript's built-in data structures like arrays and strings are examples of reusable ADTs.

# Examples
The text uses the analogy of an electric mixer: "The people who design and assemble a mixer have to do specialized work requiring material science and understanding of electricity. They cover all that up in a smooth plastic shell so that the people who only want to mix pancake batter don't have to worry about all that---they have to understand only the few knobs that the mixer can be operated with." (Ch 6, lines 50-58)

# Relationships
## Builds Upon
- object, function
## Enables
- encapsulation, interface, class-declaration, polymorphism
## Related
- modularity concepts in Chapter 10
## Contrasts With
- Unstructured programming without type separation

# Common Errors
- **Error**: Creating an ADT for every real-world concept encountered
  **Correction**: Not every concept needs its own class; focus on useful abstractions that reduce program complexity

# Common Confusions
- **Confusion**: ADTs require single-object focus
  **Clarification**: "The fixation on single *objects* as the main unit of organization in classical object-oriented programming is somewhat unfortunate since useful pieces of functionality often involve a group of different object classes working closely together." (Ch 6)

# Source Reference
Chapter 6: The Secret Life of Objects, Section "Abstract Data Types", lines 40-92 of source file.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly defined in the source text with detailed explanation
- Cross-reference status: verified against chapter summary
