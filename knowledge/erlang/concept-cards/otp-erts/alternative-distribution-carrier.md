---
# === CORE IDENTIFICATION ===
concept: Alternative Distribution Carrier
slug: alternative-distribution-carrier

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
section: "Introduction"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "custom distribution carrier"
  - "alternative carrier"
  - "custom distribution transport"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - distribution-protocol
  - distribution-handshake
  - distribution-module
extends:
  - distribution-protocol
related:
  - distribution-controller-process
  - alternative-node-discovery
  - erlang-driver
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a distribution carrier?"
  - "How do I implement an alternative distribution carrier?"
  - "What must I know before implementing a custom distribution carrier?"
---

# Quick Definition

An alternative distribution carrier replaces TCP/IP as the transport protocol for Erlang distribution. Implementing one requires writing an Erlang driver (or using an existing one), an Erlang interface module for the driver, a distribution module with well-defined callbacks, and boot scripts to make the implementation available at startup.

# Core Definition

The ERTS documentation describes the process of replacing TCP/IP with another protocol for Erlang distribution. The main steps are:

1. **Writing an Erlang driver** (optional since ERTS 10.0): The protocol must be available to the Erlang machine. Traditionally this required a native C driver, but since ERTS 10.0 distribution controller processes allow implementing the transport entirely in Erlang. For example, distribution over UDP could use `gen_udp` with custom retransmission logic.

2. **Writing an Erlang interface for the driver**: An interface module (typically mimicking `inet`/`inet_tcp`) enables testing the driver independently and provides the API used by the distribution module.

3. **Writing a distribution module**: A module with the suffix `_dist` that implements well-defined callbacks for finding nodes, creating listen sockets, connecting, and performing handshakes. The `dist_util` module handles most of the handshake complexity.

4. **Creating boot scripts**: The protocol must be available at boot time. Code can only depend on `Kernel`, `STDLIB`, and the application itself -- no calls to the `application` module or modules not loaded at boot time.

The carrier must implement a reliable, order-maintaining, variable-length packet-oriented protocol. All error correction, resending, and packaging must be handled by the carrier or its underlying protocol.

# Prerequisites

- **distribution-protocol** -- Understanding the overall protocol being implemented
- **distribution-handshake** -- The carrier must support the handshake procedure
- **distribution-module** -- The callback module structure for the carrier

# Key Properties

1. The carrier must provide reliable, ordered, lossless delivery (by default)
2. Ordering can be relaxed to per-sender/receiver pairs by rejecting strict-order flags
3. Since ERTS 10.0, distribution controller processes allow pure-Erlang implementations
4. The distribution module name must end with `_dist` suffix
5. Enabled via `-proto_dist <name>` command-line argument (e.g., `-proto_dist gen_tcp` for `gen_tcp_dist`)
6. If not using EPMD, also specify `-no_epmd`
7. Code must work during the startup phase -- only `Kernel`, `STDLIB`, and the custom application can be used
8. Each connection needs exactly one distribution controller (process or port)
9. The `dist_util` module provides handshake, cookie, timer, and ticking utilities
10. Drivers must set `ERL_DRV_FLAG_SOFT_BUSY` for distribution use

# Construction / Recognition

## To Construct/Create:
1. Choose a transport protocol and decide whether to use a driver or distribution controller processes
2. Implement the distribution module with required callbacks (`listen/1,2`, `accept/1`, `accept_connection/5`, `setup/5`, `close/1`, `select/1`)
3. Populate the `#hs_data{}` record with callback funs and pass to `dist_util:handshake_we_started/1` or `dist_util:handshake_other_started/1`
4. Enable with `erl -proto_dist <name>` (where the module is `<name>_dist`)

## To Identify/Recognize:
1. A module named `*_dist` in the Kernel application's examples or a custom application
2. Uses `-proto_dist` flag at the command line
3. Implements the distribution module callback API

# Context & Application

Alternative distribution carriers enable Erlang distribution over non-TCP transports such as Unix domain sockets, UDP, shared memory, or custom protocols. The `gen_tcp_dist` and `erl_uds_dist` examples in the Kernel application demonstrate pure-Erlang implementations using distribution controller processes. This capability is essential for embedded systems, specialized network environments, or performance-critical deployments where TCP/IP is not optimal.

# Examples

**Example 1** (Putting It All Together): Starting a node with a custom distribution carrier:
```bash
$ erl -pa $ERL_TOP/lib/kernel/examples/uds_dist/ebin \
      -proto_dist uds -no_epmd -sname bong
```

**Example 2** (Putting It All Together): Starting distribution at runtime for testing:
```erlang
net_kernel:start([bing, shortnames]).
```

**Example 3** (Introduction): Using `ERL_FLAGS` for complex parameters:
```bash
$ ERL_FLAGS="-pa $ERL_TOP/lib/kernel/examples/uds_dist/ebin -proto_dist uds -no_epmd"
$ export ERL_FLAGS
$ erl -sname bang
```

# Relationships

## Builds Upon
- **distribution-protocol** -- The carrier implements the transport layer of the distribution protocol
- **distribution-handshake** -- The carrier must support the handshake procedure via `dist_util`
- **distribution-module** -- The callback module defines the carrier's Erlang API

## Related
- **distribution-controller-process** -- Process-based distribution control (since ERTS 10.0)
- **alternative-node-discovery** -- Custom node discovery often accompanies custom carriers
- **erlang-driver** -- Native C drivers for custom transport protocols

## Contrasts With
None

# Common Errors

- **Error**: Implementing a driver that performs blocking operations in callbacks
  **Correction**: Driver callback routines execute in the main thread of the Erlang machine. They must never block. All I/O must be non-blocking, using `driver_select` for readiness notification.

- **Error**: Using modules not available at boot time in the distribution module
  **Correction**: Only `Kernel`, `STDLIB`, and the distribution application itself can be used. No calls to the `application` module are allowed.

- **Error**: Allowing more than one distribution controller per connection
  **Correction**: There must be exactly one distribution controller per connection. A process or port can only be a distribution controller for one connection, and the registration cannot be undone.

# Common Confusions

- **Confusion**: Thinking a native C driver is always required
  **Clarification**: Since ERTS 10.0, distribution controller processes can manage distribution traffic from Erlang code. A driver is only needed if the transport protocol requires one. Examples like `gen_tcp_dist` and `erl_uds_dist` are written entirely in Erlang.

- **Confusion**: Thinking the distribution module handles the handshake directly
  **Clarification**: The `dist_util` module handles most handshake logic. The distribution module provides callbacks (in a `#hs_data{}` record) that `dist_util` uses to send/receive data and manage the connection.

# Source Reference

"How to Implement an Alternative Carrier for the Erlang Distribution" chapter, sections "Introduction", "Distribution Module", "The Driver", and "Putting It All Together".

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: HIGH -- explicitly described step-by-step process with examples
- Uncertainties: None
- Cross-reference status: Verified against planned slugs
