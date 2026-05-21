---
concept: Driver Concurrency
slug: driver-concurrency
category: system-configuration
subcategory: null
tier: advanced
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Drivers"
chapter_number: null
pdf_page: null
section: "Drivers and Concurrency"
extraction_confidence: high
aliases:
  - "driver locking"
  - "port driver concurrency"
  - "driver-level lock"
  - "port-level lock"
prerequisites:
  - erlang-process-creation
  - smp-runtime-concurrency
extends: []
related:
  - driver-binary-handling
contrasts_with: []
answers_questions:
  - "How does the runtime handle concurrency for drivers?"
  - "How can I avoid lock contention when using ports in a multi-scheduler system?"
---

# Quick Definition

The Erlang runtime system takes a lock before running any driver code. By default the lock is per-driver (all ports sharing a driver are serialized), but a driver can be configured for per-port locking, and a scheduler-based port selection pattern can eliminate lock contention entirely.

# Core Definition

The runtime system always takes a lock before running any code in a driver. By default, that lock is at the driver level: if several ports have been opened to the same driver, only code for one port can be running at the same time. A driver can be configured to have one lock for each port instead.

For stateless (functional) drivers, a pattern exists to avoid lock contention entirely: open several ports with registered names beforehand and select the port to use based on the scheduler ID. This ensures that each scheduler thread uses a different port, eliminating contention on the port lock (Ericsson/OTP Team, "Drivers" chapter, "Drivers and Concurrency" section).

# Prerequisites

- **erlang-process-creation** -- Understanding ports and processes is needed to understand the driver/port relationship
- **smp-runtime-concurrency** -- Understanding scheduler threads is needed to understand the lock contention problem and the scheduler-based solution

# Key Properties

1. The runtime system ALWAYS takes a lock before running driver code
2. Default locking is at the driver level (one lock for all ports of that driver)
3. A driver can be configured for per-port locking (one lock per port)
4. For functional (stateless) drivers, multiple named ports can be opened to avoid contention
5. Port selection based on `erlang:system_info(scheduler_id)` distributes ports across schedulers
6. With N ports and at most N schedulers, there will be no lock contention on port locks

# Construction / Recognition

## Scheduler-Based Port Selection Pattern

1. Define a tuple of registered port names (one per expected scheduler):

```erlang
-define(PORT_NAMES(),
    {some_driver_01, some_driver_02, some_driver_03, some_driver_04,
     some_driver_05, some_driver_06, some_driver_07, some_driver_08,
     some_driver_09, some_driver_10, some_driver_11, some_driver_12,
     some_driver_13, some_driver_14, some_driver_15, some_driver_16}).
```

2. Select a port based on the current scheduler ID:

```erlang
client_port() ->
    element(erlang:system_info(scheduler_id) rem tuple_size(?PORT_NAMES()) + 1,
        ?PORT_NAMES()).
```

3. As long as the number of schedulers does not exceed the number of ports, there will be no lock contention.

# Context & Application

Driver concurrency is relevant when using port drivers (C-based or native code extensions) in multi-core Erlang systems. The default driver-level lock serializes all port operations for a given driver, which can become a bottleneck when multiple scheduler threads try to use the same driver simultaneously.

**Typical contexts:**

- High-throughput systems using native code via port drivers
- Database drivers or crypto drivers with heavy usage across multiple processes
- Systems where driver performance is a bottleneck in profiling

**When to use per-port locking:** When the driver holds per-port state and multiple ports are used concurrently.

**When to use the scheduler-based pattern:** When the driver is stateless (functional) -- it performs computation and returns a result without retaining state between calls.

# Examples

**Example** (Drivers chapter, "Drivers and Concurrency" section): Scheduler-based port selection to eliminate lock contention:

```erlang
-define(PORT_NAMES(),
    {some_driver_01, some_driver_02, some_driver_03, some_driver_04,
     some_driver_05, some_driver_06, some_driver_07, some_driver_08,
     some_driver_09, some_driver_10, some_driver_11, some_driver_12,
     some_driver_13, some_driver_14, some_driver_15, some_driver_16}).

client_port() ->
    element(erlang:system_info(scheduler_id) rem tuple_size(?PORT_NAMES()) + 1,
        ?PORT_NAMES()).
```

> As long as there are no more than 16 schedulers, there will never be any lock contention on the port lock for the driver.

# Relationships

## Related

- **driver-binary-handling** -- Binary handling techniques are used alongside concurrency patterns for driver efficiency
- **smp-runtime-concurrency** -- Driver locking interacts with the SMP scheduler thread model

## Builds Upon

- **smp-runtime-concurrency** -- The scheduler-based port selection pattern depends on understanding SMP scheduler threads

# Common Errors

- **Error**: Opening a single port to a driver and using it from many processes, creating a serialization bottleneck
  **Correction**: Open multiple ports (one per scheduler or more) and select ports based on scheduler ID to distribute load

- **Error**: Using the scheduler-based pattern with a stateful driver
  **Correction**: The pattern assumes the driver is functional (stateless). Stateful drivers need per-port locking with appropriate state management

# Common Confusions

- **Confusion**: Believing that per-port locking is always better than per-driver locking
  **Clarification**: Per-port locking reduces contention but adds overhead per port. For drivers used by a single port, per-driver locking is sufficient

- **Confusion**: Thinking the scheduler-based pattern works with any number of schedulers
  **Clarification**: The pattern works without contention only when the number of schedulers does not exceed the number of pre-opened ports. With more schedulers than ports, some contention is possible

# Source Reference

"Drivers" chapter, "Drivers and Concurrency" section. Includes the `PORT_NAMES` macro and `client_port/0` function demonstrating scheduler-based port selection for lock contention avoidance.

# Verification Notes

- Definition: Directly from source text, first three paragraphs of "Drivers and Concurrency" section
- The locking levels (driver-level and port-level) are explicit in the source
- The scheduler-based pattern is provided as a complete code example in the source
- The constraint ("as long as there are no more than 16 schedulers") is explicit in the source
- Confidence: HIGH -- explicit explanation with complete code example in official documentation
- Cross-references: All slug references verified against planned extractions
- Uncertainties: None
