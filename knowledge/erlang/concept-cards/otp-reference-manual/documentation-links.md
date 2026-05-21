---
# === CORE IDENTIFICATION ===
concept: Documentation Links
slug: documentation-links

# === CLASSIFICATION ===
category: documentation
subcategory: markdown-documentation
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Documentation"
chapter_number: null
pdf_page: null
section: "Links in Markdown"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "doc links"
  - "Markdown links in documentation"
  - "MFA links"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - doc-attribute
  - moduledoc-attribute
extends: []
related:
  - documentation-metadata
  - exdoc-tool
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I link to other functions from Erlang documentation?"
  - "How do I link to other modules, types, or callbacks?"
  - "What link prefixes are available in Erlang documentation?"
  - "How do I link to documentation in other applications?"
---

# Quick Definition
Erlang documentation in Markdown supports automatic linking to functions, modules, types, callbacks, and extra pages. Links are created using inline code segments with MFA syntax, and different prefixes (`m:`, `t:`, `c:`, `e:`) denote the target entity type.

# Core Definition
The Erlang Reference Manual states: "When writing documentation in Markdown, links are automatically found in any inline code segment that looks like an MFA." (Documentation, "Links in Markdown"). For example, `` `sub/2` `` creates a link to `sub/2` in the current module. Links can also use explicit Markdown link syntax: `` [subtract](`sub/2`) ``. Different entity types use prefixes: `module:function/arity` for remote functions, `m:module` for modules, `t:type/arity` for types, `c:callback/arity` for callbacks, and `e:app:page` for extra pages in other applications.

# Prerequisites
- **doc-attribute** -- Links are used within documentation text
- **moduledoc-attribute** -- Links are used within module documentation text

# Key Properties
1. Automatic linking: `` `sub/2` `` auto-links to the local function
2. Remote functions: `` `module:function/arity` ``
3. Module links: `` `m:module` `` with optional anchors `` `m:module#anchor` ``
4. Type links: `` `t:type/arity` `` or `` `t:module:type/arity` ``
5. Callback links: `` `c:callback/arity` `` or `` `c:module:callback/arity` ``
6. Extra pages (other apps): `` `e:app:page` `` with optional anchors
7. Named links: `` [name](`target`) `` syntax
8. Reference-style links are also supported

# Construction / Recognition
## Link Types:
```erlang
%% Local function
-doc "See `sub/2` for more details".

%% Remote function
-doc "See `arith:sub/2` for more details".

%% Module
-doc "See `m:arith` for more details".
-doc "See `m:arith#anchor` for more details".

%% Type
-doc "See `t:number/0` for more details".
-doc "See `t:arith:number/0` for more details".

%% Callback
-doc "See `c:increment/0` for more details".
-doc "See `c:arith:increment/0` for more details".

%% Extra page in another application
-doc "See `e:stdlib:unicode_usage` for more details".
-doc "See `e:stdlib:unicode_usage#notes-about-raw-filenames` for more details".
```

## Named Link Variants:
```erlang
-doc "See [subtract](`sub/2`) for more details".
-doc "See [`sub/2`] for more details".
```

# Context & Application
Documentation links create a navigable web of cross-references between functions, types, callbacks, and modules. They are essential for generated HTML/ePub documentation (via ExDoc) and are also used by IDE tooling. Automatic MFA detection means simple inline code references become clickable links without additional markup, making documentation both readable in source and navigable in rendered form.

# Examples
**Example 1** (Links in Markdown -- local function):
```erlang
-doc "See `sub/2` for more details".
```

**Example 2** (Links in Markdown -- named link variants):
```erlang
-doc "See [subtract](`sub/2`) for more details".
-doc "See [`sub/2`] for more details".
-doc """
See [subtract] for more details

[subtract]: `sub/2`
""".
-doc """
See [subtract][1] for more details

[1]: `sub/2`
""".
```
All four produce the same link.

**Example 3** (Links in Markdown -- extra pages):
```erlang
-doc "See `e:stdlib:unicode_usage` for more details".
```

# Relationships
## Builds Upon
- **doc-attribute** -- Links are used within `-doc` text
- **moduledoc-attribute** -- Links are used within `-moduledoc` text

## Enables
Navigable cross-references in generated documentation.

## Related
- **exdoc-tool** -- ExDoc renders these links as HTML hyperlinks

## Contrasts With
None.

# Common Errors
- **Error**: Forgetting the prefix for non-function entities
  **Correction**: Use `m:` for modules, `t:` for types, `c:` for callbacks, `e:` for extra pages. Without a prefix, the link targets a function.

- **Error**: Linking to a function that does not exist
  **Correction**: The link will be created but may not resolve. Verify the target exists.

# Common Confusions
- **Confusion**: Thinking all backtick-enclosed text becomes a link
  **Clarification**: Only inline code that "looks like an MFA" (e.g., `sub/2`, `m:arith`) is auto-linked. Arbitrary code snippets remain as plain code.

# Source Reference
"Documentation" chapter, "Links in Markdown" section.

# Verification Notes
- Definition source: Direct from source text with all prefix types listed
- Confidence rationale: High -- explicit link syntax with examples for each type
- Uncertainties: None
- Cross-reference status: All slugs verified
