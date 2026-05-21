---
# === CORE IDENTIFICATION ===
concept: Spawn Request
slug: spawn-request

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Processes"
chapter_number: null
pdf_page: null
section: "Signals"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS ===
aliases:
  - spawn_request
  - asynchronous spawn

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-process
  - erlang-signals
  - process-creation
extends:
  - process-creation
related:
  - process-links
  - process-monitors
  - process-aliases
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How can a process be spawned asynchronously?"
  - "What is spawn_request and how does it differ from spawn?"
  - "How does spawn_request interact with links and monitors?"
---

# Quick Definition
`spawn_request/1,2,3,4,5` is an advanced BIF that initiates asynchronous process creation by sending a `spawn_request` signal to the spawn service. Unlike `spawn/3`, which blocks until the new process exists, `spawn_request` returns a reference immediately and delivers the result as a `spawn_reply` message, enabling non-blocking remote process creation.

# Core Definition
The Erlang Reference Manual describes `spawn_request`/`spawn_reply` as a signal pair: the request signal "is sent to the spawn service which responds with the reply signal." The reply signal is either "converted into a message or dropped, depending on the reply and how the `spawn_request` signal was configured." The regular spawn BIFs (`spawn/1,2,3,4`, `spawn_link/1,2,3,4`, `spawn_monitor/1,2,3,4`) are implemented on top of `spawn_request` internally. (Processes chapter, "Sending Signals" and "Receiving Signals" sections).

The `spawn_request` BIF supports options for link, monitor, and alias creation -- allowing all of these to be set up atomically as part of the spawn operation. A pending spawn request can be abandoned using `spawn_request_abandon/1`.

# Prerequisites
- **erlang-process** -- Must understand processes to spawn them
- **erlang-signals** -- spawn_request operates through the signal mechanism
- **process-creation** -- spawn_request is an advanced variant of process creation

# Key Properties
1. Returns a reference immediately without blocking -- the actual process creation happens asynchronously
2. The spawn result is delivered as a `spawn_reply` message to the requesting process
3. Supports options for atomically creating links, monitors, and aliases along with the new process
4. Can spawn processes on remote nodes without blocking the caller
5. All regular spawn BIFs (`spawn`, `spawn_link`, `spawn_monitor`) are built on top of `spawn_request`
6. A pending request can be abandoned with `spawn_request_abandon/1`
7. The spawn service consists of multiple independently executing entities, so ordering between multiple spawn_reply signals is not preserved
8. Available in arities 1 through 5 for various levels of configuration

# Construction / Recognition
## To Construct/Create:
1. Call `spawn_request(Module, Function, Args)` for basic async spawn
2. Call `spawn_request(Node, Module, Function, Args, Options)` for full control including remote node, link, monitor, and alias options
3. Handle the reply with a `receive` matching on the returned reference

## To Abandon:
1. Call `spawn_request_abandon(ReqRef)` to abandon a pending spawn request -- any future reply will be dropped

## To Identify/Recognize:
1. The `spawn_reply` message in the mailbox indicates a spawn_request has completed
2. The reference returned by `spawn_request` matches the reference in the reply

# Context & Application
`spawn_request` is an advanced feature designed for scenarios where the caller cannot afford to block on process creation, particularly when spawning on remote nodes where the round-trip time may be significant. It is also the primitive upon which all other spawn variants are built, making it the most flexible (and most complex) spawn mechanism.

**Typical contexts:**
- Spawning processes on remote nodes without blocking
- Implementing custom spawn strategies with specific link/monitor/alias configurations
- High-performance systems that cannot tolerate blocking spawn operations
- Framework-level code that needs fine-grained control over spawn behavior

**When NOT to use:**
- For simple local spawning, use `spawn/3`, `spawn_link/3`, or `spawn_monitor/3`
- Unless you specifically need asynchronous spawn semantics, the simpler variants are preferred

# Examples
**Example 1** (Processes, "Sending Signals" section): The `spawn_request`/`spawn_reply` signal pair is listed among the core signals: "Sent due to a call to one of the `spawn/1,2,3,4`, `spawn_link/1,2,3,4`, `spawn_monitor/1,2,3,4`, `spawn_opt/2,3,4,5`, `spawn_request/1,2,3,4,5` BIFs. The request signal is sent to the spawn service which responds with the reply signal."

**Example 2** (Processes, "Receiving Signals" section): The spawn_reply handling: "Convert into a message or drop the signal, depending on the reply and how the `spawn_request` signal was configured. If the signal is converted into a message, it is also added to the message queue."

# Relationships
## Builds Upon
- **process-creation** -- spawn_request is an asynchronous extension of process creation

## Enables
Nothing directly -- it is the most advanced spawn primitive.

## Related
- **process-links** -- Links can be created atomically with spawn_request via options
- **process-monitors** -- Monitors can be created atomically with spawn_request via options
- **process-aliases** -- Aliases can be created atomically with spawn_request via `{alias, _}` option

## Contrasts With
No direct contrast -- spawn_request is the underlying primitive for all spawn variants.

# Common Errors
- **Error**: Forgetting to handle the `spawn_reply` message, leaving it in the mailbox
  **Correction**: Always receive and handle the spawn_reply message. If the spawn is no longer needed, call `spawn_request_abandon/1` to ensure the reply is dropped.

- **Error**: Assuming spawn_reply messages from multiple requests arrive in order
  **Correction**: The spawn service consists of multiple independent entities, so spawn_reply order is not guaranteed across multiple requests. Use the reference to match each reply to its request.

# Common Confusions
- **Confusion**: Thinking `spawn_request` is needed for normal process creation
  **Clarification**: For most use cases, `spawn/3`, `spawn_link/3`, or `spawn_monitor/3` are sufficient and simpler. `spawn_request` is an advanced primitive intended for non-blocking remote spawning and framework-level code.

# Source Reference
Processes chapter, "Signals" section ("Sending Signals" and "Receiving Signals" subsections), and "Process Creation" section for the list of spawn BIF variants.

# Verification Notes
- Definition source: Synthesized from multiple sections -- spawn_request is described across the signals section rather than having its own dedicated section
- Confidence rationale: Medium -- the reference manual describes the signal behavior but the full API details require consulting the erlang module documentation
- Uncertainties: Exact message format of spawn_reply and full option set are not detailed in this source chapter
- Cross-reference status: All referenced slugs correspond to existing or planned cards
