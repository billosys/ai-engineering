---
# === CORE IDENTIFICATION ===
concept: "code_change/3 Callback"
slug: code-change

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: gen-server-callbacks
tier: advanced

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "gen_server Behaviour"
chapter_number: null
pdf_page: null
section: "Handling Other Messages"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS ===
aliases:
  - "code_change callback"
  - "hot code upgrade callback"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-server
extends: []
related:
  - gen-server-init
  - gen-server-terminate
  - release
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does a gen_server support hot code upgrades?"
  - "What is code_change/3 for?"
---

# Quick Definition

`code_change/3` is the gen_server callback invoked during a hot code upgrade to convert the server's internal state from the old code version to the new one.

# Core Definition

The gen_server Behaviour chapter describes `code_change/3` as "the final function to implement" for a gen_server callback module. It is defined as: `code_change(OldVsn, State, Extra) -> {ok, NewState}`. This callback is invoked during release handling when a running system is upgraded to a new version of the code, allowing the gen_server to transform its internal state to match the expectations of the new code.

# Prerequisites

- **gen_server** — code_change/3 is a callback of the gen_server behaviour.

# Key Properties

1. Called during hot code upgrades (release handling).
2. Receives the old version (`OldVsn`), current state, and an extra term.
3. Must return `{ok, NewState}` with the state converted for the new code version.
4. Allows state format migration between code versions without stopping the server.
5. Part of OTP's support for upgrading running systems.

# Construction / Recognition

## To Construct/Create:
1. Implement `code_change(OldVsn, State, Extra)` in the callback module.
2. Convert the state from the old format to the new format.
3. Return `{ok, NewState}`.

## To Identify/Recognize:
1. A function named `code_change/3` in a gen_server callback module.
2. Typically contains state transformation logic between versions.

# Context & Application

`code_change/3` supports Erlang/OTP's unique ability to upgrade running systems without downtime. During a release upgrade, the release handler calls `code_change/3` on each gen_server to allow it to transform its internal state to be compatible with the new code. This is part of the broader release handling mechanism described in the OTP Design Principles.

# Examples

**Example 1** (gen_server_concepts.md, "Handling Other Messages"): The skeleton of a code_change callback:
```erlang
code_change(OldVsn, State, Extra) ->
    %% Code to convert state (and more) during code change.
    ...
    {ok, NewState}.
```

# Relationships

## Builds Upon
- **gen_server** — code_change/3 is a gen_server callback.

## Enables
- No specific downstream concepts within this source.

## Related
- **gen_server:init** — init establishes initial state; code_change transforms it during upgrades
- **gen_server:terminate** — both are lifecycle callbacks
- **release** — code_change is invoked as part of release handling

## Contrasts With
- No direct contrasts in source.

# Common Errors

- **Error**: Forgetting to handle state migration when the state record format changes between versions.
  **Correction**: Always check the `OldVsn` and transform the state accordingly when the internal state structure changes.

# Common Confusions

- **Confusion**: Thinking code_change/3 is called every time the module is reloaded.
  **Clarification**: `code_change/3` is called only during structured release upgrades (via release handling), not during ad-hoc code reloading with `l(Module)` in the shell.

# Source Reference

OTP Design Principles, "gen_server Behaviour" chapter, "Handling Other Messages" section (gen_server_concepts.md). Also related to "Release Handling" chapter.

# Verification Notes

- Definition source: From gen_server_concepts.md, described briefly as "the final function to implement."
- Confidence rationale: Medium — the source provides only a brief skeleton. Full details of code_change semantics are in the release handling and gen_server reference documentation.
- Uncertainties: The source does not elaborate on when OldVsn, State, and Extra are populated or how they interact with the release handler.
- Cross-reference status: References gen-server, gen-server-init, gen-server-terminate, release (planned cards).
