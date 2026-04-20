---
# === CORE IDENTIFICATION ===
concept: Syntax Tree
slug: syntax-tree

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
  - parse tree
  - AST
  - abstract syntax tree

# === TYPED RELATIONSHIPS ===
prerequisites:
  - parsing
extends: []
related:
  - expression-evaluation
  - interpreter
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a syntax tree?"
---

# Quick Definition
A syntax tree is a tree-shaped data structure produced by a parser that represents the hierarchical structure of a program, where expressions contain other expressions as branches.

# Core Definition
"Such a data structure is called a *syntax tree*. If you imagine the objects as dots and the links between them as lines between those dots... the structure has a treelike shape. The fact that expressions contain other expressions, which in turn might contain more expressions, is similar to the way tree branches split and split again." (Eloquent JavaScript, Ch. 12, lines 127-132)

# Prerequisites
- **Parsing**: Syntax trees are the output of parsing

# Key Properties
1. Has a hierarchical (tree) structure with no cycles
2. Different node types represent different language elements (values, identifiers, applications)
3. Each node has a `type` property and type-specific properties
4. Leaf nodes represent atomic elements (numbers, strings, names)
5. Interior nodes represent compound expressions that contain sub-expressions

# Construction / Recognition
The Egg language uses three node types:
```json
{
  type: "apply",
  operator: {type: "word", name: ">"},
  args: [
    {type: "word", name: "x"},
    {type: "value", value: 5}
  ]
}
```
(lines 116-124)

- `"value"` nodes: literal strings or numbers with a `value` property
- `"word"` nodes: identifiers with a `name` property
- `"apply"` nodes: applications with `operator` and `args` properties

# Context & Application
Syntax trees are the intermediate representation between source text and execution. They are used in interpreters, compilers, code analyzers, and refactoring tools.

# Examples
From the source, the expression `>(x, 5)` produces:
```json
{
  type: "apply",
  operator: {type: "word", name: ">"},
  args: [
    {type: "word", name: "x"},
    {type: "value", value: 5}
  ]
}
```

The DOM (Chapter 14) is also described as having a tree structure similar to syntax trees.

# Relationships
## Builds Upon
- Parser output
## Enables
- Program evaluation and interpretation
- Code analysis and transformation
## Related
- DOM tree (similar tree structure for HTML documents)
- Expression evaluation
## Contrasts With
- Flat text representation of programs

# Common Errors
- **Error**: Assuming syntax trees always mirror the exact source text structure
  **Correction**: Abstract syntax trees may simplify or reorganize the source structure

# Common Confusions
- **Confusion**: The syntax tree is the program itself
  **Clarification**: The syntax tree is a *representation* of the program that can be evaluated

# Source Reference
Chapter 12: Project: A Programming Language, Section "Parsing", lines 96-134 of 12-project-a-programming-language.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Clearly defined with diagram and examples
- Cross-reference status: verified against Ch. 14 DOM tree discussion
