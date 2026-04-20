---
# === CORE IDENTIFICATION ===
concept: Resilient Parser
slug: resilient-parser

# === CLASSIFICATION ===
category: architecture
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Biome Documentation"
source_slug: biome
authors: "Biome Contributors"
chapter: "internals/architecture.mdx"
chapter_number: null
pdf_page: null
section: "Resilient and recoverable parser"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "error-resilient parser"
  - "recoverable parser"
  - "resilient and recoverable parser"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - concrete-syntax-tree
extends: []
related:
  - bogus-nodes
  - trivia
  - green-and-red-tree-pattern
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the CST relate to error-resilient parsing?"
  - "How does Biome handle syntax errors?"
---

# Quick Definition
Biome's resilient parser is a parser that can continue parsing after encountering syntax errors, recovering to produce a valid CST even from malformed source code, using bogus nodes to mark erroneous sections.

# Core Definition
In order to construct a CST, a parser needs to be error-resilient and recoverable. Resilient means a parser that is able to resume parsing after encountering syntax errors that belong to the language. Recoverable means a parser that is able to understand where an error occurred and resume parsing by creating correct information. The recoverable part is not a science, and no rules are set in stone -- depending on what was being parsed and where the error occurred, the parser may or may not recover in an expected way.

# Prerequisites
- concrete-syntax-tree: Must understand the CST data structure that the parser produces

# Key Properties
1. **Resilience** -- Able to resume parsing after encountering syntax errors
2. **Recoverability** -- Able to understand error locations and resume creating correct syntax nodes
3. **Non-deterministic recovery** -- Recovery quality depends on context; no fixed rules govern all cases
4. **Bogus node fallback** -- When recovery is not possible, bogus nodes mark erroneous syntax
5. **Missing node insertion** -- Can insert "missing" markers for expected but absent tokens

# Construction / Recognition
The resilient parser is Biome's internal parser implementation. Its behavior is observable through:
- CST output showing `missing (required)` for expected but absent tokens
- `JsBogusStatement` and similar bogus nodes for unrecoverable syntax
- Detailed parse error diagnostics indicating what was expected vs. found

# Context & Application
Error-resilient parsing is essential for editor integration, where developers are constantly writing incomplete or syntactically incorrect code. Without resilient parsing, Biome could not provide formatting, linting, or diagnostics for files that contain any syntax errors. This capability allows Biome to "format malformed code as you write it."

# Examples
From internals/architecture.mdx, "Resilient and recoverable parser" section:

**Good recovery** -- missing parentheses in `while`:
```js
while {}
```
The parser recovers well: parentheses and condition are marked as `missing (required)`, while the code block is correctly parsed as a `JsBlockStatement`.

**Partial recovery** -- malformed function declaration:
```js
function}
```
The parser cannot fully understand the syntax during recovery, so it creates a `JsBogusStatement` containing the stray `}` token, while also creating a `TsDeclareFunctionDeclaration` with missing required parts.

Error diagnostic example:
```
main.tsx:1:7 parse
  expected `(` but instead found `{`
  > 1 | while {}
            ^
```

# Relationships
## Builds Upon
- concrete-syntax-tree

## Enables
- bogus-nodes (as a fallback mechanism)
- Editor integration with incomplete code
- Formatting of malformed code

## Related
- trivia
- green-and-red-tree-pattern

## Contrasts With
- Traditional parsers that halt on the first syntax error

# Common Errors
1. Assuming the parser always recovers perfectly -- recovery quality is context-dependent and non-deterministic
2. Expecting bogus nodes only for severe errors -- even minor mismatches can produce bogus nodes if recovery is difficult in that context

# Common Confusions
1. **Resilient vs. recoverable** -- These are distinct properties. Resilient means the parser does not stop at errors. Recoverable means it can produce correct syntax information after an error. A parser can be resilient (continue parsing) without being fully recoverable (produce correct trees).
2. **Error recovery vs. error correction** -- The parser does not fix code; it represents broken code as accurately as possible in the CST using missing markers and bogus nodes.

# Source Reference
- internals/architecture.mdx: "Resilient and recoverable parser" section

# Verification Notes
- High confidence: Explicitly defined with two contrasting examples showing good and partial recovery
