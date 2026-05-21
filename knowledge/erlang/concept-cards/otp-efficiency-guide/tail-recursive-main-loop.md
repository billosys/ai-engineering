---
concept: Tail-Recursive Main Loop
slug: tail-recursive-main-loop
category: performance
subcategory: null
tier: foundational
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Processes"
chapter_number: null
pdf_page: null
section: "Creating an Erlang Process"
extraction_confidence: high
aliases:
  - "tail-recursive loop"
  - "process main loop"
  - "tail call in receive loop"
prerequisites: []
extends: []
related:
  - erlang-process-creation
  - receive-optimization
contrasts_with: []
answers_questions:
  - "Why must the main loop of an Erlang process be tail-recursive?"
  - "What happens if a process loop is not tail-recursive?"
---

# Quick Definition

The main (outer) loop of an Erlang process must be tail-recursive to prevent the stack from growing unboundedly until the process terminates.

# Core Definition

The main (outer) loop for a process _must_ be tail-recursive. Otherwise, the stack grows until the process terminates. A function call is tail-recursive when it is the last operation in the function clause, meaning no return address needs to be pushed onto the stack (Ericsson/OTP Team, "Processes" chapter, "Creating an Erlang Process" section).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. The recursive call to the loop function must be the last expression in each clause
2. No code after the recursive call means no return address is pushed onto the stack
3. A non-tail-recursive loop will grow the stack with every message processed
4. Unreachable code after a `receive` block can still break tail recursion because the compiler pushes a return address

# Construction / Recognition

## To Construct a Tail-Recursive Loop

1. Define the loop function with a `receive` block
2. In each clause of the `receive`, process the message
3. Make the recursive call to the loop function the very last expression in each clause
4. Ensure there is NO code after the `receive...end` block

## To Recognize a Non-Tail-Recursive Loop

1. Look for code after the `receive...end` block
2. Even if that code is unreachable, the compiler still generates a return address push
3. Check that every clause ends with the recursive call

# Context & Application

Tail recursion in the main loop is one of the most fundamental efficiency requirements in Erlang programming. Since Erlang processes are meant to be long-lived (servers, gen_servers, etc.), a non-tail-recursive loop would continuously consume stack space with each message received, eventually exhausting memory.

**Typical contexts:**

- Implementing custom server loops
- Writing OTP-style gen_server callbacks (OTP handles this automatically)
- Any long-lived process that receives and processes messages

# Examples

**DO NOT** (Processes chapter): Non-tail-recursive loop -- the `io:format/2` call after `receive...end` prevents tail-call optimization, even though it is unreachable:

```erlang
loop() ->
  receive
     {sys, Msg} ->
         handle_sys_msg(Msg),
         loop();
     {From, Msg} ->
          Reply = handle_msg(Msg),
          From ! Reply,
          loop()
  end,
  io:format("Message is processed~n", []).
```

**DO** (Processes chapter): Correct tail-recursive loop -- the `receive...end` block is the last expression, and each clause ends with `loop()`:

```erlang
loop() ->
   receive
      {sys, Msg} ->
         handle_sys_msg(Msg),
         loop();
      {From, Msg} ->
         Reply = handle_msg(Msg),
         From ! Reply,
         loop()
 end.
```

# Relationships

## Related

- **erlang-process-creation** -- The process's initial stack is part of the 233-word heap; tail recursion keeps it from growing
- **receive-optimization** -- Receive expressions are typically inside the tail-recursive loop

# Common Errors

- **Error**: Placing code after the `receive...end` block, even if it is logically unreachable
  **Correction**: Remove any code after `receive...end`. Even unreachable code causes the compiler to push a return address, breaking tail-call optimization

- **Error**: Performing the recursive call in a non-tail position (e.g., wrapping it in another function call)
  **Correction**: Ensure the recursive call is the very last expression evaluated in each clause

# Common Confusions

- **Confusion**: Believing that unreachable code does not affect optimization
  **Clarification**: The compiler still generates stack-frame pushes for code after `receive...end` even if it can never execute. The call to `io:format/2` in the DO NOT example will never run, but a return address is still pushed to the stack each time `loop/0` is called recursively

- **Confusion**: Thinking that tail recursion only matters for performance
  **Clarification**: In a long-running process loop, non-tail-recursive calls are not merely slower -- they cause unbounded stack growth that will eventually crash the process

# Source Reference

"Processes" chapter, "Creating an Erlang Process" section. Includes both a DO NOT and DO example demonstrating the difference between non-tail-recursive and tail-recursive main loops.

# Verification Notes

- Definition: Direct from source, paragraph between the memory discussion and the code examples
- Code examples: Reproduced exactly from source DO/DO NOT examples
- The source explicitly states "The call to `io:format/2` will never be executed, but a return address will still be pushed to the stack each time `loop/0` is called recursively"
- Confidence: HIGH -- explicit definition with clear DO/DO NOT examples in official documentation
- Cross-references: All slug references verified against planned extractions
- Uncertainties: None
