---
# === CORE IDENTIFICATION ===
concept: Process Creation
slug: process-creation

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Processes"
chapter_number: null
pdf_page: null
section: "Process Creation"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - spawning
  - spawn

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-process
extends: []
related:
  - links
  - monitors
  - process-registration
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create and spawn a new Erlang process?"
  - "What are the different spawn variants in Erlang?"
---

# Quick Definition
Process creation in Erlang is done by calling one of the `spawn` BIF variants, which creates a new lightweight process and returns its pid. The new process begins executing the specified function with the given arguments.

# Core Definition
The Erlang Reference Manual states: "A process is created by calling `spawn()`" and "`spawn()` creates a new process and returns the pid." The basic form is `spawn(Module, Name, Args) -> pid()` where `Module` and `Name` are atoms and `Args` is a list of arguments. "The new process starts executing in `Module:Name(Arg1,...,ArgN)` where the arguments are the elements of the (possibly empty) `Args` argument list." (Processes chapter, "Process Creation" section).

# Prerequisites
- **erlang-process** -- Must understand what a process is before creating one

# Key Properties
1. `spawn/1,2,3,4` creates a new process and returns its pid
2. `spawn_link/1,2,3,4` atomically creates a process and establishes a link
3. `spawn_monitor/1,2,3,4` atomically creates a process and establishes a monitor
4. `spawn_opt/2,3,4,5` creates a process with additional options
5. `spawn_request/1,2,3,4,5` provides asynchronous process creation
6. The new process starts executing the specified function immediately
7. The spawned process is independent of the spawning process (unless linked)

# Construction / Recognition
## To Construct/Create:
1. Call `spawn(Module, Name, Args)` with the module, function name, and argument list
2. Or use `spawn(Fun)` with a fun (closure) for simpler cases
3. Use `spawn_link/N` if you want to link to the new process atomically
4. Use `spawn_monitor/N` if you want to monitor the new process atomically
5. Use `spawn_opt/N` for additional options (e.g., setting priority, heap size)

## To Identify/Recognize:
1. Any call to a `spawn*` BIF is a process creation
2. The return value is a pid (process identifier)

# Context & Application
Process creation is the most fundamental operation in concurrent Erlang programming. Because processes are lightweight, it is idiomatic to spawn processes liberally -- one per connection, one per request, one per task. The atomic variants (`spawn_link`, `spawn_monitor`) are preferred when fault tolerance is needed, as they prevent race conditions between creating the process and establishing the supervision relationship.

# Examples
**Example 1** (Processes, "Process Creation" section): The basic spawn call:
```erlang
spawn(Module, Name, Args) -> pid()
  Module = Name = atom()
  Args = [Arg1,...,ArgN]
    ArgI = term()
```

**Example 2** (Processes, "Process Creation" section): The available spawn BIF variants listed in the source:
- `spawn/1,2,3,4`
- `spawn_link/1,2,3,4`
- `spawn_monitor/1,2,3,4`
- `spawn_opt/2,3,4,5`
- `spawn_request/1,2,3,4,5`

# Relationships
## Builds Upon
- **erlang-process** -- Process creation brings new processes into existence

## Enables
- **process-registration** -- A created process can be registered under a name
- **message-sending** -- Once created, processes can exchange messages
- **links** -- `spawn_link` atomically creates a link with the new process
- **monitors** -- `spawn_monitor` atomically creates a monitor on the new process

## Related
- **process-termination** -- The counterpart to process creation

## Contrasts With
No direct contrasts.

# Common Errors
- **Error**: Using `spawn/3` followed by `link/1` instead of `spawn_link/3` when a link is needed
  **Correction**: Use `spawn_link/3` to atomically create the process and the link. Separate `spawn` + `link` has a race condition where the process could terminate before the link is established.

# Common Confusions
- **Confusion**: Believing `spawn` blocks until the new process finishes
  **Clarification**: `spawn` returns immediately with the pid of the new process. The new process executes concurrently.

# Source Reference
Processes chapter, "Process Creation" section.

# Verification Notes
- Definition source: Direct from source
- Confidence rationale: High -- explicit definition with clear BIF signatures
- Uncertainties: None
- Cross-reference status: All slugs verified against planned extraction
