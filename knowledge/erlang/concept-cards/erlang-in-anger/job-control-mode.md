---
concept: Job Control Mode
slug: job-control-mode
category: distribution
subcategory: remote-access
tier: foundational
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Connecting to Remote Nodes"
chapter_number: 4
pdf_page: null
section: "Job Control Mode"
extraction_confidence: high
aliases:
  - JCL
  - JCL mode
prerequisites:
  - remote-shell-connection
extends: []
related:
  - remsh
  - distribution-cookie
contrasts_with:
  - ssh-daemon-shell
  - named-pipe-connection
answers_questions:
  - "What is JCL?"
  - "How do I connect to a remote node?"
  - "What's the command to enter Job Control Mode?"
---

# Quick Definition

Job Control Mode (JCL) is the interactive menu reached by pressing `^G` in an Erlang shell, from which you can connect to, interrupt, kill, or list shell jobs — including starting a remote shell on another node.

# Core Definition

"The Job Control Mode (JCL mode) is the menu you get when you press `^G` in the Erlang shell. From that menu, there is an option allowing you to connect to a remote shell" (Chapter 4, "Job Control Mode").

When you start a remote shell through JCL, "the local shell runs all the line editing and job management locally, but the evaluation is actually done remotely. All output coming from said remote evaluation will be forwarded to the local shell."

# Prerequisites

- `remote-shell-connection`: JCL is one of the four mechanisms for connecting an interactive shell to a running VM.

# Key Properties

1. Entered by pressing `^G` in any Erlang shell.
2. The menu offers: `c` (connect to job), `i` (interrupt job), `k` (kill job), `j` (list jobs), `s` (start local shell), `r` (start remote shell), `q` (quit erlang), `?`/`h` (help).
3. `r 'node@host'` starts a remote shell job; `c` connects to it.
4. Line editing and job management always run locally; only evaluation runs remotely.
5. Quitting via `^G q` is safe because job management is local — it terminates only your local shell, not the remote node.
6. Starting the initial shell with `-hidden` avoids connecting to an entire cluster automatically.

# Construction / Recognition

1. Press `^G` to enter JCL mode.
2. Type `r 'server@ferdmbp.local'` to start a remote shell job.
3. Type `c` to connect to that job.
4. To leave, press `^G` again and type `q` (safe — local quit).

# Context & Application

Used for ad-hoc live connection to a remote node from within an existing Erlang shell, when distribution (cookie + named nodes) is already set up.

# Examples

From Chapter 4, "Job Control Mode":

```erlang-repl
(somenode@ferdmbp.local)1>
User switch command
 --> h
  c [nn]            - connect to job
  i [nn]            - interrupt job
  k [nn]            - kill job
  j                 - list all jobs
  s [shell]         - start local shell
  r [node [shell]]  - start remote shell
  q                 - quit erlang
  ? | h             - this message
 --> r 'server@ferdmbp.local'
 --> c
Eshell Vx.x.x  (abort with ^G)
(server@ferdmbp.local)1>
```

Safe exit:

```erlang-repl
(server@ferdmbp.local)1>
User switch command
 --> q
```

# Relationships

## Builds Upon
- remote-shell-connection

## Enables

## Related
- remsh
- distribution-cookie

## Contrasts With
- ssh-daemon-shell
- named-pipe-connection

# Common Errors

- Confusing `^G q` with `q()`: `^G q` quits only the local shell job safely; `q()` evaluated in a remote shell would shut down the remote node.

# Common Confusions

- JCL's `q` is local, so it's always safe — the danger is in *evaluated* functions like `q()` or `init:stop()`, not in JCL itself.
- JCL job management is local even when the connected shell is remote.

# Source Reference

Chapter 4: Connecting to Remote Nodes, Section "Job Control Mode". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from the chapter.
- Confidence rationale: high — explicitly defined with worked examples.
- Uncertainties: none.
- Cross-reference status: Verified
