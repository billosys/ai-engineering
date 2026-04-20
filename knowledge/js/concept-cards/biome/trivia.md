---
# === CORE IDENTIFICATION ===
concept: Trivia
slug: trivia

# === CLASSIFICATION ===
category: architecture
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Biome Documentation"
source_slug: biome
authors: "Biome Contributors"
chapter: "internals/architecture.mdx"
chapter_number: null
pdf_page: null
section: "Parser and CST"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "leading trivia"
  - "trailing trivia"
  - "syntax trivia"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - concrete-syntax-tree
extends: []
related:
  - green-and-red-tree-pattern
  - resilient-parser
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is trivia in the context of Biome's parser?"
  - "How does Biome represent whitespace and comments in its syntax tree?"
---

# Quick Definition
Trivia is the term for all syntactically insignificant information in source code -- spaces, tabs, and comments -- that the CST preserves by attaching to adjacent syntax nodes as either leading or trailing trivia.

# Core Definition
Trivia is represented by all the information that is not important for a program to run: spaces, tabs, and comments. Trivia is attached to a node in the CST. A node can have leading trivia and trailing trivia. Reading code from left to right, leading trivia appears before a keyword, and trailing trivia appears after a keyword.

# Prerequisites
- concrete-syntax-tree: Must understand what the CST is and that it preserves all source information

# Key Properties
1. **Three types** -- Spaces, tabs, and comments
2. **Attached to nodes** -- Trivia is not free-floating; it is attached to specific syntax nodes
3. **Directional** -- Categorized as either leading (before) or trailing (after) a token
4. **Leading trivia rule** -- Every trivia up to the token/keyword, including line breaks, is leading trivia
5. **Trailing trivia rule** -- Everything after the token until the next line break (but not including it) is trailing trivia

# Construction / Recognition
To determine whether trivia is leading or trailing:
- **Trailing trivia**: Everything on the same line after a token, up to (but not including) the next line break
- **Leading trivia**: Everything from the start of a line (or after previous trailing trivia) up to and including the token's line breaks, before the token itself

# Context & Application
Trivia is essential for tools that need to preserve or manipulate whitespace and comments. The formatter uses trivia information to reformat code while preserving comments in their correct positions. The linter can inspect comments for directives (like disable comments). Without trivia in the syntax tree, these tools would lose critical information.

# Examples
From internals/architecture.mdx, "Parser and CST" section:

```js
const a = "foo"; // comment 1
// comment 2
const b = "bar";
```

In the CST representation:
- `// comment 1` is **trailing trivia** of the `;` (SEMICOLON) token, because it appears on the same line after the semicolon
- `// comment 2` is **leading trivia** of the `const` (CONST_KW) keyword, because it appears on a preceding line before the keyword

CST representation:
```
SEMICOLON@15..27 ";" [] [Whitespace(" "), Comments("// comment 1")]
CONST_KW@27..45 "const" [Newline("\n"), Comments("// comment 2"), Newline("\n")] [Whitespace(" ")]
```

# Relationships
## Builds Upon
- concrete-syntax-tree

## Enables
- Comment-preserving formatting
- Comment-aware linting

## Related
- green-and-red-tree-pattern

## Contrasts With
- Significant syntax tokens (keywords, operators, identifiers)

# Common Errors
1. Assuming comments on the next line are trailing trivia of the previous token -- they are actually leading trivia of the next token
2. Forgetting that line breaks themselves are part of trivia categorization (line breaks delimit trailing from leading)

# Common Confusions
1. **Trivia vs. insignificant tokens** -- Trivia is not discarded; it is preserved in the CST and attached to nodes. The term "not important for a program to run" means runtime insignificance, not that the information is thrown away.
2. **Leading vs. trailing boundary** -- The line break is the boundary: same-line content after a token is trailing; content on subsequent lines before the next token is leading.

# Source Reference
- internals/architecture.mdx: "Parser and CST" section, trivia definition and example

# Verification Notes
- High confidence: Explicitly defined with clear rules and a detailed example in the source
