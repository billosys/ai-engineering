---
concept: readdir
slug: fs-readdir
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
  - fs.readdir
prerequisites:
  - file-system-module
extends:
  - file-system-module
related:
  - fs-stat
  - fs-readfile
contrasts_with: []
answers_questions:
  - "How do I list files in a directory with Node.js?"
---

# Quick Definition
`readdir` returns an array of filenames in a directory, used for listing directory contents in file servers and build tools.

# Core Definition
"The `node:fs` module contains many other useful functions: `readdir` will give you the files in a directory as an array of strings" (Ch. 20). In the file server example, `readdir` lists directory contents when a GET request targets a directory.

# Prerequisites
- **File system module**: readdir is from node:fs

# Key Properties
1. Returns array of filename strings (not full paths)
2. Available in callback, promise, and sync variants
3. Does not include "." and ".." entries

# Construction / Recognition
```javascript
import {readdir} from "node:fs/promises";
let files = await readdir(path);
return {body: files.join("\n")};
```

# Context & Application
Used in file servers, build tools, directory scanners, and any application that needs to enumerate files.

# Examples
From the file server:
```javascript
if (stats.isDirectory()) {
  return {body: (await readdir(path)).join("\n")};
}
```

# Relationships
## Builds Upon
- file-system-module
## Enables
- Directory listing, file discovery, build tooling
## Related
- fs-stat, fs-readfile
## Contrasts With
- glob patterns (readdir lists direct children only)

# Common Errors
- **Error**: Expecting full paths from readdir
  **Correction**: readdir returns only filenames; construct full paths with path.join

# Common Confusions
- **Confusion**: readdir recursively lists all files
  **Clarification**: It only lists immediate children; recursion requires manual implementation

# Source Reference
Chapter 20: Node.js, Section "The filesystem module", lines 413-418; file server GET handler, lines 780-800 of 20-nodejs.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Used in practical example
- Cross-reference status: verified
