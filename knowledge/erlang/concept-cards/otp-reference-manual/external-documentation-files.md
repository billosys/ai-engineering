---
# === CORE IDENTIFICATION ===
concept: External Documentation Files
slug: external-documentation-files

# === CLASSIFICATION ===
category: documentation
subcategory: module-documentation
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Documentation"
chapter_number: null
pdf_page: null
section: "External documentation files"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "file-based documentation"
  - "external doc files"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - doc-attribute
  - moduledoc-attribute
extends: []
related:
  - documentation-metadata
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I put Erlang documentation in a separate file?"
  - "What is the {file, Path} syntax for documentation?"
  - "Are external documentation file paths relative or absolute?"
---

# Quick Definition
The `-moduledoc` and `-doc` attributes can reference external files using `{file, "path/to/doc.md"}` syntax. The path is relative to the source file containing the attribute.

# Core Definition
The Erlang Reference Manual states: "The `-moduledoc` and `-doc` attributes can also be placed in external files. To do so, use `-doc {file, \"path/to/doc.md\"}` to point to the documentation. The path used is relative to the file where the `-doc` attribute is located." (Documentation, "External documentation files").

# Prerequisites
- **doc-attribute** -- External files are used with `-doc`
- **moduledoc-attribute** -- External files are used with `-moduledoc`

# Key Properties
1. Syntax: `-doc {file, "path/to/doc.md"}.` or `-moduledoc {file, "path/to/doc.md"}.`
2. Path is relative to the source file containing the attribute
3. The external file contains only the documentation text, not the attribute syntax
4. The file format should match the module's documentation format (default: Markdown)
5. Useful for long documentation that would clutter the source file

# Construction / Recognition
## To Use External Documentation:
1. Create a documentation file (e.g., `doc/add.md`)
2. Write the documentation content in the file (no attribute syntax needed)
3. Reference it from the source: `-doc({file, "../doc/add.md"}).`
4. Use relative paths from the source file's location

# Context & Application
External documentation files are useful when module or function documentation is extensive enough to clutter the source code. They are particularly recommended for module-level documentation (`-moduledoc`), where usage examples, diagrams, and detailed API descriptions can be lengthy. The file path is relative to the source file, making the project structure self-contained.

# Examples
**Example 1** (External documentation files):
```markdown
%% doc/add.md
Adds two numbers.
```

```erlang
%% src/arith.erl
-doc({file, "../doc/add.md"}).
add(One, Two) -> One + Two.
```

**Example 2** (External moduledoc with non-Markdown format):
```erlang
-moduledoc {file, "../doc/arith.asciidoc"}.
-moduledoc #{format => "text/asciidoc"}.
```

# Relationships
## Builds Upon
- **doc-attribute** -- External files extend `-doc`
- **moduledoc-attribute** -- External files extend `-moduledoc`

## Enables
Separation of extensive documentation from source code.

## Related
- **documentation-metadata** -- Metadata (like `format`) can be set alongside external file references

## Contrasts With
None.

# Common Errors
- **Error**: Using an absolute path instead of a relative path
  **Correction**: Paths must be relative to the source file containing the attribute.

- **Error**: Including `-doc` or `-moduledoc` syntax in the external file
  **Correction**: The external file should contain only the documentation text, not Erlang attributes.

# Common Confusions
- **Confusion**: Thinking the path is relative to the project root
  **Clarification**: The path is relative to the file where the attribute is located. If the source is in `src/arith.erl` and the doc is in `doc/add.md`, the path is `"../doc/add.md"`.

# Source Reference
"Documentation" chapter, "External documentation files" section.

# Verification Notes
- Definition source: Direct from source text with example
- Confidence rationale: High -- explicit syntax and path semantics described
- Uncertainties: None
- Cross-reference status: All slugs verified
