---
concept: Message Sending Cost
slug: message-sending-cost
category: process-management
subcategory: null
tier: foundational
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Processes"
chapter_number: null
pdf_page: null
section: "Sending Messages"
extraction_confidence: high
aliases:
  - "message passing cost"
  - "inter-process message copying"
prerequisites: []
extends: []
related:
  - erlang-process-creation
  - loss-of-sharing
  - literal-pool
  - receive-optimization
contrasts_with: []
answers_questions:
  - "What data is copied when sending messages between Erlang processes?"
  - "What are the exceptions to message copying on the same node?"
  - "How does message sending differ between local and remote nodes?"
---

# Quick Definition

All data in messages sent between Erlang processes is copied, with two exceptions on the same node: refc binaries (reference-counted binaries larger than 64 bytes) and literals are passed by reference rather than copied.

# Core Definition

All data in messages sent between Erlang processes is copied, except for refc binaries and literals on the same Erlang node. When a message is sent to a process on another Erlang node, it is first encoded to the Erlang External Format before being sent through a TCP/IP socket. The receiving Erlang node decodes the message and distributes it to the correct process (Ericsson/OTP Team, "Processes" chapter, "Sending Messages" section).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. All data in inter-process messages is copied by default
2. Refc binaries (reference-counted, large binaries) are NOT copied on the same node -- only the reference is passed
3. Literals (constants from the literal pool) are NOT copied on the same node -- only the reference is passed
4. For remote (inter-node) messages, ALL data is copied: first encoded to Erlang External Format, sent via TCP/IP, then decoded
5. The copying behavior means each process has its own isolated heap -- no shared mutable state

# Construction / Recognition

## To Minimize Message Copying Cost

1. When sending large data, prefer refc binaries (>64 bytes) which are passed by reference on the same node
2. Use literal terms from the module's literal pool when possible -- they are not copied
3. Be aware that shared subterms in a message will be flattened (see loss-of-sharing)
4. For cross-node communication, minimize message size since all data must be serialized

# Context & Application

Message copying is fundamental to Erlang's concurrency model. Each process has its own heap, and message passing copies data between heaps. This provides process isolation (no shared mutable state) and enables per-process garbage collection, but at the cost of copying overhead.

**Typical contexts:**

- Designing message protocols between processes
- Deciding what data to include in messages vs. storing in ETS or persistent_term
- Performance tuning of high-throughput message passing systems
- Understanding why large binary passing is efficient (refc binaries)

# Examples

**Example** (Processes chapter, "Sending Messages" section): The source states the copying rule concisely:

> All data in messages sent between Erlang processes is copied, except for refc binaries and literals on the same Erlang node.

**Example** (cross-node sending): When sending to another node:

> When a message is sent to a process on another Erlang node, it is first encoded to the Erlang External Format before being sent through a TCP/IP socket. The receiving Erlang node decodes the message and distributes it to the correct process.

# Relationships

## Related

- **erlang-process-creation** -- Processes communicate exclusively through message passing
- **loss-of-sharing** -- Shared subterms within a message are flattened during copying
- **literal-pool** -- Literals are one of the two exceptions to the message-copying rule
- **receive-optimization** -- The receiving side of message passing can be optimized

# Common Errors

- **Error**: Sending large binaries as iolists when a single refc binary would avoid copying
  **Correction**: Prefer sending data as a single binary >64 bytes to take advantage of reference-counted binary sharing on the same node

- **Error**: Assuming that data structures with shared subterms will retain their compact representation after being sent
  **Correction**: Sharing is lost when copying; a 22-word structure with sharing can become 4094 words after sending (see loss-of-sharing)

# Common Confusions

- **Confusion**: Believing all binaries are passed by reference
  **Clarification**: Only refc binaries (>64 bytes) are passed by reference. Heap binaries (<=64 bytes) are copied like other terms

- **Confusion**: Thinking message copying is a design flaw
  **Clarification**: Message copying is intentional -- it provides process isolation, prevents shared mutable state, and enables independent per-process garbage collection

- **Confusion**: Assuming literals are always copied
  **Clarification**: Literals on the same node are NOT copied in messages. However, they ARE copied when inserted into ETS tables, and they are copied to process heaps when the owning module is unloaded

# Source Reference

"Processes" chapter, "Sending Messages" section. Brief section covering copying semantics for local and remote message passing.

# Verification Notes

- Definition: Directly quoted from source, paragraph 1 of "Sending Messages" section
- The two exceptions (refc binaries and literals) are explicitly named in the source
- Cross-node encoding/decoding process is directly from source text
- Confidence: HIGH -- explicit, concise definition in official documentation
- Cross-references: Source itself links to binaryhandling.md for refc_binary and eff_guide_processes.md for literal-pool
- Uncertainties: None
