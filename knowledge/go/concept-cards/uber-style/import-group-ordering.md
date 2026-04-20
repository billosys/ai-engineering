---
# === CORE IDENTIFICATION ===
concept: Import Group Ordering
slug: import-group-ordering

# === CLASSIFICATION ===
category: style
subcategory: imports
tier: foundational

# === PROVENANCE ===
source: "Uber Go Style Guide"
source_slug: uber-style
authors: "Prashant Varanasi, Simon Newton"
chapter: "Style"
chapter_number: 4
pdf_page: null
section: "Import Group Ordering"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "import grouping"
  - "goimports ordering"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - import-aliasing
  - package-names
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I organize imports in a Go file?"
  - "How many import groups should a Go file have?"
  - "What is the standard import ordering enforced by goimports?"
---

# Quick Definition

Organize imports into two groups separated by a blank line: standard library packages first, then everything else.

# Core Definition

Go files should have exactly two import groups. The first group contains standard library imports; the second group contains all third-party and internal packages. The two groups are separated by a single blank line. This is the default grouping applied by `goimports`, so running the tool will automatically enforce this convention (Uber Go Style Guide, "Import Group Ordering").

# Prerequisites

- **Go import syntax** -- Understanding Go's `import` declaration and parenthesized import blocks

# Key Properties

1. Exactly two import groups: standard library and everything else
2. Groups are separated by a blank line within the import block
3. This convention matches the default behavior of `goimports`
4. Imports within each group should be sorted alphabetically (handled by `goimports`)

# Construction / Recognition

## To Apply:
1. Place all standard library imports (e.g., `"fmt"`, `"os"`, `"net/http"`) in the first group
2. Insert a blank line after the standard library group
3. Place all third-party and internal imports in the second group
4. Run `goimports` to automatically enforce this layout

## To Recognize:
1. Look for import blocks without a blank line separating standard library from third-party imports -- this is the anti-pattern
2. Look for more than two groups (some teams use three groups, but Uber style uses two)

# Context & Application

This guideline applies to every Go source file. Consistent import ordering makes it easy to scan a file's dependencies at a glance and quickly distinguish between standard library and external dependencies. The convention is intentionally simple -- two groups, not three or more -- which reduces bike-shedding and is automatically enforceable via `goimports`.

# Examples

**Example 1 -- Bad** (Style, "Import Group Ordering"):

Standard library and third-party imports mixed in one group:

```go
import (
  "fmt"
  "os"
  "go.uber.org/atomic"
  "golang.org/x/sync/errgroup"
)
```

**Example 2 -- Good** (Style, "Import Group Ordering"):

Two groups separated by a blank line:

```go
import (
  "fmt"
  "os"

  "go.uber.org/atomic"
  "golang.org/x/sync/errgroup"
)
```

# Relationships

## Related
- **import-aliasing** -- Governs when to alias imports; applied within these groups
- **package-names** -- Good package naming reduces the need for import aliases

# Common Errors

- **Error**: Mixing standard library and third-party imports in a single group without a blank line separator
  **Correction**: Add a blank line between the standard library block and the third-party block

- **Error**: Creating three or more import groups (e.g., separating internal packages from third-party)
  **Correction**: The Uber style uses exactly two groups; everything non-stdlib goes in the second group

# Common Confusions

- **Confusion**: Believing that internal/company packages should form a separate third group
  **Clarification**: The Uber style prescribes exactly two groups. Internal packages belong in the second group alongside third-party packages.

- **Confusion**: Thinking import ordering must be done manually
  **Clarification**: Running `goimports` automatically applies this two-group ordering

# Source Reference

Chapter 4: Style, Section "Import Group Ordering".

# Verification Notes

- Definition source: Directly from the "Import Group Ordering" section of the Uber Go Style Guide
- Confidence rationale: HIGH -- the source explicitly states "There should be two import groups" with a clear bad/good example
- Uncertainties: None
- Cross-reference status: Related slugs verified against planned extractions
