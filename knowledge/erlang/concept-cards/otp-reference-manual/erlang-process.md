---
# === CORE IDENTIFICATION ===
concept: Erlang Process
slug: erlang-process

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
section: "Processes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - process
  - lightweight process

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - process-creation
  - process-registration
  - process-termination
  - message-sending
  - message-receiving
  - links
  - monitors
  - process-dictionary
contrasts_with:
  - erlang-port

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an Erlang process?"
  - "What must I understand before working with Erlang processes?"
---

# Quick Definition
An Erlang process is a lightweight, independently executing entity with its own memory that grows and shrinks dynamically. Erlang is designed for massive concurrency through these processes, which have a small memory footprint, are fast to create and terminate, and incur low scheduling overhead.

# Core Definition
The Erlang Reference Manual states: "Erlang is designed for massive concurrency. Erlang processes are lightweight (grow and shrink dynamically) with a small memory footprint, fast to create and terminate, and the scheduling overhead is low." (Processes chapter, "Processes" section). Processes are the fundamental unit of concurrency in Erlang. Each process has its own memory, a message queue for receiving signals, and a process dictionary. Processes communicate exclusively through asynchronous signal passing.

# Prerequisites
This is a foundational concept with no prerequisites within this source.

# Key Properties
1. Lightweight -- processes grow and shrink dynamically in memory
2. Small memory footprint compared to OS threads
3. Fast to create and terminate
4. Low scheduling overhead
5. Each process has its own isolated memory (no shared state)
6. Each process has a message queue for receiving messages
7. Each process has a process dictionary (process-local key-value storage)
8. Processes communicate through asynchronous signals
9. Each process is identified by a unique process identifier (pid)

# Construction / Recognition
## To Construct/Create:
1. Call one of the `spawn` BIF variants: `spawn/1,2,3,4`, `spawn_link/1,2,3,4`, `spawn_monitor/1,2,3,4`, `spawn_opt/2,3,4,5`, or `spawn_request/1,2,3,4,5`
2. The new process starts executing in the specified function with the given arguments

## To Identify/Recognize:
1. A process is identified by its pid (process identifier)
2. A process can optionally be registered under an atom name
3. Use `self()` to get the pid of the current process
4. Use `is_process_alive/1` to check if a process is alive

# Context & Application
Processes are the central abstraction in Erlang's concurrency model. Unlike threads in most languages, Erlang processes share no state and can only communicate via message passing. This isolation makes concurrent programs easier to reason about and enables the "let it crash" philosophy central to OTP's fault-tolerance model. The Erlang VM (BEAM) can manage millions of processes efficiently.

**Typical contexts:**
- Concurrent request handling in servers
- Supervision trees for fault tolerance
- Actor-model-style message-passing architectures
- Isolating failure domains

# Examples
**Example 1** (Processes, "Process Creation" section): A process is created by calling `spawn(Module, Name, Args) -> pid()`, where `Module` and `Name` are atoms and `Args` is the argument list. The new process starts executing in `Module:Name(Arg1,...,ArgN)`.

# Relationships
## Builds Upon
This is a foundational concept; it does not build upon other concepts.

## Enables
- **process-creation** -- Process creation is how new processes come into existence
- **message-sending** -- Processes communicate by sending signals/messages
- **links** -- Processes can be linked for error propagation
- **monitors** -- Processes can monitor each other unidirectionally
- **process-dictionary** -- Each process has its own dictionary

## Related
- **process-registration** -- Processes can be registered under names
- **process-termination** -- How processes end
- **erlang-signals** -- The mechanism for all inter-process communication

## Contrasts With
- **erlang-port** -- Ports provide communication with external programs, while processes are internal Erlang execution units

# Common Errors
- **Error**: Attempting to share memory or state between processes directly
  **Correction**: Erlang processes share no memory. All data exchange must happen through message passing. Data sent in messages is copied between process heaps.

# Common Confusions
- **Confusion**: Thinking Erlang processes are OS threads or processes
  **Clarification**: Erlang processes are managed by the BEAM VM scheduler, not the OS. They are far lighter than OS threads (typically starting at a few hundred bytes of memory) and the VM can handle millions of them.

# Source Reference
Processes chapter, "Processes" section. The definition and key properties are from the opening paragraph.

# Verification Notes
- Definition source: Direct from source, opening paragraph of the Processes chapter
- Confidence rationale: High -- explicit definition with clear terminology
- Uncertainties: None
- Cross-reference status: All related slugs correspond to planned cards in this extraction
