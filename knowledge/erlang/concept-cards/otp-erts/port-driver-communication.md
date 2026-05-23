---
concept: Port-Driver Communication
slug: port-driver-communication
category: performance
subcategory: native-code-integration
tier: intermediate
source: "ERTS User's Guide"
source_slug: otp-erts
authors: "Ericsson AB"
chapter: "How to Implement a Driver / erl_driver / driver_entry"
chapter_number: null
pdf_page: null
section: "Calling a Driver as a Port in Erlang"
extraction_confidence: high
aliases:
  - "driver communication protocol"
  - "port command protocol"
prerequisites:
  - erlang-driver
  - driver-entry
extends:
  - erlang-driver
related:
  - external-term-format
  - erl-nif
contrasts_with: []
answers_questions:
  - "How do ports and drivers communicate?"
  - "What are the different ways to send data to a driver?"
  - "How does a driver send data back to Erlang?"
---

# Quick Definition

Ports and drivers communicate through several mechanisms with different performance characteristics: `port_control/3` for synchronous request-response (fastest, no context switch), `port_command/2` for asynchronous data sending (triggers `output`/`outputv` callback), and `driver_output`/`driver_output_term` for the driver to send data back as messages to the port owner.

# Core Definition

Communication between Erlang and a linked-in driver occurs through the port abstraction. There are multiple pathways, each with distinct characteristics:

**Erlang to Driver (data in):**

1. `port_control/3` -- Invokes the driver's `control` callback synchronously. The source describes it as "the fastest way of calling a driver and get a response. It makes no context switch in the Erlang emulator and requires no message passing." (driver_entry, `control` field). Data is passed directly in buffers; return data comes back via `*rbuf`.

2. `port_command/2` or `Port ! {self(), {command, Data}}` -- Invokes the driver's `output` callback (or `outputv` if defined, which is faster as it passes an `ErlIOVec` directly without copying). This is asynchronous -- the driver receives the data but does not return a value directly.

3. `erlang:port_call/3` -- Invokes the driver's `call` callback. Similar to `control` but uses external term format for both input and output, returning an Erlang term directly.

**Driver to Erlang (data out):**

1. `driver_output` / `driver_output2` -- Sends data to the port owner as a message of the form `{Port, {data, Data}}`. The data arrives as a binary or list of integers depending on how the port was opened.

2. `driver_output_term` -- Sends Erlang terms directly to the port owner without going through binary term format. This avoids the need for `binary_to_term/1` on the Erlang side.

3. `driver_output_binary` -- Sends a driver binary, which is faster as it avoids copying the data buffer.

**I/O event integration:**

`driver_select` registers file descriptors (Unix) or event objects (Windows) with the emulator's event loop. When the fd becomes ready, the emulator calls `ready_input` or `ready_output`, enabling non-blocking async I/O patterns.

# Prerequisites

- **erlang-driver** -- The driver framework that communication occurs within
- **driver-entry** -- The callbacks that implement the driver side of communication

# Key Properties

1. `port_control/3` is the fastest path: synchronous, no context switch, no message passing
2. `port_command/2` triggers `output`/`outputv` asynchronously; `outputv` avoids a data copy
3. Return data from `control` depends on `PORT_CONTROL_FLAG_BINARY`: if set, data returns as binary; if not, as list of integers
4. `driver_output` sends data as messages; the port must be opened in binary mode (`[binary]`) to receive binaries rather than integer lists
5. `driver_select` integrates with the emulator's event loop for async I/O without blocking
6. `driver_async` dispatches work to a thread pool; when done, `ready_async` is called from the emulator thread to send results back
7. The driver queue (`SysIOVec`) provides buffering for output data

# Construction / Recognition

## To Construct/Create:

Synchronous pattern (fastest):
1. Erlang calls `port_control(Port, Command, Data)`
2. Driver's `control` callback processes data, writes result to `*rbuf`
3. Return value is immediately available to the Erlang caller

Asynchronous pattern (non-blocking I/O):
1. Erlang calls `port_control(Port, Command, Data)` to initiate an operation
2. Driver registers fd with `driver_select(port, event, DO_READ|DO_WRITE, 1)`
3. Emulator calls `ready_input`/`ready_output` when fd is ready
4. Driver sends results back via `driver_output(port, buf, len)`
5. Erlang receives `{Port, {data, Data}}` message

Thread pool pattern:
1. Driver's `output` callback allocates work data and calls `driver_async(port, key, async_fn, data, free_fn)`
2. `async_fn` runs in a separate thread from the pool
3. When complete, `ready_async` is called from the emulator thread
4. `ready_async` sends results via `driver_output_term`

## To Identify/Recognize:

1. Erlang code using `port_control/3`, `port_command/2`, or `erlang:port_call/3`
2. Receive clauses matching `{Port, {data, Data}}`
3. Driver code calling `driver_output*`, `driver_select`, or `driver_async`

# Context & Application

The choice of communication mechanism depends on the use case:

- For quick synchronous calls (data transformation, lookups): use `port_control/3` with `control` callback
- For streaming or fire-and-forget data: use `port_command/2` with `output`/`outputv`
- For non-blocking I/O (network, file descriptors): use `driver_select` with `ready_input`/`ready_output`
- For CPU-intensive blocking work: use `driver_async` with `ready_async`

The source documents note that the `ei` library from `erl_interface` is commonly used to encode data in binary term format when using `port_control/3`, with `binary_to_term/1` on the Erlang side to decode results.

# Examples

**Example 1** (How to Implement a Driver, "Calling a Driver as a Port in Erlang"): Synchronous communication via `port_control/3`:

```erlang
connect(ConnectStr) ->
    Port = open_port({spawn, ?MODULE}, []),
    case binary_to_term(port_control(Port, ?DRV_CONNECT, ConnectStr)) of
        ok -> {ok, Port};
        Error -> Error
    end.

select(Port, Query) ->
    binary_to_term(port_control(Port, ?DRV_SELECT, Query)).
```

**Example 2** (How to Implement a Driver, "Sample Asynchronous Driver"): Async communication using `driver_select` and `driver_output`:

```erlang
%% Erlang side: port opened in binary mode
Port = open_port({spawn, ?MODULE}, [binary]),
port_control(Port, ?DRV_CONNECT, ConnectStr),
receive
    {Port, {data, Data}} ->
        binary_to_term(Data)
end.
```

```c
/* Driver side: register for I/O events */
driver_select(data->port, (ErlDrvEvent)socket, DO_READ, 1);
/* ... later, in ready_io callback: */
driver_output(data->port, x.buff, x.index);
```

# Relationships

## Builds Upon

- **erlang-driver** -- The driver framework
- **driver-entry** -- The callback functions that implement communication

## Related

- **external-term-format** -- Often used for encoding data between driver and Erlang

# Common Errors

- **Error**: Using `port_command/2` when a synchronous response is needed
  **Correction**: Use `port_control/3` for request-response patterns; it is faster and returns data directly

- **Error**: Not opening the port in binary mode when the driver sends binary data via `driver_output`
  **Correction**: Call `open_port({spawn, Name}, [binary])` to receive data as binaries rather than lists of integers

- **Error**: Trying to return data to Erlang from within the `driver_async` callback function
  **Correction**: Driver API functions cannot be called from the async thread; return data in `ready_async`, which runs on the emulator thread

# Common Confusions

- **Confusion**: Thinking `port_control/3` is slower because it is synchronous
  **Clarification**: It is actually the fastest calling mechanism -- it avoids context switches and message passing entirely

- **Confusion**: Conflating `driver_output` with the `output` callback
  **Clarification**: The `output` callback is called when Erlang sends data TO the driver; `driver_output` is a function the driver calls to send data back TO Erlang

# Source Reference

- "How to Implement a Driver" (Calling a Driver as a Port in Erlang, Sample Asynchronous Driver, An Asynchronous Driver Using driver_async)
- "driver_entry" (control, output, outputv, ready_input, ready_output, ready_async field descriptions)
- "erl_driver" (Output functions, Queue handling, Asynchronous calls sections)

# Verification Notes

- `port_control` quote: Directly from driver_entry.md, `control` field description
- Communication patterns: Synthesized from multiple source files but each mechanism is explicitly documented
- Confidence: HIGH -- all communication mechanisms are thoroughly documented across source files
