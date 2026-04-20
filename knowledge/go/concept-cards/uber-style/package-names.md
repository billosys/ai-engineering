---
# === CORE IDENTIFICATION ===
concept: Package Names
slug: package-names

# === CLASSIFICATION ===
category: style
subcategory: naming
tier: foundational

# === PROVENANCE ===
source: "Uber Go Style Guide"
source_slug: uber-style
authors: "Prashant Varanasi, Simon Newton"
chapter: "Style"
chapter_number: 4
pdf_page: null
section: "Package Names"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "package naming conventions"
  - "Go package naming"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - function-names
  - import-aliasing
  - import-group-ordering
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How should I name Go packages?"
  - "Why should package names be short and lowercase?"
  - "What package names should I avoid in Go?"
---

# Quick Definition

Package names must be all lowercase, short, singular (not plural), and never generic names like "common", "util", "shared", or "lib".

# Core Definition

When naming Go packages, choose a name that is all lower-case with no capitals or underscores, short and succinct, not plural, and not a generic uninformative name like "common", "util", "shared", or "lib". The package name should not need to be renamed using named imports at most call sites. Remember that the package name is identified in full at every call site, so brevity matters (Uber Go Style Guide, "Package Names").

# Prerequisites

- **Go package system** -- Understanding that package names appear as qualifiers at every usage site (e.g., `http.Get()`)

# Key Properties

1. All lower-case: no capitals or underscores
2. Short and succinct: the name appears at every call site as a qualifier
3. Not plural: use `net/url`, not `net/urls`
4. Not generic: avoid "common", "util", "shared", "lib" -- these are uninformative
5. Should not need renaming via import aliases at most call sites

# Construction / Recognition

## To Apply:
1. Choose a name that describes what the package *provides*, not what it *contains*
2. Keep it short -- one word is ideal
3. Use lowercase only, no underscores or mixed case
4. Use singular form (e.g., `url` not `urls`)
5. Avoid catch-all names like `util`, `common`, `shared`, `lib`, `helpers`

## To Recognize:
1. Look for packages named `util`, `common`, `helpers`, `shared`, `misc` -- these violate the guideline
2. Look for plural package names -- these should typically be singular
3. Look for packages with underscores or uppercase letters in the name

# Context & Application

Package naming matters because Go uses the package name as a qualifier at every call site. A name like `stringutil.Reverse` is clearer than `util.Reverse`. Short, descriptive names reduce verbosity while maintaining clarity. This guideline aligns with the broader Go community conventions documented in the official "Package Names" blog post.

# Examples

**Example 1 -- Good package names**:

```
net/url       -- not net/urls (singular, not plural)
http          -- short and descriptive
bytes         -- describes what the package provides
```

**Example 2 -- Bad package names**:

```
common        -- uninformative
util          -- too generic
shared        -- vague
lib           -- says nothing about purpose
net/urls      -- should be singular: net/url
```

# Relationships

## Related
- **function-names** -- Function naming conventions complement package naming
- **import-aliasing** -- Good package names reduce the need for import aliases
- **import-group-ordering** -- Packages are organized within import groups

# Common Errors

- **Error**: Creating a package named `util` or `helpers` as a dumping ground for miscellaneous functions
  **Correction**: Split utilities into focused packages named after what they provide (e.g., `timeutil`, `httputil`)

- **Error**: Using plural package names like `models`, `handlers`, `controllers`
  **Correction**: Use singular form: `model`, `handler`, `controller`

# Common Confusions

- **Confusion**: Thinking that short names sacrifice clarity
  **Clarification**: Because the package name qualifies every usage (e.g., `http.Get`), short names actually improve readability at call sites

- **Confusion**: Believing underscores are acceptable in package names
  **Clarification**: Package names must be all lowercase with no underscores. Underscores in package names trigger `go vet` warnings.

# Source Reference

Chapter 4: Style, Section "Package Names".

# Verification Notes

- Definition source: Directly from the "Package Names" section of the Uber Go Style Guide
- Confidence rationale: HIGH -- the source provides an explicit bullet-point list of naming requirements
- Uncertainties: None
- Cross-reference status: Related slugs verified against planned extractions
