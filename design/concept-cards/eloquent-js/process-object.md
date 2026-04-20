---
concept: Process Object
slug: process-object
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
  - process
  - process.argv
  - process.exit
prerequisites:
  - nodejs
extends: []
related:
  - node-cli
contrasts_with: []
answers_questions:
  - "How do I access command-line arguments in Node.js?"
  - "How do I exit a Node.js program?"
---

# Quick Definition
The `process` global object in Node.js provides information about and control over the current process, including command-line arguments (`argv`), the current working directory (`cwd()`), and the ability to exit (`exit()`).

# Core Definition
"The `process` binding, just like the `console` binding, is available globally in Node. It provides various ways to inspect and manipulate the current program" (Ch. 20). `process.exit(code)` ends the process with a status code (0 = success). `process.argv` is an array of command-line arguments where actual arguments start at index 2.

# Prerequisites
- **Node.js**: process is a Node global

# Key Properties
1. `process.argv` -- array of command-line arguments (node, script, args...)
2. `process.exit(code)` -- terminate with exit status
3. `process.cwd()` -- current working directory
4. Available globally (no import needed)

# Construction / Recognition
```bash
$ node showargv.js one --and two
["node", "/tmp/showargv.js", "one", "--and", "two"]
```

```javascript
let argument = process.argv[2]; // first real argument
```

# Context & Application
Essential for building CLI tools. Every Node script that accepts arguments or needs to report success/failure uses the process object.

# Examples
```javascript
import {reverse} from "./reverse.mjs";
let argument = process.argv[2];
console.log(reverse(argument));
```

# Relationships
## Builds Upon
- nodejs
## Enables
- CLI tools, exit status reporting, environment access
## Related
- node-cli, path-module
## Contrasts With
- Browser window object (different global context)

# Common Errors
- **Error**: Reading process.argv[0] as the first argument
  **Correction**: argv[0] is "node", argv[1] is the script; actual arguments start at index 2

# Common Confusions
- **Confusion**: process.exit() is always needed
  **Clarification**: Node exits automatically when there's nothing left to do; exit() is for early termination

# Source Reference
Chapter 20: Node.js, Section "The node command", lines 82-151 of 20-nodejs.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Explicitly explained with examples
- Cross-reference status: verified
