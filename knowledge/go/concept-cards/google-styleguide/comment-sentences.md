---
# === CORE IDENTIFICATION ===
concept: Comment Sentences
slug: comment-sentences

# === CLASSIFICATION ===
category: commentary
subcategory: formatting
tier: foundational

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Style Decisions"
chapter_number: 3
pdf_page: null
section: "Comment sentences"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "comment punctuation"
  - "comment capitalization"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - doc-comments
extends: []
related:
  - package-comments
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Should Go comments be full sentences?"
  - "When can Go comments be sentence fragments?"
  - "How should end-of-line struct field comments be written?"
---

# Quick Definition

Complete-sentence comments should be capitalized and punctuated like standard English. Sentence fragments have no punctuation requirements. Doc comments must always be complete sentences. End-of-line comments (e.g., for struct fields) can be simple phrases assuming the field name is the subject.

# Core Definition

Comments that are complete sentences should be capitalized and punctuated like standard English sentences. As an exception, it is acceptable to begin a sentence with an uncapitalized identifier name if it is otherwise clear, though this is best done only at the start of a paragraph. Comments that are sentence fragments have no requirements for punctuation or capitalization. Documentation comments should always be complete sentences and therefore always capitalized and punctuated. Simple end-of-line comments, especially for struct fields, can be simple phrases that assume the field name is the subject (Google Go Style Guide, "Style Decisions", "Comment sentences").

# Prerequisites

- **doc-comments** -- Understanding which comments are documentation comments (and thus must be full sentences)

# Key Properties

1. Full-sentence comments: capitalize and punctuate
2. Fragment comments: no punctuation/capitalization requirements
3. Doc comments are always full sentences
4. End-of-line struct field comments can be phrases
5. Uncapitalized identifier at start of sentence is acceptable (at paragraph beginning)

# Construction / Recognition

## To Apply:
1. For doc comments (above declarations), write complete sentences with capitalization and punctuation
2. For end-of-line comments on struct fields, use simple phrases (field name is implied subject)
3. For inline/fragment comments, capitalization and punctuation are optional
4. If starting a sentence with an identifier name, you may leave it uncapitalized

## To Recognize:
1. Look for doc comments without proper capitalization/punctuation -- they should be full sentences
2. Look for overly formal end-of-line comments -- they can be simpler phrases

# Context & Application

This guidance strikes a balance between formality and practicality. Doc comments appear in Godoc and serve as official API documentation, so they need to be properly formed sentences. End-of-line comments for struct fields are read in the context of the field declaration, so the field name provides the implicit subject, making full sentences unnecessary and often verbose.

# Examples

**Example 1 -- Good: mixed comment styles in a struct** (Decisions, "Comment sentences"):

```go
// Good:
// A Server handles serving quotes from the collected works of Shakespeare.
type Server struct {
    // BaseDir points to the base directory under which Shakespeare's works are stored.
    //
    // The directory structure is expected to be the following:
    //   {BaseDir}/manifest.json
    //   {BaseDir}/{name}/{name}-part{number}.txt
    BaseDir string

    WelcomeMessage  string // displayed when user logs in
    ProtocolVersion string // checked against incoming requests
    PageLength      int    // lines per page when printing (optional; default: 20)
}
```

# Relationships

## Related
- **doc-comments** -- Doc comments must be full sentences per this rule
- **package-comments** -- Package-level comments follow the same sentence rules

# Common Errors

- **Error**: Writing a doc comment as a fragment: `// the main handler`
  **Correction**: Write a full sentence: `// Handler serves the main HTTP endpoint.`

- **Error**: Writing overly verbose end-of-line struct field comments as full sentences
  **Correction**: Use a simple phrase: `// optional; default: 10`

# Common Confusions

- **Confusion**: Thinking all comments must be full sentences
  **Clarification**: Only doc comments must be full sentences; fragments and end-of-line comments can be phrases

- **Confusion**: Believing you cannot start a sentence with a lowercase identifier
  **Clarification**: It is acceptable, especially at the beginning of a paragraph, when the identifier name is clear

# Source Reference

Chapter 3: Style Decisions, Section "Comment sentences".

# Verification Notes

- Definition source: Directly from the "Comment sentences" section of Google Go Style Decisions
- Confidence rationale: HIGH -- explicit rules with a detailed code example
- Uncertainties: None
- Cross-reference status: Related slugs verified against planned extractions
