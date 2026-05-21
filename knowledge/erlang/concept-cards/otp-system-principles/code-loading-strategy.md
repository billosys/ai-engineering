---
# === CORE IDENTIFICATION ===
concept: Code Loading Strategy
slug: code-loading-strategy

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
  - "code loading mode"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - embedded-mode
  - interactive-mode
  - code-path
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is embedded mode vs interactive mode for code loading?"
  - "How does embedded mode differ from interactive mode?"
---

# Quick Definition

The code loading strategy determines whether the Erlang runtime system loads all code at startup (embedded mode) or loads code on demand when first referenced (interactive mode). It is selected via the `-mode` command-line flag.

# Core Definition

As stated in OTP System Principles: "The runtime system can be started in either _embedded_ or _interactive_ mode. Which one is decided by the command-line flag `-mode`." The default mode is `interactive`. If more than one `-mode` flag is given, the first one is used. The two modes govern fundamentally different approaches to when and how BEAM code is loaded into the runtime system.

# Prerequisites

- Understanding of the Erlang runtime system and the `erl` command
- Understanding of boot scripts (boot scripts control what is loaded in embedded mode)

# Key Properties

1. Two mutually exclusive modes: embedded and interactive.
2. Selected via the `-mode` command-line flag (e.g., `erl -mode embedded`).
3. Default mode is `interactive`.
4. If multiple `-mode` flags are given, only the first is used.
5. Determines the relationship between code availability and system startup.

# Construction / Recognition

## To Construct/Create:
1. Decide whether all code must be available at startup (embedded) or can be loaded on demand (interactive).
2. For embedded mode: `erl -mode embedded` — ensure a complete boot script is provided.
3. For interactive mode: use the default, or explicitly `erl -mode interactive`.

## To Identify/Recognize:
1. Check the command-line arguments for `-mode embedded` or `-mode interactive`.
2. If no `-mode` flag is present, the system is running in interactive mode.

# Context & Application

The code loading strategy is a critical deployment decision. Interactive mode is convenient during development because modules are loaded automatically when first called. Embedded mode is used in production releases where all code must be loaded deterministically at startup, and where no dynamic code loading should occur unless explicitly requested. Embedded mode requires a user-defined boot script that enumerates all applications and modules to load.

# Examples

**Example 1** (System Principles, "Code Loading Strategy"): Starting the system in embedded mode:
```text
% erl -mode embedded
```

# Relationships

## Builds Upon
- **boot-script** — embedded mode loads all code according to the boot script at startup

## Enables
- **embedded-mode** — one of the two strategies
- **interactive-mode** — the other strategy

## Related
- **code-path** — in interactive mode, the code path determines where modules are found

## Contrasts With
- No direct contrast — the concept encompasses both modes.

# Common Errors

- **Error**: Running in embedded mode without a comprehensive boot script, causing missing modules at runtime.
  **Correction**: Ensure the boot script includes all required applications and modules when using embedded mode.

- **Error**: Specifying multiple `-mode` flags expecting the last to take effect.
  **Correction**: Only the first `-mode` flag is used; remove duplicate flags.

# Common Confusions

- **Confusion**: Thinking the default mode is embedded because production systems use it.
  **Clarification**: The default mode is always `interactive`. Embedded mode must be explicitly selected.

# Source Reference

"Code Loading Strategy" section, "System Principles" chapter, "OTP System Principles" documentation.

# Verification Notes

- Definition source: Direct from source text.
- Confidence rationale: High — explicitly described with clear semantics and command-line syntax.
- Uncertainties: None.
- Cross-reference status: References embedded-mode, interactive-mode, code-path (cards in this extraction).
