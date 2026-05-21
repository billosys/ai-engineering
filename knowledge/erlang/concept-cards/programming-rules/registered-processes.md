---
concept: Registered Processes
slug: registered-processes
category: processes-concurrency
subcategory: processes-servers-messages
tier: intermediate
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "Processes, Servers and Messages"
chapter_number: 5
pdf_page: null
section: "5.3 Registered processes"
extraction_confidence: high
aliases:
  - "registered process"
  - "process registration"
  - "register a process with the module name"
prerequisites: []
extends: []
related:
  - implement-process-in-one-module
  - module-names
contrasts_with: []
answers_questions:
  - "What name should a registered process be given?"
  - "Which processes should be registered?"
---

# Quick Definition

Register a process under the same name as its module, and only register processes that are meant to live a long time.

# Core Definition

"Registered processes should be registered with the same name as the module. This makes it easy to find the code for a process" (Programming Rules, 5.3). The rule adds: only register processes that should live a long time.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. A registered process's name matches the name of its implementing module.
2. The matching name makes the process's code easy to locate.
3. Only long-lived processes are registered.

# Construction / Recognition

## To Apply

1. When registering a process, use its module's name as the registered name.
2. Register only long-lived processes; leave short-lived ones unregistered.

## To Recognize a Violation

1. A registered process's name differs from its module name, or a short-lived process is registered.

# Context & Application

A core process-design principle (section 5).

- **Typical contexts**: long-lived servers.
- **Common applications**: registering a server process as `?MODULE`.

# Examples

The source states the principle directly; no code listing is given.

# Relationships

## Related

- **Implement a process in one module** — the module/process name correspondence depends on it.
- **Module names** — registered-process names inherit the module-naming conventions.

# Common Errors

- **Error**: Registering a short-lived worker process.
  **Correction**: Register only long-lived processes.

# Common Confusions

- **Confusion**: Thinking any process can be registered for convenient addressing.
  **Clarification**: Registration is reserved for long-lived processes, named after their module.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 5.3 "Registered processes".

# Verification Notes

- Definition source: Direct adaptation of section 5.3.
- Confidence rationale: HIGH — the rule is stated explicitly.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
