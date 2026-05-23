---
# === CORE IDENTIFICATION ===
concept: Distribution Controller Process
slug: distribution-controller-process

# === CLASSIFICATION ===
category: distribution
subcategory: protocol
tier: advanced

# === PROVENANCE ===
source: "ERTS User's Guide"
source_slug: otp-erts
authors: "Ericsson AB"
chapter: "How to Implement an Alternative Carrier for the Erlang Distribution"
chapter_number: null
pdf_page: null
section: "Distribution Module"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "dist controller"
  - "distribution controller"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - alternative-distribution-carrier
  - distribution-protocol
extends:
  - alternative-distribution-carrier
related:
  - distribution-module
  - distribution-connection
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a distribution controller process?"
  - "How does a distribution controller manage a distribution connection?"
  - "What BIFs are available to distribution controller processes?"
---

# Quick Definition

A distribution controller is a process (or port) responsible for dispatching traffic over a single distribution connection. Since ERTS 10.0, distribution controllers can be Erlang processes (not just ports), enabling distribution carriers to be implemented entirely in Erlang without native C drivers.

# Core Definition

The ERTS documentation states that support for distribution controller processes was introduced in ERTS version 10.0: "the traffic over a distribution channel can be managed by a process instead of only by a port. This makes it possible to implement large parts of the logic in Erlang code, and you perhaps do not even need a new driver for the protocol."

Key rules for distribution controllers:
- There must be exactly one distribution controller per connection
- A process or port can only be distribution controller for one connection
- The registration as distribution controller cannot be undone -- it persists until the controller terminates
- The distribution controller should not ignore exit signals; it may trap exits but must voluntarily terminate when an exit signal is received
- The distribution controller and the connection supervisor process should be linked together for cleanup

When the handshake completes, the `f_handshake_complete` callback provides a `DHandle` (distribution handle) needed for the following BIFs available to distribution controller processes:
- `erlang:dist_ctrl_get_data/1` -- get outgoing data to send to the remote node
- `erlang:dist_ctrl_get_data_notification/1` -- request notification when outgoing data is available
- `erlang:dist_ctrl_input_handler/2` -- register an input handler process for incoming data
- `erlang:dist_ctrl_put_data/2` -- deliver received data from the remote node

# Prerequisites

- **alternative-distribution-carrier** -- Distribution controllers are part of implementing alternative carriers
- **distribution-protocol** -- Understanding the protocol that the controller manages

# Key Properties

1. Exactly one distribution controller per connection -- no sharing, no reassignment
2. Can be either a process or a port (process support added in ERTS 10.0)
3. Registration is permanent -- persists until the controller terminates
4. Must be linked to the connection supervisor process
5. Must not ignore exit signals (may trap exits but must terminate on receipt)
6. Receives a `DHandle` after handshake completion for use with `dist_ctrl_*` BIFs
7. Created by the acceptor process (for incoming connections) or the setup process (for outgoing)
8. The `f_handshake_complete` callback signals when the controller can begin dispatching traffic

# Construction / Recognition

## To Construct/Create:
1. Spawn a process to serve as the distribution controller for a connection
2. Create the controller during `accept/1` (for incoming) or `setup/5` (for outgoing)
3. Link the controller to the connection supervisor process
4. After handshake, use the `DHandle` from `f_handshake_complete` to call `dist_ctrl_*` BIFs
5. Implement a loop that calls `erlang:dist_ctrl_get_data/1` to get outbound data and sends it via the transport

## To Identify/Recognize:
1. A process that holds a distribution handle (`DHandle`)
2. A process that calls `erlang:dist_ctrl_get_data/1` and `erlang:dist_ctrl_put_data/2`
3. Referenced as `DistCtrl` or `DistController` in distribution module callbacks

# Context & Application

Distribution controller processes are the key innovation (since ERTS 10.0) that enables implementing Erlang distribution carriers without native C code. Before this, distribution traffic could only be managed by ports, requiring a C driver. With process-based controllers, one can implement distribution over any transport accessible from Erlang (e.g., `gen_tcp`, `gen_udp`, `ssl`). The `gen_tcp_dist` and `erl_uds_dist` examples both use distribution controller processes.

# Examples

**Example 1** (Distribution Module): A distribution controller process using `dist_ctrl_*` BIFs after handshake completion:
```erlang
f_handshake_complete = fun(DistCtrl, Node, DHandle) ->
    %% Now the distribution channel is up
    %% Start getting outbound data
    erlang:dist_ctrl_get_data_notification(DHandle),
    %% Register an input handler for inbound data
    erlang:dist_ctrl_input_handler(DHandle, self()),
    %% Enter the dispatch loop
    controller_loop(DistCtrl, DHandle)
end
```

**Example 2** (Distribution Module): The acceptor process creates a distribution controller and notifies the kernel:
```erlang
%% In the acceptor process after accepting a connection:
Kernel ! {accept, AcceptorPid, DistController, Family, Proto}
%% Kernel responds with:
%%   {Kernel, controller, SupervisorPid}   -- accepted
%%   {Kernel, unsupported_protocol}        -- rejected (fatal)
```

# Relationships

## Builds Upon
- **alternative-distribution-carrier** -- Controllers are a component of alternative carrier implementations
- **distribution-protocol** -- The controller dispatches protocol messages

## Related
- **distribution-module** -- The distribution module creates and manages distribution controllers
- **distribution-connection** -- The controller handles the data flow of a connected distribution channel

## Contrasts With
None

# Common Errors

- **Error**: Creating multiple distribution controllers for one connection
  **Correction**: Exactly one distribution controller per connection. Each controller can only manage one connection.

- **Error**: Ignoring exit signals in the distribution controller
  **Correction**: The controller may trap exits, but must voluntarily terminate when an exit signal is received. Ignoring exits can leave orphaned connections.

- **Error**: Trying to unregister or reassign a distribution controller
  **Correction**: Registration as a distribution controller cannot be undone. It persists until the controller process terminates.

# Common Confusions

- **Confusion**: Thinking the distribution controller and connection supervisor are the same process
  **Clarification**: They are separate entities that must be linked. The connection supervisor handles the handshake and monitors the connection. The distribution controller dispatches traffic. They may be the same process in some implementations, but conceptually they serve different roles.

- **Confusion**: Thinking process-based controllers require a driver
  **Clarification**: The entire point of distribution controller processes (ERTS 10.0+) is to avoid needing a native C driver. The transport can be managed entirely in Erlang.

# Source Reference

"How to Implement an Alternative Carrier for the Erlang Distribution" chapter, section "Distribution Module", especially the introductory note about ERTS 10.0 and the `f_handshake_complete` callback description.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: HIGH -- explicitly defined with clear rules and BIF documentation
- Uncertainties: None
- Cross-reference status: Verified against planned slugs
