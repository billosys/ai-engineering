---
# === CORE IDENTIFICATION ===
concept: Shutdown Time
slug: shutdown-time

# === CLASSIFICATION ===
category: applications-releases
subcategory: supervision
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Supervisors"
chapter_number: 7
pdf_page: 188
section: "The child specification"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "ShutdownTime"
  - "shutdown directive"
  - "brutal_kill"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - child-specification
extends: []
related:
  - restart-type
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a child specification?"
  - "How do I write a supervisor and define its child specifications?"
---

# Quick Definition

The shutdown time is the field of a child specification that bounds how long a supervisor waits for a child to terminate after issuing the EXIT signal, before unconditionally killing it. It can be a millisecond count, `infinity`, or `brutal_kill`.

# Core Definition

`ShutdownTime` is a positive integer denoting a time in milliseconds, or the atom `infinity`. It is the maximum time allowed to pass between the supervisor issuing the EXIT signal and the `terminate` callback function returning; if the child is overloaded and takes longer, the supervisor steps in and unconditionally terminates the child process (Cesarini & Vinoski, p. 181). `terminate` is called only if the child traps exits. As an alternative, specifying `brutal_kill` makes the supervisor unconditionally terminate the child immediately via `exit(ChildPid, kill)` (pp. 181-182). In the map form (Erlang 18.0+) it is the optional `shutdown` key.

# Prerequisites

- **Child specification** — Shutdown time is one field of a child specification.

# Key Properties

1. Three forms: a positive integer (milliseconds), the atom `infinity`, or the atom `brutal_kill`.
2. With a millisecond value, the supervisor waits that long for `terminate` to return, then unconditionally kills the child.
3. `terminate` runs only if the child traps exits; otherwise the EXIT signal terminates it directly.
4. `brutal_kill` kills the child immediately with `exit(ChildPid, kill)`, skipping cleanup.
5. `infinity` should never be used for a worker, only (commonly) for child supervisors.

# Construction / Recognition

## To Construct/Create:
1. Estimate how long the child legitimately needs to clean up in `terminate`.
2. Use a finite millisecond value for workers; consider `infinity` for child supervisors with large subtrees.
3. Use `brutal_kill` if no cleanup is needed.

## To Identify/Recognize:
1. It is the fourth element of a child-spec tuple, or the `shutdown` key in the map form.

# Context & Application

- **Typical contexts**: Every child specification.
- **Common applications**: Giving a worker a bounded window to flush state; giving a child supervisor enough time to shut down its subtree.
- **Historical/stylistic notes**: The book warns never to set `infinity` for a worker — a worker stuck talking to defunct hardware would hang in `terminate` forever and stop the system from restarting (p. 182).

# Examples

**Example 1** (p. 175): In `frequency_sup`, children are given a shutdown time of `2000` milliseconds.

**Example 2** (p. 181): The book describes specifying `brutal_kill` "if you are feeling grumpy or do not need the behavior to clean up after itself."

## Worked Example

A 2,000 ms shutdown time in a child specification (p. 175):

```erlang
child(Module) ->
    {Module, {Module, start_link, []},
     permanent, 2000, worker, [Module]}.
```

The supervisor waits up to 2,000 ms for the child's `terminate` to return before killing it.

# Relationships

## Builds Upon
- *(none)*

## Enables
- *(none)*

## Related
- **Restart type** — Both are fields of the same child specification.

## Contrasts With
- *(none)*

# Common Errors

- **Error**: Setting `infinity` as the shutdown time for a worker.
  **Correction**: Use a finite (even if large) millisecond value so a hung `terminate` cannot block the whole system from restarting.

# Common Confusions

- **Confusion**: Expecting `terminate` to always run before the shutdown timeout elapses.
  **Clarification**: `terminate` is called only if the child traps exits, and there is no guarantee it is reached — the child might be busy serving other requests.

# Source Reference

Chapter 7: Supervisors, "The child specification" (ShutdownTime), pages 181-182.

# Verification Notes

- Definition source: Direct adaptation from pp. 181-182.
- Confidence rationale: HIGH — explicitly defined with all three forms and a cautionary example.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs for this source.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
