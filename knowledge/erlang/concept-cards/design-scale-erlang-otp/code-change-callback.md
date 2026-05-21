---
# === CORE IDENTIFICATION ===
concept: Code Change Callback
slug: code-change-callback

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: behaviour-callbacks
tier: advanced

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: Francesco Cesarini & Steve Vinoski
chapter: "Release Upgrades"
chapter_number: 11
pdf_page: 336
section: "The Code to Upgrade"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - code_change
  - "code_change/3"
  - "code_change/4"
  - system_code_change

# === TYPED RELATIONSHIPS ===
prerequisites:
  - software-upgrade
  - fully-qualified-function-call
extends: []
related:
  - application-upgrade-file
  - upgrading-records
  - high-level-instructions
  - upgrading-special-processes
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the code_change callback and when is it called?"
  - "How do I perform a release upgrade?"
  - "What must I understand before performing release upgrades?"
---

# Quick Definition

The `code_change` callback is the behavior callback function that migrates a process's state when its module is upgraded or downgraded. It is invoked during a synchronized code replacement, after the new module is loaded (or, on a downgrade, before).

# Core Definition

`code_change` is a behavior callback used to update the state of the behavior (Cesarini & Vinoski, p. 340-341, pdf p. 336). It takes three arguments when called within an event handler or a generic server, and four when called from within a finite state machine. The first argument, `Vsn`, is the version of the old module being upgraded from (or `{down, Vsn}` when downgrading); for FSMs a `State` argument is also passed, containing the FSM state at upgrade time; the final arguments are the loop data and any `Extra` argument passed in the upgrade instructions. On success it returns `{ok, NewState, NewLoopData}` (FSM) or `{ok, NewLoopData}` (server/event handler); returning `{error, Reason}` causes the upgrade to fail and the node to restart the previous version (for servers and FSMs).

# Prerequisites

- **Software upgrade** — `code_change` runs as part of an upgrade; the upgrade concept comes first.
- **Fully qualified function call** — `code_change` is reached via a fully qualified call during the upgrade.

# Key Properties

1. Behavior callback for migrating process state during upgrade/downgrade.
2. `code_change/4` for FSMs (`Vsn, State, LoopData, Extra`); `code_change/3` for generic servers and event handlers (`Vsn, LoopData, Extra`).
3. `Vsn` is the version being upgraded from, or `{down, Vsn}` for a downgrade.
4. `State` is passed only to FSMs and holds the state at upgrade time.
5. Returns `{ok, NewState, NewLoopData}` (FSM) or `{ok, NewLoopData}` (server/event handler).
6. `{error, Reason}` from a server/FSM fails the upgrade and restarts the previous version.
7. For event handlers, returning anything other than `{ok, NewLoopData}` or terminating abnormally removes the handler but does not revert the node.
8. On an upgrade `code_change` runs after loading the new module; on a downgrade it runs before — unless `ModType` is set to `static`.
9. When versions do not matter, use wildcards for `Vsn`; for modules without a `-vsn`, use the md5 checksum.

# Construction / Recognition

## To Implement code_change:
1. Export `code_change/3` (server/event handler) or `code_change/4` (FSM).
2. Match on `Vsn` to handle upgrades, and on `{down, Vsn}` to handle downgrades.
3. Adapt `LoopData`/`State` (and any records, schemas, protocols) to the new format.
4. Return `{ok, NewState, NewLoopData}` or `{ok, NewLoopData}`.

## To Recognize It:
1. A `code_change/3` or `code_change/4` clause in a behavior callback module.
2. Compiler warning `undefined callback function code_change/4` when the callback is missing.

# Context & Application

- **Typical contexts**: Migrating behavior state across versions during a release upgrade.
- **Common applications**: Adapting loop data, database schemas, protocols, process flags; even manipulating mailbox messages.
- **Historical/stylistic notes**: Adding `code_change` clauses that simply return the original state avoids the undefined-function runtime error when a process is on an old version.

# Examples

**Example 1** (p. 341): The coffee FSM's `code_change/4` handling both upgrade and downgrade:

```erlang
code_change('1.0', State, LoopData, _Extra) ->
 {ok, State, LoopData};
code_change({down, '1.0'}, service, LoopData, _Extra) ->
 hw:reboot(),
 hw:display("Make Your Selection", []),
 {ok, selection, LoopData};
code_change({down, '1.0'}, payment, {_Type, _Price, Paid}, _Extra) ->
 hw:return_change(Paid),
 hw:display("Make Your Selection", []),
 {ok, selection, {}};
code_change({down, '1.0'}, State, LoopData, _Extra) ->
 {ok, State, LoopData}.
```

**Example 2** (p. 342): The `code_change/3` for upgrading a record format:

```erlang
code_change('1.0', {freq, Free, Alloc}, _Extra) ->
 {ok, {freq, Free, Alloc, []}};
code_change({down, '1.0'}, {freq, Free, Alloc, Blocked}, _Extra) ->
 {ok, {freq, Free++Blocked, Alloc}}.
```

# Relationships

## Builds Upon
- **Software upgrade** — `code_change` is the state-migration step of an upgrade.
- **Fully qualified function call** — `code_change` is invoked via a fully qualified call.

## Related
- **Application upgrade file** — `{advanced, Extra}` instructions trigger `code_change`.
- **Upgrading records** — `code_change` handles record-format changes via tuple representation.
- **High-level instructions** — The `update` instruction with `{advanced, Extra}` invokes `code_change`.
- **Upgrading special processes** — Special processes use `system_code_change/4` instead.

# Common Errors

- **Error**: Omitting `code_change` clauses and triggering an upgrade.
  **Correction**: Provide `code_change` clauses (even ones that just return the state) to avoid the undefined-function runtime error.

- **Error**: Forgetting downgrade clauses for `{down, Vsn}`.
  **Correction**: Handle `{down, Vsn}` explicitly; a downgrade reboots and starts the old version, so revert any persistent values.

# Common Confusions

- **Confusion**: Thinking `code_change` always has the same arity.
  **Clarification**: It is `code_change/4` for FSMs and `code_change/3` for generic servers and event handlers.

- **Confusion**: Believing `code_change` always runs after the new module loads.
  **Clarification**: On an upgrade it runs after loading; on a downgrade it runs before loading — unless `ModType` is `static`.

# Source Reference

Chapter 11: Release Upgrades, section "The Code to Upgrade," pages 340-341 (pdf p. 336). See also "Upgrading Records" (p. 342) and "Upgrading Special Processes" (`system_code_change/4`, p. 351).

# Verification Notes

- Definition source: Direct adaptation of pp. 340-341.
- Confidence rationale: HIGH — the source explicitly specifies the callback's signatures, arguments, and return values.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
