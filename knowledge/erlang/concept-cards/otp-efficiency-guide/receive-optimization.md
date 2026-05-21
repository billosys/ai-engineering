---
concept: Receive Optimization
slug: receive-optimization
category: performance
subcategory: null
tier: intermediate
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Processes"
chapter_number: null
pdf_page: null
section: "Fetching Received Messages"
extraction_confidence: high
aliases:
  - "selective receive optimization"
  - "receive marker optimization"
  - "message queue optimization"
prerequisites:
  - erlang-process-creation
  - message-sending-cost
extends: []
related:
  - recv-opt-info
  - tail-recursive-main-loop
contrasts_with: []
answers_questions:
  - "How do I optimize receive operations to avoid scanning the full message queue?"
  - "How does the compiler optimize selective receive with monitor references?"
---

# Quick Definition

The Erlang compiler can optimize `receive` expressions that match on a reference created by `monitor/2` or `make_ref/0`, allowing the emulator to skip messages that arrived before the reference was created instead of scanning the entire message queue.

# Core Definition

The cost of fetching a received message from the message queue depends on how complicated the `receive` expression is. A simple expression that matches any message retrieves the first message in the queue and is very cheap. However, a selective `receive` that matches only specific messages must search the entire message queue until it finds a match, which is very expensive for processes with long message queues.

The compiler provides an optimization for the common pattern of sending a request and waiting for a response: when a `receive` expression matches on a reference created by `monitor/2` or `make_ref/0`, the compiler knows that reference cannot exist in any message that arrived before the call. It tells the emulator to search only messages that arrived after the reference-creating call, effectively marking the queue position (Ericsson/OTP Team, "Processes" chapter, "Fetching Received Messages" section).

# Prerequisites

- **erlang-process-creation** -- Understanding processes and their message queues is required to understand receive behavior
- **message-sending-cost** -- Understanding how messages are sent and copied is foundational to understanding receive patterns

# Key Properties

1. A non-selective `receive` (matching any message) is always fast -- it takes the first message in the queue
2. A selective `receive` must search the entire message queue for a matching message
3. The optimization kicks in when all clauses match a reference from `monitor/2` or `make_ref/0`
4. The compiler marks the queue position at the point where the reference was created
5. Only messages arriving AFTER the reference creation are searched
6. The optimization works across function boundaries (the reference can be passed as a parameter)
7. The reference must be a "suitable reference" -- globally unique identifiers like monitor refs or `make_ref/0` results

# Construction / Recognition

## To Use the Optimization

1. Create a reference using `monitor/2` or `make_ref/0`
2. Send a request that includes the reference
3. Immediately follow with a `receive` where ALL clauses match on the reference
4. The compiler will automatically apply the optimization

## Pattern: Monitor-Based Request/Response

```erlang
MRef = monitor(process, Process),
Process ! {self(), MRef, Request},
receive
    {MRef, Reply} ->
        erlang:demonitor(MRef, [flush]),
        handle_reply(Reply);
    {'DOWN', MRef, _, _, Reason} ->
        handle_error(Reason)
end.
```

## Pattern: Cross-Function Reference Passing

```erlang
cross_function_receive() ->
    Ref = make_ref(),
    cross_function_receive(Ref).

cross_function_receive(Ref) ->
    receive
        {Ref, Message} -> handle_msg(Message)
    end.
```

# Context & Application

This optimization is critical for processes that handle high message volumes or have large message queues. Without it, every selective receive would scan the entire queue from the beginning, turning O(1) expected operations into O(n) worst-case scans.

**Typical contexts:**

- gen_server call implementations (gen:call uses monitor-based receive)
- Request/response patterns between processes
- Any process that sends a request and waits for a specific reply
- High-throughput servers where message queue depth may fluctuate

**Why it matters:** In production systems, a process may have thousands of messages in its queue. Without this optimization, each selective receive would scan all of them, leading to quadratic performance degradation as the queue grows.

# Examples

**Example 1** (Processes chapter, "Fetching Received Messages" section): A simple, always-fast receive:

```erlang
receive
    Message -> handle_msg(Message)
end.
```

**Example 2** (Processes chapter): Optimized receive using `monitor/2`:

```erlang
MRef = monitor(process, Process),
Process ! {self(), MRef, Request},
receive
    {MRef, Reply} ->
        erlang:demonitor(MRef, [flush]),
        handle_reply(Reply);
    {'DOWN', MRef, _, _, Reason} ->
        handle_error(Reason)
end.
```

The compiler knows `MRef` cannot exist before the `monitor/2` call and tells the emulator to search only messages that arrived after that call.

**Example 3** (Processes chapter): Cross-function optimization -- the reference is passed as a parameter and the optimization still applies:

```erlang
cross_function_receive() ->
    Ref = make_ref(),
    cross_function_receive(Ref).

cross_function_receive(Ref) ->
    receive
        {Ref, Message} -> handle_msg(Message)
    end.
```

# Relationships

## Related

- **recv-opt-info** -- The compiler option that reports whether receive optimization was applied
- **tail-recursive-main-loop** -- Receive expressions are typically inside the tail-recursive loop

## Builds Upon

- **erlang-process-creation** -- Processes and their message queues are the foundation
- **message-sending-cost** -- Message sending creates the messages that receive fetches

# Common Errors

- **Error**: Using a variable that is NOT a newly created reference (e.g., a function argument or pattern-matched value) in selective receive without verifying optimization
  **Correction**: Use `recv_opt_info` to verify the compiler applied the optimization; ensure the variable is a reference from `monitor/2` or `make_ref/0`

- **Error**: Having some receive clauses that do not match the reference, preventing the optimization
  **Correction**: Ensure ALL clauses in the receive expression match on the same reference

# Common Confusions

- **Confusion**: Believing that all selective receives are automatically optimized
  **Clarification**: Only selective receives where ALL clauses match a suitable reference (from `monitor/2` or `make_ref/0`) are optimized. A receive matching on an arbitrary `Tag` variable is NOT optimized

- **Confusion**: Thinking the optimization requires the reference to be in the same function
  **Clarification**: The optimization works across function boundaries -- a reference created by `make_ref/0` in one function can be passed as a parameter to another function containing the `receive`, and the optimization still applies

# Source Reference

"Processes" chapter, "Fetching Received Messages" section. Includes three code examples: non-selective receive, monitor-based optimized receive, and cross-function optimized receive.

# Verification Notes

- Definition: Synthesized from multiple paragraphs in the "Fetching Received Messages" section
- The mechanism (compiler tells emulator to skip earlier messages) is explicitly described in the source
- All code examples are from the source text
- The cross-function optimization is explicitly demonstrated in the source
- Confidence: HIGH -- detailed explanation with multiple examples in official documentation
- Cross-references: All slug references verified against planned extractions
- Uncertainties: None
