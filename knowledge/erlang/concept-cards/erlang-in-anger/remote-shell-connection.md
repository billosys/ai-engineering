---
concept: Remote Shell Connection
slug: remote-shell-connection
category: distribution
subcategory: remote-access
tier: foundational
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Connecting to Remote Nodes"
chapter_number: 4
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - remote node connection
prerequisites: []
extends: []
related:
  - job-control-mode
  - remsh
  - ssh-daemon-shell
  - named-pipe-connection
  - distribution-cookie
contrasts_with: []
answers_questions:
  - "How do I connect to a remote node?"
  - "Can a single Erlang VM have multiple shells connected at once?"
---

# Quick Definition

A remote shell connection is an interactive Erlang shell (a REPL-like "interactor") that runs against a live, already-running Erlang virtual machine, allowing inspection and debugging of a production node without restarting it.

# Core Definition

Unlike traditional servers, an Erlang VM does not need a shell at all — it will "happily run byte code and stick with that, no shell needed." Because of Erlang's concurrency, multiprocessing, and distribution support, in-software REPLs can run as arbitrary Erlang processes. As the source states: "unlike a single screen session with a single shell, it's possible to have as many Erlang shells connected and interacting with one virtual machine as you want at a time" (Chapter 4, intro).

The book describes four ways to connect to a remote node: Job Control Mode (JCL), `-remsh`, the SSH daemon, and named pipes (`run_erl`/`to_erl`).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. An Erlang VM can have any number of shells connected to it simultaneously.
2. A shell is just an Erlang process — not a special privileged session.
3. Most connection methods require a shared cookie and named nodes; named pipes and the SSH daemon do not require distribution.
4. All methods require *a priori* measures — you must set up access before trouble strikes; you cannot retrofit a connection mechanism onto a node that wasn't prepared.
5. The four documented methods are: JCL mode, `-remsh`, SSH daemon, named pipes.

# Construction / Recognition

To use any remote shell, you must prepare the target node ahead of time: give it a node name and cookie (for distribution-based methods), or start it under `run_erl` (named pipes), or start the SSH daemon application. Then connect using one of the four methods.

# Context & Application

Used for live debugging and inspection of production systems where "stuff is already bad and no function exists for it" — that is, when programmed management/configuration interfaces don't cover the situation you face. The interactive approach complements (rather than replaces) planned management functions and configuration reloads.

# Examples

From Chapter 4 intro: "Erlang uses something closer to an 'interactor' than a REPL. Basically, a regular Erlang virtual machine does not need a REPL... However, because of how it works with concurrency and multiprocessing, and good support for distribution, it is possible to have in-software REPLs that run as arbitrary Erlang processes."

# Relationships

## Builds Upon

## Enables
- job-control-mode
- remsh
- ssh-daemon-shell
- named-pipe-connection

## Related
- distribution-cookie

## Contrasts With

# Common Errors

- Failing to prepare a node for remote access before it gets into trouble — none of the four methods can be added retroactively.
- Running `q()` or `init:stop()` while connected remotely, which terminates the *remote host*, not just your session.

# Common Confusions

- An Erlang shell is not like a single `screen`/`tmux` session: many independent shells can talk to one VM at once.
- A VM with no shell is still fully functional; the shell is an optional convenience, not a runtime requirement.

# Source Reference

Chapter 4: Connecting to Remote Nodes, intro section. (No PDF pages — this source has none.)

# Verification Notes

- Definition source: synthesized from chapter introduction.
- Confidence rationale: high — the chapter explicitly frames the concept and enumerates the four methods.
- Uncertainties: none.
- Cross-reference status: Verified
