---
concept: fs Module (File System)
slug: fs-module
category: node-apis
subcategory: file system
tier: foundational
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Server-Side JavaScript with Node"
chapter_number: 16
pdf_page: 620
section: "16.7 Working with Files"
extraction_confidence: high
aliases:
  - filesystem module
  - fs.readFile
  - fs.writeFile
  - fs/promises
prerequisites:
  - node-programming-model
  - error-first-callbacks
extends: []
related:
  - path-module
  - node-streams
contrasts_with: []
answers_questions:
  - "How do I create an HTTP server in Node.js?"
---

# Quick Definition

Node's "fs" module provides a comprehensive API for file I/O with three variants for each operation: callback-based (`fs.readFile`), synchronous (`fs.readFileSync`), and Promise-based (`fs.promises.readFile`), plus streaming APIs via `createReadStream` and `createWriteStream`.

# Core Definition

The "fs" module is Node's API for working with files and directories. Most functions come in callback-based, synchronous (Sync suffix), and Promise-based (fs.promises namespace) variants. Key functions include `readFile`/`writeFile` (whole-file operations), `createReadStream`/`createWriteStream` (streaming), `copyFile`, `rename`, `unlink` (delete), `stat` (metadata), `mkdir`, and `readdir`. An encoding argument (e.g., "utf8") returns strings instead of Buffers (Flanagan, Ch. 16, pp. 620-630).

# Prerequisites

- **node-programming-model** — Must understand Node's async model.
- **error-first-callbacks** — The callback variants use this pattern.

# Key Properties

1. Three API styles: callback, sync, Promise-based.
2. `readFile`/`writeFile` for whole-file operations.
3. `createReadStream`/`createWriteStream` for streaming.
4. `stat()` returns file metadata (size, timestamps, permissions).
5. `unlink()` deletes files (Unix naming convention).
6. `fs.promises` provides native Promise-based versions (Node 10+).

# Construction / Recognition

```javascript
const fs = require("fs");
let text = fs.readFileSync("data.csv", "utf8");
fs.promises.readFile("data.csv", "utf8").then(processFileText);
```

# Context & Application

Essential for any Node program that reads configuration, processes data files, serves static content, or logs output.

# Examples

From the source (p. 622-624): Reading files synchronously, with callbacks, and with Promises/async-await. Writing files with `writeFile`, `appendFile`, and `createWriteStream`.

# Relationships

## Builds Upon
- **node-programming-model** — Uses Node's async patterns
- **error-first-callbacks** — Callback-based variants use this pattern

## Enables
- File-based applications, servers, scripts

## Related
- **path-module** — Complements fs with path manipulation
- **node-streams** — fs streaming APIs return stream objects

## Contrasts With
- (None)

# Common Errors

- **Error**: Using synchronous file operations in a server's request handler.
  **Correction**: Use async or Promise-based variants to avoid blocking the event loop.

# Common Confusions

- **Confusion**: `fs.unlink()` is for unlinking a directory.
  **Clarification**: `unlink()` deletes a file. Use `rmdir()` for empty directories.

# Source Reference

Chapter 16: Server-Side JavaScript with Node, Section 16.7, pages 620-630.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Comprehensive section covering all variants
- Uncertainties: None
- Cross-reference status: Verified
