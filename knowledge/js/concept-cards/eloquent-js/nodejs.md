---
concept: Node.js
slug: nodejs
category: server-side
subcategory: runtime
tier: intermediate
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Node.js"
chapter_number: 20
pdf_page: null
section: "Background"
extraction_confidence: high
aliases:
  - Node
  - node runtime
prerequisites:
  - function
  - module
extends: []
related:
  - process-object
  - file-system-module
  - http-module
contrasts_with: []
answers_questions:
  - "What is Node.js?"
  - "How do I run JavaScript outside the browser?"
---

# Quick Definition
Node.js is a program that runs JavaScript outside the browser, enabling command-line tools, HTTP servers, and other server-side applications using asynchronous, event-driven programming.

# Core Definition
"This chapter and the next one will briefly introduce Node.js, a program that allows you to apply your JavaScript skills outside of the browser. With it, you can build anything from small command line tools to HTTP servers that power dynamic websites" (Ch. 20). Node was designed for asynchronous programming: "Node was initially conceived for the purpose of making asynchronous programming easy and convenient."

# Prerequisites
- **Functions**: Node uses JavaScript functions
- **Modules**: Node has its own module system

# Key Properties
1. Runs JavaScript outside the browser
2. Designed for asynchronous I/O
3. Supports both CommonJS (require) and ES modules (import/export)
4. Built-in modules: node:fs, node:http, node:path
5. No browser APIs (no document, no prompt)
6. NPM for package management

# Construction / Recognition
```bash
$ node hello.js
Hello world
```

```javascript
// ES module (.mjs file)
import {reverse} from "./reverse.mjs";
console.log(reverse(process.argv[2]));
```

# Context & Application
Node powers web servers, build tools, CLI utilities, and full-stack JavaScript applications. It's the standard server-side JavaScript runtime.

# Examples
Running the REPL:
```
$ node
> 1 + 1
2
> [-1, -2, -3].map(Math.abs)
[1, 2, 3]
```

# Relationships
## Builds Upon
- function, module, async-function
## Enables
- Server-side JavaScript, CLI tools, file-system-module, http-module
## Related
- process-object, stream, path-module
## Contrasts With
- Browser JavaScript (has DOM, no filesystem access)

# Common Errors
- **Error**: Using browser APIs like document or prompt in Node
  **Correction**: Node has no browser APIs; use Node-specific modules instead

# Common Confusions
- **Confusion**: Node.js is a programming language
  **Clarification**: Node is a runtime for JavaScript; the language is JavaScript

# Source Reference
Chapter 20: Node.js, Sections "Background" and "The node command", lines 32-151 of 20-nodejs.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Core chapter topic, thoroughly introduced
- Cross-reference status: verified
