---
concept: Node CLI
slug: node-cli
category: server-side
subcategory: node-core
tier: intermediate
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Node.js"
chapter_number: 20
pdf_page: null
section: "The node command"
extraction_confidence: high
aliases:
  - node command
  - node REPL
prerequisites:
  - nodejs
extends: []
related:
  - process-object
contrasts_with: []
answers_questions:
  - "How do I run a JavaScript file with Node?"
  - "What is the Node.js REPL?"
---

# Quick Definition
The `node` command runs JavaScript files from the terminal or, without arguments, opens an interactive REPL (Read-Eval-Print Loop) for typing and evaluating JavaScript expressions.

# Core Definition
"When Node.js is installed on a system, it provides a program called `node`, which is used to run JavaScript files" (Ch. 20). Running `node` without a file "provides you with a prompt at which you can type JavaScript code and immediately see the result." `console.log` in Node prints to standard output (the terminal).

# Prerequisites
- **Node.js**: The node command comes with Node installation

# Key Properties
1. `node file.js` -- run a script file
2. `node` (no args) -- start interactive REPL
3. Output goes to stdout (terminal), not browser console
4. `.mjs` extension enables ES module syntax

# Construction / Recognition
```bash
$ node hello.js
Hello world

$ node
> 1 + 1
2
> process.exit(0)
```

# Context & Application
The primary way to execute Node scripts, test code interactively, and develop server-side applications.

# Examples
Running an ES module:
```bash
$ node main.mjs JavaScript
tpircSavaJ
```

# Relationships
## Builds Upon
- nodejs
## Enables
- Script execution, interactive development, server startup
## Related
- process-object
## Contrasts With
- Browser developer console (different environment)

# Common Errors
- **Error**: Using import/export in a .js file without package.json type: "module"
  **Correction**: Use .mjs extension or set "type": "module" in package.json

# Common Confusions
- **Confusion**: The Node REPL is the same as the browser console
  **Clarification**: The Node REPL has no DOM, no window, but has process, fs, etc.

# Source Reference
Chapter 20: Node.js, Section "The node command", lines 80-151 of 20-nodejs.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Clear explanation
- Cross-reference status: verified
