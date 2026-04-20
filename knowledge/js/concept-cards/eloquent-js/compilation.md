---
# === CORE IDENTIFICATION ===
concept: Compilation
slug: compilation

# === CLASSIFICATION ===
category: language-implementation
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Project: A Programming Language"
chapter_number: 12
pdf_page: null
section: "Compilation"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - compiler

# === TYPED RELATIONSHIPS ===
prerequisites:
  - parsing
  - syntax-tree
extends: []
related:
  - interpreter
contrasts_with:
  - interpreter

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is compilation?"
---

# Quick Definition
Compilation is the process of transforming a program into a different, more efficient representation before execution, rather than interpreting it directly.

# Core Definition
"*Compilation* is the process of adding another step between the parsing and the running of a program, which transforms the program into something that can be evaluated more efficiently by doing as much work as possible in advance." "Traditionally, compilation involves converting the program to machine code, the raw format that a computer's processor can execute. But any process that converts a program to a different representation can be thought of as compilation." (Eloquent JavaScript, Ch. 12, lines 610-624)

# Prerequisites
- **Parsing**: Compilation works on parsed program representations
- **Syntax tree**: The input to the compilation step

# Key Properties
1. Adds a transformation step between parsing and execution
2. Aims for more efficient execution by doing work ahead of time
3. Can target machine code, bytecode, or another language
4. Can resolve variable bindings at compile time instead of runtime
5. Any program-to-program transformation counts as compilation

# Construction / Recognition
The source suggests compiling Egg to JavaScript: "It would be possible to write an alternative evaluation strategy for Egg, one that first converts the program to a JavaScript program, uses `Function` to invoke the JavaScript compiler on it, and runs the result." (lines 627-631)

# Context & Application
Compilation is used to produce faster-executing programs. Modern JavaScript engines use JIT (just-in-time) compilation to achieve this.

# Examples
From the source: "For example, in well-designed languages it is obvious, for each use of a binding, which binding is being referred to, without actually running the program. This can be used to avoid looking up the binding by name every time it is accessed, instead directly fetching it from some predetermined memory location." (lines 614-618)

# Relationships
## Builds Upon
- Parsing and syntax trees
## Enables
- Faster program execution
## Related
- Interpreter (both process parsed programs)
## Contrasts With
- Interpretation (which executes directly from the syntax tree)

# Common Errors
- **Error**: Assuming compilation always means producing machine code
  **Correction**: Any program transformation is compilation, including transpilation to another high-level language

# Common Confusions
- **Confusion**: Interpreted languages cannot use compilation
  **Clarification**: Many "interpreted" languages use JIT compilation internally

# Source Reference
Chapter 12: Project: A Programming Language, Section "Compilation", lines 602-637 of 12-project-a-programming-language.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Clearly defined with concrete examples
- Cross-reference status: verified
