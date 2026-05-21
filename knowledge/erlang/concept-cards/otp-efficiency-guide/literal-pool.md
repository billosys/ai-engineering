---
concept: Literal Pool
slug: literal-pool
category: performance
subcategory: null
tier: intermediate
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Processes"
chapter_number: null
pdf_page: null
section: "Literal Pool"
extraction_confidence: high
aliases:
  - "constant pool"
  - "module literal pool"
  - "global literal pool"
  - "persistent_term pool"
prerequisites:
  - erlang-process-creation
  - message-sending-cost
extends: []
related:
  - loss-of-sharing
  - initial-heap-size-tuning
contrasts_with: []
answers_questions:
  - "What is a literal pool in Erlang?"
  - "When are literals copied and when are they shared?"
  - "How do I configure the virtual address space reserved for literals?"
---

# Quick Definition

A literal pool is a region of memory where constant Erlang terms (literals) are stored per-module, avoiding repeated construction of the same term. Literals are not copied when sent between processes on the same node, but are copied when inserted into ETS tables or when the owning module is unloaded.

# Core Definition

Constant Erlang terms (called _literals_) are kept in _literal pools_; each loaded module has its own pool. A function referencing a literal does not rebuild the term on every call -- the term is located in the module's literal pool. There also exists a global literal pool managed by the `persistent_term` module.

Copying behavior for literals:
- When inserted into an ETS table: the literal is **copied** (because the owning module could be unloaded)
- When sent to another process on the same node: the literal is **not** copied
- When the module holding a literal is unloaded: the literal is **copied** to the heap of all processes that hold references to it

By default, 1 GB of virtual address space is reserved for all literal pools (in BEAM code and persistent terms). This can be changed with the `+MIscs` option (Ericsson/OTP Team, "Processes" chapter, "Literal Pool" section).

# Prerequisites

- **erlang-process-creation** -- Understanding process heaps is needed to understand where literals live vs. where process data lives
- **message-sending-cost** -- Literals are an exception to the message-copying rule

# Key Properties

1. Each loaded module has its own literal pool
2. A global literal pool exists, managed by `persistent_term`
3. Literals are NOT reconstructed on each function call -- they reference the pool
4. Literals are NOT copied when sent to another process on the same node
5. Literals ARE copied when inserted into an ETS table
6. When a module is unloaded, its literals are copied to the heaps of all referencing processes
7. Default virtual address space for all literal pools: 1 GB
8. The reserved space can be adjusted with `+MIscs` (in MB)

# Construction / Recognition

## To Use Literals Efficiently

1. Define constant terms inline in functions -- they automatically go into the module's literal pool
2. For globally shared constants, use `persistent_term` which manages the global literal pool
3. Be aware that ETS insertion copies literals

## To Adjust Literal Pool Address Space

Raise the reserved virtual address space to 2 GB:
```
erl +MIscs 2048
```

# Context & Application

Literal pools are an important optimization in the BEAM VM. They prevent the repeated allocation and garbage collection of constant terms, and they enable zero-copy message passing for constants between processes on the same node.

**Typical contexts:**

- Defining lookup tables or constant data structures in modules
- Using `persistent_term` for application-wide configuration that rarely changes
- Understanding why ETS inserts of constant data may use more memory than expected
- Hot code loading scenarios where module unloading triggers literal copying

**Important consideration for module unloading:** When a module is unloaded, all its literals must be copied to the heaps of processes holding references. In systems with many processes referencing the same literals, this can cause a significant spike in memory usage and GC activity.

# Examples

**Example 1** (Processes chapter, "Literal Pool" section): A function using a literal tuple that is NOT reconstructed on each call:

```erlang
days_in_month(M) ->
    element(M, {31,28,31,30,31,30,31,31,30,31,30,31}).
```

The tuple `{31,28,31,30,31,30,31,31,30,31,30,31}` is stored in the module's literal pool. It is not rebuilt on every invocation and not discarded by the garbage collector.

**Example 2** (Processes chapter): Adjusting the virtual address space for literals:

```
erl +MIscs 2048
```

This raises the reserved virtual address space for literals from the default 1 GB to 2 GB (2048 MB).

# Relationships

## Related

- **loss-of-sharing** -- Like shared subterms, literals have special copy semantics that can lead to unexpected memory behavior
- **initial-heap-size-tuning** -- Literals do not consume process heap space, so they do not count toward heap sizing
- **message-sending-cost** -- Literals are one of the two exceptions to the message-copying rule (along with refc binaries)

# Common Errors

- **Error**: Assuming that a constant term embedded in a function is rebuilt on every call
  **Correction**: The compiler places constant terms in the module's literal pool; they are stored once and referenced thereafter

- **Error**: Not accounting for literal copying when planning module hot-upgrades in production
  **Correction**: When a module is unloaded, its literals are copied to all processes that reference them. Plan for the memory spike during code upgrades

# Common Confusions

- **Confusion**: Believing literals are always zero-copy everywhere
  **Clarification**: Literals are NOT copied in local message sends, but they ARE copied when inserted into ETS tables (because the module could be unloaded) and they are copied to process heaps when the module is unloaded

- **Confusion**: Conflating module literal pools with the `persistent_term` global pool
  **Clarification**: Each module has its own literal pool for its embedded constants. The `persistent_term` module manages a separate, global literal pool. Both share the same reserved virtual address space configured by `+MIscs`

# Source Reference

"Processes" chapter, "Literal Pool" section. Includes the `days_in_month/1` example, copy semantics for ETS and message sending, module unloading behavior, `persistent_term` mention, and `+MIscs` configuration.

# Verification Notes

- Definition: Directly from source, opening paragraph of "Literal Pool" section
- Copying rules (ETS, message send, module unload): Each explicitly stated in source text
- The 1 GB default and `+MIscs` option: Explicit in source with example
- The `persistent_term` global pool: Mentioned explicitly in source
- The `days_in_month/1` example: Taken directly from source
- Confidence: HIGH -- explicit definition with clear semantics and examples in official documentation
- Cross-references: All slug references verified against planned extractions
- Uncertainties: None
