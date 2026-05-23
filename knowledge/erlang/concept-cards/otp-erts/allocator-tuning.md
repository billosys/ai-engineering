---
concept: Allocator Tuning
slug: allocator-tuning
category: performance
subcategory: memory-management
tier: advanced
source: "ERTS User's Guide"
source_slug: otp-erts
authors: "Ericsson AB"
chapter: "erts_alloc"
chapter_number: null
pdf_page: null
section: "System Flags Effecting erts_alloc"
extraction_confidence: high
aliases:
  - "+M flags"
  - "allocator configuration"
  - "erts_alloc tuning"
  - "memory allocator flags"
prerequisites:
  - erts-alloc
  - memory-carriers
extends:
  - erts-alloc
related:
  - crash-dump
contrasts_with: []
answers_questions:
  - "How do I tune ERTS memory allocators?"
  - "What are the +M flags?"
  - "How do I configure carrier sizes and allocation strategies?"
---

# Quick Definition

Allocator tuning is performed via `+M<S><P> <V>` command-line flags passed to `erl`, where `<S>` identifies the allocator (or `u` for all `alloc_util`-based allocators), `<P>` is the parameter, and `<V>` is the value. Key tuning parameters include singleblock carrier threshold (`sbct`), allocation strategy (`as`), carrier sizes (`mmbcs`, `smbcs`, `lmbcs`), thread-specific instances (`t`), and carrier abandonment (`acul`).

# Core Definition

The ERTS documentation warns: "Only use these flags if you are sure what you are doing. Unsuitable settings can cause serious performance degradation and even a system crash at any time during operation." (erts_alloc, System Flags).

The flag syntax is `+M<S><P> <V>`:
- `<S>` = allocator identifier letter (uppercase) or `u` for all alloc_util allocators
- `<P>` = parameter name
- `<V>` = value

Allocator letter codes:
- B: `binary_alloc`, D: `std_alloc`, E: `ets_alloc`, F: `fix_alloc`
- H: `eheap_alloc`, I: `literal_alloc`, L: `ll_alloc`, M: `mseg_alloc`
- R: `driver_alloc`, S: `sl_alloc`, T: `temp_alloc`, Y: `sys_alloc`

Key parameters for `alloc_util`-based allocators:

- **`sbct`** -- Singleblock carrier threshold (KB): blocks >= this go to SBCs
- **`as`** -- Allocation strategy: `bf`, `aobf`, `aoff`, `aoffcbf`, `aoffcaobf`, `ageffcaoff`, `ageffcbf`, `ageffcaobf`, `gf`, `af`
- **`mmbcs`** -- Main multiblock carrier size (never deallocated)
- **`smbcs`** / **`lmbcs`** -- Smallest/largest `mseg_alloc` MBC sizes
- **`mbcgs`** -- MBC growth stages
- **`t`** -- Enable multiple thread-specific instances (default: `NoSchedulers+1`)
- **`acul`** -- Abandon carrier utilization limit (0-100% or `de` for default)
- **`e`** -- Enable/disable the allocator
- **`atags`** -- Add allocation tags for instrumentation

For `mseg_alloc`:
- **`+MMscs`** -- Super carrier size (MB): large contiguous virtual address space
- **`+MMmcs`** -- Maximum cached segments (0-30, default 10)
- **`+MMlp`** -- Enable large pages for super carrier segments

# Prerequisites

- **erts-alloc** -- The allocator library being tuned
- **memory-carriers** -- Understanding carriers is necessary to interpret tuning parameters

# Key Properties

1. Flags are passed as command-line arguments to `erl`
2. Using `u` as the allocator letter affects ALL `alloc_util`-based allocators at once
3. `erts_alloc` is not obligated to strictly use the provided settings -- it can adjust or ignore them
4. The `+Mea` flag provides preset configurations: `min` (disable all), `max` (enable all, default)
5. Thread-specific instances (`+M<S>t true`) give each scheduler its own lock-free allocator instance
6. Dirty allocator instances (`+Mdai`) give dirty schedulers their own allocator instances to reduce contention
7. Carrier pools (`+M<S>cp`) control which allocator instances can share abandoned carriers
8. The `instrument` module can be used with `+M<S>atags true` to inspect allocation metadata
9. Current settings and status are viewable via `erlang:system_info({allocator, Alloc})`
10. Most flags are highly implementation-dependent and can change or be removed without notice

# Construction / Recognition

## To Construct/Create:

Common tuning scenarios:

```text
# Reduce binary_alloc fragmentation with address-order first fit
erl +MBas aoff

# Increase eheap_alloc main MBC for systems with many processes
erl +MHmmbcs 2048

# Enable carrier abandonment for all alloc_util allocators
erl +Muacul de

# Create a 4GB super carrier with large pages
erl +MMscs 4096 +MMlp on

# Enable dirty allocator instances (one per dirty CPU scheduler)
erl +Mdai max

# Enable allocation tagging for binary_alloc and driver_alloc (default)
erl +MBatags true +MRatags true

# Inspect current settings
erlang:system_info({allocator, binary_alloc}).
```

## To Identify/Recognize:

1. Command-line arguments matching the `+M` prefix pattern
2. `vm.args` or `sys.config` files containing `+M` flags
3. Release configuration setting emulator flags

# Context & Application

Allocator tuning is typically performed reactively -- after observing memory issues in production. The diagnostic workflow is:

1. Check allocator status: `erlang:system_info({allocator, Alloc})`
2. Look for high carrier counts with low utilization (fragmentation)
3. Check if carriers are being abandoned and migrated effectively
4. Examine the allocation strategy and consider alternatives
5. Check crash dumps for allocator statistics

Common production scenarios:

- **Memory not returned to OS**: Often caused by fragmentation in MBCs; consider `+M<S>acul de` for carrier abandonment, or `+M<S>as aoff` strategies
- **Lock contention on allocators**: Ensure thread-specific instances are enabled (`+M<S>t true`, the default)
- **Dirty scheduler contention**: Enable dirty allocator instances with `+Mdai max`
- **Large binary allocation overhead**: Tune `+MBsbct` to control the MBC/SBC threshold for binary_alloc

The source notes: "Most of these flags are highly implementation-dependent and can be changed or removed without prior notice. `erts_alloc` is not obliged to strictly use the settings that have been passed to it (it can even ignore them)."

# Examples

**Example 1** (erts_alloc, System Flags): The flag syntax and allocator letters:

```text
+M<S><P> <V>

Where:
  <S> = B (binary_alloc), D (std_alloc), E (ets_alloc), F (fix_alloc),
        H (eheap_alloc), I (literal_alloc), L (ll_alloc), M (mseg_alloc),
        R (driver_alloc), S (sl_alloc), T (temp_alloc), Y (sys_alloc)
  <P> = parameter name
  <V> = value
```

**Example 2** (erts_alloc, Flags): Thread-specific instances:

"Multiple, thread-specific instances of the allocator. Default behavior is `NoSchedulers+1` instances. Each scheduler uses a lock-free instance of its own and other threads use a common instance."

**Example 3** (erts_alloc, Flags): The `acful` flag for OS-level memory reclamation:

"When the utilization of a carrier falls below this limit erts_alloc instructs the OS that unused memory in the carrier can be re-used for allocation by other OS processes. On Unix this is done by calling `madvise(..., ..., MADV_FREE)` on the unused memory region."

# Relationships

## Builds Upon

- **erts-alloc** -- The allocator library being configured
- **memory-carriers** -- Tuning parameters directly affect carrier behavior

## Related

- **crash-dump** -- Crash dumps contain allocator statistics useful for tuning decisions

# Common Errors

- **Error**: Tuning allocator parameters without understanding the current state
  **Correction**: Always check `erlang:system_info({allocator, Alloc})` first to understand current behavior before making changes

- **Error**: Applying the same tuning to all allocators indiscriminately (e.g., `+Muas aoff`)
  **Correction**: Different allocators benefit from different strategies; `temp_alloc` should use `af`, while `binary_alloc` might benefit from `aoff`

- **Error**: Setting `+Mea min` in production
  **Correction**: Disabling allocators forces everything through `sys_alloc`, destroying the fragmentation benefits of specialized allocation

# Common Confusions

- **Confusion**: Thinking `+M` flags are guaranteed to be respected exactly
  **Clarification**: The source explicitly states "`erts_alloc` is not obliged to strictly use the settings that have been passed to it (it can even ignore them)"

- **Confusion**: Believing carrier abandonment is enabled by default for all strategies
  **Clarification**: Abandonment defaults to `de` but only works with specific strategies; if the current strategy does not support it, enabling `acul` also switches the strategy to `aoffcbf`

- **Confusion**: Thinking `+MHmmbcs` controls the total memory available to `eheap_alloc`
  **Clarification**: It only sets the size of the main (initial, never-freed) multiblock carrier; the allocator creates additional carriers as needed

# Source Reference

- "erts_alloc" reference (System Flags Effecting erts_alloc, including all flag subsections)
- "erts_alloc" reference (Notes section)

# Verification Notes

- Warning: Directly quoted from erts_alloc.md System Flags section
- Flag syntax: From erts_alloc.md
- Allocator letter codes: Complete list from source
- Parameter descriptions: Summarized from individual flag documentation
- "Not obliged" quote: Directly from erts_alloc.md Notes
- Confidence: HIGH -- all flags are individually documented in the source
