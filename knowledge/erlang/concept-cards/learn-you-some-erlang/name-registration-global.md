---
concept: Global Name Registration
slug: name-registration-global
category: distribution
subcategory: distribution-infrastructure
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Distribunomicon"
chapter_number: 26
pdf_page: null
section: "The global Module"
extraction_confidence: high
aliases:
  - "global module"
  - "global registry"
  - "global name registration"
prerequisites:
  - distributed-node
  - node-connection
extends: []
related:
  - distributed-message-passing
contrasts_with: []
answers_questions:
  - "What is the global module?"
  - "How do I register a process name across all nodes?"
  - "How are global name conflicts resolved?"
---

# Global Name Registration

## Quick Definition

The `global` module is an alternative, cluster-wide process registry. It spreads registered names to all connected nodes, replicates the data, handles node failures, and resolves naming conflicts.

## Core Definition

`global` "is an alternative process registry. It automatically spreads its data to all connected nodes, replicates data there, handles node failures, and supports different conflict-resolution strategies when nodes get back online" (Ch. 26, "The global Module"). Unlike the local registry, names registered with `global` can be *any* term, and the registry works across the whole cluster. It integrates with OTP behaviours: changing `{local, Name}` to `{global, Name}` in `start_link` and in calls/casts distributes a server.

## Prerequisites

- **Distributed-node** — Global names span nodes
- **Node-connection** — The registry spreads across connected nodes

## Key Properties

1. `global:register_name(Name, Pid)` registers a cluster-wide name; `global:unregister_name(Name)` removes it
2. `global:re_register_name(Name, Pid)` transfers a name without it ever pointing to nothing
3. `global:whereis_name(Name)` finds a pid; `global:send(Name, Message)` sends to it
4. Registered names can be any Erlang term, not just atoms
5. On a naming conflict (two nodes connect with different processes sharing a name), `global` kills one by default
6. A third argument to register/re-register supplies a `Resolve(Name, Pid1, Pid2)` conflict function
7. Built-in resolvers: `global:random_exit_name/3` (default, kills randomly), `global:random_notify_name/3`, `global:notify_all_name/3`
8. `global` is somewhat slow to detect conflicts and node-downs and is best for a small, stable set of registrations

## Construction / Recognition

### To register globally

1. `global:register_name(Name, Pid)` — `Name` may be any term
2. Look up with `global:whereis_name(Name)`; send with `global:send(Name, Msg)`
3. For OTP servers, use `{global, Name}` instead of `{local, Name}` in `start_link` and calls/casts

## Context & Application

`global` lets you forget node names and topology while still locating processes. From R15B01, the `{via, RegistryModule, Name}` form allows other compatible registries too.

## Examples

**Example** (Ch. 26): A custom conflict resolver that keeps the process with the longer mailbox —

```erlang
Resolve = fun(_Name, Pid1, Pid2) ->
    case process_info(Pid1, message_queue_len)
       > process_info(Pid2, message_queue_len) of
        true -> Pid1;
        false -> Pid2
    end
end,
global:register_name({zombie, 12}, self(), Resolve).
```

## Relationships

### Builds Upon

- **Distributed-node** — Global names cross node boundaries
- **Node-connection** — Registry data spreads across connected nodes

### Related

- **Distributed-message-passing** — `global:send` delivers to globally registered processes

## Common Errors

- **Error**: Relying on `global` for a large, rapidly-changing set of names.
  **Correction**: `global` is best for a small, stable set; it is slow to detect conflicts and node failures.
- **Error**: Writing a `Resolve` function that returns a non-pid or crashes.
  **Correction**: If `Resolve` crashes or returns something other than a pid, the name is unregistered.

## Common Confusions

- **Confusion**: Thinking `global` names must be atoms like the local registry.
  **Clarification**: Global names can be any Erlang term.
- **Confusion**: Believing conflicts are always resolved silently.
  **Clarification**: The default resolver kills one process randomly; supply a `Resolve` function to control it.

## Source Reference

Chapter 26, "Distribunomicon," section "The global Module."

## Verification Notes

- Definition: Direct adaptation from "The global Module"
- Key Properties: All explicit in source
- Confidence: HIGH — the section demonstrates the API and conflict resolution
- Cross-references: `distributed-node`, `node-connection`, `distributed-message-passing` planned this chapter
