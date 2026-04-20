---
# === CORE IDENTIFICATION ===
concept: Bogus Nodes
slug: bogus-nodes

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
  - "bogus node"
  - JsBogusStatement
  - JsBogusExpression

# === TYPED RELATIONSHIPS ===
prerequisites:
  - resilient-parser
  - concrete-syntax-tree
extends: []
related:
  - trivia
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a bogus node?"
  - "How does Biome mark erroneous syntax in the CST?"
---

# Quick Definition
Bogus nodes are special CST nodes that Biome's parser uses to wrap and isolate syntax that could not be correctly parsed, protecting downstream consumers from processing invalid syntax as if it were valid.

# Core Definition
The parser uses "Bogus" nodes to protect consumers from consuming incorrect syntax. These nodes are used to decorate the broken code caused by a syntax error. When the parser cannot properly understand the syntax during the recovery phase, it wraps the erroneous tokens in bogus nodes (such as `JsBogusStatement`) to clearly mark them as invalid within the CST.

# Prerequisites
- resilient-parser: Must understand how the parser handles errors and recovers
- concrete-syntax-tree: Must understand the CST structure that bogus nodes exist within

# Key Properties
1. **Consumer protection** -- Primary purpose is to protect downstream tools from processing incorrect syntax
2. **Error decoration** -- Wraps broken code caused by syntax errors
3. **Language-specific types** -- Named by language and syntax category (e.g., `JsBogusStatement`, `JsBogusExpression`)
4. **Contains raw tokens** -- Bogus nodes contain the actual tokens from the source that could not be parsed into proper syntax nodes
5. **Last-resort mechanism** -- Used when the parser cannot recover to produce correct syntax nodes

# Construction / Recognition
Bogus nodes are created automatically by the parser when it encounters syntax it cannot recover from. They are recognizable in CST output by their `Bogus` naming convention (e.g., `JsBogusStatement`). They contain an `items` list with the raw tokens that could not be parsed.

# Context & Application
Bogus nodes serve as a safety mechanism in the toolchain. When the linter or formatter encounters a bogus node, it knows to skip or handle that section specially rather than attempting to analyze or format clearly broken syntax. This prevents cascading errors where tools might misinterpret invalid syntax and produce misleading diagnostics or incorrect transformations.

# Examples
From internals/architecture.mdx, "Resilient and recoverable parser" section:

Given the malformed code:
```js
function}
```

The parser produces a `JsBogusStatement` wrapping the stray `}` token:
```
JsBogusStatement {
  items: [
    R_CURLY@8..9 "}" [] [],
  ],
},
```

The source explains: "The parser can't properly understand the syntax during the recovery phase, so it needs to rely on the bogus nodes to mark some syntax as erroneous."

# Relationships
## Builds Upon
- resilient-parser
- concrete-syntax-tree

## Enables
- Safe downstream processing of malformed code
- Clear separation of valid and invalid syntax in the tree

## Related
- trivia

## Contrasts With
- Regular syntax nodes (which represent correctly parsed code)
- Missing nodes (which represent expected but absent tokens, not erroneous tokens)

# Common Errors
1. Treating bogus nodes as regular syntax nodes -- they should be handled specially or skipped by tools
2. Assuming bogus nodes mean the entire file failed to parse -- only the specific section wrapped in the bogus node is erroneous

# Common Confusions
1. **Bogus nodes vs. missing nodes** -- Missing nodes represent tokens the parser expected but did not find (like `missing (required)` for a missing parenthesis). Bogus nodes wrap tokens that are present but could not be incorporated into valid syntax.
2. **Bogus nodes vs. parse errors** -- Bogus nodes are the CST representation of unparseable syntax; parse errors are the diagnostic messages reported to the user. Both arise from the same situation but serve different purposes.

# Source Reference
- internals/architecture.mdx: "Resilient and recoverable parser" section, bogus node explanation and `function}` example

# Verification Notes
- High confidence: Explicitly defined with a clear example showing JsBogusStatement in the CST output
