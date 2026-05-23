---
concept: NIF (Native Implemented Function)
slug: erl-nif
category: performance
subcategory: native-code-integration
tier: intermediate
source: "ERTS User's Guide"
source_slug: otp-erts
authors: "Ericsson AB"
chapter: "erl_nif"
chapter_number: null
pdf_page: null
section: "Description"
extraction_confidence: high
aliases:
  - "NIF"
  - "Native Implemented Function"
  - "erl_nif"
  - "NIF library"
prerequisites:
  - erlang-process
extends: []
related:
  - nif-resources
  - dirty-nif-schedulers
  - nif-lifecycle
  - erlang-driver
  - external-term-format
contrasts_with:
  - erlang-driver
answers_questions:
  - "What is a NIF (Native Implemented Function)?"
  - "How do I implement a NIF library?"
  - "What must I know before writing a NIF?"
  - "What distinguishes a NIF from a driver?"
  - "How do drivers relate to NIFs as FFI mechanisms?"
---

# Quick Definition

A NIF (Native Implemented Function) is a C function that replaces an Erlang function, called transparently by Erlang code without any difference to the caller. NIF libraries are dynamically linked shared libraries loaded at runtime via `erlang:load_nif/2`. NIFs are simpler and faster than drivers for synchronous native code integration but carry the critical risk that a misbehaving NIF can crash or corrupt the entire VM.

# Core Definition

The ERTS documentation states: "A NIF library contains native implementation of some functions of an Erlang module. The native implemented functions (NIFs) are called like any other functions without any difference to the caller. A NIF library is built as a dynamically linked library file and loaded in runtime by calling `erlang:load_nif/2`." (erl_nif, Description).

The safety warning is critical and prominently placed: "A native function is executed as a direct extension of the native code of the VM. Execution is not made in a safe environment. The VM _cannot_ provide the same services as provided when executing Erlang code, such as pre-emptive scheduling or memory protection." Specific consequences:

- A native function that crashes will crash the whole VM
- An erroneously implemented native function can cause VM internal state inconsistency, leading to crashes or misbehaviors at any point afterward
- A native function doing lengthy work before returning degrades VM responsiveness and can cause extreme memory usage and bad load balancing between schedulers

A NIF receives its arguments as `ERL_NIF_TERM` values within an `ErlNifEnv` environment and returns an `ERL_NIF_TERM`. All terms belong to environments, and their lifetime is controlled by the environment's lifetime. The NIF API provides `enif_get_*` functions to read terms and `enif_make_*` functions to create terms.

# Prerequisites

- **erlang-process** -- NIFs execute in the context of the calling process's scheduler thread

# Key Properties

1. NIFs are called transparently -- the caller cannot distinguish a NIF from a regular Erlang function
2. Each NIF must have an Erlang stub implementation (typically calling `erlang:nif_error/1`) as a fallback before the NIF library is loaded
3. The `-nifs([func/arity])` attribute declares which functions will be replaced by NIFs
4. Loading uses `-on_load(init/0)` directive with `erlang:load_nif/2`
5. A NIF library is persistent once loaded -- it is not unloaded until the module instance is purged
6. A well-behaving NIF must return within approximately 1 millisecond
7. NIFs that cannot return quickly must use yielding, threading, or dirty schedulers
8. All `ERL_NIF_TERM` values belong to an `ErlNifEnv` and are valid only as long as that environment exists
9. Three environment types exist: process-bound (NIF call), callback (load/upgrade), and process-independent (created with `enif_alloc_env`)
10. A NIF is thread-safe without explicit synchronization as long as it acts as a pure function reading only its arguments

# Construction / Recognition

## To Construct/Create:

1. Write a C source file including `erl_nif.h`
2. Implement NIF functions with signature: `ERL_NIF_TERM func(ErlNifEnv* env, int argc, const ERL_NIF_TERM argv[])`
3. Define a static array of `ErlNifFunc` descriptors
4. Initialize with `ERL_NIF_INIT(module, funcs, load, NULL, upgrade, unload)`
5. Write the Erlang module with `-nifs()` attribute and stub implementations
6. Use `-on_load(init/0)` to call `erlang:load_nif/2`
7. Compile: `gcc -fPIC -shared -o module.so module.c -I $ERL_ROOT/usr/include/`

## To Identify/Recognize:

1. C code including `erl_nif.h` and using `ERL_NIF_INIT` macro
2. Erlang modules with `-nifs()` attribute and `-on_load` directive
3. Functions calling `erlang:load_nif/2`
4. Stub functions calling `erlang:nif_error/1`

# Context & Application

NIFs are the preferred mechanism for integrating native C code with Erlang when synchronous function call semantics are appropriate. Compared to drivers:

- NIFs are simpler: no port abstraction, no message passing, direct function call semantics
- NIFs are faster for synchronous calls: they replace the Erlang function directly
- Drivers are better for async I/O integration (via `driver_select`) and when the port abstraction (owner process, links, message-based communication) is beneficial

The ~1 ms return time requirement is critical. For long-running work, three strategies exist (in order of preference):

1. **Yielding NIF** -- Split work into chunks, use `enif_schedule_nif` to reschedule
2. **Threaded NIF** -- Dispatch to a separate thread, send result back via `enif_send`
3. **Dirty NIF** -- Execute on dirty schedulers (CPU-bound or I/O-bound)

`enif_consume_timeslice()` should typically always be used to inform the runtime about NIF call length.

# Examples

**Example 1** (erl_nif, Example): A minimal NIF library:

```c
/* niftest.c */
#include <erl_nif.h>

static ERL_NIF_TERM hello(ErlNifEnv* env, int argc,
                          const ERL_NIF_TERM argv[])
{
    return enif_make_string(env, "Hello world!", ERL_NIF_LATIN1);
}

static ErlNifFunc nif_funcs[] =
{
    {"hello", 0, hello}
};

ERL_NIF_INIT(niftest,nif_funcs,NULL,NULL,NULL,NULL)
```

```erlang
-module(niftest).
-export([init/0, hello/0]).
-nifs([hello/0]).
-on_load(init/0).

init() ->
      erlang:load_nif("./niftest", 0).

hello() ->
      erlang:nif_error("NIF library not loaded").
```

**Example 2** (erl_nif, Functionality, "Read and write Erlang terms"): Best practice for atom creation during loading:

```c
ERL_NIF_TERM world_atom;

static int load(ErlNifEnv* env, void** priv_data, ERL_NIF_TERM load_info)
{
    world_atom = enif_make_atom(env, "world");
    return 0;
}

static ERL_NIF_TERM hello(ErlNifEnv* env, int argc,
                          const ERL_NIF_TERM argv[])
{
    ERL_NIF_TERM hello_string =
        enif_make_string(env, "Hello", ERL_NIF_LATIN1);
    return enif_make_tuple2(env, hello_string, world_atom);
}
```

Atoms created during `load` or `upgrade` can be stored in global variables and used in any environment.

# Relationships

## Builds Upon

- **erlang-process** -- NIFs execute in the calling process's scheduler thread context

## Related

- **nif-resources** -- Resource objects for safely wrapping C data structures in NIF terms
- **dirty-nif-schedulers** -- Dirty schedulers for long-running NIF work
- **nif-lifecycle** -- Load, upgrade, and unload callbacks for NIF library management
- **external-term-format** -- NIFs can use `enif_binary_to_term`/`enif_term_to_binary` for term serialization

## Contrasts With

- **erlang-driver** -- Drivers use port-based communication (more complex, supports async I/O); NIFs use direct function replacement (simpler, faster for synchronous calls)

# Common Errors

- **Error**: Writing a NIF that takes longer than 1 ms to return without using yielding, threading, or dirty schedulers
  **Correction**: Use `enif_consume_timeslice()` to report time usage; split into chunks with `enif_schedule_nif`, dispatch to threads, or mark as dirty NIF

- **Error**: Not providing Erlang stub functions for NIFs
  **Correction**: Every NIF must have an Erlang implementation (typically `erlang:nif_error("NIF library not loaded")`) to be invoked before the library loads or as a fallback

- **Error**: Storing a pointer to a process-bound `ErlNifEnv` between NIF calls
  **Correction**: Process-bound environments are only valid during the NIF call; use `enif_alloc_env` for process-independent environments that persist

- **Error**: Declaring a NIF as local and not exporting it, then having the compiler optimize it away
  **Correction**: A NIF can be local, but the stub function must not be optimized away; ensure it is referenced or exported

# Common Confusions

- **Confusion**: Thinking NIFs run in a separate thread or sandboxed environment
  **Clarification**: NIFs execute as a direct extension of the VM's native code in the scheduler thread; a crash kills the entire VM

- **Confusion**: Believing NIF libraries are unloaded when `erlang:load_nif/2` is called again
  **Clarification**: A NIF library is persistent -- it is not unloaded until the module instance it belongs to is purged. The `upgrade` callback handles library transitions.

- **Confusion**: Confusing `ERL_NIF_TERM` with regular C values
  **Clarification**: `ERL_NIF_TERM` is an opaque type that can only be read/written through API functions; it is bound to its `ErlNifEnv` and invalid after the environment is destroyed

# Source Reference

- "erl_nif" reference (Description, Example, Functionality, Initialization, Data Types sections)

# Verification Notes

- Definition: Directly quoted from erl_nif.md Description
- Warning: Verbatim from erl_nif.md WARNING section
- Minimal example: Directly from erl_nif.md Example section
- Atom creation pattern: From erl_nif.md Functionality section
- 1 ms guideline: From erl_nif.md "Long-running NIFs" section
- Confidence: HIGH -- all content directly from the official erl_nif reference
