---
concept: Connecting in Init Anti-Pattern
slug: connect-in-init-anti-pattern
category: anti-patterns
subcategory: supervision
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Building Open Source Erlang Software"
chapter_number: 2
pdf_page: null
section: "Example: Initializing without guaranteeing connections"
extraction_confidence: high
aliases:
  - "Guaranteeing a connection in init/1"
prerequisites:
  - supervisor-init-guarantees
  - synchronous-supervision-startup
extends: []
related:
  - let-it-crash
contrasts_with:
  - supervisor-init-guarantees
answers_questions:
  - "Why is connecting to a remote service in init/1 a problem?"
  - "What state should not go in a process's init function?"
---

# Quick Definition

The connect-in-init anti-pattern is establishing a connection to an external service inside a process's `init/1` and making that connection a guarantee — which, given synchronous startup with no cooldown, can prevent the whole system from booting when the service is down.

# Core Definition

From Chapter 2, section "Example: Initializing without guaranteeing connections": code that "attempts to guarantee a connection as part of the process' state" is the anti-pattern. The problematic init:

```erlang
init(Args) ->
    Opts = parse_args(Args),
    {ok, Port} = connect(Opts),
    {ok, #state{sock=Port, opts=Opts}}.
```

If `connect/1` fails, `init/1` crashes; the supervisor retries with no cooldown; after too many failures the application — and possibly the node — shuts down.

# Prerequisites

- `supervisor-init-guarantees` — the anti-pattern violates the guarantees principle.
- `synchronous-supervision-startup` — synchronous, cooldown-free restart is what makes the anti-pattern destructive.

# Key Properties

1. The mistake: making a *remote* connection a hard guarantee of the init phase.
2. Consequence: a down or unreachable service causes repeated init crashes and a failed boot.
3. The fix: initialize the connection *manager*, not the connection — send yourself a `reconnect` message and start with `sock=undefined`.
4. After the fix, the guarantee weakens from "the connection is available" to "the connection manager is available."
5. Forcing a connection in init is acceptable *only* when you can truly guarantee the dependency (e.g. a co-located database that boots first).

# Construction / Recognition

Recognize it: an `init/1` that calls `connect/...` and pattern-matches `{ok, _}` on the result for a remote service. Fix it: rewrite init to defer connection:

```erlang
init(Args) ->
    Opts = parse_args(Args),
    self() ! reconnect,
    {ok, #state{sock=undefined, opts=Opts}}.
```

Then handle `reconnect` in `handle_info/2`, retrying in a loop, and have calls return `{error, not_connected}` while disconnected.

# Context & Application

This anti-pattern appears in database and service clients. The corrected form lets the *callers* decide how much failure they tolerate, rather than the client forcing a system-wide failure.

# Examples

From Chapter 2, section "Example: Initializing without guaranteeing connections": the before/after `init/1` pair is shown verbatim. The book notes the rewrite means "you now allow initializations with fewer guarantees: they went from *the connection is available* to *the connection manager is available*." Chapter 2's Hands-On exercise points at `recon_demo`'s `council_member` worker, which "starts a server and connects to it in its `init/1` function," as a case to refactor.

# Relationships

## Builds Upon
Nothing — it is a recognition/anti-pattern card.

## Enables
Nothing.

## Related
- `let-it-crash` — the anti-pattern abuses crash-restart by retrying something that cannot stabilize.

## Contrasts With
- `supervisor-init-guarantees` — the correct practice the anti-pattern violates.

# Common Errors

- Adding a cooldown to the supervisor to "fix" the failing boot, instead of weakening the init guarantee.
- Pattern-matching `{ok, Conn} = connect(...)` in init for a remote service.

# Common Confusions

- Connecting in init is not *always* wrong — it is wrong only when the dependency cannot be genuinely guaranteed. A co-located, boot-ordered database may legitimately be connected in init.
- Doing a best-effort connect in init is fine *as an optimization*, as long as the process is also able to reconnect later.

# Source Reference

Chapter 2: Building Open Source Erlang Software, Section "Example: Initializing without guaranteeing connections". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from Chapter 2, section "Example: Initializing without guaranteeing connections."
- Confidence rationale: high — the source presents explicit before/after code and names the mistake.
- Uncertainties: none.
- Cross-reference status: Verified
