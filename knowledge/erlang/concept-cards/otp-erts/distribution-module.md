---
# === CORE IDENTIFICATION ===
concept: Distribution Module
slug: distribution-module

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
  - "dist module"
  - "_dist module"
  - "distribution callback module"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - distribution-protocol
  - distribution-handshake
extends: []
related:
  - alternative-distribution-carrier
  - distribution-controller-process
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a distribution module in Erlang?"
  - "What callbacks must a distribution module implement?"
  - "How do I implement an alternative distribution carrier?"
---

# Quick Definition

A distribution module is an Erlang module with the `_dist` suffix that implements well-defined callbacks for `net_kernel` to manage distribution connections. It handles node discovery, listening for connections, connecting to other nodes, and performing the handshake -- delegating most handshake complexity to `dist_util`.

# Core Definition

The ERTS documentation describes the distribution module as one that "exposes an API that `net_kernel` calls in order to manage connections to other nodes. The module name should have the suffix `_dist`." The module must create a listening entity, an acceptor process, and for each connection, a connection supervisor process and a distribution controller.

The following callbacks are mandatory:
- **`listen(Name)` / `listen(Name, Host)`** -- Called once at distribution startup to create a listening entity. Returns `{ok, {Listen, Address, Creation}}`. If using EPMD, typically uses `erl_epmd` to register the listen port.
- **`address()`** -- Returns the `#net_address{}` record without creating a listen socket.
- **`accept(Listen)`** -- Spawns an acceptor process (preferably at `max` priority) that accepts incoming connections and creates distribution controllers.
- **`accept_connection(AcceptorPid, DistCtrl, MyNode, Allowed, SetupTime)`** -- Spawns a connection supervisor that performs the incoming handshake via `dist_util:handshake_other_started/1`.
- **`setup(Node, Type, MyNode, LongOrShortNames, SetupTime)`** -- Spawns a connection supervisor that connects to a remote node and performs the outgoing handshake via `dist_util:handshake_we_started/1`.
- **`close(Listen)`** -- Closes the listen handle.
- **`select(NodeName)`** -- Returns `true` if the hostname is valid for this protocol.

Optional callbacks: `setopts(Listen, Opts)` and `getopts(Listen, Opts)`.

The handshake is configured via a `#hs_data{}` record (defined in `kernel/include/dist_util.hrl`) containing callback funs for send, receive, address resolution, tick, statistics, and socket options.

# Prerequisites

- **distribution-protocol** -- The module implements parts of the distribution protocol
- **distribution-handshake** -- The module delegates handshake logic to `dist_util`

# Key Properties

1. Module name must end with `_dist` suffix (e.g., `gen_tcp_dist`, `uds_dist`)
2. Enabled via `-proto_dist <name>` (strip the `_dist` suffix)
3. Seven mandatory callbacks: `listen/1,2`, `address/0`, `accept/1`, `accept_connection/5`, `setup/5`, `close/1`, `select/1`
4. Two optional callbacks: `setopts/2`, `getopts/2`
5. Uses `dist_util:handshake_we_started/1` (initiator) and `dist_util:handshake_other_started/1` (acceptor)
6. Connection supervisor processes should execute at `max` priority
7. Use `dist_util:net_ticker_spawn_options()` for spawn options (default: `[link, {priority, max}]`)
8. The `#hs_data{}` record contains both handshake-phase funs (`f_send`, `f_recv`, `f_address`, etc.) and connection-phase funs (`mf_tick`, `mf_getstat`)
9. Can configure distribution flags via `add_flags`, `reject_flags`, and `require_flags` in `#hs_data{}`

# Construction / Recognition

## To Construct/Create:
1. Create a module named `<protocol>_dist`
2. Implement all mandatory callbacks
3. In `accept_connection/5` and `setup/5`, populate a `#hs_data{}` record and call the appropriate `dist_util` function
4. Create distribution controllers (process or port) for each connection
5. Enable with `erl -proto_dist <protocol>`

## To Identify/Recognize:
1. Module name ending in `_dist`
2. Exports `listen/1` or `listen/2`, `accept/1`, `setup/5`, etc.
3. Uses `dist_util:handshake_we_started/1` or `dist_util:handshake_other_started/1`

# Context & Application

The distribution module is the central abstraction for pluggable distribution carriers. By implementing this module, developers can run Erlang distribution over any transport -- TCP, TLS, Unix domain sockets, UDP (with retransmission), shared memory, or custom protocols. The OTP source includes reference implementations: `inet_tcp_dist` (standard TCP), `inet_tls_dist` (TLS), `gen_tcp_dist` (process-based TCP), and `erl_uds_dist` (Unix domain sockets).

# Examples

**Example 1** (Distribution Module, callbacks): The listen callback for a custom distribution module:
```erlang
listen(Name) ->
    {ok, Socket} = my_transport:listen(0),
    {ok, Port} = my_transport:port(Socket),
    {ok, Creation} = erl_epmd:register_node(Name, Port),
    {ok, Host} = inet:gethostname(),
    Address = #net_address{host = Host, protocol = my_proto, family = inet},
    {ok, {Socket, Address, Creation}}.
```

**Example 2** (Distribution Module, #hs_data{}): Key fields in the handshake data record:
```erlang
#hs_data{
    kernel_pid = Kernel,
    other_node = Node,
    this_node = MyNode,
    socket = DistCtrl,          %% the distribution controller
    timer = dist_util:start_timer(SetupTime),
    f_send = fun my_transport:send/2,
    f_recv = fun my_transport:recv/3,
    f_address = fun(_, N) -> get_address(N) end,
    f_setopts_pre_nodeup = fun(_) -> ok end,
    f_setopts_post_nodeup = fun(_) -> ok end,
    f_getll = fun(DistCtrl) -> DistCtrl end,
    mf_tick = fun my_transport:tick/1,
    mf_getstat = fun my_transport:getstat/1,
    f_handshake_complete = fun handshake_complete/3
}
```

# Relationships

## Builds Upon
- **distribution-protocol** -- The module implements the protocol's connection management
- **distribution-handshake** -- Handshake is delegated to `dist_util` using callback funs

## Related
- **alternative-distribution-carrier** -- The distribution module is the core component of an alternative carrier
- **distribution-controller-process** -- Created and managed by the distribution module

## Contrasts With
None

# Common Errors

- **Error**: Not linking the connection supervisor to the caller of `accept_connection/5` or `setup/5`
  **Correction**: The spawned process should be linked to the caller (a `net_kernel` representative). Use `dist_util:net_ticker_spawn_options()` which includes `link` by default.

- **Error**: Using a non-blocking tick operation in `mf_tick`
  **Correction**: Actually, the tick MUST be non-blocking. The documentation warns: "It is of vital importance that this operation does not block the caller for a long time. This since it is called from the connection supervisor."

- **Error**: Setting undefined `#hs_data{}` fields to non-`undefined` values
  **Correction**: "Not documented fields should not be set, i.e., should be left as `undefined`."

# Common Confusions

- **Confusion**: Thinking the distribution module handles handshake logic directly
  **Clarification**: The distribution module provides callbacks in a `#hs_data{}` record. The actual handshake protocol is implemented by `dist_util:handshake_we_started/1` and `dist_util:handshake_other_started/1`.

- **Confusion**: Thinking `socket` in `#hs_data{}` must be an actual socket
  **Clarification**: The `socket` field holds the distribution controller identifier, which can be either a process or port identifier. The name is historical.

# Source Reference

"How to Implement an Alternative Carrier for the Erlang Distribution" chapter, section "Distribution Module", including "Exported Callback Functions", "The #hs_data{} Record", "Distribution Data Delivery", and "Enable Your Distribution Module".

# Verification Notes

- Definition source: Direct from source text with complete callback specifications
- Confidence rationale: HIGH -- explicitly defined with detailed API
- Uncertainties: None
- Cross-reference status: Verified against planned slugs
