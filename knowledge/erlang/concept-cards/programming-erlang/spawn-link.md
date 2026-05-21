---
# === CORE IDENTIFICATION ===
concept: spawn_link
slug: spawn-link

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: process-creation
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Errors in Concurrent Programs"
chapter_number: 13
pdf_page: null
section: "Error Handling Primitives"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "spawn_link/1"
  - "spawn_link/3"
  - "spawn_link/4"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - process
  - spawn
  - link
extends:
  - spawn
related:
  - spawn-monitor
  - distributed-erlang
contrasts_with:
  - spawn-monitor

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I spawn a process and link it atomically?"
  - "Why must spawning and linking be a single atomic operation?"
  - "How do I make a set of processes that all die together?"
---

# Quick Definition

`spawn_link` creates a new process and atomically establishes a link between the parent and the child in a single operation, avoiding the race that arises from a separate `spawn` followed by `link`.

# Core Definition

`spawn_link(Fun)` and `spawn_link(Mod, Func, Args)` behave like `spawn(Fun)` or `spawn(Mod, Func, Args)` and also create a link between the parent and child processes (Chapter 13, "Error Handling Primitives"). The combined operation exists because `spawn` and `link` were once separate primitives; an obscure bug occurred when a spawned process died before the `link` statement ran, so the process died but no error signal was generated. To fix this, `spawn_link` was added as an *atomic* operation (Chapter 13 sidebar "Why Spawning and Linking Must Be an Atomic Operation"). A distributed form, `spawn_link(Node, ...)`, spawns the linked process on a remote node.

# Prerequisites

- **Process** — `spawn_link` creates a process.
- **Spawn** — `spawn_link` is `spawn` plus an atomic link.
- **Link** — Understanding the link semantics is required to use `spawn_link` correctly.

# Key Properties

1. Creates a new process exactly like `spawn`.
2. Atomically links the new process to its parent.
3. The link is established before the child can possibly die — no race.
4. Available in `Fun` and `Mod/Func/Args` forms, and a remote `Node` form.
5. If the child crashes abnormally, the exit signal reaches the parent (which dies unless trapping exits).

# Construction / Recognition

## To Use spawn_link:
1. Call `spawn_link(fun() -> ... end)` or `spawn_link(Mod, Func, Args)`.
2. The returned `Pid` is already linked to the calling process.
3. To spawn-and-link on a remote node, use `spawn_link(Node, ...)`.

## To Recognize It:
1. Look for `spawn_link` calls where parent and child should fate-share.
2. Look for it inside functions that build "die together" process groups.

# Context & Application

- **Typical contexts**: Building process groups that all die together; OTP-style supervised processes.
- **Common applications**: Worker groups; the book's `start(Fs)` function.
- **Historical/stylistic notes**: Its existence is a lesson that "even simple-looking programs can be tricky when concurrency is involved."

# Examples

**Example 1** (Chapter 13, "Making a Set of Processes That All Die Together"): `start(Fs)` spawns a process that evaluates `[spawn_link(F) || F <- Fs]`, linking every worker. If any worker dies, they all die.

**Example 2** (Chapter 13 sidebar): The historical definition `spawn_link(Mod, Func, Args) -> Pid = spawn(Mod, Fun, Args), link(Pid), Pid.` is shown as the buggy non-atomic version that `spawn_link` replaced.

# Relationships

## Builds Upon
- **Spawn** — `spawn_link` extends `spawn` with an atomic link.

## Enables
- Process groups that fate-share; supervised worker structures.

## Related
- **Distributed Erlang** — the `spawn_link(Node, ...)` form links across nodes.

## Contrasts With
- **spawn-monitor** — `spawn_monitor` creates a unidirectional monitor and returns `{Pid, Ref}`; `spawn_link` creates a bidirectional link and returns just `Pid`.

# Common Errors

- **Error**: Using `spawn` then `link` separately.
  **Correction**: Use `spawn_link` so the link cannot be missed if the child dies immediately.
- **Error**: Calling `spawn_link` from a process that does not trap exits when you only want notification.
  **Correction**: Either trap exits in the parent or use `spawn_monitor` instead.

# Common Confusions

- **Confusion**: `spawn_link` and `spawn` followed by `link` are equivalent.
  **Clarification**: They are not — only `spawn_link` is atomic and free of the spawn/link race.
- **Confusion**: `spawn_link` returns a reference like `spawn_monitor`.
  **Clarification**: `spawn_link` returns only the `Pid`; `spawn_monitor` returns `{Pid, Ref}`.

# Source Reference

Chapter 13: Errors in Concurrent Programs, section "Error Handling Primitives" (the `spawn_link/1` and `spawn_link/3` specs), sidebar "Why Spawning and Linking Must Be an Atomic Operation," and section "Making a Set of Processes That All Die Together." Distributed form in Chapter 14, "Libraries and BIFS for Distributed Programming."

# Verification Notes

- Definition source: Direct adaptation of the `spawn_link` BIF specs and the atomicity sidebar.
- Confidence rationale: HIGH — `spawn_link` is explicitly specified and its rationale explained.
- Uncertainties: None.
- Cross-reference status: Slugs match canonical `spawn`/`link` and planned `spawn-monitor`/`distributed-erlang` cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
