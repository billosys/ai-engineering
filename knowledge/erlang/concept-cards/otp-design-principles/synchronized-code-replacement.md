---
# === CORE IDENTIFICATION ===
concept: Synchronized Code Replacement
slug: synchronized-code-replacement

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
  - residence-module
  - release-handling-instructions
extends: []
related:
  - changing-internal-state
  - changing-a-supervisor
  - application-upgrade-file
contrasts_with:
  - simple-code-replacement

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes simple code replacement from synchronized code replacement?"
  - "When must I use the update instruction?"
---

# Quick Definition

Synchronized code replacement is the process of suspending affected processes, asking them to transform their internal state and switch to the new module version, then resuming them, triggered by the `update` instruction.

# Core Definition

According to the OTP Design Principles "Release Handling" chapter: "If a more complex change has been made, for example, a change to the format of the internal state of a `gen_server`, simple code replacement is not sufficient. Instead, it is necessary to: Suspend the processes using the module (to avoid that they try to handle any requests before the code replacement is completed). Ask them to transform the internal state format and switch to the new version of the module. Remove the old version. Resume the processes. This is called _synchronized code replacement_." The release handler performs this via `sys:suspend/1,2`, `sys:change_code/4,5`, and `sys:resume/1,2`.

# Prerequisites

- **Code Replacement** -- Synchronized code replacement is one form of code replacement.
- **Residence Module** -- Needed for understanding when synchronized replacement is required.
- **Release Handling Instructions** -- Uses the `update` instruction.

# Key Properties

1. Uses `{update, Module, {advanced, Extra}}` for state transformation.
2. Uses `{update, Module, supervisor}` for supervisor changes.
3. Four-phase process: suspend -> code_change -> load new version -> resume.
4. The release handler calls `sys:suspend/1,2`, `sys:change_code/4,5`, and `sys:resume/1,2`.
5. Triggers `code_change/3` in behaviour processes (gen_server, gen_statem, gen_event).
6. Triggers `system_code_change/4` in special processes.
7. Affected processes are found by traversing supervision trees and checking `Modules` in child specifications.
8. For event managers (`Modules=dynamic`), the list of installed handlers is checked.

# Construction / Recognition

## To Construct/Create:
1. Determine the change requires state transformation or is a supervisor change.
2. Implement `code_change/3` in the callback module (for behaviours) or `system_code_change/4` (for special processes).
3. Write `{update, Module, {advanced, Extra}}` or `{update, Module, supervisor}` in the .appup file.
4. Ensure the module is listed in the `Modules` field of the child specification.

## To Identify/Recognize:
1. The `{update, Module, ...}` instruction in an .appup file.
2. A `code_change/3` or `system_code_change/4` function in the module.
3. State format changes between versions.

# Context & Application

Synchronized code replacement is necessary whenever the internal state of a process must change to be compatible with new code, or when a supervisor's child specifications or restart strategy change. It is more complex and intrusive than simple code replacement because processes are briefly suspended, preventing them from handling requests during the transition. The `Extra` term in `{advanced, Extra}` is passed directly to `code_change/3`, allowing the developer to provide migration hints.

# Examples

**Example 1** (release_handling.md, "update"): The instructions for synchronized code replacement:

```erlang
{update, Module, {advanced, Extra}}
{update, Module, supervisor}
```

**Example 2** (appup_cookbook.md, "Changing Internal State"): An .appup file for ch3 where the state format changes from `Chs` to `{Chs, N}`:

```erlang
{"2",
 [{"1", [{update, ch3, {advanced, []}}]}],
 [{"1", [{update, ch3, {advanced, []}}]}]
}.
```

With the corresponding `code_change/3`:

```erlang
code_change({down, _Vsn}, {Chs, N}, _Extra) ->
    {ok, Chs};
code_change(_Vsn, Chs, _Extra) ->
    {ok, {Chs, 0}}.
```

# Relationships

## Builds Upon
- **Code Replacement** -- Synchronized replacement is the more complex form.
- **Residence Module** -- Required for residence module changes.

## Enables
- **Changing Internal State** -- State transformation is performed during synchronized replacement.
- **Changing a Supervisor** -- Supervisor updates use the `supervisor` variant.

## Related
- **Application Upgrade File** -- The `update` instruction is written in .appup files.

## Contrasts With
- **Simple Code Replacement** -- Simple replacement just loads new code without suspending processes. Synchronized replacement suspends processes, transforms state, loads code, and resumes processes. Use simple replacement when no state change is needed and the module is functional.

# Common Errors

- **Error**: Not implementing `code_change/3` when using `{advanced, Extra}`.
  **Correction**: The `code_change/3` callback must be implemented and exported. It receives the old version, the current state, and the `Extra` term, and must return `{ok, NewState}`.

- **Error**: Forgetting to handle the downgrade case in `code_change/3`.
  **Correction**: The first argument is `{down, Vsn}` for downgrades and `Vsn` for upgrades. Both cases must be handled.

# Common Confusions

- **Confusion**: Thinking synchronized code replacement is only for residence modules.
  **Clarification**: It is also needed for callback modules (functional modules) when the internal state format of the process changes. The `update` instruction with `{advanced, Extra}` triggers `code_change/3` on the process regardless of whether the changed module is a residence module or functional module.

# Source Reference

OTP Design Principles, "Release Handling" chapter, section "update" (release_handling.md). Also "Appup Cookbook" chapter, section "Changing Internal State" (appup_cookbook.md).

# Verification Notes

- Definition source: Directly quoted from release_handling.md "update" section.
- Confidence rationale: Explicitly named and defined concept with detailed process description.
- Uncertainties: None.
- Cross-reference status: Cross-references code-replacement, residence-module, simple-code-replacement, changing-internal-state, changing-a-supervisor (new cards).
