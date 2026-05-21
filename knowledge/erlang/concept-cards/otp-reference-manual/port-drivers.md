---
# === CORE IDENTIFICATION ===
concept: Port Drivers
slug: port-drivers

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Ports and Port Drivers"
chapter_number: null
pdf_page: null
section: "Port Drivers"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - linked-in driver
  - port driver

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-port
extends:
  - erlang-port
related:
  - opening-a-port
  - port-settings
contrasts_with:
  - erlang-port

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a port driver?"
  - "How does a port driver differ from a regular port?"
  - "What are the risks of using port drivers?"
---

# Quick Definition
A port driver is a C program that is dynamically linked into the Erlang runtime system and appears as a port from the Erlang programmer's perspective. Unlike regular ports (which run in separate OS processes), port drivers run inside the VM, providing higher performance but at the risk of crashing the entire runtime.

# Core Definition
The Erlang Reference Manual states: "It is possible to write a driver in C according to certain principles and dynamically link it to the Erlang runtime system. The linked-in driver looks like a port from the Erlang programmer's point of view and is called a _port driver_." The manual includes a warning: "An erroneous port driver causes the entire Erlang runtime system to leak memory, hang, or crash." (Ports and Port Drivers chapter, "Port Drivers" section).

# Prerequisites
- **erlang-port** -- Port drivers are a variant of ports and share the same interface

# Key Properties
1. Written in C according to specific principles (erl_driver, driver_entry APIs)
2. Dynamically linked into the Erlang runtime system
3. Looks identical to a regular port from the Erlang side
4. Runs inside the Erlang VM process, not in a separate OS process
5. Higher performance than external ports (no OS process boundary, no stdin/stdout marshaling)
6. An erroneous port driver can leak memory, hang, or crash the entire Erlang VM
7. Additional BIFs available for port drivers: `port_control/3` and `erlang:port_call/3`
8. Loaded via the `erl_ddll` module in the Kernel application

# Construction / Recognition
## To Construct/Create:
1. Write the driver in C using the `erl_driver` and `driver_entry` APIs
2. Load the driver dynamically using the `erl_ddll` module
3. Open the driver as a port: `open_port({spawn, DriverName}, Settings)`
4. If a loaded port driver matches the `Command` name, it is used instead of starting an external program

## To Identify/Recognize:
1. A port driver is created when `open_port({spawn, Command}, _)` finds a loaded driver matching `Command`
2. `port_control/3` and `erlang:port_call/3` are only meaningful for port drivers, not external ports

# Context & Application
Port drivers are used when the performance overhead of communicating with a separate OS process is unacceptable. They provide low-latency, high-throughput C-level integration at the cost of safety -- a bug in the driver can take down the entire Erlang node.

**Typical contexts:**
- High-performance C library integration where NIF is not suitable
- Legacy driver code (modern Erlang often prefers NIFs for C integration)
- Database drivers, crypto operations, or other performance-critical native code

**When NOT to use:**
- When safety is paramount and the external program might crash -- use a regular port instead
- For simple external program communication -- regular ports are safer and simpler
- Consider NIFs as an alternative for many use cases (though NIFs carry similar crash risks)

# Examples
**Example 1** (Ports and Port Drivers, "Port Drivers" section): The warning about port driver risks: "An erroneous port driver causes the entire Erlang runtime system to leak memory, hang, or crash."

**Example 2** (Ports and Port Drivers, "Port BIFs" section): Additional BIFs for port drivers:
- `port_control/3` -- synchronous control call to the driver
- `erlang:port_call/3` -- synchronous call to the driver

**Example 3** (Ports and Port Drivers, "Port Drivers" section): Resources for writing port drivers:
- `erl_driver` in ERTS -- driver API
- `driver_entry` in ERTS -- driver entry point specification
- `erl_ddll` in Kernel -- dynamic driver loading

# Relationships
## Builds Upon
- **erlang-port** -- Port drivers extend the port concept with in-VM C code

## Enables
Nothing directly -- port drivers are a terminal capability.

## Related
- **opening-a-port** -- Port drivers are opened with the same `open_port/2` BIF
- **port-settings** -- Settings apply to port drivers as well

## Contrasts With
- **erlang-port** -- Regular ports run in separate OS processes and are safe (the external program cannot crash the VM). Port drivers run inside the VM with higher performance but can crash the entire runtime.

# Common Errors
- **Error**: Assuming a port driver crash only affects the port
  **Correction**: A port driver runs inside the Erlang VM. A crash, memory leak, or hang in the driver affects the entire runtime system, not just the port.

- **Error**: Using `port_control/3` or `erlang:port_call/3` on a regular (non-driver) port
  **Correction**: These BIFs are specific to port drivers. They will not work correctly on ports connected to external programs.

# Common Confusions
- **Confusion**: Thinking port drivers and NIFs are the same thing
  **Clarification**: Both run C code inside the VM, but they have different APIs and execution models. Port drivers use the `erl_driver`/`driver_entry` API and communicate via the port protocol. NIFs use the `erl_nif` API and are called directly as Erlang functions. Both carry crash risks.

- **Confusion**: Thinking port drivers run in a separate process like regular ports
  **Clarification**: Port drivers are linked into the Erlang VM and execute within the same OS process. This is precisely why they are dangerous -- there is no OS-level isolation.

# Source Reference
Ports and Port Drivers chapter, "Port Drivers" section, with additional BIF information from "Port BIFs" section.

# Verification Notes
- Definition source: Direct from source
- Confidence rationale: High -- clear definition and explicit warning about risks
- Uncertainties: None
- Cross-reference status: All referenced slugs correspond to planned cards
