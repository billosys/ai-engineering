---
# === CORE IDENTIFICATION ===
concept: ExDoc Tool
slug: exdoc-tool

# === CLASSIFICATION ===
category: documentation
subcategory: tooling
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Documentation"
chapter_number: null
pdf_page: null
section: "Using ExDoc to generate HTML/ePub documentation"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "ExDoc"
  - "rebar3_ex_doc"
  - "ex_doc"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - doc-attribute
  - moduledoc-attribute
  - documentation-compilation
extends: []
related:
  - documentation-links
  - documentation-metadata
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I generate HTML documentation for Erlang?"
  - "What is ExDoc?"
  - "How do I set up ExDoc with rebar3?"
---

# Quick Definition
ExDoc is a documentation generation tool with built-in support for Erlang's Markdown-based documentation. It generates HTML and ePub output from EEP-48 documentation chunks. The simplest integration for Erlang projects is through the `rebar3_ex_doc` plugin.

# Core Definition
The Erlang Reference Manual states: "ExDoc has built-in support to generate documentation from Markdown. The simplest way is by using the rebar3_ex_doc plugin." (Documentation, "Using ExDoc to generate HTML/ePub documentation"). ExDoc reads the compiled EEP-48 documentation chunks and generates formatted output. It can also be run as a standalone escript downloaded from the GitHub releases page.

# Prerequisites
- **doc-attribute** -- ExDoc renders `-doc` content
- **moduledoc-attribute** -- ExDoc renders `-moduledoc` content
- **documentation-compilation** -- ExDoc reads compiled EEP-48 chunks

# Key Properties
1. Generates HTML and ePub documentation
2. Built-in Markdown support
3. Primary integration: `rebar3_ex_doc` plugin
4. Also available as a standalone escript
5. Renders documentation links as HTML hyperlinks
6. Run with `rebar3 ex_doc` after configuration
7. Output defaults to `doc/index.html`
8. Supports extras (like README), main page, and source URL configuration

# Construction / Recognition
## rebar3 Setup:
Add to `rebar3.config`:
```erlang
%% Enable the plugin
{plugins, [rebar3_ex_doc]}.

{ex_doc, [
  {extras, ["README.md"]},
  {main, "README.md"},
  {source_url, "https://github.com/namespace/your_app"}
]}.
```

## Generate Documentation:
```
rebar3 ex_doc
```
Output: `doc/index.html`

## Standalone Escript:
Download from GitHub releases and run:
```
ex_doc --help
```

# Context & Application
ExDoc is the recommended tool for generating professional documentation from Erlang projects. Originally from the Elixir ecosystem, it supports Erlang's EEP-48 documentation format natively. It renders Markdown documentation, resolves cross-reference links, and produces navigable HTML documentation suitable for hosting on the web. If writing documentation that will use ExDoc, reading its own documentation is "highly recommended."

# Examples
**Example 1** (Using ExDoc -- rebar3 configuration):
```erlang
{plugins, [rebar3_ex_doc]}.

{ex_doc, [
  {extras, ["README.md"]},
  {main, "README.md"},
  {source_url, "https://github.com/namespace/your_app"}
]}.
```

**Example 2** (Using ExDoc -- generating docs):
```
$ rebar3 ex_doc
```
Generates documentation to `doc/index.html`.

# Relationships
## Builds Upon
- **documentation-compilation** -- ExDoc reads compiled EEP-48 chunks
- **doc-attribute** -- ExDoc renders function/type/callback documentation
- **moduledoc-attribute** -- ExDoc renders module documentation

## Enables
Professional, navigable HTML/ePub documentation for Erlang projects.

## Related
- **documentation-links** -- ExDoc resolves MFA links to HTML hyperlinks
- **documentation-metadata** -- ExDoc displays metadata (since, deprecated, etc.)

## Contrasts With
None.

# Common Errors
- **Error**: Running `rebar3 ex_doc` without adding the plugin
  **Correction**: Add `{plugins, [rebar3_ex_doc]}.` to `rebar3.config` first.

# Common Confusions
- **Confusion**: Thinking ExDoc is required to view documentation
  **Clarification**: Documentation is available in the shell via `h/1` without ExDoc. ExDoc is only needed for generating HTML/ePub output.

# Source Reference
"Documentation" chapter, "Using ExDoc to generate HTML/ePub documentation" section.

# Verification Notes
- Definition source: Direct from source text with configuration example
- Confidence rationale: High -- explicit setup instructions provided
- Uncertainties: None
- Cross-reference status: All slugs verified
