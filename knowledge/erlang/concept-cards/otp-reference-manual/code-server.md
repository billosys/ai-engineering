---
# === CORE IDENTIFICATION ===
concept: Code Server
slug: code-server

# === CLASSIFICATION ===
category: core-idioms
subcategory: code-loading
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Compilation and Code Loading"
chapter_number: null
pdf_page: null
section: "Code Loading"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "code module"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-compilation
  - beam-object-code
extends: []
related:
  - code-loading-modes
  - code-replacement
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Erlang code server?"
  - "How is code loaded in Erlang?"
  - "What manages module loading in the Erlang runtime?"
---

# Quick Definition
The code server is the component of the Erlang runtime system responsible for loading object code into the system. It is implemented in the `code` module in the Kernel application.

# Core Definition
The Erlang Reference Manual states: "The object code must be _loaded_ into the Erlang runtime system. This is handled by the _code server_, see module `code` in Kernel." (Compilation and Code Loading, "Code Loading" section).

# Prerequisites
- **erlang-compilation** -- Code must be compiled before it can be loaded
- **beam-object-code** -- The code server loads BEAM object code

# Key Properties
1. Implemented in the `code` module (Kernel application)
2. Responsible for loading, managing, and purging module code
3. Operates according to a code loading strategy: interactive or embedded
4. Maintains the code path -- a list of directories to search for `.beam` files
5. Manages the current and old versions of each loaded module
6. Handles purging of old code when a third version is loaded

# Construction / Recognition
## To Construct/Create:
The code server is started automatically as part of the Erlang runtime system; it is not created by application code.

## To Identify/Recognize:
1. Any use of the `code` module functions
2. The code server process is always running in an Erlang node

# Context & Application
The code server is central to Erlang's runtime operation. It manages the code path (where to find modules), loads modules on demand or at startup, and orchestrates hot code loading by maintaining current and old versions of modules. Understanding the code server is essential for managing releases, debugging code loading issues, and implementing hot upgrades.

# Examples
**Example 1** (common code server operations):
```erlang
1> code:which(lists).
"/usr/lib/erlang/lib/stdlib-4.0/ebin/lists.beam"
2> code:is_loaded(my_module).
false
3> code:load_file(my_module).
{module, my_module}
```

# Relationships
## Builds Upon
- **erlang-compilation** -- The code server loads compiled code
- **beam-object-code** -- Loads `.beam` files

## Enables
- **code-loading-modes** -- The code server operates in interactive or embedded mode
- **code-replacement** -- The code server manages current and old code versions

## Related
- **on-load-function** -- The code server triggers on_load functions

## Contrasts With
None.

# Common Errors
- **Error**: Module not found because the code path does not include the directory containing the `.beam` file
  **Correction**: Use `code:add_path(Dir)` or `code:add_patha(Dir)` to add directories to the code path

# Common Confusions
- **Confusion**: Thinking modules are loaded when the VM starts in interactive mode
  **Clarification**: In interactive mode, modules are loaded on demand (when first referenced), not at startup. In embedded mode, all modules are loaded at startup from a boot script.

# Source Reference
"Compilation and Code Loading" chapter, "Code Loading" section.

# Verification Notes
- Definition source: Direct quote from source
- Confidence rationale: High -- explicit identification of the code server
- Uncertainties: Detailed API of the `code` module is in the Kernel documentation, not this section
- Cross-reference status: All slugs correspond to planned or existing cards
