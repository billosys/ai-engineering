# CCDP: Composite Cognition Dispatch Protocol

**Draft Specification — Version 0.2**
**August 2026**

---

## 1. Abstract

This document specifies the Composite Cognition Dispatch Protocol (CCDP), a message-envelope protocol for routing cognitive requests through a deliberately constrained dispatcher to a heterogeneous set of cognitive services — large language models, theorem provers, classical planners, databases, human review queues, and composite LLM+service hybrids — under human supervision. CCDP is a supervision-tree protocol, not an agent-to-agent protocol: one side of every link is a protocol enforcement and execution coordinator that reads envelope metadata and performs structural operations — routing, schema validation, plan execution, audit — without reasoning about message content. The protocol carries the intelligence the dispatcher does not have.

CCDP's novel contribution is the epistemic dimension of cognitive dispatch. Every response carries a provenance grade indicating the evidence strength behind it (error responses, health messages, and notifications are excluded from this requirement) — from opaque assertion through formal verification to human attestation — with defined composition rules for how grades propagate through multi-service operations. Escalation is a first-class protocol operation, not an error state: a service that cannot meet the requested provenance grade returns a structured escalation that the dispatcher routes upward. Structured audit metadata is mandatory at every link. Typed service contracts are enforced through a capability registry with schema versioning and compatibility checking.

CCDP layers on HTTP transport and JSON-RPC 2.0 wire format, adding an envelope-based routing layer with provenance, audit, cost signals, health monitoring, and deadline propagation. It is designed so that a conforming Dispatcher can be implemented as a stateless-per-request coordinator with no natural-language understanding, while conforming Services range from stateless functions to long-running human review queues behind the same typed interface. Security and audit properties in this specification are protocol-level requirements; production deployments must additionally address operational security, key management, monitoring, and infrastructure hardening beyond the protocol's scope.
