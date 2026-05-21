---
concept: Each Process Should Only Have One Role
slug: one-role-per-process
category: processes-concurrency
subcategory: processes-servers-messages
tier: intermediate
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "Processes, Servers and Messages"
chapter_number: 5
pdf_page: null
section: "5.5 Each process should only have one \"role\""
extraction_confidence: high
aliases:
  - "one role per process"
  - "client or server, not both"
  - "process roles"
prerequisites: []
extends: []
related:
  - one-process-per-concurrent-activity
  - separate-error-handling-from-normal-code
contrasts_with: []
answers_questions:
  - "Can a process be both a client and a server?"
  - "What roles can a process have in a system?"
---

# Quick Definition

A process should have only one role — for example client *or* server, supervisor *or* worker — not a combination.

# Core Definition

"As far as possible a process should only have one role, i.e. it can be a client or a server but should not combine these roles" (Programming Rules, 5.5). The source lists roles a process might have: **Supervisor** — watches other processes and restarts them on failure; **Worker** — a normal work process (can have errors); **Trusted Worker** — not allowed to have errors.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. A process has a single role.
2. Client and server roles are not combined in one process.
3. Named roles include Supervisor, Worker, and Trusted Worker.
4. A Supervisor watches and restarts; a Worker may fail; a Trusted Worker must not fail.

# Construction / Recognition

## To Apply

1. Assign each process exactly one role.
2. Split a process that acts as both client and server into two.

## To Recognize a Violation

1. A process both serves requests and acts as a client to other servers.

# Context & Application

A core process-design principle (section 5).

- **Typical contexts**: client-server architectures, supervision trees.
- **Common applications**: separating a supervisor process from the workers it restarts.

# Examples

The source enumerates the roles (Supervisor, Worker, Trusted Worker) rather than giving a code listing.

# Relationships

## Related

- **Assign exactly one parallel process to each true concurrent activity** — companion process-design rule.
- **Separate error handling and normal case code** — error recovery is a distinct role (Supervisor).

# Common Errors

- **Error**: Letting one process both serve clients and act as a client itself.
  **Correction**: Split it so each process holds a single role.

# Common Confusions

- **Confusion**: Thinking a "Trusted Worker" is just a careful Worker.
  **Clarification**: The distinction is strict — a Worker may have errors; a Trusted Worker is not allowed to.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 5.5 "Each process should only have one 'role'".

# Verification Notes

- Definition source: Direct adaptation of section 5.5.
- Confidence rationale: HIGH — the rule and the role list are stated explicitly.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
