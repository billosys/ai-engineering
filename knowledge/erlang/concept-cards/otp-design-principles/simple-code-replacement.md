---
# === CORE IDENTIFICATION ===
concept: Simple Code Replacement
slug: simple-code-replacement

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - code-replacement
  - functional-module
  - release-handling-instructions
extends: []
related:
  - application-upgrade-file
contrasts_with:
  - synchronized-code-replacement

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes simple code replacement from synchronized code replacement?"
  - "When should I use load_module in an .appup file?"
---

# Quick Definition

Simple code replacement is the process of loading a new version of a functional module and removing the old version, without suspending processes or transforming state, triggered by the `load_module` instruction.

# Core Definition

According to the OTP Design Principles "Release Handling" chapter: "If a simple extension has been made to a functional module, it is sufficient to load the new version of the module into the system, and remove the old version. This is called _simple code replacement_ and for this the following instruction is used: `{load_module, Module}`." Simple code replacement is appropriate when the change does not affect any process's internal state format and the module is not a residence module (i.e., no process has its loop function in this module).

# Prerequisites

- **Code Replacement** -- Simple code replacement is one form of code replacement.
- **Functional Module** -- Simple code replacement applies to functional modules.
- **Release Handling Instructions** -- Uses the `load_module` instruction.

# Key Properties

1. Uses the `{load_module, Module}` instruction.
2. Only loads the new module version and purges the old one.
3. No process suspension or resumption occurs.
4. No state transformation is triggered.
5. Appropriate for functional modules where no internal state format changes.
6. Can specify module dependencies: `{load_module, Module, DepMods}`.
7. The most common instruction for upgrading callback modules.

# Construction / Recognition

## To Construct/Create:
1. Determine the module is a functional module (not a loop module for any process).
2. Confirm no internal state format changes are needed.
3. Write `{load_module, Module}` in the .appup file for both upgrade and downgrade.
4. If other modules depend on this module, use `{load_module, Module, DepMods}` in dependent modules.

## To Identify/Recognize:
1. The `{load_module, Module}` instruction in an .appup file.
2. The changed module is a callback module or utility module.
3. No `code_change/3` callback is needed.

# Context & Application

Simple code replacement is the most straightforward upgrade path and should be used whenever possible. It is the default choice for changes to callback modules that do not alter the internal state format, such as adding a new function, fixing a bug in existing logic, or adding a new message handler. Because it does not suspend processes, it has minimal impact on system operation during the upgrade.

# Examples

**Example 1** (release_handling.md, "load_module"): The basic instruction:

```text
{load_module, Module}
```

**Example 2** (appup_cookbook.md, "Changing a Functional Module"): When a functional module has been changed (e.g., new function added or bug corrected):

```erlang
{"2",
 [{"1", [{load_module, m}]}],
 [{"1", [{load_module, m}]}]
}.
```

**Example 3** (appup_cookbook.md, "Changing a Callback Module"): The ch3 callback module with a new `available/0` function:

```erlang
{"2",
 [{"1", [{load_module, ch3}]}],
 [{"1", [{load_module, ch3}]}]
}.
```

# Relationships

## Builds Upon
- **Code Replacement** -- Simple code replacement is one of the two forms.
- **Functional Module** -- Simple code replacement applies to functional modules.

## Enables
- None directly.

## Related
- **Application Upgrade File** -- The `load_module` instruction is written in .appup files.

## Contrasts With
- **Synchronized Code Replacement** -- Synchronized replacement suspends processes, calls `code_change/3`, and resumes processes. Simple replacement just loads the new module. Use synchronized replacement when internal state needs transformation or the module is a residence module.

# Common Errors

- **Error**: Using simple code replacement when the internal state format has changed.
  **Correction**: If the gen_server (or other behaviour) state format changes, use synchronized code replacement (`update` with `{advanced, Extra}`) instead, even though the callback module is technically a functional module.

# Common Confusions

- **Confusion**: Thinking simple code replacement cannot be used for callback modules.
  **Clarification**: Callback modules are functional modules by definition and can use simple code replacement -- unless the change also requires a state transformation.

# Source Reference

OTP Design Principles, "Release Handling" chapter, section "load_module" (release_handling.md). Also "Appup Cookbook" chapter, sections "Changing a Functional Module" and "Changing a Callback Module" (appup_cookbook.md).

# Verification Notes

- Definition source: Directly quoted from release_handling.md "load_module" section.
- Confidence rationale: Explicitly named and defined concept.
- Uncertainties: None.
- Cross-reference status: Cross-references code-replacement, functional-module, synchronized-code-replacement, application-upgrade-file (new cards).
