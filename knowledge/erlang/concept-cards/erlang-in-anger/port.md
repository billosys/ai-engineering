---
concept: Port
slug: port
category: data-types
subcategory: ports
tier: foundational
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Runtime Metrics"
chapter_number: 5
pdf_page: null
section: "Ports"
extraction_confidence: high
aliases:
  - Erlang port
  - ports
prerequisites: []
extends: []
related:
  - port-types
  - inet-port-inspection
  - port-count-anomaly
contrasts_with: []
answers_questions:
  - "What is a port?"
  - "How should ports be monitored globally?"
---

# Quick Definition

A port is an Erlang data type that represents a connection to the outside world — TCP/UDP/SCTP sockets, file descriptors, and external programs or drivers.

# Core Definition

"Ports are a datatype that encompasses all kinds of connections and sockets opened to the outside world: TCP sockets, UDP sockets, SCTP sockets, file descriptors, and so on" (Chapter 5, "Ports").

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. A port is a first-class Erlang data type.
2. It abstracts external connections: TCP/UDP/SCTP sockets, file descriptors, port programs, and port drivers.
3. The total count is obtained with `length(erlang:ports())`, but that merges all types into one figure.
4. `recon:port_types()` returns the count broken down by type.
5. Each port has a controlling process (the "connected" process).
6. Ports can be linked with processes much like processes link with each other.
7. Like processes, ports support introspection — via `erlang:port_info/2` and `recon:port_info/1-2`.

# Construction / Recognition

Ports are created implicitly when you open a socket, file, or external program. Count them with `length(erlang:ports())`; classify them with `recon:port_types()`; inspect an individual one with `recon:port_info/1`.

# Context & Application

Tracking port counts globally — like process counts — helps assess load and usage and detect leaks. Knowing a node's normal port count makes anomalies (overload, DoS, descriptor leaks) recognizable.

# Examples

From Chapter 5, "Ports": "In a manner similar to processes, *Ports* should be considered... There is a general function (again, similar to processes) to count them: `length(erlang:ports())`."

# Relationships

## Builds Upon

## Enables
- port-types
- inet-port-inspection

## Related
- port-count-anomaly
- process-count-metric

## Contrasts With

# Common Errors

- Using `length(erlang:ports())` and assuming the figure tells you *what kind* of resource is leaking — it merges all types; use `recon:port_types()` to break it down.

# Common Confusions

- An Erlang "port" is a data type for external connections — not a TCP port number.
- A port is conceptually parallel to a process: both can be linked, both have rich introspection, both are counted as load metrics.

# Source Reference

Chapter 5: Runtime Metrics, Section "Ports". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from the chapter.
- Confidence rationale: high — explicitly defined.
- Uncertainties: none.
- Cross-reference status: Verified
