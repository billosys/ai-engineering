---
concept: Atom Creation Safety
slug: atom-creation-safety
category: anti-patterns
subcategory: resource-exhaustion
tier: intermediate
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Common Caveats"
chapter_number: null
pdf_page: null
section: "list_to_atom/1, binary_to_atom/1,2"
extraction_confidence: high
aliases:
  - "atom table exhaustion"
  - "atom leak"
  - "list_to_atom safety"
  - "binary_to_atom safety"
prerequisites:
  - erlang-system-limits
extends: []
related:
  - erlang-data-type-memory-sizes
contrasts_with: []
answers_questions:
  - "Why is converting arbitrary input to atoms dangerous?"
  - "How can atom creation lead to denial-of-service?"
  - "What are safe alternatives to list_to_atom/1?"
---

# Quick Definition

Atoms are never garbage-collected, and the emulator terminates when the atom limit (1,048,576 by default) is reached. Converting arbitrary input strings to atoms via `list_to_atom/1` or `binary_to_atom/1,2` can exhaust the atom table and crash the system.

# Core Definition

Atoms are not garbage-collected in Erlang. Once an atom is created, it is never removed. The emulator terminates if the limit for the number of atoms (1,048,576 by default) is reached. Therefore, converting arbitrary input strings or binaries to atoms can be dangerous in a system that runs continuously (Ericsson/OTP Team, "Common Caveats," section "list_to_atom/1, binary_to_atom/1,2").

If only certain well-defined atoms are allowed as input, the safe alternatives `list_to_existing_atom/1`, `binary_to_existing_atom/1`, or `binary_to_existing_atom/2` can be used to guard against denial-of-service attacks. All atoms that are allowed must have been created earlier, for example by using them in a module and loading that module.

Additionally, using `list_to_atom/1`, `binary_to_atom/1`, or `binary_to_atom/2` to construct an atom that is then passed to `apply/3` is quite expensive.

# Prerequisites

- **erlang-system-limits** -- Understanding the atom limit (default 1,048,576) and that it is a hard system constraint

# Key Properties

1. Atoms are never garbage-collected
2. The emulator terminates (crashes) when the atom limit is reached
3. Default atom limit is 1,048,576
4. `list_to_atom/1`, `binary_to_atom/1`, and `binary_to_atom/2` create new atoms from arbitrary input
5. `list_to_existing_atom/1`, `binary_to_existing_atom/1,2` only succeed if the atom already exists
6. Constructing atoms dynamically for use with `apply/3` is expensive
7. Pre-creating allowed atoms (e.g., by referencing them in a loaded module) enables safe use of `*_to_existing_atom` functions

# Construction / Recognition

## Recognizing the Anti-Pattern

1. Search for calls to `list_to_atom/1`, `binary_to_atom/1`, or `binary_to_atom/2`
2. Check whether the input comes from external/untrusted sources (user input, network data, files)
3. If external input can produce arbitrary strings, this is a potential atom exhaustion vulnerability

## Applying the Fix

1. Replace `list_to_atom/1` with `list_to_existing_atom/1`
2. Replace `binary_to_atom/1,2` with `binary_to_existing_atom/1,2`
3. Ensure all valid atoms are pre-created (e.g., referenced in a module that is loaded at startup)
4. Handle the `badarg` error that occurs when the atom does not exist

# Context & Application

This is a security and reliability concern for any Erlang system that processes external input. It is particularly relevant in:

- Web servers and API handlers that parse user-supplied data
- Protocol parsers converting wire format strings to atoms
- Configuration parsers that convert arbitrary keys to atoms
- Any long-running system where atom accumulation can occur over time

The issue is a potential denial-of-service vector: an attacker who can cause the system to create atoms from arbitrary input can crash the entire Erlang node by exhausting the atom table.

# Examples

**DO NOT** -- Dynamic atom construction for apply (source: "Common Caveats," section "list_to_atom/1, binary_to_atom/1,2"):

```erlang
apply(list_to_atom("some_prefix" ++ Var), foo, Args)
```

```erlang
apply(binary_to_atom(<<"some_prefix", Var/binary>>), foo, Args)
```

```erlang
apply(binary_to_atom(<<"some_prefix", Var/binary>>, utf8), foo, Args)
```

**DO** -- Use existing atom variants for untrusted input:

```erlang
try list_to_existing_atom(Input) of
    Atom -> handle(Atom)
catch
    error:badarg -> {error, unknown_atom}
end
```

# Relationships

## Related

- **erlang-data-type-memory-sizes** -- Atoms consume 1 word in the process heap plus space in the global atom table
- **erlang-system-limits** -- The atom limit is documented as a system limit (1,048,576 default, configurable with `+t`)

# Common Errors

- **Error**: Using `list_to_atom/1` to convert user-supplied HTTP parameters to atoms
  **Correction**: Use `list_to_existing_atom/1` and pre-define the valid atom set

- **Error**: Building module names dynamically with `list_to_atom/1` for plugin systems
  **Correction**: Maintain an explicit allowlist of valid module atoms, or use `list_to_existing_atom/1`

# Common Confusions

- **Confusion**: Believing atoms are garbage-collected like other Erlang terms
  **Clarification**: Atoms are permanent. Once created, they exist for the lifetime of the VM. There is no atom GC.

- **Confusion**: Thinking the atom limit can be removed entirely
  **Clarification**: The limit can be raised with the `+t` flag, but there is always a finite limit, and each atom consumes memory permanently

# Source Reference

"Common Caveats," section "list_to_atom/1, binary_to_atom/1,2." The source covers the non-GC nature of atoms, the default limit, the existing-atom alternatives, and provides three DO NOT examples of dynamic atom construction with `apply/3`.

# Verification Notes

- Definition: Direct from source -- "Atoms are not garbage-collected. Once an atom is created, it is never removed."
- Default limit (1,048,576): Explicit in source
- Safe alternatives: Explicitly listed in source
- DO NOT examples: Verbatim from source
- Confidence: HIGH -- explicit documentation with clear recommendations from official OTP guide
