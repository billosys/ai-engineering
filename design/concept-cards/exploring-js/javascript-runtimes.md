---
concept: JavaScript Runtimes
slug: javascript-runtimes
category: web-development
subcategory: null
tier: foundational
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Next steps: overview of web development"
chapter_number: 49
pdf_page: null
section: "49.2 Things worth learning for web development"
extraction_confidence: high
aliases:
  - server-side JavaScript
  - Node.js runtimes
prerequisites: []
extends: []
related:
  - web-development-overview
  - package-managers
contrasts_with: []
answers_questions:
  - "What should I learn next for web development?"
---

# Quick Definition

JavaScript runtimes are platforms that execute JavaScript outside the browser, used for server-side code and command-line tools. Node.js is the most popular, with Deno and Bun as alternatives. WinterCG standardizes API interoperability across runtimes.

# Core Definition

"Exploring JavaScript" Ch. 49: "Some JavaScript platforms are for running code on servers. But they are also used for running command-line tools. The most popular runtime is Node.js. Most JavaScript-related tools (even compilers!) are implemented in Node.js-based JavaScript and installed via npm." Other runtimes include Deno and Bun. WinterCG "aims to provide a space for JavaScript runtimes to collaborate on API interoperability."

# Prerequisites

Foundational concept with no prerequisites.

# Key Properties

1. Node.js: most popular, used for servers and CLI tools
2. Deno: alternative runtime by Node.js creator
3. Bun: fast alternative runtime
4. WinterCG: standardizes cross-runtime API interoperability
5. Most JS tools are implemented in Node.js

# Construction / Recognition

Not a code construct. Runtimes are execution environments.

# Context & Application

Understanding runtimes is essential for server-side JavaScript development and for running JavaScript development tools.

# Examples

From the source: "A good way to get started with Node.js, is to use it for shell scripting."

(Ch. 49, Section 49.2, lines 109-110)

# Relationships

## Related
- **Web development overview** -- runtimes are part of the web ecosystem
- **Package managers** -- npm is Node.js's package manager

# Common Errors

- **Error**: Assuming browser APIs are available in Node.js
  **Correction**: Browser-specific APIs (DOM, window) are not available in server runtimes

# Common Confusions

- **Confusion**: JavaScript can only run in browsers
  **Clarification**: JavaScript runs on servers (Node.js, Deno, Bun), in CLI tools, and in many other environments

# Source Reference

Chapter 49: Next steps: overview of web development, Section 49.2, lines 105-118.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit discussion of runtimes
- Cross-reference status: verified
