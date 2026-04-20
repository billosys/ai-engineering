---
# === CORE IDENTIFICATION ===
concept: Interpreter
slug: interpreter

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
  - evaluator
  - tree-walking interpreter

# === TYPED RELATIONSHIPS ===
prerequisites:
  - parsing
  - syntax-tree
  - expression-evaluation
extends: []
related:
  - compilation
  - runtime-environment
contrasts_with:
  - compilation

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an interpreter?"
---

# Quick Definition
An interpreter is a program that directly executes a language by acting on the syntax tree representation produced by a parser, without first compiling it to another form.

# Core Definition
"What we have built is an interpreter. During evaluation, it acts directly on the representation of the program produced by the parser." (Eloquent JavaScript, Ch. 12, lines 605-607)

# Prerequisites
- **Parsing**: The interpreter needs a parser to produce syntax trees
- **Syntax tree**: The interpreter acts on tree-structured representations
- **Expression evaluation**: The core mechanism of interpretation

# Key Properties
1. Directly executes the parsed representation of a program
2. Combines parsing and evaluation to run programs
3. Typically simpler to implement than a compiler
4. May be slower than compiled code since it works on the tree representation
5. The evaluator's recursive structure mirrors the language's recursive structure

# Construction / Recognition
```javascript
function run(program) {
  return evaluate(parse(program), Object.create(topScope));
}
```
(lines 515-517)

# Context & Application
Interpreters are used for scripting languages, REPLs, configuration languages, and any context where simplicity and flexibility are more important than raw execution speed.

# Examples
From the source, running a program in the Egg language:
```javascript
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
(lines 526-535)

"Building your own programming language is surprisingly easy (as long as you do not aim too high) and very enlightening." (lines 32-33)

# Relationships
## Builds Upon
- Parser (to produce syntax trees) and evaluator (to execute them)
## Enables
- Running programs in the defined language
## Related
- Runtime environment (provides built-in values and functions)
## Contrasts With
- Compilation (which transforms the program before execution)

# Common Errors
- **Error**: Not providing useful error messages when the program fails
  **Correction**: Include line/column information and clear descriptions of what went wrong

# Common Confusions
- **Confusion**: Interpreters cannot be fast
  **Clarification**: Modern interpreters use techniques like JIT compilation to achieve near-compiled speeds

# Source Reference
Chapter 12: Project: A Programming Language, Section "Compilation", lines 602-607 of 12-project-a-programming-language.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Clearly defined in contrast to compilation
- Cross-reference status: verified
