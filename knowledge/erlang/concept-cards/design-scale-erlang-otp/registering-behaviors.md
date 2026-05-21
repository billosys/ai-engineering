---
# === CORE IDENTIFICATION ===
concept: Registering Behaviors (Name Scope)
slug: registering-behaviors

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: gen-server
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Generic Servers"
chapter_number: 3
pdf_page: 96
section: "Going Global"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - NameScope
  - local registration
  - global registration
  - "{via, Module, Name}"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - starting-a-gen-server
extends: []
related:
  - distributed-erlang
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How can a gen_server be registered locally or globally?"
  - "What is a NameScope?"
  - "Can a gen_server run without being registered?"
---

# Quick Definition

A behavior process can be registered locally, globally, or via a custom registry — collectively called the NameScope — or left unregistered and addressed by pid.

# Core Definition

"Behavior processes can be registered locally or globally" (Cesarini & Vinoski, p. 97). Local registration uses `{local, ServerName}`, "equivalent to registering the process using the `register(ServerName, Pid)` BIF." Global registration uses `{global, Name}` and "piggyback[s] on the global name server, which makes [processes] transparently accessible in a cluster" — equivalent to `global:register_name(Name, Pid)` (p. 98). A custom registry uses `{via, Module, Name}`, where `Module` exports `register_name/2`, `unregister_name/1`, `whereis_name/1`, and `send/2`. "We aggregate `{via, Module, Name}`, `{local, Name}`, and `{global, Name}` using NameScope" (p. 98). Registration is optional: omitting the name field allows multiple instances and addressing by pid.

# Prerequisites

- **Starting a gen_server** — The NameScope is the first argument of `gen_server:start_link`/`start`.

# Key Properties

1. `{local, Name}` registers the process locally (like the `register/2` BIF).
2. `{global, Name}` registers via the global name server, giving cluster-wide location transparency.
3. `{via, Module, Name}` uses a custom registry module exporting four functions.
4. The three forms are collectively called the NameScope.
5. For globally registered processes, `Name` may be any Erlang term, not just an atom.
6. Registration is optional — omitting the name field allows multiple instances of the same behavior.
7. Unregistered processes are addressed by pid.

# Construction / Recognition

## To Construct:
1. Pass `{local, Name}`, `{global, Name}`, or `{via, Module, Name}` as the NameScope to `start_link`.
2. Use the same NameScope in `call`/`cast`.
3. To run unregistered, use the `start_link/3` arity that omits the name field.

## To Recognize:
1. A `{local|global|via, ...}` tuple as the first argument of a behavior `start` function.

# Context & Application

- **Typical contexts**: Most servers register locally; global and via are used for clustering and custom topologies.
- **Common applications**: Cluster-wide singletons via `{global, Name}`; multiple parallel instances by leaving processes unregistered.
- **Historical/stylistic notes**: `multi_call/3` and `abcast/3` broadcast a request to servers across a cluster of nodes.

# Examples

**Example 1** (p. 98): Global registration and calls:

```erlang
gen_server:start_link({global,Name},Mod,Args,Opts) -> {ok, Pid} | ignore | {error, Reason}
gen_server:call({global, Name}, Message) -> Reply
gen_server:cast({global, Name}, Message) -> ok
```

**Example 2** (p. 98): Starting unregistered, addressed by pid:

```erlang
gen_server:start_link(Mod, Args, Opts) -> {ok, Pid} | ignore | {error, Reason}
```

# Relationships

## Builds Upon
- **Starting a gen_server** — NameScope is supplied at startup.

## Enables
- *(none specific in scope)*

## Related
- **Distributed Erlang** — Global registration provides location transparency across nodes.

## Contrasts With
- *(none)*

# Common Errors

- **Error**: Registering a behavior when multiple instances are needed.
  **Correction**: Omit the name field to run unregistered, allowing parallel instances addressed by pid.

# Common Confusions

- **Confusion**: Thinking a behavior must be registered.
  **Clarification**: Registration is optional; an unregistered behavior is simply addressed by its pid.

# Source Reference

Chapter 3: Generic Servers, Section "Going Global," pages 97-99.

# Verification Notes

- Definition source: Direct quotes from pp. 97-98.
- Confidence rationale: HIGH — explicit treatment of all three scopes plus unregistered processes.
- Uncertainties: None.
- Cross-reference status: `distributed-erlang` is a planned card (Chapter 1 covers Distributed Erlang; this extraction's scope is Ch. 1-3 — see note).
- Re-extraction notes: Fresh extraction — no pre-existing card for this source. Note: Chapter 1's "Distributed Erlang" section was not separately carded as it falls outside the likely-concepts focus of this assignment; the reference is to a planned card.
</content>
</invoke>
