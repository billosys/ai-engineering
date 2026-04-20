---
concept: Transpilers
slug: transpilers
category: web-development
subcategory: tooling
tier: foundational
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Next steps: overview of web development"
chapter_number: 49
pdf_page: null
section: "49.3.1.1 Transpilers"
extraction_confidence: high
aliases:
  - source-to-source compilers
prerequisites: []
extends: []
related:
  - javascript-tools-overview
  - bundlers
contrasts_with: []
answers_questions:
  - "What JavaScript-related tools should I know about?"
---

# Quick Definition

A transpiler is a compiler that compiles source code to source code. TypeScript (JavaScript superset with static typing) and Babel (compiles modern JS to older versions) are the two most popular JavaScript transpilers.

# Core Definition

"Exploring JavaScript" Ch. 49: "A transpiler is a compiler that compiles source code to source code." TypeScript "is a superset of JavaScript. Roughly, it is the latest version of JavaScript plus static typing." The TypeScript compiler `tsc` both type-checks and compiles TypeScript to JavaScript. Babel "compiles upcoming and modern JavaScript features to older versions of the language."

# Prerequisites

Foundational concept with no prerequisites.

# Key Properties

1. TypeScript: static typing + compilation to JavaScript
2. Babel: modern JS features to older browser-compatible JS
3. Trend: faster tools for compilation, `tsc` only for type-checking
4. Babel usage declining due to evergreen browsers and TypeScript popularity

# Construction / Recognition

Not demonstrated with code in the source. TypeScript files use `.ts` extension; Babel configured via `.babelrc`.

# Context & Application

Transpilers enable using modern language features while maintaining compatibility. TypeScript is the dominant choice for adding type safety.

# Examples

From the source: TypeScript performs two tasks: type-checking and compiling to JavaScript. "One important trend is to use faster tools (such as bundlers) for the relatively simple task of compiling TypeScript to JavaScript."

(Ch. 49, Section 49.3.1.1, lines 248-274)

# Relationships

## Related
- **JavaScript tools overview** -- transpilers are one tool category
- **Bundlers** -- often handle transpilation as a step

# Common Errors

- **Error**: Assuming TypeScript code runs directly in browsers
  **Correction**: TypeScript must be compiled to JavaScript first

# Common Confusions

- **Confusion**: Transpilation and compilation are different things
  **Clarification**: Transpilation is a form of compilation; the term emphasizes source-to-source transformation

# Source Reference

Chapter 49: Next steps: overview of web development, Section 49.3.1.1, lines 248-274.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit definition with two key examples
- Cross-reference status: verified
