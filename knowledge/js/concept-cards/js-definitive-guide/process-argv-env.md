---
concept: process.argv and process.env
slug: process-argv-env
category: node-apis
subcategory: fundamentals
tier: foundational
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Server-Side JavaScript with Node"
chapter_number: 16
pdf_page: 596
section: "16.1.2 Command-Line Arguments and Environment Variables"
extraction_confidence: high
aliases:
  - command-line arguments
  - environment variables
prerequisites:
  - node-programming-model
extends: []
related: []
contrasts_with: []
answers_questions:
  - "How do I create an HTTP server in Node.js?"
---

# Quick Definition

`process.argv` is an array of command-line argument strings (with the Node executable path as element 0 and the script path as element 1), and `process.env` is an object whose properties are the environment variable names and string values.

# Core Definition

`process.argv` provides command-line arguments as an array of strings. The first element is the path to the Node executable, the second is the path to the JavaScript file being executed, and remaining elements are user-provided arguments. `process.env` makes environment variables available as an object with string property values (Flanagan, Ch. 16, pp. 596-597).

# Prerequisites

- **node-programming-model** — Must understand the Node runtime.

# Key Properties

1. `process.argv[0]`: fully qualified path to the node executable.
2. `process.argv[1]`: fully qualified path to the script file.
3. `process.argv[2+]`: user-provided arguments.
4. Node's own flags (like `--trace-uncaught`) are consumed and don't appear in `process.argv`.
5. `process.env` values are always strings.

# Construction / Recognition

```javascript
console.log(process.argv); // ['/usr/local/bin/node', '/tmp/script.js', '--arg1']
console.log(process.env.HOME); // '/Users/david'
```

# Context & Application

Used in CLI tools and scripts to accept user input and configuration from the command line and environment.

# Examples

From the source (p. 596): Running `node argv.js --arg1 --arg2 filename` produces `process.argv` containing the full paths and the user arguments.

# Relationships

## Builds Upon
- **node-programming-model** — Part of Node's runtime environment

## Enables
- CLI tool development

## Related
- (None)

## Contrasts With
- (None)

# Common Errors

- **Error**: Accessing `process.argv[0]` expecting the first user argument.
  **Correction**: User arguments start at `process.argv[2]`.

# Common Confusions

- **Confusion**: `process.env` values can be numbers or booleans.
  **Clarification**: All `process.env` values are strings. Parse them explicitly if needed.

# Source Reference

Chapter 16: Server-Side JavaScript with Node, Section 16.1.2, pages 596-597.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Clear example output
- Uncertainties: None
- Cross-reference status: Verified
