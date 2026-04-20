---
concept: Path Module
slug: path-module
category: server-side
subcategory: node-modules
tier: intermediate
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Node.js"
chapter_number: 20
pdf_page: null
section: "A file server"
extraction_confidence: high
aliases:
  - node:path
  - path.resolve
prerequisites:
  - nodejs
extends: []
related:
  - file-system-module
contrasts_with: []
answers_questions:
  - "How do I work with file paths safely in Node.js?"
---

# Quick Definition
The `node:path` module provides utilities for working with file paths, including `resolve` for converting relative paths to absolute and `sep` for the platform-specific path separator.

# Core Definition
The file server uses `resolve` from `node:path` to safely map URLs to file paths, and `sep` to check path boundaries: "the `resolve` function from the `node:path` module [...] resolves relative paths. It then verifies that the result is below the working directory" (Ch. 20).

# Prerequisites
- **Node.js**: path is a built-in module

# Key Properties
1. `resolve(path)` -- resolves relative path to absolute
2. `sep` -- platform path separator ("/" or "\\")
3. Cross-platform path handling
4. Prevents path traversal attacks (../../../etc/passwd)

# Construction / Recognition
```javascript
import {resolve, sep} from "node:path";
const baseDirectory = process.cwd();

function urlPath(url) {
  let {pathname} = new URL(url, "http://d");
  let path = resolve(decodeURIComponent(pathname).slice(1));
  if (path != baseDirectory &&
      !path.startsWith(baseDirectory + sep)) {
    throw {status: 403, body: "Forbidden"};
  }
  return path;
}
```

# Context & Application
Essential for any Node application working with file paths, especially servers that map URLs to files. Prevents directory traversal security vulnerabilities.

# Examples
"File paths are strings in Node. To map such a string to an actual file, there's a nontrivial amount of interpretation going on. Paths may, for example, include `../` to refer to a parent directory."

# Relationships
## Builds Upon
- nodejs
## Enables
- Safe file path resolution, cross-platform compatibility
## Related
- file-system-module, process-object
## Contrasts With
- String concatenation for paths (unsafe, not cross-platform)

# Common Errors
- **Error**: Concatenating paths with "/" directly
  **Correction**: Use path.resolve or path.join for cross-platform safety

# Common Confusions
- **Confusion**: resolve() only joins paths
  **Clarification**: It resolves to an absolute path, following ".." and "." segments

# Source Reference
Chapter 20: Node.js, Section "A file server", lines 700-748 of 20-nodejs.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Used in security-sensitive context
- Cross-reference status: verified
