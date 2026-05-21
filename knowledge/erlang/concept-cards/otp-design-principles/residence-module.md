---
# === CORE IDENTIFICATION ===
concept: Residence Module
slug: residence-module

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
  - "loop module"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - release-handling
  - code-replacement
extends: []
related:
  - synchronized-code-replacement
  - application-upgrade-file
  - behaviour
contrasts_with:
  - functional-module

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes a functional module from a residence module?"
  - "What is a residence module?"
---

# Quick Definition

A residence module is a module where a process has its tail-recursive loop function(s); if a process's loop spans multiple modules, all of them are residence modules for that process.

# Core Definition

According to the OTP Design Principles "Release Handling" chapter: "_Residence module_ - The module where a process has its tail-recursive loop function(s). If these functions are implemented in several modules, all those modules are residence modules for the process." For OTP behaviours, the behaviour module (e.g., `gen_server`, `gen_statem`, `gen_event`, `supervisor`) is the residence module for the process. Changing a residence module generally requires synchronized code replacement because the process needs to switch to the new code at a controlled point in its execution.

# Prerequisites

- **Release Handling** -- The concept is relevant in the context of release handling.
- **Code Replacement** -- Understanding why residence modules need special handling.

# Key Properties

1. Contains the tail-recursive loop function(s) of a process.
2. A single process can have multiple residence modules if the loop spans several modules.
3. For OTP behaviours, the behaviour module itself is the residence module.
4. OTP does not provide support for changing standard behaviour residence modules (supervisor, gen_server, etc.) -- these typically require a runtime system restart.
5. Special processes can have user-written residence modules that require synchronized code replacement.
6. The release handler finds processes using a module by checking child specification `Modules` fields.

# Construction / Recognition

## To Construct/Create:
1. Any module containing the tail-recursive loop function of a process is a residence module.
2. In OTP, this is typically the behaviour module (gen_server, gen_statem, etc.), not the user's callback module.
3. For special processes, the user-written loop module is the residence module.

## To Identify/Recognize:
1. The module is listed in the `Modules` field of a child specification.
2. For event managers, `Modules=dynamic` is used and the event manager reports its handlers.
3. The module contains the primary receive loop or the tail-recursive server loop.

# Context & Application

Residence modules require synchronized code replacement because a process must switch to the new version of its loop function at a controlled point. For standard OTP behaviours, the residence modules are part of STDLIB and can only be upgraded by restarting the runtime system. For special processes, the user must implement `system_code_change/4` to handle the transition. Understanding this distinction is critical for writing correct .appup files.

# Examples

**Example 1** (release_handling.md, "Release Handling Instructions"): "For a process implemented using an OTP behaviour, the behaviour module is the residence module for that process. The callback module is a functional module."

**Example 2** (appup_cookbook.md, "Changing a Residence Module"): "In a system implemented according to the OTP design principles, all processes, except system processes and special processes, reside in one of the behaviours `supervisor`, `gen_server`, `gen_statem`, `gen_event`, or `gen_fsm`. These belong to the STDLIB application and upgrading/downgrading normally requires a runtime system restart."

**Example 3** (appup_cookbook.md, "Changing Code for a Special Process"): For special processes, the residence module can be updated using synchronized code replacement via `system_code_change/4`:

```erlang
{"2",
 [{"1", [{update, ch4, {advanced, []}}]}],
 [{"1", [{update, ch4, {advanced, []}}]}]
}.
```

# Relationships

## Builds Upon
- **Code Replacement** -- Residence modules determine when synchronized replacement is needed.

## Enables
- **Synchronized Code Replacement** -- Residence modules require this type of replacement.

## Related
- **Application Upgrade File** -- The .appup file must use `update` instructions for residence modules.
- **Behaviour** -- OTP behaviour modules are residence modules for their processes.

## Contrasts With
- **Functional Module** -- A functional module is not the loop module for any process and can use simple code replacement. A residence module requires synchronized code replacement.

# Common Errors

- **Error**: Trying to upgrade a standard OTP behaviour module (gen_server, etc.) without a runtime restart.
  **Correction**: Standard behaviour modules belong to STDLIB and require a runtime system restart for upgrades. Use `restart_new_emulator` for such cases.

- **Error**: Not listing the residence module in the child specification's `Modules` field.
  **Correction**: The release handler finds affected processes by checking `Modules` in child specifications. If a special process's residence module is not listed, the release handler cannot find or update it.

# Common Confusions

- **Confusion**: Thinking all modules used by a gen_server process are residence modules.
  **Clarification**: Only the behaviour module (gen_server itself) is the residence module. The callback module (your implementation) is a functional module, even though the gen_server process calls functions in it.

# Source Reference

OTP Design Principles, "Release Handling" chapter, section "Release Handling Instructions" (release_handling.md). Also "Appup Cookbook" chapter, sections "Changing a Residence Module" and "Changing Code for a Special Process" (appup_cookbook.md).

# Verification Notes

- Definition source: Directly quoted from release_handling.md "Release Handling Instructions" section.
- Confidence rationale: Explicitly defined term with clear OTP behavioural context.
- Uncertainties: None.
- Cross-reference status: Cross-references code-replacement, synchronized-code-replacement, functional-module, behaviour (cross-source reference).
