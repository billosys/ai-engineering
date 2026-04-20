---
# === CORE IDENTIFICATION ===
concept: Doc Comments
slug: doc-comments

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
section: "Doc comments"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "documentation comments"
  - "Godoc comments"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - comment-sentences
  - package-comments
  - examples-in-documentation
  - named-result-parameters
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Which Go declarations need doc comments?"
  - "How should a doc comment begin?"
  - "Do unexported declarations need doc comments?"
---

# Quick Definition

All top-level exported names must have doc comments. Comments should be full sentences that begin with the name of the object being described. An article ("a", "an", "the") can precede the name.

# Core Definition

All top-level exported names must have doc comments, as should unexported type or function declarations with unobvious behavior or meaning. These comments should be full sentences that begin with the name of the object being described. An article ("a", "an", "the") can precede the name to make it read more naturally. Doc comments appear in Godoc and are surfaced by IDEs, so they should be written for anyone using the package. A documentation comment applies to the following symbol, or to a group of fields if it appears in a struct. The same conventions should be followed for unexported code comments to make future export easy (Google Go Style Guide, "Style Decisions", "Doc comments").

# Prerequisites

- **Go exported identifiers** -- Understanding which identifiers are exported and require doc comments
- **Godoc** -- Awareness that doc comments are rendered in Go's documentation tool

# Key Properties

1. All top-level exported names must have doc comments
2. Unexported types/functions with unobvious behavior should also have doc comments
3. Comments must be full sentences
4. Comments must begin with the name of the object being described
5. An article (a, an, the) may precede the name
6. Doc comments appear in Godoc and IDEs
7. Struct field groups can share a single documentation comment

# Construction / Recognition

## To Apply:
1. Write a comment directly above the exported declaration
2. Start the comment with the name of the object: "// Encode writes..."
3. Use full sentences with proper capitalization and punctuation
4. For unexported code, follow the same convention for ease of future export
5. In structs, use comments to group related fields

## To Recognize:
1. Look for exported names without doc comments -- they need one
2. Look for doc comments that do not start with the object name
3. Look for doc comments that are not full sentences

# Context & Application

Doc comments are the primary mechanism for Go API documentation. Godoc extracts these comments and presents them as package documentation. Because they serve as the public interface documentation, they must be clear, complete, and follow the convention of starting with the object name. This convention enables tools to generate consistent documentation and allows grep-like searching for documentation about specific identifiers.

# Examples

**Example 1 -- Good: standard doc comments** (Decisions, "Doc comments"):

```go
// Good:
// A Request represents a request to run a command.
type Request struct { ...

// Encode writes the JSON encoding of req to w.
func Encode(w io.Writer, req *Request) { ...
```

**Example 2 -- Good: struct with grouped field documentation** (Decisions, "Doc comments"):

```go
// Good:
// Options configure the group management service.
type Options struct {
    // General setup:
    Name  string
    Group *FooGroup

    // Dependencies:
    DB *sql.DB

    // Customization:
    LargeGroupThreshold int // optional; default: 10
    MinimumMembers      int // optional; default: 2
}
```

# Relationships

## Related
- **comment-sentences** -- Rules for when full sentences vs fragments are appropriate
- **package-comments** -- Package-level doc comments follow similar conventions
- **examples-in-documentation** -- Runnable examples supplement doc comments
- **named-result-parameters** -- Named results improve Godoc output for doc comments

# Common Errors

- **Error**: Writing a doc comment that does not start with the object name
  **Correction**: Always start with the name: "// Request represents..." not "// This struct represents..."

- **Error**: Omitting doc comments on exported names
  **Correction**: Every exported top-level name must have a doc comment

# Common Confusions

- **Confusion**: Thinking unexported names never need doc comments
  **Clarification**: Unexported types and functions with unobvious behavior should have doc comments too

- **Confusion**: Believing doc comments are only for types and functions
  **Clarification**: All exported names need doc comments, including constants, variables, and interface methods

# Source Reference

Chapter 3: Style Decisions, Section "Doc comments".

# Verification Notes

- Definition source: Directly from the "Doc comments" section of Google Go Style Decisions
- Confidence rationale: HIGH -- explicit rules with code examples
- Uncertainties: None
- Cross-reference status: Related slugs verified against planned extractions
