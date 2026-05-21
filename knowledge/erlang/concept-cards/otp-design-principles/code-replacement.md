---
# === CORE IDENTIFICATION ===
concept: Code Replacement
slug: code-replacement

# === CLASSIFICATION ===
category: applications-releases
subcategory: releases
tier: advanced

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "Release Handling"
chapter_number: null
pdf_page: null
section: "Release Handling Instructions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "hot code loading"
  - "hot code swapping"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - release-handling
extends: []
related:
  - simple-code-replacement
  - synchronized-code-replacement
  - functional-module
  - residence-module
  - release-handling-instructions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes simple code replacement from synchronized code replacement?"
  - "What is code replacement in OTP?"
---

# Quick Definition

Code replacement is the Erlang language feature that allows module code to be changed at runtime, serving as the foundation for the OTP release handling framework.

# Core Definition

According to the OTP Design Principles "Release Handling" chapter: "An important feature of the Erlang programming language is the ability to change module code at runtime, _code replacement_." Code replacement in the OTP framework takes two forms: _simple code replacement_ (loading a new module version, sufficient for functional modules) and _synchronized code replacement_ (suspending processes, transforming state, loading new code, and resuming processes, required for residence modules). The type of replacement needed depends on whether the changed module is a functional module or a residence module.

# Prerequisites

- **Release Handling** -- Code replacement is performed within the release handling framework.

# Key Properties

1. Erlang supports two versions of a module simultaneously (current and old).
2. Simple code replacement only loads the new version and purges the old one.
3. Synchronized code replacement involves suspending processes, transforming state, loading code, and resuming processes.
4. The type of replacement depends on whether the module is a functional module or a residence module.
5. Code replacement is orchestrated by the release handler using instructions in .appup and relup files.

# Construction / Recognition

## To Construct/Create:
1. Determine if the module is a functional module or residence module.
2. For functional modules, use the `load_module` instruction (simple code replacement).
3. For residence modules (or when internal state changes), use the `update` instruction (synchronized code replacement).
4. Specify these instructions in the .appup file.

## To Identify/Recognize:
1. `{load_module, Module}` instructions indicate simple code replacement.
2. `{update, Module, {advanced, Extra}}` instructions indicate synchronized code replacement.
3. The distinction depends on whether any process uses the module as its loop module.

# Context & Application

Code replacement is the mechanism that enables Erlang's legendary ability to upgrade live systems without downtime. Understanding the distinction between simple and synchronized replacement is critical for writing correct .appup files. Using the wrong type of replacement can lead to processes running old code or crashing during upgrades.

# Examples

**Example 1** (release_handling.md, "Release Handling Instructions"): The `load_module` instruction for simple code replacement of a functional module:

```text
{load_module, Module}
```

**Example 2** (release_handling.md, "Release Handling Instructions"): The `update` instruction for synchronized code replacement:

```erlang
{update, Module, {advanced, Extra}}
{update, Module, supervisor}
```

# Relationships

## Builds Upon
- **Release Handling** -- Code replacement is the core mechanism used by release handling.

## Enables
- **Simple Code Replacement** -- One of the two forms of code replacement.
- **Synchronized Code Replacement** -- The other form of code replacement.

## Related
- **Functional Module** -- Determines which type of code replacement to use.
- **Residence Module** -- Determines which type of code replacement to use.
- **Release Handling Instructions** -- Instructions that control code replacement.

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Using simple code replacement for a residence module.
  **Correction**: If a module is the loop module for any process, synchronized code replacement (the `update` instruction) must be used instead of `load_module`.

# Common Confusions

- **Confusion**: Thinking code replacement is automatic.
  **Clarification**: While Erlang supports loading new module versions at runtime, the OTP release handling framework requires explicit instructions (.appup files) to orchestrate the replacement correctly, especially for synchronized code replacement.

# Source Reference

OTP Design Principles, "Release Handling" chapter, section "Release Handling Instructions" (release_handling.md).

# Verification Notes

- Definition source: Directly from release_handling.md "Release Handling Principles" and "Release Handling Instructions" sections.
- Confidence rationale: Explicitly defined concept forming the basis of release handling.
- Uncertainties: None.
- Cross-reference status: Cross-references release-handling, simple-code-replacement, synchronized-code-replacement, functional-module, residence-module (new cards).
