---
# === CORE IDENTIFICATION ===
concept: Module
slug: module

# === CLASSIFICATION ===
category: modularity
subcategory: fundamentals
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Modules"
chapter_number: 10
pdf_page: null
section: "Modular programs"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function
  - object
  - interface
extends: []
related:
  - es-module
  - dependency
  - package
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a module?"
  - "What must I know before writing a module system?"
---

# Quick Definition
A module is a piece of program that specifies which other pieces it relies on (dependencies) and which functionality it provides for other modules to use (its interface).

# Core Definition
Haverbeke defines: "*Modules* are an attempt to avoid these problems. A module is a piece of program that specifies which other pieces it relies on and which functionality it provides for other modules to use (its *interface*)." (Ch 10, "Modular programs")

# Prerequisites
- **Functions**: Modules contain functions and other code
- **Objects**: Module interfaces are collections of bindings
- **Interfaces**: Module interfaces have much in common with object interfaces

# Key Properties
1. Specifies dependencies (what other modules it needs)
2. Specifies an interface (what it provides to others)
3. Keeps internal details private
4. Dependencies should be explicit and clear
5. "When the ways in which modules interact with each other are explicit, a system becomes more like LEGO" (Ch 10)

# Construction / Recognition
Modules are recognized by their explicit declarations of what they import and export.

# Context & Application
Modules solve the problem of program structure. Without them, "Everything sticks together, and when you try to pick out a piece, the whole thing comes apart" -- the "big ball of mud" anti-pattern. (Ch 10)

# Examples
```javascript
// A simple module with no dependencies
const names = ["Sunday", "Monday", "Tuesday", "Wednesday",
               "Thursday", "Friday", "Saturday"];

export function dayName(number) {
  return names[number];
}
export function dayNumber(name) {
  return names.indexOf(name);
}
```
The `names` constant is private (not exported); `dayName` and `dayNumber` are the interface. (Ch 10, "ES modules", lines 119-129)

# Relationships
## Builds Upon
- function, object, interface
## Enables
- es-module, package, dependency management
## Related
- encapsulation (module-level)
## Contrasts With
- N/A

# Common Errors
- **Error**: Creating modules without clear interfaces
  **Correction**: Design modules with small, focused interfaces that hide implementation details

# Common Confusions
- **Confusion**: Modules and files are the same thing
  **Clarification**: While ES modules map to files, the concept of a module is about clear interfaces and dependencies, not just file separation

# Source Reference
Chapter 10: Modules, Section "Modular programs", lines 58-87.

# Verification Notes
- Definition source: direct
- Confidence rationale: Core concept of the chapter, explicitly defined
- Cross-reference status: verified against chapter summary
