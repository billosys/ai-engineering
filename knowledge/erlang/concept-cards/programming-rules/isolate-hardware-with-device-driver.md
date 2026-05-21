---
concept: Isolate Hardware Interfaces With A Device Driver
slug: isolate-hardware-with-device-driver
category: core-idioms
subcategory: sw-engineering-principles
tier: intermediate
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "SW Engineering Principles"
chapter_number: 3
pdf_page: null
section: "3.14 Isolate hardware interfaces with a device driver"
extraction_confidence: high
aliases:
  - "device driver isolation"
  - "hardware as Erlang processes"
prerequisites: []
extends: []
related:
  - isolate-dirty-code
  - tag-messages
contrasts_with: []
answers_questions:
  - "How should hardware interfaces be isolated in an Erlang system?"
---

# Quick Definition

Isolate hardware from the system behind device drivers that make the hardware look and behave like ordinary Erlang processes.

# Core Definition

"Hardware should be isolated from the system through the use of device drivers. The device drivers should implement hardware interfaces which make the hardware appear as if they were Erlang processes" (Programming Rules, 3.14). Hardware should appear to receive and send normal Erlang messages and respond conventionally when errors occur.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Hardware is accessed only through device drivers.
2. A device driver presents the hardware as if it were an Erlang process.
3. The hardware appears to send and receive ordinary Erlang messages.
4. The hardware responds conventionally — like a process — when errors occur.

# Construction / Recognition

## To Apply

1. Wrap each hardware interface in a device driver.
2. Expose it to the rest of the system as a message-driven Erlang process.

## To Recognize a Violation

1. System code touches hardware directly instead of through a process-like driver.

# Context & Application

A core software-engineering principle (section 3).

- **Typical contexts**: telecom and embedded systems with hardware interfaces.
- **Common applications**: a driver process that turns hardware events into Erlang messages.

# Examples

The source states the principle directly; no code example is given.

# Relationships

## Related

- **Isolate "tricky" or "dirty" code into separate modules** — hardware code is a kind of dirty code to isolate.
- **Tag messages** — the messages the driver exchanges should be tagged like any others.

# Common Errors

- **Error**: Letting application code interact with hardware directly.
  **Correction**: Route all hardware access through a driver that behaves like a process.

# Common Confusions

- **Confusion**: Thinking a device driver is only low-level glue.
  **Clarification**: Its purpose is also architectural — making hardware uniform with the system's process/message model.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 3.14 "Isolate hardware interfaces with a device driver".

# Verification Notes

- Definition source: Direct adaptation of section 3.14.
- Confidence rationale: HIGH — the rule is stated explicitly.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
