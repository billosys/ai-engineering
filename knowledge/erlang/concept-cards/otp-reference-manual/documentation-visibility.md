---
# === CORE IDENTIFICATION ===
concept: Documentation Visibility
slug: documentation-visibility

# === CLASSIFICATION ===
category: documentation
subcategory: module-documentation
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Documentation"
chapter_number: null
pdf_page: null
section: "What is visible versus hidden?"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "hidden documentation"
  - "visible vs hidden"
  - "-doc false"
  - "-moduledoc false"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - doc-attribute
  - moduledoc-attribute
extends: []
related:
  - documentation-metadata
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I hide a module from documentation?"
  - "How do I hide an exported function from documentation?"
  - "What determines if a type is visible in documentation?"
  - "What is the default visibility of exported functions and types?"
---

# Quick Definition
By default, all exported functions, exported types, and callbacks are visible in documentation. Non-exported types referenced by visible entities are also visible but marked as not part of the public API. Modules and entities can be hidden using `-moduledoc false.` and `-doc false.` respectively.

# Core Definition
The Erlang Reference Manual states: "By default, all modules in an application are visible, but by setting `-moduledoc false.`, specific modules can be hidden from being listed as part of the available API." For entities: "By default, all exported functions, exported types and callbacks are considered visible and part of the module's public API. In addition, any non-exported type that is referred to by any other visible type attribute is also visible, but not considered to be part of the public API." (Documentation, "What is visible versus hidden?"). To hide a visible entity: "you need to set the `-doc` attribute to `false`." Documentation added to automatically hidden entities (non-exported) "is ignored and will generate a warning."

# Prerequisites
- **doc-attribute** -- `-doc false` hides entities
- **moduledoc-attribute** -- `-moduledoc false` hides modules

# Key Properties
1. Default: all exported functions, exported types, and callbacks are visible
2. Non-exported types referenced by visible entities are visible but marked `exported => false`
3. Hide a module: `-moduledoc false.`
4. Hide an entity: `-doc false.`
5. Hiding an exported function also hides non-exported types only referenced by that function
6. Documentation on non-exported entities is ignored and generates a warning
7. Non-exported entities should be documented with comments, not `-doc`

# Construction / Recognition
## To Hide a Module:
```erlang
-moduledoc false.
```

## To Hide an Exported Function:
```erlang
-doc false.
example() -> one.
```

## Visibility Cascade:
When a visible function references a non-exported type, the type becomes visible. When the function is hidden, the type becomes hidden too (if not referenced elsewhere).

# Context & Application
Visibility control allows modules to have exported functions that are not part of the public API -- for example, functions exported for internal use by other modules in the same application. The `-moduledoc false` is useful for hiding internal implementation modules from application-level documentation. The automatic visibility of referenced non-exported types ensures that documentation is complete: if a public function returns a non-exported type, that type's documentation is accessible.

# Examples
**Example 1** (What is visible versus hidden -- referenced type becomes visible):
```erlang
-export([example/0]).

-type private() :: one.
-spec example() -> private().
example() -> one.
```
Both `example/0` and `private/0` are visible. `private/0` has `exported => false`.

**Example 2** (What is visible versus hidden -- hiding an exported function):
```erlang
-export([example/0]).

-type private() :: one.
-spec example() -> private().
-doc false.
example() -> one.
```
Both `example/0` and `private/0` are hidden because the function is explicitly hidden.

# Relationships
## Builds Upon
- **doc-attribute** -- `-doc false` is the mechanism for hiding entities
- **moduledoc-attribute** -- `-moduledoc false` is the mechanism for hiding modules

## Enables
Control over what appears in generated documentation and shell help.

## Related
- **documentation-metadata** -- The `exported` metadata key relates to visibility

## Contrasts With
None.

# Common Errors
- **Error**: Adding `-doc` to a non-exported function
  **Correction**: Non-exported functions are automatically hidden. Adding `-doc` to them is ignored and generates a compiler warning. Use comments instead.

# Common Confusions
- **Confusion**: Thinking `-doc false` un-exports a function
  **Clarification**: `-doc false` only hides the function from documentation. The function remains exported and callable. It is purely a documentation visibility control.

- **Confusion**: Thinking non-exported types are always hidden
  **Clarification**: A non-exported type becomes visible if it is referenced by a visible entity (e.g., a function spec). It is visible in documentation but marked `exported => false` to indicate it is not part of the public API.

# Source Reference
"Documentation" chapter, "What is visible versus hidden?" section.

# Verification Notes
- Definition source: Direct from source text with examples
- Confidence rationale: High -- explicit rules and examples provided
- Uncertainties: None
- Cross-reference status: All slugs verified
