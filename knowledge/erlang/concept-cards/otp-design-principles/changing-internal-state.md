---
# === CORE IDENTIFICATION ===
concept: Changing Internal State
slug: changing-internal-state

# === CLASSIFICATION ===
category: applications-releases
subcategory: releases
tier: advanced

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "Appup Cookbook"
chapter_number: null
pdf_page: null
section: "Changing Internal State"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "code_change/3"
  - "state migration"
  - "state transformation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - synchronized-code-replacement
  - gen-server
extends: []
related:
  - application-upgrade-file
  - functional-module
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I handle state changes during a release upgrade?"
  - "What is code_change/3 used for?"
---

# Quick Definition

Changing internal state is the process of transforming a behaviour process's state format during a release upgrade using the `code_change/3` callback, triggered by the `{update, Module, {advanced, Extra}}` instruction.

# Core Definition

According to the OTP Design Principles "Appup Cookbook" chapter: "In this case, simple code replacement is not sufficient. The process must explicitly transform its state using the callback function `code_change/3` before switching to the new version of the callback module. Thus, synchronized code replacement is used." The `code_change/3` callback receives the old version identifier (`Vsn` for upgrades, `{down, Vsn}` for downgrades), the current state, and the `Extra` term from the instruction, and must return `{ok, NewState}`. For special processes, the equivalent is `system_code_change/4`.

# Prerequisites

- **Synchronized Code Replacement** -- State changes require synchronized code replacement.
- **gen_server** (or other OTP behaviour) -- The process whose state is being transformed must be an OTP behaviour process.

# Key Properties

1. Required when the internal state format of a process changes between versions.
2. Uses the `{update, Module, {advanced, Extra}}` instruction in the .appup file.
3. The `Extra` term is passed directly to `code_change/3`.
4. `code_change/3` signature: `code_change(OldVsn, State, Extra) -> {ok, NewState}`.
5. First argument is `Vsn` for upgrade, `{down, Vsn}` for downgrade.
6. `Vsn` is the module's `-vsn` attribute value, or the beam file checksum if no vsn attribute.
7. For special processes, `system_code_change/4` is used instead.
8. Must handle both upgrade and downgrade transformations.

# Construction / Recognition

## To Construct/Create:
1. Implement and export `code_change/3` in the callback module.
2. Handle the upgrade case: transform old state format to new format.
3. Handle the downgrade case (first argument is `{down, Vsn}`): transform new state format back to old format.
4. Write `{update, Module, {advanced, Extra}}` in the .appup file.

## To Identify/Recognize:
1. A `code_change/3` function exported from a callback module.
2. An `{update, Module, {advanced, Extra}}` instruction in the .appup file.
3. Different state formats between module versions.

# Context & Application

State migration is one of the most common and important aspects of release handling. Any time a gen_server, gen_statem, or gen_event handler changes its internal state representation, the developer must implement `code_change/3` to transform existing process states to the new format. This enables live systems to upgrade without losing process state or requiring restarts. The `Extra` term provides a mechanism for passing migration parameters.

# Examples

**Example 1** (appup_cookbook.md, "Changing Internal State"): The ch3 module's state changes from `Chs` (just channels) to `{Chs, N}` (channels plus a counter). The .appup file:

```erlang
{"2",
 [{"1", [{update, ch3, {advanced, []}}]}],
 [{"1", [{update, ch3, {advanced, []}}]}]
}.
```

The `code_change/3` implementation:

```erlang
code_change({down, _Vsn}, {Chs, N}, _Extra) ->
    {ok, Chs};
code_change(_Vsn, Chs, _Extra) ->
    {ok, {Chs, 0}}.
```

On upgrade: wraps the old state `Chs` into `{Chs, 0}` (initializing counter to 0).
On downgrade: extracts `Chs` from `{Chs, N}`, discarding the counter.

**Example 2** (appup_cookbook.md, "Changing Code for a Special Process"): For special processes, `system_code_change/4` is used:

```erlang
system_code_change(Chs, _Module, _OldVsn, _Extra) ->
    {ok, Chs}.
```

# Relationships

## Builds Upon
- **Synchronized Code Replacement** -- State changes are performed as part of synchronized replacement.
- **gen_server** -- The most common behaviour requiring state migration.

## Enables
- None directly.

## Related
- **Application Upgrade File** -- The `update` instruction is specified in .appup files.
- **Functional Module** -- Even though callback modules are functional modules, state changes still require the `update` instruction.

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Not handling the downgrade case in `code_change/3`.
  **Correction**: The function must handle both `Vsn` (upgrade) and `{down, Vsn}` (downgrade) as the first argument. Missing the downgrade case will crash the process during a downgrade.

- **Error**: Assuming `Vsn` is a human-readable version string.
  **Correction**: `Vsn` is the value of the `-vsn` module attribute. If no `-vsn` attribute is defined, it is the beam file checksum (a large integer). Define a `-vsn` attribute for meaningful version values.

# Common Confusions

- **Confusion**: Thinking `code_change/3` is called automatically for all module changes.
  **Clarification**: `code_change/3` is only called when the .appup file uses the `{update, Module, {advanced, Extra}}` instruction. Simple `load_module` does not trigger it. The developer must explicitly specify when state transformation is needed.

# Source Reference

OTP Design Principles, "Appup Cookbook" chapter, section "Changing Internal State" (appup_cookbook.md). Also "Release Handling" chapter, section "update" (release_handling.md).

# Verification Notes

- Definition source: Directly from appup_cookbook.md "Changing Internal State" section.
- Confidence rationale: Explicitly documented with code examples for both upgrade and downgrade.
- Uncertainties: None.
- Cross-reference status: Cross-references synchronized-code-replacement, gen-server (cross-source), application-upgrade-file (new cards).
