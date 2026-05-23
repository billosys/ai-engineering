---
concept: Dirty NIF Schedulers
slug: dirty-nif-schedulers
category: performance
subcategory: native-code-integration
tier: advanced
source: "ERTS User's Guide"
source_slug: otp-erts
authors: "Ericsson AB"
chapter: "erl_nif"
chapter_number: null
pdf_page: null
section: "Functionality / Long-running NIFs / Dirty NIF"
extraction_confidence: high
aliases:
  - "dirty NIFs"
  - "dirty schedulers"
  - "dirty CPU scheduler"
  - "dirty I/O scheduler"
  - "ERL_NIF_DIRTY_JOB_CPU_BOUND"
  - "ERL_NIF_DIRTY_JOB_IO_BOUND"
prerequisites:
  - erl-nif
extends:
  - erl-nif
related:
  - nif-resources
  - nif-lifecycle
contrasts_with: []
answers_questions:
  - "How do I handle long-running NIF work without blocking the scheduler?"
  - "What are dirty schedulers?"
  - "What is the difference between dirty CPU and dirty I/O schedulers?"
---

# Quick Definition

Dirty NIF schedulers are a separate pool of scheduler threads dedicated to executing NIFs that cannot complete within the ~1 ms time budget of a normal scheduler. A NIF is classified as "dirty" and scheduled on either dirty CPU schedulers (for CPU-bound work) or dirty I/O schedulers (for I/O-bound/blocking work), preventing it from blocking normal Erlang scheduling.

# Core Definition

The ERTS documentation states: "A NIF that cannot be split and cannot execute in a millisecond or less is called a 'dirty NIF', as it performs work that the ordinary schedulers of the Erlang runtime system cannot handle cleanly. Applications that make use of such functions must indicate to the runtime that the functions are dirty so they can be handled specially. This is handled by executing dirty jobs on a separate set of schedulers called dirty schedulers. A dirty NIF executing on a dirty scheduler does not have the same duration restriction as a normal NIF." (erl_nif, Functionality, Long-running NIFs, Dirty NIF).

The source emphasizes correct classification: "It is important to classify the dirty job correct. An I/O bound job should be classified as such, and a CPU bound job should be classified as such. If you should classify CPU bound jobs as I/O bound jobs, dirty I/O schedulers might starve ordinary schedulers. I/O bound jobs are expected to either block waiting for I/O, and/or spend a limited amount of time moving data."

Dirty NIFs are the third and least preferred option for handling long-running native work. The source explicitly states the preference order:
1. **Yielding NIF** (preferred) -- split work into chunks via `enif_schedule_nif`
2. **Threaded NIF** -- dispatch to custom threads, send results via `enif_send`
3. **Dirty NIF** -- execute on dirty schedulers

# Prerequisites

- **erl-nif** -- Dirty schedulers are a feature of the NIF API for handling long-running NIF calls

# Key Properties

1. Two types of dirty schedulers: CPU-bound (`ERL_NIF_DIRTY_JOB_CPU_BOUND`) and I/O-bound (`ERL_NIF_DIRTY_JOB_IO_BOUND`)
2. CPU-bound dirty schedulers are configured via `+SDcpu`; I/O-bound via `+SDio`
3. A dirty NIF can be declared statically (via flags in `ErlNifFunc`) or dynamically (via `enif_schedule_nif`)
4. A job that alternates between CPU and I/O work can be reclassified and rescheduled using `enif_schedule_nif`
5. While a process executes a dirty NIF, suspend and garbage collection cannot occur until the NIF returns
6. Process termination is partially handled: Erlang resources (registered name, ETS tables) are released and signals triggered, but NIF execution continues
7. A dirty NIF can check if its process is still alive via `enif_is_current_process_alive`
8. Communication via `enif_send` and `enif_port_command` is silently dropped if the sending process is not alive
9. Blocking multi-scheduling requires all dirty operations on all dirty schedulers to complete first

# Construction / Recognition

## To Construct/Create:

Static declaration in `ErlNifFunc` array:
```c
static ErlNifFunc nif_funcs[] = {
    {"cpu_intensive", 1, cpu_intensive_nif, ERL_NIF_DIRTY_JOB_CPU_BOUND},
    {"blocking_io",   1, blocking_io_nif,   ERL_NIF_DIRTY_JOB_IO_BOUND}
};
```

Dynamic scheduling from within a NIF:
```c
return enif_schedule_nif(env, "do_work", ERL_NIF_DIRTY_JOB_CPU_BOUND,
                         do_work_nif, argc, argv);
```

## To Identify/Recognize:

1. `ErlNifFunc` entries with `flags` set to `ERL_NIF_DIRTY_JOB_CPU_BOUND` or `ERL_NIF_DIRTY_JOB_IO_BOUND`
2. Calls to `enif_schedule_nif` with dirty scheduler flags
3. NIFs that perform blocking operations (file I/O, network calls, heavy computation)

# Context & Application

Dirty schedulers exist because the normal BEAM scheduler is cooperative -- it relies on Erlang reductions and NIF timeslice reporting to maintain fairness. A NIF that blocks for seconds or minutes would starve all other processes on that scheduler thread.

The dirty scheduler pool runs these problematic NIFs on separate threads where they cannot interfere with normal scheduling. However, this comes with trade-offs: processes executing dirty NIFs cannot be suspended or garbage collected until the NIF returns, and blocking multi-scheduling becomes expensive.

The yielding NIF approach (splitting work into chunks via `enif_schedule_nif`) is always preferred from both performance and system characteristics perspectives, because it allows the VM to regain control between chunks. Dirty NIFs are for cases where the work genuinely cannot be split -- typically when calling third-party libraries with blocking APIs.

# Examples

**Example 1** (erl_nif, Functionality, Long-running NIFs, Dirty NIF): Static dirty NIF declaration:

```c
static ErlNifFunc nif_funcs[] = {
    {"compute", 1, compute_nif, ERL_NIF_DIRTY_JOB_CPU_BOUND}
};
```

**Example 2** (erl_nif, Functionality, Long-running NIFs): The yielding NIF pattern (preferred over dirty NIFs):

The source states: "Call a NIF that first performs a chunk of the work, then invokes the `enif_schedule_nif` function to schedule another NIF call to perform the next chunk. The final call scheduled in this manner can then return the overall result."

A job that alternates between I/O and CPU work can be dynamically reclassified:

```c
/* After I/O phase, switch to CPU-bound dirty scheduler */
return enif_schedule_nif(env, "cpu_phase",
                         ERL_NIF_DIRTY_JOB_CPU_BOUND,
                         cpu_phase_nif, argc, argv);
```

# Relationships

## Builds Upon

- **erl-nif** -- Dirty schedulers are part of the NIF infrastructure for handling long-running work

## Related

- **nif-resources** -- Resources used in dirty NIFs require the same synchronization considerations
- **nif-lifecycle** -- Dirty NIF behavior during module upgrade/unload

# Common Errors

- **Error**: Classifying CPU-bound work as I/O-bound
  **Correction**: The source explicitly warns that misclassifying CPU work as I/O can starve ordinary schedulers; use `ERL_NIF_DIRTY_JOB_CPU_BOUND` for computation

- **Error**: Assuming a dirty NIF's process will be cleanly terminated if the process exits
  **Correction**: While Erlang resources are released, the NIF execution continues; use `enif_is_current_process_alive` to check and return early

- **Error**: Using dirty NIFs when the work could be split into chunks
  **Correction**: The yielding NIF approach via `enif_schedule_nif` is explicitly preferred for both performance and system behavior

# Common Confusions

- **Confusion**: Thinking dirty schedulers provide the same guarantees as normal schedulers
  **Clarification**: Processes on dirty schedulers cannot be suspended or garbage collected until the NIF returns; other processes waiting for these operations may wait a very long time

- **Confusion**: Believing dirty NIFs are the primary solution for long-running native work
  **Clarification**: The source explicitly ranks yielding NIFs first, threaded NIFs second, and dirty NIFs third in order of preference

- **Confusion**: Thinking `enif_schedule_nif` is only for dirty NIFs
  **Clarification**: `enif_schedule_nif` can schedule any NIF (regular or dirty) and is the core mechanism for the yielding NIF pattern

# Source Reference

- "erl_nif" reference (Functionality section, "Long-running NIFs" subsection, including "Yielding NIF," "Threaded NIF," and "Dirty NIF" sub-subsections)
- "erl_nif" reference (Data Types: ErlNifFunc `flags` field)

# Verification Notes

- Definition: Directly quoted from erl_nif.md, "Dirty NIF" section
- Classification warning: Directly quoted from source
- Preference order: Explicitly stated in source with yielding NIFs described as "always preferred"
- Process termination behavior: Detailed from the "Dirty NIF" section
- Confidence: HIGH -- dirty NIF behavior is thoroughly documented with explicit guidance
