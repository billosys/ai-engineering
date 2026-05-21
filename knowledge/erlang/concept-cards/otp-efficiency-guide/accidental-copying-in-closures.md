---
concept: Accidental Copying in Closures
slug: accidental-copying-in-closures
category: performance
subcategory: process-spawning
tier: intermediate
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Common Caveats"
chapter_number: null
pdf_page: null
section: "Accidental Copying and Loss of Sharing"
extraction_confidence: high
aliases:
  - "closure data capture"
  - "fun environment copying"
  - "accidental data copying"
prerequisites:
  - erlang-data-type-memory-sizes
extends: []
related:
  - append-operator-efficiency
  - loss-of-sharing
contrasts_with: []
answers_questions:
  - "How do I avoid accidental data copying when spawning processes with closures?"
  - "What is loss of sharing when copying terms?"
  - "Why does spawning with a fun copy the entire closure environment?"
---

# Quick Definition

When a fun (closure) references a variable, the entire value bound to that variable is copied into the spawned process's heap -- even if the fun only uses a small part of it. Extracting needed fields before the fun avoids copying unnecessary data.

# Core Definition

When spawning a new process using a fun, one can accidentally copy more data to the process than intended. If a fun references a variable that holds a large data structure (such as a record or map), the entire structure is copied into the new process's heap when `spawn/1` executes, even if the fun only accesses a single field. This applies equally to records, maps, and any compound term captured by the closure (Ericsson/OTP Team, "Common Caveats," section "Accidental Copying and Loss of Sharing").

The problem is compounded when the captured data contains shared subterms, because sharing is lost during inter-process copying (see related concept: loss-of-sharing).

# Prerequisites

- **erlang-data-type-memory-sizes** -- Understanding memory sizes of records, lists, and tuples is needed to appreciate the cost of accidental copying

# Key Properties

1. A fun captures all variables it references from its enclosing scope
2. The entire value bound to a referenced variable is copied, not just the accessed parts
3. The copy happens when the fun is used with `spawn/1` or sent to another process
4. Records, maps, and any compound terms are affected equally
5. The severity depends on the size of the captured data structure
6. Loss of sharing during copying can cause the copy to be many times larger than the original

# Construction / Recognition

## Recognizing the Anti-Pattern

1. Look for `spawn/1` or message-sending with a fun argument
2. Check if the fun references a variable bound to a large structure (record, map, etc.)
3. Verify whether the fun uses only a subset of that structure's fields
4. If yes, the unused fields are being copied unnecessarily

## Applying the Fix

1. Before the fun, extract only the fields or map values actually needed
2. Bind these extracted values to local variables
3. Reference only the local variables inside the fun

# Context & Application

This caveat is particularly dangerous in `gen_server` and other OTP behavior implementations where the `State` variable often contains a large, complex data structure. Common scenarios include:

- Spawning worker processes that need only a piece of the server state
- Sending funs as messages to other processes
- Creating funs in `handle_call/3` callbacks that capture the entire state record

**Severity example from source:** A state record initialized with `lists:seq(1, 10000)` copies about 20,000 heap words unnecessarily. With shared subterms, a 32-word structure can expand to 131,070 words when copied due to loss of sharing.

# Examples

**DO NOT** -- Fun captures entire record (source: "Common Caveats," section "Accidental Copying and Loss of Sharing"):

```erlang
accidental1(State) ->
    spawn(fun() ->
                  io:format("~p\n", [State#state.info])
          end).
```

The fun only uses `State#state.info`, but the entire `State` record is copied to the new process.

**DO NOT** -- Same problem with maps (source: same section):

```erlang
accidental2(State) ->
    spawn(fun() ->
                  io:format("~p\n", [map_get(info, State)])
          end).
```

**DO NOT** -- Fun sent as a reply captures entire state (source: same section):

```erlang
handle_call(give_me_a_fun, _From, State) ->
    Fun = fun() -> State#state.size =:= 42 end,
    {reply, Fun, State}.
```

**DO** -- Extract needed fields before the fun (source: same section):

```erlang
fixed_accidental1(State) ->
    Info = State#state.info,
    spawn(fun() ->
                  io:format("~p\n", [Info])
          end).
```

**DO** -- Same fix for maps (source: same section):

```erlang
fixed_accidental2(State) ->
    Info = map_get(info, State),
    spawn(fun() ->
                  io:format("~p\n", [Info])
          end).
```

# Relationships

## Related

- **append-operator-efficiency** -- Another form of unintended data copying in common Erlang patterns
- **loss-of-sharing** -- Shared subterms are lost during inter-process copying, amplifying the accidental copy problem

# Common Errors

- **Error**: Referencing a state record inside a spawned fun when only one field is needed
  **Correction**: Bind the needed field to a variable outside the fun, then reference only that variable

- **Error**: Assuming the runtime is smart enough to copy only the accessed fields
  **Correction**: Erlang copies the entire term bound to each captured variable; there is no partial copying

# Common Confusions

- **Confusion**: Believing this only affects `spawn/1`
  **Clarification**: Any mechanism that sends a fun to another process (message passing, `gen_server` replies) triggers the same copying behavior

- **Confusion**: Thinking the size of the copy equals the size of the original
  **Clarification**: Due to loss of sharing, the copy can be vastly larger than the original (the source gives an example where 32 words become 131,070 words)

# Source Reference

"Common Caveats," section "Accidental Copying and Loss of Sharing." The source provides three DO NOT examples (record, map, gen_server fun), two DO examples (fixed versions), and a detailed quantitative example showing loss of sharing amplification (32 words -> 131,070 words).

# Verification Notes

- Definition: Directly stated in source -- "when spawning a new process using a fun, one can accidentally copy more data to the process than intended"
- All examples: Verbatim from source
- Quantitative figures (20,000 words, 32 -> 131,070 words): Explicit in source
- Loss of sharing reference: Source explicitly links to a later section
- Confidence: HIGH -- extensive examples and detailed explanation in official OTP guide
