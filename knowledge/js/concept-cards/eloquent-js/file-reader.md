---
concept: FileReader
slug: file-reader
category: http-forms
subcategory: browser-api
tier: intermediate
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "HTTP and Forms"
chapter_number: 18
pdf_page: null
section: "File fields"
extraction_confidence: high
aliases:
  - file input
  - file API
prerequisites:
  - input-element
  - event-handler
extends: []
related:
  - data-url
  - promise
contrasts_with: []
answers_questions:
  - "How do I read files from the user's computer in JavaScript?"
---

# Quick Definition
`FileReader` is a browser API for asynchronously reading files selected by the user through a file input, providing the content as text, a data URL, or binary data via event-based callbacks.

# Core Definition
"Reading a file is done by creating a `FileReader` object, registering a `'load'` event handler for it, and calling its `readAsText` method, giving it the file we want to read. Once loading finishes, the reader's `result` property contains the file's content" (Ch. 18, "File fields"). File objects from `<input type="file">` have `name`, `size`, and `type` properties.

# Prerequisites
- **Input elements**: File fields provide the File objects
- **Event handlers**: FileReader uses load/error events

# Key Properties
1. `readAsText(file)` -- reads as string
2. `readAsDataURL(file)` -- reads as data: URL
3. `result` property -- contains content after load
4. "load" event -- fires when reading completes
5. "error" event -- fires on failure

# Construction / Recognition
```javascript
let reader = new FileReader();
reader.addEventListener("load", () => {
  console.log("File", file.name, "starts with",
              reader.result.slice(0, 20));
});
reader.readAsText(file);
```

# Context & Application
Used for client-side file processing: reading images for preview, parsing CSV/JSON data, loading configurations, and the pixel art editor's load feature.

# Examples
Wrapping FileReader in a promise:
```javascript
function readFileText(file) {
  return new Promise((resolve, reject) => {
    let reader = new FileReader();
    reader.addEventListener("load", () => resolve(reader.result));
    reader.addEventListener("error", () => reject(reader.error));
    reader.readAsText(file);
  });
}
```

# Relationships
## Builds Upon
- input-element, event-handler
## Enables
- Client-side file processing, image loading, data-url
## Related
- promise, data-url
## Contrasts With
- Server-side file reading (Node.js fs module)

# Common Errors
- **Error**: Trying to read file.content directly
  **Correction**: File objects don't expose content directly; you must use FileReader

# Common Confusions
- **Confusion**: FileReader is synchronous
  **Clarification**: It's asynchronous (event-based), designed before promises; wrap in Promise for modern usage

# Source Reference
Chapter 18: HTTP and Forms, Section "File fields", lines 928-1020 of 18-http-and-forms.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Complete API coverage with promise wrapper
- Cross-reference status: verified (also used in Ch. 19)
