---
# === CORE IDENTIFICATION ===
concept: Host Environments
slug: host-environments

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: language-overview
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Introduction to JavaScript"
chapter_number: 1
pdf_page: 19
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - runtime environment
  - execution environment

# === TYPED RELATIONSHIPS ===
prerequisites:
  - javascript-language-overview
extends: []
related:
  - global-object
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures?"
---

# Quick Definition

A host environment is the platform in which JavaScript runs, providing input/output capabilities and APIs beyond the core language — the two primary host environments are web browsers and Node.js.

# Core Definition

The core JavaScript language "defines a minimal API for working with numbers, text, arrays, sets, maps, and so on, but does not include any input or output functionality. Input and output (as well as more sophisticated features, such as networking, storage, and graphics) are the responsibility of the 'host environment' within which JavaScript is embedded." (p. 19-20)

# Prerequisites

- **javascript-language-overview** — Must understand the language to understand where it runs

# Key Properties

1. The core language has no I/O — host environments provide it
2. Web browsers: provide DOM, HTTP requests, mouse/keyboard input, HTML/CSS output
3. Node.js: provides file system access, networking, HTTP server capabilities
4. Each host environment has its own global object and APIs
5. The browser has been available since the language's creation; Node since 2010

# Construction / Recognition

Browser environment: code runs in `<script>` tags or the developer console.
Node environment: code runs via `node filename.js` or the Node REPL.

# Context & Application

Understanding host environments is important because many APIs that feel like "JavaScript" (e.g., `document`, `window`, `fs`, `process`) are actually provided by the host environment, not the core language.

# Examples

From the source text (p. 20):
- Browser: "allows JavaScript code to obtain input from the user's mouse and keyboard and by making HTTP requests. And it allows JavaScript code to display output to the user with HTML and CSS."
- Node: "gives JavaScript access to the entire operating system, allowing JavaScript programs to read and write files, send and receive data over the network, and make and serve HTTP requests."

# Relationships

## Builds Upon
- **javascript-language-overview** — Host environments are where the language executes

## Enables
- **global-object** — Each host environment provides a different global object

## Related
- **global-object** — The global object varies by host environment (Window in browsers, global in Node)

## Contrasts With
- None within this source

# Common Errors

- **Error**: Assuming `document` or `process` are part of core JavaScript.
  **Correction**: These are host-environment-specific APIs provided by browsers and Node.js respectively.

# Common Confusions

- **Confusion**: JavaScript can only run in web browsers.
  **Clarification**: Since 2010, Node.js has provided a server-side host environment for JavaScript.

# Source Reference

Chapter 1: Introduction to JavaScript, pages 19-20.

# Verification Notes

- Definition source: Direct quote from pp. 19-20
- Confidence rationale: High — clearly explained in the source
- Uncertainties: None
- Cross-reference status: Verified
