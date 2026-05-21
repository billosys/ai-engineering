---
concept: Scheduler and Run Queue
slug: scheduler-and-run-queue
category: processes-concurrency
subcategory: concurrency-model
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "The Hitchhiker's Guide to Concurrency"
chapter_number: 10
pdf_page: null
section: "Concurrency Implementation"
extraction_confidence: high
aliases:
  - "scheduler"
  - "run queue"
  - "SMP scheduler"
prerequisites:
  - process
extends: []
related:
  - concurrency-vs-parallelism
contrasts_with: []
answers_questions:
  - "How does the Erlang VM schedule processes?"
  - "What is a run queue?"
---

# Scheduler and Run Queue

## Quick Definition

A scheduler is a VM thread (one per core) that runs Erlang processes; each scheduler has its own run queue — a list of processes awaiting a time slice. The VM balances load across schedulers automatically.

## Core Definition

To handle the potentially huge number of processes a program creates, "the VM starts one thread per core that acts as a *scheduler*. Each of these schedulers has a *run queue*, or a list of Erlang processes on which to spend a slice of time. When one of the schedulers has too many tasks in its run queue, some tasks are migrated to another queue." Thus "each Erlang VM takes care of doing all the load balancing, and the programmer doesn't need to worry about it." The VM also performs other optimizations, such as throttling the rate at which messages can be sent to overloaded processes. The chapter notes that since R13B there is one run queue per scheduler (earlier there was a single shared queue), which allows better parallelism; the VM startup line `[smp:2:2]` shows two cores with two schedulers (Hébert, ch. 10, "Concurrency Implementation," "Symmetric Multiprocessing and You" sidebar).

## Prerequisites

- **Process** — Schedulers exist to run processes

## Key Properties

1. The VM starts one scheduler thread per core
2. Each scheduler has its own run queue of processes awaiting a time slice
3. Overloaded run queues migrate tasks to other queues — automatic load balancing
4. Since R13B there is one run queue per scheduler (previously a single shared queue)
5. The VM throttles message sends to overloaded processes
6. The startup tag `[smp:N:M]` reports cores and schedulers; absence means SMP is disabled
7. The programmer never manages scheduling — it is fully VM-controlled

## Construction / Recognition

## To Reason About Scheduling

1. Expect one scheduler per core, each with its own run queue
2. Trust the VM to migrate processes and balance load — do not build process pools
3. Check the VM startup line for `[smp:N:M]` to see cores and schedulers
4. Disable SMP with `erl -smp disable` only for purely sequential, scheduling-sensitive workloads

## Examples

> **SMP startup tag** (ch. 10): `[smp:2:2]` "means that two cores are available, with two schedulers (each having a run queue)."
>
> **Automatic balancing** (ch. 10): "when one of the schedulers has too many tasks in its run queue, some tasks are migrated to another queue."

## Relationships

## Related

- **Concurrency vs. parallelism** — Schedulers are how the VM turns concurrency into parallelism on multicore hardware

## Common Errors

- **Error**: Building a fixed process pool to control concurrency
  **Correction**: Let the VM schedule freely; use as many processes as the design needs
- **Error**: Leaving SMP enabled for a purely sequential, scheduling-sensitive benchmark
  **Correction**: For such cases `erl -smp disable` can avoid load-distribution overhead

## Common Confusions

- **Confusion**: Thinking the OS schedules Erlang processes
  **Clarification**: The Erlang VM, not the OS, schedules processes via its own scheduler threads

## Source Reference

Chapter 10, "The Hitchhiker's Guide to Concurrency," section "Concurrency Concepts," subsection "Concurrency Implementation," and the "Symmetric Multiprocessing and You" sidebar.

## Verification Notes

- Scheduler/run-queue definition and R13B note: directly from ch. 10
- Confidence: HIGH — explicitly described
