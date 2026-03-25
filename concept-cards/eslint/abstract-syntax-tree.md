---
# === CORE IDENTIFICATION ===
concept: Abstract Syntax Tree
slug: abstract-syntax-tree

# === CLASSIFICATION ===
category: ast
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "use/core-concepts/glossary.md"
chapter_number: null
pdf_page: null
section: "Abstract Syntax Tree (AST)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "AST"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - estree
  - parsers
  - esquery-and-selectors
  - rules
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an AST?"
  - "What is an abstract syntax tree?"
  - "How does ESLint represent code internally?"
  - "What are AST nodes?"
---

# Quick Definition
An abstract syntax tree (AST) is a structured representation of code syntax where each section of source code is a node that may have properties and child nodes.

# Core Definition
An AST is a tree-shaped data structure representing the syntactic structure of source code. Each section of source code is referred to as a node, and each node may have any number of properties, including properties that store child nodes. ESLint uses the ESTree AST format. Parsers convert source code strings into ASTs, and ESLint rules are given an AST to evaluate, producing violations on parts of the AST when they detect problems.

# Prerequisites
Foundational computer science concept with no prerequisites within ESLint.

# Key Properties
1. **Hierarchical structure** -- Tree of nodes representing code syntax
2. **Node-based** -- Each section of code is a node with a type and properties
3. **Child nodes** -- Nodes may contain other nodes as properties
4. **ESTree format** -- ESLint uses the ESTree specification for its AST format
5. **Rule input** -- Rules receive the AST and check it for patterns

# Construction / Recognition
- Produced by parsers (Espree for standard JavaScript)
- Consumed by rules for pattern matching
- Can be queried using ESQuery selectors
- Each node has a `type` property (e.g., `BinaryExpression`, `Literal`, `ExpressionStatement`)

# Context & Application
ASTs are the foundation of how ESLint analyzes code. Rather than working with raw source text, ESLint converts code into an AST and then runs rules against the tree structure. This allows rules to reason about code structure rather than text patterns, making analysis more reliable and expressive.

# Examples
From use/core-concepts/glossary.md:
- "A structured representation of code syntax."
- "Each section of source code in an AST is referred to as a node."
- The code `1 + 2;` produces a tree with an `ExpressionStatement` containing a `BinaryExpression` with two `Literal` child nodes.

# Relationships
## Enables
- rules (pattern checking on AST)
- esquery-and-selectors (querying AST nodes)
- violations (produced from AST locations)

## Related
- estree (the specific AST format)
- parsers (produce ASTs)

# Common Errors
1. Assuming the AST contains formatting details -- ASTs represent structure, not whitespace or formatting (those are "trivia")

# Common Confusions
1. **AST vs. source code** -- The AST is a structured representation; it is not the raw text. Changes to whitespace may not change the AST
2. **AST vs. ESTree** -- AST is the general concept; ESTree is the specific format/specification ESLint uses

# Source Reference
- use/core-concepts/glossary.md: Abstract Syntax Tree (AST) definition, Node definition

# Verification Notes
- High confidence: Explicitly defined in the glossary with structural description
