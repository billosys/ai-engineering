---
concept: Driver Entry
slug: driver-entry
category: performance
subcategory: native-code-integration
tier: intermediate
source: "ERTS User's Guide"
source_slug: otp-erts
authors: "Ericsson AB"
chapter: "driver_entry"
chapter_number: null
pdf_page: null
section: "Description"
extraction_confidence: high
aliases:
  - "driver_entry struct"
  - "ErlDrvEntry"
  - "driver callback struct"
prerequisites:
  - erlang-driver
extends:
  - erlang-driver
related:
  - port-driver-communication
  - erl-nif
contrasts_with: []
answers_questions:
  - "What is the driver_entry struct?"
  - "What callbacks does a driver implement?"
  - "How does the emulator interact with a driver?"
---

# Quick Definition

The `driver_entry` is a C struct containing ~15 function pointers that define a driver's interface to the Erlang emulator. It specifies the callbacks the emulator invokes at various lifecycle points: when the driver is loaded (`init`), when a port is opened (`start`) or closed (`stop`), when data arrives (`output`/`outputv`), when I/O events fire (`ready_input`/`ready_output`), and more.

# Core Definition

The ERTS documentation states: "The `driver_entry` structure is a C struct that all Erlang drivers define. It contains entry points for the Erlang driver, which are called by the Erlang emulator when Erlang code accesses the driver." (driver_entry, Description).

The struct is declared as `ErlDrvEntry` and contains the following key entry points:

- `init` -- Called at load time (once for the driver)
- `start` -- Called when `open_port/2` creates a new port instance; returns a driver-defined handle
- `stop` -- Called when the port is closed
- `output` -- Called when data is sent to the port via `port_command/2` or `Port ! {self(), {command, Data}}`
- `ready_input` / `ready_output` -- Called when an event registered with `driver_select` fires
- `control` -- Called from `port_control/3`; a synchronous ioctl-like interface (fastest calling mechanism)
- `call` -- Similar to `control` but uses external term format
- `outputv` -- Faster alternative to `output` that takes an `ErlIOVec` directly
- `ready_async` -- Called after `driver_async` work completes
- `timeout` -- Called when the driver's timer expires
- `flush` -- Called before `stop` when the driver queue has data
- `process_exit` -- Called when a monitored process exits
- `stop_select` -- Called when it is safe to close an event object after `driver_select`
- `finish` -- Called when the driver is unloaded

The only exported function from a driver is `driver_init`, declared via the `DRIVER_INIT(drivername)` macro, which returns a pointer to this struct.

# Prerequisites

- **erlang-driver** -- The driver_entry struct is the core interface definition for an Erlang driver

# Key Properties

1. The `start` callback is the only one that receives the port handle; it must store it for later use
2. `start` returns a driver-defined handle (`ErlDrvData`) that is passed to all subsequent callbacks
3. `control` is the fastest calling mechanism -- no context switch, no message passing
4. `outputv` is preferred over `output` for binary mode ports as it avoids data copying
5. The struct must NOT be declared `const` because the emulator modifies the `handle` and `handle2` fields
6. Extended interface fields (`extended_marker`, `major_version`, `minor_version`, `driver_flags`) are required since ERTS 5.9
7. `driver_flags` can set `ERL_DRV_FLAG_USE_PORT_LOCKING` for port-level rather than driver-level locking

# Construction / Recognition

## To Construct/Create:

1. Declare a static `ErlDrvEntry` struct
2. Set needed callback pointers; use `NULL` for unused callbacks
3. Set `driver_name` to match the atom used in `open_port/2` and the shared library filename
4. Set extended marker fields for version management
5. Export via `DRIVER_INIT(drivername)` which returns a pointer to the struct

## To Identify/Recognize:

1. A C variable of type `ErlDrvEntry` or `struct erl_drv_entry`
2. Contains the characteristic sequence of function pointer fields (init, start, stop, output, ready_input, ...)
3. Referenced by `DRIVER_INIT` macro

# Context & Application

The `driver_entry` struct is the contract between a driver and the Erlang emulator. A common pattern is to implement only the callbacks needed: a minimal driver might implement just `start`, `stop`, and `control`. More sophisticated drivers add `ready_input`/`ready_output` for async I/O, `ready_async` for thread pool work, or `outputv` for efficient binary handling.

The `start` callback typically allocates a driver-specific state struct, stores the port handle in it, and returns it as `ErlDrvData`. This pattern gives all subsequent callbacks access to both the driver state and the port handle.

# Examples

**Example 1** (driver_entry, Data Types): The full struct definition shows all 15+ callback fields:

```c
typedef struct erl_drv_entry {
    int (*init)(void);
    ErlDrvData (*start)(ErlDrvPort port, char *command);
    void (*stop)(ErlDrvData drv_data);
    void (*output)(ErlDrvData drv_data, char *buf, ErlDrvSizeT len);
    void (*ready_input)(ErlDrvData drv_data, ErlDrvEvent event);
    void (*ready_output)(ErlDrvData drv_data, ErlDrvEvent event);
    char *driver_name;
    void (*finish)(void);
    void *handle;            /* Reserved, used by emulator internally */
    ErlDrvSSizeT (*control)(...);
    void (*timeout)(ErlDrvData drv_data);
    void (*outputv)(ErlDrvData drv_data, ErlIOVec *ev);
    void (*ready_async)(ErlDrvData drv_data, ErlDrvThreadData thread_data);
    void (*flush)(ErlDrvData drv_data);
    ErlDrvSSizeT (*call)(...);
    /* ... extended fields ... */
} ErlDrvEntry;
```

**Example 2** (How to Implement a Driver, "Sample Driver"): A minimal driver entry using only start, stop, and control:

```c
static ErlDrvEntry pq_driver_entry = {
    NULL,      /* init */
    start,
    stop,
    NULL,      /* output */
    NULL,      /* ready_input */
    NULL,      /* ready_output */
    "pg_sync", /* the name of the driver */
    NULL,      /* finish */
    NULL,      /* handle */
    control,
    NULL,      /* timeout */
    NULL,      /* outputv */
    NULL,      /* ready_async */
    NULL,      /* flush */
    NULL,      /* call */
    NULL       /* event */
};
```

# Relationships

## Builds Upon

- **erlang-driver** -- driver_entry is the callback interface that defines a driver

## Related

- **port-driver-communication** -- The callbacks in driver_entry implement the communication protocol between ports and drivers

# Common Errors

- **Error**: Declaring the `driver_entry` as `const`
  **Correction**: The emulator modifies the `handle` and `handle2` fields; a `const` struct in read-only memory will crash the emulator

- **Error**: Not setting the extended marker fields in modern ERTS
  **Correction**: Since ERTS 5.9, drivers must set `extended_marker` to `ERL_DRV_EXTENDED_MARKER` and set the version fields appropriately

- **Error**: Forgetting to store the port handle in the `start` callback
  **Correction**: The port handle is only passed to `start`; store it in your driver data struct so other callbacks can use it with driver API functions

# Common Confusions

- **Confusion**: Believing `output` and `control` serve the same purpose
  **Clarification**: `output` handles data sent via `port_command/2` (asynchronous, one-way); `control` handles `port_control/3` (synchronous, returns data directly -- the fastest calling mechanism)

- **Confusion**: Thinking `outputv` replaces `output`
  **Clarification**: If `outputv` is non-NULL, the emulator calls it instead of `output` for binary-mode ports; it is faster because it passes an `ErlIOVec` directly without copying

# Source Reference

- "driver_entry" reference (Description, Data Types sections)
- "How to Implement a Driver" (Sample Driver, Sample Asynchronous Driver sections)

# Verification Notes

- Definition: Directly quoted from driver_entry.md Description
- Struct fields: From the typedef in driver_entry.md Data Types
- Field descriptions: Summarized from individual field documentation
- Confidence: HIGH -- struct is fully documented with all fields described
