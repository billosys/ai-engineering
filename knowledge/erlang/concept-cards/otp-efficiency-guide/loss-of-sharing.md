---
concept: Loss of Sharing
slug: loss-of-sharing
category: memory-management
subcategory: null
tier: intermediate
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Processes"
chapter_number: null
pdf_page: null
section: "Loss of Sharing"
extraction_confidence: high
aliases:
  - "shared subterm loss"
  - "subterm sharing"
  - "term sharing loss"
  - "shared subterm flattening"
prerequisites:
  - erlang-process-creation
  - message-sending-cost
extends: []
related:
  - literal-pool
  - accidental-copying-in-closures
contrasts_with: []
answers_questions:
  - "What is loss of sharing when copying terms?"
  - "How do I avoid accidental data copying when spawning processes with closures?"
  - "Why does sending a compact data structure result in much higher memory usage?"
  - "Why can a copied term be many times larger than the original?"
  - "How do shared subterms affect inter-process data copying?"
---

# Quick Definition

Loss of sharing occurs when an Erlang term with shared subterms is copied (via message send, `spawn`, or ETS insert), causing the shared subterms to be duplicated -- potentially expanding a compact 22-word structure into a 4,094-word flat copy.

# Core Definition

An Erlang term can have shared subterms -- for example, `{SubTerm, SubTerm}` where both elements point to the same underlying data. Shared subterms are NOT preserved in the following cases:

- When a term is sent to another process
- When a term is passed as the initial process arguments in the `spawn` call
- When a term is stored in an ETS table

This is an intentional optimization: most applications do not send messages with shared subterms. However, when sharing IS present, the flattened copy can be dramatically larger than the original. The diagnostic tools `erts_debug:size/1` (reports size with sharing) and `erts_debug:flat_size/1` (reports size without sharing, i.e., the copy size) can be used to measure the impact (Ericsson/OTP Team, "Processes" chapter, "Loss of Sharing" section).

It is possible to build an experimental variant of the runtime system that will preserve sharing when copying terms by giving the `--enable-sharing-preserving` option to the `configure` script.

# Prerequisites

- **erlang-process-creation** -- Understanding process isolation and independent heaps is needed to understand why copying occurs
- **message-sending-cost** -- Loss of sharing is a consequence of the message-copying mechanism

# Key Properties

1. Shared subterms are internal pointers to the same data within a process heap
2. Copying a term with shared subterms produces a flat copy where each reference becomes a separate copy
3. Three operations cause loss of sharing: message send, spawn arguments, ETS insert
4. The size explosion can be dramatic (e.g., 22 words to 4,094 words in the source example)
5. This behavior is an intentional optimization for the common case (most terms have no sharing)
6. An experimental `--enable-sharing-preserving` configure option exists to build a runtime that preserves sharing
7. `erts_debug:size/1` reports the size with sharing; `erts_debug:flat_size/1` reports the size without sharing

# Construction / Recognition

## To Detect Sharing in a Term

1. Use `erts_debug:size/1` to get the actual heap size (preserving sharing)
2. Use `erts_debug:flat_size/1` to get the flat size (as if sharing were lost)
3. If `flat_size` is much greater than `size`, the term has significant sharing

## To Create a Term with Sharing (Demonstration)

```erlang
kilo_byte() ->
    kilo_byte(10, [42]).

kilo_byte(0, Acc) ->
    Acc;
kilo_byte(N, Acc) ->
    kilo_byte(N-1, [Acc|Acc]).
```

This creates a deep list where each cons cell shares its sublists. The result is 1,024 bytes of data represented in only 22 words of heap space.

# Context & Application

Loss of sharing is a subtle source of memory problems in Erlang systems. It most commonly affects code that builds data structures with internal sharing (often through recursive list construction) and then sends them between processes or stores them in ETS.

**Typical contexts:**

- Sending deeply shared data structures between processes
- Passing shared-subterm arguments to `spawn` (including closures that capture shared data)
- Inserting shared-subterm data into ETS tables
- Debugging unexpected memory usage spikes

**Important note for spawn:** When data is passed as initial process arguments in a `spawn` call, sharing is lost. This includes data captured in closures passed to `spawn/1` and `spawn/3`. This is the mechanism behind "accidental data copying when spawning processes with closures."

# Examples

**Example 1** (Processes chapter, "Loss of Sharing" section): Building a term with sharing:

```erlang
kilo_byte() ->
    kilo_byte(10, [42]).

kilo_byte(0, Acc) ->
    Acc;
kilo_byte(N, Acc) ->
    kilo_byte(N-1, [Acc|Acc]).
```

The result converts to a 1,024-byte binary:
```erlang
1> byte_size(list_to_binary(efficiency_guide:kilo_byte())).
1024
```

But uses only 22 words of heap space due to sharing:
```erlang
2> erts_debug:size(efficiency_guide:kilo_byte()).
22
```

The flat size (what it becomes after copying) is 4,094 words:
```erlang
3> erts_debug:flat_size(efficiency_guide:kilo_byte()).
4094
```

**Example 2** (Processes chapter): Verifying sharing loss through ETS:

```erlang
4> T = ets:new(tab, []).
#Ref<0.1662103692.2407923716.214181>
5> ets:insert(T, {key,efficiency_guide:kilo_byte()}).
true
6> erts_debug:size(element(2, hd(ets:lookup(T, key)))).
4094
7> erts_debug:flat_size(element(2, hd(ets:lookup(T, key)))).
4094
```

After passing through ETS, `erts_debug:size/1` and `erts_debug:flat_size/1` return the same value (4,094) -- sharing has been lost.

# Relationships

## Related

- **literal-pool** -- Like shared subterms, literals have special copy semantics that can lead to unexpected memory behavior
- **message-sending-cost** -- Loss of sharing is a direct consequence of message copying between processes
- **accidental-copying-in-closures** -- Loss of sharing amplifies the cost of accidental copying through closures

# Common Errors

- **Error**: Building data structures with heavy internal sharing and then sending them to other processes, expecting compact representation
  **Correction**: Measure with `erts_debug:size/1` vs. `erts_debug:flat_size/1` before sending; if flat_size is much larger, consider restructuring the data or serializing it differently

- **Error**: Capturing large shared data structures in closures passed to `spawn`
  **Correction**: Be aware that all data in spawn arguments is copied with sharing lost. Pass only the data the new process actually needs, or use ETS/persistent_term as a shared data store

- **Error**: Estimating copy cost based on the in-process size of a term
  **Correction**: Terms with shared subterms can be vastly larger when copied; measure the flat size with `erts_debug:flat_size/1` to get the true copy size

# Common Confusions

- **Confusion**: Believing that Erlang preserves structural sharing across process boundaries
  **Clarification**: Erlang intentionally does NOT preserve sharing during copying. This is an optimization for the common case. An experimental `--enable-sharing-preserving` configure option exists but is not the default

- **Confusion**: Thinking that `erts_debug:size/1` shows the size after copying
  **Clarification**: `erts_debug:size/1` shows the actual heap usage (with sharing preserved). Use `erts_debug:flat_size/1` to see what the size would be after copying (without sharing)

- **Confusion**: Assuming loss of sharing only matters for messages
  **Clarification**: It affects three operations: message sends, spawn arguments, AND ETS inserts. All three flatten shared subterms

# Source Reference

"Processes" chapter, "Loss of Sharing" section. Includes the `kilo_byte/0` example function, shell sessions demonstrating `erts_debug:size/1` vs. `erts_debug:flat_size/1`, ETS verification, and mention of the `--enable-sharing-preserving` configure option. Also discussed in "Common Caveats" chapter, section "Accidental Copying and Loss of Sharing" with additional quantitative examples.

# Verification Notes

- Definition: Directly from source, first paragraphs of "Loss of Sharing" section in Processes chapter
- The three cases (message send, spawn, ETS) are listed explicitly as a bulleted list in the source
- The kilo_byte example and all shell session values (22, 4094, 1024) are from the source
- The `--enable-sharing-preserving` option is mentioned in the source's final paragraph
- The source explicitly states this is "an optimization. Most applications do not send messages with shared subterms."
- Re-extracted to incorporate Processes chapter material over earlier extraction from Common Caveats chapter; preserved existing aliases and CQ links from prior card
- Confidence: HIGH -- explicit definition with comprehensive worked examples in official documentation
- Cross-references: All slug references verified against planned extractions
- Uncertainties: None
