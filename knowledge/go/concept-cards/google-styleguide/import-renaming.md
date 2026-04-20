---
# === CORE IDENTIFICATION ===
concept: Import Renaming
slug: import-renaming

# === CLASSIFICATION ===
category: imports
subcategory: naming
tier: intermediate

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Style Decisions"
chapter_number: 3
pdf_page: null
section: "Import renaming"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "import aliasing"
  - "package import renaming"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - package-names
extends: []
related:
  - import-grouping-google
  - import-blank
  - import-dot
contrasts_with:
  - import-aliasing

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When should I rename an imported Go package?"
  - "How should renamed proto imports be suffixed?"
  - "What should I do when an import name collides with a local variable?"
---

# Quick Definition

Rename imports only for name collisions, uninformative package names, or generated proto packages. Proto renames must have a `pb` suffix. Use `pkg` suffix (e.g., `urlpkg`) when a package name collides with a common local variable name.

# Core Definition

Package imports should not normally be renamed, but renaming is appropriate in three situations: (1) when there is a name collision with another import, in which case the most local or project-specific import should be renamed; (2) when a generated protocol buffer package has underscores in its name, in which case it must be renamed with a `pb` suffix (e.g., `foosvcpb`); and (3) when a non-generated package has an uninformative name like `util` or `v1`, though this should be done sparingly. Renamed imports must follow standard package naming rules (no underscores, no capitals). When a package name collides with a common local variable name (e.g., `url`, `ssh`), the preferred rename uses a `pkg` suffix (e.g., `urlpkg`). Consistency is important: the same local name should be used for the same package across files in nearby packages (Google Go Style Guide, "Style Decisions", "Import renaming").

# Prerequisites

- **package-names** -- Understanding what makes a good package name helps determine when renaming is needed

# Key Properties

1. Do not rename imports unnecessarily
2. Must rename for name collisions -- prefer renaming the most local/project-specific import
3. Must rename proto packages to remove underscores and add `pb` suffix
4. Can rename uninformative names (`util`, `v1`) sparingly
5. Renamed names must follow package naming rules (lowercase, no underscores)
6. Use `pkg` suffix for collisions with common local variables: `urlpkg`
7. Be consistent across files and nearby packages

# Construction / Recognition

## To Apply:
1. Check if two imports would have the same name -- rename the more local one
2. For proto imports with underscores, rename with `pb` suffix: `foosvcpb`
3. For uninformative names, rename only if surrounding context does not clarify
4. For collisions with local variable names, add `pkg` suffix
5. Use the same rename consistently across the project

## To Recognize:
1. Look for renamed imports where no collision exists -- the rename may be unnecessary
2. Look for proto imports without `pb` suffix -- they need it
3. Look for inconsistent renames of the same package across files

# Context & Application

Import renaming adds a layer of indirection that can confuse readers who are used to the standard package name. The guidance to rename sparingly preserves the predictability of Go code -- when you see `http.Get()`, you immediately know it refers to `net/http`. The `pb` suffix convention for proto packages is specific to Google's codebase but widely adopted, making proto usage immediately recognizable.

# Examples

**Example 1 -- Good: proto package renaming with pb suffix** (Decisions, "Import renaming"):

```go
// Good:
import (
    foosvcpb "path/to/package/foo_service_go_proto"
)
```

**Example 2 -- Good: renaming uninformative versioned packages** (Decisions, "Import renaming"):

```go
// Good:
import (
    core "github.com/kubernetes/api/core/v1"
    meta "github.com/kubernetes/apimachinery/pkg/apis/meta/v1beta1"
)
```

**Example 3 -- Good: using pkg suffix for local variable collision** (Decisions, "Import renaming"):

```go
// Good:
import (
    urlpkg "net/url"
)

func process(url string) {
    u, err := urlpkg.Parse(url)
    // ...
}
```

# Relationships

## Related
- **import-grouping-google** -- Renamed imports appear within their appropriate group
- **import-blank** -- Side-effect imports are a different import form
- **import-dot** -- Dot imports are prohibited; renaming is the acceptable alternative
- **package-names** -- Good package names reduce the need for renaming

## Contrasts With
- **import-aliasing** (Uber style) -- Uber style focuses on path-vs-name mismatch; Google style also covers proto and uninformative names

# Common Errors

- **Error**: Renaming a proto import without the `pb` suffix
  **Correction**: Always use a `pb` suffix for proto package renames: `foopb`, `foosvcpb`

- **Error**: Renaming standard library packages for brevity (e.g., `fp "path/filepath"`)
  **Correction**: Do not rename standard library packages unless there is an actual collision

# Common Confusions

- **Confusion**: Thinking you must rename when a package name matches a local variable name
  **Clarification**: Renaming is only necessary if the package is still used when the variable is in scope; otherwise, shadowing is acceptable

- **Confusion**: Believing all versioned imports need renaming
  **Clarification**: Only rename `v1`, `v2` etc. when the surrounding code does not provide enough context about which package is being used

# Source Reference

Chapter 3: Style Decisions, Section "Import renaming".

# Verification Notes

- Definition source: Directly from the "Import renaming" section of Google Go Style Decisions
- Confidence rationale: HIGH -- explicit rules with examples for each case
- Uncertainties: None
- Cross-reference status: Related slugs verified against planned extractions
