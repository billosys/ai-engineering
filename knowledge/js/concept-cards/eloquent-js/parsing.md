---
# === CORE IDENTIFICATION ===
concept: Parsing
slug: parsing

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
section: "Parsing"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - parser
  - syntactic analysis

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function
extends: []
related:
  - syntax-tree
  - tokenization
  - expression-evaluation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is parsing in the context of programming languages?"
---

# Quick Definition
Parsing is the process of reading text and producing a data structure that reflects the structure of the program contained in that text.

# Core Definition
"The most immediately visible part of a programming language is its *syntax*, or notation. A *parser* is a program that reads a piece of text and produces a data structure that reflects the structure of the program contained in that text. If the text does not form a valid program, the parser should point out the error." (Eloquent JavaScript, Ch. 12, lines 53-58)

# Prerequisites
- **Functions**: Parsers are typically implemented as recursive functions
- Understanding of regular expressions helps with tokenization

# Key Properties
1. Transforms text input into a structured data representation
2. Validates that the input conforms to the language syntax
3. Reports errors for invalid input
4. For recursive languages, parsers are themselves recursive
5. The output is typically a syntax tree

# Construction / Recognition
```javascript
function parseExpression(program) {
  program = skipSpace(program);
  let match, expr;
  if (match = /^"([^"]*)"/.exec(program)) {
    expr = {type: "value", value: match[1]};
  } else if (match = /^\d+\b/.exec(program)) {
    expr = {type: "value", value: Number(match[0])};
  } else if (match = /^[^\s(),#"]+/.exec(program)) {
    expr = {type: "word", name: match[0]};
  } else {
    throw new SyntaxError("Unexpected syntax: " + program);
  }
  return parseApply(expr, program.slice(match[0].length));
}
```
(lines 170-184)

# Context & Application
Parsing is the first phase of language processing, used in compilers, interpreters, configuration file readers, and any tool that processes structured text.

# Examples
From the source:
```javascript
console.log(parse("+(a, 10)"));
// -> {type: "apply",
//    operator: {type: "word", name: "+"},
//    args: [{type: "word", name: "a"},
//           {type: "value", value: 10}]}
```
(lines 270-275)

# Relationships
## Builds Upon
- Regular expressions for pattern matching
- Recursive functions
## Enables
- Syntax tree construction
- Program evaluation/interpretation
## Related
- Tokenization (breaking input into tokens)
- Syntax trees (the output of parsing)
## Contrasts With
- Evaluation (which acts on the parsed structure)

# Common Errors
- **Error**: Not handling all valid input forms in the parser
  **Correction**: Ensure the parser covers all syntax cases and provides clear error messages

# Common Confusions
- **Confusion**: Parsing and evaluation are the same thing
  **Clarification**: "It would also be possible to combine the parser and the evaluator into one function and evaluate during parsing, but splitting them up this way makes the program clearer and more flexible." (lines 346-349)

# Source Reference
Chapter 12: Project: A Programming Language, Section "Parsing", lines 50-282 of 12-project-a-programming-language.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Central concept with extensive code examples
- Cross-reference status: verified
