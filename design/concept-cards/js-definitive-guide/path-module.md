---
concept: path Module
slug: path-module
category: node-apis
subcategory: file system
tier: foundational
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Server-Side JavaScript with Node"
chapter_number: 16
pdf_page: 620
section: "16.7.1 Paths, File Descriptors, and FileHandles"
extraction_confidence: high
aliases:
  - path utilities
prerequisites:
  - node-programming-model
extends: []
related:
  - fs-module
contrasts_with: []
answers_questions:
  - "How do I create an HTTP server in Node.js?"
---

# Quick Definition

Node's "path" module provides cross-platform utility functions for manipulating file paths, including `basename()`, `dirname()`, `extname()`, `join()`, `resolve()`, and `normalize()`.

# Core Definition

The "path" module defines utility functions for working with file and directory names. Key functions include `path.basename(p)` (filename), `path.dirname(p)` (directory), `path.extname(p)` (extension), `path.join(...segments)` (combines segments with proper separators), `path.resolve(...segments)` (produces absolute paths), and `path.normalize(p)` (cleans up `../` and `//`). Use `path.posix` or `path.win32` for platform-specific behavior (Flanagan, Ch. 16, pp. 620-621).

# Prerequisites

- **node-programming-model** — Path is a Node core module.

# Key Properties

1. `path.sep` is "/" on Unix, "\\" on Windows.
2. `join()` combines segments with the platform separator and normalizes.
3. `resolve()` returns an absolute path, working backward from the last argument.
4. `normalize()` is string manipulation only; does not access the filesystem.
5. `__filename` and `__dirname` provide the current file's absolute path and directory.

# Construction / Recognition

```javascript
const path = require("path");
path.join("src", "pkg", "t.js")    // => "src/pkg/t.js"
path.resolve("/tmp", "t.js")       // => "/tmp/t.js"
path.basename("src/pkg/test.js")   // => "test.js"
```

# Context & Application

Used whenever file paths need to be constructed, parsed, or normalized, especially in cross-platform code.

# Examples

From the source (p. 620-621): Parsing a path to get basename, extname, dirname; normalizing paths with `../` segments; resolving relative paths to absolute.

# Relationships

## Builds Upon
- **node-programming-model** — Part of Node's core library

## Enables
- Cross-platform file path handling

## Related
- **fs-module** — Path module complements filesystem operations

## Contrasts With
- (None)

# Common Errors

- **Error**: Concatenating paths with string concatenation instead of `path.join()`.
  **Correction**: Use `path.join()` to handle platform-specific separators and normalization.

# Common Confusions

- **Confusion**: `path.normalize()` checks if the path exists.
  **Clarification**: `normalize()` is purely string manipulation. Use `fs.realpath()` for filesystem-aware resolution.

# Source Reference

Chapter 16: Server-Side JavaScript with Node, Section 16.7.1, pages 620-621.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Clear examples for all key functions
- Uncertainties: None
- Cross-reference status: Verified
