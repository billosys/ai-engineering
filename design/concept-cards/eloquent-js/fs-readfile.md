---
concept: readFile
slug: fs-readfile
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
  - readFileSync
  - fs.readFile
prerequisites:
  - file-system-module
extends:
  - file-system-module
related:
  - fs-writefile
  - stream
contrasts_with: []
answers_questions:
  - "How do I read a file in Node.js?"
  - "How do I read and write files in Node.js?"
---

# Quick Definition
`readFile` reads the entire contents of a file asynchronously, returning either a string (when encoding like "utf8" is specified) or a Buffer (binary data), via callback, promise, or synchronous API.

# Core Definition
"The function called `readFile` reads a file and then calls a callback with the file's contents" (Ch. 20). "The second argument to `readFile` indicates the character encoding used to decode the file into a string. [...] If you do not pass an encoding, Node will assume you are interested in the binary data and will give you a `Buffer` object instead of a string."

# Prerequisites
- **File system module**: readFile is from node:fs

# Key Properties
1. Callback: `readFile(path, encoding, callback)`
2. Promise: `readFile(path, encoding)` from node:fs/promises
3. Sync: `readFileSync(path, encoding)`
4. Without encoding, returns Buffer (binary)
5. With "utf8" encoding, returns string

# Construction / Recognition
```javascript
// Callback
import {readFile} from "node:fs";
readFile("file.txt", "utf8", (error, text) => {
  if (error) throw error;
  console.log(text);
});

// Promise
import {readFile} from "node:fs/promises";
let text = await readFile("file.txt", "utf8");

// Synchronous
import {readFileSync} from "node:fs";
let text = readFileSync("file.txt", "utf8");
```

# Context & Application
The most common file operation in Node. Used for reading configuration, data files, templates, and any file-based input.

# Examples
Reading binary data:
```javascript
readFile("file.txt", (error, buffer) => {
  console.log("The file contained", buffer.length, "bytes.",
              "The first byte is:", buffer[0]);
});
```

# Relationships
## Builds Upon
- file-system-module
## Enables
- File-based data loading, configuration reading
## Related
- fs-writefile, stream
## Contrasts With
- Streaming reads (createReadStream for large files)

# Common Errors
- **Error**: Forgetting to handle errors in the callback
  **Correction**: Always check the error parameter first; use try/catch with promises

# Common Confusions
- **Confusion**: readFileSync is safe to use in servers
  **Clarification**: Sync operations block the entire process; avoid in servers handling requests

# Source Reference
Chapter 20: Node.js, Section "The filesystem module", lines 354-450 of 20-nodejs.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: All three variants shown
- Cross-reference status: verified
