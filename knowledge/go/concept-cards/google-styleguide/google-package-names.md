---
# === CORE IDENTIFICATION ===
concept: Google Package Names
slug: google-package-names

# === CLASSIFICATION ===
category: naming
subcategory: packages
tier: foundational

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Decisions"
chapter_number: 3
pdf_page: null
section: "Naming"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Go package naming conventions"
  - "package name rules"
  - "avoid util packages"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - mixedcaps-naming
extends: []
related:
  - underscores-in-go-names
  - naming-principles
  - receiver-names
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How should Go packages be named?"
  - "Can Go package names contain underscores or uppercase letters?"
  - "Why should I avoid naming a package util or common?"
  - "How should renamed imports be handled?"
---

# Quick Definition

Go package names must be lowercase only (with numbers allowed), no underscores, and never uninformative names like `util`, `common`, `helper`, `model`, or `testhelper`. Multi-word package names should remain unbroken and all lowercase. Renamed imports must also comply with these rules.

# Core Definition

Go package names must be concise and use only lowercase letters and numbers (e.g., `k8s`, `oauth2`). Multi-word package names should remain unbroken and in all lowercase (e.g., `tabwriter` not `tabWriter`, `TabWriter`, or `tab_writer`). Package names should not have underscores, with an exception for packages only imported by generated code. Avoid names likely to be shadowed by common local variable names (e.g., prefer `usercount` over `count`). Avoid uninformative names like `util`, `utility`, `common`, `helper`, `model`, `testhelper` -- these tempt users to rename them at import time. When a package is renamed at import (e.g., `import foopb "path/to/foo_go_proto"`), the local name must comply with these same rules, and the same local name should be used consistently across files.

# Prerequisites

- **mixedcaps-naming** -- Understanding that Go uses MixedCaps for identifiers but package names are a special case (all lowercase)

# Key Properties

1. Lowercase letters and numbers only (e.g., `k8s`, `oauth2`)
2. No underscores (except packages imported only by generated code)
3. Multi-word names unbroken and all lowercase (`tabwriter` not `tab_writer`)
4. Avoid names that shadow common local variables (prefer `usercount` over `count`)
5. Avoid uninformative names: `util`, `utility`, `common`, `helper`, `model`, `testhelper`
6. Renamed imports must follow the same rules
7. Consistent local names across files when renaming imports

# Construction / Recognition

## To Apply:
1. Choose a name that describes what the package provides
2. Use only lowercase letters and numbers, no underscores
3. Keep multi-word names as a single lowercase word
4. Verify the name is not a common local variable name
5. Avoid generic names; prefer specific, descriptive names
6. When renaming imports, use a name that follows package naming rules

## To Recognize:
1. Package names with underscores (e.g., `string_util`) -- violation
2. Package names with uppercase letters (e.g., `StringUtil`) -- violation
3. Generic package names (`util`, `common`, `helper`, `misc`) -- violation
4. Inconsistent import aliases for the same package across files

# Context & Application

Package names appear at every call site as a qualifier (`http.Get`, `json.Marshal`), so they must be short and informative. Uninformative names like `util` fail because `util.Sort` tells the reader nothing about the package's purpose, and different call sites end up renaming it to something more descriptive anyway. The shadowing guidance (prefer `usercount` over `count`) prevents confusion when a local variable would hide the package name.

# Examples

**Example 1 -- Good and bad package names (from source)**:

```go
// Good:
package tabwriter   // not tab_writer or TabWriter
package oauth2      // lowercase with numbers
package k8s         // abbreviation, lowercase

// Bad:
package tab_writer  // underscores not allowed
package TabWriter   // uppercase not allowed
package util        // uninformative
package common      // uninformative
package helper      // uninformative
```

**Example 2 -- Avoiding shadowed names (from source)**:

```go
// Good: unlikely to be shadowed
package usercount

// Bad: easily shadowed by local variable
package count
```

**Example 3 -- Black box test packages (from source)**:

```go
// Good:
package linkedlist_test    // _test suffix for black box tests

// Bad:
package linked_list_test   // underscore in the name portion
```

# Relationships

## Related
- **underscores-in-go-names** -- Details the underscore exception for generated code packages
- **naming-principles** -- General naming philosophy applies to packages
- **receiver-names** -- Another category-specific naming convention

# Common Errors

- **Error**: Creating a `util` or `helpers` package as a dumping ground
  **Correction**: Split into focused packages named after what they provide (e.g., `httputil`, `timeformat`)

- **Error**: Using underscores in multi-word package names
  **Correction**: Concatenate words in lowercase: `tabwriter` not `tab_writer`

- **Error**: Using different import aliases for the same package in different files
  **Correction**: Choose one local name and use it consistently across all files

# Common Confusions

- **Confusion**: Thinking package names follow the same MixedCaps convention as other identifiers
  **Clarification**: Package names are a special case: all lowercase, no underscores, no mixed case

- **Confusion**: Believing short package names sacrifice clarity
  **Clarification**: Since the package name qualifies every usage (`http.Get`), short names enhance readability at call sites

# Source Reference

Chapter 3: Decisions, Section "Naming" > "Package names".

# Verification Notes

- Definition source: Directly from the "Package names" section of Style Decisions
- Confidence rationale: HIGH -- detailed guidance with explicit examples and rules
- Uncertainties: None
- Cross-reference status: Related slugs verified against planned extractions
