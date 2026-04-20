---
# === CORE IDENTIFICATION ===
concept: Import Aliasing
slug: import-aliasing

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
section: "Import Aliasing"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "named imports"
  - "import renaming"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - import-group-ordering
  - package-names
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When should I alias an import in Go?"
  - "Should I rename standard library imports?"
  - "How do I handle import name conflicts in Go?"
---

# Quick Definition

Alias imports only when the package name does not match the last element of the import path, or when there is a direct conflict between imports.

# Core Definition

Import aliasing must be used when the package name does not match the last element of the import path (e.g., `client "example.com/client-go"` where the directory is `client-go` but the package name is `client`). In all other scenarios, import aliases should be avoided unless there is a direct conflict between two imports that would otherwise have the same name. Unnecessary aliasing adds cognitive overhead by introducing a non-standard name for a well-known package (Uber Go Style Guide, "Import Aliasing").

# Prerequisites

- **Go import paths** -- Understanding that the last element of an import path is typically the package name
- **import-group-ordering** -- Aliases are applied within the standard two-group import structure

# Key Properties

1. Alias when the package name does not match the last path element
2. Alias when two different packages would have the same name (conflict resolution)
3. Do not alias standard library packages unnecessarily
4. Do not alias packages whose name already matches their last path element
5. Unnecessary aliases obscure the canonical package name

# Construction / Recognition

## To Apply:
1. Check if the package name matches the last element of the import path. If it does, do not alias.
2. If the package name differs from the last path element, alias it (e.g., `client "example.com/client-go"`)
3. If two imports conflict (same package name), alias one or both to disambiguate
4. Never alias for purely stylistic preference

## To Recognize:
1. Look for aliased imports where the alias matches the last path element -- the alias is unnecessary
2. Look for aliased standard library imports -- almost always unnecessary
3. Look for conflicts where aliasing is genuinely needed

# Context & Application

This guideline reduces confusion by keeping package references predictable. When a developer sees `http.Get()`, they expect it refers to `"net/http"`. Aliasing `"net/http"` to something like `nethttp` would break this expectation. However, some third-party packages have import paths that do not match their package names (e.g., versioned paths like `"example.com/trace/v2"` where the package is `trace`), and aliasing is appropriate there.

# Examples

**Example 1 -- Required aliasing** (Style, "Import Aliasing"):

Package name does not match the last element of the import path:

```go
import (
  "net/http"

  client "example.com/client-go"
  trace "example.com/trace/v2"
)
```

**Example 2 -- Bad: unnecessary aliasing** (Style, "Import Aliasing"):

```go
import (
  "fmt"
  "os"
  runtimetrace "runtime/trace"

  nettrace "golang.net/x/trace"
)
```

**Example 3 -- Good: alias only when needed** (Style, "Import Aliasing"):

```go
import (
  "fmt"
  "os"
  "runtime/trace"

  nettrace "golang.net/x/trace"
)
```

# Relationships

## Related
- **import-group-ordering** -- Aliases are applied within the two-group import structure
- **package-names** -- Good package naming reduces the need for aliases

# Common Errors

- **Error**: Aliasing standard library imports for brevity (e.g., `fp "path/filepath"`)
  **Correction**: Use the standard name. The import path `"path/filepath"` already gives you the `filepath` package name.

- **Error**: Aliasing `"runtime/trace"` as `runtimetrace` when there is no conflict
  **Correction**: Only alias if another import also has the package name `trace`

# Common Confusions

- **Confusion**: Thinking all versioned imports (e.g., `v2`) need aliasing
  **Clarification**: If the package name matches the directory before `/v2`, Go handles this automatically. Alias only when the actual package name differs from the path's last element.

- **Confusion**: Believing the dot import (`. "package"`) is an acceptable alternative
  **Clarification**: Dot imports should be avoided as they pollute the namespace and obscure where identifiers come from

# Source Reference

Chapter 4: Style, Section "Import Aliasing".

# Verification Notes

- Definition source: Directly from the "Import Aliasing" section of the Uber Go Style Guide
- Confidence rationale: HIGH -- the source provides explicit rules and bad/good examples
- Uncertainties: None
- Cross-reference status: Related slugs verified against planned extractions
