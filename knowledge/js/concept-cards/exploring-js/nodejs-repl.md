---
# === CORE IDENTIFICATION ===
concept: Node.js REPL
slug: nodejs-repl

# === CLASSIFICATION ===
category: tooling
subcategory: development-tools
tier: intermediate

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Consoles: interactive JavaScript command lines"
chapter_number: 10
pdf_page: null
section: "10.1.2 The Node.js REPL"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - Node REPL
  - read-eval-print loop

# === TYPED RELATIONSHIPS ===
prerequisites:
  - node-js-platform
extends: []
related:
  - browser-console
  - console-api
contrasts_with:
  - browser-console

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I try out JavaScript code in Node.js?"
---

# Quick Definition

The Node.js REPL (Read-Eval-Print Loop) is an interactive command line started via the `node` command, allowing developers to type JavaScript expressions and see results immediately.

# Core Definition

"*REPL* stands for *read-eval-print loop* and basically means *command line*. To use it, you must first start Node.js from an operating system command line, via the command `node`." (Ch. 10, &sect;10.1.2). The REPL reads input, evaluates it, prints the result, and loops. Input is indicated by `>` in REPL interaction examples.

# Prerequisites

- **node-js-platform** -- the REPL runs on Node.js

# Key Properties

1. REPL = Read-Eval-Print Loop
2. Started via `node` command on the terminal
3. Input shown with `>` prefix in documentation
4. Evaluates JavaScript expressions and shows results
5. Useful for quick experimentation

# Construction / Recognition

```
$ node
> 3 + 5
8
```

# Context & Application

The Node.js REPL is used throughout the book for demonstrating expressions. It's a quick way to test JavaScript snippets without creating files.

# Examples

From the source text (Ch. 10, &sect;10.1.2):
```
> 3 + 5
8
```

# Relationships

## Builds Upon
- **node-js-platform** -- REPL is a Node.js feature

## Enables
- Quick JavaScript experimentation on the command line

## Related
- **console-api** -- output via `console.log()` in the REPL

## Contrasts With
- **browser-console** -- browser-based alternative

# Common Errors

- **Error**: Expecting multi-line statements to work the same as in files.
  **Correction**: REPL evaluates per-line; multi-line constructs may need careful formatting.

# Common Confusions

- **Confusion**: Thinking REPL output format matches `console.log()` output.
  **Clarification**: REPL shows the return value of expressions; `console.log()` prints to stdout separately.

# Source Reference

Chapter 10: Consoles, Section 10.1.2, lines 62-97.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicit definition with usage example
- Cross-reference status: verified
