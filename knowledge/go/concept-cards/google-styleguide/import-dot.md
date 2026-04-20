---
# === CORE IDENTIFICATION ===
concept: Import Dot
slug: import-dot

# === CLASSIFICATION ===
category: imports
subcategory: restrictions
tier: foundational

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Style Decisions"
chapter_number: 3
pdf_page: null
section: "Import \"dot\" (import .)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "dot import"
  - "import dot"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - import-renaming
  - import-grouping-google
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Can I use import . (dot import) in Google Go code?"
  - "Why are dot imports discouraged in Go?"
  - "What problems do dot imports cause?"
---

# Quick Definition

Do not use `import .` (dot import) in the Google codebase. It brings exported identifiers into the current package without qualification, making it harder to tell where functionality comes from.

# Core Definition

The `import .` form is a Go language feature that allows bringing identifiers exported from another package into the current package without package qualification. This feature must not be used in the Google codebase because it makes it harder to tell where functionality is coming from. When identifiers appear without qualification, readers cannot determine at a glance whether a name refers to a local declaration or an imported one, significantly reducing code readability (Google Go Style Guide, "Style Decisions", "Import dot").

# Prerequisites

- **Go import declarations** -- Understanding the different forms of import declarations in Go

# Key Properties

1. Do not use `import .` in Google Go code
2. Dot imports bring all exported names into the current namespace
3. Makes it unclear where identifiers originate
4. Reduces readability by removing package qualification
5. This is a firm prohibition, not just a recommendation

# Construction / Recognition

## To Apply:
1. Always use qualified package names: `foo.Bar()` not `Bar()` via dot import
2. If you want shorter names, consider import renaming instead

## To Recognize:
1. Look for `import . "package"` declarations -- these must be removed
2. Look for unqualified identifiers that seem to come from another package

# Context & Application

While dot imports might seem convenient in test files (where you are testing a package and want to call its functions without qualification), Go style at Google prohibits them even there. The readability cost outweighs the typing convenience. When reading `Bar()` in a test file, the reader must determine whether `Bar` is defined in the test file, the package under test (via dot import), or some transitive dependency. Using `foo.Bar()` makes the origin immediately clear.

# Examples

**Example 1 -- Bad: dot import obscures origin** (Decisions, "Import dot"):

```go
// Bad:
package foo_test

import (
    "bar/testutil" // also imports "foo"
    . "foo"
)

var myThing = Bar() // Bar defined in package foo; no qualification needed.
```

**Example 2 -- Good: explicit qualification** (Decisions, "Import dot"):

```go
// Good:
package foo_test

import (
    "bar/testutil" // also imports "foo"
    "foo"
)

var myThing = foo.Bar()
```

# Relationships

## Related
- **import-renaming** -- Import renaming is the acceptable way to shorten package names (vs dot import)
- **import-grouping-google** -- Dot imports would not appear in any group since they are prohibited

# Common Errors

- **Error**: Using dot import in test files for convenience
  **Correction**: Use explicit package qualification: `foo.Bar()` instead of `Bar()`

- **Error**: Using dot import to avoid long package names
  **Correction**: Use import renaming with a shorter alias instead

# Common Confusions

- **Confusion**: Thinking dot imports are acceptable in test files since some open-source projects use them
  **Clarification**: Google style prohibits dot imports everywhere, including test files

- **Confusion**: Confusing dot import with blank import
  **Clarification**: Blank import (`import _ "pkg"`) runs init functions but does not import names; dot import (`import . "pkg"`) imports all exported names into the current namespace

# Source Reference

Chapter 3: Style Decisions, Section "Import dot (import .)".

# Verification Notes

- Definition source: Directly from the "Import dot" section of Google Go Style Decisions
- Confidence rationale: HIGH -- explicit prohibition with clear bad/good examples
- Uncertainties: None
- Cross-reference status: Related slugs verified against planned extractions
