---
# === CORE IDENTIFICATION ===
concept: Hashbang Lines
slug: hashbang-lines

# === CLASSIFICATION ===
category: syntax-fundamentals
subcategory: basic-syntax
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Syntax"
chapter_number: 9
pdf_page: null
section: "9.3 Hashbang lines (Unix shell scripts)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - shebang
  - sha-bang
  - sharp-exclamation

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - node-js-platform
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a hashbang line in JavaScript?"
---

# Quick Definition

A hashbang line (`#!`) at the start of a JavaScript file specifies which executable should run the script, standardized in ES2023 and commonly used with Node.js.

# Core Definition

"In a Unix shell script, we can add a first line that starts with `#!` to tell Unix which executable should be used to run the script." (Ch. 9, &sect;9.3). ^ES2023^: Hashbang grammar was standardized so JavaScript formally ignores the first line if it starts with `#!`. Common form for Node.js: `#!/usr/bin/env node`.

# Prerequisites

Foundational concept with no prerequisites.

# Key Properties

1. ^ES2023^: Formally standardized in ECMAScript 2023
2. First line only; starts with `#!`
3. Treated as a comment by JavaScript
4. Common: `#!/usr/bin/env node`
5. Use `env -S` for passing arguments to node

# Construction / Recognition

```
#!/usr/bin/env node
```
Or with arguments:
```
#!/usr/bin/env -S node --enable-source-maps
```

# Context & Application

Used for creating executable Node.js scripts that can be run directly from the command line without explicitly calling `node`.

# Examples

From the source text (Ch. 9, &sect;9.3; Ch. 6, &sect;6.3):
```
#!/usr/bin/env node
#!/usr/bin/env -S node --enable-source-maps --no-warnings=ExperimentalWarning
```

# Relationships

## Builds Upon
- No prerequisites

## Enables
- Executable Node.js shell scripts

## Related
- **node-js-platform** -- hashbangs are primarily used with Node.js

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Placing the hashbang line anywhere other than the first line.
  **Correction**: The hashbang must be the very first line of the file.

# Common Confusions

- **Confusion**: Thinking hashbang lines are JavaScript comments.
  **Clarification**: They are treated as comments by JS, but their purpose is to tell the OS which interpreter to use.

# Source Reference

Chapter 9: Syntax, Section 9.3, lines 576-593. Chapter 6, Section 6.3, lines 433-441.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicitly described with examples
- Cross-reference status: verified across Ch. 6 and Ch. 9
