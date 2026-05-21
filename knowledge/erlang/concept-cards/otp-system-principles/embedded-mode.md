---
# === CORE IDENTIFICATION ===
concept: Embedded Mode
slug: embedded-mode

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
  - "embedded code loading"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - code-loading-strategy
extends: []
related:
  - code-path
contrasts_with:
  - interactive-mode

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is embedded mode vs interactive mode for code loading?"
  - "How does embedded mode differ from interactive mode?"
---

# Quick Definition

Embedded mode is the Erlang runtime code loading strategy in which all code is loaded during system startup according to the boot script, with no automatic loading of modules at runtime.

# Core Definition

As stated in OTP System Principles: "In embedded mode, all code is loaded during system startup according to the boot script. (Code can be loaded later by **explicitly** ordering the code server to load it.)" This means that after startup completes, any module not already loaded will not be found automatically — the code server will not search for it. Explicit calls to the code server are required to load additional modules after boot.

# Prerequisites

- **code-loading-strategy** — embedded mode is one of the two code loading strategies
- Understanding of boot scripts — they define what gets loaded in embedded mode

# Key Properties

1. All code is loaded at system startup time.
2. Loading is governed by the boot script.
3. No automatic/dynamic loading of modules when first referenced.
4. Additional code can only be loaded by explicitly ordering the code server to do so.
5. Activated via `erl -mode embedded`.

# Construction / Recognition

## To Construct/Create:
1. Prepare a boot script that lists all required applications and modules.
2. Generate the boot script from a `.rel` file using `systools:make_script/1,2`.
3. Start the runtime with `erl -mode embedded -boot Name`.

## To Identify/Recognize:
1. The system was started with `-mode embedded`.
2. Calling a function in an unloaded module fails rather than triggering automatic loading.

# Context & Application

Embedded mode is the standard choice for production deployments and OTP releases. It ensures deterministic startup — all code is loaded up front, so there are no surprises from missing modules at runtime. This is especially important for systems that must operate reliably without access to the source code tree or a development environment. The OTP release system generates boot scripts that specify exactly which modules to load.

# Examples

**Example 1** (System Principles, "Code Loading Strategy"): Starting in embedded mode:
```text
% erl -mode embedded
```

**Example 2** (System Principles, "User-Defined Boot Scripts"): The source notes that creating a user-defined boot script "is true especially when running Erlang in embedded mode."

# Relationships

## Builds Upon
- **code-loading-strategy** — embedded mode is one of the two available strategies
- **boot-script** — embedded mode depends on the boot script to know which code to load

## Enables
- **release** — OTP releases use embedded mode to ensure all application code is loaded deterministically

## Related
- **code-path** — while code-path exists in embedded mode, it is not used for automatic module discovery

## Contrasts With
- **interactive-mode** — in interactive mode, code is loaded on demand; in embedded mode, all code must be loaded at startup

# Common Errors

- **Error**: Using embedded mode without a complete boot script, leading to `undef` errors for missing modules.
  **Correction**: Generate a comprehensive boot script from a `.rel` file that includes all applications the system needs.

# Common Confusions

- **Confusion**: Thinking that no code can be loaded after startup in embedded mode.
  **Clarification**: Code can be loaded after startup, but only by explicitly requesting the code server to load it — it is not automatic.

# Source Reference

"Code Loading Strategy" section, "System Principles" chapter, "OTP System Principles" documentation.

# Verification Notes

- Definition source: Directly quoted from source text.
- Confidence rationale: High — explicit definition with clear semantics.
- Uncertainties: None.
- Cross-reference status: References interactive-mode, code-loading-strategy, code-path (cards in this extraction).
