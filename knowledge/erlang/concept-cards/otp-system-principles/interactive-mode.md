---
# === CORE IDENTIFICATION ===
concept: Interactive Mode
slug: interactive-mode

# === CLASSIFICATION ===
category: applications-releases
subcategory: runtime-configuration
tier: intermediate

# === PROVENANCE ===
source: "OTP System Principles"
source_slug: otp-system-principles
authors: "Ericsson AB"
chapter: "System Principles"
chapter_number: null
pdf_page: null
section: "Code Loading Strategy"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "interactive code loading"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - code-loading-strategy
extends: []
related:
  - code-path
contrasts_with:
  - embedded-mode

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is embedded mode vs interactive mode for code loading?"
  - "How does embedded mode differ from interactive mode?"
---

# Quick Definition

Interactive mode is the default Erlang runtime code loading strategy in which modules are dynamically loaded when first referenced, with the code server searching the code path to find them.

# Core Definition

As stated in OTP System Principles: "In interactive mode, code is dynamically loaded when first required, which means that when an attempt is made to call a function in a module that is not loaded, the code server searches the code path and loads the module into the system." Interactive mode is the default when no `-mode` flag is specified.

# Prerequisites

- **code-loading-strategy** — interactive mode is one of the two code loading strategies
- **code-path** — the code server uses the code path to search for modules

# Key Properties

1. Code is loaded dynamically when first referenced.
2. The code server searches the code path to find unloaded modules.
3. This is the default mode — no `-mode` flag is needed.
4. A call to an unloaded module triggers automatic loading rather than an error.
5. Convenient for development and experimentation.

# Construction / Recognition

## To Construct/Create:
1. Start the runtime without a `-mode` flag (default), or with `erl -mode interactive`.
2. Ensure the code path includes all directories where modules reside.

## To Identify/Recognize:
1. No `-mode` flag was specified, or `-mode interactive` was used.
2. Modules are loaded transparently when first called — no explicit load step is needed.

# Context & Application

Interactive mode is the natural choice for development, testing, and exploratory programming in the Erlang shell. Developers can compile modules, add directories to the code path, and call functions without worrying about boot scripts or explicit code loading. However, it is generally not used for production deployments because it introduces non-determinism — the system depends on the code path being correctly configured and modules being discoverable at runtime.

# Examples

**Example 1** (System Principles, "Code Loading Strategy"): The default mode when no `-mode` flag is present:
```text
% erl
```
This starts the system in interactive mode. Calling a function in a module that has not been loaded will cause the code server to search the code path and load it automatically.

# Relationships

## Builds Upon
- **code-loading-strategy** — interactive mode is one of the two available strategies
- **code-path** — the code server uses the code path to locate modules on demand

## Enables
- Development workflows — interactive mode enables rapid iteration without rebuilding boot scripts

## Related
- **code-path** — the code path determines where modules are found during on-demand loading

## Contrasts With
- **embedded-mode** — in embedded mode, all code must be loaded at startup; in interactive mode, code is loaded on demand

# Common Errors

- **Error**: Expecting interactive mode in production and finding that modules fail to load because the code path is incomplete.
  **Correction**: In production, use embedded mode with a complete boot script, or ensure the code path is correctly set up.

# Common Confusions

- **Confusion**: Thinking interactive mode requires a boot script listing all modules.
  **Clarification**: Interactive mode does not require listing modules in a boot script — they are loaded on demand from the code path.

# Source Reference

"Code Loading Strategy" section, "System Principles" chapter, "OTP System Principles" documentation.

# Verification Notes

- Definition source: Directly quoted from source text.
- Confidence rationale: High — explicit definition with clear semantics.
- Uncertainties: None.
- Cross-reference status: References embedded-mode, code-loading-strategy, code-path (cards in this extraction).
