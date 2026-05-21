---
# === CORE IDENTIFICATION ===
concept: Documentation Compilation
slug: documentation-compilation

# === CLASSIFICATION ===
category: documentation
subcategory: tooling
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Documentation"
chapter_number: null
pdf_page: null
section: "Compiling and getting documentation"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "EEP-48 chunks"
  - "documentation chunks"
  - "compiling docs"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - doc-attribute
  - moduledoc-attribute
extends: []
related:
  - exdoc-tool
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How is Erlang documentation compiled?"
  - "How do I retrieve documentation at runtime?"
  - "How do I disable documentation compilation?"
  - "What are EEP-48 documentation chunks?"
---

# Quick Definition
The Erlang compiler automatically inserts documentation into EEP-48 documentation chunks in the compiled beam file. Documentation can be retrieved at runtime with `code:get_doc/1` or viewed with the shell `h/1` command. Compilation of documentation chunks can be disabled with the `no_docs` flag.

# Core Definition
The Erlang Reference Manual states: "The Erlang compiler will by default insert documentation into EEP-48 documentation chunks when compiling a module." (Documentation, "Compiling and getting documentation"). "By passing the `no_docs` flag to `compile:file/1`, or `+no_docs` to `erlc`, no documentation chunk is inserted." "The documentation can then be retrieved using `code:get_doc/1`, or viewed using the shell built-in command `h/1`."

# Prerequisites
- **doc-attribute** -- Documentation must be written before it can be compiled
- **moduledoc-attribute** -- Module documentation must be written before compilation

# Key Properties
1. Documentation is compiled into EEP-48 chunks in the beam file by default
2. EEP-48 is the standard for documentation storage in beam files
3. Disable with `no_docs` flag to `compile:file/1` or `+no_docs` to `erlc`
4. Retrieve at runtime: `code:get_doc/1`
5. View in shell: `h(Module)` or `h(Module, Function)`
6. Shell shows both module documentation and function documentation with signatures

# Construction / Recognition
## Default Compilation (docs included):
```
erlc my_module.erl
```

## Compilation Without Docs:
```
erlc +no_docs my_module.erl
```
Or:
```erlang
compile:file("my_module.erl", [no_docs]).
```

## Retrieving Documentation:
```erlang
1> h(arith).         %% Module documentation
2> h(arith, add).    %% Function documentation
```

# Context & Application
Documentation compilation into EEP-48 chunks means documentation is always available at runtime when beam files are loaded, without needing separate documentation files. This enables the shell `h/1` command, IDE integration, and programmatic access via `code:get_doc/1`. The `no_docs` flag is useful for production deployments where documentation is not needed and beam file size should be minimized.

# Examples
**Example 1** (Compiling and getting documentation):
```text
1> h(arith).

      arith

  A module for basic arithmetic.

2> h(arith, add).

      add(One, Two)

  Adds two numbers.
```

# Relationships
## Builds Upon
- **doc-attribute** -- `-doc` content is compiled into chunks
- **moduledoc-attribute** -- `-moduledoc` content is compiled into chunks

## Enables
- **exdoc-tool** -- ExDoc reads the compiled documentation chunks

## Related
None.

## Contrasts With
None.

# Common Errors
- **Error**: Expecting documentation in beam files compiled with `no_docs`
  **Correction**: The `no_docs` flag suppresses documentation chunk generation. Remove the flag to include documentation.

# Common Confusions
- **Confusion**: Thinking documentation requires a separate generation step
  **Clarification**: The Erlang compiler automatically includes documentation in beam files. No separate step is needed for runtime access via `h/1`. A separate tool (ExDoc) is only needed for HTML/ePub output.

# Source Reference
"Documentation" chapter, "Compiling and getting documentation" section.

# Verification Notes
- Definition source: Direct from source text
- Confidence rationale: High -- explicit compilation and retrieval described
- Uncertainties: None
- Cross-reference status: All slugs verified
