---
# === CORE IDENTIFICATION ===
concept: supervisor Behaviour
slug: supervisor

# === CLASSIFICATION ===
category: applications-releases
subcategory: supervision
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Making a System with OTP"
chapter_number: 23
pdf_page: null
section: "The Supervision Tree"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "supervisor"
  - "gen_supervisor"
  - "-behaviour(supervisor)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - behaviour
  - gen-server
  - link
extends: []
related:
  - supervision-tree
  - restart-strategy
  - child-specification
  - otp-application
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a supervisor?"
  - "How do I build a supervision tree?"
  - "How do links relate to process supervision?"
---

# Quick Definition

A supervisor is an OTP behaviour whose job is to start, monitor, and restart worker processes if they fail. You write a callback module whose `init/1` returns a restart strategy and a list of child specifications.

# Core Definition

"Supervisors are created using the OTP `supervisor` behavior. This behavior is parameterized with a callback module that specifies the supervisor strategy and how to start the individual worker processes in the supervision tree" (Programming Erlang, "The Supervision Tree"). The callback module's `init/1` returns a data structure of the form:

```erlang
init(...) ->
    {ok, {
      {RestartStrategy, MaxRestarts, Time},
      [Worker1, Worker2, ...]
    }}.
```

`RestartStrategy` is `one_for_one` or `one_for_all`; `MaxRestarts` and `Time` define a restart frequency; the `WorkerN` entries are child specifications. A supervisor is started with `supervisor:start_link({local, Name}, Mod, Args)`. The book also refers to the behaviour as `gen_supervisor`.

# Prerequisites

- **Behaviour** — `supervisor` is an OTP behaviour, declared with `-behaviour(supervisor)`.
- **gen_server** — supervised workers are typically gen_server processes.
- **Link** — supervision is built on process links so the supervisor detects worker failures.

# Key Properties

1. An OTP behaviour declared with `-behaviour(supervisor).`.
2. The callback module's `init/1` returns `{ok, {{RestartStrategy, MaxRestarts, Time}, [ChildSpec, ...]}}`.
3. The supervisor monitors its children and restarts them on failure according to the restart strategy.
4. If more than `MaxRestarts` happen in `Time` seconds, the supervisor terminates all children and itself.
5. Started with `supervisor:start_link({local, ?MODULE}, ?MODULE, Args)`.
6. Children may themselves be supervisors, building a tree.

# Construction / Recognition

## To Construct a Supervisor:
1. Write a callback module with `-behaviour(supervisor).`.
2. Implement `init/1` to return `{ok, {{RestartStrategy, MaxRestarts, Time}, [ChildSpec, ...]}}`.
3. Provide a `start_link` function calling `supervisor:start_link({local, ?MODULE}, ?MODULE, Args)`.
4. Each child specification names a worker's `{Mod, Func, ArgList}` start function plus restart and shutdown options.

## To Recognize:
1. A module with `-behaviour(supervisor).` and an `init/1` returning a `{ok, {{...}, [...]}}` tuple is a supervisor.

# Context & Application

- **Typical contexts**: The fault-tolerance layer of any OTP system — detecting and recovering from worker crashes.
- **Common applications**: `sellaprime_supervisor` watches the `area_server` and `prime_server`, restarting either if it crashes.
- **Historical/stylistic notes**: Using `gen_server` and `gen_supervisor` correctly, Erlang systems have reached "99.9999999 percent reliability (that's nine 9s)."

# Examples

**Example 1** ("The Supervision Tree"): `sellaprime_supervisor` declares `-behaviour(supervisor).` and starts with `supervisor:start_link({local,?MODULE}, ?MODULE, Args)`.

**Example 2** ("Starting the System"): When `area_server` hits its deliberate `function_clause` error, "the crash was detected by the supervisor, and the area server was restarted by the supervisor" — and logged automatically.

# Relationships

## Builds Upon
- **Behaviour** — `supervisor` is one of the OTP behaviours.
- **Link** — supervision uses process links to detect worker failures.

## Enables
- **Supervision tree** — supervisors are the internal nodes of a supervision tree.
- **Restart strategy** — the supervisor applies a `one_for_one` or `one_for_all` strategy.
- **Child specification** — the supervisor starts each worker from a child spec.

## Related
- **gen_server** — the workers a supervisor watches are usually gen_servers.
- **OTP application** — an application's `start/2` callback typically starts the top supervisor.

## Contrasts With
- (No direct contrast within this chapter.)

# Common Errors

- **Error**: Setting `MaxRestarts`/`Time` so a crash-loop is never bounded.
  **Correction**: Choose a restart frequency so the supervisor gives up (terminates) if a process crashes repeatedly for the same reason.

- **Error**: Forgetting to make supervised workers link back (via `start_link`).
  **Correction**: Workers must be started with `start_link` so the supervisor is linked and notified of crashes.

# Common Confusions

- **Confusion**: Thinking a supervisor does application work.
  **Clarification**: A supervisor's only job is to start, monitor, and restart its children; the work is done by the workers.

- **Confusion**: Believing a supervisor restarts forever.
  **Clarification**: If restarts exceed `MaxRestarts` within `Time` seconds, the supervisor terminates all children and itself.

# Source Reference

Chapter 23: Making a System with OTP, section "The Supervision Tree"; also "Starting the System" and "File System Organization". No page numbers (EPUB-origin source).

# Verification Notes

- Definition source: Direct quotes and code from "The Supervision Tree".
- Confidence rationale: HIGH — the supervisor behaviour and its init structure are explicitly defined and demonstrated.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards in this batch.
- Re-extraction notes: Fresh extraction; no pre-existing card. Canonical slug `supervisor` per extraction instructions.
