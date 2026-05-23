---
concept: NIF Thread Safety
slug: nif-thread-safety
category: processes-concurrency
subcategory: native-code-synchronization
tier: advanced
source: "ERTS User's Guide"
source_slug: otp-erts
authors: "Ericsson AB"
chapter: "erl_nif"
chapter_number: null
pdf_page: null
section: "Functionality / Threads and concurrency"
extraction_confidence: high
aliases:
  - "NIF concurrency"
  - "enif_mutex"
  - "NIF thread primitives"
  - "enif_send from non-scheduler threads"
prerequisites:
  - erl-nif
extends:
  - erl-nif
related:
  - nif-resources
  - dirty-nif-schedulers
  - nif-lifecycle
contrasts_with: []
answers_questions:
  - "How do I synchronize shared state in NIFs?"
  - "Can I call NIFs from multiple threads?"
  - "How do I send messages from non-scheduler threads?"
---

# Quick Definition

A NIF is inherently thread-safe when it acts as a pure function reading only its arguments. When shared mutable state is involved (static variables, private data, or mutable resource objects), the NIF author must provide explicit synchronization using the NIF thread API: mutexes (`enif_mutex_*`), condition variables (`enif_cond_*`), read/write locks (`enif_rwlock_*`), and thread-specific data (`enif_tsd_*`). The `enif_send` function is explicitly thread-safe and can be called from any thread, including non-scheduler threads.

# Core Definition

The ERTS documentation states: "A NIF is thread-safe without any explicit synchronization as long as it acts as a pure function and only reads the supplied arguments. When you write to a shared state either through static variables or `enif_priv_data`, you need to supply your own explicit synchronization. This includes terms in process independent environments that are shared between threads. Resource objects also require synchronization if you treat them as mutable." (erl_nif, Functionality, Threads and concurrency).

The source also notes: "The library initialization callbacks `load` and `upgrade` are thread-safe even for shared state data."

The NIF API provides POSIX-like thread primitives:
- **Mutexes** (`ErlNifMutex`) -- Mutual exclusion locks for protecting critical sections
- **Condition variables** (`ErlNifCond`) -- For threads waiting on specific conditions
- **Read/write locks** (`ErlNifRWLock`) -- Multiple readers or single writer
- **Thread-specific data** (`ErlNifTSDKey`) -- Per-thread storage

For cross-thread communication with Erlang processes, `enif_send` is the key function. It is explicitly documented as thread-safe and can be called with `caller_env` set to `NULL` from custom threads not spawned by ERTS. The message is sent in a process-independent environment that becomes invalidated after a successful send.

# Prerequisites

- **erl-nif** -- Thread safety is a concern within the NIF framework

# Key Properties

1. Pure NIFs (reading only arguments, no shared state) are thread-safe without synchronization
2. Mutable shared state (static variables, `enif_priv_data`, mutable resources, shared process-independent environments) requires explicit synchronization
3. `load` and `upgrade` callbacks are thread-safe for shared state data
4. `enif_send` is thread-safe and can be called from any thread (pass `NULL` for `caller_env` from non-ERTS threads)
5. Process-independent environments (`enif_alloc_env`) can store terms between NIF calls and send them across threads
6. Most NIF API functions are NOT thread-safe unless explicitly documented as such
7. The NIF thread API is a portable subset of POSIX threads
8. There is no condition variable wait with timeout in the NIF API (due to issues with `pthread_cond_timedwait` and system clock changes)

# Construction / Recognition

## To Construct/Create:

Protecting shared mutable state:
```c
static ErlNifMutex* my_mutex;
static int shared_counter;

static int load(ErlNifEnv* env, void** priv_data, ERL_NIF_TERM load_info) {
    my_mutex = enif_mutex_create("my_mutex");
    shared_counter = 0;
    return 0;
}

static ERL_NIF_TERM increment(ErlNifEnv* env, int argc,
                               const ERL_NIF_TERM argv[]) {
    enif_mutex_lock(my_mutex);
    shared_counter++;
    int val = shared_counter;
    enif_mutex_unlock(my_mutex);
    return enif_make_int(env, val);
}
```

Sending from a non-scheduler thread:
```c
/* In a custom thread (not an ERTS scheduler thread): */
ErlNifEnv* msg_env = enif_alloc_env();
ERL_NIF_TERM msg = enif_make_atom(msg_env, "done");
enif_send(NULL, &target_pid, msg_env, msg);
/* msg_env is invalidated after successful send */
enif_free_env(msg_env);
```

## To Identify/Recognize:

1. NIF code using `enif_mutex_*`, `enif_rwlock_*`, `enif_cond_*`, or `enif_tsd_*` functions
2. `enif_send` calls with `NULL` as the first argument (indicating non-scheduler thread)
3. Process-independent environments used to transfer terms between threads

# Context & Application

Thread safety in NIFs matters in several scenarios:

1. **Shared module state**: Multiple NIF calls accessing `enif_priv_data` or static variables concurrently (different Erlang processes calling the same NIF simultaneously on different schedulers)
2. **Mutable resource objects**: When resource objects are modified after creation and accessed from multiple processes
3. **Custom worker threads**: When a NIF spawns threads (via `enif_thread_create`) that need to communicate results back to Erlang processes
4. **Dirty NIFs**: NIFs on dirty schedulers may run concurrently with regular NIFs accessing the same data

The `enif_send` function is particularly important because it is the only way to send data from a non-scheduler thread back to an Erlang process. It uses a process-independent environment that is invalidated after a successful send, so the environment must be freed or cleared afterward.

# Examples

**Example 1** (erl_nif, Functionality, Threads and concurrency): The source states the thread safety guarantee:

```text
A NIF is thread-safe without any explicit synchronization as long as it acts
as a pure function and only reads the supplied arguments.
```

**Example 2** (erl_nif, enif_send): Sending a message from any thread:

```c
int enif_send(ErlNifEnv* caller_env, ErlNifPid* to_pid,
              ErlNifEnv* msg_env, ERL_NIF_TERM msg);
```

The `caller_env` parameter is documented as: "The environment of the calling thread (process bound or callback environment) or `NULL` if calling from a custom thread not spawned by ERTS."

The function returns `true` if the message is sent successfully, `false` if the target process is not alive or the sender is not alive.

# Relationships

## Builds Upon

- **erl-nif** -- Thread safety is a concern within NIF programming

## Related

- **nif-resources** -- Resource objects require synchronization when treated as mutable
- **dirty-nif-schedulers** -- Dirty NIFs run on separate threads and may access shared data concurrently
- **nif-lifecycle** -- load/upgrade callbacks are thread-safe for shared state

# Common Errors

- **Error**: Accessing `enif_priv_data` from multiple NIFs without synchronization
  **Correction**: Protect access with a mutex, rwlock, or other synchronization primitive

- **Error**: Using `enif_send` from a non-ERTS thread with a non-NULL `caller_env`
  **Correction**: Pass `NULL` as `caller_env` when calling from threads not spawned by ERTS

- **Error**: Reusing a process-independent environment after a successful `enif_send`
  **Correction**: The environment is invalidated by a successful send; free it with `enif_free_env` or clear it with `enif_clear_env`

- **Error**: Assuming all NIF API functions are thread-safe
  **Correction**: Most NIF API functions are NOT thread-safe; only use functions explicitly documented as thread-safe from arbitrary threads

# Common Confusions

- **Confusion**: Thinking NIFs need synchronization because they can be called from multiple Erlang processes
  **Clarification**: Each NIF call gets its own process-bound environment and arguments; synchronization is only needed for shared mutable state outside the NIF arguments

- **Confusion**: Believing `enif_send` can only be called from scheduler threads
  **Clarification**: `enif_send` is explicitly thread-safe and works from any thread; use `NULL` for `caller_env` from non-ERTS threads

# Source Reference

- "erl_nif" reference (Functionality section, "Threads and concurrency" subsection)
- "erl_nif" reference (enif_send function documentation)
- "erl_nif" reference (Data Types: ErlNifEnv, process-independent environment)

# Verification Notes

- Thread safety statement: Directly quoted from erl_nif.md, "Threads and concurrency"
- load/upgrade thread safety: Directly stated in source
- enif_send thread safety: Explicitly documented as thread-safe in function reference
- NULL caller_env: Directly from enif_send documentation
- Confidence: HIGH -- thread safety rules are explicitly documented
