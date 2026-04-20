---
concept: writeFile
slug: fs-writefile
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
  - fs.writeFile
prerequisites:
  - file-system-module
extends:
  - file-system-module
related:
  - fs-readfile
  - stream
contrasts_with: []
answers_questions:
  - "How do I write a file in Node.js?"
  - "How do I read and write files in Node.js?"
---

# Quick Definition
`writeFile` writes data to a file asynchronously, creating the file if it doesn't exist or overwriting it if it does, with automatic UTF-8 encoding for string content.

# Core Definition
"A similar function, `writeFile`, is used to write a file to disk" (Ch. 20). "Here it was not necessary to specify the encoding -- `writeFile` will assume that when it is given a string to write, rather than a `Buffer` object, it should write it out as text using its default character encoding, which is UTF-8."

# Prerequisites
- **File system module**: writeFile is from node:fs

# Key Properties
1. `writeFile(path, content, callback)` -- callback style
2. Automatically uses UTF-8 for strings
3. Creates the file if it doesn't exist
4. Overwrites existing content

# Construction / Recognition
```javascript
import {writeFile} from "node:fs";
writeFile("graffiti.txt", "Node was here", err => {
  if (err) console.log(`Failed to write file: ${err}`);
  else console.log("File written.");
});
```

# Context & Application
Used for saving data, generating output files, writing logs, and persisting application state.

# Examples
From the file server, PUT handler uses createWriteStream for streaming writes instead of writeFile for full-content writes.

# Relationships
## Builds Upon
- file-system-module
## Enables
- File creation, data persistence, log writing
## Related
- fs-readfile, stream
## Contrasts With
- createWriteStream (streaming writes for large content)

# Common Errors
- **Error**: Assuming writeFile appends to the file
  **Correction**: writeFile overwrites; use appendFile to add content

# Common Confusions
- **Confusion**: writeFile creates parent directories
  **Clarification**: It only creates the file; parent directories must exist

# Source Reference
Chapter 20: Node.js, Section "The filesystem module", lines 395-410 of 20-nodejs.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Clearly explained with example
- Cross-reference status: verified
