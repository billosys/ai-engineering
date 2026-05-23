---
concept: Driver Async Operations
slug: driver-async-operations
category: performance
subcategory: native-code-integration
tier: advanced
source: "ERTS User's Guide"
source_slug: otp-erts
authors: "Ericsson AB"
chapter: "How to Implement a Driver / erl_driver"
chapter_number: null
pdf_page: null
section: "An Asynchronous Driver Using driver_async"
extraction_confidence: high
aliases:
  - "driver_async"
  - "driver_select"
  - "asynchronous driver"
  - "driver thread pool"
prerequisites:
  - erlang-driver
  - driver-entry
  - port-driver-communication
extends:
  - erlang-driver
related:
  - dirty-nif-schedulers
  - erl-nif
contrasts_with: []
answers_questions:
  - "How do I perform blocking work in a driver without halting the emulator?"
  - "What is driver_async?"
  - "How does driver_select work for non-blocking I/O?"
---

# Quick Definition

Driver async operations are two mechanisms for performing work in a driver without blocking the emulator: `driver_async` dispatches blocking work to a thread pool and calls `ready_async` when done; `driver_select` registers file descriptors with the emulator's event loop and calls `ready_input`/`ready_output` when I/O is ready. Both patterns prevent the driver from halting the BEAM while waiting for external operations.

# Core Definition

The ERTS documentation describes two asynchronous patterns:

**`driver_async`** (thread pool): The erl_driver reference states: "Performs an asynchronous call. The function `async_invoke` is invoked in a thread separate from the emulator thread. This enables the driver to perform time-consuming, blocking operations without blocking the emulator." The thread pool size is configured with `+A` (command-line argument to `erl`).

The workflow is explicitly described in the tutorial: "First, the work must be prepared. In the example, this is done in `output`. We could have used `control`, but we want some variation in the examples. In our driver, we allocate a structure that contains anything that is needed for the asynchronous task to do the work. This is done in the main emulator thread. Then the asynchronous function is called from a driver thread, separate from the main emulator thread. Notice that the driver functions are not re-entrant, so they are not to be used. Finally, after the function is completed, the driver callback `ready_async` is called from the main emulator thread, this is where we return the result to Erlang."

**`driver_select`** (I/O event integration): Registers a file descriptor (Unix) or event object (Windows) with the emulator. When the fd becomes ready for reading or writing, the emulator calls the driver's `ready_input` or `ready_output` callback. The tutorial demonstrates this with a postgres async connection: the postgres socket is registered with `driver_select`, and results arrive via `ready_input` when data is available.

# Prerequisites

- **erlang-driver** -- Async operations are part of the driver framework
- **driver-entry** -- The `ready_async`, `ready_input`, and `ready_output` callbacks
- **port-driver-communication** -- Async operations are a communication pattern between drivers and the emulator

# Key Properties

**driver_async:**
1. Work is dispatched to a thread from the async thread pool (configured with `+A`)
2. The async function runs in a separate thread -- driver API functions must NOT be called from it
3. `ready_async` is called from the emulator thread when the async work completes
4. Results can only be returned to Erlang from `ready_async`, not from the async function
5. With a `NULL` key, threads are used round-robin; with a key, the same key always uses the same thread
6. `driver_async_port_key(port)` ensures a driver instance always uses the same thread for sequential execution
7. If no thread pool is available (`+A0`), the call is made synchronously

**driver_select:**
1. Registers file descriptors/events with `DO_READ` and/or `DO_WRITE` flags
2. The emulator uses `select` (Unix) or `WaitForMultipleObjects` (Windows) internally
3. `ready_input` is called when the fd is ready for reading
4. `ready_output` is called when the fd is ready for writing
5. False events can occur -- a robust driver must handle spurious wakeups
6. Selection can be removed by calling `driver_select` with `0` as the on/off parameter
7. The `stop_select` callback is called when it is safe to close the event object

# Construction / Recognition

## To Construct/Create:

driver_async pattern:
```c
static void output(ErlDrvData drv_data, char *buf, int len) {
    ErlDrvPort port = (ErlDrvPort)drv_data;
    /* Allocate work data -- must copy input, it's invalid after return */
    struct work_data* data = driver_alloc(sizeof(struct work_data));
    memcpy(data->input, buf, len);
    /* Dispatch to thread pool */
    driver_async(port, NULL, do_work, data, do_free);
}

static void do_work(void* async_data) {
    /* Runs in thread pool -- NO driver API calls allowed */
    struct work_data* d = (struct work_data*)async_data;
    d->result = expensive_computation(d->input);
}

static void ready_async(ErlDrvData drv_data, ErlDrvThreadData thread_data) {
    /* Runs in emulator thread -- can use driver API */
    ErlDrvPort port = (ErlDrvPort)drv_data;
    struct work_data* d = (struct work_data*)thread_data;
    driver_output(port, d->result, d->result_len);
    driver_free(d);
}
```

driver_select pattern:
```c
static int do_connect(const char *s, our_data_t* data) {
    PGconn* conn = PQconnectStart(s);
    int socket = PQsocket(conn);
    data->socket = socket;
    driver_select(data->port, (ErlDrvEvent)socket, DO_READ, 1);
    driver_select(data->port, (ErlDrvEvent)socket, DO_WRITE, 1);
    return 0;
}

static void ready_io(ErlDrvData drv_data, ErlDrvEvent event) {
    /* Called when the socket is ready for I/O */
    our_data_t* data = (our_data_t*)drv_data;
    /* Read data from socket, send results back */
    driver_output(data->port, result_buf, result_len);
    /* Remove write select when no longer needed */
    driver_select(data->port, (ErlDrvEvent)data->socket, DO_WRITE, 0);
}
```

## To Identify/Recognize:

1. Calls to `driver_async` in driver code
2. Calls to `driver_select` with `DO_READ`/`DO_WRITE` flags
3. `ready_async`, `ready_input`, or `ready_output` callbacks in the `driver_entry`

# Context & Application

These two async patterns serve different use cases:

- **`driver_async`**: Best for CPU-intensive or blocking library calls (e.g., database queries, compression, encryption). The work is offloaded entirely to a thread pool thread.

- **`driver_select`**: Best for I/O-bound operations (e.g., socket communication, file I/O). The driver integrates with the emulator's event loop, which is more efficient than blocking a thread.

The driver tutorial demonstrates both patterns with a postgres database driver: the synchronous version blocks the emulator, the `driver_select` version uses async postgres APIs with socket-based notification, and the `driver_async` version uses a thread pool for CPU-intensive work (permutation computation).

For new code, NIFs with dirty schedulers or custom threads provide simpler alternatives to these patterns. However, `driver_select` remains unique in its ability to integrate file descriptors directly with the BEAM event loop.

# Examples

**Example 1** (How to Implement a Driver, "An Asynchronous Driver Using driver_async"): Thread pool async pattern for permutation computation:

```c
static void output(ErlDrvData drv_data, char *buf, int len) {
    ErlDrvPort port = reinterpret_cast<ErlDrvPort>(drv_data);
    void* async_data = new our_async_data(port, *buf, buf+1, len);
    driver_async(port, NULL, do_perm, async_data, do_free);
}

static void ready_async(ErlDrvData drv_data, ErlDrvThreadData async_data) {
    ErlDrvPort port = reinterpret_cast<ErlDrvPort>(drv_data);
    our_async_data* d = reinterpret_cast<our_async_data*>(async_data);
    /* ... build result terms ... */
    driver_output_term(port, result, result_n);
    delete d;
}
```

**Example 2** (How to Implement a Driver, "Sample Asynchronous Driver"): I/O event pattern with postgres async connection:

```c
driver_select(data->port, (ErlDrvEvent)socket, DO_READ, 1);
driver_select(data->port, (ErlDrvEvent)socket, DO_WRITE, 1);
```

The `ready_io` function handles both connection completion and query results by checking the `connecting` flag.

# Relationships

## Builds Upon

- **erlang-driver** -- Async operations are driver framework features
- **driver-entry** -- The async-related callbacks (`ready_async`, `ready_input`, `ready_output`)
- **port-driver-communication** -- Async operations are communication patterns

## Related

- **dirty-nif-schedulers** -- NIFs use dirty schedulers for similar long-running work; drivers use `driver_async`

# Common Errors

- **Error**: Calling driver API functions from within the `driver_async` callback
  **Correction**: The source explicitly states "the driver functions are not re-entrant, so they are not to be used" from the async thread; only access your own data structures

- **Error**: Not copying input data before returning from the callback that calls `driver_async`
  **Correction**: The source warns "We must copy the original data, it is not valid after we have returned from the `output` function"

- **Error**: Not handling false events (spurious wakeups) from `driver_select`
  **Correction**: The source states "False events can occur. That is, calls to `ready_input` or `ready_output` although no real events are signaled... a robust driver must nevertheless be able to handle such cases."

# Common Confusions

- **Confusion**: Thinking `driver_async` creates new threads for each call
  **Clarification**: It uses a pre-allocated thread pool (sized by `+A`); calls are queued if a thread is busy

- **Confusion**: Believing `driver_select` blocks the emulator waiting for I/O
  **Clarification**: `driver_select` registers the fd with the emulator's existing event loop (using `select`/`poll`/`epoll`); the emulator continues normally and calls back when the fd is ready

- **Confusion**: Thinking `ready_async` runs in the async thread
  **Clarification**: `ready_async` runs in the emulator thread, which is why it CAN use driver API functions to send results back

# Source Reference

- "How to Implement a Driver" (Sample Asynchronous Driver, An Asynchronous Driver Using driver_async)
- "erl_driver" (driver_async function, Asynchronous calls, driver_select function)
- "driver_entry" (ready_async, ready_input, ready_output, stop_select)

# Verification Notes

- driver_async workflow: Directly quoted from "How to Implement a Driver," driver_async section
- driver_async description: Quoted from erl_driver.md driver_async function
- driver_select behavior: Summarized from erl_driver.md and driver_entry ready_input/ready_output descriptions
- False events warning: Directly from driver_entry.md ready_input description
- Confidence: HIGH -- both patterns are demonstrated with complete examples in source
