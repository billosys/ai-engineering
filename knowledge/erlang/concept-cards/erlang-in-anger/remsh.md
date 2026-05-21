---
concept: Remsh
slug: remsh
category: distribution
subcategory: remote-access
tier: foundational
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Connecting to Remote Nodes"
chapter_number: 4
pdf_page: null
section: "Remsh"
extraction_confidence: high
aliases:
  - "-remsh"
  - remote shell flag
prerequisites:
  - remote-shell-connection
extends:
  - job-control-mode
related:
  - distribution-cookie
contrasts_with:
  - ssh-daemon-shell
  - named-pipe-connection
answers_questions:
  - "How do I connect to a remote node?"
---

# Quick Definition

`-remsh` is an `erl` command-line flag that starts a new Erlang VM whose shell is immediately attached to a remote node, bypassing the manual Job Control Mode steps.

# Core Definition

"There's a mechanism entirely similar to the one available through the JCL mode, although invoked in a different manner. The entire JCL mode sequence can be bypassed by starting the shell" with `-remsh` (Chapter 4, "Remsh").

"The underlying mechanisms are the same as when using JCL mode, but the initial shell is started remotely instead of locally (JCL is still local)."

# Prerequisites

- `remote-shell-connection`: `-remsh` is one of the four connection mechanisms.

# Key Properties

1. Invoked as a command-line flag when starting `erl`, not interactively.
2. Long-name form: `erl -name local@domain.name -remsh remote@domain.name`.
3. Short-name form: `erl -sname local@domain -remsh remote@domain`.
4. Uses the same underlying mechanism as JCL mode.
5. The initial shell is started *remotely* (with JCL, the initial shell starts locally).
6. Accepts all other Erlang arguments, e.g. `-hidden` and `-setcookie $COOKIE`.
7. `^G` remains the safest way to exit the remote shell.

# Construction / Recognition

Start `erl` with the `-remsh` flag pointing at the target node, supplying a matching cookie and a local node name (long or short). The new VM's shell connects to the remote node automatically.

# Context & Application

Used when you want a one-command way to drop straight into a remote node's shell — for instance, in deployment scripts or operator tooling — without going through `^G r ... c`.

# Examples

From Chapter 4, "Remsh":

```text
erl -name local@domain.name -remsh remote@domain.name
```

```text
erl -sname local@domain -remsh remote@domain
```

"All other Erlang arguments (such as `-hidden` and `-setcookie $COOKIE`) are also valid."

# Relationships

## Builds Upon
- remote-shell-connection
- job-control-mode

## Enables

## Related
- distribution-cookie

## Contrasts With
- ssh-daemon-shell
- named-pipe-connection

# Common Errors

- Forgetting `-setcookie` when the two nodes do not share a cookie file — connection will silently fail.
- Mixing long-name (`-name`) and short-name (`-sname`) conventions between the local and remote nodes — they must match.

# Common Confusions

- `-remsh` is *not* a different protocol from JCL: it uses the same distribution mechanism; only the invocation differs and the initial shell starts remotely.
- Job control is still local even with `-remsh`, so `^G` exits cleanly.

# Source Reference

Chapter 4: Connecting to Remote Nodes, Section "Remsh". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from the chapter.
- Confidence rationale: high — explicitly defined with both invocation forms.
- Uncertainties: none.
- Cross-reference status: Verified
