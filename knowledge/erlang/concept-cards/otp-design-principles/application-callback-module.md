---
# === CORE IDENTIFICATION ===
concept: Application Callback Module
slug: application-callback-module

# === CLASSIFICATION ===
category: applications-releases
subcategory: application-structure
tier: intermediate

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "Applications"
chapter_number: null
pdf_page: null
section: "Application Callback Module"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "application callback"
  - "application behaviour module"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - application
  - behaviour
  - callback-module
  - supervision-tree
extends:
  - callback-module
related:
  - application-resource-file
  - application-master
  - supervisor-behaviour
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the application callback module relate to the application master?"
  - "How do I create an OTP application?"
---

# Quick Definition

An application callback module implements the `application` behaviour, defining `start/2` and `stop/1` callbacks that describe how to start the supervision tree and clean up when the application stops.

# Core Definition

According to the OTP Design Principles "Applications" chapter: "How to start and stop the code for the application, including its supervision tree, is described by two callback functions: `start(StartType, StartArgs) -> {ok, Pid} | {ok, Pid, State}` and `stop(State)`." The callback module is specified by the `mod` key in the application resource file and is invoked by the application master during application lifecycle events.

# Prerequisites

- **Application** — the callback module exists to manage an application's lifecycle.
- **Behaviour** — the callback module implements the `application` behaviour.
- **Callback Module** — this is a specific kind of callback module.
- **Supervision Tree** — `start/2` is expected to create the supervision tree.

# Key Properties

1. Implements the `application` behaviour with `-behaviour(application).`
2. Exports `start/2` — called when starting the application; must create the supervision tree and return `{ok, Pid}` or `{ok, Pid, State}`.
3. Exports `stop/1` — called after the application has been stopped; performs cleanup. The `State` argument defaults to `[]`.
4. `StartType` is usually the atom `normal`, but can be `{failover, Node}` or `{takeover, Node}` for distributed applications.
5. `StartArgs` is defined by the `mod` key in the .app file.
6. The application master calls `start/2` to begin the application and `stop/1` after shutdown.

# Construction / Recognition

## To Construct/Create:
1. Create a module and declare `-behaviour(application).`
2. Export `start/2` and `stop/1`.
3. In `start/2`, start the top supervisor (e.g., call `my_sup:start_link()`).
4. Return `{ok, Pid}` where `Pid` is the top supervisor's pid.
5. In `stop/1`, perform any necessary cleanup and return `ok`.
6. Reference this module in the .app file's `mod` key.

## To Identify/Recognize:
1. Module declares `-behaviour(application).`
2. Exports `start/2` and `stop/1` callback functions.
3. Referenced in the `mod` key of an .app file.

# Context & Application

The application callback module is the entry point for an OTP application's lifecycle. When `application:start/1` is called, the application master invokes the callback module's `start/2` function, which is expected to start the top-level supervisor. This is the bridge between the application framework and the application's supervision tree.

# Examples

**Example 1** (applications.md, "Application Callback Module"): The `ch_app` callback module for the channel allocator supervision tree:
```erlang
-module(ch_app).
-behaviour(application).

-export([start/2, stop/1]).

start(_Type, _Args) ->
    ch_sup:start_link().

stop(_State) ->
    ok.
```

**Example 2** (applications.md, "Application Callback Module"): The `start/2` callback receives `StartType` (usually `normal`) and `StartArgs` defined by the `mod` key. When called as `ch_app:start(normal, [])`, it starts the `ch_sup` supervisor.

# Relationships

## Builds Upon
- **Application** — the callback module is a required part of a non-library application.
- **Behaviour** — implements the `application` behaviour.
- **Callback Module** — this is a specific instance of the callback module pattern.
- **Supervision Tree** — `start/2` creates the supervision tree.

## Enables
- **Application Master** — the application master calls the callback module's functions.
- **Failover** — the `StartType` argument communicates failover events to the callback.
- **Takeover** — the `StartType` argument communicates takeover events to the callback.

## Related
- **Application Resource File** — the .app file's `mod` key specifies the callback module and start arguments.
- **Supervisor Behaviour** — `start/2` typically delegates to a supervisor's `start_link`.

## Contrasts With
- No direct contrasts in source.

# Common Errors

- **Error**: Not returning `{ok, Pid}` from `start/2`.
  **Correction**: Always return the pid of the top supervisor as `{ok, Pid}` or `{ok, Pid, State}`.

- **Error**: Doing heavy initialization in `stop/1` instead of cleanup.
  **Correction**: `stop/1` is called after the application has already been stopped (supervision tree terminated). It should only perform final cleanup.

# Common Confusions

- **Confusion**: Thinking `stop/1` shuts down the supervision tree.
  **Clarification**: The actual stopping of the application (shutting down the supervision tree) is handled automatically. `stop/1` is called after that, for any necessary cleaning up.

# Source Reference

OTP Design Principles, "Applications" chapter, "Application Callback Module" section (applications.md).

# Verification Notes

- Definition source: Directly from applications.md "Application Callback Module" section, with code example quoted.
- Confidence rationale: High — explicitly defined with callback signatures, semantics, and a concrete example.
- Uncertainties: None.
- Cross-reference status: References application, behaviour, callback-module, supervision-tree, application-resource-file, application-master.
