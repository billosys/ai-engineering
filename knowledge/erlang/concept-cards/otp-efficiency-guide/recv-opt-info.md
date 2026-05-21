---
concept: recv_opt_info Compiler Option
slug: recv-opt-info
category: performance
subcategory: null
tier: intermediate
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Processes"
chapter_number: null
pdf_page: null
section: "Option recv_opt_info"
extraction_confidence: high
aliases:
  - "recv_opt_info"
  - "receive optimization info"
  - "receive optimization diagnostics"
prerequisites:
  - receive-optimization
extends:
  - receive-optimization
related:
  - tail-recursive-main-loop
contrasts_with: []
answers_questions:
  - "What is the `recv_opt_info` compiler option?"
  - "How do I check whether the compiler optimized a receive expression?"
---

# Quick Definition

The `recv_opt_info` compiler option causes the Erlang compiler to emit informational warnings about whether `receive` expressions have been optimized to avoid scanning the full message queue.

# Core Definition

The `recv_opt_info` option can be given to the compiler or `erlc` to print information about receive optimizations. It is a diagnostic tool, not a permanent build option, because all the messages it generates cannot be eliminated (they are always emitted when the option is active). The option reports whether each `receive` expression is optimized, not optimized, or always fast (non-selective) (Ericsson/OTP Team, "Processes" chapter, "Option recv_opt_info" section).

# Prerequisites

- **receive-optimization** -- Understanding how the compiler optimizes selective receive is required to interpret the diagnostic output

# Key Properties

1. Activated by passing `+recv_opt_info` to `erlc` or the compiler
2. Can also be set via the `ERL_COMPILER_OPTIONS` environment variable
3. Generates informational warnings (not errors) for every `receive` expression
4. NOT intended as a permanent Makefile option because warnings cannot be suppressed
5. Reports three categories: INFO (always fast), NOT OPTIMIZED, and OPTIMIZED
6. For OPTIMIZED cases, identifies which reference is used and where it was created

# Construction / Recognition

## To Use recv_opt_info

1. Pass the option to `erlc`:
   ```
   erlc +recv_opt_info Mod.erl
   ```
2. Or set it via environment variable (preferred for temporary use):
   ```
   export ERL_COMPILER_OPTIONS=recv_opt_info
   ```
3. Review the generated warnings to check optimization status of each `receive`

## To Interpret the Output

- `INFO: not a selective receive, this is always fast` -- Non-selective receive, no optimization needed
- `NOT OPTIMIZED: all clauses do not match a suitable reference` -- Selective receive that cannot be optimized
- `OPTIMIZED: reference used to mark a message queue position` -- Queue position marker placed at reference creation
- `OPTIMIZED: all clauses match reference created by monitor/2 at ...` -- All clauses match the reference
- `INFO: passing reference created by make_ref/0 at ...` -- Reference being passed to another function
- `OPTIMIZED: all clauses match reference in function parameter 1` -- Cross-function optimization applied

# Context & Application

The `recv_opt_info` option is a debugging/tuning tool for verifying that critical receive expressions are optimized. It is particularly useful when refactoring code to ensure that optimization is not accidentally broken.

**Typical contexts:**

- Verifying that a request/response pattern is properly optimized
- Debugging performance issues caused by message queue scanning
- Code review of receive-heavy modules
- One-time analysis before deployment (not for CI/CD)

**Practical tip:** The environment variable approach (`export ERL_COMPILER_OPTIONS=recv_opt_info`) is recommended over adding it to Makefiles, since the warnings cannot be eliminated and would clutter CI output.

# Examples

**Example** (Processes chapter, "Option recv_opt_info" section): Sample compiler output for various receive patterns:

```erlang
%% DO
simple_receive() ->
%% efficiency_guide.erl:194: Warning: INFO: not a selective receive, this is always fast
receive
    Message -> handle_msg(Message)
end.

%% DO NOT, unless Tag is known to be a suitable reference
selective_receive(Tag, Message) ->
%% efficiency_guide.erl:200: Warning: NOT OPTIMIZED: all clauses do not match a suitable reference
receive
    {Tag, Message} -> handle_msg(Message)
end.

%% DO
optimized_receive(Process, Request) ->
%% efficiency_guide.erl:206: Warning: OPTIMIZED: reference used to mark a message queue position
    MRef = monitor(process, Process),
    Process ! {self(), MRef, Request},
    %% efficiency_guide.erl:208: Warning: OPTIMIZED: matches reference created by monitor/2 at efficiency_guide.erl:206
    receive
        {MRef, Reply} ->
        erlang:demonitor(MRef, [flush]),
        handle_reply(Reply);
    {'DOWN', MRef, _, _, Reason} ->
    handle_error(Reason)
    end.

%% DO
cross_function_receive() ->
    %% OPTIMIZED: reference used to mark a message queue position
    Ref = make_ref(),
    %% INFO: passing reference created by make_ref/0
    cross_function_receive(Ref).

cross_function_receive(Ref) ->
    %% OPTIMIZED: all clauses match reference in function parameter 1
    receive
        {Ref, Message} -> handle_msg(Message)
    end.
```

# Relationships

## Extends

- **receive-optimization** -- recv_opt_info is the diagnostic tool for verifying receive optimization

## Related

- **tail-recursive-main-loop** -- The receive expressions diagnosed by recv_opt_info are typically inside main loops

# Common Errors

- **Error**: Adding `+recv_opt_info` permanently to Makefiles or rebar config
  **Correction**: Use the environment variable (`export ERL_COMPILER_OPTIONS=recv_opt_info`) for temporary analysis, since the generated warnings cannot be eliminated

- **Error**: Ignoring "NOT OPTIMIZED" warnings for receives in hot code paths
  **Correction**: Refactor the receive to use `monitor/2` or `make_ref/0` references so the optimization can apply

# Common Confusions

- **Confusion**: Thinking `recv_opt_info` changes the generated code
  **Clarification**: It is purely diagnostic -- it only prints information about what the compiler already does. The optimization is always applied when possible, regardless of whether `recv_opt_info` is set

- **Confusion**: Believing that "NOT OPTIMIZED" means the code is broken
  **Clarification**: A non-optimized selective receive works correctly; it just may be slower for processes with long message queues. Whether this matters depends on the specific use case

# Source Reference

"Processes" chapter, "Option recv_opt_info" subsection under "Fetching Received Messages". Includes erlc invocation syntax, environment variable usage, and annotated code examples showing all warning categories.

# Verification Notes

- Definition: Directly from source text in the "Option recv_opt_info" subsection
- Warning message categories: All six warning formats reproduced from source
- The advice against permanent Makefile inclusion is explicit in the source: "recv_opt_info is not meant to be a permanent option added to your Makefiles, because all messages that it generates cannot be eliminated"
- Confidence: HIGH -- explicit documentation with comprehensive examples in official guide
- Cross-references: All slug references verified against planned extractions
- Uncertainties: None
