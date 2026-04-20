---
# === CORE IDENTIFICATION ===
concept: Package Comments
slug: package-comments

# === CLASSIFICATION ===
category: commentary
subcategory: documentation
tier: foundational

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Style Decisions"
chapter_number: 3
pdf_page: null
section: "Package comments"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "package doc comment"
  - "package-level documentation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - doc-comments
extends: []
related:
  - comment-sentences
  - package-names
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How should Go packages be documented?"
  - "Can I have a blank line between the package comment and the package clause?"
  - "How should main package comments differ from library package comments?"
---

# Quick Definition

Every package must have a package doc comment immediately above the `package` clause with no blank line between them. Exactly one file per package should contain the comment. For `main` packages, describe the command's behavior using the binary name.

# Core Definition

Package comments must appear immediately above the package clause with no blank line between the comment and the package name. There must be exactly one package comment per package; if a package comprises multiple files, exactly one file should contain the package comment. Comments for `main` packages have a slightly different form: the name of the binary (from the BUILD file) takes the place of the package name, and the comment describes the command's behavior. Acceptable forms for main packages include "The seed_generator command...", "Binary seed_generator...", "Command seed_generator...", or "Program seed_generator...". For long package documentation, a `doc.go` file containing only the comment and the package clause is acceptable (Google Go Style Guide, "Style Decisions", "Package comments").

# Prerequisites

- **doc-comments** -- Package comments follow the doc comment convention of starting with the entity name
- **Go package structure** -- Understanding that a package can span multiple files

# Key Properties

1. Must appear immediately above `package` clause -- no blank line between
2. Exactly one package comment per package (one file only)
3. Library packages: start with "Package <name> ..."
4. Main packages: use binary name, describe command behavior
5. For long docs, use a dedicated `doc.go` file
6. Multiline `/* */` comments acceptable, especially for copyable command examples
7. Maintainer comments (after imports) are not subject to package comment rules

# Construction / Recognition

## To Apply:
1. Write a comment starting with "Package <name>" for library packages
2. For `main` packages, start with the binary name and describe the command
3. Place the comment directly above the `package` clause, no blank line
4. Ensure only one file in the package has the package comment
5. For long documentation, create a `doc.go` file

## To Recognize:
1. Look for packages without a package comment -- they need one
2. Look for blank lines between the comment and `package` clause -- remove them
3. Look for multiple files with package comments -- consolidate to one

# Context & Application

Package comments are the first thing a developer sees when browsing documentation. They set the tone for the entire package and help users quickly determine if the package is relevant to their needs. The no-blank-line rule ensures Godoc correctly associates the comment with the package declaration. For commands, using the binary name helps users find documentation for the tool they are using.

# Examples

**Example 1 -- Good: library package comment** (Decisions, "Package comments"):

```go
// Good:
// Package math provides basic constants and mathematical functions.
//
// This package does not guarantee bit-identical results across architectures.
package math
```

**Example 2 -- Good: main package comment** (Decisions, "Package comments"):

```go
// Good:
// The seed_generator command is a utility that generates a Finch seed file
// from a set of JSON study configs.
package main
```

**Example 3 -- Good: multiline comment with command example** (Decisions, "Package comments"):

```go
// Good:
/*
The seed_generator command is a utility that generates a Finch seed file
from a set of JSON study configs.

    seed_generator *.json | base64 > finch-seed.base64
*/
package template
```

**Example 4 -- Acceptable forms for main package comments** (Decisions, "Package comments"):

```go
// Binary seed_generator ...
// Command seed_generator ...
// Program seed_generator ...
// The seed_generator command ...
// The seed_generator program ...
// Seed_generator ...
```

# Relationships

## Related
- **comment-sentences** -- Package comments must be full sentences
- **package-names** -- The package name appears in the package comment
- **doc-comments** -- Package comments follow the same "start with name" convention

# Common Errors

- **Error**: Leaving a blank line between the package comment and the `package` clause
  **Correction**: Remove the blank line; the comment must be immediately above `package`

- **Error**: Having package comments in multiple files
  **Correction**: Consolidate to exactly one file (use `doc.go` for long comments)

# Common Confusions

- **Confusion**: Thinking maintainer comments above imports are package comments
  **Clarification**: Comments placed after the import block are not package comments and are not subject to these rules

- **Confusion**: Believing the binary name in main package comments must match the command-line invocation exactly
  **Clarification**: Capitalizing the binary name is required when it is the first word, even if the actual binary is lowercase

# Source Reference

Chapter 3: Style Decisions, Section "Package comments".

# Verification Notes

- Definition source: Directly from the "Package comments" section of Google Go Style Decisions
- Confidence rationale: HIGH -- explicit rules with multiple examples and acceptable forms
- Uncertainties: None
- Cross-reference status: Related slugs verified against planned extractions
