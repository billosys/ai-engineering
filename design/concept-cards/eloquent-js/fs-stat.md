---
concept: stat
slug: fs-stat
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
  - fs.stat
  - file stats
prerequisites:
  - file-system-module
extends:
  - file-system-module
related:
  - fs-readdir
  - fs-readfile
contrasts_with: []
answers_questions:
  - "How do I check if a file exists or is a directory in Node.js?"
---

# Quick Definition
`stat` retrieves metadata about a file (size, modification date, type), with an `isDirectory()` method to distinguish files from directories, throwing an ENOENT error for nonexistent paths.

# Core Definition
"The `stats` object returned by `stat` tells us a number of things about a file, such as its size (`size` property) and its modification date (`mtime` property). Here we are interested in the question of whether it is a directory or a regular file, which the `isDirectory` method tells us" (Ch. 20).

# Prerequisites
- **File system module**: stat is from node:fs

# Key Properties
1. `stats.size` -- file size in bytes
2. `stats.mtime` -- last modification date
3. `stats.isDirectory()` -- true if path is a directory
4. Throws error with `code: "ENOENT"` if file doesn't exist
5. Promise version from node:fs/promises

# Construction / Recognition
```javascript
import {stat} from "node:fs/promises";
try {
  let stats = await stat(path);
  if (stats.isDirectory()) { /* ... */ }
} catch (error) {
  if (error.code != "ENOENT") throw error;
  return {status: 404, body: "File not found"};
}
```

# Context & Application
Used to determine file type before reading, check file existence, and serve appropriate responses in file servers.

# Examples
From the file server's GET handler:
```javascript
let stats = await stat(path);
if (stats.isDirectory()) {
  return {body: (await readdir(path)).join("\n")};
} else {
  return {body: createReadStream(path), type: lookup(path)};
}
```

# Relationships
## Builds Upon
- file-system-module
## Enables
- File type checking, existence verification, metadata access
## Related
- fs-readdir, fs-readfile, http-createserver
## Contrasts With
- access() (only checks existence/permissions, not metadata)

# Common Errors
- **Error**: Using stat to check existence before read (TOCTOU race condition)
  **Correction**: For simple reads, just try the operation and handle ENOENT

# Common Confusions
- **Confusion**: stat throws a normal Error for missing files
  **Clarification**: The error has a `code` property; "ENOENT" means "no such file or directory"

# Source Reference
Chapter 20: Node.js, Section "The filesystem module", line 415; file server, lines 774-827 of 20-nodejs.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Used in practical file server example
- Cross-reference status: verified
