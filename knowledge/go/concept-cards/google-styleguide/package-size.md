---
# === CORE IDENTIFICATION ===
concept: Package Size
slug: package-size

# === CLASSIFICATION ===
category: api-design
subcategory: package-organization
tier: intermediate

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Best Practices"
chapter_number: 4
pdf_page: null
section: "Package size"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "package organization"
  - "when to split packages"
  - "package cohesion"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - package-names
extends: []
related:
  - util-packages
  - test-double-packages
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How big should a Go package be?"
  - "When should I split a Go package into multiple packages?"
  - "Is there a 'one type, one file' convention in Go?"
---

# Quick Definition

Package size should be guided by cohesion rather than arbitrary limits. Related types with tightly coupled implementations belong together. Avoid both overly large monolithic packages and overly small single-type packages. Files within a package should be focused but not tiny.

# Core Definition

Go package sizing considers several factors: godoc groups all exported symbols in a single page, so related types that clients use together benefit from being in the same package. Types with tightly coupled implementations can share unexported identifiers within a package without polluting the public API. If a hypothetical user must import two packages to use either meaningfully, they should probably be combined. However, conceptually distinct functionality should get its own package, where the short package name and exported type name form a meaningful identifier (e.g., `bytes.Buffer`, `ring.New`). Go has no "one type, one file" convention. Files should be focused enough to locate things easily and small enough to navigate, but there is no rule against large files or against multiple types per file. The standard library splits large packages across multiple files grouped by related functionality.

# Prerequisites

- **package-names** -- Understanding that package names are part of the API

# Key Properties

1. Group types that clients typically use together in the same package
2. Group types with tightly coupled implementations to share unexported identifiers
3. If users must import both packages to use either, combine them
4. Conceptually distinct functionality warrants its own package
5. No "one type, one file" convention in Go
6. Files should be focused and navigable but can be large
7. Standard library exemplifies good file organization within packages

# Construction / Recognition

## To Apply:
1. Ask: do clients need both types together? If yes, keep in one package
2. Ask: do the implementations share internal details? If yes, keep together
3. Ask: is this concept distinct enough to stand alone? If yes, separate it
4. Split files by related functionality, not by type

## To Recognize:
1. Package where `package-name.TypeName` forms meaningful identifiers
2. Files grouped by functionality (e.g., `client.go`, `server.go`, `cookie.go` in `net/http`)
3. No artificially tiny packages with a single type

# Context & Application

The Go blog post on package names is a key reference. Standard library examples illustrate the range: small cohesive packages like `csv` (reader.go + writer.go), medium packages like `flag` (single file), and large packages like `net/http` (split across client.go, server.go, cookie.go) and `os` (split across exec.go, file.go, tempfile.go). In Bazel-based projects, multiple `go_library` targets can exist in one directory. For open-source projects, each package typically gets its own directory.

# Examples

**Example 1 -- Small cohesive package**:

`package csv` -- CSV encoding and decoding split between `reader.go` and `writer.go`.

**Example 2 -- Medium package in a single file**:

`package flag` -- command line flag management all in `flag.go`.

**Example 3 -- Large package split across files**:

`package http` -- `client.go` for HTTP clients, `server.go` for servers, `cookie.go` for cookie management.

**Example 4 -- Meaningful package.Type identifiers**:

```go
bytes.Buffer
ring.New
```

# Relationships

## Related
- **util-packages** -- Avoiding generic package names relates to proper package sizing
- **test-double-packages** -- Test double packages as an example of cohesive small packages

## Contrasts With
(none)

# Common Errors

- **Error**: Creating a single-type package for every struct
  **Correction**: Group related types together; Go does not have a one-type-one-file convention

- **Error**: Putting everything in one massive package
  **Correction**: Separate conceptually distinct functionality into its own package

# Common Confusions

- **Confusion**: Thinking smaller packages are always better
  **Clarification**: Cohesion matters more than size; if users must import both to use either, combine them

- **Confusion**: Believing one file per type is idiomatic Go
  **Clarification**: Go has no such convention; group related code by functionality within files

# Source Reference

Chapter 4: Best Practices, Section "Package size".

# Verification Notes

- Definition source: Directly from the "Package size" section of Best Practices
- Confidence rationale: HIGH -- detailed guidance with standard library examples
- Uncertainties: None
- Cross-reference status: References Go blog post on package names, standard library examples
