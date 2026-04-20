---
concept: WebAssembly
slug: web-assembly
category: web-development
subcategory: null
tier: foundational
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Next steps: overview of web development"
chapter_number: 49
pdf_page: null
section: "49.2.1 Keep an eye on WebAssembly (Wasm)!"
extraction_confidence: high
aliases:
  - Wasm
prerequisites: []
extends: []
related:
  - web-development-overview
contrasts_with: []
answers_questions:
  - "What should I learn next for web development?"
---

# Quick Definition

WebAssembly (Wasm) is a universal virtual machine built into most JavaScript engines that runs static, lower-level code at near-native speed, complementing JavaScript which handles dynamic, higher-level code.

# Core Definition

"Exploring JavaScript" Ch. 49: "WebAssembly is a universal virtual machine that is built into most JavaScript engines. We often get the following distribution of work: JavaScript is for dynamic, higher-level code. WebAssembly is for static, lower-level code." C/C++ compiled to Wasm is "about 50% as fast as the same code, compiled to native."

# Prerequisites

Foundational concept with no prerequisites.

# Key Properties

1. Built into most JavaScript engines
2. Near-native performance for static/lower-level code
3. Good compilation target for C, C++, Rust, etc.
4. JavaScript will NOT be replaced by Wasm (all browser APIs are JS-based)
5. JavaScript will NOT be compiled to Wasm (would lose optimization benefits)
6. WASI (WebAssembly System Interface) extends Wasm beyond browsers
7. Use cases: video codecs, machine learning, gaming

# Construction / Recognition

Not demonstrated with code. WebAssembly modules are loaded and instantiated via JavaScript APIs.

# Context & Application

WebAssembly is complementary to JavaScript, not a replacement. JavaScript remains the best choice for high-level, dynamic web code. Wasm excels for compute-intensive, lower-level tasks.

# Examples

From the source: "Use cases include support for new video formats, machine learning, gaming, etc."

(Ch. 49, Section 49.2.1, lines 162-167)

# Relationships

## Related
- **Web development overview** -- Wasm is part of the web platform

# Common Errors

- **Error**: Expecting WebAssembly to replace JavaScript for web development
  **Correction**: JavaScript and Wasm are complementary; JS for high-level, Wasm for low-level

# Common Confusions

- **Confusion**: WebAssembly is only for browsers
  **Clarification**: WASI enables Wasm to run outside browsers, in clouds and embedded devices

# Source Reference

Chapter 49: Next steps: overview of web development, Section 49.2.1, lines 151-224.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit section with clear positioning
- Cross-reference status: verified
