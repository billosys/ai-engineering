---
# === CORE IDENTIFICATION ===
concept: Process Registration
slug: process-registration

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
section: "Registered Processes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - registered process
  - name registration

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-process
  - process-creation
extends: []
related:
  - message-sending
  - process-aliases
contrasts_with:
  - process-aliases

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I address a process by name instead of pid?"
  - "What are the BIFs for registering processes in Erlang?"
---

# Quick Definition
Process registration allows an Erlang process to be addressed by a symbolic atom name instead of its pid. The name is automatically unregistered when the process terminates.

# Core Definition
The Erlang Reference Manual states: "Besides addressing a process by using its pid, there are also BIFs for registering a process under a name. The name must be an atom and is automatically unregistered if the process terminates." (Processes chapter, "Registered Processes" section). Three BIFs are provided for name registration: `register/2`, `registered/0`, and `whereis/1`.

# Prerequisites
- **erlang-process** -- Must understand what a process is
- **process-creation** -- A process must exist before it can be registered

# Key Properties
1. The registered name must be an atom
2. The name is automatically unregistered when the process terminates
3. Only one process can be registered under a given name at a time
4. `register(Name, Pid)` associates a name with a process
5. `registered/0` returns a list of all registered names
6. `whereis(Name)` returns the pid registered under a name, or `undefined`
7. Registered names are local to each node (not distributed)

# Construction / Recognition
## To Construct/Create:
1. Create a process using any spawn variant
2. Call `register(Name, Pid)` where `Name` is an atom and `Pid` is the process identifier

## To Identify/Recognize:
1. Call `whereis(Name)` to look up the pid for a registered name
2. Call `registered()` to list all registered names on the current node

# Context & Application
Process registration is essential for creating well-known services that other processes need to find by name rather than passing pids around. OTP supervisors, gen_servers, and other behaviours commonly register under names. Since registered names are local to a node, distributed systems must specify the node when sending messages to registered processes on remote nodes using the `{Name, Node} ! Message` syntax.

# Examples
**Example 1** (Processes, "Registered Processes" section): The source provides a table of name registration BIFs:

| BIF | Description |
|-----|-------------|
| `register(Name, Pid)` | Associates the name `Name`, an atom, with the process `Pid`. |
| `registered/0` | Returns a list of names that have been registered using `register/2`. |
| `whereis(Name)` | Returns the pid registered under `Name`, or `undefined` if the name is not registered. |

# Relationships
## Builds Upon
- **erlang-process** -- Registration provides an alternative way to identify a process
- **process-creation** -- A process must be created before it can be registered

## Enables
- **message-sending** -- Messages can be sent to registered names instead of pids

## Related
- **process-aliases** -- Another mechanism for identifying processes in message sending

## Contrasts With
- **process-aliases** -- Aliases are references (not atoms), can be deactivated without terminating the process, and are designed for request/reply scenarios rather than well-known services

# Common Errors
- **Error**: Trying to register two processes under the same name
  **Correction**: A name can only be associated with one process at a time. Unregister the old process first or use a different name.

# Common Confusions
- **Confusion**: Assuming registered names are global across all nodes
  **Clarification**: Registered names are local to each node. For global name registration, use the `global` module or specify `{Name, Node}` for remote sends.

# Source Reference
Processes chapter, "Registered Processes" section.

# Verification Notes
- Definition source: Direct from source
- Confidence rationale: High -- explicit definition with BIF table
- Uncertainties: None
- Cross-reference status: All slugs verified against planned extraction
