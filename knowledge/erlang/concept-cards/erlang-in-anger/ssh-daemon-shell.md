---
concept: SSH Daemon Shell
slug: ssh-daemon-shell
category: distribution
subcategory: remote-access
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Connecting to Remote Nodes"
chapter_number: 4
pdf_page: null
section: "SSH Daemon"
extraction_confidence: high
aliases:
  - SSH daemon
  - ssh:daemon
prerequisites:
  - remote-shell-connection
extends: []
related:
  - named-pipe-connection
contrasts_with:
  - job-control-mode
  - remsh
answers_questions:
  - "How do I connect to a remote node?"
  - "How do I reach an Erlang node without Erlang installed locally?"
---

# Quick Definition

The SSH daemon shell uses Erlang/OTP's bundled SSH implementation to expose a remote Erlang shell over SSH, reachable by any standard SSH client without requiring Erlang or distribution on the connecting machine.

# Core Definition

"Erlang/OTP comes shipped with an SSH implementation that can both act as a server and a client. Part of it is a demo application providing a remote shell working in Erlang" (Chapter 4, "SSH Daemon").

A daemon is started with `ssh:daemon/2`, and any SSH client can then connect to the chosen port to get an Erlang shell.

# Prerequisites

- `remote-shell-connection`: the SSH daemon is one of the four connection mechanisms.

# Key Properties

1. Built into Erlang/OTP — no extra library needed.
2. Requires starting the `ssh` application (e.g. `application:ensure_all_started(ssh)`).
3. `ssh:daemon(Port, Options)` starts the listener; key options are `system_dir` (host key files) and `user_dir` (SSH config files).
4. Any SSH client connects: `ssh -p Port user@host`.
5. Does not require Erlang installed on the connecting machine.
6. Disconnecting (closing the terminal) leaves the node running.
7. `-oLogLevel=DEBUG` on the `ssh` client gives debug output for connection troubles.

# Construction / Recognition

1. Generate host keys (e.g. `ssh-keygen -t rsa -f /tmp/ssh/ssh_host_rsa_key`).
2. Start the `ssh` application.
3. Call `ssh:daemon(8989, [{system_dir, ...}, {user_dir, ...}])`.
4. Connect from any machine with `ssh -p 8989 user@host`.

# Context & Application

Useful for interacting with an Erlang installation from a machine that has no Erlang installed and no distribution set up. Production use normally requires SSH keys/passwords configured in advance.

# Examples

From Chapter 4, "SSH Daemon":

```erlang-repl
$ mkdir /tmp/ssh
$ ssh-keygen -t rsa -f /tmp/ssh/ssh_host_rsa_key
$ ssh-keygen -t rsa1 -f /tmp/ssh/ssh_host_key
$ ssh-keygen -t dsa -f /tmp/ssh/ssh_host_dsa_key
$ erl
1> application:ensure_all_started(ssh).
{ok,[crypto,asn1,public_key,ssh]}
2> ssh:daemon(8989, [{system_dir, "/tmp/ssh"},
2>                   {user_dir, "/home/ferd/.ssh"}]).
{ok,<0.52.0>}
```

Connecting:

```erlang-repl
$ ssh -p 8989 ferd@127.0.0.1
Eshell Vx.x.x  (abort with ^G)
1>
```

# Relationships

## Builds Upon
- remote-shell-connection

## Enables

## Related
- named-pipe-connection

## Contrasts With
- job-control-mode
- remsh

# Common Errors

- Running `q()` or `init:stop()` inside the SSH session: "Do not run functions such as `q()` or `init:stop()`, which will terminate the remote host."
- Forgetting to start the `ssh` application before calling `ssh:daemon/2`.

# Common Confusions

- The SSH daemon shell is unlike JCL/`-remsh`: it does not use Erlang distribution or cookies — it's a plain SSH connection.
- Closing the SSH session is the safe way to leave; only evaluated functions like `q()` are dangerous.

# Source Reference

Chapter 4: Connecting to Remote Nodes, Section "SSH Daemon". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from the chapter.
- Confidence rationale: high — explicitly defined with full worked example.
- Uncertainties: none.
- Cross-reference status: Verified
