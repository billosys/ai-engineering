---
concept: File System Module
slug: file-system-module
category: server-side
subcategory: node-modules
tier: intermediate
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Node.js"
chapter_number: 20
pdf_page: null
section: "The filesystem module"
extraction_confidence: high
aliases:
  - node:fs
  - fs module
prerequisites:
  - nodejs
  - module
extends: []
related:
  - fs-readfile
  - fs-writefile
  - fs-readdir
  - fs-stat
  - stream
contrasts_with: []
answers_questions:
  - "How do I read and write files in Node.js?"
  - "What is the Node.js fs module?"
---

# Quick Definition
The `node:fs` module provides functions for reading, writing, and managing files and directories, available in callback-based (`node:fs`), promise-based (`node:fs/promises`), and synchronous variants.

# Core Definition
"One of the most commonly used built-in modules in Node is the `node:fs` module, which stands for filesystem. It exports functions for working with files and directories" (Ch. 20, "The filesystem module"). Three API styles: callback (readFile), promise (from node:fs/promises), and synchronous (readFileSync).

# Prerequisites
- **Node.js**: fs is a Node built-in module
- **Modules**: Accessed via import

# Key Properties
1. `readFile` -- read file contents
2. `writeFile` -- write data to a file
3. `readdir` -- list files in a directory
4. `stat` -- get file information
5. `rename`, `unlink` -- rename/delete files
6. Promise versions in `node:fs/promises`
7. Sync versions (readFileSync) block the process

# Construction / Recognition
```javascript
import {readFile} from "node:fs";
readFile("file.txt", "utf8", (error, text) => {
  if (error) throw error;
  console.log("The file contains:", text);
});
```

Promise-based:
```javascript
import {readFile} from "node:fs/promises";
readFile("file.txt", "utf8")
  .then(text => console.log("The file contains:", text));
```

# Context & Application
Essential for any Node application that works with files: reading configuration, serving static files, logging, data persistence.

# Examples
Synchronous reading:
```javascript
import {readFileSync} from "node:fs";
console.log(readFileSync("file.txt", "utf8"));
```

# Relationships
## Builds Upon
- nodejs, module
## Enables
- File I/O, server-side data persistence, build tools
## Related
- fs-readfile, fs-writefile, fs-readdir, fs-stat, stream, path-module
## Contrasts With
- Browser file access (requires user selection via file input)

# Common Errors
- **Error**: Not passing encoding to readFile, getting a Buffer instead of string
  **Correction**: Pass "utf8" as second argument for text files

# Common Confusions
- **Confusion**: node:fs and node:fs/promises are different modules
  **Clarification**: Same functions, different API styles (callbacks vs promises)

# Source Reference
Chapter 20: Node.js, Section "The filesystem module", lines 354-456 of 20-nodejs.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Three API styles explained with examples
- Cross-reference status: verified
