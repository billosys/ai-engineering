---
# === CORE IDENTIFICATION ===
concept: ESLint Architecture
slug: eslint-architecture

# === CLASSIFICATION ===
category: architecture
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "contribute/architecture/index.md"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "ESLint internal architecture"
  - "ESLint component architecture"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - eslint
extends: []
related:
  - eslint-source-code-object
  - rules
  - plugins
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the main components of ESLint's internal architecture?"
  - "How do ESLint's components communicate with each other?"
  - "What is the separation of concerns in ESLint?"
  - "What are the boundaries and responsibilities of each ESLint component?"
---

# Quick Definition
ESLint's internal architecture is organized into layered components -- cli, CLIEngine, Linter, SourceCode, and Rules -- each with strictly defined responsibilities and access constraints.

# Core Definition
ESLint's architecture follows a clear separation of concerns across several key modules. At the top level, `bin/eslint.js` bootstraps the CLI by passing command line arguments to the `cli` object. The `cli` object (`lib/cli.js`) handles I/O, file reading, directory traversal, and formatting. The `CLIEngine` class (`lib/cli-engine/`) manages configuration file loading, plugin/parser resolution, and delegates actual code verification to the `Linter` class. The `Linter` class (`lib/linter/`) is the core verification engine: it parses source text into an AST using espree (or a configured parser), traverses the AST emitting node-type events, and executes rules against those events. The `SourceCode` class (`lib/source-code/`) represents parsed source code alongside its AST. The `RuleTester` class (`lib/rule-tester/`) provides a testing harness modeled after Mocha. The public API (`lib/api.js`) exposes `Linter`, `ESLint`, `RuleTester`, and `SourceCode` via `require("eslint")`.

# Prerequisites
- eslint: Understanding ESLint's purpose and basic usage

# Key Properties
1. **Layered responsibility** -- Each component has explicit permissions (may/may not access filesystem, console, or process)
2. **Linter is I/O-free** -- The core `Linter` class performs no file I/O, no console output, and uses no Node.js-specific features, making it embeddable
3. **Event-driven traversal** -- The Linter emits AST node-type events (e.g., "Identifier", "Identifier:exit") during traversal, which rules subscribe to
4. **Rules are maximally constrained** -- Rules may only inspect the AST and report warnings; they cannot access the filesystem, console, or perform async operations
5. **CLI as thin wrapper** -- `bin/eslint.js` is intentionally minimal, delegating all logic to `cli`
6. **CLIEngine manages environment** -- Handles configuration loading, plugin resolution, and file discovery before delegating to Linter

# Construction / Recognition
- The public API exports four classes: `Linter`, `ESLint`, `RuleTester`, `SourceCode`
- The Linter's `verify()` method accepts source text and configuration, returns lint results
- The CLI object's `execute()` method accepts command-line argument arrays
- Each component has a strict "may not" list preventing boundary violations

# Context & Application
Understanding ESLint's architecture is essential for contributors working on ESLint core, for integration developers embedding ESLint in tools, and for plugin authors who need to understand what APIs are available within rule execution contexts. The layered design allows ESLint to be used as a CLI tool, as an embedded library in Node.js programs, or as part of editor integrations.

# Examples
From contribute/architecture/index.md:
- "`lib/linter/` - this module is the core `Linter` class that does code verifying based on configuration options. This file does no file I/O and does not interact with the `console` at all."
- "Once the AST is available, `estraverse` is used to traverse the AST from top to bottom. At each node, the `Linter` object emits an event that has the same name as the node type."
- "Individual rules are the most specialized part of the ESLint architecture. Rules can do very little, they are simply a set of instructions executed against an AST that is provided."

# Relationships
## Enables
- eslint-source-code-object
- rules
- plugins
- parsers

## Related
- abstract-syntax-tree
- configuration-files

## Contrasts With
- Monolithic linter designs where all components share state and I/O access

# Common Errors
1. Assuming rules can access the filesystem -- rules operate only on the AST provided to them
2. Confusing ESLint class with Linter class -- ESLint is the high-level async API; Linter is the synchronous core verifier

# Common Confusions
1. **CLIEngine vs. Linter** -- CLIEngine handles file discovery and config loading; Linter handles only code verification against a provided configuration
2. **ESLint class vs. cli object** -- The ESLint class is the programmatic API; the cli object is the command-line interface wrapper

# Source Reference
- contribute/architecture/index.md: Full architecture overview with component responsibilities and constraints

# Verification Notes
- High confidence: Architecture components and their responsibilities are explicitly documented
- Constraint lists ("may not") taken directly from architecture documentation
