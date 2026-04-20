---
# === CORE IDENTIFICATION ===
concept: Import Grouping (Google)
slug: import-grouping-google

# === CLASSIFICATION ===
category: imports
subcategory: organization
tier: foundational

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Style Decisions"
chapter_number: 3
pdf_page: null
section: "Import grouping"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "import ordering"
  - "import organization"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - import-renaming
  - import-blank
  - import-dot
contrasts_with:
  - import-group-ordering

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How should imports be grouped in Google Go code?"
  - "Where do proto imports go in the import block?"
  - "Where should side-effect imports be placed?"
---

# Quick Definition

Organize imports into four groups separated by blank lines: (1) standard library, (2) other packages (project and vendored), (3) protocol buffer imports, (4) side-effect imports.

# Core Definition

Imports in Google Go code should be organized into four groups, separated by blank lines, in the following order: (1) Standard library packages, (2) Other packages including project and vendored packages, (3) Protocol Buffer imports (e.g., `fpb "path/to/foo_go_proto"`), and (4) Side-effect imports using the blank identifier (e.g., `_ "path/to/package"`). This grouping provides visual separation that makes it easy to identify the origin and purpose of each import at a glance (Google Go Style Guide, "Style Decisions", "Import grouping").

# Prerequisites

- **Go import syntax** -- Understanding the basic import declaration syntax in Go
- **Go standard library** -- Being able to identify standard library packages vs third-party

# Key Properties

1. Four distinct groups separated by blank lines
2. Group 1: Standard library packages
3. Group 2: Other packages (project, vendored, third-party)
4. Group 3: Protocol buffer imports (with `pb` suffix)
5. Group 4: Side-effect imports (with `_` blank identifier)
6. Order within groups follows `goimports` alphabetical sorting

# Construction / Recognition

## To Apply:
1. Place all standard library imports in the first group
2. Place all non-stdlib, non-proto, non-side-effect imports in the second group
3. Place all proto imports in the third group
4. Place all side-effect imports in the fourth group
5. Separate each group with a blank line
6. Let `goimports` sort within each group

## To Recognize:
1. Look for proto imports mixed with regular imports -- they should be separated
2. Look for side-effect imports mixed with regular imports -- they should be last
3. Look for missing blank lines between groups

# Context & Application

This four-group structure is more granular than the common two-group (stdlib + everything else) convention used in many Go projects. The separation of proto imports acknowledges their prevalence in Google's codebase and makes it easy to identify generated code dependencies. Isolating side-effect imports makes their presence visible and deliberate, since side effects can have surprising consequences.

# Examples

**Example 1 -- Good: four-group import structure** (Decisions, "Import grouping"):

```go
// Good:
package main

import (
    "fmt"
    "hash/adler32"
    "os"

    "github.com/dsnet/compress/flate"
    "golang.org/x/text/encoding"
    "google.golang.org/protobuf/proto"

    foopb "myproj/foo/proto/proto"

    _ "myproj/rpc/protocols/dial"
    _ "myproj/security/auth/authhooks"
)
```

# Relationships

## Related
- **import-renaming** -- Renamed imports (especially proto with `pb` suffix) appear in their appropriate group
- **import-blank** -- Side-effect imports form the fourth group
- **import-dot** -- Dot imports are prohibited and therefore do not appear in any group

## Contrasts With
- **import-group-ordering** (Uber style) -- Uber uses a two-group structure (stdlib + everything else); Google uses four groups

# Common Errors

- **Error**: Mixing proto imports with regular third-party imports
  **Correction**: Separate proto imports into their own group (group 3)

- **Error**: Placing side-effect imports among regular imports
  **Correction**: Side-effect imports must be in the last group

# Common Confusions

- **Confusion**: Thinking `google.golang.org/protobuf/proto` is a proto import
  **Clarification**: The `proto` runtime library is a regular package (group 2); only generated proto packages (with `_go_proto` suffix) belong in group 3

- **Confusion**: Believing this grouping is enforced by `goimports`
  **Clarification**: `goimports` handles stdlib vs non-stdlib; the four-group convention requires manual maintenance or custom tooling

# Source Reference

Chapter 3: Style Decisions, Section "Import grouping".

# Verification Notes

- Definition source: Directly from the "Import grouping" section of Google Go Style Decisions
- Confidence rationale: HIGH -- explicit ordering with a complete code example
- Uncertainties: None
- Cross-reference status: Related slugs verified against planned extractions
