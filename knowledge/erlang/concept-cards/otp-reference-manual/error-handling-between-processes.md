---
# === CORE IDENTIFICATION ===
concept: Error Handling Between Processes
slug: error-handling-between-processes

# === CLASSIFICATION ===
category: error-handling
subcategory: process-error-handling
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Errors and Error Handling"
chapter_number: null
pdf_page: null
section: "Handling of Run-time Errors in Erlang"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "inter-process error handling"
  - "error propagation between processes"
  - "process monitoring for errors"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-process
  - exception-classes
  - exit-reasons
extends: []
related:
  - erlang-signals
  - process-termination
  - try-expression
contrasts_with:
  - error-handling-within-processes

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do Erlang processes detect failures in other processes?"
  - "What is the difference between error handling within and between processes?"
  - "How do links and monitors enable error handling across processes?"
---

# Quick Definition

Error handling between processes uses links and monitors to detect when a process terminates. Linked processes receive exit signals; monitoring processes receive `'DOWN'` messages. This is the foundation of Erlang's supervision-based fault tolerance.

# Core Definition

Processes can monitor other processes and detect process terminations. Error handling between processes is achieved through links (bidirectional, causing linked processes to receive exit signals) and monitors (unidirectional, causing the monitoring process to receive `'DOWN'` messages). This mechanism enables supervisor-based fault tolerance where a supervisor process monitors worker processes and can restart them when they fail. This contrasts with error handling within a single process, which uses `try`/`catch` (Erlang Reference Manual, "Errors and Error Handling" chapter, "Handling of Run-time Errors in Erlang" section).

# Prerequisites

- **erlang-process** — Understanding processes as the fundamental unit of concurrency.
- **exception-classes** — Understanding what exceptions cause process termination.
- **exit-reasons** — The exit reason is communicated via exit signals.

# Key Properties

1. Links are bidirectional: if either process dies, the other receives an exit signal.
2. Monitors are unidirectional: only the monitoring process is notified.
3. Exit signals carry the exit reason from the terminated process.
4. A process can trap exit signals (`process_flag(trap_exit, true)`) to handle them as messages.
5. Monitors produce `{'DOWN', Ref, process, Pid, Reason}` messages.
6. This is the foundation of OTP supervisor behavior.

# Construction / Recognition

## Links:
```erlang
link(Pid)                      %% create a link
spawn_link(Module, Fun, Args)  %% spawn and link atomically
```

## Monitors:
```erlang
Ref = monitor(process, Pid)    %% monitor a process
spawn_monitor(Module, Fun, Args) %% spawn and monitor
```

## Handling:
```erlang
%% Trapping exits (links):
process_flag(trap_exit, true),
receive
    {'EXIT', Pid, Reason} -> handle_exit(Pid, Reason)
end.

%% Receiving monitor messages:
receive
    {'DOWN', Ref, process, Pid, Reason} -> handle_down(Pid, Reason)
end.
```

# Context & Application

Error handling between processes is central to Erlang's "let it crash" philosophy. Rather than defending against every possible error within a process, the idiomatic approach is to let processes crash and have supervisors detect and respond to failures. This separation of error detection (via links/monitors) from error handling (in supervisor processes) produces more robust systems than defensive programming within individual processes.

# Examples

**Example 1**: Supervisor-style monitoring:

```erlang
start_worker() ->
    {Pid, Ref} = spawn_monitor(fun worker_loop/0),
    monitor_loop(Pid, Ref).

monitor_loop(Pid, Ref) ->
    receive
        {'DOWN', Ref, process, Pid, normal} ->
            ok;
        {'DOWN', Ref, process, Pid, Reason} ->
            io:format("Worker crashed: ~p~n", [Reason]),
            start_worker()  %% restart
    end.
```

**Example 2**: Link-based error propagation:

```erlang
start() ->
    process_flag(trap_exit, true),
    Pid = spawn_link(fun worker/0),
    receive
        {'EXIT', Pid, Reason} ->
            {worker_died, Reason}
    end.
```

# Relationships

## Builds Upon
- **erlang-process** — Error handling between processes requires understanding processes.
- **exception-classes** — Exit reasons in signals come from exception classes.
- **exit-reasons** — Exit signals carry exit reasons.

## Enables
- Supervision trees and fault-tolerant system design.

## Related
- **erlang-signals** — Exit signals are the mechanism for inter-process error notification.
- **process-termination** — A terminated process triggers error handling in linked/monitoring processes.
- **try-expression** — Error handling within a single process.

## Contrasts With
- **error-handling-within-processes** — Within-process handling uses `try`/`catch`; between-process handling uses links/monitors.

# Common Errors

- **Error**: Using links for monitoring when only one-way notification is needed, causing the monitoring process to crash when the monitored process exits.
  **Correction**: Use `monitor/2` for one-way observation; use `link/1` only when both processes should die together or when trapping exits.

# Common Confusions

- **Confusion**: Thinking `try`/`catch` in one process can catch errors from another process.
  **Clarification**: `try`/`catch` only catches exceptions within the same process. To detect errors in other processes, use links or monitors.

# Source Reference

Erlang Reference Manual, "Errors and Error Handling" chapter, "Handling of Run-time Errors in Erlang" section.

# Verification Notes

- Definition source: Direct from source text, supplemented with standard Erlang knowledge
- Confidence rationale: High — source clearly distinguishes within-process and between-process error handling
- Uncertainties: None
- Cross-reference status: Links to process and signal concepts verified
