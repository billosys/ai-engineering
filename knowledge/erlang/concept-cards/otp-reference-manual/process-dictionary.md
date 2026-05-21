---
# === CORE IDENTIFICATION ===
concept: Process Dictionary
slug: process-dictionary

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Processes"
chapter_number: null
pdf_page: null
section: "Process Dictionary"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - process dict
  - per-process dictionary

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-process
extends: []
related:
  - process-termination
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How can a process store mutable key-value state?"
  - "What BIFs access the process dictionary?"
  - "Is the process dictionary shared between processes?"
---

# Quick Definition
The process dictionary is a per-process key-value store that provides mutable state within a single process. It is accessed through the BIFs `put/2`, `get/0,1`, `get_keys/1`, and `erase/0,1`.

# Core Definition
The Erlang Reference Manual states: "Each process has its own process dictionary, accessed by calling the following BIFs: `put(Key, Value)`, `get(Key)`, `get()`, `get_keys(Value)`, `erase(Key)`, `erase()`." (Processes chapter, "Process Dictionary" section). The process dictionary is private to each process -- no other process can read or modify it. It provides a side-effect-based storage mechanism that persists for the lifetime of the process.

# Prerequisites
- **erlang-process** -- The process dictionary exists within a process and is private to it

# Key Properties
1. Each process has exactly one process dictionary
2. The dictionary is private -- only the owning process can access it
3. It provides mutable key-value storage via `put/2` and `get/1`
4. `put(Key, Value)` stores a value and returns the old value (or `undefined` if no previous value)
5. `get(Key)` retrieves the value for a key (or `undefined` if not found)
6. `get()` returns the entire dictionary as a list of `{Key, Value}` tuples
7. `get_keys(Value)` returns all keys associated with a given value
8. `erase(Key)` removes a key and returns its value
9. `erase()` removes all entries and returns the full dictionary
10. The dictionary is destroyed when the process terminates

# Construction / Recognition
## To Use:
1. `put(Key, Value)` -- store a key-value pair; returns the previous value or `undefined`
2. `get(Key)` -- retrieve a value by key; returns `undefined` if not present
3. `get()` -- retrieve the entire dictionary as `[{Key, Value}]`
4. `get_keys(Value)` -- find all keys with a specific value
5. `erase(Key)` -- delete a single entry; returns the removed value
6. `erase()` -- delete all entries; returns the full former dictionary

## To Identify/Recognize:
1. Any call to `put/2`, `get/0,1`, `get_keys/1`, or `erase/0,1` operates on the calling process's dictionary
2. Use `process_info(Pid, dictionary)` to inspect another process's dictionary (for debugging)

# Context & Application
The process dictionary is a pragmatic escape hatch from Erlang's immutable-variable model. It allows state to be stored implicitly rather than threaded through function arguments. However, it introduces side effects and makes code harder to reason about, test, and debug.

**Typical contexts:**
- OTP frameworks use the process dictionary internally (e.g., `$ancestors`, `$initial_call`)
- Storing metadata that would be impractical to thread through every function call
- Random number generator state (legacy usage; modern code uses `rand` module state)

**When NOT to use:**
- For general application state -- use explicit state in `gen_server` or function arguments instead
- When testability matters -- process dictionary usage makes functions impure and harder to test in isolation
- The OTP design guidelines generally discourage direct use of the process dictionary in application code

# Examples
**Example 1** (Processes, "Process Dictionary" section): The six BIFs for process dictionary access:
```erlang
put(name, "Alice"),          %% returns undefined (no previous value)
put(name, "Bob"),            %% returns "Alice" (previous value)
get(name),                   %% returns "Bob"
get(),                       %% returns [{name, "Bob"}]
get_keys("Bob"),             %% returns [name]
erase(name),                 %% returns "Bob", removes the entry
erase().                     %% returns [], dictionary is empty
```

# Relationships
## Builds Upon
- **erlang-process** -- The process dictionary is an inherent part of each process

## Enables
Nothing directly -- the process dictionary is a utility mechanism.

## Related
- **process-termination** -- The process dictionary is destroyed when the process terminates

## Contrasts With
No direct contrasts within this source.

# Common Errors
- **Error**: Assuming the process dictionary persists after process termination
  **Correction**: The process dictionary is destroyed when its owning process terminates. If the data must survive, it should be sent to another process or stored in ETS/persistent storage before termination.

- **Error**: Using the process dictionary as a substitute for proper state management
  **Correction**: In OTP applications, use `gen_server` state, explicit function arguments, or ETS tables for application state. The process dictionary should be reserved for framework-level metadata.

# Common Confusions
- **Confusion**: Thinking the process dictionary is shared or accessible from other processes
  **Clarification**: The process dictionary is completely private to the owning process. While `process_info(Pid, dictionary)` can inspect another process's dictionary, this is a debugging tool and involves signal exchange -- it is not a shared-memory mechanism.

# Source Reference
Processes chapter, "Process Dictionary" section.

# Verification Notes
- Definition source: Direct from source -- the BIF list is explicitly enumerated
- Confidence rationale: High -- concise, self-contained section with complete API listing
- Uncertainties: None -- the source is brief but complete
- Cross-reference status: Minimal relationships; this is a relatively isolated concept
