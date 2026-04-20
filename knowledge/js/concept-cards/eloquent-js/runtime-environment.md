---
# === CORE IDENTIFICATION ===
concept: Runtime Environment
slug: runtime-environment

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
section: "The environment"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - environment
  - top scope
  - global scope

# === TYPED RELATIONSHIPS ===
prerequisites:
  - scope-in-interpreter
  - expression-evaluation
extends: []
related:
  - interpreter
  - special-form
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a runtime environment?"
---

# Quick Definition
The runtime environment is the collection of built-in values, functions, and operators available to a program at execution time.

# Core Definition
The environment is built by populating a top-level scope object with the language's primitive values and operations. In Egg, this includes Boolean values, arithmetic operators, comparison operators, and output functions. "This is really all that's needed to interpret Egg. It's that simple. But without defining a few special forms and adding some useful values to the environment, you can't do much with this language yet." (Eloquent JavaScript, Ch. 12, lines 352-355)

# Prerequisites
- **Scope**: Understanding how the scope object provides name resolution
- **Expression evaluation**: The evaluator uses the environment during execution

# Key Properties
1. Provides built-in values (true, false)
2. Provides primitive operations (+, -, *, /, ==, <, >)
3. Provides I/O functions (print)
4. Programs run in a fresh scope that inherits from the top scope
5. The environment can be extended with new bindings

# Construction / Recognition
```javascript
const topScope = Object.create(null);
topScope.true = true;
topScope.false = false;

for (let op of ["+", "-", "*", "/", "==", "<", ">"]) {
  topScope[op] = Function("a, b", `return a ${op} b;`);
}

topScope.print = value => {
  console.log(value);
  return value;
};
```
(lines 467-505)

# Context & Application
Every programming language needs a runtime environment that provides the basic building blocks programs are built from.

# Examples
From the source, running a program in the environment:
```javascript
function run(program) {
  return evaluate(parse(program), Object.create(topScope));
}

run(`
do(define(total, 0),
   define(count, 1),
   while(<(count, 11),
         do(define(total, +(total, count)),
            define(count, +(count, 1)))),
   print(total))
`);
// -> 55
```
(lines 515-535)

# Relationships
## Builds Upon
- Scope objects for name resolution
## Enables
- Program execution with built-in operations
## Related
- Interpreter (uses the environment to run programs)
## Contrasts With
- User-defined bindings (which are created by the program itself)

# Common Errors
- **Error**: Directly modifying the top scope during program execution
  **Correction**: Use `Object.create(topScope)` to create a fresh scope for each program run

# Common Confusions
- **Confusion**: The runtime environment is part of the language syntax
  **Clarification**: The environment is a library of values and functions available at runtime, separate from the language's syntax

# Source Reference
Chapter 12: Project: A Programming Language, Section "The environment", lines 451-535 of 12-project-a-programming-language.md.

# Verification Notes
- Definition source: synthesized from source code and explanation
- Confidence rationale: Complete implementation shown
- Cross-reference status: verified
