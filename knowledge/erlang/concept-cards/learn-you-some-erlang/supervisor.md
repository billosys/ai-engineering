---
concept: Supervisor
slug: supervisor
category: applications-releases
subcategory: supervision
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Who Supervises the Supervisors?"
chapter_number: 17
pdf_page: null
section: "Supervisor Concepts"
extraction_confidence: high
aliases:
  - "supervisor behaviour"
  - OTP supervisor
prerequisites:
  - otp-behaviour
  - process
  - worker-process
extends:
  - otp-behaviour
related:
  - supervisor-restart-strategy
  - child-specification
  - restart-intensity
  - supervision-tree
  - simple-one-for-one-supervisor
contrasts_with:
  - worker-process
answers_questions:
  - "What is a supervisor?"
  - "How do supervisors relate to the \"let it crash\" philosophy?"
  - "How do I write a supervisor?"
  - "What must I understand before using supervisors?"
---

# Supervisor

## Quick Definition

A supervisor is an OTP behaviour whose only job is to start, monitor, and restart its child processes when they die. Supervisors can supervise workers and other supervisors.

## Core Definition

"If supervisors are supposed to be processes that do nothing but make sure their children are restarted when they die, workers are processes that are in charge of doing actual work" (Ch. 17, "Supervisor Concepts"). OTP supervisors improve on hand-rolled ones: "they let you define how many times a worker should be restarted in a given period before giving up. They let you have more than one worker per supervisor, and even let you pick from a few patterns to determine how they should depend on each other in case of a failure."

A supervisor has a single callback function, `init/1`, which returns:

```erlang
{ok, {{RestartStrategy, MaxRestart, MaxTime}, [ChildSpec]}}.
```

## Prerequisites

- **OTP behaviour** — The supervisor is one of the OTP behaviours.
- **Process** — Supervisors and their children are processes; supervision relies on links and exit signals.
- **Worker process** — Workers are what supervisors most often supervise.

## Key Properties

1. The only callback to implement is `init/1`.
2. `init/1` returns `{ok, {{RestartStrategy, MaxRestart, MaxTime}, [ChildSpec]}}`.
3. A supervisor can supervise both workers and other supervisors (forming a tree).
4. Children's `StartFunc` must be OTP-compliant and link to the caller (use `gen_*:start_link`).
5. Every process should be supervised — unsupervised processes are unaccountable and risk slow memory leaks.
6. Supervisors enable orderly, well-ordered VM shutdown: the top supervisor terminates and the request propagates down the tree.
7. Started with `supervisor:start_link/2,3`.

## Construction / Recognition

## To Write a Supervisor

1. Add `-behavior(supervisor).`
2. Export and define `start_link/N` calling `supervisor:start_link(...)`.
3. Implement `init/1` returning `{ok, {{Strategy, MaxRestart, MaxTime}, [ChildSpecs]}}`.
4. Make each child's start function a `gen_*:start_link` wrapper.
5. Choose a restart strategy and restart limits suited to the children.

## Context & Application

Supervisors are "one of the most useful parts of OTP" and embody the "let it crash" philosophy — instead of defensive coding, workers crash and supervisors restart them into a known-good state. Chapter 17 builds a `band_supervisor` managing musician `gen_server`s with varying tolerance ("lenient," "angry," "jerk").

The supervisor behaviour is fully current in modern OTP. Modern OTP also accepts a map-based child spec and supervisor flags; the book uses the older tuple form.

## Examples

**Example 1** (Ch. 17): `band_supervisor` declares `-behavior(supervisor).`, with `start_link(Type) -> supervisor:start_link({local,?MODULE}, ?MODULE, Type).`

**Example 2** (Ch. 17): `init(lenient) -> init({one_for_one, 3, 60});` then a full `init/1` returning child specs for `singer`, `bass`, `drum`, and `keytar`.

## Relationships

## Builds Upon

- **OTP behaviour** — Generic supervision machinery factored out by OTP.

## Related

- **supervisor-restart-strategy** — How the supervisor reacts when a child dies.
- **child-specification** — Describes each child the supervisor manages.
- **restart-intensity** — The `MaxRestart`/`MaxTime` limit before the supervisor gives up.
- **supervision-tree** — Supervisors of supervisors form a tree.

## Contrasts With

- **worker-process** — A worker does the actual work and may crash; a supervisor does no work, only supervises.

## Common Errors

- **Error**: Giving a child a start function that does not link to the supervisor.
  **Correction**: Use a `gen_*:start_link` wrapper; supervision depends on the link.
- **Error**: Spawning processes outside any supervision tree.
  **Correction**: Place every process under a supervisor so it is accountable and shuts down cleanly.

## Common Confusions

- **Confusion**: Thinking supervisors do application work.
  **Clarification**: Supervisors do *nothing but* manage children; all real work is done by workers.

## Source Reference

Chapter 17: "Who Supervises the Supervisors?", sections "Supervisor Concepts" and "Using Supervisors."

## Verification Notes

- Definition: Direct quotes from "Supervisor Concepts."
- Key Properties: Synthesised from the `init/1` return shape and the shutdown discussion.
- Confidence: HIGH — explicitly defined with code.
