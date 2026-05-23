---
# === CORE IDENTIFICATION ===
concept: Alternative Node Discovery
slug: alternative-node-discovery

# === CLASSIFICATION ===
category: distribution
subcategory: registries
tier: advanced

# === PROVENANCE ===
source: "ERTS User's Guide"
source_slug: otp-erts
authors: "Ericsson AB"
chapter: "How to Implement an Alternative Node Discovery for Erlang Distribution"
chapter_number: null
pdf_page: null
section: "Introduction"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "custom EPMD module"
  - "custom node discovery"
  - "alternative discovery"
  - "EPMD replacement"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - epmd
  - distribution-protocol
extends: []
related:
  - epmd-protocol
  - alternative-distribution-carrier
contrasts_with:
  - epmd

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I implement alternative node discovery?"
  - "How do I replace EPMD with a custom discovery mechanism?"
  - "What callbacks must a custom EPMD module implement?"
---

# Quick Definition

Alternative node discovery allows replacing the standard EPMD-based mechanism for locating Erlang nodes. A custom EPMD module implements the same API as `erl_epmd` and is enabled via the `-epmd_module` command-line flag. This feature was added in Erlang/OTP 21.

# Core Definition

The ERTS documentation states: "To implement your own node discovery module you have to write your own EPMD module." The custom module is responsible for providing the location of other nodes. The standard distribution modules (`inet_tcp_dist`/`inet_tls_dist`) call the EPMD module to get the IP address and port of the target node. The default `erl_epmd` module resolves hostnames via DNS and uses the EPMD Unix process on port 4369, but a custom module can connect to any service for node discovery.

A discovery module is enabled by setting `-epmd_module <Module>` when starting Erlang.

The module must implement these mandatory callbacks:
- **`start_link/0`** -- Start any processes needed by the discovery module
- **`names/1`** -- Return node names held by the registrar for the given host
- **`register_node/3`** -- Register the given node name with the registrar
- **`port_please/2`** -- Return the distribution port used by the given node

Optional callbacks:
- **`address_please/3`** -- Return the address of the given node (if not implemented, `erl_epmd:address_please/3` is used). This callback may also return the port, in which case `port_please/3` may be omitted.
- **`listen_port_please/2`** -- Return the port the local node should listen to (if not implemented, `erl_epmd:listen_port_please/2` is used).

# Prerequisites

- **epmd** -- Understanding the standard EPMD that is being replaced
- **distribution-protocol** -- The discovery module serves the node discovery phase of distribution

# Key Properties

1. Enabled via `-epmd_module <Module>` command-line flag
2. Added in Erlang/OTP 21
3. Must implement the same API as `erl_epmd`
4. Four mandatory callbacks: `start_link/0`, `names/1`, `register_node/3`, `port_please/2`
5. Two optional callbacks: `address_please/3`, `listen_port_please/2`
6. `address_please/3` can return both address and port, making `port_please/2` optional
7. Can connect to any backend service -- DNS, service mesh, cloud API, etcd, Consul, etc.
8. Works with the standard distribution modules (`inet_tcp_dist`, `inet_tls_dist`) -- no need to replace the carrier
9. Combine with `-no_epmd` to prevent the standard EPMD from starting

# Construction / Recognition

## To Construct/Create:
1. Create a module implementing the `erl_epmd` callback API
2. Implement the four mandatory callbacks and any optional ones
3. Enable with `erl -epmd_module my_discovery_module`
4. Optionally add `-no_epmd` to suppress the standard EPMD daemon

## To Identify/Recognize:
1. A module referenced via `-epmd_module` in `erl` command-line arguments
2. Exports `start_link/0`, `names/1`, `register_node/3`, `port_please/2`

# Context & Application

Alternative node discovery is valuable in environments where the standard EPMD model is insufficient: cloud deployments where nodes are discovered via service registries (etcd, Consul, Kubernetes DNS), embedded systems without a daemon infrastructure, or systems requiring centralized discovery. Unlike alternative distribution carriers, which replace the transport, alternative node discovery only replaces how nodes find each other -- the actual distribution protocol remains unchanged.

# Examples

**Example 1** (Discovery module): A minimal custom EPMD module:
```erlang
-module(my_epmd).
-export([start_link/0, names/1, register_node/3, port_please/2,
         address_please/3]).

start_link() ->
    ignore.  %% No background process needed

names(Host) ->
    %% Query a custom service registry
    my_registry:list_nodes(Host).

register_node(Name, Port, _Family) ->
    %% Register with a custom service registry
    my_registry:register(Name, Port),
    {ok, rand:uniform(3)}.  %% Return creation

port_please(Name, Host) ->
    %% Look up port from custom service registry
    case my_registry:lookup(Name, Host) of
        {ok, Port} -> {port, Port, 5};
        error -> noport
    end.

address_please(Name, Host, AddressFamily) ->
    %% Return both address and port
    erl_epmd:address_please(Name, Host, AddressFamily).
```

**Example 2** (Discovery module): Enabling the custom module:
```bash
$ erl -epmd_module my_epmd -no_epmd -sname mynode
```

# Relationships

## Builds Upon
None

## Related
- **epmd** -- The standard daemon that alternative discovery replaces
- **epmd-protocol** -- The protocol that need not be implemented when using a custom module
- **alternative-distribution-carrier** -- Often combined with custom discovery but conceptually separate

## Contrasts With
- **epmd** -- Standard EPMD uses a local daemon and DNS; alternative discovery can use any backend

# Common Errors

- **Error**: Forgetting to add `-no_epmd` when using a custom discovery module
  **Correction**: Without `-no_epmd`, the standard EPMD daemon will still start alongside your custom module. Add `-no_epmd` to prevent this unless you want both.

- **Error**: Not implementing `start_link/0` even when no processes are needed
  **Correction**: `start_link/0` is mandatory. Return `ignore` if no supervision is needed.

# Common Confusions

- **Confusion**: Thinking alternative node discovery replaces the distribution protocol
  **Clarification**: It only replaces the discovery mechanism (how nodes find each other). The distribution protocol, handshake, and connected-node communication remain unchanged.

- **Confusion**: Thinking `address_please/3` is mandatory
  **Clarification**: It is optional. If not implemented, the default `erl_epmd:address_please/3` is used. However, if `address_please/3` returns the port, then `port_please/2` can be omitted.

# Source Reference

"How to Implement an Alternative Node Discovery for Erlang Distribution" chapter, sections "Introduction" and "Discovery module".

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: HIGH -- explicitly defined with complete callback list
- Uncertainties: None
- Cross-reference status: Verified against planned slugs
