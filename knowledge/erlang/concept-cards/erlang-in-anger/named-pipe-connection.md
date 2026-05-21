---
concept: Named Pipe Connection
slug: named-pipe-connection
category: distribution
subcategory: remote-access
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Connecting to Remote Nodes"
chapter_number: 4
pdf_page: null
section: "Named Pipes"
extraction_confidence: high
aliases:
  - run_erl
  - to_erl
  - named pipes
prerequisites:
  - remote-shell-connection
extends: []
related:
  - ssh-daemon-shell
contrasts_with:
  - job-control-mode
  - remsh
answers_questions:
  - "How do I connect to a remote node?"
  - "Can I connect to a node that has no name?"
---

# Quick Definition

A named pipe connection wraps a running Erlang node in a named pipe using `run_erl`, so that the `to_erl` program can attach a shell to it locally without any Erlang distribution.

# Core Definition

"A little known way to connect with an Erlang node that requires no explicit distribution is through named pipes. This can be done by starting Erlang with `run_erl`, which wraps Erlang in a named pipe" (Chapter 4, "Named Pipes").

`run_erl` takes the pipe file name and a log directory; `to_erl` attaches to the pipe.

# Prerequisites

- `remote-shell-connection`: named pipes are one of the four connection mechanisms.

# Key Properties

1. Requires no explicit distribution — and no node name (you can connect to an unnamed node this way).
2. `run_erl /tmp/erl_pipe /tmp/log_dir "erl"` — first arg is the named pipe file, second is the log directory, third is the command to run (with optional args, e.g. `"erl +K true"`).
3. `to_erl /tmp/erl_pipe` attaches a shell to the pipe.
4. Closing stdio (`^D`) disconnects while leaving the node running.
5. Logs are saved to the specified directory; `run_erl` calls `fsync` for each piece of output, which can hurt performance under heavy stdout IO.
6. It is a local-only mechanism — `to_erl` must run on the same machine as the pipe.

# Construction / Recognition

1. Start the node: `run_erl /tmp/erl_pipe /tmp/log_dir "erl"`.
2. Attach a shell: `to_erl /tmp/erl_pipe`.
3. Detach with `^D`.

# Context & Application

Useful when you want a recoverable, log-capturing shell for a node started as a service, without setting up distribution or node names. The `fsync`-per-output behavior means it is a poor choice for nodes that emit a lot of standard output.

# Examples

From Chapter 4, "Named Pipes":

```erlang-repl
$ run_erl /tmp/erl_pipe /tmp/log_dir "erl"
```

```erlang-repl
$ to_erl /tmp/erl_pipe
Attaching to /tmp/erl_pipe (^D to exit)

1>
```

# Relationships

## Builds Upon
- remote-shell-connection

## Enables

## Related
- ssh-daemon-shell

## Contrasts With
- job-control-mode
- remsh

# Common Errors

- Using named pipes for a node that produces heavy stdout output — the `fsync` per output line causes a serious performance hit.
- Running `q()` or `init:stop()` while attached — this terminates the node, not just the `to_erl` session.

# Common Confusions

- `to_erl` is local-only: it is not a network mechanism like `-remsh` or the SSH daemon.
- Detaching with `^D` is safe and leaves the node running; only evaluated shutdown functions are dangerous.

# Source Reference

Chapter 4: Connecting to Remote Nodes, Section "Named Pipes". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from the chapter.
- Confidence rationale: high — explicitly defined with worked examples.
- Uncertainties: none.
- Cross-reference status: Verified
