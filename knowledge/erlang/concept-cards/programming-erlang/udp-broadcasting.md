---
# === CORE IDENTIFICATION ===
concept: UDP Broadcasting
slug: udp-broadcasting

# === CLASSIFICATION ===
category: distribution
subcategory: socket-programming
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Programming with Sockets"
chapter_number: 17
pdf_page: null
section: "Broadcasting to Multiple Machines"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "broadcast channel"
  - "{broadcast, true}"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-udp-module
  - udp-datagram
extends: []
related:
  - inet-module
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I broadcast a message to multiple machines?"
  - "How do I set up a UDP broadcast channel?"
  - "What is the {broadcast, true} option?"
---

# Quick Definition

UDP broadcasting sends a single datagram to every machine on a local area network at once, by opening a UDP socket with the `{broadcast, true}` option and sending to the network's broadcast address.

# Core Definition

UDP broadcasting sets up a broadcast channel so that a message is delivered to all machines on the local network ("Broadcasting to Multiple Machines"). The `broadcast` module's `send/1` function obtains the interface broadcast address via `inet:ifget("eth0", [broadaddr])`, opens a UDP socket with `gen_udp:open(5010, [{broadcast, true}])`, and sends the data with `gen_udp:send(S, Ip, 6000, IoList)` to that broadcast address. The `listen/0` function opens port 6000 on every machine and receives the broadcast datagrams. "`broadcast:send(IoList)` broadcasts `IoList` to all machines on the local area network."

# Prerequisites

- **gen_udp module** — Broadcasting is built with `gen_udp:open` and `gen_udp:send`.
- **UDP datagram** — Broadcasts are unreliable UDP datagrams.

# Key Properties

1. Requires opening the UDP socket with the `{broadcast, true}` option.
2. The datagram is sent to the network interface's broadcast address (found via `inet:ifget`).
3. Two ports are used: one to send the broadcast, one for all machines to listen on.
4. Only the broadcasting process opens the send port; every machine opens the listen port.
5. The interface name must be correct (e.g., "en0" on macOS, "eth0" on Linux) and broadcasting must be supported.
6. Routers usually drop UDP broadcasts, so listeners on different subnets typically will not receive them.

# Construction / Recognition

## To broadcast:
1. Get the broadcast address with `inet:ifget(Interface, [broadaddr])`.
2. Open a UDP socket with `gen_udp:open(SendPort, [{broadcast, true}])`.
3. Send with `gen_udp:send(S, BroadcastIp, ListenPort, IoList)`.
4. Close the socket.

## To listen for broadcasts:
1. On every machine, call `gen_udp:open(ListenPort)`.
2. Loop receiving datagrams.

# Context & Application

- **Typical contexts**: Service discovery and announcements on a local area network.
- **Common applications**: The chapter's `broadcast` module distributes an iolist to all LAN machines.
- **Historical/stylistic notes**: The chosen port numbers (5010, 6000) have no significance; any free ports work.

# Examples

**Example 1** ("Broadcasting to Multiple Machines", `broadcast.erl`): `send/1` checks `inet:ifget("eth0", [broadaddr])`, opens `gen_udp:open(5010, [{broadcast, true}])`, and sends to the broadcast IP on port 6000.

## Worked Example

```erlang
send(IoList) ->
    case inet:ifget("eth0", [broadaddr]) of
        {ok, [{broadaddr, Ip}]} ->
            {ok, S} = gen_udp:open(5010, [{broadcast, true}]),
            gen_udp:send(S, Ip, 6000, IoList),
            gen_udp:close(S);
        _ ->
            io:format("Bad interface name, or\n"
                      "broadcasting not supported\n")
    end.
```

# Relationships

## Related
- **inet module** — `inet:ifget` retrieves the interface's broadcast address.

# Common Errors

- **Error**: Using the wrong interface name (e.g., "eth0" on a machine where the interface is "en0").
  **Correction**: Use the correct interface name for the operating system; `inet:ifget` fails otherwise.

- **Error**: Forgetting the `{broadcast, true}` option.
  **Correction**: A normal UDP socket cannot send to a broadcast address; the option must be set.

# Common Confusions

- **Confusion**: Expecting broadcasts to reach machines on other subnets.
  **Clarification**: Routers drop UDP broadcasts by default, so only same-subnet machines receive them.

# Source Reference

Chapter 17: "Programming with Sockets", section "Broadcasting to Multiple Machines". Code from `broadcast.erl`.

# Verification Notes

- Definition source: Direct synthesis and quotes from "Broadcasting to Multiple Machines".
- Confidence rationale: HIGH — the technique and code are explicitly presented.
- Uncertainties: None.
- Cross-reference status: Verified; canonical slugs used.
- Re-extraction notes: Fresh extraction.
