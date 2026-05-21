---
# === CORE IDENTIFICATION ===
concept: Pid
slug: pid

# === CLASSIFICATION ===
category: data-types
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Data Types"
chapter_number: null
pdf_page: null
section: "Pid"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - process identifier

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - erlang-term
  - reference
  - port-identifier
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an Erlang term?"
---

# Quick Definition
A pid (process identifier) is a data type that uniquely identifies an Erlang process among all processes alive on connected nodes. Pids are used to send signals and messages to processes.

# Core Definition
The Erlang Reference Manual states: "Pid is an abbreviation for process identifier. Each process has a Pid which identifies the process. Pids are unique among processes that are alive on connected nodes. However, a Pid of a terminated process may be reused as a Pid for a new process after a while." Pids are obtained via `self/0` (current process), `spawn/3` (return value), or `spawn_request/5` (via message). They are typically used to send signals to processes. The `is_pid/1` BIF tests whether a term is a pid (Data Types, "Pid" section).

# Prerequisites
This is a foundational concept with no prerequisites within this source.

# Key Properties
1. Uniquely identifies a process among alive processes on connected nodes
2. A terminated process's pid may be reused after a while
3. Obtained via `self/0` (calling process), or as spawn return value/message
4. Typically used when sending signals or messages to a process
5. Tested with `is_pid/1` BIF
6. Printed representation: `<X.Y.Z>` (e.g., `<0.58.0>`)

# Construction / Recognition
## To Construct/Create:
1. Get current process pid: `self()`
2. Spawn a new process: `Pid = spawn(Module, Function, Args)`
3. Use `spawn_request/5` and receive the pid via message

## To Identify/Recognize:
1. Use `is_pid/1` BIF
2. Pids print as `<X.Y.Z>` format

# Context & Application
Pids are central to Erlang's concurrency model. Every process has a pid, and message passing between processes requires knowing the recipient's pid. Pids are used for:
- Sending messages: `Pid ! Message`
- Monitoring processes: `erlang:monitor(process, Pid)`
- Linking processes: `link(Pid)`
- Registering named processes: `register(Name, Pid)`

# Examples
**Example 1** (Data Types, "Pid" section):
```erlang
-module(m).
-export([loop/0]).

loop() ->
    receive
        who_are_you ->
            io:format("I am ~p~n", [self()]),
            loop()
    end.

1> P = spawn(m, loop, []).
<0.58.0>
2> P ! who_are_you.
I am <0.58.0>
who_are_you
```

# Relationships
## Builds Upon
This is a foundational type with no prerequisites.

## Enables
No direct dependents within this extraction scope.

## Related
- **erlang-term** -- Pids are a kind of term
- **reference** -- References are unique values like pids, but serve different purposes
- **port-identifier** -- Ports are another kind of identifier for external interfaces

## Contrasts With
No direct contrasts within this source.

# Common Errors
- **Error**: Storing a pid and assuming it always refers to the same process
  **Correction**: A pid of a terminated process may be reused for a new process. Use monitors to detect process termination.

# Common Confusions
- **Confusion**: Assuming pids are globally unique forever
  **Clarification**: Pids are unique among *alive* processes on connected nodes. After termination, a pid may eventually be reused.

# Source Reference
Data Types chapter, "Pid" section. References "Processes" chapter for more details.

# Verification Notes
- Definition source: Direct quote from source
- Confidence rationale: High -- explicit definition with example
- Uncertainties: None
- Cross-reference status: All slugs correspond to planned cards
