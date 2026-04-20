---
# === CORE IDENTIFICATION ===
concept: Custom Processors
slug: custom-processors

# === CLASSIFICATION ===
category: extending
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "extend/custom-processors.md"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "ESLint processor"
  - "preprocess"
  - "postprocess"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - eslint
  - creating-plugins
extends:
  - creating-plugins
related:
  - custom-rules
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do processors extract lintable code from non-JavaScript files?"
  - "What is the difference between preprocess and postprocess?"
  - "How do you enable autofix support in a custom processor?"
  - "How do code blocks work in processors?"
---

# Quick Definition
A custom processor tells ESLint how to extract and lint code blocks from non-JavaScript files by implementing `preprocess` (splitting input into lintable blocks) and `postprocess` (aggregating and adjusting lint messages).

# Core Definition
A processor is an object with two methods:

- **preprocess(text, filename)**: Takes file contents and filename, returns an array of code blocks. Each block has `text` (the code content) and `filename` (including file extension, which tells ESLint how to process the block). ESLint checks matching `files` entries in the config to determine if blocks should be linted.

- **postprocess(messages, filename)**: Takes a two-dimensional array of lint messages (one array per code block from preprocess) and the filename. Must adjust error locations to correspond to the original unprocessed file and return a single flat array of messages.

To support autofix, the processor must set `supportsAutofix: true` and the `postprocess` method must transform `fix` properties (with `range` and `text`) to refer to positions in the original file.

Each processor can have its own `meta` object with `name` and `version` for caching and debugging.

# Prerequisites
- Understanding of ESLint plugins (processors are distributed inside plugins)

# Key Properties
1. **preprocess** -- Splits file content into code blocks with text and filename
2. **postprocess** -- Aggregates lint messages and adjusts locations to original file
3. **supportsAutofix** -- Boolean flag (defaults to false) that must be true for autofix support
4. **Code blocks** -- Objects with `text` and `filename` properties; file extension determines linting rules
5. **meta** -- Optional name/version for processor-level identification

# Construction / Recognition
```js
processors: {
    "processor-name": {
        meta: { name: "eslint-processor-name", version: "1.2.3" },
        preprocess(text, filename) {
            return [
                { text: code1, filename: "0.js" },
                { text: code2, filename: "1.js" }
            ];
        },
        postprocess(messages, filename) {
            return [].concat(...messages);
        },
        supportsAutofix: true
    }
}
```

# Context & Application
Processors enable linting code embedded in non-JavaScript files. The canonical example is `@eslint/markdown`, which extracts JavaScript code blocks from Markdown files. For HTML files, a processor might combine all script blocks into one; for Markdown, each code block can be independent. Processors are referenced in config as `"plugin-namespace/processor-name"`.

# Examples
From extend/custom-processors.md:
- "you could write a custom processor to extract and process JavaScript from Markdown files"
- Code blocks for HTML vs. Markdown: "for .html files, you might want to return just one item in the array by combining all scripts. However, for .md files, you can return multiple items because each JavaScript block might be independent."

# Relationships
## Part Of
- creating-plugins

## Related
- custom-rules

# Common Errors
1. Forgetting to adjust fix locations in postprocess -- autofixes will target wrong positions in the original file
2. Not setting `supportsAutofix: true` -- ESLint will not apply fixes even with `--fix`
3. Returning messages with unadjusted line/column numbers -- errors will point to wrong locations

# Source Reference
- extend/custom-processors.md: Full processor interface, LintMessage type, autofix support

# Verification Notes
- High confidence: directly extracted from the official custom processors documentation
