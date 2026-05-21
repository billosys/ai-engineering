---
concept: Remote Shell
slug: remote-shell
category: distribution
subcategory: distribution-tooling
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Distribunomicon"
chapter_number: 26
pdf_page: null
section: "Remote Shells"
extraction_confidence: high
aliases:
  - "remote shell"
  - "distributed shell"
prerequisites:
  - distributed-node
  - node-connection
extends: []
related:
  - hidden-node
contrasts_with: []
answers_questions:
  - "What is a remote shell in Erlang?"
  - "How do I open a shell on another node?"
  - "How do I administer a -noshell node?"
---

# Remote Shell

## Quick Definition

A remote shell is a job that lets you drive another node's shell as if it were local. It is reached through the Ctrl-G job-control menu's `r` (remote shell) command.

## Core Definition

Erlang's Ctrl-G job-control menu includes a `r [node [shell]]` option to "start remote shell" (Ch. 26, "Remote Shells"). After starting a remote job on another node and connecting to it with `c`, the remote shell is used the same way as a local one. This is especially useful to administer a node started with the `-noshell` option: if such a node has a name, you can connect to do DevOps tasks like reloading modules and debugging code.

## Prerequisites

- **Distributed-node** — A remote shell targets a named node
- **Node-connection** — The nodes must be reachable to start a remote job

## Key Properties

1. Reached via the Ctrl-G (^G) job-control menu's `r [node [shell]]` command
2. After `r node@host`, use `j` to list jobs and `c` to connect to the remote job
3. A connected remote shell behaves like a local shell
4. Older Erlang versions lack features like autocompletion in remote shells
5. It is the way to administer a `-noshell` named node (reload modules, debug)
6. Calling `q()` or `init:stop()` in a remote shell terminates the *remote* node
7. Ctrl-G returns you to the original node

## Construction / Recognition

### To open a remote shell

1. Press Ctrl-G in your local shell
2. Enter `r remote_node@host`
3. List jobs with `j`, then connect with `c`
4. Use the shell normally; press Ctrl-G to return to the local node

## Context & Application

Remote shells are a core DevOps tool for headless (`-noshell`) production nodes — connect, reload code, inspect state, then leave.

## Examples

**Example** (Ch. 26): Starting a remote job on `mustard` —

```
--> r mustard@ferdmbp
--> c
(mustard@ferdmbp)1> node().
mustard@ferdmbp
```

## Relationships

### Builds Upon

- **Distributed-node** — Remote shells connect to named nodes
- **Node-connection** — Reachability between nodes is required

### Related

- **Hidden-node** — A hidden admin node is a natural place to run remote shells from

## Common Errors

- **Error**: Calling `q()` or `init:stop()` in a remote shell to "exit".
  **Correction**: That terminates the remote node; use Ctrl-G to return to your local node instead.

## Common Confusions

- **Confusion**: Thinking a remote shell is just a local shell with a different prompt.
  **Clarification**: It drives the remote node's shell process; commands run there, and stopping it stops the remote node.

## Source Reference

Chapter 26, "Distribunomicon," section "Remote Shells."

## Verification Notes

- Definition: Direct adaptation from "Remote Shells"
- Key Properties: All explicit in source
- Confidence: HIGH — the section demonstrates the remote shell workflow
- Cross-references: `distributed-node`, `node-connection`, `hidden-node` planned this chapter
