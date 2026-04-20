---
concept: Static Checking
slug: static-checking
category: web-development
subcategory: tooling
tier: foundational
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Next steps: overview of web development"
chapter_number: 49
pdf_page: null
section: "49.3.2 Static checking"
extraction_confidence: high
aliases:
  - linting
  - type checking
  - code formatting
prerequisites: []
extends: []
related:
  - javascript-tools-overview
  - transpilers
contrasts_with: []
answers_questions:
  - "What JavaScript-related tools should I know about?"
---

# Quick Definition

Static checking analyzes source code without running it to detect problems. It includes linters (ESLint, Biome), code formatters (Prettier, Biome), and type checkers (TypeScript).

# Core Definition

"Exploring JavaScript" Ch. 49: "Static checking means analyzing source code statically (without running it). It can be used to detect a variety of problems." Four subcategories: linters (check for problematic patterns), code style checkers (check formatting), code formatters (automatically format), and type checkers (add static typing).

# Prerequisites

Foundational concept with no prerequisites.

# Key Properties

1. Linters: ESLint, Biome, oxlint -- detect anti-patterns, unused variables
2. Code formatters: Prettier, Biome -- automatically format code
3. Type checkers: TypeScript -- add static type checking
4. "Linters are especially useful if you are still learning the language"

# Construction / Recognition

Not demonstrated with code. Configured via tool-specific configuration files.

# Context & Application

Static checking catches bugs early, enforces code style consistency, and improves code quality without running the code.

# Examples

From the source: "Popular linters include ESLint, Biome, oxlint, quick-lint-js"

(Ch. 49, Section 49.3.2, lines 345-363)

# Relationships

## Related
- **JavaScript tools overview** -- static checking is one tool category
- **Transpilers** -- TypeScript is both a transpiler and type checker

# Common Errors

- **Error**: Ignoring linter warnings as noise
  **Correction**: Linter rules exist for good reasons; configure rules to match project needs

# Common Confusions

- **Confusion**: Code formatters and linters do the same thing
  **Clarification**: Formatters fix styling automatically; linters detect logical issues and anti-patterns

# Source Reference

Chapter 49: Next steps: overview of web development, Section 49.3.2, lines 345-363.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit categorization with tool names
- Cross-reference status: verified
