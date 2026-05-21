---
# === CORE IDENTIFICATION ===
concept: Process Aliases
slug: process-aliases

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Processes"
chapter_number: null
pdf_page: null
section: "Process Aliases"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - process alias
  - alias

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-process
  - message-sending
  - monitors
extends:
  - message-sending
related:
  - process-registration
  - priority-messages
contrasts_with:
  - process-registration

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a process alias in Erlang?"
  - "How do process aliases help with request/reply patterns?"
---

# Quick Definition
A process alias is a reference-typed identifier that can be used to send messages to a process, designed primarily for request/reply scenarios. Unlike pids, an alias can be deactivated so that subsequent messages sent to it are silently dropped before reaching the message queue.

# Core Definition
The Erlang Reference Manual states that a process alias is "a term of the type reference" that can be used as the receiver identifier when sending a message. "The typical use case that process aliases were designed for is a request/reply scenario. Using a process alias when sending the reply makes it possible for the receiver of the reply to prevent the reply from reaching its message queue if the operation times out or if the connection between the processes is lost." When the alias is active, "messages will be delivered the same way as if the process identifier of the process that created the alias had been used. When the alias has been deactivated, messages sent using the alias will be dropped before entering the message queue of the receiver." (Processes chapter, "Process Aliases" section).

# Prerequisites
- **erlang-process** -- Must understand processes as message receivers
- **message-sending** -- Must understand how messages are sent and received
- **monitors** -- Aliases can be created together with monitors using the same reference

# Key Properties
1. An alias is a term of type `reference`
2. Created by calling `alias/0,1` BIFs or combined with a monitor via `monitor/3`
3. When created with a monitor, the same reference serves as both monitor reference and alias
4. An active alias delivers messages as if the process pid were used
5. A deactivated alias causes messages to be dropped before reaching the message queue
6. Messages already in the queue when deactivation occurs are NOT removed
7. Deactivated explicitly via `unalias/1` or automatically based on configured events
8. Only the creating process can create or deactivate an alias
9. Cannot look up an alias, look up the process it identifies, check if active, or check if a reference is an alias

# Construction / Recognition
## To Construct/Create:
1. Call `erlang:alias/0` or `erlang:alias/1` to create a standalone alias
2. Or pass the `{alias, _}` option to `erlang:monitor/3` to create a combined monitor+alias
3. Or pass the `{alias, _}` option via `spawn_opt/5` or `spawn_request/5`

## To Identify/Recognize:
1. An alias is a reference -- it cannot be distinguished from other references programmatically
2. There is no BIF to check if a reference is an alias or if an alias is active

# Context & Application
Process aliases solve a specific problem in request/reply communication patterns. Without aliases, when a client times out waiting for a reply, the reply may still arrive later and pollute the message queue. With aliases, the client creates an alias, sends it with the request, and deactivates the alias on timeout. Any late reply is then silently dropped. The restrictions (cannot look up, cannot check status) are "intentional design decisions relating to performance, scalability, and distribution transparency."

# Examples
**Example 1** (Processes, "Process Aliases" section): Creating an alias with automatic deactivation via monitor: "If the alias is created together with a monitor, the same reference will be used both as monitor reference and alias. Creating a monitor and an alias at the same time is done by passing the `{alias, _}` option to the `monitor/3` BIF."

**Example 2** (Processes, "Process Aliases" section): Restrictions on aliases -- "It is _not_ possible to: create an alias identifying a process other than the caller; deactivate an alias unless it identifies the caller; look up an alias; look up the process identified by an alias; check if an alias is active or not; check if a reference is an alias."

# Relationships
## Builds Upon
- **message-sending** -- Aliases provide an alternative way to address message recipients
- **monitors** -- Aliases can be created together with monitors sharing the same reference

## Enables
- **priority-messages** -- Priority aliases are a special kind of process alias

## Related
- **process-registration** -- Another mechanism for identifying processes by something other than pid

## Contrasts With
- **process-registration** -- Registration uses atoms (global per node), aliases use references (opaque, not lookupable). Registration persists until the process terminates; aliases can be deactivated independently.

# Common Errors
- **Error**: Expecting messages already in the queue to be removed when an alias is deactivated
  **Correction**: Deactivating an alias only affects future messages. Messages already in the queue remain and must be handled.

# Common Confusions
- **Confusion**: Thinking aliases are just another form of process names
  **Clarification**: Aliases are opaque references designed for the specific use case of request/reply timeout handling. They cannot be looked up, shared globally, or inspected, unlike registered names.

# Source Reference
Processes chapter, "Process Aliases" section.

# Verification Notes
- Definition source: Direct from source with extensive quoting
- Confidence rationale: High -- comprehensive section with explicit definition and design rationale
- Uncertainties: None
- Cross-reference status: All slugs verified against planned extraction
