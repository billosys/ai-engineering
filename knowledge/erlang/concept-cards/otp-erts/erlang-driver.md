---
concept: Erlang Driver
slug: erlang-driver
category: performance
subcategory: native-code-integration
tier: intermediate
source: "ERTS User's Guide"
source_slug: otp-erts
authors: "Ericsson AB"
chapter: "How to Implement a Driver / erl_driver"
chapter_number: null
pdf_page: null
section: "Introduction"
extraction_confidence: high
aliases:
  - "linked-in driver"
  - "port driver"
  - "Erlang port driver"
  - "erl_driver"
prerequisites:
  - erlang-process
  - erlang-ports
extends: []
related:
  - driver-entry
  - port-driver-communication
  - erl-nif
  - external-term-format
contrasts_with:
  - erl-nif
answers_questions:
  - "What is an Erlang driver?"
  - "How do drivers relate to NIFs as FFI mechanisms?"
  - "How do I implement an Erlang driver?"
  - "What distinguishes a NIF from a driver?"
---

# Quick Definition

An Erlang driver is a C library linked to the Erlang emulator and accessed through a port, providing native code integration for performance-critical work or OS resource access. Drivers communicate with Erlang processes via port commands and use a callback-based interface defined by the `driver_entry` struct.

# Core Definition

The ERTS documentation states: "A driver in Erlang is a library written in C, which is linked to the Erlang emulator and called from Erlang. Drivers can be used when C is more suitable than Erlang, to speed up things, or to provide access to OS resources not directly accessible from Erlang." (How to Implement a Driver, Introduction).

A driver can be dynamically loaded as a shared library or statically linked with the emulator. Each driver instance is associated with an Erlang port and has a port owner process. The driver exports a single function via the `DRIVER_INIT` macro, which returns a pointer to a `driver_entry` struct containing callback function pointers.

The erl_driver documentation warns with extreme severity: "A driver callback is executed as a direct extension of the native code of the VM. Execution is not made in a safe environment. The VM _cannot_ provide the same services as provided when executing Erlang code, such as pre-emptive scheduling or memory protection. If the driver callback function does not behave well, the whole VM will misbehave." Specific risks include: a crashing callback crashes the whole VM, erroneous implementations can cause VM state inconsistency, and lengthy work degrades responsiveness.

# Prerequisites

- **erlang-process** -- Processes own ports that communicate with drivers
- **erlang-ports** -- Drivers are accessed through the Erlang port mechanism

# Key Properties

1. Drivers are C libraries linked to the emulator, either dynamically (shared library) or statically
2. Each driver instance is associated with an Erlang port and a port owner process
3. A driver exports only one function (`driver_init`) via the `DRIVER_INIT` macro, returning a `driver_entry` struct
4. Driver callbacks execute in the emulator thread -- they must be non-blocking (return within ~1 ms)
5. Drivers are locked either at driver level (default, one thread at a time) or port level (`ERL_DRV_FLAG_USE_PORT_LOCKING`)
6. A crash in a driver crashes the entire VM -- there is no memory protection
7. Drivers support asynchronous operation via `driver_async` (thread pool), `driver_select` (I/O readiness), and timer callbacks
8. NIFs are generally preferred over drivers for new code

# Construction / Recognition

## To Construct/Create:

1. Write a C source file that includes `erl_driver.h`
2. Define a `driver_entry` struct with the necessary callback functions (at minimum: `start`, `stop`, and one of `output`/`control`)
3. Export the entry via `DRIVER_INIT(drivername)` macro
4. Compile as a shared library (e.g., `gcc -shared -fpic`)
5. Load from Erlang with `erl_ddll:load_driver/2`
6. Open a port with `open_port({spawn, DriverName}, Options)`

## To Identify/Recognize:

1. Code that uses `erl_ddll:load_driver/2` followed by `open_port/2`
2. C code that includes `erl_driver.h` and defines a `driver_entry` struct
3. Communication via `port_command/2`, `port_control/3`, or `Port ! {self(), {command, Data}}`

# Context & Application

Drivers were historically the primary mechanism for integrating native C code with Erlang. They provide bidirectional communication through the port protocol, support for asynchronous I/O via `driver_select` and `driver_async`, and a queue mechanism for buffering output.

The synchronous driver pattern (using `port_control/3`) is the fastest way to call a driver and get a response -- it requires no context switch and no message passing. The asynchronous pattern (using `driver_select` or `driver_async`) avoids blocking the emulator at the cost of complexity.

For new code, NIFs are generally preferred because they are simpler to implement and have lower overhead for synchronous calls. Drivers remain useful when I/O event integration (via `driver_select`) is needed, or when the port abstraction (with its owner process, links, and message-based communication) is beneficial.

# Examples

**Example 1** (How to Implement a Driver, "Sample Driver"): A synchronous postgres driver using `port_control/3`:

```c
static ErlDrvEntry pq_driver_entry = {
    NULL,                        /* init */
    start,
    stop,
    NULL,                        /* output */
    NULL,                        /* ready_input */
    NULL,                        /* ready_output */
    "pg_sync",                   /* the name of the driver */
    NULL,                        /* finish */
    NULL,                        /* handle */
    control,
    NULL,                        /* timeout */
    NULL,                        /* outputv */
    NULL,                        /* ready_async */
    NULL,                        /* flush */
    NULL,                        /* call */
    NULL                         /* event */
};
```

The Erlang side loads and uses it:

```erlang
connect(ConnectStr) ->
    case erl_ddll:load_driver(".", "pg_sync") of
        ok -> ok;
        {error, already_loaded} -> ok;
        E -> exit({error, E})
    end,
    Port = open_port({spawn, ?MODULE}, []),
    case binary_to_term(port_control(Port, ?DRV_CONNECT, ConnectStr)) of
        ok -> {ok, Port};
        Error -> Error
    end.
```

**Example 2** (How to Implement a Driver, "Sample Asynchronous Driver"): An asynchronous postgres driver using `driver_select` for non-blocking I/O:

```c
driver_select(data->port, (ErlDrvEvent)socket, DO_READ, 1);
driver_select(data->port, (ErlDrvEvent)socket, DO_WRITE, 1);
```

When the socket is ready, the emulator calls `ready_input` or `ready_output`, and the driver sends results back via `driver_output`.

# Relationships

## Builds Upon

- **erlang-process** -- Port owner processes communicate with drivers through port commands
- **erlang-ports** -- Drivers are the native code behind Erlang ports

## Related

- **driver-entry** -- The callback struct that defines a driver's interface to the emulator
- **port-driver-communication** -- The protocol for data exchange between ports and drivers
- **external-term-format** -- Drivers often use the `ei` library to encode/decode terms in binary format

## Contrasts With

- **erl-nif** -- NIFs replace Erlang functions directly (no port needed), are simpler, and are preferred for new code; drivers use the port abstraction and support async I/O via `driver_select`

# Common Errors

- **Error**: Performing blocking or lengthy work in a driver callback (e.g., synchronous database queries)
  **Correction**: Use `driver_async` to dispatch blocking work to the async thread pool, or `driver_select` for non-blocking I/O

- **Error**: Not storing the port handle in the `start` callback for later use
  **Correction**: The port handle is only passed to `start`; stash it in your driver data structure for use with driver API functions in other callbacks

- **Error**: Modifying a driver binary after it has been sent to the emulator
  **Correction**: Once a binary is sent to the emulator, it becomes shared and must not be changed by the driver

# Common Confusions

- **Confusion**: Thinking drivers run in a separate process or have memory protection
  **Clarification**: Drivers execute as a direct extension of the VM's native code in the emulator thread; a crash in the driver crashes the entire VM

- **Confusion**: Believing `port_control/3` and `port_command/2` are the same
  **Clarification**: `port_control/3` is a synchronous ioctl-like call (fastest, no message passing); `port_command/2` sends data asynchronously through the `output`/`outputv` callback

# Source Reference

- "How to Implement a Driver" chapter (Introduction, Sample Driver, Sample Asynchronous Driver, An Asynchronous Driver Using driver_async)
- "erl_driver" reference (Description, Functionality sections)
- "driver_entry" reference (Description, Data Types)

# Verification Notes

- Definition: Directly quoted from "How to Implement a Driver," Introduction section
- Warning text: Verbatim from erl_driver.md WARNING section
- Example code: From the pg_sync sample driver in "How to Implement a Driver"
- Confidence: HIGH -- concepts explicitly defined in multiple source documents
