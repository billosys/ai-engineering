---
# === CORE IDENTIFICATION ===
concept: Functional Module
slug: functional-module

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
  - "callback module (in release handling context)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - release-handling
  - code-replacement
extends: []
related:
  - simple-code-replacement
  - application-upgrade-file
  - callback-module
contrasts_with:
  - residence-module

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes a functional module from a residence module?"
  - "When can simple code replacement be used?"
---

# Quick Definition

A functional module is a module that is not the residence module for any process -- that is, no process has its tail-recursive loop function in that module.

# Core Definition

According to the OTP Design Principles "Release Handling" chapter: "_Functional module_ - A module that is not a residence module for any process." The source further clarifies: "For a process implemented using an OTP behaviour, the behaviour module is the residence module for that process. The callback module is a functional module." This distinction is critical for release handling because functional modules can be upgraded using simple code replacement (`load_module` instruction) without suspending or transforming any processes.

# Prerequisites

- **Release Handling** -- The distinction is relevant in the context of release handling.
- **Code Replacement** -- Understanding the two types of code replacement.

# Key Properties

1. No process has its tail-recursive loop function in a functional module.
2. In OTP terms, callback modules are functional modules.
3. Can be upgraded using simple code replacement (`load_module`).
4. No process suspension or state transformation is needed during replacement.
5. A module can be both functional for some contexts and non-functional in others (e.g., if used as a special process loop module).

# Construction / Recognition

## To Construct/Create:
1. Any module that is not used as the loop module of any process is a functional module.
2. OTP callback modules (the modules you write implementing gen_server callbacks, etc.) are functional modules.

## To Identify/Recognize:
1. Check if any process's child specification lists the module in its `Modules` field as a loop module.
2. For OTP behaviours, the callback module (your implementation) is functional; the behaviour module (gen_server, gen_statem, etc.) is the residence module.
3. The module is not referenced as a residence module in any supervision tree.

# Context & Application

The functional/residence module distinction determines what type of release handling instruction to use in .appup files. For functional modules, simple code replacement (`load_module`) is sufficient. This is the most common case in OTP applications since most developer-written modules are callback modules. Only when the internal state format changes does the callback module need synchronized code replacement (via the `code_change/3` callback).

# Examples

**Example 1** (release_handling.md, "Release Handling Instructions"): "For a process implemented using an OTP behaviour, the behaviour module is the residence module for that process. The callback module is a functional module."

**Example 2** (appup_cookbook.md, "Changing a Functional Module"): When a functional module changes, simple code replacement is sufficient:

```erlang
{"2",
 [{"1", [{load_module, m}]}],
 [{"1", [{load_module, m}]}]
}.
```

**Example 3** (appup_cookbook.md, "Changing a Callback Module"): "A callback module is a functional module, and for code extensions simple code replacement is sufficient."

# Relationships

## Builds Upon
- **Code Replacement** -- The functional module concept determines which type of code replacement to use.

## Enables
- **Simple Code Replacement** -- Functional modules are upgraded via simple code replacement.

## Related
- **Application Upgrade File** -- The module type determines the instruction in the .appup file.
- **Callback Module** -- OTP callback modules are functional modules.

## Contrasts With
- **Residence Module** -- A residence module is where a process has its loop function. A functional module is any module that is not a residence module for any process.

# Common Errors

- **Error**: Treating a callback module that changes internal state as needing only simple code replacement.
  **Correction**: If the state format changes, the callback module still needs synchronized code replacement (via `code_change/3`), even though it is technically a functional module. The distinction is about the module's role, but state changes require the `update` instruction regardless.

# Common Confusions

- **Confusion**: Thinking "functional module" means a module containing only pure functions.
  **Clarification**: In release handling, "functional module" specifically means a module that is not the loop module for any process. It has nothing to do with functional programming purity.

# Source Reference

OTP Design Principles, "Release Handling" chapter, section "Release Handling Instructions" (release_handling.md). Also "Appup Cookbook" chapter, sections "Changing a Functional Module" and "Changing a Callback Module" (appup_cookbook.md).

# Verification Notes

- Definition source: Directly quoted from release_handling.md "Release Handling Instructions" section.
- Confidence rationale: Explicitly defined term with clear distinction from residence module.
- Uncertainties: None.
- Cross-reference status: Cross-references code-replacement, simple-code-replacement, residence-module, callback-module (cross-source reference).
