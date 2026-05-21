---
concept: Port Types
slug: port-types
category: data-types
subcategory: ports
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Runtime Metrics"
chapter_number: 5
pdf_page: null
section: "Ports"
extraction_confidence: high
aliases:
  - "recon:port_types"
  - port type names
prerequisites:
  - port
extends:
  - port
related:
  - inet-port-inspection
  - port-count-anomaly
contrasts_with: []
answers_questions:
  - "How can I find the type of a port (Files, TCP, UDP)?"
  - "How should ports be monitored globally?"
---

# Quick Definition

Port types are the VM-defined string names that classify each port (e.g. `"tcp_inet"`, `"efile"`); `recon:port_types()` returns the count of ports grouped by type.

# Core Definition

From Chapter 5, "Ports": "one can use `recon` to get them sorted by type... This list contains the types and the count for each type of port. The type name is a string and is defined by the Erlang VM itself."

# Prerequisites

- `port`: port types classify the port data type.

# Key Properties

1. Type names are strings, defined by the Erlang VM.
2. `*_inet` ports are sockets, with the prefix naming the protocol — `tcp_inet` (TCP), `udp_inet` (UDP), `sctp_inet` (SCTP).
3. `efile` is the type for files.
4. `"0/1"` and `"2/2"` are file descriptors for standard I/O channels (stdin/stdout) and standard error (stderr) respectively.
5. Other types are named after the driver they talk to — examples of *port programs* or *port drivers*.
6. `recon:port_types()` returns a list of `{TypeName, Count}` tuples.

# Construction / Recognition

Call `recon:port_types()` to see the breakdown by type. Use the type names to tell whether a leak is in TCP sockets, files, etc.

# Context & Application

Used to monitor port usage globally and, after a crash, to tell *which kind* of resource leaked (TCP vs UDP vs files), which in turn hints at where the buggy code is.

# Examples

From Chapter 5, "Ports":

```erlang-repl
1> recon:port_types().
[{"tcp_inet",21480},
 {"efile",2},
 {"udp_inet",2},
 {"0/1",1},
 {"2/2",1},
 {"inet_gethost 4 ",1}]
```

# Relationships

## Builds Upon
- port

## Enables

## Related
- inet-port-inspection
- port-count-anomaly

## Contrasts With

# Common Errors

- Assuming a non-`*_inet` type name is meaningless — it usually names the driver/port program, which is itself a useful clue.

# Common Confusions

- `"0/1"` and `"2/2"` are not socket types — they are the standard I/O and stderr file descriptors.
- The `*_inet` suffix marks sockets; the prefix is the transport protocol.

# Source Reference

Chapter 5: Runtime Metrics, Section "Ports". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from the chapter.
- Confidence rationale: high — explicitly defined with example output.
- Uncertainties: none.
- Cross-reference status: Verified
