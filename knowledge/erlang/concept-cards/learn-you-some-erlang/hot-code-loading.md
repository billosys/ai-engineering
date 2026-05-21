---
concept: Hot Code Loading
slug: hot-code-loading
category: production-ops
subcategory: code-upgrades
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Leveling Up in the Process Quest"
chapter_number: 22
pdf_page: null
section: "The Hiccups of Appups and Relups"
extraction_confidence: high
aliases:
  - "code hot-loading"
  - "live code upgrade"
  - "code reloading"
  - "hot code swapping"
prerequisites:
  - gen-server
  - otp-application
  - supervisor
extends: []
related:
  - appup
  - relup
  - code-change-callback
contrasts_with: []
answers_questions:
  - "What is hot code loading?"
  - "Why is live code upgrade dangerous?"
  - "How does Erlang upgrade running code safely?"
---

# Hot Code Loading

## Quick Definition

Hot code loading is the act of replacing a module's code in a running Erlang VM without stopping the system. Doing it the simple way is easy; doing it safely without crashing processes is much harder.

## Core Definition

Hot code loading lets you recompile a module, make a fully qualified function call, and have running processes pick up the new version. The book opens Chapter 22 stating "Code hot-loading is simple in Erlang... However, doing it the right (and safe) way is much more difficult" (Ch. 22, "The Hiccups of Appups and Relups"). The danger arises because live upgrades can change a module's interface, internal data structures, function names, or records (which are tuples), each of which can cause processes still holding old data or expecting old message formats to crash with no matching clause. Safe hot code loading therefore requires freezing processes, changing their code, and resuming them — handled inside OTP by the `sys` and `release_handler` modules (Ch. 22).

## Prerequisites

- **Gen-server** — The classic upgrade hazard the book describes is an incompatible change to a `gen_server`'s `handle_cast/2` between versions
- **Otp-application** — Code upgrades in practice are organized at the application and release level (appups/relups)
- **Supervisor** — Suspending processes for upgrade requires walking the supervision tree to find all children to suspend

## Key Properties

1. The naive technique is a fully qualified call (`?MODULE:loop(N)`) triggered by a hidden `update` message, so a running loop jumps to the newest loaded code
2. The naive technique fails when the function's arguments change, because in-flight messages may be processed by code reloaded mid-loop
3. Generic loops (where the module is a variable) cannot be hot-upgraded safely with ad hoc tricks at all
4. Safe upgrades require three OTP steps: `sys:suspend(PidOrName)`, `sys:change_code(PidOrName, Mod, OldVsn, Extra)`, then `sys:resume(PidOrName)`
5. The Erlang VM keeps two versions of a module loaded; processes still running old code are killed when a third version loads if they have not upgraded
6. Code upgrades risk crashing processes that change records, message interfaces, or internal state shape between versions

## Construction / Recognition

### To do a safe single-process upgrade manually

1. Suspend the process with `sys:suspend(PidOrName)`
2. Force the process to update via `sys:change_code(PidOrName, Mod, OldVsn, Extra)`
3. Resume it with `sys:resume(PidOrName)`

### To upgrade systematically

Use appups and relups rather than ad hoc `sys` scripts (see `appup`, `relup`).

## Context & Application

Hot code loading is a flagship Erlang feature that supports systems that must never be shut down (originally telephone switches). The book is emphatic that if you can avoid live upgrades and instead do rolling restarts of VMs, you should — relups are a "do or die" tool (Ch. 22, "The Ninth Circle of Erl").

## Examples

**Example** (Ch. 22): A `gen_server` whose `handle_cast/2` is changed to take a different argument; loading it on the production VM produces a flood of error reports because old and new `handle_cast` functions are incompatible and no clause matches.

**Example** (Ch. 22): The naive update loop —

```erlang
loop(N) ->
    receive
        update -> ?MODULE:loop(N);
        ...
    end.
```

works only when `loop/1`'s arguments are unchanged; otherwise it must delegate to a `code_change/1` function instead.

## Relationships

### Builds Upon

- **Gen-server** — Behaviour processes are the typical subject of hot upgrades

### Enables

- **Appup** — Per-application upgrade instructions automate hot loading
- **Relup** — Per-release upgrade instructions orchestrate it across applications

### Related

- **Code-change-callback** — The OTP callback invoked during a controlled upgrade

### Contrasts With

- **Rolling-upgrade** — Restarting VMs with new code instead of swapping code in place

## Common Errors

- **Error**: Hot-loading a module with a changed `handle_cast`/`handle_call` argument shape on a live system.
  **Correction**: Use a controlled `sys:change_code` / appup `{update, Mod, {advanced, Extra}}` upgrade so the process suspends and migrates its state.
- **Error**: Leaving a process blocked (e.g. in `gen_tcp:accept`) so it cannot process an upgrade message.
  **Correction**: Keep processes responsive; blocked processes get killed when old code is purged.

## Common Confusions

- **Confusion**: Believing hot code loading guarantees zero downtime automatically.
  **Clarification**: Only the mechanism is provided; unsafe interface or state changes still crash processes.
- **Confusion**: Thinking a fully qualified call alone makes upgrades safe.
  **Clarification**: It only jumps to new code; it does not migrate state or coordinate timing with in-flight messages.

## Source Reference

Chapter 22, "Leveling Up in the Process Quest," sections "The Hiccups of Appups and Relups" and "The Ninth Circle of Erl." See the `loop/1` code listings and the `sys:suspend`/`sys:change_code`/`sys:resume` discussion.

## Verification Notes

- Definition: Direct adaptation from the chapter opening and "The Hiccups of Appups and Relups"
- Key Properties: Items 1-5 explicit in source; item 6 synthesized from the chapter's danger discussion
- Confidence: HIGH — the chapter explicitly explains the mechanism and its hazards
- Cross-references: `appup`, `relup`, `code-change-callback` are planned cards in this chapter; `gen-server`, `supervisor`, `otp-application` are shared slugs
