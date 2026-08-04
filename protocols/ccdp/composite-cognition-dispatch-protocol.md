---
title: "CCDP: Composite Cognition Dispatch Protocol"
description: >
  A message-envelope protocol for routing cognitive requests through a
  deliberately simple dispatcher to heterogeneous cognitive services under
  human supervision.
version: "0.1"
date: 2026-08-04
author: Duncan McGreggor
status: Draft Specification
---

## Table of Contents

- [1. Abstract](#section-1)
- [2. Status of This Memo and Conventions](#section-2)
  - [2.1. Status of This Memo](#section-2-1)
  - [2.2. Requirements Language](#section-2-2)
  - [2.3. Data Format Conventions](#section-2-3)
  - [2.4. Notation](#section-2-4)
  - [2.5. Normative Status of Non-Prose Elements](#section-2-5)
- [3. Introduction](#section-3)
  - [3.1. The Problem](#section-3-1)
  - [3.2. Why Existing Protocols Are Insufficient](#section-3-2)
  - [3.3. What Is Different About Cognitive Dispatch](#section-3-3)
  - [3.4. Design Principles](#section-3-4)
  - [3.5. Scope](#section-3-5)
- [4. Terminology](#section-4)
- [5. Architecture Overview](#section-5)
  - [5.1. Topology](#section-5-1)
  - [5.2. Component Roles](#section-5-2)
  - [5.3. Service Modes](#section-5-3)
  - [5.4. The Decomposition Service](#section-5-4)
  - [5.5. Relationship to Supervision Trees](#section-5-5)
- [6. Protocol Layers](#section-6)
  - [6.1. Layering Rationale](#section-6-1)
  - [6.2. Layer Architecture](#section-6-2)
  - [6.3. Layer Independence](#section-6-3)
  - [6.4. Comparison to the Emerging Agent Protocol Stack](#section-6-4)
  - [6.5. Structural Operations Across Layers](#section-6-5)
- [7. Message Format](#section-7)
  - [7.1. Wire Encoding](#section-7-1)
  - [7.2. Message Types](#section-7-2)
  - [7.3. Envelope Structure](#section-7-3)
  - [7.4. Content Structure](#section-7-4)
  - [7.5. Dispatcher Audit Annotation](#section-7-5)
  - [7.6. Size Limits](#section-7-6)
  - [7.7. Extensibility and Forward Compatibility](#section-7-7)
  - [7.8. Machine-Readable Schemas](#section-7-8)
  - [7.9. HTTP Status Code Mapping](#section-7-9)
- [8. Capability Registry](#section-8)
  - [8.1. Role and Scope](#section-8-1)
  - [8.2. Capability Records](#section-8-2)
  - [8.3. Well-Known Capability Types](#section-8-3)
  - [8.4. Registry Interface](#section-8-4)
  - [8.5. Schema Versioning and Compatibility](#section-8-5)
  - [8.6. Registry Availability](#section-8-6)
- [9. Routing](#section-9)
  - [9.1. Routing Principles](#section-9-1)
  - [9.2. Routing Algorithm](#section-9-2)
  - [9.3. Routing for Decomposed Sub-Requests](#section-9-3)
  - [9.4. Escalation Routing](#section-9-4)
  - [9.5. Retry Policy](#section-9-5)
  - [9.6. Circuit Breaker Integration](#section-9-6)
  - [9.7. Routing Table](#section-9-7)
- [10. Provenance and Evidence Grades](#section-10)
  - [10.1. Rationale](#section-10-1)
  - [10.2. Grade Taxonomy](#section-10-2)
  - [10.3. Grade Assignment Rules](#section-10-3)
  - [10.4. Grade Comparison and Ordering](#section-10-4)
  - [10.5. Grade Composition](#section-10-5)
  - [10.6. Worked Examples [Informative]](#section-10-6)
  - [10.7. Provenance in the Audit Trail](#section-10-7)
  - [10.8. Provenance and Trust](#section-10-8)
- [11. Audit Trail](#section-11)
  - [11.1. Audit as Core Protocol](#section-11-1)
  - [11.2. Audit Record Structure](#section-11-2)
  - [11.3. Trace Context Propagation](#section-11-3)
  - [11.4. Mandatory Audit Fields](#section-11-4)
  - [11.5. Audit Storage and Retention](#section-11-5)
  - [11.6. Audit Store Failure Behavior](#section-11-6)
  - [11.7. Audit as Supervision Input](#section-11-7)
- [12. Flow Control and Resource Signals](#section-12)
  - [12.1. The Resource Problem](#section-12-1)
  - [12.2. Cost Budgets](#section-12-2)
  - [12.3. Capacity Advertisements](#section-12-3)
  - [12.4. Deadline Propagation](#section-12-4)
  - [12.5. Back-Pressure](#section-12-5)
  - [12.6. Resource-Aware Routing](#section-12-6)
  - [12.7. Bullwhip Effect Warning](#section-12-7)
- [13. Error Handling and Escalation](#section-13)
  - [13.1. Error Philosophy](#section-13-1)
  - [13.2. Protocol Error Codes](#section-13-2)
  - [13.3. Escalation Reasons](#section-13-3)
  - [13.4. Escalation Chain Processing](#section-13-4)
  - [13.5. Service Error Handling](#section-13-5)
  - [13.6. Health Monitoring and Circuit Breakers](#section-13-6)
  - [13.7. Graceful Degradation](#section-13-7)
- [14. Decomposition](#section-14)
  - [14.1. The Decomposition Problem](#section-14-1)
  - [14.2. When Decomposition Occurs](#section-14-2)
  - [14.3. Decomposition Plan Structure](#section-14-3)
  - [14.4. Dispatcher Execution of Decomposition Plans](#section-14-4)
  - [14.5. Decomposition Service Contract](#section-14-5)
  - [14.6. Recursive Decomposition](#section-14-6)
- [15. Security](#section-15)
  - [15.1. Security Posture](#section-15-1)
  - [15.2. Authentication](#section-15-2)
  - [15.3. Authorization](#section-15-3)
  - [15.4. Message Integrity](#section-15-4)
  - [15.5. Replay Protection](#section-15-5)
  - [15.6. Isolation](#section-15-6)
  - [15.7. Credential Handling](#section-15-7)
  - [15.8. Rate Limiting as Security](#section-15-8)
- [16. Conformance](#section-16)
  - [16.1. Conforming Dispatcher](#section-16-1)
  - [16.2. Conforming Service](#section-16-2)
  - [16.3. Conforming Registry](#section-16-3)
  - [16.4. Conformance Levels](#section-16-4)
  - [16.5. Interoperability](#section-16-5)
  - [16.6. Conformance Testing](#section-16-6)
- [17. Security Considerations](#section-17)
  - [17.1. Threat Model](#section-17-1)
  - [17.2. Known Attack Vectors](#section-17-2)
  - [17.3. NSA/CISA Recommendations Applied to CCDP](#section-17-3)
  - [17.4. Honest Limitations](#section-17-4)
- [18. References](#section-18)
  - [18.1. Normative References](#section-18-1)
  - [18.2. Informative References — Protocol Design Foundations](#section-18-2)
  - [18.3. Informative References — Theoretical Foundations](#section-18-3)
  - [18.4. Informative References — Additional Sources](#section-18-4)
- [19. Version History](#section-19)
  - [19.1. Version 0.2.0](#section-19-1)
  - [19.2. Version 0.1.0](#section-19-2)

<a id="section-1"></a>
## Abstract

This document specifies the Composite Cognition Dispatch Protocol (CCDP), a message-envelope protocol for routing cognitive requests through a deliberately constrained dispatcher to a heterogeneous set of cognitive services — large language models, theorem provers, classical planners, databases, human review queues, and composite LLM+service hybrids — under human supervision. CCDP is a supervision-tree protocol, not an agent-to-agent protocol: one side of every link is a protocol enforcement and execution coordinator that reads envelope metadata and performs structural operations — routing, schema validation, plan execution, audit — without reasoning about message content. The protocol carries the intelligence the dispatcher does not have.

CCDP's novel contribution is the epistemic dimension of cognitive dispatch. All RESPONSE, ESCALATION, and DECOMPOSITION_RESULT messages that carry cognitive outputs include a provenance grade indicating the evidence strength behind them — from opaque assertion through formal verification to human attestation — with defined composition rules for how grades propagate through multi-service operations. Error responses, health messages, and notifications do not carry provenance. Escalation is a first-class protocol operation, not an error state: a service that cannot meet the requested provenance grade returns a structured escalation that the dispatcher routes upward. Structured audit metadata is mandatory for every Dispatcher-mediated hop — every message the Dispatcher processes generates an audit record. Typed service contracts are enforced through a capability registry with schema versioning and compatibility checking.

CCDP layers on HTTP transport and JSON-RPC 2.0 wire format, adding an envelope-based routing layer with provenance, audit, cost signals, health monitoring, and deadline propagation. It is designed so that a conforming Dispatcher can be implemented as a self-contained-message coordinator with no natural-language understanding — each message carries all context needed for processing; however, high-availability deployments require shared operational state for replay caches, circuit-breaker state, health tables, and audit stores (Section 5.1) — while conforming Services range from stateless functions to long-running human review queues behind the same typed interface. Security and audit properties in this specification are protocol-level requirements; production deployments must additionally address operational security, key management, monitoring, and infrastructure hardening beyond the protocol's scope.

<a id="section-2"></a>
# Status of This Memo and Conventions

<a id="section-2-1"></a>
## Status of This Memo

This document specifies a protocol for composite cognition dispatch. It is published as an initial specification for examination, implementation feedback, and iterative refinement. Distribution is unlimited.

This specification is versioned following Semantic Versioning [SemVer] (MAJOR.MINOR.PATCH). The current version is 0.2.0. A MAJOR version increment indicates breaking changes to the wire format or core semantics. A MINOR version increment indicates backward-compatible additions. A PATCH version increment indicates clarifications or corrections.

This specification uses two independent version identifiers. The **document version** (currently 0.2.0) tracks the maturity of the specification text — its completeness, internal consistency, and review status. The **wire protocol version** (currently `"1.0"`, carried in every message's `envelope.ccdp_version` field) tracks the on-the-wire format. A document revision that clarifies prose, tightens conformance requirements, or adds non-breaking features increments the document version without changing the wire protocol version. A document revision that changes message structure, adds required envelope fields, or alters wire semantics increments the wire protocol version. Implementations negotiate by wire protocol version; the document version is for human readers and specification governance.

**Pre-1.0 stability note.** While the document version is below 1.0 and no conforming implementations have been declared, document revisions MAY change wire-visible semantics without incrementing the wire protocol version. The wire protocol version will be frozen at the first stable release (document version 1.0.0). Implementers building against pre-1.0 drafts should track the document version and expect wire-level changes between revisions.

<a id="section-2-2"></a>
## Requirements Language

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 [RFC 2119] [RFC 8174] when, and only when, they appear in all capitals, as shown here.

<a id="section-2-3"></a>
## Data Format Conventions

This specification uses JSON [RFC 8259] for all data representation. Field names use `snake_case`. Timestamps use ISO 8601 format with mandatory UTC timezone designator (`Z`). Unique identifiers use UUID v4 [RFC 9562] unless otherwise specified.

Trace identifiers (`trace_id`) and span identifiers (`span_id`) use W3C Trace Context format — 32-character and 16-character lowercase hexadecimal strings respectively — not UUID format. Where this specification says "unique identifiers use UUID v4," it refers to application-level identifiers such as `request_id` and `idempotency_key`, not trace-context identifiers.

All examples in this document are informative unless explicitly marked as normative. Where examples show JSON structures, elided fields are indicated by comments (`// ...`) and do not imply that those fields are optional.

Where examples show JSON structures with `// ...` comments, the comments are an expository convenience and are not valid JSON. Implementations MUST NOT include comments in wire-format messages. The content type for all CCDP messages is `application/json` with charset UTF-8. JSON numbers follow IEEE 754 double-precision semantics; implementations requiring higher precision for monetary or cryptographic values SHOULD use string-encoded representations. Enumeration values in this specification use `UPPER_SNAKE_CASE` (e.g., `FORMALLY_VERIFIED`, `SEARCH_EXHAUSTED`). Reverse-domain identifiers (capability types, metadata namespace keys) use dot-separated segments (e.g., `org.ccdp.language.generation`). These conventions are normative for wire-format values.

Monetary values in CCDP messages SHOULD be represented as strings (e.g., `"4.50"` not `4.50`) to avoid IEEE 754 floating-point precision loss. All monetary-value examples in this specification use string representations.

<a id="section-2-4"></a>
## Notation

When this specification refers to a message field, it uses dot notation: `envelope.request_id` refers to the `request_id` field within the `envelope` object. Array elements are indicated by bracket notation: `envelope.provenance.evidence[0]` refers to the first element of the `evidence` array within the `provenance` object.

The notation `Section N` refers to sections of this specification by their number. Cross-references to other standards use their document identifier (e.g., [RFC 2119]).

<a id="section-2-5"></a>
## Normative Status of Non-Prose Elements

All examples in this specification are informative unless explicitly marked as normative. Tables that list requirements use normative language (MUST, SHOULD, MAY) and carry the same force as prose requirements. Diagrams are informative aids. Design notes (marked as such) are informative rationale and do not create protocol obligations.

<a id="section-3"></a>
# Introduction

<a id="section-3-1"></a>
## The Problem

A composite cognition system assembles engineering-grade cognitive output by routing requests to specialized services — each operating in its domain of competence — rather than relying on a single monolithic model to simulate all cognitive faculties. The architectural claim is grounded in a structural result: a single forward pass of a transformer (or state-space model) sits in the complexity class TC⁰ and cannot compute inherently sequential functions in a single pass (that is, functions outside TC⁰ require either multiple passes or external state — the formal justification for external cognitive organs, not a claim that LLMs cannot perform any sequential reasoning) [Merrill & Sabharwal 2023]. Chain-of-thought mitigates this by externalizing serial state into the token stream, but an LLM cannot reliably verify its own reasoning by introspection — self-correction without external feedback often leaves accuracy flat or makes it worse [Huang et al. 2024]. The error floor is architectural, not a reliability defect.

The consequence is that a language model is best understood as a *language organ* — superb at natural-language understanding, generation, translation between representations, and fuzzy pattern completion — composed with *external organs* that provide the faculties it lacks: deduction (theorem provers, SMT solvers), planning (classical planners with sound validators), durable state (typed ledger with provenance), and selection/verification (calibrated verifiers, process-reward models). A human supervisor provides the faculties for which no working external organ exists: broad abstraction, specification, and open-ended value judgment [ARC-AGI-2; Chollet et al. 2025].

This architecture requires a protocol. Requests must flow from humans (and from services making sub-requests) through a central point — the dispatcher — to the appropriate service, with responses flowing back. The dispatcher must route correctly, and every link in the chain must be auditable. The protocol must carry enough structure for routing decisions to be classification rather than reasoning — the dispatcher reads envelopes, not content.

No existing protocol jointly satisfies these requirements: typed envelope routing through a non-cognitive coordinator, mandatory structured audit, provenance grades with composition rules, first-class escalation, cost and deadline signals, and a capability registry with schema versioning.

<a id="section-3-2"></a>
## Why Existing Protocols Are Insufficient

<a id="section-3-2-1"></a>
### MCP (Model Context Protocol)

MCP is the closest existing protocol to CCDP's problem space — it connects language models to external capabilities. Its core abstraction (tools, resources, prompts) covers most LLM-to-service interactions.

[Informative] Its ecosystem velocity — a large and fast-growing community of server implementations — is further evidence the abstraction is useful, though this is a qualitative ecosystem observation rather than a claim grounded in a primary source.

MCP's July 2026 stateless pivot [MCP 2026-07-28 RC] is a significant operational improvement: self-contained requests, routing headers, W3C Trace Context propagation. But MCP has five structural shortcomings that its architectural evolution does not address:

**Designed for smart consumers, not dumb dispatchers.** MCP assumes the client (the LLM/host) is the intelligent party — it interprets natural-language tool descriptions, decides which tools to invoke, and manages conversation flow. Tool descriptions are free-text strings meant for LLM consumption. For CCDP's dispatcher — a protocol enforcement and execution coordinator that operates on envelope metadata — MCP carries insufficient routing structure. The protocol intelligence lives in the consumer, not the envelope.

**No mandatory audit.** MCP does not mandate structured logging of tool invocations. Audit trails are implementation concerns. For a supervision-tree architecture where every link must be inspectable, audit metadata must be a core protocol field, not an afterthought.

**No cost or resource signals.** MCP provides no protocol-native required cost budget, consumption reporting, or deadline enforcement fields comparable to CCDP's flow-control layer (Section 12). A dispatcher cannot make resource-rational routing decisions without this information. TCP has congestion signals (ECN, window advertisements); a cognitive dispatch protocol needs cognitive-resource signals.

**Security by implementation discipline.** MCP's security posture is highly dependent on implementation discipline rather than protocol guarantees: no mandated authentication, tool parameter injection enabling arbitrary code execution, tool naming collisions exploitable from public registries. The 2026-07-28 spec adds OAuth 2.0 authorization with Pushed Authorization Requests [RFC 9126] and PKCE [RFC 7636], but the "security by convention" orientation persists.

**No epistemic dimension.** Most fundamentally, MCP treats service outputs as data. CCDP treats them as *claims with epistemic status*. A prover's output and an LLM's output are structurally different kinds of evidence, and the protocol must carry that distinction. MCP has no concept of provenance grades, evidence strength, or provenance-grade-below-threshold escalation (CCDP's `PROVENANCE_BELOW_REQUIREMENT` escalation reason).

<a id="section-3-2-2"></a>
### A2A (Agent-to-Agent Protocol)

A2A [Google 2025] fills the peer-to-peer coordination gap MCP leaves. Its Agent Cards provide capability discovery; its task lifecycle (submitted → working → completed/failed) suits long-running operations; and its opacity principle — agents collaborate on capabilities without exposing internals — is architecturally sound.

A2A's limitation for CCDP is that it assumes both sides of a link are *agents* — capable, autonomous entities that negotiate and decide. CCDP's dispatcher is deliberately not an agent. It is a protocol enforcement and execution coordinator. A2A's complexity (Agent Card infrastructure, multi-transport support, autonomous negotiation) is overkill for a system where one side is a constrained coordinator, not an autonomous agent, and its peer-to-peer topology does not match CCDP's star topology.

<a id="section-3-2-3"></a>
### gRPC and Protocol Buffers

gRPC provides the right *ideas*: typed contracts via protobuf schemas, streaming, interceptor chains for cross-cutting concerns. Industry-proven at Google scale.

gRPC's *implementation complexity* works against the constrained-coordinator principle. Schema version management is a chronic operational wound — the discipline of never reusing field numbers, managing `.proto` file distribution, and coordinating the protoc toolchain across heterogeneous services creates friction that compounds. gRPC's full implementation stack is substantial, and its operational overhead (protoc toolchain, `.proto` file distribution, field-number management) works against the constrained-coordinator principle. A dispatcher should not need a protoc toolchain. CCDP adopts gRPC's design principles (typed contracts, deadline propagation, interceptor-style audit) without its implementation weight, using JSON Schema for runtime-validatable contracts and JSON-RPC 2.0 for the wire format.

<a id="section-3-2-4"></a>
### FIPA-ACL: The Cautionary Tale

FIPA-ACL [1990s–2000s] established the concept of typed communicative acts — messages typed by performative (request, inform, query, escalate) with sender/receiver/content/ontology metadata. This concept is exactly right for cognitive dispatch.

FIPA-ACL never escaped the lab. It lacked verifiable identity, governance frameworks, runtime tooling, and practical deployment paths. It was described in a comprehensive survey as having limited practical deployment despite its formal elegance [arXiv:2509.02317]. CCDP inherits FIPA's insight — speech acts as message types — while designing explicitly against its failure modes: every protocol feature must be practically deployable with minimal tooling, not formally elegant in isolation.

<a id="section-3-3"></a>
## What Is Different About Cognitive Dispatch

The distinction between cognitive dispatch and data routing — the reason CCDP cannot be a thin layer over an existing RPC framework — lies in three properties unique to cognitive output:

**Cognitive outputs are claims, not data.** A database query returns a fact. A theorem prover returns a proof. An LLM returns a plausible completion. These are structurally different kinds of evidence, and a protocol that treats them identically forces the consumer to reconstruct epistemic status from scratch at every boundary. CCDP makes provenance a first-class protocol field: every response carries a grade indicating the evidence strength behind it, with defined composition rules for multi-service operations (Section 10).

**Provenance-grade insufficiency is a routing event, not an error.** When a cognitive service cannot produce output at the requested provenance grade, this is not a failure — it is information. "I can generate candidate solutions but cannot verify them" is a legitimate, structured response that the dispatcher should route to a verification service or escalate to a human. CCDP defines escalation as a protocol message type with structured routing semantics (Section 13).

**The specification-recursion problem.** Formal verification relocates error rather than eliminating it: "did we build it right?" becomes "did we specify the right thing?" [Vericoding; Goodhart 1975]. An LLM that games a weak specification into a vacuous proof is not a verification failure — it is a Goodhart failure. CCDP's provenance system is designed with this recursion in mind: a grade of FORMALLY_VERIFIED carries a scope field binding it to a specific specification, and the specification's own provenance is separately tracked (Section 10).

<a id="section-3-4"></a>
## Design Principles

CCDP is governed by eight principles, each grounded in the research base:

1. **The dispatcher is a constrained coordinator, not a reasoner — it performs structural operations (validation, routing, plan execution, audit) without cognitive capability.** Routing decisions MUST be possible from envelope metadata alone, without understanding message content. (From: the networking-switch concept — a switch reads headers and forwards packets.)

2. **The end-to-end principle applies.** The dispatcher verifies *protocol* correctness (well-formed envelopes, valid routing, schema compliance, timeout enforcement) — structural validation, not semantic interpretation (Section 4). *Content* correctness is the service's responsibility. (From: Saltzer, Reed & Clark 1984.)

3. **Audit is mandatory, not optional.** Every message passing through the dispatcher gets structured audit metadata. This is core protocol behavior, not an extension. (From: the general security principle that implementation-discipline-dependent security fails unpredictably across deployments — see Section 3.2.1's analysis of MCP.)

4. **Provenance grades are first-class.** Every response carries an evidence-strength field. This is the protocol's novel contribution. (From: the Spence signaling theory — quality signals work only when expensive to fake.)

5. **Escalation is a protocol operation, not an error.** Services can return "I cannot handle this at the required provenance grade" as a structured escalation that the dispatcher routes upward. (From: OTP supervision — escalation through the supervision tree is normal operation.)

6. **Typed contracts in a registry.** Services register their capabilities (input/output schemas, cost hints, health endpoints, isolation requirements) in a capability registry. Schema evolution is enforced at the registry. (From: Avro schema registry — centralized version management with compatibility checking.)

7. **Extensibility without breakage.** Unknown metadata fields are preserved and forwarded. New capabilities are added as metadata keys without protocol version bumps. (From: TCP options field, HTTP headers, protobuf unknown-field forwarding.)

8. **Security by default.** Mutual authentication and bearer-token scoping are required at all conformance levels. Message signing is required for Full conformance when producing high-grade provenance (FORMALLY_VERIFIED, HUMAN_ATTESTED) and for all cross-administrative-domain deployments. See Section 15 for the complete signing policy. (From: NSA/CISA findings — security as a protocol guarantee, not an implementation choice.)

<a id="section-3-5"></a>
## Scope

CCDP specifies the message format, routing semantics, registry interface, provenance system, audit requirements, and security baseline for communication between a dispatcher and cognitive services. It does not specify:

- The internal implementation of any service
- The storage backend of the capability registry
- The training or architecture of any language model
- The human interface for supervision or escalation review
- The specific set of capability types (which are registry-managed, not protocol-defined; the protocol defines a set of well-known Capability Types as extension points in Section 8.3; the registry manages the open-ended set of deployment-specific types)

CCDP is transport-layer agnostic in principle but specifies HTTP as the REQUIRED base transport and JSON-RPC 2.0 as the REQUIRED wire format. Future specifications MAY define bindings for other transports.

<a id="section-4"></a>
# Terminology

This section defines terms used throughout this specification. Terms defined here are capitalized when used in their technical sense.

**Artifact Reference.** A URI pointing to a verifiable artifact (proof object, test result, signed attestation) stored outside the CCDP message. Artifact References appear in Evidence entries and Decomposition Plan result references. The URI form, dereference authority, and access-control requirements are deployment-defined. Artifact References SHOULD include an integrity hash for content verification. Artifact References that appear in audit records are subject to the audit retention policy (Section 11.5). Deployments MUST ensure that referenced artifacts remain resolvable for the configured audit retention period.

**Audit Record.** A structured log entry created by the Dispatcher for each message processed. Audit Records are defined in Section 11. Each Audit Record carries an `audit_schema_version` field independent of the CCDP document and wire versions.

**Authenticated Sender.** The identity of the immediate sender of a message, as established by the transport layer (mTLS certificate Common Name, or bearer-token subject claim). The Authenticated Sender is distinct from the Requester (`source_id`), which identifies the original originator across hops. For a Request arriving from the Requester, the Authenticated Sender and the Requester are the same entity. For a forwarded message, the Authenticated Sender is the Dispatcher, while the Requester remains the original originator. Signature verification and authorization checks MUST use the Authenticated Sender identity, not `source_id`, because `source_id` is an unauthenticated claim carried in the message payload.

**Capability.** A typed cognitive function that a Service can perform, identified by a Capability Type and described by a Capability Record in the Registry. Examples: "deduction," "planning," "language-generation," "human-review." A Capability is an interface contract, not an implementation — multiple Services MAY implement the same Capability Type with different backing implementations (Section 5.3).

**Capability Record.** The Registry entry for a Capability, containing: the Capability Type identifier, input and output JSON Schemas, cost hints, health-check endpoint, isolation requirements, supported Provenance Grades, and schema version metadata (Section 8).

**Capability Scope.** The set of capability types a bearer token or identity is authorized to access, expressed as a list of exact capability-type strings or wildcard patterns (Section 15.3.2). Scopes are evaluated during routing authorization.

**Capability Type.** A string identifier for a class of cognitive function, using reverse-domain notation (e.g., `org.ccdp.deduction`, `org.ccdp.planning`). The protocol defines a set of well-known Capability Types (Section 8.3); implementations MAY define additional types through the Registry.

**Conformance Level.** The level of protocol compliance claimed by an implementation: Core (all MUST requirements) or Full (all MUST and SHOULD requirements). See Section 16.4.

**Content.** The payload of a CCDP message — the actual cognitive input or output. Content is opaque to the Dispatcher: the Dispatcher MUST NOT interpret, transform, or make routing decisions based on Content. The Dispatcher MAY perform structural validation of Content against JSON Schemas and MAY resolve typed references within Content wrappers during decomposition plan execution (Section 14). These are structural operations, not semantic interpretation (see Structural Validation vs Semantic Interpretation below). Content structure is governed by the Capability Record's input and output schemas.

**Cost Budget.** The resource constraints on a Request, carried in the `cost_budget` envelope field. Includes optional limits on compute time, token consumption, and monetary cost. Propagated and partitioned through decomposition and escalation.

**Decomposition.** The process of breaking a complex request into a set of typed sub-requests, each routable to a different Service. Decomposition is performed by a Decomposition Service — a Service whose Capability Type is `org.ccdp.decomposition` — and produces a Decomposition Plan (Section 14).

**Decomposition Plan.** A structured description of how a complex request has been decomposed: the set of sub-requests, their dependency ordering, and the composition function that assembles sub-results into the final result (Section 14).

**Dispatcher.** The central routing component of a CCDP system. The Dispatcher receives messages, reads their Envelopes, makes routing decisions based on Envelope metadata and Registry lookups, forwards messages to Services, and manages audit logging, health monitoring, and escalation routing. The Dispatcher is a constrained protocol enforcement and execution coordinator. It performs structural operations — routing, schema validation, decomposition plan execution, typed-reference resolution, structural result assembly, audit logging, health monitoring, and deadline/budget enforcement — but has no cognitive capability. It never reasons about what content means. A conforming Dispatcher MUST NOT reason about message Content (Section 16.1).

**Envelope.** The structured metadata portion of a CCDP message, containing all information the Dispatcher needs for routing, audit, and protocol enforcement. The Envelope includes message type, identity and tracing fields, routing fields, constraint fields, provenance fields, audit fields, and extensible metadata. The Dispatcher reads the Envelope and selected structural Content fields (schema shapes, typed references) to route and process messages (Section 7).

**Escalation.** A structured protocol response indicating that a Service cannot fulfill a request at the required provenance grade or capability level. An Escalation is a first-class message type (not an error), carrying the reason for escalation, the achieved provenance grade (if any), a partial result (if available), and a suggested routing target. The Dispatcher routes Escalations according to the Escalation Chain (Section 13).

**Escalation Chain.** An ordered list of fallback targets for a given Capability Type, defined in the Registry. When a Service returns an Escalation, the Dispatcher routes to the next target in the chain. The chain typically terminates at a human review queue (Section 13.4).

**Evidence.** A structured record within a Provenance field documenting a specific piece of support for a response's epistemic status. Evidence entries carry a type (e.g., "proof-object," "test-result," "human-signature"), a reference to the supporting artifact, and the Service that produced it (Section 10). Evidence entries MUST include a `type` field (string) and a `description` field (string). Evidence entries at grades VALIDATED and above MUST include `artifact_ref` with `integrity` when a supporting artifact exists. For grades OPAQUE through COMPUTED, artifact references with integrity are RECOMMENDED. The `integrity` sub-field contains a hash algorithm and digest (e.g., `"integrity": {"algorithm": "sha256", "digest": "..."}`). The Dispatcher MUST NOT dereference artifact references.

**Health Status.** A Service's self-reported operational state, communicated through Health messages: HEALTHY (fully operational), DEGRADED (partially operational with reduced capability or capacity), or UNHEALTHY (not accepting requests). The Dispatcher maintains a Health Table and uses Health Status for routing decisions (Section 13.6).

**Message.** The atomic unit of CCDP communication. A Message consists of an Envelope and a Content payload, encoded as a JSON-RPC 2.0 request or response. Messages are typed by the `envelope.type` field (Section 7).

**Message Type.** The classification of a CCDP Message by its protocol function. The defined Message Types are: REQUEST, RESPONSE, NOTIFICATION, ESCALATION, HEALTH_REQUEST, HEALTH_RESPONSE, and DECOMPOSITION_RESULT (Section 7.2).

**Priority.** The scheduling priority of a Request: LOW, NORMAL, HIGH, or CRITICAL. Carried in the `priority` envelope field. Used by Services for internal scheduling and by the Dispatcher as a routing tiebreaker.

**Provenance.** Structured metadata on a RESPONSE or ESCALATION message documenting the epistemic status of the result: the Provenance Grade, the Evidence supporting it, the Service that produced it, and the computational resources consumed. Provenance is a REQUIRED field on all responses (Section 10).

**Provenance Grade.** An ordinal classification of the evidence strength behind a cognitive output. The defined grades, from weakest to strongest, are: OPAQUE, ASSERTED, HEURISTIC, COMPUTED, VALIDATED, CROSS_CHECKED, FORMALLY_VERIFIED, and HUMAN_ATTESTED. Grades propagate through composed operations according to defined composition rules (Section 10).

**Received vs Derived.** *Received* Content and Provenance are values supplied by a Service in a Response, an Escalation, or by a Requester in a Request. The Dispatcher MUST NOT mutate received values — it forwards them as-is (modulo Dispatcher-mutable envelope fields listed in Section 15.4.3). *Derived* Content and Provenance are values the Dispatcher constructs during decomposition plan execution: sub-request Content assembled from plan templates and resolved `$ref` references, and composed Provenance computed from sub-result grades using the composition rules in Section 10.5. Creating derived values from a plan specification is a structural operation; the Dispatcher never generates derived content through cognitive reasoning. Where this specification says "MUST NOT modify Content" or "MUST NOT modify Provenance," it means received values. Derived values are created, not modified.

**Registry.** The Capability Registry — a service that stores Capability Records, enforces schema versioning and compatibility, and answers routing queries from the Dispatcher. The Registry is a CCDP infrastructure component, not a cognitive Service. Its interface is defined in Section 8; its implementation is not specified.

**Request.** A CCDP Message of type REQUEST, carrying a cognitive task from a requester (human or Service) to the Dispatcher for routing to an appropriate Service.

**Requester.** The human, application, or Service that originates a CCDP Request. The Requester is identified by the `source_id` envelope field and authenticated via bearer tokens (for external requesters) or mTLS identity (for Service-to-Service sub-requests).

**Response.** A CCDP Message of type RESPONSE, carrying the result of a cognitive task from a Service back through the Dispatcher to the requester. Every Response MUST carry Provenance metadata (Section 10).

**Service.** Any component that implements one or more Capabilities and communicates with the Dispatcher using the CCDP protocol. Services are heterogeneous: they may be LLM endpoints, theorem provers, classical planners, databases, human review queues, composite LLM+service hybrids, or Decomposition Services. From the Dispatcher's perspective, all Services expose the same typed interface — the Dispatcher does not know or care what implementation backs a Service (Section 5.3).

**Service Mode.** The implementation pattern behind a Service. Four modes are recognized (though the Dispatcher is agnostic to mode): Mode 1 (LLM alone), Mode 2 (deterministic service alone), Mode 3 (LLM + deterministic service composite), and Mode 4 (human queue). The same Capability Type MAY be implemented in different modes by different Services (Section 5.3).

**Span.** A single unit of work within a Trace, corresponding to one hop through the Dispatcher (one Service invocation). Spans carry a unique `span_id` and reference their parent via `parent_span_id`, forming a tree of operations within a Trace (Section 11).

**Structural Validation vs Semantic Interpretation.** Structural validation operates on typed metadata, schema-defined field shapes, and reference resolution without understanding what the content means. Semantic interpretation reasons about the meaning, intent, or implications of content. The Dispatcher performs structural validation; semantic interpretation is the exclusive domain of Services. Schema validation, DAG execution, typed-reference substitution, and structural result assembly are structural operations. Natural-language understanding, logical reasoning, and content-meaning-based decisions are semantic interpretation.

**Trace.** The complete audit trail of a top-level request and all operations it spawns, identified by a unique `trace_id`. A Trace spans the lifetime of a request through routing, service invocation, possible decomposition into sub-requests, escalation, and final response. Trace context propagation follows W3C Trace Context [W3C-TC] (Section 11).

**Trace Context.** The W3C Trace Context fields (`traceparent` and `tracestate`) propagated through CCDP messages to enable distributed tracing across the system. CCDP maps these to Envelope fields (Section 11.3).

<a id="section-5"></a>
# Architecture Overview

<a id="section-5-1"></a>
## Topology

A CCDP system has a star topology with the Dispatcher at the center. All communication between Services passes through the Dispatcher. Services do not communicate directly with each other.

```
                    ┌──────────────┐
                    │    Human     │
                    │  Supervisor  │
                    └──────┬───────┘
                           │ (escalation, oversight)
                           │
          ┌────────────────┼─────────────────┐
          │           DISPATCHER             │
          │  ┌───────────┐ ┌──────────────┐  │
          │  │ Structural│ │   Registry   │  │
          │  │Coordinator│ │   Client     │  │
          │  └───────────┘ └──────────────┘  │
          │  ┌──────────┐ ┌───────────────┐  │
          │  │  Router  │ │ Audit Logger  │  │
          │  └──────────┘ └───────────────┘  │
          │  ┌──────────┐ ┌───────────────┐  │
          │  │  Health  │ │    Security   │  │
          │  │ Monitor  │ │   Enforcer    │  │
          │  └──────────┘ └───────────────┘  │
          └─────┬───┬───┬───┬───┬───┬───┬────┘
                │   │   │   │   │   │   │
                ▼   ▼   ▼   ▼   ▼   ▼   ▼
               ┌─┐ ┌─┐ ┌─┐ ┌─┐ ┌─┐ ┌─┐ ┌─┐
               │S│ │S│ │S│ │S│ │S│ │S│ │S│
               │1│ │2│ │3│ │4│ │5│ │6│ │7│
               └─┘ └─┘ └─┘ └─┘ └─┘ └─┘ └─┘
           LLM  Z3  Plan Human Decomp Verif  DB
```

This topology is a deliberate design choice, not a scaling constraint. The Dispatcher is the single point of protocol enforcement — authentication, routing, audit logging, health monitoring, and deadline enforcement all happen at the Dispatcher. A Service that bypasses the Dispatcher bypasses all of these guarantees.

The star topology avoids the O(N²) communication explosion that full-mesh agent architectures face [arXiv:2509.02317]. With N services, CCDP requires N links (Dispatcher ↔ Service), not N(N-1)/2. The cost is that the Dispatcher is a single point of failure; high-availability deployment is an infrastructure concern outside this specification's scope, but the protocol's self-contained message design simplifies Dispatcher replication, though production deployments must address shared state for replay caches, circuit-breaker state, health tables, and audit-store consistency (see Section 15.5 and Section 13.6).

<a id="section-5-2"></a>
## Component Roles

A CCDP system comprises four kinds of components. Each has a defined role and a defined boundary of responsibility.

<a id="section-5-2-1"></a>
### The Dispatcher

The Dispatcher is the protocol's routing and enforcement engine. It is a constrained protocol enforcement and execution coordinator — not a reasoner. Its duties include structural operations that go beyond simple routing, but it has no cognitive capability and never reasons about message content. Its responsibilities are:

- **Envelope parsing**: Read the Envelope of every incoming Message. Reject malformed Envelopes.
- **Authentication**: Verify the identity of the sender (Section 15). Reject unauthenticated messages.
- **Routing**: Select a target Service based on the Envelope's `capability_type` and the Registry's Capability Records (Section 9). The routing decision is logged.
- **Schema validation**: Verify that the Request's Content conforms to the target Service's input schema and that the Response's Content conforms to the declared output schema (Section 8).
- **Deadline enforcement**: Propagate deadline constraints and enforce timeouts (Section 12.4).
- **Audit logging**: Write a structured audit record for every Message that passes through (Section 11).
- **Health monitoring**: Track Service health via periodic Health messages and route around unhealthy Services (Section 13.6).
- **Escalation routing**: When a Service returns an Escalation, route to the next target in the Escalation Chain (Section 13.4).
- **Provenance passthrough**: Forward received Provenance metadata from Responses without modification. The Dispatcher MUST NOT alter received Provenance grades. (Composed Provenance the Dispatcher derives during decomposition result assembly is a different case — see the Received vs Derived definition in Section 4.)
- **Metadata preservation**: Forward all unknown metadata fields without modification (Section 7.7).

The Dispatcher MUST NOT — this is the semantic-interpretation side of the Structural Validation vs Semantic Interpretation boundary (Section 4):

- Interpret, parse, or make decisions based on the Content of any Message
- Mutate received Content — Content supplied by a Requester or Service in a Request, Response, or Escalation. During decomposition plan execution, the Dispatcher creates derived Content for sub-requests by assembling plan templates and resolving typed references (Section 14.3.3). This is structural construction from a plan specification, not modification of existing content. See the Received vs Derived definition in Section 4.
- Generate cognitive output of any kind
- Modify received Provenance grades or Evidence entries
- Cache or reuse Response Content across different Requests (unless the Service's Capability Record explicitly permits it via a `cacheable` flag)

<a id="section-5-2-2"></a>
### Services

A Service implements one or more Capabilities and communicates with the Dispatcher using CCDP messages. A Service's responsibilities are:

- **Contract compliance**: Accept only Requests that conform to its declared input schema. Produce Responses that conform to its declared output schema.
- **Provenance reporting**: Attach accurate Provenance metadata to every Response, including the Provenance Grade, Evidence entries, and computational resource consumption (Section 10).
- **Escalation**: When a Request exceeds the Service's capability or provenance-grade threshold, return a structured Escalation rather than producing low-provenance output silently (Section 13).
- **Health reporting**: Respond to Health requests with accurate Health Status (Section 13.6).
- **Deadline compliance**: Respect the `deadline` field. If the Service cannot complete within the remaining deadline budget, it SHOULD return an Escalation with reason `DEADLINE_INSUFFICIENT` rather than starting work it cannot finish.
- **Idempotency**: For the same `request_id`, a Service MUST return the same Response. This makes retry safe (Section 7.3).

**Idempotency scope.** The idempotency requirement is scoped by service type. Mode 2 (deterministic) Services MUST return byte-identical responses for the same `request_id`. Mode 1 (LLM) and Mode 3 (composite) Services MUST return semantically equivalent responses — the same conclusion at the same or higher provenance grade — but MAY differ in surface form (wording, formatting). For protocol conformance purposes, idempotency is tested by requiring Services to cache and return the original Response for duplicate `request_id` values within the idempotency window. Semantic equivalence is a service-quality property, not a protocol-testable conformance requirement. Mode 4 (human queue) Services MUST return the same response if the human has already submitted a result for the `request_id`; if the human has not yet responded, a retry with the same `request_id` is a no-op (the request remains in the queue). Implementations SHOULD maintain a response cache keyed by `request_id` with a configurable TTL (RECOMMENDED: 24 hours).

A Service MAY:

- Invoke other Services by sending Requests through the Dispatcher (sub-requests carry the same `trace_id` and a new `span_id`)
- Maintain internal state across requests (but MUST NOT depend on the Dispatcher maintaining state)
- Implement multiple Capability Types behind a single endpoint

<a id="section-5-2-3"></a>
### The Registry

The Capability Registry stores Capability Records and answers queries from the Dispatcher. Its responsibilities are:

- **Capability storage**: Maintain the current Capability Record for every registered Service, including schemas, cost hints, health endpoints, and isolation requirements.
- **Schema versioning**: Track schema versions for each Capability Type and enforce compatibility rules at registration time (Section 8.5).
- **Routing queries**: Answer Dispatcher queries of the form "which Services implement Capability Type X?" with a list of matching Services, their endpoints, cost hints, and health status.
- **Health aggregation**: Optionally aggregate Health Status from Services and include it in routing query responses.

The Registry interface is defined in Section 8. The storage backend is not specified — implementations MAY use a database, a configuration file, a distributed key-value store, or any other mechanism that satisfies the interface contract.

<a id="section-5-2-4"></a>
### The Human Supervisor

The Human Supervisor occupies the top of the supervision tree. The Human Supervisor is not a CCDP component in the protocol sense — the protocol does not specify the human interface — but the protocol is designed to support human supervision:

- Escalation Chains terminate at a human review queue (a Service of Mode 4 — Section 5.3).
- Audit Trails provide the Human Supervisor with complete visibility into every routing decision, service invocation, and provenance grade (Section 11).
- The Dispatcher MAY be configured to require Human Supervisor approval for routing decisions above a cost threshold or below a provenance-grade threshold.
- The Provenance system's HUMAN_ATTESTED grade is the highest epistemic grade, reflecting the irreducible role of human judgment in specification and value assessment.

<a id="section-5-3"></a>
## Service Modes

A Service's implementation is opaque to the Dispatcher — the Dispatcher routes to a typed interface, not to an implementation. However, this specification recognizes four implementation patterns (Service Modes) because they produce structurally different Provenance characteristics:

<a id="section-5-3-1"></a>
### Mode 1: LLM Alone

The Service is an LLM endpoint. Requests are natural-language prompts (or structured prompts); responses are natural-language completions. Typical Provenance Grade: ASSERTED or HEURISTIC.

Mode 1 is appropriate for language-native tasks: drafting, brainstorming, translation, summarization, natural-language understanding. The LLM's native strength is the crystallize → serialize → deserialize → instantiate translation loop — getting concepts between representations.

Mode 1 is not appropriate for tasks requiring deductive correctness, sound planning, or verifiable selection — the forward-pass ceiling (TC⁰) and self-correction limits make these structurally unreliable without external verification.

<a id="section-5-3-2"></a>
### Mode 2: Deterministic Service Alone

The Service is a theorem prover, SMT solver, classical planner, database, calculator, or other deterministic engine. Requests are formal inputs (logical formulas, PDDL domains, SQL queries); responses are verified outputs. Typical Provenance Grade: COMPUTED or FORMALLY_VERIFIED.

Mode 2 is appropriate for tasks with formal specifications: proof checking, plan validation, constraint solving, data retrieval. The output is correct by construction given correct input — the remaining failure mode is input correctness, not computation correctness.

<a id="section-5-3-3"></a>
### Mode 3: LLM + Deterministic Service Composite

The most architecturally significant mode. An LLM sits in front of a deterministic service as a translator: it converts a natural-language request into the service's formal input language, passes it through, and converts the formal output back to natural language. From the Dispatcher's perspective, this is a single Service with a single typed interface — the internal LLM translation layer is not visible in the protocol.

This is the "LLM proposes, engine disposes" pattern [PAL; Logic-LM; SatLM; LLM-Modulo]. The Provenance Grade of the output depends on how much of the result rests on the deterministic engine versus the LLM translation: if the LLM's contribution is limited to translation and the engine verifies the result, the grade may be VALIDATED or FORMALLY_VERIFIED with an Evidence entry documenting the verification. If the translation itself is uncertain, the Provenance should reflect that uncertainty.

Mode 3 is the primary path for expanding the system's capabilities: tasks that cannot be handled by Mode 2 alone (because they require natural-language understanding at the input boundary) and cannot be trusted to Mode 1 alone (because they require correctness guarantees at the output boundary).

<a id="section-5-3-4"></a>
### Mode 4: Human Queue

The Service is a human review queue. Requests are placed in a queue for human processing; responses arrive when a human completes the task and submits a result in the typed format. From the Dispatcher's perspective, the interface is identical — same envelope, same content schema, same provenance — just slower and more expensive.

Typical Provenance Grade: HUMAN_ATTESTED (the highest grade).

Mode 4 is appropriate for tasks requiring irreducible human judgment: specification review, value/novelty assessment, broad abstraction, and any task for which no external organ produces reliable output. Mode 4 is also the default Escalation target: when automated Services cannot meet the requested provenance grade, the Escalation Chain terminates at a human queue.

<a id="section-5-3-5"></a>
### Mode Substitution and Progressive Automation

The four modes share a critical property: **modes are interchangeable without changing the Dispatcher's routing logic.** A Capability Type that starts as Mode 4 (human does everything behind a typed interface) can be progressively replaced with Mode 3 (LLM + deterministic service) and then Mode 2 (deterministic service alone) as tooling matures — without changing the Dispatcher, the Registry schemas, or any other Service's integration.

This is the architectural basis for incremental automation: start with everything in Mode 4 and the Dispatcher is trivially simple (a message router to human queues). Then, one Service at a time, substitute in a more automated implementation. The Dispatcher never gets smarter; the Services behind it get more capable.

Mode substitution has multiple protocol-visible effects: Provenance Grade, cost (different modes have different cost profiles), latency, evidence entries (different methods produce different evidence), signing (some modes may not support signing), and isolation properties. For example, a Mode 2 replacement will report FORMALLY_VERIFIED where the Mode 4 predecessor reported HUMAN_ATTESTED. Consumers of the output can use the Provenance Grade to calibrate their trust — the protocol ensures the change in backing implementation is transparent through the epistemic metadata. Mode substitution is transparent only when the consumer's `provenance_requirement.min_grade` is met by the replacement mode's typical grade. A consumer requiring `HUMAN_ATTESTED` cannot be served by a Mode 2 replacement reporting `FORMALLY_VERIFIED` unless the consumer's policy accepts formal verification as equivalent for that claim type. Deployments SHOULD configure mode-substitution policies per capability type that account for all these effects, not just provenance.

<a id="section-5-4"></a>
## The Decomposition Service

Decomposition — breaking a complex request into typed sub-requests — is itself a cognitive act. Rather than requiring the Dispatcher to perform decomposition (which would violate the constrained-coordinator principle) or requiring the human to pre-decompose all requests (which does not scale), CCDP treats decomposition as a first-class Service with Capability Type `org.ccdp.decomposition`.

The Decomposition Service receives a complex Request and returns a Decomposition Plan: a set of typed sub-requests, their dependency ordering (which sub-requests can run in parallel, which must be sequential), and a composition function specifying how sub-results are assembled into the final result.

The Dispatcher then routes each sub-request independently through the normal routing process. Sub-requests carry the same `trace_id` as the parent and new `span_id` values, linking them in the audit trail. Results are composed according to the Decomposition Plan's composition specification.

Result composition is a structural operation: the Dispatcher assembles typed sub-results according to the plan's composition specification (template assembly, concatenation, or selection) without reasoning about what the sub-results mean. When composition requires cognitive judgment (e.g., synthesizing sub-results into a coherent narrative), the plan routes composition to a dedicated Composition Service with capability type `org.ccdp.composition` (Section 14.3.4).

Because the Decomposition Service is behind the same typed interface as every other Service, it is subject to the same audit, provenance, health-check, and escalation discipline. A Decomposition Plan carries its own Provenance Grade (reflecting the evidence strength behind the decomposition itself), and if the Decomposition Service cannot decompose a request, it returns an Escalation rather than producing a bad decomposition silently.

The Decomposition Service is a natural Mode 3 candidate: an LLM translates a natural-language request into a structured decomposition plan, which a validator then checks for consistency (all sub-requests have valid Capability Types, dependencies are acyclic, the composition function references all sub-results). The validated decomposition carries a higher Provenance Grade than the raw LLM decomposition.

Decomposition is detailed in Section 14.

<a id="section-5-5"></a>
## Relationship to Supervision Trees

CCDP's architecture maps to the classic supervision-tree model:

- **The Human Supervisor is the top supervisor.** Holds the specification and value/novelty judgment — the irreducible inputs. Owns the restart policy: what counts as a known-good state.
- **The Dispatcher is the intermediate supervisor.** Routes messages to worker processes, monitors health, restarts (reroutes around) failed workers, and escalates to the top supervisor when no worker can handle the request.
- **Services are worker processes.** Each supervised, each with a typed protocol on its wire. They crash loudly (return structured errors or Escalations) rather than silently emitting corrupt output.
- **"Let it crash" is the failure discipline.** A Service that fails — an unsound plan, a vacuous proof, a mistranslation — crashes loudly and its failure is named, logged, and routed to the Escalation Chain. The output is not forwarded. This is the direct antidote to silent failures.
- **Typed protocols on the wires.** Every link between Dispatcher and Service is a typed contract enforced by the Registry. Malformed messages are rejected at the boundary. This is the supervision tree's process isolation principle expressed as protocol enforcement.

The key property inherited from OTP: you build reliable systems from unreliable components not by making the components correct, but by strong isolation, message-passing-only interaction, supervision, and restart from a known-good state [Armstrong 2003].

<a id="section-6"></a>
# Protocol Layers

<a id="section-6-1"></a>
## Layering Rationale

CCDP follows the TCP/IP tradition of layered protocol design: each layer provides a specific abstraction, relies only on the layer below, and can evolve independently. The layering is deliberate — it separates transport concerns (how bytes move) from routing concerns (where messages go) from epistemic concerns (how much to trust the result).

Unlike TCP/IP, where the application layer is unspecified by the transport, CCDP's upper layers carry load-bearing protocol semantics. Provenance grades, audit metadata, and escalation semantics are not application concerns delegated to the endpoints — they are protocol-layer features enforced at the Dispatcher. This is the sense in which "the protocol is smart": the layers above transport carry intelligence that a Dispatcher with no cognitive capability of its own can enforce mechanically.

<a id="section-6-2"></a>
## Layer Architecture

CCDP defines four layers, mapped to their TCP/IP analogs:

```
┌──────────────────────────────────────────────────────┐
│  Layer 4: Content Layer                              │
│  (opaque payload — analogous to Application Layer)   │
│  • Service-specific input/output                     │
│  • Schema-governed by Capability Records             │
│  • Opaque to Dispatcher                              │
├──────────────────────────────────────────────────────┤
│  Layer 3: Epistemic Layer                            │
│  (CCDP's novel contribution — no TCP/IP analog)      │
│  • Provenance grades and evidence                    │
│  • Escalation semantics                              │
│  • Decomposition plans                               │
│  • Cost and resource signals                         │
├──────────────────────────────────────────────────────┤
│  Layer 2: Routing and Audit Layer                    │
│  (analogous to Internet/Network Layer)               │
│  • Capability-type-based routing                     │
│  • Registry lookups                                  │
│  • Trace/span identification                         │
│  • Mandatory audit metadata                          │
│  • Deadline propagation                              │
│  • Health monitoring                                 │
├──────────────────────────────────────────────────────┤
│  Layer 1: Transport Layer                            │
│  (analogous to Transport + Link Layers)              │
│  • HTTP (REQUIRED)                                   │
│  • JSON-RPC 2.0 wire format                          │
│  • TLS for encryption                                │
│  • Authentication (mTLS or token-based)              │
└──────────────────────────────────────────────────────┘
```

<a id="section-6-2-1"></a>
### Layer 1: Transport

The Transport Layer provides reliable, encrypted, authenticated byte delivery between the Dispatcher and Services.

**HTTP is REQUIRED** as the base transport protocol. CCDP messages are HTTP POST requests to defined endpoints. HTTP was chosen for ubiquity: it works with all Service types (LLM endpoints, web services, queue systems), is supported by all programming languages, and composes with existing infrastructure (load balancers, proxies, monitoring).

**JSON-RPC 2.0 is REQUIRED** as the wire format. Every CCDP message is a JSON-RPC 2.0 request or response, with CCDP-specific method names and parameter structures. JSON-RPC was chosen for simplicity: its specification fits on one page, it is transport-agnostic, and it imposes minimal parsing overhead on a Dispatcher with no cognitive capability of its own. Both MCP and A2A chose JSON-RPC 2.0 for the same reasons.

**TLS 1.3 (or later) is REQUIRED** for all Dispatcher-to-Service communication. Plaintext HTTP MUST NOT be used in production deployments. Self-signed certificates MAY be used in development environments.

**Authentication** is performed at this layer. The REQUIRED mechanism is mutual TLS (mTLS) for Dispatcher-to-Service authentication. Bearer tokens with scoped permissions MAY be used as an additional authorization mechanism (Section 15). Bearer-token validation is logically an application-level concern (it checks CCDP-scoped authorization, not transport-level connectivity). It is placed in the Transport Layer for implementation convenience: tokens are typically carried in HTTP headers and checked before message parsing begins. This is a pragmatic layer crossing, not a design error.

Implementations MAY support additional transports (e.g., QUIC for latency-critical paths, WebSocket for long-lived connections) as protocol extensions, provided they satisfy the same reliability, encryption, and authentication guarantees. The Transport Layer is the most substitutable layer in the stack.

<a id="section-6-2-2"></a>
### Layer 2: Routing and Audit

The Routing and Audit Layer provides addressing, routing, tracing, and mandatory audit. This is the layer the Dispatcher primarily operates on — it reads Layer 2 fields to make routing decisions and writes Layer 2 fields for audit.

**Routing fields** identify the message's source, destination, and purpose:
- `capability_type`: what cognitive function is requested
- `source_id`: who sent this message
- `destination_id`: who should receive it (may be empty for the Dispatcher to fill)
- `request_id`: unique identifier for this request (for idempotency and correlation)
- `trace_id`: identifier for the entire request chain (for distributed tracing)
- `span_id`: identifier for this specific hop
- `parent_span_id`: identifier of the parent hop (for decomposed sub-requests)

**Audit fields** are populated by the Dispatcher on every message:
- `received_at`: when the Dispatcher received the message
- `routed_at`: when the Dispatcher forwarded the message
- `routing_decision`: why this Service was selected
- `dispatcher_id`: which Dispatcher instance handled this message

**Deadline fields** enforce time budgets:
- `deadline`: absolute timestamp by which the response must arrive
- `remaining_budget_ms`: remaining time budget (computed by subtracting elapsed time at each hop)

**Health fields** carry Service health information for routing decisions.

Layer 2 carries protocol-enforcement fields. The required set varies by message type — see the per-message required-field matrix in Section 7.3. Fields such as `capability_type` and `destination_id` are required on REQUEST messages but absent or optional on RESPONSE, HEALTH, and NOTIFICATION messages. The Dispatcher reads Layer 2 fields for routing and protocol enforcement. It also reads selected Layer 3 fields (provenance requirements, cost budgets, deadlines) for routing policy and reads Layer 4 Content structurally for schema validation and typed-reference resolution. These cross-layer reads are enumerated in Section 6.5. The Dispatcher MUST NOT perform semantic interpretation of any layer's content.

<a id="section-6-2-3"></a>
### Layer 3: Epistemic

The Epistemic Layer carries the information that makes CCDP different from a generic RPC protocol. It has no TCP/IP analog — this is CCDP's novel contribution.

**Provenance fields** carry the epistemic status of a response:
- `grade`: the Provenance Grade (OPAQUE through HUMAN_ATTESTED)
- `evidence`: structured Evidence entries documenting the basis for the grade
- `scope`: what claim the grade applies to (for FORMALLY_VERIFIED: the specification)
- `composition_trace`: how this grade was derived from component grades (for composed results)

**Escalation fields** carry structured escalation information:
- `reason`: why the Service is escalating (typed: PROVENANCE_BELOW_REQUIREMENT, CAPABILITY_EXCEEDED, DEADLINE_INSUFFICIENT, etc.)
- `achieved_grade`: the Provenance Grade the Service could achieve (if lower than requested)
- `partial_result`: any partial output produced before escalation
- `suggested_target`: where the Dispatcher should route next

**Decomposition fields** carry decomposition plan structure:
- `sub_requests`: the set of typed sub-requests
- `dependencies`: the dependency graph between sub-requests
- `composition`: how sub-results are assembled

**Cost and resource fields** carry resource consumption and budget information:
- `cost_budget`: the requester's resource constraints
- `cost_consumed`: the actual resources consumed by the Service
- `capacity`: the Service's current available capacity

The Dispatcher reads selected Layer 3 fields for routing and enforcement purposes: `provenance_requirement.min_grade` for candidate filtering, `cost_budget` for cost-aware routing, and `deadline`/`remaining_budget_ms` for deadline enforcement. This is structural use of typed metadata, not semantic interpretation of content. It MAY enforce structural rules (e.g., reject a Response missing the `provenance` field) but MUST NOT interpret their content (e.g., the Dispatcher does not evaluate whether a Provenance Grade is accurate — that is the Service's responsibility, subject to audit).

<a id="section-6-2-4"></a>
### Layer 4: Content

The Content Layer carries the actual cognitive input and output — the problem to be solved, the proof to be checked, the text to be drafted, the plan to be validated. Content is entirely opaque to the Dispatcher.

Content structure is governed by the Capability Record's input and output JSON Schemas, stored in the Registry. The Dispatcher MAY validate Content against these schemas (structural schema validation is a Layer 2 enforcement function), but MUST NOT interpret the Content's meaning — the Structural Validation vs Semantic Interpretation distinction (Section 4) is what separates the two.

Content is typed by the `content.type` field, which indicates the format of the payload: `natural-language`, `formal-logic`, `proof-object`, `validated-plan`, `structured-data`, or a custom type defined in the Capability Record.

<a id="section-6-3"></a>
## Layer Independence

Each layer can evolve independently:

- **Transport substitution**: Replace HTTP with QUIC or WebSocket without changing routing, provenance, or content semantics. The only constraint is that the new transport must provide reliable, encrypted, authenticated byte delivery. Non-HTTP transports MUST provide equivalent mechanisms for message signing (Section 15.4), bearer-token authentication (Section 15.2), trace-context propagation (Section 11.3), and status/error signaling (Section 13.2). A transport-binding specification for non-HTTP transports is out of scope for this document but is needed before non-HTTP deployments can claim conformance.
- **Routing evolution**: Add new routing strategies (content-hash routing, geographic routing) without changing transport or epistemic semantics. New routing fields are added as metadata extensions.
- **Epistemic evolution**: Add new Evidence types or new composition rules without changing transport or routing. Adding new Provenance Grades is a protocol extension that requires a document version increment. New grades affect the ordering used for routing, conformance checking, and policy evaluation. The grade set is versioned through the Registry; deployments MUST ensure that all components recognize the grade vocabulary before grades are used in production. New epistemic fields are added as metadata extensions. Existing implementations that do not understand the new fields MUST preserve and forward them (Section 7.7).
- **Content evolution**: Service-specific schemas evolve through the Registry's schema versioning mechanism (Section 8.5) without affecting any lower layer.

This independence is a direct application of the end-to-end principle: each layer does only what it must, and correctness guarantees that belong to a higher layer are not duplicated at a lower layer. The Dispatcher enforces protocol correctness (Layer 2); Services enforce content correctness (Layer 4); the Epistemic Layer (Layer 3) carries the metadata that connects them.

<a id="section-6-4"></a>
## Comparison to the Emerging Agent Protocol Stack

Several sources describe a layered agent protocol stack forming: MCP for tool integration, A2A for agent coordination, WebMCP for browser interaction. CCDP's layering differs in three respects:

**The Epistemic Layer has no counterpart.** The emerging stack has no protocol-level concept of provenance, evidence strength, or epistemic status. This is the gap CCDP fills — the recognition that cognitive outputs are claims with pedigree, not data with types.

**The Dispatcher is a protocol enforcer, not a capable agent.** In the emerging stack, the "client" or "orchestrator" is assumed to be an intelligent agent. CCDP's Dispatcher is closer to a policy-enforcing message coordinator: it reads headers and structural metadata, applies routing policies, executes decomposition plans, validates schemas, and forwards processed messages — all without cognitive capability. The protocol carries the intelligence; the Dispatcher enforces it.

**Audit is a layer concern, not an extension.** In the emerging stack, observability comes from bolting on OpenTelemetry or similar frameworks. In CCDP, audit fields are mandatory Layer 2 elements — the Dispatcher writes them as part of its core function, not as an opt-in integration.

<a id="section-6-5"></a>
## Structural Operations Across Layers

The Dispatcher's structural operations cross layer boundaries by design. Schema validation reads Layer 4 (Content) structure against Layer 2 (Capability Record) definitions. Decomposition plan execution resolves typed references in Layer 4 Content using Layer 2 sub-request identifiers. Budget and deadline propagation reads Layer 3 constraints and writes updated values on forwarded messages. These crossings are explicitly allowed: the Dispatcher operates on typed metadata and structural shapes, not on semantic meaning — the Structural Validation vs Semantic Interpretation distinction (Section 4). Section 16 lists these as conformance requirements rather than layer violations.

<a id="section-7"></a>
# Message Format

<a id="section-7-1"></a>
## Wire Encoding

Every CCDP message is encoded as a JSON-RPC 2.0 [JSON-RPC] request or response, transported over HTTP POST. The JSON-RPC `method` field identifies the CCDP message type; the `params` field carries the CCDP Envelope and Content.

A CCDP Request encoded as JSON-RPC 2.0:

```json
{
  "jsonrpc": "2.0",
  "method": "ccdp/request",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "params": {
    "envelope": { /* ... Layer 2 and 3 fields ... */ },
    "content": { /* ... Layer 4 payload ... */ }
  }
}
```

A CCDP Response encoded as JSON-RPC 2.0:

```json
{
  "jsonrpc": "2.0",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "result": {
    "envelope": { /* ... Layer 2 and 3 fields ... */ },
    "content": { /* ... Layer 4 payload ... */ }
  }
}
```

The JSON-RPC `id` field MUST match the CCDP `envelope.request_id`. This enables correlation at both the JSON-RPC layer and the CCDP layer.

<a id="section-7-2"></a>
## Message Types

The following CCDP message types are defined:

| Identifier | Type | Direction | JSON-RPC Encoding |
|---|---|---|---|
| `ccdp/request` | REQUEST | Requester → Dispatcher → Service | JSON-RPC request (`method`, `id`, `params`) |
| `ccdp/escalation` | ESCALATION | Service → Dispatcher → Escalation target | JSON-RPC request (`method`, `id`, `params`) |
| `ccdp/health.request` | HEALTH_REQUEST | Dispatcher → Service | JSON-RPC request (`method`, `id`, `params`) |
| `ccdp/decomposition.result` | DECOMPOSITION_RESULT | Decomposition Service → Dispatcher | JSON-RPC request (`method`, `id`, `params`) |
| `ccdp/notification` | NOTIFICATION | Any → Dispatcher → Any | JSON-RPC notification (`method`, `params`, no `id`) |
| *(n/a)* | RESPONSE | Service → Dispatcher → Requester | JSON-RPC response (`id`, `result`) |
| *(n/a)* | HEALTH_RESPONSE | Service → Dispatcher | JSON-RPC response (`id`, `result`) |

REQUEST, ESCALATION, HEALTH_REQUEST, and DECOMPOSITION_RESULT are encoded as JSON-RPC requests — they carry a `method` field, an `id`, and `params`. NOTIFICATION is encoded as a JSON-RPC notification — it carries a `method` and `params` but no `id`, and no response is expected. RESPONSE and HEALTH_RESPONSE are encoded as JSON-RPC responses — they carry an `id` correlating to a prior request and a `result` object containing the CCDP envelope and content. JSON-RPC responses do not carry a `method` field; the CCDP message type is identified by the `envelope.type` field within the `result` object.

<a id="section-7-3"></a>
## Envelope Structure

The Envelope is the structured metadata portion of every CCDP message. The Dispatcher reads only the Envelope; Content is opaque.

<a id="section-7-3-1"></a>
### Common Envelope Fields (All Message Types)

The following fields are REQUIRED on every CCDP message envelope:

```json
{
  "envelope": {
    "ccdp_version": "1.0",
    "type": "REQUEST",
    "request_id": "550e8400-e29b-41d4-a716-446655440000",
    "trace_id": "4bf92f3577b34da6a3ce929d0e0e4736",
    "span_id": "00f067aa0ba902b7",
    "timestamp": "2026-08-03T14:30:00.000Z",
    "source_id": "client-app-01",
    "metadata": {}
  }
}
```

**`ccdp_version`** (string, REQUIRED): The CCDP protocol version. MUST be `"1.0"` for this specification. Implementations MUST reject messages with an unrecognized version. The wire protocol version is independent of the document version (Section 2.1). This specification document is version 0.2.0; the wire protocol version remains `"1.0"` because the on-the-wire message format has not changed.

**`type`** (string, REQUIRED): The message type. One of: `"REQUEST"`, `"RESPONSE"`, `"NOTIFICATION"`, `"ESCALATION"`, `"HEALTH_REQUEST"`, `"HEALTH_RESPONSE"`, `"DECOMPOSITION_RESULT"`. For method-bearing messages (REQUEST, ESCALATION, HEALTH_REQUEST, DECOMPOSITION_RESULT, NOTIFICATION), the `envelope.type` value MUST correspond to the JSON-RPC `method` field. For response messages (RESPONSE, HEALTH_RESPONSE), the `envelope.type` is carried inside the `result` object and is the sole identifier of the CCDP message type — JSON-RPC responses have no `method` field.

**`request_id`** (string, REQUIRED): A UUID v4 uniquely identifying this request. Used for idempotency, correlation, and replay protection. A Service that receives a Request with a `request_id` it has already processed MUST return the cached Response without re-executing the request. For NOTIFICATION messages (JSON-RPC notifications), the `request_id` field carries the identifier of the related request (e.g., the request whose progress is being reported) or a unique identifier for the notification itself. Since JSON-RPC notifications do not carry an `id` field, the JSON-RPC `id`-must-match-`request_id` rule does not apply to notifications.

**`trace_id`** (string, REQUIRED): A 32-character lowercase hexadecimal string identifying the entire request chain, compatible with W3C Trace Context `trace-id`. All messages spawned from the same top-level request — including decomposed sub-requests, escalations, and health checks triggered by the request — share the same `trace_id`.

**`span_id`** (string, REQUIRED): A 16-character lowercase hexadecimal string identifying this specific operation within the trace, compatible with W3C Trace Context `parent-id`. Each hop through the Dispatcher generates a new `span_id`. The originator of a top-level Request generates the initial `span_id`. For each subsequent hop — forwarding to a Service, dispatching a sub-request, or routing an escalation — the Dispatcher generates a new `span_id` and sets `parent_span_id` to the previous hop's `span_id`. Services MUST NOT generate new `span_id` values for their Response; the Response carries the same `span_id` as the Request it answers.

**`timestamp`** (string, REQUIRED): ISO 8601 timestamp with UTC timezone (`Z`). The time the message was created by its originator.

**`source_id`** (string, REQUIRED): The identifier of the component that originated this message. For Requests from external clients, this is the client identifier. For Responses, this is the Service identifier. For forwarded messages, this is the originator, not the Dispatcher. When the Dispatcher forwards a message, it does not overwrite `source_id`. The Dispatcher's identity is recorded in the `audit.dispatcher_id` field (Section 7.5), not in `source_id`. This means `source_id` always identifies the originator, and `audit.dispatcher_id` identifies the intermediary. If future extensions require explicit sender/forwarder identification, they SHOULD use metadata keys (e.g., `org.ccdp.forwarder_id`) rather than overloading `source_id`. For signature verification and authorization, implementations MUST use the Authenticated Sender identity established by the transport layer (Section 4, Section 15.2), not the `source_id` payload field. The `source_id` field is an unauthenticated originator claim; the Authenticated Sender is cryptographically verified.

**`metadata`** (object, REQUIRED but MAY be empty): Extensible key-value metadata. Unknown keys MUST be preserved and forwarded by all intermediaries, including the Dispatcher. Keys use reverse-domain notation for namespacing (e.g., `"com.example.custom_field": "value"`). Keys in the `org.ccdp.*` namespace are reserved for protocol-defined extensions.

<a id="section-7-3-2"></a>
### REQUEST Envelope Fields

In addition to Common fields, REQUEST envelopes carry:

```json
{
  "envelope": {
    // ... common fields ...
    "type": "REQUEST",
    "capability_type": "org.ccdp.deduction",
    "destination_id": null,
    "parent_span_id": null,
    "deadline": "2026-08-03T14:31:00.000Z",
    "remaining_budget_ms": 60000,
    "cost_budget": {
      "max_compute_seconds": 120,
      "max_tokens": 50000,
      "max_monetary_cost": "0.50",
      "monetary_unit": "USD"
    },
    "provenance_requirement": {
      "min_grade": "VALIDATED"
    },
    "priority": "NORMAL",
    "idempotency_key": null
  }
}
```

**`capability_type`** (string, REQUIRED): The Capability Type being requested, using reverse-domain notation. The Dispatcher uses this field, together with the Registry, to select the target Service. Well-known types are listed in Section 8.3.

**`destination_id`** (string or null, OPTIONAL): The specific Service to route to. If null, the Dispatcher selects a Service based on `capability_type` and routing rules (Section 9). If specified, the Dispatcher MUST route to that Service if it is healthy and registered for the given `capability_type`; otherwise the Dispatcher MUST return an error.

**`parent_span_id`** (string or null, OPTIONAL): For sub-requests spawned by a Decomposition Plan, the `span_id` of the parent request. Null for top-level requests. Used for constructing the span tree in the audit trail.

**`deadline`** (string, REQUIRED): ISO 8601 timestamp. The absolute time by which the Response MUST arrive at the original requester. The Dispatcher MUST NOT forward a Request to a Service if the remaining time before `deadline` is insufficient for the Service's advertised latency (from its Capability Record).

**`remaining_budget_ms`** (integer, REQUIRED): Remaining time budget in milliseconds. At each hop, the Dispatcher subtracts elapsed time and sets this field to the updated value. Services SHOULD use `remaining_budget_ms` rather than computing from `deadline` to avoid clock-skew issues.

**`cost_budget`** (object, OPTIONAL): Resource constraints on the request. All sub-fields are optional; omitted fields indicate no constraint. `max_compute_seconds` caps wall-clock compute time. `max_tokens` caps token consumption (for LLM services). `max_monetary_cost` caps monetary cost. `monetary_unit` is the ISO 4217 currency code. The Dispatcher MAY use cost_budget for routing decisions (prefer cheaper services). Services MUST NOT exceed the cost_budget; if they would, they MUST return an Escalation with reason `BUDGET_EXCEEDED`. For backward compatibility with v0.1 implementations, Dispatchers SHOULD accept `max_monetary_units` as an alias for `max_monetary_cost` in request envelopes.

**`provenance_requirement`** (object, OPTIONAL): The minimum acceptable Provenance Grade for the response. If the Service cannot achieve this grade, it MUST return an Escalation with reason `PROVENANCE_BELOW_REQUIREMENT` and the grade it could achieve. If omitted, no minimum grade is required.

**`priority`** (string, OPTIONAL): One of `"LOW"`, `"NORMAL"`, `"HIGH"`, `"CRITICAL"`. Defaults to `"NORMAL"`. Services MAY use priority for internal scheduling. The Dispatcher MAY use priority as a tiebreaker in routing decisions.

**`idempotency_key`** (string or null, OPTIONAL): If provided, a string that groups logically equivalent requests. Two Requests with the same `idempotency_key` SHOULD produce the same result. This is distinct from `request_id`-based idempotency (which is per-message): `idempotency_key` allows a requester to declare that a retried request with a new `request_id` is logically the same request.

<a id="section-7-3-3"></a>
### RESPONSE Envelope Fields

In addition to Common fields, RESPONSE envelopes carry:

```json
{
  "envelope": {
    // ... common fields ...
    "type": "RESPONSE",
    "request_id": "550e8400-e29b-41d4-a716-446655440000",
    "status": "SUCCESS",
    "provenance": {
      "grade": "VALIDATED",
      "evidence": [
        {
          "type": "test-suite-result",
          "description": "All 47 unit tests passed",
          "artifact_ref": "test-results/run-2026-08-03-001.json",
          "service_id": "test-runner-01"
        }
      ],
      "scope": "Code conforms to specification spec-2026-001",
      "service_id": "code-verifier-01",
      "service_version": "2.3.1",
      "service_mode": 3,
      "computation": {
        "tokens_consumed": 12500,
        "compute_seconds": 4.7,
        "model_id": "claude-opus-4-20260801"
      },
      "composition_trace": null
    }
  }
}
```

**`request_id`** (string, REQUIRED): The `request_id` of the Request this Response answers. MUST match the `request_id` of the original Request.

**`status`** (string, REQUIRED): One of `"SUCCESS"`, `"PARTIAL"`, `"ERROR"`. `SUCCESS` indicates the request was fully completed. `PARTIAL` indicates the Service produced a result but could not fully satisfy the request (the response includes what was achieved). `ERROR` indicates a failure (see Section 13 for error handling).

**`provenance`** (object, REQUIRED): The epistemic metadata for this response. MUST be present on every RESPONSE and ESCALATION. Structure defined in Section 10. Sub-fields:

- **`grade`** (string, REQUIRED): The Provenance Grade. One of the defined grades (Section 10.2).
- **`evidence`** (array, REQUIRED but MAY be empty): Evidence entries supporting the grade. Each entry has `type` (string), `description` (string), optionally `artifact_ref` (string, a reference to a verifiable artifact), and optionally `service_id` (string, the Service that produced the evidence).
- **`scope`** (string, OPTIONAL): What claim the grade applies to. REQUIRED when grade is `FORMALLY_VERIFIED` — it MUST identify the specification against which verification was performed.
- **`service_id`** (string, REQUIRED): The Service that produced this response.
- **`service_version`** (string, REQUIRED): The version of the Service.
- **`service_mode`** (integer, OPTIONAL): The Service Mode (1–4) if known.
- **`computation`** (object, OPTIONAL): Computational resources consumed. Sub-fields: `tokens_consumed` (integer), `compute_seconds` (number), `model_id` (string, the model used if LLM-based), and any additional fields the Service wishes to report.
- **`composition_trace`** (object or null, OPTIONAL): For responses composed from sub-request results, the composition trace documenting how the grade was derived (Section 10.5).

<a id="section-7-3-4"></a>
### ESCALATION Envelope Fields

An Escalation is a structured response indicating the Service cannot fulfill the request. It shares the RESPONSE envelope structure with additional escalation-specific fields:

```json
{
  "envelope": {
    // ... common fields ...
    "type": "ESCALATION",
    "request_id": "550e8400-e29b-41d4-a716-446655440000",
    "escalation": {
      "reason": "PROVENANCE_BELOW_REQUIREMENT",
      "detail": "LLM translation uncertainty too high for formal verification",
      "achieved_grade": "HEURISTIC",
      "requested_grade": "VALIDATED",
      "suggested_target": "human-review-queue-01",
      "partial_result_available": true
    },
    "provenance": {
      // ... provenance of the partial result, if any ...
    }
  }
}
```

**`escalation`** (object, REQUIRED):
- **`reason`** (string, REQUIRED): One of the defined escalation reasons (Section 13.3).
- **`detail`** (string, OPTIONAL): Human-readable explanation.
- **`achieved_grade`** (string, OPTIONAL): The Provenance Grade the Service could achieve, if it produced a partial result.
- **`requested_grade`** (string, OPTIONAL): The grade that was requested via `provenance_requirement.min_grade`.
- **`suggested_target`** (string, OPTIONAL): A Service ID or Capability Type the Dispatcher should try next.
- **`partial_result_available`** (boolean, REQUIRED): Whether the Content of this message contains a partial result.

When `partial_result_available` is true, the Content contains whatever the Service was able to produce before escalating. The Dispatcher MUST include this partial result when forwarding the escalation. This is the canonical location for partial results. Partial results MUST be carried in the ESCALATION message's Content, not in metadata. When the Dispatcher forwards the original Request through the escalation chain, it accumulates partial results from prior Services in the Request's metadata under the key `org.ccdp.partial_results` (Section 13.4.1) for downstream Services' reference. The Content of the forwarded Request remains the original requester's Content.

<a id="section-7-3-5"></a>
### NOTIFICATION Envelope Fields

Notifications are one-way messages that do not expect a response. They use the Common envelope fields plus:

```json
{
  "envelope": {
    // ... common fields ...
    "type": "NOTIFICATION",
    "capability_type": "org.ccdp.notification",
    "notification_type": "STATUS_UPDATE",
    "destination_id": "client-app-01"
  }
}
```

**`notification_type`** (string, REQUIRED): The kind of notification. Well-known types include `"STATUS_UPDATE"` (progress on a long-running request), `"RESOURCE_ALERT"` (a Service's resource utilization has crossed a threshold), and `"HEALTH_CHANGE"` (a Service's health status has changed). Implementations MAY define additional notification types.

**`destination_id`** (string, REQUIRED): Where to send the notification.

<a id="section-7-3-6"></a>
### HEALTH_REQUEST and HEALTH_RESPONSE Envelope Fields

Health messages are used by the Dispatcher to probe Service health (Section 13.6).

HEALTH_REQUEST:
```json
{
  "envelope": {
    // ... common fields ...
    "type": "HEALTH_REQUEST",
    "destination_id": "z3-prover-01"
  }
}
```

A HEALTH_REQUEST always targets a specific Service — the Dispatcher probes each registered Service's health endpoint individually (Section 13.6.1), it does not broadcast. `destination_id` is therefore REQUIRED on HEALTH_REQUEST.

HEALTH_RESPONSE:
```json
{
  "envelope": {
    // ... common fields ...
    "type": "HEALTH_RESPONSE",
    "health": {
      "status": "HEALTHY",
      "capabilities": {
        "org.ccdp.deduction": {
          "available": true,
          "current_load": 0.35,
          "queue_depth": 2,
          "estimated_latency_ms": 5000
        }
      },
      "capacity": {
        "max_concurrent_requests": 10,
        "current_concurrent_requests": 3
      },
      "detail": null
    }
  }
}
```

**`health.status`** (string, REQUIRED): One of `"HEALTHY"`, `"DEGRADED"`, `"UNHEALTHY"`.

**`health.capabilities`** (object, OPTIONAL): Per-capability status. Each key is a Capability Type; the value reports availability, current load (0.0–1.0), queue depth, and estimated latency for that capability.

**`health.capacity`** (object, OPTIONAL): Overall capacity information.

**`health.detail`** (string, OPTIONAL): Human-readable detail about the health status, particularly when DEGRADED or UNHEALTHY.

<a id="section-7-3-7"></a>
### DECOMPOSITION_RESULT Envelope Fields

Decomposition results are sent by the Decomposition Service and carry the decomposition plan. The full structure is defined in Section 14; the envelope fields are:

```json
{
  "envelope": {
    // ... common fields ...
    "type": "DECOMPOSITION_RESULT",
    "request_id": "550e8400-e29b-41d4-a716-446655440000",
    "provenance": {
      // ... provenance of the decomposition itself ...
    }
  }
}
```

The Content of a DECOMPOSITION_RESULT message is the Decomposition Plan (Section 14.3).

<a id="section-7-3-8"></a>
### Per-Message Required-Field Matrix

| Field | REQUEST | RESPONSE | ESCALATION | NOTIFICATION | HEALTH_REQ | HEALTH_RESP | DECOMP_RESULT |
|---|---|---|---|---|---|---|---|
| `ccdp_version` | R | R | R | R | R | R | R |
| `request_id` | R | R | R | R | R | R | R |
| `type` | R | R | R | R | R | R | R |
| `trace_id` | R | R | R | R | R | R | R |
| `span_id` | R | R | R | R | R | R | R |
| `source_id` | R | R | R | R | R | R | R |
| `capability_type` | R | S | S | O | — | — | R |
| `destination_id` | O | — | O | R | R | — | — |
| `priority` | O | — | O | — | — | — | — |
| `provenance_requirement` | O | — | O | — | — | — | — |
| `provenance` | — | R | R\* | — | — | — | S |
| `cost_budget` | O | — | O | — | — | — | O |
| `deadline` | R | — | O | — | — | — | O |
| `timestamp` | R | R | R | R | R | R | R |

R = REQUIRED, S = RECOMMENDED (SHOULD), O = OPTIONAL, — = not applicable. This matrix is normative. Where prose elsewhere in this section or other sections conflicts with this matrix, the matrix takes precedence.

\* `provenance` is REQUIRED on ESCALATION when the message carries partial results (Section 7.3.4); it MAY be omitted for escalations with no cognitive output (e.g., pure routing failures). `priority` and `provenance_requirement` are request-directional fields that do not apply to a Decomposition Service's plan output — DECOMPOSITION_RESULT carries neither.

<a id="section-7-4"></a>
## Content Structure

The Content is the opaque payload of a CCDP message. Its structure is governed by the Capability Record's input schema (for Requests) or output schema (for Responses).

```json
{
  "content": {
    "type": "natural-language",
    "schema_ref": "org.ccdp.deduction/input/v2",
    "body": {
      // ... capability-specific payload ...
    }
  }
}
```

**`content.type`** (string, REQUIRED): The content format. Well-known types:
- `"natural-language"`: Free-text natural language
- `"formal-logic"`: Logical formulas (the specific logic is identified by the schema)
- `"proof-object"`: A machine-checkable proof
- `"validated-plan"`: A plan that has been validated by a sound validator
- `"structured-data"`: Generic structured data
- `"code"`: Source code (language identified by the schema)
- `"multipart"`: Multiple content parts (see below)

Custom content types MAY be defined in Capability Records using reverse-domain notation.

**`content.schema_ref`** (string, OPTIONAL): A reference to the JSON Schema governing this content's `body`, in the format `{capability_type}/{direction}/{version}`. If present, the Dispatcher MAY validate the body against this schema.

**`content.body`** (any, REQUIRED): The actual payload. Structure determined by the schema.

<a id="section-7-4-1"></a>
### Multipart Content

When a response contains multiple distinct outputs (e.g., generated code plus a proof of correctness), the `content.type` is `"multipart"` and the body is an array of typed parts:

```json
{
  "content": {
    "type": "multipart",
    "body": {
      "parts": [
        {
          "type": "code",
          "label": "implementation",
          "body": { "language": "rust", "source": "fn verify(...) { ... }" }
        },
        {
          "type": "proof-object",
          "label": "correctness-proof",
          "body": { "prover": "verus", "proof": "..." }
        }
      ]
    }
  }
}
```

Each part carries its own `type` and `label`. The `label` field is a human-readable identifier that the Decomposition Plan's composition function can reference when assembling results from sub-requests.

<a id="section-7-5"></a>
## Dispatcher Audit Annotation

When the Dispatcher forwards a message, it MUST annotate the envelope with audit metadata. These fields are written by the Dispatcher, not by the originator:

```json
{
  "envelope": {
    // ... existing fields ...
    "audit": {
      "dispatcher_id": "dispatcher-prod-01",
      "received_at": "2026-08-03T14:30:00.123Z",
      "routed_at": "2026-08-03T14:30:00.145Z",
      "routing_decision": {
        "selected_service": "z3-prover-01",
        "reason": "lowest_cost_healthy",
        "candidates_considered": 3,
        "registry_query_ms": 12
      },
      "schema_validation": {
        "input_valid": true,
        "schema_version": "v2"
      }
    }
  }
}
```

The `audit` field is detailed in Section 11.

<a id="section-7-6"></a>
## Size Limits

Implementations MUST support messages of at least 16 MiB. Implementations SHOULD support messages of at least 64 MiB. Messages exceeding the implementation's size limit MUST be rejected with HTTP status 413 (Payload Too Large). If the message is small enough to parse but exceeds the CCDP implementation's processing limit, it MUST be rejected with CCDP error code `-32602` (Invalid params) with a `data.reason` of `"message_too_large"`.

For content payloads that exceed these limits (e.g., large proof objects, extensive code), implementations SHOULD use a reference-based approach: the `content.body` contains a reference (URI) to the full content stored in an external system, rather than the content inline.

<a id="section-7-7"></a>
## Extensibility and Forward Compatibility

The `metadata` field on every envelope provides the extension point for protocol evolution:

1. Unknown keys in `metadata` MUST be preserved by all intermediaries (including the Dispatcher) when forwarding a message. An implementation that does not understand a metadata key MUST NOT strip it, modify it, or use it for routing decisions.

Metadata keys in the `org.ccdp.*` namespace that begin with `org.ccdp.request.*` are request-directional: they are meaningful on REQUEST and ESCALATION messages and SHOULD NOT be blindly copied to RESPONSE messages. Metadata keys beginning with `org.ccdp.response.*` are response-directional. Keys without a directional prefix are bidirectional and MUST be preserved in both directions. This prevents request-only control metadata (e.g., escalation history, routing hints) from leaking into responses.

2. New protocol features SHOULD be introduced as metadata keys in the `org.ccdp.*` namespace before being promoted to top-level envelope fields in a subsequent protocol version.

3. Implementation-specific metadata SHOULD use reverse-domain notation (e.g., `com.example.my_field`) to avoid collisions.

4. An implementation that receives an envelope with an unrecognized `type` field MUST reject the message with error code `-32600` (invalid request) rather than silently dropping it.

This approach follows the TCP/IP tradition of extensible headers: existing implementations continue to work as new fields are added, and the protocol evolves without version bumps for non-breaking changes.

<a id="section-7-8"></a>
## Machine-Readable Schemas

A companion `schemas/` directory will contain normative JSON Schemas for each message type defined in this section. Until these schemas are published, the field definitions and per-message matrix in this section are the normative message specification. The planned schemas cover:

- `envelope.schema.json` — common envelope fields and per-message-type required/optional field sets
- `content.schema.json` — Content wrapper structure (type, body, schema_ref)
- `provenance.schema.json` — provenance grade, evidence entries, composition rules
- `escalation.schema.json` — escalation reason, detail, partial result
- `health.schema.json` — health request and response structures
- `decomposition-plan.schema.json` — plan structure, sub-requests, typed result references, composition spec
- `audit-record.schema.json` — audit record fields and per-message-type requirements

When published, the schemas will be normative, versioned with the document version. Implementations SHOULD validate messages against these schemas during development and testing. Creating the companion schemas is an implementation prerequisite tracked in the README.

<a id="section-7-9"></a>
## HTTP Status Code Mapping

When CCDP messages are transported over HTTP, the following mapping applies:

| Scenario | HTTP Status | CCDP Behavior |
|---|---|---|
| Successful response | 200 OK | JSON-RPC result with CCDP envelope |
| JSON parse error | 400 Bad Request | JSON-RPC error `-32700` |
| Authentication failure | 401 Unauthorized | No JSON-RPC body; Dispatcher logs auth failure |
| Authorization failure (valid token, insufficient scope) | 403 Forbidden | JSON-RPC error `-32009` |
| Message too large to parse | 413 Payload Too Large | No JSON-RPC body |
| Rate limited by Dispatcher | 429 Too Many Requests | JSON-RPC error `-32014` (see Section 13.2) with `Retry-After` in error `data` |
| Rate limited by Service | (Dispatcher absorbs) | Dispatcher treats as DEGRADED, follows retry/reroute (Section 13.5) |
| Internal Dispatcher error | 500 Internal Server Error | JSON-RPC error `-32603` |

HTTP status codes in the 4xx range indicate client-side issues; 5xx indicate Dispatcher-side issues. The JSON-RPC error body, when present, carries the structured CCDP error with trace context for audit correlation.

<a id="section-8"></a>
# Capability Registry

<a id="section-8-1"></a>
## Role and Scope

The Capability Registry is the central source of truth for what Services exist, what they can do, and how to interact with them. The Dispatcher consults the Registry for every routing decision. The Registry enforces schema versioning to ensure that Services evolve without breaking consumers.

This section specifies the Registry's *interface* — the queries it must answer and the records it must maintain. It does not specify the storage backend, replication strategy, or deployment topology. A conforming Registry MAY be a database, a configuration file, a distributed key-value store, an in-memory data structure, or any mechanism that satisfies the interface contract.

<a id="section-8-2"></a>
## Capability Records

A Capability Record describes one Service's implementation of one Capability Type. A Service that implements multiple Capability Types has one record per type.

<a id="section-8-2-1"></a>
### Record Structure

```json
{
  "capability_record": {
    "service_id": "z3-prover-01",
    "capability_type": "org.ccdp.deduction",
    "version": "2.1.0",
    "endpoint": "https://z3-prover-01.internal:8443/ccdp",
    "status": "ACTIVE",

    "input_schema": {
      "$schema": "https://json-schema.org/draft/2020-12/schema",
      "type": "object",
      "properties": {
        "logic": { "type": "string", "enum": ["propositional", "first-order", "smt-lib2"] },
        "formula": { "type": "string" },
        "timeout_ms": { "type": "integer", "minimum": 100 }
      },
      "required": ["logic", "formula"]
    },

    "output_schema": {
      "$schema": "https://json-schema.org/draft/2020-12/schema",
      "type": "object",
      "properties": {
        "result": { "type": "string", "enum": ["sat", "unsat", "unknown", "timeout"] },
        "model": { "type": ["object", "null"] },
        "proof": { "type": ["string", "null"] }
      },
      "required": ["result"]
    },

    "cost_hints": {
      "estimated_latency_ms": { "p50": 500, "p95": 5000, "p99": 30000 },
      "estimated_cost_per_request": { "monetary_units": "0.001", "monetary_unit": "USD" },
      "token_cost": null,
      "compute_intensive": true
    },

    "provenance_capabilities": {
      "max_grade": "FORMALLY_VERIFIED",
      "typical_grade": "FORMALLY_VERIFIED",
      "evidence_types": ["proof-object", "counterexample"]
    },

    "health_check": {
      "endpoint": "https://z3-prover-01.internal:8443/ccdp/health",
      "interval_seconds": 30,
      "timeout_ms": 5000
    },

    "isolation": {
      "executes_arbitrary_code": false,
      "requires_sandbox": false,
      "network_access": false,
      "filesystem_access": false
    },

    "escalation_chain": [
      {"kind": "service_id", "value": "isabelle-prover-01"},
      {"kind": "capability_type", "value": "org.ccdp.human_review"}
    ],

    "cacheable": false,
    "max_input_size": 1048576,

    "tags": ["formal-methods", "smt", "sat"],
    "description": "Z3 SMT solver for propositional and first-order logic",
    "registered_at": "2026-07-15T10:00:00Z",
    "updated_at": "2026-08-01T14:00:00Z",

    "metadata": {}
  }
}
```

<a id="section-8-2-2"></a>
### Field Definitions

**`service_id`** (string, REQUIRED): Unique identifier for the Service instance.

**`capability_type`** (string, REQUIRED): The Capability Type this record describes.

**`version`** (string, REQUIRED): Semantic version of this record's schema contract. Used for schema versioning (Section 8.5).

**`endpoint`** (string, REQUIRED): The HTTPS endpoint where the Service accepts CCDP messages.

**`status`** (string, REQUIRED): One of `"ACTIVE"` (accepting requests), `"DRAINING"` (completing in-flight requests but not accepting new ones), `"INACTIVE"` (not accepting requests), `"DEPRECATED"` (will be removed; consumers should migrate).

**`input_schema`** (object, REQUIRED): JSON Schema [JSON-SCHEMA-2020-12] describing the valid structure of `content.body` for Requests to this Service. The Dispatcher SHOULD validate request Content against the Service's input schema before forwarding (REQUIRED for Full conformance, RECOMMENDED for Core conformance; see Section 16).

**`output_schema`** (object, REQUIRED): JSON Schema describing the structure of `content.body` for Responses from this Service. The Dispatcher SHOULD validate Response content against this schema before forwarding to the requester.

**`cost_hints`** (object, REQUIRED): Resource consumption estimates for routing decisions. Fields:
- `estimated_latency_ms`: Object with percentile keys (`p50`, `p95`, `p99`), values in milliseconds.
- `estimated_cost_per_request`: Monetary cost estimate with `monetary_units` (string, decimal) and `monetary_unit` (ISO 4217 string).
- `token_cost`: For LLM-based services, estimated tokens per request. Null for non-LLM services.
- `compute_intensive`: Boolean indicating whether the service consumes significant compute resources.

**`provenance_capabilities`** (object, REQUIRED): What Provenance Grades this Service can produce.
- `max_grade`: The highest grade this Service can assign to its output.
- `typical_grade`: The grade most responses will carry.
- `evidence_types`: Array of Evidence types this Service can produce (e.g., `"proof-object"`, `"test-result"`, `"human-signature"`).

**`health_check`** (object, REQUIRED): Health monitoring configuration.
- `endpoint`: URL for health check probes.
- `interval_seconds`: How often the Dispatcher should probe.
- `timeout_ms`: How long to wait for a health response before marking UNHEALTHY.

**`isolation`** (object, REQUIRED): Security and isolation requirements.
- `executes_arbitrary_code`: Whether the Service executes user-provided code.
- `requires_sandbox`: Whether the Service should run in a sandboxed environment.
- `network_access`: Whether the Service requires network access beyond the Dispatcher.
- `filesystem_access`: Whether the Service requires filesystem access.

**`escalation_chain`** (array of typed entries, REQUIRED but MAY be empty): Ordered list of fallback targets to try if this Service returns an Escalation. The Dispatcher processes the chain in order. An empty chain means escalation goes directly to the Human Supervisor's queue. Escalation chain entries are typed objects: `{"kind": "service_id", "value": "human-review-queue-01"}` or `{"kind": "capability_type", "value": "org.ccdp.human_review"}`. The `kind` field disambiguates the entry; string-only entries are ambiguous and MUST NOT be used.

**`cacheable`** (boolean, OPTIONAL, default false): Whether the Dispatcher MAY cache and reuse Response Content for identical Requests (same `capability_type` and identical Content). When true, the Dispatcher MAY return a cached Response without forwarding the Request, provided the cache entry has not expired (expiry is deployment-configured).

**`max_input_size`** (integer, OPTIONAL): Maximum input Content size in bytes that the Service can accept. Used by the Dispatcher for structural decomposition triggers (Section 14.2) — if a Request's Content exceeds the target Service's `max_input_size`, the Dispatcher MAY initiate decomposition without content inspection.

**`tags`** (array of strings, OPTIONAL): Descriptive tags for search and categorization.

**`description`** (string, OPTIONAL): Human-readable description of the Service and its capabilities.

**`registered_at`** (string, REQUIRED): ISO 8601 timestamp of initial registration.

**`updated_at`** (string, REQUIRED): ISO 8601 timestamp of last record update.

**`metadata`** (object, OPTIONAL): Extensible metadata. Same semantics as envelope metadata (Section 7.7).

**Static vs dynamic fields.** The Capability Record contains both static metadata (capability type, schemas, cost hints, isolation requirements, escalation chain) and dynamic telemetry (health status, current load, queue depth, estimated latency). Static fields change only through Registry update operations. Dynamic fields are updated by health probes (Section 13.6) and MAY be cached by the Dispatcher with a configurable TTL (RECOMMENDED: 30 seconds). Routing decisions based on stale dynamic data are an inherent risk; the Dispatcher SHOULD timestamp dynamic field updates and prefer fresh data for high-priority or high-cost requests.

<a id="section-8-3"></a>
## Well-Known Capability Types

The following Capability Types are defined by this specification. Implementations MAY define additional types.

| Capability Type | Description | Typical Mode |
|----------------|-------------|--------------|
| `org.ccdp.deduction` | Logical deduction, theorem proving, SMT solving | Mode 2 or 3 |
| `org.ccdp.planning` | Task planning, decomposition into action sequences | Mode 2 or 3 |
| `org.ccdp.language.generation` | Natural language generation, drafting, summarization | Mode 1 |
| `org.ccdp.language.translation` | Translation between natural languages or representations | Mode 1 or 3 |
| `org.ccdp.language.analysis` | Natural language understanding, classification, extraction | Mode 1 |
| `org.ccdp.verification` | Verification of code, proofs, plans against specifications | Mode 2 or 3 |
| `org.ccdp.selection` | Ranking, scoring, best-of-N selection | Mode 1, 2, or 3 |
| `org.ccdp.retrieval` | Information retrieval, database query, knowledge lookup | Mode 2 |
| `org.ccdp.decomposition` | Request decomposition into typed sub-requests | Mode 1 or 3 |
| `org.ccdp.human_review` | Human review, judgment, attestation | Mode 4 |
| `org.ccdp.code.generation` | Source code generation | Mode 1 or 3 |
| `org.ccdp.code.execution` | Code execution in a sandboxed environment | Mode 2 |
| `org.ccdp.composition` | Custom composition of Decomposition sub-results requiring judgment (Section 14.3.4) | Mode 1 or 3 |

Custom Capability Types SHOULD use reverse-domain notation (e.g., `com.example.custom_capability`) to avoid collisions with well-known types.

<a id="section-8-4"></a>
## Registry Interface

The Registry MUST support the following query operations. These are defined as logical operations, not specific API endpoints — implementations MAY expose them as REST APIs, gRPC services, function calls, or any other mechanism.

<a id="section-8-4-1"></a>
### Register

Register a new Capability Record or update an existing one.

**Input:** A Capability Record.
**Behavior:** If no record exists for the given (`service_id`, `capability_type`) pair, create one. If a record exists, update it subject to schema compatibility rules (Section 8.5). If the update would break compatibility, reject it with an error. The record is identified by the tuple `(service_id, capability_type, major_version)`. The `major_version` component of the record identity is derived from the `version` field by extracting the major component of the semantic version string (e.g., version `"2.1.0"` has `major_version` 2). The Registry MUST treat records with the same `(service_id, capability_type)` but different major versions as distinct records that coexist during transitions. During major-version transitions, old and new versions coexist as separate records with the same `(service_id, capability_type)` but different `major_version` values. The Dispatcher selects the appropriate version based on the Request's `content.schema_ref` or deployment policy.
**Output:** The stored record with server-assigned timestamps, or an error with the incompatibility details.

<a id="section-8-4-2"></a>
### Lookup

Look up Services that implement a given Capability Type.

**Input:** `capability_type` (required), `status_filter` (optional, defaults to `["ACTIVE"]`), `min_provenance_grade` (optional), `max_cost` (optional), `tags` (optional).
**Output:** The Lookup operation returns matching Capability Records. Sorting and ranking are the Dispatcher's responsibility (Section 9.2), not the Registry's. The Registry MAY return results in any order. The Registry MAY accept query parameters (e.g., minimum provenance grade, maximum cost) to filter results, but the Dispatcher makes the final routing decision. Empty array if no matches.

<a id="section-8-4-3"></a>
### Get

Retrieve a specific Capability Record.

**Input:** `service_id`, `capability_type`, `version?` (optional). If `version` is omitted, returns the latest version. If `version` is provided, returns that specific version.
**Output:** The Capability Record, or an error if not found.

<a id="section-8-4-4"></a>
### Deregister

Remove a Capability Record.

**Input:** `service_id`, `capability_type`, `version?` (optional). If `version` is omitted, deregisters all versions. If `version` is provided, deregisters only that version.
**Behavior:** Set the record's status to `INACTIVE`. The record SHOULD be retained for audit purposes (the `registered_at` and `updated_at` fields are part of the audit trail). The record SHOULD NOT be permanently deleted.
**Output:** Confirmation, or an error if not found.

<a id="section-8-4-5"></a>
### List Schema Versions

List all schema versions for a Capability Type.

**Input:** `capability_type`, `major_version?` (optional filter).
**Output:** An array of `{version, compatibility, registered_at}` entries, ordered by version.

<a id="section-8-4-6"></a>
### Registry API Binding

This specification defines the Registry's logical operations and data model. It does not mandate a specific wire protocol for Registry access. Implementations MAY expose the Registry as a REST API, a gRPC service, an in-process library, or any other mechanism that satisfies the operation contracts above. If two CCDP deployments need their Registries to interoperate (e.g., federated routing), they MUST agree on a common Registry API binding outside this specification. A future CCDP extension MAY define a standard Registry wire protocol.

<a id="section-8-4-7"></a>
### Content Schema Selection

When the Dispatcher validates Content, it selects the schema as follows: (1) If the message's `content.schema_ref` field is present, the Dispatcher looks up that schema in the Service's Capability Record. (2) If `schema_ref` is absent, the Dispatcher uses the Service's default input schema (for requests) or output schema (for responses) from the Capability Record. (3) If the Capability Record has no schema for the content type, schema validation is skipped. The Dispatcher SHOULD log schema-validation-skipped in the audit record. Schema validation is REQUIRED for Full conformance (Section 16) and RECOMMENDED for Core conformance.

`input_schema` and `output_schema` are REQUIRED fields on every Capability Record (Section 8.2.2) for the Service's primary content type, so step (3) above cannot occur for that content type. Services that accept multiple content types MAY register separate Capability Records per content type, or MAY use a permissive schema (e.g., `{}`) for content types where structural validation is not meaningful. A Capability Record with a permissive schema satisfies the schema-presence requirement; the Dispatcher logs `schema_validation: "permissive"` in the audit record.

<a id="section-8-5"></a>
## Schema Versioning and Compatibility

Schema evolution is the chronic wound of typed protocols. CCDP addresses it through the Registry, which enforces compatibility rules at registration time — not at the Dispatcher, which should not need to understand schema evolution.

<a id="section-8-5-1"></a>
### Versioning Model

Capability Record versions follow Semantic Versioning [SemVer] (MAJOR.MINOR.PATCH):

- **PATCH** increments indicate backward-compatible clarifications to the schema (e.g., updated descriptions, examples). The schema's structural validation rules are unchanged.
- **MINOR** increments indicate backward-compatible additions (e.g., new optional fields in the output schema). Existing consumers continue to work; new consumers can use the new fields.
- **MAJOR** increments indicate breaking changes (e.g., removed required fields, changed field types). Existing consumers will break.

<a id="section-8-5-2"></a>
### Compatibility Rules

The Registry MUST enforce the following compatibility rules when a Service registers or updates a Capability Record:

**PATCH update:** The new schema MUST be semantically equivalent to the previous schema. The Registry SHOULD verify that the JSON Schema validates the same set of documents.

**MINOR update:** The new input schema MUST accept a *superset* of the documents accepted by the previous schema (backward-compatible input). The new output schema MUST produce documents that are a *superset* of the previous schema — i.e., new fields may be added, but existing fields MUST NOT be removed or have their types changed (forward-compatible output).

**MAJOR update:** No compatibility constraint. The Registry MUST retain the previous version's schema for the transition period. Services SHOULD support both the old and new versions concurrently during the transition.

<a id="section-8-5-3"></a>
### Compatibility Checking

The Registry SHOULD perform structural compatibility checking at registration time. The recommended approach follows Avro's compatibility model [Kleppmann 2012]:

- **Backward compatibility** (new schema reads old data): the new input schema must accept everything the old schema accepted.
- **Forward compatibility** (old schema reads new data): the old output schema must be able to parse output produced under the new schema (by ignoring unknown fields).
- **Full compatibility** (both directions): required for MINOR updates.

Implementations MAY use JSON Schema tooling to automate compatibility checking. The Registry SHOULD reject incompatible updates with a detailed error message identifying the specific incompatibility.

**Enforceability caveat.** General JSON Schema equivalence and subset checking are undecidable problems. Conforming Registry implementations MUST enforce compatibility for a practical subset: additive properties (MINOR), identical structure with clarified descriptions (PATCH), and structural breaking changes (MAJOR). Implementations SHOULD provide tooling for automated compatibility checking but MAY require operator attestation for edge cases. The Registry MUST record whether a version update was auto-verified or operator-attested.

<a id="section-8-5-4"></a>
### Transition Period

When a Service registers a MAJOR version update, the Registry MUST support a transition period during which both the old and new versions are available. During this period:

- The old version's record has status `DEPRECATED`.
- The new version's record has status `ACTIVE`.
- The Dispatcher routes to the new version by default but MAY route to the old version if a Request's `metadata` specifies a version constraint.
- After the transition period (configured per deployment), the old version's record is set to `INACTIVE`.

<a id="section-8-6"></a>
## Registry Availability

The Registry is a critical infrastructure component — if the Registry is unavailable, the Dispatcher cannot route. Implementations SHOULD address this through:

- **Caching:** The Dispatcher SHOULD cache Registry query results with a configurable TTL. Cached results allow routing to continue during brief Registry outages.
- **Staleness tolerance:** The Dispatcher SHOULD accept stale cache entries (beyond TTL) if the Registry is unreachable, with a warning logged to the audit trail.
- **Static fallback:** The Dispatcher MAY maintain a static routing table as a fallback for critical Capability Types, used when both the Registry and the cache are unavailable.

The specific availability strategy is an implementation concern, not a protocol requirement. The protocol requires only that routing decisions are logged (including whether they were made from live Registry data, cached data, or static fallback), so that the audit trail reflects the data freshness of each routing decision.

<a id="section-9"></a>
# Routing

<a id="section-9-1"></a>
## Routing Principles

Routing is the Dispatcher's core function: given a Request with a `capability_type`, select the Service best suited to handle it. CCDP routing is *envelope-based* — the Dispatcher makes routing decisions from envelope metadata and Registry data, never from Content.

Three principles govern routing:

1. **Capability-type dispatch.** The primary routing key is `envelope.capability_type`. The Dispatcher queries the Registry for Services that implement this type and are ACTIVE.

2. **Cost-aware selection.** Among eligible Services, the Dispatcher selects based on cost hints (latency, monetary cost, compute intensity), health status, current load, and the Request's constraints (deadline, cost_budget, provenance_requirement).

3. **Deterministic tiebreaking.** When multiple Services are equally suitable, the Dispatcher applies a deterministic tiebreaking rule (e.g., round-robin, lowest-load, consistent hashing by request_id). The specific tiebreaking strategy is implementation-defined but MUST be logged.

<a id="section-9-2"></a>
## Routing Algorithm

The Dispatcher MUST implement the following routing algorithm. Steps are ordered; the Dispatcher proceeds to the next step only if the current step does not resolve the routing decision.

### Step 1: Explicit Destination

If `envelope.destination_id` is non-null, route to the specified Service. If the Service is not registered, not ACTIVE, or not healthy, return error `-32001` (service unavailable). Do not fall through to capability-based routing. Explicit destinations MUST also pass authorization, provenance feasibility, deadline, budget, and isolation checks — the same policy filters applied to normal routing (Steps 2–6). An explicit destination is a routing hint, not a bypass of protocol enforcement. If any check fails, the Dispatcher MUST return the appropriate error, not silently fall through to normal routing.

### Step 2: Capability Lookup

Query the Registry for all ACTIVE Services implementing `envelope.capability_type`. If no Services are found, return error `-32002` (no service for capability type).

### Step 3: Health Filter

Remove Services with Health Status UNHEALTHY from the candidate set. Services with Health Status DEGRADED remain eligible but are deprioritized (Step 6).

If all Services are UNHEALTHY, the Dispatcher MUST follow its deployment-configured `all_unhealthy_policy` for the requested capability type. The policy MUST be one of: `"error"` (return error `-32003`), `"escalate"` (treat as an escalation with reason `INTERNAL_DEGRADATION` and walk the escalation chain), or `"queue"` (hold the request for up to `queue_timeout_ms` milliseconds, configurable per capability type, default 30000ms; retry routing when a service becomes healthy or when the timeout expires). If the request has a deadline and the remaining deadline budget is less than `queue_timeout_ms`, the effective queue timeout is the remaining deadline budget. If the timeout expires without a healthy service, the Dispatcher returns error `-32003`. Queued requests are audit-logged with status `"queued"` and a follow-up audit entry when dequeued (routed or timed out). The default policy is `"error"`. The chosen policy MUST be recorded in the audit trail.

### Step 4: Deadline Filter

Remove Services whose `cost_hints.estimated_latency_ms.p95` exceeds `envelope.remaining_budget_ms`. A Service that is unlikely to respond within the deadline is not a viable candidate.

If all candidate services are filtered out by deadline, the Dispatcher MUST return error `-32004` (deadline not achievable). The Dispatcher MUST NOT silently route to a service that cannot plausibly meet the deadline. The audit record MUST include the remaining budget, the fastest candidate's estimated latency, and the filtering decision.

### Step 5: Provenance Filter

If `envelope.provenance_requirement.min_grade` is set, remove Services whose `provenance_capabilities.max_grade` is below the required grade.

If no candidate service can meet the Request's `provenance_requirement.min_grade`, the Dispatcher MUST NOT silently route to a lower-grade service. The Dispatcher MUST follow its deployment-configured `provenance_unavailable_policy` for the requested capability type. The policy MUST be one of: `"error"` (return error `-32005`) or `"escalate"` (treat as implicit escalation with reason `PROVENANCE_BELOW_REQUIREMENT`, routing through the escalation chain to find a service that can meet the grade requirement). The default policy is `"error"`. The chosen policy MUST be recorded in the audit trail. The Dispatcher MUST NOT forward a request to a service that cannot meet the provenance requirement without the requester's knowledge.

### Step 6: Cost-Aware Ranking

Rank the remaining candidates using a scoring function that considers:

- **Health status:** HEALTHY Services are preferred over DEGRADED Services.
- **Current load:** Services with lower `health.capabilities[type].current_load` are preferred.
- **Estimated latency:** Lower latency is preferred, weighted against the remaining deadline budget.
- **Monetary cost:** Lower cost is preferred, weighted against the Request's `cost_budget`.
- **Provenance grade:** If the Request specifies a `provenance_requirement`, Services whose `typical_grade` meets or exceeds the requirement are preferred.
- **Queue depth:** Services with lower `health.capabilities[type].queue_depth` are preferred.

The specific scoring function is implementation-defined. This specification does not mandate weights or formulas — implementations SHOULD tune their scoring function to their deployment's priorities (latency-sensitive, cost-sensitive, quality-sensitive).

### Step 7: Selection and Logging

Select the highest-ranked candidate. Log the routing decision in the `audit.routing_decision` field (Section 7.5), including:
- `selected_service`: the Service ID selected
- `reason`: why this Service was selected (e.g., `"lowest_cost_healthy"`, `"only_candidate"`, `"explicit_destination"`)
- `candidates_considered`: how many candidates were evaluated
- `registry_query_ms`: how long the Registry query took
- `filters_applied`: which filters removed candidates (e.g., `["health", "deadline"]`)

The audit record for a routing decision MUST include at minimum: the list of candidate services considered, the normalized scoring factors (health weight, cost weight, latency weight, provenance weight), the deployment policy version used, the computed score for each candidate, and the tiebreaker (if any). This enables retrospective routing analysis and debugging.

Detailed scoring traces (candidate lists, weights, per-candidate scores) MAY contain cost and capacity information that is sensitive across administrative boundaries. Deployments SHOULD classify routing audit fields by access level and redact sensitive fields in audit exports to external parties.

<a id="section-9-3"></a>
## Routing for Decomposed Sub-Requests

When the Dispatcher processes a Decomposition Plan (Section 14), it routes each sub-request independently through the same routing algorithm. Sub-requests inherit the parent's `trace_id` and `deadline` (with elapsed time subtracted) but have their own `capability_type`, `request_id`, and `span_id`.

The Dispatcher MUST respect the Decomposition Plan's dependency ordering: sub-requests with unresolved dependencies MUST NOT be dispatched until their dependencies are fulfilled. Sub-requests with no dependencies MAY be dispatched in parallel.

<a id="section-9-4"></a>
## Escalation Routing

When a Service returns an Escalation, the Dispatcher routes to the next target in the Escalation Chain. Escalation routing follows a defined sequence:

1. **Suggested target.** If `escalation.suggested_target` is set and the target is healthy, route to it.
2. **Escalation chain.** If the suggested target is unavailable or not set, walk the `escalation_chain` from the Service's Capability Record. Route to the first healthy target. Escalation targets MUST be checked using the full routing algorithm (Section 9.2): capability match, health status, authorization, provenance capability, deadline feasibility, budget feasibility, isolation requirements, and cycle detection. A health-only check is insufficient — an escalation target that is healthy but unauthorized, over-budget, or incapable of the requested provenance grade MUST be skipped.
3. **Capability fallback.** If the escalation chain is exhausted, query the Registry for other Services implementing the same Capability Type (excluding the Service that escalated) and route to the best available.
4. **Human queue.** If no automated Service can handle the request, route to a Service of type `org.ccdp.human_review`. This is the terminal escalation target.
5. **Failure.** If no human review Service is available, return error `-32006` (escalation chain exhausted) to the requester.

Each escalation routing decision is logged in the audit trail with the full escalation context: which Service escalated, why, what targets were tried, and where the request ultimately landed.

<a id="section-9-5"></a>
## Retry Policy

The Dispatcher SHOULD implement a retry policy for transient failures (network errors, timeouts, HTTP 503 responses). The retry policy:

- MUST respect idempotency: retries of the same `request_id` are safe because Services MUST be idempotent.
- MUST respect the deadline: no retry should be attempted if the remaining deadline budget is insufficient.
- SHOULD use exponential backoff with jitter for retries to the same Service.
- SHOULD try a different Service (if available) before retrying the same Service.
- MUST log each retry attempt in the audit trail.
- MUST limit total retries to a configurable maximum (RECOMMENDED: 3) to prevent retry storms.

<a id="section-9-6"></a>
## Circuit Breaker Integration

The Dispatcher MUST implement circuit breaker logic for each Service (Section 13.6). A Service's circuit breaker has three states:

- **CLOSED** (normal operation): Requests are forwarded. Failures are counted.
- **OPEN** (tripped): Requests are NOT forwarded. The Service is excluded from routing. Periodic health probes test recovery.
- **HALF_OPEN** (testing recovery): A limited number of requests are forwarded. If they succeed, the circuit breaker returns to CLOSED. If they fail, it returns to OPEN.

The circuit breaker state is an input to routing: OPEN circuit breakers effectively remove a Service from the candidate set. The transition logic (failure thresholds, recovery probe intervals) is implementation-defined.

<a id="section-9-7"></a>
## Routing Table

The Dispatcher maintains a Routing Table — a runtime data structure combining Registry data, health status, circuit breaker state, and load metrics. The Routing Table is the Dispatcher's view of the world:

```
┌──────────────────────┬────────────┬──────────┬─────────────┬──────────┐
│ Capability Type      │ Service ID │ Health   │ Circuit     │ Load     │
│                      │            │ Status   │ Breaker     │ (0.0-1.0)│
├──────────────────────┼────────────┼──────────┼─────────────┼──────────┤
│ org.ccdp.deduction   │ z3-prover  │ HEALTHY  │ CLOSED      │ 0.35     │
│ org.ccdp.deduction   │ isabelle   │ DEGRADED │ CLOSED      │ 0.80     │
│ org.ccdp.planning    │ fd-planner │ HEALTHY  │ CLOSED      │ 0.10     │
│ org.ccdp.language.*  │ llm-pool   │ HEALTHY  │ CLOSED      │ 0.55     │
│ org.ccdp.human_review│ review-q   │ HEALTHY  │ CLOSED      │ 0.20     │
│ org.ccdp.verification│ verifier   │ UNHEALTHY│ OPEN        │ —        │
└──────────────────────┴────────────┴──────────┴─────────────┴──────────┘
```

The Routing Table is refreshed from the Registry at a configurable interval (RECOMMENDED: every 30 seconds) and updated in real-time by health check responses. It is an internal Dispatcher structure, not a protocol element — its format is implementation-defined.

**Wildcard capability matching.** Capability type patterns ending in `.*` match any capability type that shares the prefix up to the wildcard. `org.ccdp.language.*` matches `org.ccdp.language.generation`, `org.ccdp.language.translation`, etc., but not `org.ccdp.language` itself (the wildcard requires at least one additional segment). Wildcard patterns are valid only in token scopes (Section 15.3.2) and routing configuration; they MUST NOT appear in Capability Records or Registry lookups. The routing table format is implementation-defined and MAY support pattern matching (e.g., glob or prefix wildcards). Pattern syntax, if supported, is not part of the CCDP wire protocol — it is a deployment-local routing configuration concern. The `org.ccdp.language.*` entry in the example above illustrates implementation flexibility, not a normative capability identifier.

<a id="section-10"></a>
# Provenance and Evidence Grades

<a id="section-10-1"></a>
## Rationale

Provenance grades are CCDP's novel contribution — the feature that distinguishes it from every existing protocol for service communication. The core insight: cognitive outputs are not data; they are *claims with epistemic status*. A database query returns a fact. A theorem prover returns a proof. An LLM returns a plausible completion. These are structurally different kinds of evidence, and a protocol that treats them identically forces every consumer to reconstruct epistemic status from scratch.

The provenance system is grounded in two theoretical foundations:

**Spence's signaling theory [Spence 1973]:** A quality signal works only when it is *expensive to fake*. Each provenance grade represents an increasing cost-to-fake — an LLM can cheaply assert anything (ASSERTED), but producing a machine-checkable proof (FORMALLY_VERIFIED) requires actual computation that cannot be faked without doing the work. The grade taxonomy is designed so that each level requires materially more effort to produce fraudulently than the level below it.

**The specification-recursion problem [Vericoding; Goodhart 1975]:** Formal verification relocates error rather than eliminating it. A proof guarantees code-meets-spec but is silent on whether the spec captures intent. Empirically, LLMs game weak specifications into vacuous proofs (~9% of "verified" specs in the Vericoding benchmark were too weak). CCDP addresses this by requiring the `scope` field on FORMALLY_VERIFIED grades — binding the grade to a specific specification whose own provenance is separately trackable.

<a id="section-10-2"></a>
## Grade Taxonomy

Eight provenance grades are defined, ordered from weakest to strongest epistemic standing. The ordering is strict: each grade implies all guarantees of the grades below it plus additional guarantees.

**Ordering caveat.** This ordering is a *policy order* for routing and conformance, not a universal epistemic truth. The ordering holds for the protocol's primary use case — selecting services and evaluating whether a response meets a requester's quality threshold. It does not hold in all epistemic contexts: HUMAN_ATTESTED does not imply deterministic COMPUTED (a human reviewer may not have performed the computation); CROSS_CHECKED does not imply VALIDATED against an external criterion unless validation was part of each independent process. The ordering reflects the protocol's design judgment that grades higher on the ladder are harder to achieve and more expensive to fake (the Spence signaling criterion), not that every higher grade subsumes every lower grade's specific method. Consumers with domain-specific epistemic requirements SHOULD inspect the `evidence` entries rather than relying solely on grade comparison.

### Grade 0: OPAQUE

No provenance information is available. The service did not report how it produced this result, or the result's origin is unknown. This grade is assigned when:
- A service does not implement provenance reporting
- A result passes through a system boundary that strips provenance
- Legacy data is ingested without epistemic metadata

OPAQUE is not an error; it is an honest statement of ignorance. Consumers SHOULD treat OPAQUE results with maximum skepticism.

### Grade 1: ASSERTED

The service claims this result but provides no verification evidence. The result reflects the service's output as-is, with no external check.

Typical sources: raw LLM output without verification, unvalidated human opinion, unchecked database entries.

A service MUST assign ASSERTED (not a higher grade) when it has performed no verification step — even if the service is highly confident. Confidence without verification evidence is assertion.

### Grade 2: HEURISTIC

The result was produced by a method with known error characteristics — a statistical model, a heuristic algorithm, a classifier with measured precision/recall, or a fuzzy search with a relevance score. The evidence includes error bounds or confidence metrics.

Typical sources: classifier output with confidence scores, statistical estimates with error bars, pattern matching with a known false-positive rate.

The distinction from ASSERTED: a HEURISTIC result carries *quantified uncertainty*, while an ASSERTED result carries no uncertainty information. A service assigning HEURISTIC MUST include evidence entries with measurable error characteristics (e.g., `"type": "classifier-confidence", "confidence": 0.92, "false_positive_rate": 0.03`).

### Grade 3: COMPUTED

The result was deterministically computed from the inputs. Given the same inputs, any correct implementation of the same algorithm would produce the same result. The computation itself is not in question; only the correctness of the inputs is.

Typical sources: arithmetic calculations, database queries (the data is what the database contains), hash computations, sorting, compilation.

A database query result is COMPUTED relative to the database's current state. The provenance of the stored data is a separate question — if the data was loaded from an unverified source, the query result is COMPUTED (the query was executed correctly) but the underlying data may be OPAQUE or ASSERTED. The `scope` field SHOULD note "computed relative to database state as of [timestamp]" when this distinction matters.

The distinction from HEURISTIC: a COMPUTED result has no uncertainty in the computation — the potential error is in the inputs, not the processing. A database query result is COMPUTED because the query was executed correctly against the data; whether the data itself is correct is a separate provenance question.

### Grade 4: VALIDATED

The result was checked against an external criterion and found consistent. The external criterion is independent of the process that produced the result — it is not self-review.

Typical sources: code that passes a test suite, a plan accepted by an external validator, output that passes a schema check, a translation verified by back-translation.

Back-translation is validation only when the back-translation process is independent of the forward translation and the consistency criterion is formally defined. A back-translation using the same LLM with the same prompt is self-review, not validation — it SHOULD be graded HEURISTIC, not VALIDATED.

The distinction from COMPUTED: VALIDATED results have been checked by an independent verification step, not just deterministically produced. A service assigning VALIDATED MUST include evidence entries identifying the validation method and its scope (what was validated, and what was not).

**Design note (a judgment call):** Test-suite validation and formal verification are separated into different grades because they have structurally different failure modes. A test suite samples — it checks finitely many cases and says nothing about unchecked cases. A formal proof exhausts — it checks all cases within the scope of the specification. The gap between "all tested cases pass" and "all possible cases are covered" is real and load-bearing in safety-critical contexts. We acknowledge that some software engineering traditions would group these together, and that the boundary between extensive testing and lightweight formal methods (property-based testing, coverage-guided fuzzing) is blurry. The separation is a design choice favoring precision over convenience.

### Grade 5: CROSS_CHECKED

The result was independently produced by multiple services using different methods, and the results are consistent. The services did not share intermediate state, prompts, or reasoning — they arrived at the same conclusion independently. Independence has degrees. Full independence means different algorithms, different training data, different infrastructure. Partial independence (same model family but different prompts, or same algorithm with different seeds) provides weaker cross-checking. A service assigning CROSS_CHECKED MUST include evidence entries documenting the independence level: `"independence": "full"` (different methods/implementations), `"independence": "partial"` (same method family, different instances/seeds), or `"independence": "replicated"` (identical replicas — this does NOT qualify for CROSS_CHECKED and MUST be graded at the individual replica's level).

Typical sources: multiple LLMs generating the same answer without seeing each other's work, a symbolic solver and a numerical solver agreeing, independent human reviewers reaching the same conclusion.

The distinction from VALIDATED: CROSS_CHECKED results are checked not just by one external criterion but by independent *production processes*. Cross-checking detects errors that no single validation method would catch — the error would need to be shared across independent processes, which is unlikely when the processes use different algorithms or representations.

A service (or the Dispatcher, when composing results) assigning CROSS_CHECKED MUST include evidence entries identifying each independent source, confirming they did not share state, and documenting the consistency criterion.

### Grade 6: FORMALLY_VERIFIED

The result has been machine-checked against a formal specification. A proof object is available and can be independently verified by any conforming proof checker.

Typical sources: theorem prover output (Lean, Isabelle, Coq), SMT solver proofs (Z3), verified-correct-by-construction code (Dafny, Verus).

A service assigning FORMALLY_VERIFIED MUST:
- Include the `scope` field identifying the specification against which verification was performed.
- Include an evidence entry of type `"proof-object"` with an `artifact_ref` pointing to the proof.
- The proof MUST be independently checkable — a claim of "formally verified" without a checkable proof artifact is at best VALIDATED.

The proof checker, specification identifier (including version), artifact hash, and verification environment SHOULD be recorded in evidence entries to enable reproducible verification. A claim of FORMALLY_VERIFIED that cannot be independently reproduced is, for practical purposes, VALIDATED.

**The specification-recursion caveat:** FORMALLY_VERIFIED means "this result is correct *relative to this specification*." It does not mean the specification is correct. The grade is silent on whether the specification captures the intended behavior. Consumers of FORMALLY_VERIFIED results SHOULD examine the `scope` field to understand what claim is actually being made and SHOULD track the specification's own provenance separately.

This caveat is not a weakness of the grade — it is an honest statement of what formal verification can and cannot do. The alternative — a grade that claims "provably correct" without binding to a specific specification — would be misleading.

### Grade 7: HUMAN_ATTESTED

The result has been reviewed and attested by a human with domain expertise. The human's identity is recorded in the provenance chain.

Typical sources: human code review with sign-off, expert judgment, specification review, value/novelty assessment.

A service assigning HUMAN_ATTESTED MUST include evidence entries identifying the human reviewer (by a verified identifier, not a free-text name) and the scope of their attestation.

**Why HUMAN_ATTESTED is the highest grade:** This is a judgment call, and we state our reasoning explicitly. In the composite cognition architecture, the human occupies the top of the supervision tree because the human provides the faculties for which no external organ exists: specification correctness, broad abstraction, and open-ended value judgment. HUMAN_ATTESTED is highest because the specification-recursion problem terminates at human judgment — someone must decide whether the specification captures intent, and that someone is a person with domain expertise.

This does not mean human judgment is infallible. It means that within the CCDP architecture, human attestation is the terminal verification step — the point where epistemic responsibility is explicitly assigned to a named individual. The provenance chain makes this assignment visible and auditable rather than implicit.

<a id="section-10-3"></a>
## Grade Assignment Rules

A Service MUST follow these rules when assigning a Provenance Grade to a Response:

1. **Accuracy over aspiration.** Assign the grade that *accurately describes* the epistemic status of the result, not the grade the requester asked for. If the requester wanted VALIDATED but the Service could only achieve ASSERTED, the Response MUST carry grade ASSERTED (and the Service SHOULD escalate if `provenance_requirement.min_grade` was set higher).

2. **Evidence required.** A grade above ASSERTED MUST be accompanied by evidence entries that substantiate it. A grade without supporting evidence MUST NOT be assigned — the Service MUST fall back to ASSERTED.

3. **Scope binding for FORMALLY_VERIFIED.** The `scope` field is REQUIRED for FORMALLY_VERIFIED. A claim of formal verification without identifying the specification is not formally verified.

4. **Independence required for CROSS_CHECKED.** Cross-checking requires that the independent sources did not share intermediate state. If the Service cannot confirm independence, it MUST assign VALIDATED (not CROSS_CHECKED).

5. **Identity required for HUMAN_ATTESTED.** The human's identity MUST be recorded in a verifiable form. Anonymous attestation is ASSERTED, not HUMAN_ATTESTED.

6. **Monotonicity.** A Service MUST NOT assign a higher grade to a result that has less epistemic support. If a Service's verification step fails or is inconclusive, the grade reflects the actual achieved level, not the attempted level.

7. **Verifier authority.** The grade reflects the strongest verification actually performed, not the strongest verification the service is capable of performing. A service with formal verification capability that skips verification for performance reasons MUST report the grade of the method actually used. Services SHOULD include an evidence entry of type `"verification_method"` documenting what method was used and why, especially when a lower-than-maximum grade is assigned.

<a id="section-10-4"></a>
## Grade Comparison and Ordering

Grades are strictly ordered: OPAQUE < ASSERTED < HEURISTIC < COMPUTED < VALIDATED < CROSS_CHECKED < FORMALLY_VERIFIED < HUMAN_ATTESTED.

A grade *meets* a requirement if it is equal to or greater than the required grade. FORMALLY_VERIFIED meets a requirement of VALIDATED. ASSERTED does not meet a requirement of COMPUTED.

Implementations MUST use the defined ordering for all grade comparisons. The integer codes (0–7) from Section 10.2 MAY be used for programmatic comparison.

<a id="section-10-5"></a>
## Grade Composition

When a result is composed from multiple sub-results — whether through Decomposition (Section 14), chained service calls, or Mode 3 internal composition — the composed result's grade must reflect the epistemic status of the whole, not just the strongest part.

<a id="section-10-5-1"></a>
### Sequential Composition (Weakest-Link Rule)

When a result is produced by a chain of operations (A feeds into B, which feeds into C), the composed grade is the **minimum** of the component grades:

```
composed_grade = min(grade_A, grade_B, grade_C)
```

Rationale: the chain is only as strong as its weakest link. If an LLM (ASSERTED) translates a request that a prover (FORMALLY_VERIFIED) checks, the composed result is ASSERTED — the correctness of the proof depends on the correctness of the translation, which is only asserted.

**Exception — verified translation:** If the translation itself is validated (e.g., by back-translation or by the prover rejecting mistranslations), the translation step's grade is VALIDATED, and the composed grade becomes min(VALIDATED, FORMALLY_VERIFIED) = VALIDATED. The Service MUST provide evidence for the translation validation.

<a id="section-10-5-2"></a>
### Parallel Composition (Cross-Check Upgrade)

When a result is independently produced by multiple services and the results agree, the composed grade may be *upgraded* to CROSS_CHECKED, provided:

1. The services used different methods or implementations (not replicas of the same service).
2. The services did not share intermediate state.
3. The results agree according to a defined consistency criterion.

The upgrade applies only if every component grade is at least ASSERTED. OPAQUE results cannot be cross-checked.

```
if all independent results agree AND independence confirmed:
  composed_grade = max(CROSS_CHECKED, min(component_grades))
else:
  composed_grade = min(component_grades)
```

Cross-check upgrade improves confidence in agreement — it does not establish truth. If all independent sources share a common-mode error (e.g., the same incorrect training data, the same flawed specification), their agreement is meaningless. The evidence entries MUST document what was cross-checked and what common-mode risks remain.

<a id="section-10-5-3"></a>
### Decomposition Composition

When a result is assembled from sub-results via a Decomposition Plan (Section 14), the composed grade considers three factors:

1. The grade of the Decomposition Plan itself (how confident are we in the decomposition?)
2. The grades of the sub-results
3. The grade of the composition step (how confident are we in the assembly?)

```
composed_grade = min(decomposition_grade, min(sub_result_grades), composition_grade)
```

If the composition step is trivial (concatenation, simple aggregation), it may be graded COMPUTED. If it requires judgment (synthesizing sub-results into a coherent narrative), it is graded according to the method used.

<a id="section-10-5-4"></a>
### Composition Trace

The `provenance.composition_trace` field documents how a composed grade was derived:

```json
{
  "composition_trace": {
    "method": "sequential",
    "components": [
      {
        "span_id": "00f067aa0ba902b7",
        "service_id": "llm-translator-01",
        "grade": "ASSERTED",
        "role": "translation"
      },
      {
        "span_id": "5b8aa5a2d2c21ea0",
        "service_id": "z3-prover-01",
        "grade": "FORMALLY_VERIFIED",
        "role": "verification"
      }
    ],
    "composed_grade": "ASSERTED",
    "rule_applied": "weakest_link"
  }
}
```

The composition trace provides full transparency into how the final grade was derived. Consumers can inspect it to understand which component limited the overall confidence.

<a id="section-10-6"></a>
## Worked Examples [Informative]

**Example 1: When HUMAN_ATTESTED is required despite formal verification.** A legal compliance check requires that a human compliance officer reviewed and signed off on the determination. Even if a formal verifier proves the logic correct, the regulatory requirement mandates human attestation. The requester sets `min_grade: HUMAN_ATTESTED`; a FORMALLY_VERIFIED response would not satisfy the requirement.

**Example 2: When FORMALLY_VERIFIED is required despite human attestation.** A cryptographic protocol implementation requires machine-checkable correctness proofs. A human expert's review (HUMAN_ATTESTED) provides confidence but not the reproducible, automated verification the deployment requires. The requester sets `min_grade: FORMALLY_VERIFIED`.

These examples illustrate why the grade ordering is a policy order, not a universal epistemic hierarchy — and why consumers with specific needs should inspect evidence entries.

<a id="section-10-7"></a>
## Provenance in the Audit Trail

Every Response's provenance is recorded in the audit trail (Section 11). The audit system records:

- The grade assigned by the Service
- The evidence entries
- The composition trace (if composed)
- Whether the grade met the Request's `provenance_requirement`
- If the grade did not meet the requirement, whether an Escalation was triggered

This enables retrospective provenance analysis: given any past result, the audit trail shows exactly what evidence supported it, how it was derived, and whether it met the requester's expectations.

Audit records store provenance summaries (grade, evidence types, service IDs) rather than full evidence artifacts. For retrospective verification, the audit record MUST include artifact references (URIs with integrity hashes) that allow independent retrieval and verification of the evidence. If durable evidence retention is required, deployments MUST configure an artifact store with appropriate retention policies. The audit record's artifact references MUST remain resolvable for the configured retention period.

<a id="section-10-8"></a>
## Provenance and Trust

A provenance grade is a *claim by the service about its own output*. The grade is only as trustworthy as the service that assigned it. A compromised or misconfigured service could assign FORMALLY_VERIFIED to unverified output.

CCDP mitigates this through three mechanisms:

1. **Evidence as checkable claims.** Evidence entries (especially `artifact_ref` entries pointing to proof objects or test results) are independently checkable. A grade of FORMALLY_VERIFIED with a proof-object reference can be verified by any conforming proof checker — the grade is not trusted on authority alone.

2. **Audit trail correlation.** The audit system records which service assigned which grade. Patterns of grade inflation (a service consistently assigning grades higher than its `provenance_capabilities.typical_grade`) can be detected and flagged.

3. **Provenance auditing service.** Deployments SHOULD include a provenance auditing service — a Service whose capability type is `org.ccdp.verification` — that spot-checks provenance claims by re-verifying evidence. This is the supply-chain inspection model applied to cognitive provenance.

The trust model is not that services are assumed honest. The trust model is that provenance claims are structured, checkable, and auditable — and that dishonest claims are detectable through the audit trail and independent verification.

<a id="section-11"></a>
# Audit Trail

<a id="section-11-1"></a>
## Audit as Core Protocol

Audit records carry an `audit_schema_version` field (string, REQUIRED) independent of the CCDP document version and wire protocol version. The current audit schema version is `"1.0"`. Changes to audit record structure increment this version. Audit consumers MUST check `audit_schema_version` and handle unknown versions gracefully (log a warning and preserve the record without interpretation).

Audit is not an extension, an integration, or a best practice. It is a REQUIRED protocol behavior. Every Message that passes through the Dispatcher MUST generate a structured audit record. This requirement is grounded in a practical lesson: the NSA/CISA assessment of MCP found that protocols without mandatory audit leave security and reliability to "implementation discipline" — which fails unpredictably across deployments.

In the supervision-tree model, the audit trail is the equivalent of Erlang/OTP's error logger — the mechanism by which failures, routing decisions, and system behavior become visible to the supervisor (ultimately, the human). Without it, the human cannot supervise.

<a id="section-11-2"></a>
## Audit Record Structure

An audit record is generated for every Message that the Dispatcher processes. The record is a structured JSON object with the following fields:

```json
{
  "audit_record": {
    "record_id": "audit-550e8400-e29b-41d4-a716-446655440000",
    "timestamp": "2026-08-03T14:30:00.145Z",

    "trace_context": {
      "trace_id": "4bf92f3577b34da6a3ce929d0e0e4736",
      "span_id": "00f067aa0ba902b7",
      "parent_span_id": null
    },

    "message_summary": {
      "type": "REQUEST",
      "request_id": "550e8400-e29b-41d4-a716-446655440000",
      "capability_type": "org.ccdp.deduction",
      "source_id": "client-app-01",
      "destination_id": "z3-prover-01",
      "priority": "NORMAL"
    },

    "routing": {
      "decision": "lowest_cost_healthy",
      "candidates_considered": 3,
      "candidates_filtered": {
        "health": 0,
        "deadline": 1,
        "provenance": 0
      },
      "selected_service": "z3-prover-01",
      "registry_source": "live",
      "registry_query_ms": 12
    },

    "validation": {
      "envelope_valid": true,
      "content_schema_valid": true,
      "schema_version": "v2",
      "authentication_verified": true,
      "authorization_verified": true
    },

    "timing": {
      "received_at": "2026-08-03T14:30:00.123Z",
      "validated_at": "2026-08-03T14:30:00.130Z",
      "routed_at": "2026-08-03T14:30:00.145Z",
      "dispatcher_overhead_ms": 22
    },

    "constraints": {
      "deadline": "2026-08-03T14:31:00.000Z",
      "remaining_budget_ms": 59877,
      "cost_budget": { "max_monetary_units": 0.50, "monetary_unit": "USD" },
      "provenance_requirement": { "min_grade": "VALIDATED" }
    },

    "dispatcher_id": "dispatcher-prod-01",
    "ccdp_version": "1.0"
  }
}
```

<a id="section-11-2-1"></a>
### Response Audit Records

When the Dispatcher receives a Response from a Service and forwards it to the requester, a second audit record is generated:

```json
{
  "audit_record": {
    "record_id": "audit-resp-550e8400-...",
    "timestamp": "2026-08-03T14:30:04.850Z",

    "trace_context": { /* ... */ },

    "message_summary": {
      "type": "RESPONSE",
      "request_id": "550e8400-e29b-41d4-a716-446655440000",
      "status": "SUCCESS",
      "source_id": "z3-prover-01",
      "destination_id": "client-app-01"
    },

    "provenance_summary": {
      "grade": "FORMALLY_VERIFIED",
      "evidence_count": 1,
      "evidence_types": ["proof-object"],
      "scope": "Formula satisfiability in QF_LIA",
      "grade_meets_requirement": true,
      "composition_method": null
    },

    "resource_consumption": {
      "service_compute_seconds": 4.7,
      "service_tokens_consumed": null,
      "total_latency_ms": 4727,
      "cost_budget_remaining": { "monetary_units": 0.499, "monetary_unit": "USD" }
    },

    "validation": {
      "output_schema_valid": true,
      "provenance_present": true,
      "provenance_grade_valid": true
    },

    "timing": {
      "service_invoked_at": "2026-08-03T14:30:00.145Z",
      "response_received_at": "2026-08-03T14:30:04.840Z",
      "response_forwarded_at": "2026-08-03T14:30:04.850Z",
      "service_latency_ms": 4695,
      "dispatcher_overhead_ms": 32
    },

    "dispatcher_id": "dispatcher-prod-01",
    "ccdp_version": "1.0"
  }
}
```

<a id="section-11-2-2"></a>
### Escalation Audit Records

Escalation audit records include the escalation context and the routing chain:

```json
{
  "audit_record": {
    // ... standard fields ...
    "message_summary": {
      "type": "ESCALATION",
      "request_id": "550e8400-...",
      "source_id": "llm-verifier-01",
      "escalation_reason": "CONFIDENCE_BELOW_THRESHOLD",
      "achieved_grade": "HEURISTIC",
      "requested_grade": "VALIDATED"
    },
    "escalation_routing": {
      "original_service": "llm-verifier-01",
      "escalation_chain_position": 1,
      "next_target": "z3-prover-01",
      "chain_remaining": ["z3-prover-01", "human-review-math-01"],
      "partial_result_forwarded": true
    }
  }
}
```

<a id="section-11-3"></a>
## Trace Context Propagation

CCDP uses W3C Trace Context [W3C-TC] for distributed tracing. The `trace_id` and `span_id` fields in the CCDP envelope map directly to the W3C `traceparent` header fields:

```
traceparent: 00-{trace_id}-{span_id}-{trace_flags}
```

The Dispatcher MUST:

1. Propagate `trace_id` unchanged through all Messages in the same request chain.
2. Generate a new `span_id` for each hop through the Dispatcher.
3. Set `parent_span_id` on forwarded messages to the incoming message's `span_id`.
4. Include the W3C `traceparent` header on HTTP requests to Services.
5. Preserve the `tracestate` header if present, appending a CCDP-specific entry: `ccdp=dispatcher_id`. The Dispatcher appends `ccdp=<dispatcher_id>` to the `tracestate` header. If the `tracestate` header would exceed 512 bytes after appending, the Dispatcher MUST truncate the oldest entries (leftmost) to make room, per W3C Trace Context [W3C-TC] §3.3.2.1. The Dispatcher MUST sanitize `tracestate` values: strip control characters and validate against the W3C tracestate grammar before forwarding.

This ensures that CCDP traces are compatible with standard distributed tracing infrastructure (OpenTelemetry, Jaeger, Zipkin). Services that use tracing internally can link their internal spans to the CCDP trace.

<a id="section-11-4"></a>
## Mandatory Audit Fields

The following audit data MUST be recorded for every Message processed by the Dispatcher. Implementations MUST NOT make any of these fields optional or configurable:

| Category | Fields | When recorded |
|----------|--------|---------------|
| Identity | `record_id`, `trace_id`, `span_id`, `parent_span_id`, `request_id` | Every message |
| Message | `type`, `capability_type`, `source_id`, `destination_id` | Every message |
| Routing | `decision`, `selected_service`, `candidates_considered`, `registry_source` | Requests and escalations |
| Validation | `envelope_valid`, `content_schema_valid`, `authentication_verified` | Every message |
| Timing | `received_at`, `routed_at`, `dispatcher_overhead_ms` | Every message |
| Constraints | `deadline`, `remaining_budget_ms` | Requests |
| Provenance | `grade`, `grade_meets_requirement` | Responses and escalations |
| Resources | `service_latency_ms`, `cost_budget_remaining` | Responses |
| Errors | `error_code`, `error_detail`, `retry_count` | Errors and retries |
| Dispatcher | `dispatcher_id`, `ccdp_version` | Every message |

**Per-message-type requirements.** Not all audit fields are meaningful for every message type. The following matrix defines which fields are REQUIRED (R), RECOMMENDED (S), or not applicable (—) for each message type:

| Field | REQUEST | RESPONSE | ESCALATION | NOTIFICATION | HEALTH_REQ | HEALTH_RESP | DECOMP_RESULT |
|---|---|---|---|---|---|---|---|
| `trace_id` | R | R | R | R | R | R | R |
| `span_id` | R | R | R | R | R | R | R |
| `request_id` | R | R | R | S | R | R | R |
| `capability_type` | R | S | S | S | — | — | R |
| `destination_id` | S | — | S | S | R | — | — |
| `source_id` | R | R | R | R | R | R | R |
| `routing_decision` | R | — | R | — | — | — | R |
| `provenance_summary` | — | R | R | — | — | — | S |
| `schema_validation` | R | S | — | — | — | — | R |
| `health_status` | — | — | — | — | — | R | — |

<a id="section-11-5"></a>
## Audit Storage and Retention

This specification does not mandate a specific audit storage mechanism. Implementations MAY use structured log files, a database, an event stream (e.g., Kafka), or any other storage that satisfies these requirements:

1. **Immutability.** Audit records, once written, MUST NOT be modified or deleted during the retention period. Append-only storage is RECOMMENDED.
2. **Queryability.** The audit store MUST support queries by `trace_id` (retrieve all records for a request chain), `request_id` (retrieve records for a specific request), `service_id` (retrieve records for a specific service), and time range.
3. **Retention.** Audit records MUST be retained for a minimum period configured per deployment. The RECOMMENDED minimum retention period is 90 days for production deployments.
4. **Integrity.** Audit records MUST be written to a tamper-evident store for CCDP Full conformance. CCDP Core conformance REQUIRES structured audit records but permits deployment-configured integrity mechanisms. For Full conformance, tamper evidence means either cryptographic chaining (each record includes a hash of the previous record), append-only storage with integrity verification, or a write-once medium. The specific mechanism is deployment-defined.

<a id="section-11-6"></a>
## Audit Store Failure Behavior

If the audit store is unavailable, the Dispatcher MUST follow its deployment-configured `audit_failure_policy`:

- **`fail_closed`** (RECOMMENDED for production): The Dispatcher MUST reject incoming requests with error `-32603` (internal error) and `data.reason` of `"audit_unavailable"` until the audit store recovers. No messages are processed without audit.
- **`buffer`**: The Dispatcher buffers audit records locally (in memory or on local disk) and continues processing messages. Buffered records MUST be flushed to the audit store when it recovers. The buffer MUST have a bounded size; when the buffer is full, the Dispatcher falls back to `fail_closed`.
- **`degrade`**: The Dispatcher continues processing messages without audit. This mode MUST NOT be used in production deployments. If used, the Dispatcher MUST set a metadata flag `org.ccdp.audit_gap: true` on all messages processed during the gap, and MUST log the gap duration and message count when the audit store recovers.

The audit failure policy MUST be declared in the Dispatcher's deployment configuration and MUST be discoverable via the Dispatcher's own health endpoint.

<a id="section-11-7"></a>
## Audit as Supervision Input

The audit trail is not just a compliance mechanism — it is the Human Supervisor's primary input for understanding system behavior. Deployments SHOULD provide tooling that enables:

- **Request tracing:** Given a `trace_id`, reconstruct the full journey of a request — every routing decision, every service invocation, every escalation, every provenance grade.
- **Provenance verification:** Given a Response, verify its provenance chain by re-checking evidence entries against the audit trail.
- **Performance analysis:** Identify latency bottlenecks, cost outliers, and routing inefficiencies from audit timing data.
- **Health monitoring:** Detect Service degradation patterns from audit error and escalation data.
- **Grade distribution analysis:** Monitor the distribution of provenance grades over time to detect grade inflation, systematic under-verification, or changes in service quality.

This tooling is outside the scope of this specification but is essential for the supervision-tree architecture to function. The audit trail provides the data; the tooling makes it actionable.

<a id="section-12"></a>
# Flow Control and Resource Signals

<a id="section-12-1"></a>
## The Resource Problem

Cognitive services have wildly heterogeneous resource characteristics. An LLM inference may cost $0.50 and take 10 seconds. A Z3 solver may cost $0.001 and take 500 milliseconds — or 30 minutes for a hard problem. A human review may cost $50 and take 2 days. A classifier may cost $0.0001 and take 20 milliseconds.

Without resource signals, the Dispatcher cannot make resource-rational decisions. TCP solved this problem with congestion control — window advertisements, ECN, slow start, AIMD. CCDP solves it with explicit resource signals at the protocol level: cost budgets on requests, resource consumption on responses, and capacity advertisements from services.

<a id="section-12-2"></a>
## Cost Budgets

A Request MAY carry a `cost_budget` field constraining the resources the Service may consume (Section 7.3.2). The cost budget is an envelope field, readable by the Dispatcher without Content inspection.

<a id="section-12-2-1"></a>
### Budget Fields

```json
{
  "cost_budget": {
    "max_compute_seconds": 120,
    "max_tokens": 50000,
    "max_monetary_cost": "0.50",
    "monetary_unit": "USD"
  }
}
```

All fields are OPTIONAL. Omitted fields indicate no constraint on that dimension. Monetary values are strings to avoid IEEE 754 floating-point precision issues (Section 2.3). Implementations MUST parse monetary strings as decimal values, not floating-point. A Service MUST NOT exceed any specified constraint. Services SHOULD implement preflight estimation where feasible — estimating resource consumption before beginning work and returning an Escalation with reason `BUDGET_EXCEEDED` if the estimate exceeds the budget. For services where cost is unpredictable (LLM generation with variable output length), the Service MUST monitor consumption during execution and abort with an Escalation if any budget limit is reached. If a Service would exceed a constraint to produce a meaningful result, it MUST return an Escalation with reason `BUDGET_EXCEEDED`, reporting the resources consumed so far and an estimate of resources needed.

When escalation reason is `BUDGET_EXCEEDED`, the `escalation` object MUST include:

```json
"budget_exceeded": {
  "dimension": "monetary" | "compute_seconds" | "tokens",
  "budget_limit": "4.50",
  "actual_or_estimated": "2.80",
  "is_estimate": true
}
```

The `detail` field MAY contain a human-readable explanation in addition to the structured fields.

<a id="section-12-2-2"></a>
### Budget Propagation

When the Dispatcher routes a Request, it MAY adjust the cost budget based on routing overhead:

- `max_compute_seconds`: No adjustment (this constrains the Service, not the Dispatcher).
- `max_monetary_cost`: The Dispatcher MAY subtract its own routing cost (if any) before forwarding.
- `max_tokens`: No adjustment (this constrains token-consuming services).

For Decomposition (Section 14), the Dispatcher partitions the parent Request's cost budget across sub-requests according to the Decomposition Plan's budget allocation. If the plan does not specify allocation, the Dispatcher SHOULD divide the budget equally among sub-requests, reserving a configurable fraction (RECOMMENDED: 10%) for composition overhead. Equal allocation is a safe default but ignores DAG shape, service cost hints, critical-path length, and task heterogeneity. Decomposition Plans SHOULD include per-sub-request `cost_fraction` and `deadline_fraction` allocations (Section 14.3.1) that reflect the expected cost profile. When allocations are not specified, the Dispatcher MUST use equal partitioning and log a warning in the audit trail.

<a id="section-12-2-3"></a>
### Budget Consumption Reporting

Every Response MUST report actual resource consumption in the `provenance.computation` field:

```json
{
  "computation": {
    "tokens_consumed": 12500,
    "compute_seconds": 4.7,
    "monetary_cost": "0.003",
    "monetary_unit": "USD",
    "model_id": "claude-opus-4-20260801"
  }
}
```

The Dispatcher records these figures in the audit trail. Over time, the audit data enables increasingly accurate cost estimation for routing decisions.

<a id="section-12-3"></a>
## Capacity Advertisements

Services advertise their current capacity through Health responses (Section 7.3.6). Capacity signals enable the Dispatcher to route away from overloaded services before they fail.

<a id="section-12-3-1"></a>
### Capacity Fields

```json
{
  "capacity": {
    "max_concurrent_requests": 10,
    "current_concurrent_requests": 7,
    "queue_depth": 3,
    "estimated_drain_time_ms": 15000
  }
}
```

**`max_concurrent_requests`** (integer): The maximum number of requests the Service can process simultaneously.

**`current_concurrent_requests`** (integer): How many requests the Service is currently processing.

**`queue_depth`** (integer): How many requests are queued but not yet processing.

**`estimated_drain_time_ms`** (integer): Estimated time to clear the current queue at current processing rates.

<a id="section-12-3-2"></a>
### Per-Capability Load

For Services implementing multiple Capability Types, the Health response provides per-capability load information:

```json
{
  "capabilities": {
    "org.ccdp.deduction": {
      "available": true,
      "current_load": 0.70,
      "queue_depth": 2,
      "estimated_latency_ms": 8000
    },
    "org.ccdp.verification": {
      "available": false,
      "current_load": 1.0,
      "queue_depth": 5,
      "estimated_latency_ms": 30000
    }
  }
}
```

A `current_load` of 1.0 indicates the Service is at capacity for that capability. A `current_load` above 0.8 SHOULD trigger the Dispatcher to prefer alternative Services.

Capacity data in health responses is a point-in-time snapshot. The Dispatcher MUST record the timestamp of each capacity update and SHOULD treat capacity data older than the Service's `health_check.interval_seconds` as stale. For high-priority or high-cost requests, the Dispatcher SHOULD perform a synchronous health probe before routing if the cached capacity data is stale. Stale capacity data used for a routing decision MUST be noted in the audit record.

<a id="section-12-4"></a>
## Deadline Propagation

Deadlines prevent unbounded latency in multi-hop request chains. The deadline mechanism is modeled on gRPC's deadline propagation [gRPC deadline] and Google's `context.Context`.

<a id="section-12-4-1"></a>
### Deadline Mechanics

Every Request carries a `deadline` (absolute UTC timestamp) and `remaining_budget_ms` (remaining time budget in milliseconds). At each hop through the Dispatcher:

1. The Dispatcher computes `elapsed_ms = now() - audit.received_at` (its own receive timestamp — see the clock-skew note below).
2. The Dispatcher sets `remaining_budget_ms = envelope.remaining_budget_ms - elapsed_ms`.
3. If `remaining_budget_ms <= 0`, the Dispatcher returns error `-32007` (deadline exceeded) without forwarding the Request.
4. If `remaining_budget_ms` is positive but less than the target Service's `cost_hints.estimated_latency_ms.p50`, the Dispatcher logs a warning and either forwards (optimistically) or returns error `-32004` (deadline not achievable).

**Relationship to the routing deadline filter.** The deadline filter in Section 9.2 Step 4 uses the Service's p95 estimated latency as the feasibility threshold: if `remaining_budget_ms < p95_latency_ms`, the service is filtered out of candidacy entirely. This step's p50 check applies to a Service that already survived that filter — it is re-evaluating margin at actual dispatch time, after further elapsed time has accrued hop-by-hop since the routing decision was made. Section 12.4.1 permits optimistic forwarding when remaining time has degraded below the Service's p50 but has not yet fallen below p95, on the grounds that the request may still succeed. These two rules are consistent: the routing filter removes candidates that almost certainly cannot meet the deadline (below p95), while flow control allows the best remaining candidate to attempt the request even with tight margins (between p50 and p95).

**Clock skew.** The Dispatcher MUST compute `remaining_budget_ms` from its own receive timestamp (`audit.received_at`), not from the originator's `envelope.timestamp`. The originator's timestamp is used for replay protection and freshness validation (Section 15.5), not for hop-by-hop deadline accounting. This avoids clock-skew errors between the originator and the Dispatcher.

<a id="section-12-4-2"></a>
### Service Deadline Behavior

A Service that receives a Request with `remaining_budget_ms` SHOULD:

1. Check whether it can plausibly complete within the budget.
2. If not, return an Escalation with reason `DEADLINE_INSUFFICIENT` immediately, rather than starting work it cannot finish.
3. If it starts work and approaches the deadline, return a partial result (if possible) with Escalation reason `DEADLINE_APPROACHING` and `partial_result_available: true`.
4. Never exceed the deadline silently — either complete in time, escalate, or error.

<a id="section-12-4-3"></a>
### Decomposition and Deadlines

For decomposed requests, the Dispatcher allocates the parent's deadline budget across sub-requests:

- Sequential sub-requests share the remaining budget serially — each sub-request gets the remaining budget after previous sub-requests complete.
- Parallel sub-requests share the remaining budget — each parallel sub-request gets the same `remaining_budget_ms` (they all must complete before the parent's deadline).
- The Decomposition Plan MAY specify per-sub-request time allocations that override the default allocation.

<a id="section-12-5"></a>
## Back-Pressure

When a Service is overloaded, it needs a way to signal the Dispatcher to slow down. CCDP supports back-pressure through three mechanisms:

<a id="section-12-5-1"></a>
### Health-Based Back-Pressure

The primary back-pressure mechanism. When a Service's `health.status` transitions to DEGRADED, the Dispatcher deprioritizes it in routing (Section 9.6). When it transitions to UNHEALTHY, the Dispatcher stops routing to it entirely.

This is the "let it crash" principle: a Service under unsustainable load declares itself degraded, and the Dispatcher routes around it rather than continuing to add load.

<a id="section-12-5-2"></a>
### HTTP 429 (Too Many Requests)

A Service MAY respond to a CCDP Request with HTTP 429 instead of a CCDP Response. The `Retry-After` header (in seconds) tells the Dispatcher when to retry. The Dispatcher:

1. MUST NOT retry before the `Retry-After` period.
2. SHOULD route to an alternative Service if one is available.
3. MUST log the 429 response in the audit trail.
4. SHOULD increment the Service's failure count in the circuit breaker.

More precisely: when a Service returns HTTP 429 (Too Many Requests) instead of a CCDP Response, the Dispatcher MUST: (a) log the 429 in the audit trail as a rate-limit event with the Service's `Retry-After` header value if present, (b) treat the Service as temporarily at capacity (equivalent to health status DEGRADED for the requested capability), (c) follow the retry/reroute strategy in Section 13.5.1, and (d) if the Dispatcher itself rate-limits a requester, it MUST return a CCDP error response with code `-32014` (rate limited) and include the `Retry-After` value in the error `data` field. Error `-32003` is reserved for all-services-unhealthy conditions (Section 9.2 Step 3); it is distinct from Dispatcher-side rate limiting. HTTP 429 MUST NOT be passed through to the requester as a raw HTTP response.

<a id="section-12-5-3"></a>
### Capacity-Based Rate Limiting

The Dispatcher MAY implement rate limiting per Service based on capacity advertisements. If a Service reports `current_load > 0.9`, the Dispatcher SHOULD limit new requests to that Service to no more than one per `estimated_latency_ms` period, allowing the queue to drain.

The specific rate-limiting algorithm is implementation-defined. The Dispatcher MUST log all rate-limiting decisions in the audit trail.

<a id="section-12-6"></a>
## Resource-Aware Routing

The Dispatcher uses resource signals for routing decisions (Section 9.2, Step 6). The interaction between resource signals and routing:

- **Cost budget constrains candidates:** A Request with `max_monetary_cost: "0.10"` eliminates Services with `estimated_cost_per_request > "0.10"` (compared as decimal values, not floating-point).
- **Deadline constrains candidates:** A Request with 5 seconds remaining eliminates Services with `estimated_latency_ms.p95 > 5000`.
- **Load influences ranking:** Among eligible candidates, lower-load Services are preferred.
- **Cost influences ranking:** Among eligible candidates, lower-cost Services are preferred (unless a higher-cost Service offers a better provenance grade that the Request requires).

This produces a natural resource-rational routing behavior: cheap, fast, lightly-loaded Services are preferred, with expensive or slow Services used only when cheaper alternatives are unavailable, unhealthy, or insufficient for the requested provenance level.

<a id="section-12-7"></a>
## Bullwhip Effect Warning

The operations research literature documents the "bullwhip effect" [Lee, Padmanabhan & Whang 1997]: in serial supply chains, demand variance amplifies upstream — a small fluctuation at the consumer end creates violent oscillations at the supplier end.

In CCDP, the analog is error amplification across serial cognitive operations. A small uncertainty in Decomposition can produce large errors in downstream sub-results, which compound when composed. The protocol does not solve this problem directly — it is a content-level concern, not a protocol-level one — but it provides the tools for detecting it:

- The composition trace (Section 10.5.4) makes the propagation path visible.
- Provenance grades on each sub-result quantify uncertainty at each stage.
- The audit trail records the full decomposition and composition chain.

Deployments SHOULD monitor for bullwhip patterns: systematically decreasing provenance grades in downstream sub-requests, or decomposition chains where the composed grade is consistently much lower than any individual sub-result grade.

<a id="section-13"></a>
# Error Handling and Escalation

<a id="section-13-1"></a>
## Error Philosophy

CCDP distinguishes three categories of failure, each with different protocol behavior:

1. **Protocol errors** — the message is malformed, the route is invalid, the authentication fails. These are dispatcher-detected and produce immediate error responses. They never reach a Service.

2. **Service errors** — the Service itself fails: crashes, times out, returns garbage. These are infrastructure failures. The Dispatcher retries, reroutes, or errors.

3. **Epistemic insufficiency** — the Service operates correctly but cannot meet the Request's epistemic requirements: the achieved provenance grade is below threshold, capability is exceeded, or the search space is exhausted without a determination. These are *not errors*. They are Escalations — structured routing events that the Dispatcher handles as normal protocol operations.

The distinction between service errors and epistemic insufficiency is load-bearing. An HTTP 500 means something broke. An Escalation with reason `CONFIDENCE_BELOW_THRESHOLD` means the Service worked correctly and honestly reported that its best output does not meet the standard. The protocol handles these differently: errors trigger retries and circuit breakers; escalations trigger the Escalation Chain.

This is the "let it crash" principle applied to cognitive systems: a Service that cannot meet the standard *should* escalate rather than silently producing low-quality output that poisons everything built on it.

<a id="section-13-2"></a>
## Protocol Error Codes

Protocol errors are returned as JSON-RPC 2.0 error responses. CCDP defines the following error codes in addition to the standard JSON-RPC error codes:

| Code | Name | Meaning |
|------|------|---------|
| `-32700` | Parse error | Invalid JSON |
| `-32600` | Invalid request | Not a valid JSON-RPC request or unrecognized CCDP message type |
| `-32601` | Method not found | Unrecognized CCDP method |
| `-32602` | Invalid params | Malformed CCDP envelope (missing required fields, invalid types) |
| `-32603` | Internal error | Dispatcher internal error |
| `-32001` | Service unavailable | Explicit destination Service is not registered, not ACTIVE, or not healthy |
| `-32002` | No service for capability | No Service registered for the requested Capability Type |
| `-32003` | All services unhealthy | All Services for the Capability Type are unhealthy |
| `-32004` | Deadline not achievable | No Service can plausibly respond within the remaining deadline |
| `-32005` | Provenance not achievable | No Service can meet the requested provenance grade |
| `-32006` | Escalation chain exhausted | All targets in the Escalation Chain have been tried and failed or escalated |
| `-32007` | Deadline exceeded | The deadline has passed before the Request could be processed |
| `-32008` | Authentication failed | The sender's identity could not be verified |
| `-32009` | Authorization denied | The sender is authenticated but not authorized for this Capability Type |
| `-32010` | Schema validation failed | The Content does not conform to the Capability Record's input or output schema |
| `-32011` | Replay detected | A message with this `request_id` and a different payload has already been processed |
| `-32012` | Decomposition depth exceeded | Maximum recursive decomposition depth reached (Section 14.6) |

Error responses include structured detail:

```json
{
  "jsonrpc": "2.0",
  "id": "550e8400-...",
  "error": {
    "code": -32010,
    "message": "Schema validation failed",
    "data": {
      "validation_errors": [
        {
          "path": "$.content.body.formula",
          "message": "required field missing",
          "schema_ref": "org.ccdp.deduction/input/v2"
        }
      ],
      "trace_id": "4bf92f3577b34da6a3ce929d0e0e4736",
      "dispatcher_id": "dispatcher-prod-01"
    }
  }
}
```

All protocol errors MUST be logged in the audit trail.

<a id="section-13-3"></a>
## Escalation Reasons

Escalation is a first-class message type, not an error. The following escalation reasons are defined:

| Reason | Meaning | Typical Next Step |
|--------|---------|-------------------|
| `CONFIDENCE_BELOW_THRESHOLD` | Service produced a result but at a lower provenance grade than requested | Route to higher-capability Service or human |
| `CAPABILITY_EXCEEDED` | The request exceeds the Service's capability (too complex, wrong domain) | Route to different Service with broader capability |
| `DEADLINE_INSUFFICIENT` | Remaining deadline budget is insufficient for this Service to complete | Route to faster Service or return partial result |
| `DEADLINE_APPROACHING` | Service started work but cannot finish before deadline; partial result available | Forward partial result; route remainder to faster Service |
| `BUDGET_EXCEEDED` | The request would exceed the cost budget | Route to cheaper Service or request budget increase |
| `SEARCH_EXHAUSTED` | The Service has explored its search space without finding a solution and cannot determine whether the problem is solvable. This is distinct from a proven-unsolvable result (which is a RESPONSE, not an Escalation). | Route to a Service with a larger search budget or different method, or to a human |
| `AMBIGUOUS_INPUT` | The input is ambiguous and the Service cannot safely interpret it | Route to human for clarification, or to an LLM for disambiguation |
| `INTERNAL_DEGRADATION` | The Service is experiencing internal degradation and prefers not to handle this request | Route to alternative Service |
| `REQUIRES_HUMAN` | The Service explicitly requests human involvement (e.g., for specification review) | Route to human review queue |

**Design note on SEARCH_EXHAUSTED:** A proven-unsolvable result is information, not failure. If a theorem prover determines that a formula is unsatisfiable, that is a correct, valuable result — it should be returned as a RESPONSE with grade FORMALLY_VERIFIED, not as an Escalation. An Escalation with reason SEARCH_EXHAUSTED is appropriate when the Service *cannot determine* whether the problem is solvable (e.g., the search space is too large) and is returning the problem rather than a result.

Implementations MAY define additional escalation reasons using reverse-domain notation (e.g., `com.example.custom_reason`).

<a id="section-13-4"></a>
## Escalation Chain Processing

When the Dispatcher receives an Escalation, it processes the Escalation Chain:

```
┌───────────┐    Escalation   ┌───────────┐    Escalation  ┌──────────┐
│ Service A │────────────────▶│ Service B │───────────────▶│  Human   │
│  (LLM)    │  CONFIDENCE_    │ (Prover)  │  CAPABILITY_   │  Queue   │
│           │  BELOW_THRESH.  │           │  EXCEEDED      │          │
└───────────┘                 └───────────┘                └──────────┘
      ▲                             ▲                            ▲
      │         Dispatcher          │        Dispatcher          │
      │         routes to           │        routes to           │
      │         next in chain       │        next in chain       │
```

The algorithm:

1. Receive Escalation from Service A.
2. Log the Escalation in the audit trail with full context.
3. If `escalation.suggested_target` is set and the target is healthy, route to it.
4. Otherwise, walk Service A's `escalation_chain` in order.
5. For each chain target:
   a. If the target is a Service ID, check health and route if healthy.
   b. If the target is a Capability Type, query the Registry and route per normal routing (Section 9.2).
   c. If the target has already been tried for this `request_id` (cycle detection), skip it.
   d. Verify the requester is authorized for the target's Capability Type (or the token scope covers it).
   e. Verify the remaining cost budget is sufficient for the target's cost hints.
   f. Verify the target can meet the request's data-class/isolation requirements (from Registry metadata).
   g. If any check fails, skip the target and continue to the next in the chain. Log the skip reason in the audit trail.
6. If all chain targets are exhausted, route to `org.ccdp.human_review` as the terminal target.
7. If no human review Service is available, return error `-32006`.

The Dispatcher MUST forward the original Request (not the Escalation) to the next target in the chain. The Dispatcher accumulates partial results from prior escalation targets in the forwarded Request's metadata under `org.ccdp.partial_results`. The most recent escalating Service's partial result is in that Service's ESCALATION message Content (the canonical location per Section 7.3.4). The metadata accumulation provides downstream Services and human reviewers with the full escalation history.

<a id="section-13-4-1"></a>
### Escalation Metadata Accumulation

As a Request traverses the Escalation Chain, the Dispatcher accumulates escalation history in the Request's metadata:

```json
{
  "metadata": {
    "org.ccdp.escalation_history": [
      {
        "service_id": "llm-verifier-01",
        "reason": "CONFIDENCE_BELOW_THRESHOLD",
        "achieved_grade": "HEURISTIC",
        "timestamp": "2026-08-03T14:30:05.000Z"
      },
      {
        "service_id": "z3-prover-01",
        "reason": "CAPABILITY_EXCEEDED",
        "detail": "Formula exceeds solver timeout",
        "timestamp": "2026-08-03T14:30:35.000Z"
      }
    ],
    "org.ccdp.partial_results": [
      {
        "service_id": "llm-verifier-01",
        "provenance": { "grade": "HEURISTIC" },
        "content": { /* ... */ }
      }
    ]
  }
}
```

This history enables downstream Services (and the Human Supervisor) to understand what has already been tried and what partial results are available.

<a id="section-13-5"></a>
## Service Error Handling

When a Service fails (as opposed to escalating), the Dispatcher follows a retry-and-reroute strategy:

<a id="section-13-5-1"></a>
### Transient Failures

Network errors, HTTP 5xx responses, and timeouts are treated as transient failures:

1. **Retry** the same Service if `remaining_budget_ms` permits, using exponential backoff (RECOMMENDED: initial delay 100ms, multiplier 2, max 3 retries).
2. **Reroute** to an alternative Service if one is available and the retry budget is exhausted.
3. **Error** if no alternative is available and retries are exhausted.

Each retry and reroute is logged in the audit trail.

<a id="section-13-5-2"></a>
### Permanent Failures

A Service that returns a CCDP error response (a JSON-RPC error with a CCDP error code) is treated as a permanent failure for this Request:

1. Do NOT retry the same Service for this Request.
2. Reroute to an alternative Service if the error suggests it (e.g., `-32010` schema validation failed may succeed with a different Service version). Rerouting after schema validation failure is appropriate only when the alternative Service supports a compatible schema version. The Dispatcher SHOULD check schema version compatibility in the Registry before rerouting, rather than blindly forwarding to another Service.
3. Error if no alternative is available.

<a id="section-13-5-3"></a>
### Malformed Responses

If a Service returns a response that is valid JSON-RPC but invalid CCDP (missing required envelope fields, missing provenance, content does not match output schema), the Dispatcher:

1. Logs the malformed response in the audit trail with full detail.
2. Treats it as a service error and follows the retry/reroute strategy.
3. Increments the Service's failure count in the circuit breaker.
4. Does NOT forward the malformed response to the requester.

<a id="section-13-6"></a>
## Health Monitoring and Circuit Breakers

<a id="section-13-6-1"></a>
### Health Check Protocol

The Dispatcher probes each Service's health at the interval specified in the Service's Capability Record (`health_check.interval_seconds`). Health checks use the `ccdp/health.request` and `ccdp/health.response` message types (Section 7.3.6).

A health check probe:
1. Sends a HEALTH_REQUEST to the Service's health endpoint.
2. Waits for a HEALTH_RESPONSE within `health_check.timeout_ms`.
3. If no response within the timeout, marks the Service as UNHEALTHY.
4. If a response arrives, updates the Service's Health Status, capacity, and per-capability load in the Routing Table.

<a id="section-13-6-2"></a>
### Health and Circuit Breaker State Transitions

The Dispatcher tracks two related but distinct state machines for each Service: the Service's **Health Status** (HEALTHY, DEGRADED, UNHEALTHY) as reported by the Service itself, and the **circuit breaker state** (CLOSED, OPEN, HALF_OPEN) as maintained by the Dispatcher based on observed failures (Section 9.6). These two machines interact — a CLOSED circuit breaker can open when an otherwise-HEALTHY service has too many observed failures — but they are tracked independently: Health Status is Service-reported (via HEALTH_RESPONSE messages), while circuit breaker state is Dispatcher-maintained (from observed request outcomes). The diagram below is an illustrative combined view showing the typical co-occurrence of states; the per-state-machine transition rules that follow are the normative definitions.

```
                ┌──────────────────────────┐
                │                          │
     ┌──────────▼──┐  failure threshold   ┌┴───────────┐
     │   HEALTHY   │─────────────────────▶│  DEGRADED  │
     │  (CLOSED)   │                      │  (CLOSED)  │
     └──────┬──────┘                      └──────┬─────┘
            │                                    │
            │              ┌─────────────────────┘
            │              │  continued failures
            │              ▼
            │        ┌───────────┐
            │        │ UNHEALTHY │
            │        │  (OPEN)   │
            │        └─────┬─────┘
            │              │
            │              │  health probe succeeds
            │              ▼
            │        ┌───────────┐
            └────────┤ UNHEALTHY │
             success │(HALF_OPEN)│
                     └───────────┘
```

Health Status transitions (Service-reported or Dispatcher-inferred):

- **HEALTHY → DEGRADED:** The Service reports DEGRADED status, or the failure rate exceeds a configurable threshold (RECOMMENDED: 3 failures in 60 seconds).
- **DEGRADED → UNHEALTHY:** The Service reports UNHEALTHY status, or the failure rate exceeds a higher threshold, or the Service fails to respond to health probes.
- **UNHEALTHY → HEALTHY:** The Service reports HEALTHY status in a health probe response, and a configurable number of subsequent requests succeed (RECOMMENDED: 3).

Circuit breaker transitions (Dispatcher-maintained, per Section 9.6):

- **CLOSED → OPEN:** Failure count exceeds `failure_threshold` within `failure_window_seconds`. The Dispatcher stops routing requests to this Service.
- **OPEN → HALF_OPEN:** A configurable recovery period elapses (RECOMMENDED: 30 seconds). The Dispatcher allows a limited number of probe requests.
- **HALF_OPEN → CLOSED:** A configurable number of requests succeed (RECOMMENDED: 3).
- **HALF_OPEN → OPEN:** Any request fails in the half-open state.

<a id="section-13-6-3"></a>
### Circuit Breaker Configuration

Circuit breaker parameters are implementation-defined but SHOULD include:

- `failure_threshold`: Number of failures before opening the circuit (RECOMMENDED: 5).
- `failure_window_seconds`: Time window for counting failures (RECOMMENDED: 60).
- `recovery_probe_interval_seconds`: How often to probe an UNHEALTHY Service (RECOMMENDED: 30).
- `half_open_request_limit`: Number of requests to allow in HALF_OPEN state (RECOMMENDED: 3).

All circuit breaker state transitions MUST be logged in the audit trail.

<a id="section-13-7"></a>
## Graceful Degradation

A Service MAY signal partial capability through the DEGRADED health status with per-capability availability:

```json
{
  "health": {
    "status": "DEGRADED",
    "capabilities": {
      "org.ccdp.deduction": { "available": true, "current_load": 0.95 },
      "org.ccdp.verification": { "available": false }
    },
    "detail": "Verification subsystem undergoing maintenance"
  }
}
```

A DEGRADED Service with `available: true` for a specific capability remains eligible for routing to that capability, but is deprioritized relative to HEALTHY Services. A DEGRADED Service with `available: false` for a capability is treated as UNHEALTHY for that capability only.

This enables finer-grained routing than binary healthy/unhealthy — a Service can shed its most expensive capability while continuing to serve cheaper ones.

<a id="section-14"></a>
# Decomposition

<a id="section-14-1"></a>
## The Decomposition Problem

Most real cognitive work requires decomposition — breaking a complex request into sub-tasks that each route to a different Service. "Fix the bug in the auth module" decomposes into locate, diagnose, repair, verify. "Prove this theorem" decomposes into formalize, search for proof strategy, execute proof steps, check. Decomposition is itself a cognitive act, and one that LLMs are demonstrably weak at — PlanBench shows LLMs collapse on longer planning horizons and hallucinate plans for unsolvable problems [Valmeekam et al. 2024].

CCDP resolves this by treating decomposition as a first-class Service: a dedicated Decomposition Service with Capability Type `org.ccdp.decomposition` that receives complex requests and emits structured Decomposition Plans. The Dispatcher routes to the Decomposition Service first, then routes each sub-request from the plan independently. The Dispatcher performs only structural operations — routing, dependency resolution, typed result-reference substitution; the decomposition intelligence lives in a dedicated, auditable Service behind a typed interface.

<a id="section-14-2"></a>
## When Decomposition Occurs

The Dispatcher invokes the Decomposition Service in one of two ways:

**Explicit decomposition request.** The requester sets `capability_type` to `org.ccdp.decomposition`, indicating that the request should be decomposed rather than handled directly. The Dispatcher routes to the Decomposition Service, receives a plan, and executes it.

**Dispatcher-initiated decomposition.** The Dispatcher MAY route a request to the Decomposition Service when:
- No single Service is registered for the requested `capability_type`.
- The request's Content exceeds the target Service's declared input constraints (e.g., the input is too large or too complex).
- The Dispatcher's routing configuration includes a rule mapping certain capability types to automatic decomposition.

Dispatcher-initiated decomposition MUST be triggered by envelope-level signals, not by content inspection. The relevant signals are: (a) no single Service is registered for the requested `capability_type` (a routing-level signal), (b) the Request's `content.body` size exceeds the target Service's declared `max_input_size` in the Capability Record (a structural size check, not semantic), (c) the Dispatcher's routing configuration includes a decomposition rule for the capability type (a policy signal). The Dispatcher MUST NOT inspect content semantics to decide whether decomposition is needed.

In both cases, the decomposition step is visible in the audit trail — the routing decision records that decomposition was invoked and why.

<a id="section-14-3"></a>
## Decomposition Plan Structure

A Decomposition Plan is the Content of a DECOMPOSITION_RESULT message. It specifies what sub-requests to create, how they depend on each other, how to allocate resources, and how to compose the results.

```json
{
  "content": {
    "type": "structured-data",
    "schema_ref": "org.ccdp.decomposition/output/v1",
    "body": {
      "plan_id": "plan-550e8400-...",
      "description": "Decompose theorem-proving request into formalization and proof search",

      "sub_requests": [
        {
          "sub_id": "sub-001",
          "capability_type": "org.ccdp.language.translation",
          "description": "Translate natural-language theorem statement into Lean 4 syntax",
          "content": {
            "type": "natural-language",
            "body": {
              "source_representation": "natural-language",
              "target_representation": "lean4",
              "text": "For all natural numbers n, if n > 1 then n has a prime factor"
            }
          },
          "constraints": {
            "deadline_fraction": 0.2,
            "cost_fraction": 0.1,
            "provenance_requirement": { "min_grade": "VALIDATED" }
          },
          "depends_on": []
        },
        {
          "sub_id": "sub-002",
          "capability_type": "org.ccdp.deduction",
          "description": "Search for proof of formalized theorem",
          "content": {
            "type": "formal-logic",
            "body": {
              "logic": "lean4",
              "formula": {"$ref": "sub-001.result", "path": "/body/translation"}
            }
          },
          "constraints": {
            "deadline_fraction": 0.7,
            "cost_fraction": 0.8,
            "provenance_requirement": { "min_grade": "FORMALLY_VERIFIED" }
          },
          "depends_on": ["sub-001"]
        },
        {
          "sub_id": "sub-003",
          "capability_type": "org.ccdp.language.translation",
          "description": "Translate proof back to natural language explanation",
          "content": {
            "type": "formal-logic",
            "body": {
              "source_representation": "lean4-proof",
              "target_representation": "natural-language",
              "proof": {"$ref": "sub-002.result", "path": "/body/proof"}
            }
          },
          "constraints": {
            "deadline_fraction": 0.1,
            "cost_fraction": 0.1,
            "provenance_requirement": { "min_grade": "ASSERTED" }
          },
          "depends_on": ["sub-002"]
        }
      ],

      "composition": {
        "method": "template",
        "template": {
          "type": "multipart",
          "body": {
            "parts": [
              { "label": "formalization", "source": "sub-001.result" },
              { "label": "proof", "source": "sub-002.result" },
              { "label": "explanation", "source": "sub-003.result" }
            ]
          }
        },
        "provenance_rule": "weakest_link"
      },

      "fallback": {
        "on_sub_failure": "escalate_parent",
        "on_composition_failure": "return_partial"
      }
    }
  }
}
```

<a id="section-14-3-1"></a>
### Sub-Request Specification

Each `sub_requests` entry contains:

**`sub_id`** (string, REQUIRED): A unique identifier within the plan, used for dependency references and result composition.

**`capability_type`** (string, REQUIRED): The Capability Type for this sub-request. The Dispatcher routes each sub-request independently.

**`description`** (string, OPTIONAL): Human-readable description of this sub-task.

**`content`** (object, REQUIRED): The Content payload for this sub-request. MAY reference results of previous sub-requests using typed result references (Section 14.3.3).

**`constraints`** (object, OPTIONAL): Resource constraints for this sub-request.
- `deadline_fraction`: Fraction of the parent's remaining deadline allocated to this sub-request (0.0 to 1.0).
- `cost_fraction`: Fraction of the parent's cost budget allocated to this sub-request.
- `provenance_requirement`: Minimum provenance grade for this sub-request.

**`depends_on`** (array of strings, REQUIRED): Sub-request IDs that must complete before this sub-request can be dispatched. Empty array means no dependencies (can run immediately).

<a id="section-14-3-2"></a>
### Dependency Graph

The dependency graph is defined by the `depends_on` arrays on each sub-request entry. The Dispatcher constructs the DAG from these arrays and validates that:

1. All `depends_on` references point to valid `sub_id` values within the same plan.
2. The resulting graph is acyclic (a cyclic dependency is a malformed plan — reject with error `-32602`).
3. All sub-requests are reachable (no orphaned entries).

Sub-requests with empty `depends_on` arrays can execute in parallel. The Dispatcher SHOULD execute independent sub-requests concurrently when resources permit.

The `dependencies` top-level field in the plan is OPTIONAL. If present, it is informative only (e.g., for visualization) and MUST be consistent with the `depends_on` arrays. In case of conflict, the `depends_on` arrays are authoritative.

<a id="section-14-3-3"></a>
### Typed Result References

Sub-request content MAY reference results from completed dependencies using typed result references. A result reference is a JSON object (not a template string) that the Dispatcher resolves structurally:

```json
{
  "$ref": "sub-001.result",
  "path": "/body/translation",
  "fallback": null
}
```

**`$ref`** (string, REQUIRED): The sub-request ID whose result is referenced, suffixed with `.result` to refer to the Response Content.

**`path`** (string, REQUIRED): A JSON Pointer [RFC 6901] path into the referenced result's Content.

**`fallback`** (any, OPTIONAL): The value to use if the referenced path does not exist in the result. If omitted and the path does not exist, the Dispatcher follows the plan's `fallback` strategy.

The Dispatcher resolves result references by: (1) waiting for the referenced dependency to complete, (2) extracting the value at the JSON Pointer path from the dependency's Response Content, (3) substituting the reference object with the extracted value. This is a structural operation — the Dispatcher reads a typed path, not natural language. The Dispatcher MUST NOT perform string interpolation, template expansion, or any transformation on the extracted value.

If a referenced dependency failed or escalated, the Dispatcher follows the plan's `fallback` strategy.

<a id="section-14-3-4"></a>
### Composition Specification

The `composition` field specifies how sub-results are assembled into the final result:

**`method`** (string, REQUIRED): One of:
- `"template"`: Assemble parts according to a template (most common).
- `"concatenation"`: Concatenate sub-results in dependency order.
- `"selection"`: Select the best sub-result by a criterion (useful for cross-checking).
- `"custom"`: A custom composition function (specified as a Content payload routed to a composition Service).

When `method` is `"custom"`, the composition payload is routed to a Service with capability type `org.ccdp.composition`. This is a well-known capability type (added to Section 8.3's well-known types). The Composition Service receives the sub-results and the composition specification and returns the composed result. The Dispatcher does not perform custom composition itself — it delegates to the Composition Service and forwards the result.

**`template`** (object, conditional): REQUIRED when `method` is `"template"`. The template for the composed result, with `source` fields referencing sub-results.

**`provenance_rule`** (string, REQUIRED): How to compute the composed result's provenance grade. One of:
- `"weakest_link"`: Composed grade = min(sub-result grades, decomposition grade). Default.
- `"cross_check"`: If independent sub-results agree, upgrade to CROSS_CHECKED (per Section 10.5.2).
- `"explicit"`: The composition step assigns its own grade (used when the composition itself involves verification).

<a id="section-14-3-5"></a>
### Fallback Strategy

The `fallback` field specifies what happens when sub-requests fail:

**`on_sub_failure`** (string, REQUIRED): One of:
- `"escalate_parent"`: Escalate the entire parent request through the parent's Escalation Chain. Any partial sub-results are included in the Escalation.
- `"skip_and_compose"`: Skip the failed sub-request and compose the result from successful sub-results only. The composition template must handle missing parts.
- `"retry_alternative"`: Retry the failed sub-request with a different Service (following normal routing with the failed Service excluded).

**`on_composition_failure`** (string, REQUIRED): One of:
- `"return_partial"`: Return the individual sub-results without composition as a multipart Response.
- `"escalate_parent"`: Escalate the entire request.

<a id="section-14-4"></a>
## Dispatcher Execution of Decomposition Plans

When the Dispatcher receives a DECOMPOSITION_RESULT, it executes the plan:

1. **Validate the plan.** Check that the dependency graph is a DAG, all `capability_type` references exist in the Registry, all `sub_id` values are unique, all `depends_on` references are valid, and resource allocations sum to ≤ 1.0.

2. **Allocate resources.** Compute each sub-request's deadline and cost budget from the parent's constraints and the plan's `constraints` fractions.

3. **Dispatch independent sub-requests.** For each sub-request with no dependencies (or all dependencies satisfied), create a CCDP Request with:
   - A new `request_id`
   - The same `trace_id` as the parent
   - A new `span_id`
   - `parent_span_id` set to the parent request's `span_id`
   - The allocated deadline and cost budget
   - The resolved Content (typed result references resolved per Section 14.3.3)

4. **Process results as they arrive.** As each sub-request completes, check which dependent sub-requests are now unblocked and dispatch them.

5. **Handle failures.** Follow the plan's `fallback` strategy for failed sub-requests.

6. **Compose the final result.** When all sub-requests (or all non-skipped sub-requests) are complete, compose the final result according to the `composition` specification.

**Composition boundary.** For `template`, `concatenation`, and `selection` composition methods, the Dispatcher performs structural assembly: it places sub-results into the template slots, concatenates them in order, or selects by a typed criterion (highest provenance grade, lowest cost). These are mechanical operations on typed wrappers, consistent with the Coordinator Dispatcher model. The Dispatcher MUST NOT perform composition that requires reasoning about content meaning — such composition MUST be routed to an `org.ccdp.composition` Service.

7. **Compute composed provenance.** Apply the `provenance_rule` to derive the composed result's provenance grade. Include the full `composition_trace` (Section 10.5.4).

8. **Return the composed Response.** Send the final Response to the original requester with the composed Content and Provenance.

All steps are logged in the audit trail, creating a complete record of the decomposition execution.

<a id="section-14-5"></a>
## Decomposition Service Contract

The Decomposition Service implements Capability Type `org.ccdp.decomposition` with:

**Input schema:** A CCDP Request (the request to be decomposed). The Decomposition Service receives the original Content and must emit a valid Decomposition Plan.

**Output schema:** A Decomposition Plan (Section 14.3).

**Provenance:** The Decomposition Plan carries its own provenance grade reflecting the evidence strength behind the decomposition. An LLM-only decomposition is graded ASSERTED or HEURISTIC. A decomposition validated by a plan checker is graded VALIDATED.

**Escalation:** If the Decomposition Service cannot decompose the request (it is atomic, it is outside the Service's domain, or the problem is ambiguous), it returns an Escalation with reason `CAPABILITY_EXCEEDED` or `AMBIGUOUS_INPUT`.

The Decomposition Service is a natural candidate for Mode 3 (LLM + validator): an LLM proposes a decomposition plan, and a validator checks structural consistency (valid capability types, acyclic dependencies, resource allocations sum correctly, all result references are valid). The validated plan carries a higher provenance grade than the raw LLM output.

<a id="section-14-6"></a>
## Recursive Decomposition

A sub-request in a Decomposition Plan MAY itself have `capability_type: "org.ccdp.decomposition"`, producing a nested decomposition. The Dispatcher handles this recursively: the sub-decomposition produces its own plan, which the Dispatcher executes as a nested sub-tree of the parent plan.

To prevent unbounded recursion, the Dispatcher MUST enforce a maximum decomposition depth (RECOMMENDED: 5). If a decomposition exceeds the maximum depth, the Dispatcher returns error `-32012` for the deepest sub-request.

The Dispatcher MUST also enforce maximum plan width (the number of sub-requests in a single plan) and maximum total node count (the total number of sub-requests across all recursion levels for a single top-level request). RECOMMENDED limits: maximum width 50 per plan, maximum total nodes 100 per top-level request. These limits prevent decomposition bombs (Section 17.2.5) and are conformance requirements for both Core and Full Dispatchers.

The audit trail records the full tree of decompositions, enabling reconstruction of arbitrarily complex request execution paths.

<a id="section-15"></a>
# Security

<a id="section-15-1"></a>
## Security Posture

Security in CCDP is a protocol guarantee, not an implementation recommendation. This design choice is a direct response to the NSA/CISA assessment of MCP, which found that MCP's security posture is "highly dependent on implementation discipline rather than protocol guarantees" — a dependency that fails unpredictably across deployments.

Every CCDP deployment MUST implement the security requirements in this section. There are no "development mode" exceptions in the specification — while individual deployments MAY relax requirements in non-production environments, the protocol defines a security floor that conforming implementations MUST meet in production.

<a id="section-15-2"></a>
## Authentication

<a id="section-15-2-1"></a>
### Dispatcher-to-Service Authentication

All communication between the Dispatcher and Services MUST be mutually authenticated. The REQUIRED mechanism is mutual TLS (mTLS):

- The Dispatcher and each Service MUST hold X.509 certificates.
- The Dispatcher MUST verify the Service's certificate on every connection.
- The Service MUST verify the Dispatcher's certificate on every connection.
- Certificates MUST be issued by a trusted Certificate Authority (CA) configured per deployment. Self-signed certificates MUST NOT be used in production.

mTLS provides authentication at the transport layer — the Dispatcher knows it is talking to the real Service, and the Service knows it is talking to the real Dispatcher. This is the baseline that prevents Service impersonation and man-in-the-middle attacks.

<a id="section-15-2-2"></a>
### Requester Authentication

External requesters (humans, applications, other systems) MUST be authenticated before the Dispatcher processes their requests. The REQUIRED mechanism is bearer tokens with the following properties:

- Tokens MUST be scoped to specific Capability Types. A token authorized for `org.ccdp.language.generation` MUST NOT be accepted for `org.ccdp.deduction`.
- Tokens MUST have a bounded lifetime (expiration timestamp). The Dispatcher MUST reject expired tokens.
- Tokens SHOULD be issued by an OAuth 2.0 authorization server using Pushed Authorization Requests [RFC 9126] with PKCE [RFC 7636]. Implementations requiring issuer validation SHOULD follow [RFC 9207].
- Tokens MUST be transmitted in the HTTP `Authorization` header.

**Token format.** This specification does not mandate a specific token format. Implementations MAY use JWT [RFC 7519] with the claims listed above, opaque tokens validated by introspection [RFC 7662], or any other bearer token format that supports the required properties (scope, expiration, audience binding). If JWT is used, the Dispatcher MUST validate the signature, expiration, audience (`aud` claim matching the Dispatcher's identifier), and scope claims. If opaque tokens are used, the Dispatcher MUST validate them via the authorization server's introspection endpoint.

**Token lifecycle.** Token clock-skew tolerance MUST be configurable (RECOMMENDED: 60 seconds). Implementations SHOULD support token revocation via revocation lists or introspection-based validity checks for long-lived sessions. Confirmation binding (proof-of-possession via `cnf` claim [RFC 7800]) is OPTIONAL but RECOMMENDED for high-security deployments where bearer-token theft is a concern.

<a id="section-15-2-3"></a>
### Service-to-Service Authentication

When a Service makes a sub-request through the Dispatcher (e.g., a Mode 3 Service invoking a Mode 2 Service), the sub-request is authenticated by the Dispatcher using the originating Service's mTLS identity. The Dispatcher MUST verify that the originating Service is authorized to invoke the target Capability Type.

<a id="section-15-3"></a>
## Authorization

<a id="section-15-3-1"></a>
### Capability-Based Authorization

The Dispatcher MUST enforce capability-based authorization: a requester (human or Service) is authorized for a specific set of Capability Types, and requests for unauthorized types are rejected with error `-32009`.

Authorization mappings are maintained in the Registry or a dedicated authorization service (implementation-defined). The mapping specifies, for each authenticated identity:

- Which Capability Types they may invoke
- Which priority levels they may use
- What maximum cost budget they may specify
- Whether they may specify `destination_id` (direct routing)

<a id="section-15-3-2"></a>
### Token Scoping

Bearer tokens MUST carry scope claims that the Dispatcher validates:

```json
{
  "sub": "client-app-01",
  "scope": ["org.ccdp.deduction", "org.ccdp.language.*"],
  "max_priority": "HIGH",
  "max_cost_usd": 10.00,
  "exp": 1722700800
}
```

The Dispatcher MUST reject:
- Requests for capability types not in the token's `scope`
- Requests with `priority` above the token's `max_priority`
- Requests with `cost_budget.max_monetary_cost` above the token's `max_cost_usd`

Wildcard scopes (e.g., `org.ccdp.language.*`) match all subtypes. Wildcard scope matching uses the following grammar: a scope pattern ending in `.*` matches any scope string that begins with the prefix (everything before `.*`) followed by a dot and one or more additional segments. `org.ccdp.language.*` matches `org.ccdp.language.generation` but not `org.ccdp.language` or `org.ccdp.*`. Exact-match scopes take precedence over wildcard matches. A token with scope `["org.ccdp.language.generation"]` is authorized for that specific capability; a token with scope `["org.ccdp.language.*"]` is authorized for any capability under that prefix.

<a id="section-15-4"></a>
## Message Integrity

<a id="section-15-4-1"></a>
### Transport-Level Integrity

TLS 1.3 provides message integrity at the transport level. This protects against tampering in transit between the Dispatcher and Services.

<a id="section-15-4-2"></a>
### Application-Level Message Signing

For environments requiring end-to-end integrity (the requester must be able to verify that the Service's response was not modified by the Dispatcher or any intermediary), CCDP supports application-level message signing:

A Service MAY sign its Response envelope and content using a digital signature:

```json
{
  "metadata": {
    "org.ccdp.signature": {
      "algorithm": "Ed25519",
      "key_id": "z3-prover-01-signing-key-2026",
      "signature": "base64-encoded-signature",
      "signed_fields": ["envelope.request_id", "envelope.provenance", "content"],
      "timestamp": "2026-08-03T14:30:04.840Z"
    }
  }
}
```

The signature covers the specified fields. The Dispatcher MUST preserve the signature in the metadata when forwarding (per the metadata preservation rule, Section 7.7). The requester can verify the signature using the Service's public key (obtained from the Registry or a key server).

**Canonicalization.** Signing JSON fields requires a deterministic serialization. Implementations MUST use JSON Canonicalization Scheme (JCS) [RFC 8785] to produce a canonical byte sequence before signing. The `signed_fields` array identifies which top-level fields are included; the canonical form is computed over the ordered concatenation of each field's JCS-canonical representation. Fields not listed in `signed_fields` are excluded from the signature and MAY be modified by intermediaries (e.g., the Dispatcher's `audit` annotation).

**Mutable and immutable fields.** The following envelope fields are designated as *Dispatcher-mutable* — the Dispatcher MAY write or update them after the originator or Service has signed the message: `audit`, `remaining_budget_ms`, and metadata keys in the `org.ccdp.dispatcher.*` namespace. All other envelope fields and the entire `content` object are *immutable after signing*. The `signed_fields` array MUST NOT include Dispatcher-mutable fields, and the Dispatcher MUST NOT modify immutable fields on a signed message. A signature that covers a Dispatcher-mutable field is invalid by construction — the verifier MUST reject it.

Message signing is OPTIONAL for CCDP Core conformance. For CCDP Full conformance, message signing is REQUIRED for Services that produce responses at grade FORMALLY_VERIFIED or HUMAN_ATTESTED, and RECOMMENDED for all other Services. For deployments spanning untrusted administrative domains (different organizations, different cloud regions), message signing is REQUIRED regardless of conformance level.

<a id="section-15-4-3"></a>
### Provenance Integrity

Provenance grades and evidence entries are security-relevant — a tampered provenance grade can cause a consumer to over-trust a result. The Dispatcher MUST NOT modify provenance fields. If application-level signing is used, provenance fields SHOULD be included in the signed fields.

<a id="section-15-5"></a>
## Replay Protection

<a id="section-15-5-1"></a>
### Request ID Uniqueness

Every Request carries a unique `request_id` (UUID v4). The Dispatcher MUST maintain a replay cache of recently processed `request_id` values (RECOMMENDED: cache size covers at least 24 hours of traffic). In high-availability deployments with multiple Dispatcher instances, the replay cache MUST be shared across all instances. Implementation options include a shared cache service (Redis, Memcached), a distributed data structure, or a consensus-based replicated store. If the replay cache is partitioned (e.g., by `request_id` hash), the partition scheme MUST ensure that all instances handling the same `request_id` query the same partition. The replay cache is a source of shared state that complicates Dispatcher replication — deployments MUST plan for cache consistency, eviction, and failure.

If the Dispatcher receives a Request with a `request_id` it has already processed:
- If the payload is identical: return the cached response (idempotency).
- If the payload is different: reject with error `-32011` (replay detected).

<a id="section-15-5-2"></a>
### Timestamp Validation

The Dispatcher MUST validate the `envelope.timestamp` field:
- Reject messages with timestamps more than a configurable window in the past (RECOMMENDED: 5 minutes).
- Reject messages with timestamps in the future (beyond a clock-skew tolerance, RECOMMENDED: 30 seconds).

These checks prevent replay attacks where an attacker captures and resubmits a valid message.

<a id="section-15-6"></a>
## Isolation

<a id="section-15-6-1"></a>
### Service Isolation Requirements

Each Capability Record declares the Service's isolation requirements (Section 8.2.2). The Dispatcher or deployment infrastructure MUST enforce these:

- **`executes_arbitrary_code: true`**: The Service MUST run in a sandboxed environment (container, VM, or equivalent) with restricted filesystem and network access.
- **`requires_sandbox: true`**: Same as above, explicitly requested by the Service.
- **`network_access: false`**: The Service MUST NOT have network access beyond the Dispatcher endpoint.
- **`filesystem_access: false`**: The Service MUST NOT have filesystem access beyond its designated working directory.

Isolation requirements declared in Registry metadata are *policy inputs*, not protocol-enforceable guarantees. The Dispatcher trusts that the deployment infrastructure enforces isolation as declared. For deployments requiring stronger assurance, implementations SHOULD support workload attestation — the Service provides a signed attestation (e.g., via a Trusted Platform Module or confidential-computing attestation service) that its runtime environment matches the declared isolation requirements. Attestation verification is an optional Full-conformance feature.

<a id="section-15-6-2"></a>
### Content Isolation

The Dispatcher MUST NOT execute, evaluate, or interpret Content from any Message. Content is treated as opaque data. This prevents content injection attacks where a malicious payload in the Content could influence Dispatcher behavior.

Specifically:
- The Dispatcher MUST NOT pass Content through an eval, template engine, or interpreter.
- Schema validation of Content MUST use a JSON Schema validator that does not execute code (no `$code` or `$eval` extensions).
- Log entries that include Content excerpts MUST sanitize or truncate them to prevent log injection.

The typed result-reference mechanism in Section 14.3.3 is not a template engine — it performs JSON Pointer extraction and structural substitution without interpreting content values. This satisfies the content-isolation requirement.

<a id="section-15-6-3"></a>
### Tool Naming and Registry Security

The MCP fault taxonomy study identified tool naming collisions as an attack vector — malicious entries in public registries with names that shadow legitimate tools. CCDP mitigates this through:

- **Namespaced capability types:** Reverse-domain notation prevents accidental collisions.
- **Registry access control:** Only authorized identities may register or update Capability Records.
- **Registration audit:** All Registry modifications are logged with the modifier's identity and timestamp.
- **Schema validation at registration:** The Registry MUST validate that input and output schemas are well-formed JSON Schema before accepting a registration.

<a id="section-15-7"></a>
## Credential Handling

Services that require credentials (API keys, database passwords, etc.) MUST NOT receive them through the CCDP protocol. Credentials are provisioned through out-of-band mechanisms (environment variables, secret managers, key vaults). The CCDP protocol carries authentication tokens for *protocol-level* identity, not application-level credentials.

The Dispatcher MUST NOT log, cache, or inspect bearer tokens beyond what is necessary for authentication. Token values MUST be redacted in audit logs.

<a id="section-15-8"></a>
## Rate Limiting as Security

Rate limiting (Section 12.5) serves a security function in addition to its resource management role:

- **Denial of service prevention:** Per-requester rate limits prevent a single requester from exhausting Service capacity.
- **Cost abuse prevention:** Per-token cost budgets (Section 15.3.2) prevent a compromised token from incurring unlimited cost.
- **Goodhart-style gaming prevention:** Rate limits on verification services prevent gaming where an attacker submits many weak proofs hoping one trivially passes.

Rate limiting parameters are deployment-configured, not protocol-specified.

<a id="section-16"></a>
# Conformance

<a id="section-16-1"></a>
## Conforming Dispatcher

A conforming Dispatcher MUST implement all of the following:

<a id="section-16-1-1"></a>
### Message Processing

1. Parse all CCDP message types defined in Section 7.2.
2. Validate envelope structure: reject messages with missing REQUIRED fields or invalid field types (Section 7.3).
3. Validate `ccdp_version`: reject messages with unrecognized versions.
4. Preserve and forward all unknown `metadata` fields without modification (Section 7.7).

4a. Respect metadata directionality: keys in `org.ccdp.request.*` are request-directional (preserve on forwarded requests, do not copy to responses); keys in `org.ccdp.response.*` are response-directional (preserve on forwarded responses, do not copy to subsequent requests). Keys with sensitivity labels (defined by deployment policy) MUST be stripped at administrative domain boundaries. Keys without a directional prefix are bidirectional.
5. Never perform semantic interpretation of message Content — never reason about what content means, never make routing decisions based on content meaning. The Dispatcher MAY perform structural validation (JSON Schema checking) and structural operations (typed-reference resolution, template assembly, size checks) on Content as specified in Sections 7, 8, and 14. See the Structural Validation vs Semantic Interpretation definition in Section 4.
6. Never modify message Content.
7. Never modify Provenance grades, Evidence entries, or composition traces.

<a id="section-16-1-2"></a>
### Authentication and Authorization

8. Authenticate all incoming messages (Section 15.2).
9. Reject unauthenticated messages with error `-32008`.
10. Enforce capability-based authorization: reject requests for unauthorized Capability Types with error `-32009` (Section 15.3).
11. Validate bearer token scopes, expiration, and cost limits.

<a id="section-16-1-3"></a>
### Routing

12. Implement the routing algorithm defined in Section 9.2.
13. Query the Registry for service lookup (Section 8.4.2).
14. Filter candidates by health status, deadline, and provenance requirement.
15. Route escalations through the Escalation Chain (Section 13.4).
16. Log all routing decisions in the audit trail.

<a id="section-16-1-4"></a>
### Schema Validation

17. Validate Request Content against the target Service's input schema before forwarding (Section 8.2.2).
18. Validate Response Content against the Service's output schema before forwarding to the requester. For CCDP Core conformance, this validation is RECOMMENDED. For CCDP Full conformance, this validation is REQUIRED.

<a id="section-16-1-5"></a>
### Deadline Enforcement

19. Propagate deadline and `remaining_budget_ms` at every hop (Section 12.4).
20. Reject requests that have already exceeded their deadline with error `-32007`.

<a id="section-16-1-6"></a>
### Audit

21. Generate a structured audit record for every message processed (Section 11.2).
22. Record all mandatory audit fields (Section 11.4).
23. Propagate W3C Trace Context (Section 11.3).

<a id="section-16-1-7"></a>
### Health Monitoring

24. Probe Service health at the intervals specified in Capability Records (Section 13.6).
25. Maintain a routing table with health status and circuit breaker state (Section 9.7).
26. Implement circuit breaker logic (Section 9.6).

<a id="section-16-1-8"></a>
### Security

27. Require TLS 1.3 or later for all Service communication (Section 15.2).
28. Implement replay protection (Section 15.5).
29. Never execute or interpret Content (Section 15.6.2).
30. Redact bearer tokens in audit logs (Section 15.7).

<a id="section-16-1-9"></a>
### Decomposition Execution

31. Validate Decomposition Plans received from a Decomposition Service: acyclic dependency graph, valid capability types, valid resource allocations, width and total-node limits (Section 14). [CORE]
32. Execute Decomposition Plans: dispatch sub-requests, resolve typed result references, compose results using structural methods (template, concatenation, selection). Route custom composition to an `org.ccdp.composition` Service. [FULL]
33. Enforce maximum decomposition depth, width, and total-node limits (Section 14.6). [CORE for validation, FULL for execution]

<a id="section-16-2"></a>
## Conforming Service

A conforming Service MUST implement all of the following:

<a id="section-16-2-1"></a>
### Protocol Compliance

1. Accept CCDP Request messages and return CCDP Response, Escalation, or Error messages (Section 7).
2. Include the `ccdp_version` field on all messages.
3. Use the `request_id` from the Request on the corresponding Response.
4. Preserve and forward all unknown `metadata` fields from the Request to the Response.

<a id="section-16-2-2"></a>
### Contract Compliance

5. Accept only Requests whose Content conforms to the registered input schema.
6. Produce Responses whose Content conforms to the registered output schema.
7. Reject malformed Requests with a CCDP error response rather than attempting to interpret them.

<a id="section-16-2-3"></a>
### Provenance

8. Include a `provenance` field on every Response and Escalation (Section 10).
9. Assign an accurate Provenance Grade following the grade assignment rules (Section 10.3).
10. Include Evidence entries substantiating any grade above ASSERTED.
11. Include the `scope` field for FORMALLY_VERIFIED grades.
12. Report computational resource consumption in `provenance.computation`.

<a id="section-16-2-4"></a>
### Escalation

13. Return an Escalation (not a low-provenance-grade Response) when the Service cannot meet the Request's `provenance_requirement.min_grade` (Section 13.3).
14. Return an Escalation when the Request would exceed the `cost_budget`.
15. Return an Escalation when the `remaining_budget_ms` is insufficient to complete the work.
16. Include `partial_result_available` on all Escalations.

<a id="section-16-2-5"></a>
### Idempotency

17. For the same `request_id`, return the same Response without re-executing the request (Section 7.3.1). Implementations SHOULD maintain a response cache keyed by `request_id` with a configurable TTL (RECOMMENDED: 24 hours).

<a id="section-16-2-6"></a>
### Health

18. Respond to HEALTH_REQUEST messages with accurate HEALTH_RESPONSE messages (Section 7.3.6).
19. Report accurate health status: HEALTHY, DEGRADED, or UNHEALTHY.
20. Report per-capability availability when implementing multiple Capability Types.

<a id="section-16-2-7"></a>
### Security

21. Verify the Dispatcher's identity on incoming connections (mTLS certificate verification, Section 15.2.1).
22. Reject connections from unrecognized Dispatchers.

<a id="section-16-2-8"></a>
### Deadline Compliance

23. Respect the `remaining_budget_ms` field.
24. Return an Escalation with reason `DEADLINE_INSUFFICIENT` or `DEADLINE_APPROACHING` rather than exceeding the deadline silently.

<a id="section-16-3"></a>
## Conforming Registry

A conforming Registry MUST implement all of the following:

<a id="section-16-3-1"></a>
### Operations

1. Support the Register operation (Section 8.4.1).
2. Support the Lookup operation (Section 8.4.2).
3. Support the Get operation (Section 8.4.3).
4. Support the Deregister operation (Section 8.4.4).
5. Support the List Schema Versions operation (Section 8.4.5).

<a id="section-16-3-2"></a>
### Schema Management

6. Store and return input and output JSON Schemas for each Capability Record.
7. Track schema versions using Semantic Versioning [SemVer].
8. Enforce compatibility rules for PATCH and MINOR version updates (Section 8.5.2). Compatibility enforcement covers the practical subset defined in Section 8.5: additive properties for MINOR, identical structure for PATCH, and structural-breaking detection for MAJOR. General JSON Schema equivalence is undecidable; the Registry MAY require operator attestation for compatibility decisions that exceed automated checking capability (Section 8.5).
9. Support transition periods for MAJOR version updates (Section 8.5.4).

<a id="section-16-3-3"></a>
### Security

10. Authenticate all Registry modification operations (register, update, deregister).
11. Log all modifications with the modifier's identity and timestamp.
12. Validate that registered schemas are well-formed JSON Schema before accepting.

<a id="section-16-3-4"></a>
### Availability

13. Respond to Lookup queries within a bounded time (RECOMMENDED: 99th percentile under 100ms).
14. Retain deregistered records for audit purposes (Section 8.4.4).

<a id="section-16-4"></a>
## Conformance Levels

Implementations MAY claim conformance at one of two levels:

**CCDP Core:** Implements all MUST requirements for the relevant component type (Dispatcher, Service, or Registry). This is the minimum for interoperability.

**CCDP Full:** Implements all MUST and SHOULD requirements. Includes application-level message signing, cryptographic audit integrity, and advanced routing features (provenance-aware ranking, decomposition execution, recursive decomposition).

Implementations MUST declare their conformance level in their documentation and in the Registry (for Services) via a `metadata` field: `"org.ccdp.conformance_level": "core"` or `"org.ccdp.conformance_level": "full"`.

<a id="section-16-5"></a>
## Interoperability

A CCDP Core Dispatcher MUST be able to communicate with any CCDP Core Service. A CCDP Full Dispatcher MUST be able to communicate with both CCDP Core and CCDP Full Services. Differences in conformance level MUST NOT cause protocol errors — they MAY result in reduced functionality. A CCDP Core Dispatcher MUST validate Decomposition Plans but is not required to execute them. A Core Dispatcher MAY route decomposition requests to a human queue, an external orchestrator, or return error `-32002` (no service for capability) if no decomposition executor is available. A CCDP Full Dispatcher MUST execute valid Decomposition Plans.

Unknown metadata fields from a higher conformance level MUST be preserved and forwarded, ensuring that Full implementations can exchange extended metadata through a Core intermediary.

<a id="section-16-6"></a>
## Conformance Testing

A future companion document will define a conformance test suite for CCDP Core and Full implementations. Each MUST requirement in this section is intended to correspond to one or more testable assertions. Implementations claiming conformance SHOULD publish their test results against the conformance suite when it becomes available.

Until the conformance suite is available, implementations SHOULD self-test against the following minimum verification:

1. Send a valid REQUEST and verify correct routing and RESPONSE.
2. Send a REQUEST with an invalid envelope and verify error `-32602`.
3. Send a REQUEST for an unauthorized capability and verify error `-32009`.
4. Trigger an escalation and verify correct escalation chain processing.
5. Submit a Decomposition Plan and verify sub-request dispatch and result composition (Full only).
6. Verify that unknown metadata keys survive a round-trip through the Dispatcher.
7. Verify that provenance fields are not modified by the Dispatcher.

<a id="section-17"></a>
# Security Considerations

<a id="section-17-1"></a>
## Threat Model

CCDP operates in an environment where:

- Services are heterogeneous and may include LLM endpoints, which are susceptible to prompt injection, output manipulation, and confidential-data extraction.
- The Dispatcher is a high-value target: compromising it grants access to all Services and audit data.
- The Registry is a high-value target: a tampered Registry can redirect traffic to malicious Services.
- External requesters may be malicious, compromised, or negligent.
- Network links between components, while encrypted (TLS), traverse infrastructure that may be hostile.

The threat model assumes:

1. Attackers may attempt to compromise any single component (Dispatcher, Service, Registry, requester).
2. Attackers may attempt to intercept or modify messages in transit (mitigated by TLS).
3. Attackers may attempt to exploit protocol features (escalation chains, decomposition, provenance) for unauthorized access or quality degradation.
4. Insider threats: a Service operator may deliberately misreport provenance grades.

The threat model does NOT assume:

1. Multiple colluding compromised components (this is a single-fault model). While multi-component collusion is out of scope for protocol-level defense, it is a high-risk scenario for large-scale deployments. Deployments handling sensitive data or operating across organizational boundaries SHOULD implement defense-in-depth measures beyond the protocol: independent audit verification, cross-domain provenance spot-checking, and organizational access controls that limit the blast radius of a single compromised identity.
2. Compromise of the TLS infrastructure itself (CA compromise).
3. Quantum computing attacks on current cryptographic primitives.

<a id="section-17-2"></a>
## Known Attack Vectors

<a id="section-17-2-1"></a>
### Content Injection

**Threat:** A malicious requester crafts Content that, when processed by an LLM Service, causes the LLM to produce unintended output (prompt injection) or exfiltrate data from its context.

**CCDP mitigations:**
- The Dispatcher never processes Content, so injection cannot affect routing.
- Input schema validation (Section 8.2.2) constrains the structural shape of Content, reducing the protocol-level attack surface. Schema validation does not mitigate semantic prompt-injection attacks — a structurally valid string can still be a prompt injection. Content-level injection defense is the Service's responsibility (see Section 17.4).
- Services SHOULD implement their own input sanitization and output validation.

**Residual risk:** Content injection is fundamentally a Service-level concern. CCDP's contribution is ensuring that injection cannot affect protocol behavior (routing, audit, provenance) — only the Service's content processing.

<a id="section-17-2-2"></a>
### Provenance Grade Inflation

**Threat:** A compromised or dishonest Service assigns higher Provenance Grades than its output merits (e.g., assigning FORMALLY_VERIFIED to unverified LLM output).

**CCDP mitigations:**
- Evidence entries must substantiate grades above ASSERTED (Section 10.3). A grade of FORMALLY_VERIFIED without a proof-object evidence entry is a protocol violation.
- The audit trail records all provenance claims, enabling retrospective detection of inflation patterns.
- Application-level message signing (Section 15.4.2) binds provenance claims to Service identity, creating accountability.
- The provenance auditing service pattern (Section 10.8) enables spot-checking by re-verifying evidence.

**Residual risk:** A sufficiently sophisticated attacker could forge evidence entries (e.g., generate a fake proof object). Full mitigation requires independent proof checking — the protocol makes evidence available for checking but does not perform the check itself.

<a id="section-17-2-3"></a>
### Registry Poisoning

**Threat:** An attacker gains write access to the Registry and registers a malicious Service with a legitimate Capability Type, or modifies an existing Service's endpoint to redirect traffic.

**CCDP mitigations:**
- Registry access control: only authorized identities may register or update records (Section 15.6.3).
- Registration audit: all Registry modifications are logged with identity and timestamp.
- Namespaced capability types: reverse-domain notation prevents accidental shadowing.
- Schema validation at registration: the Registry validates schemas, preventing structurally malformed entries.

**Residual risk:** If an attacker compromises the Registry's authentication mechanism, they can redirect traffic. This is a single-point-of-failure risk inherent in a centralized registry. Deployments SHOULD implement Registry audit monitoring with alerts on unexpected modifications.

**Registry poisoning.** If an attacker compromises Registry write access (e.g., by obtaining a Registry administrator credential), they can inject malicious Capability Records — redirecting requests to attacker-controlled Services, lowering isolation requirements, or inflating provenance claims. Mitigations: Registry write operations SHOULD require multi-party approval for production registries. Capability Record changes SHOULD be audited with the same rigor as code deployments. Deployments SHOULD implement out-of-band record verification (a second system independently validates that registered service endpoints match expected infrastructure). Registry backup and rollback procedures MUST be documented.

<a id="section-17-2-4"></a>
### Escalation Chain Exploitation

**Threat:** An attacker crafts a request that deliberately triggers escalation through a chain of increasingly expensive services, consuming resources without producing useful output (a cost-amplification attack).

**CCDP mitigations:**
- Cost budgets propagate through escalation: each escalation target receives the remaining cost budget, which decreases as resources are consumed.
- Per-requester rate limiting prevents sustained cost attacks.
- The Dispatcher logs each escalation, making the attack pattern visible.
- Cycle detection prevents infinite escalation loops (Section 13.4).

**Residual risk:** A single expensive escalation (e.g., triggering a human review that costs $50) is possible within the cost budget. Deployments SHOULD set per-request cost ceilings appropriate to their risk tolerance.

<a id="section-17-2-5"></a>
### Decomposition Bomb

**Threat:** A malicious Decomposition Service returns a plan with exponentially many sub-requests (e.g., each sub-request decomposes into 10 more), overwhelming the Dispatcher and consuming unbounded resources.

**CCDP mitigations:**
- Maximum decomposition depth (Section 14.6, RECOMMENDED: 5).
- Cost budget partitioning: the parent's cost budget is divided among sub-requests. Exponential decomposition rapidly exhausts the budget.
- The Dispatcher validates plans before execution (Section 14.4), including resource allocation checks.

**Residual risk:** A plan with many sub-requests at a single level (wide but shallow) is valid and could be expensive. Section 14.6 now defines normative limits: maximum plan width of 50 sub-requests and maximum total nodes of 100 per top-level request. These limits are conformance requirements enforced by the Dispatcher.

<a id="section-17-2-6"></a>
### Replay Attacks

**Threat:** An attacker captures a valid signed message and replays it to trigger duplicate service invocations, potentially consuming resources or duplicating side effects.

**CCDP mitigations:**
- Request ID uniqueness and replay cache (Section 15.5.1).
- Timestamp validation with bounded acceptance window (Section 15.5.2).
- Service idempotency: replayed requests with the same `request_id` return cached responses without re-execution.

**Residual risk:** Within the acceptance window (RECOMMENDED: 5 minutes), a replayed message with the original `request_id` will be handled via idempotency (cached response returned). Outside the window, it will be rejected.

<a id="section-17-2-7"></a>
### Data Exfiltration via Provenance

**Threat:** A malicious Service embeds sensitive data in provenance Evidence entries (e.g., embedding confidential data in an `artifact_ref` field), which then flows through the audit trail and potentially to unauthorized consumers.

**CCDP mitigations:**
- Evidence `artifact_ref` fields are references (URIs), not inline data. Access to the referenced artifacts is governed by the artifact storage system's access controls, not by CCDP.
- The Dispatcher logs provenance but does not dereference artifact references.
- Deployments SHOULD implement data-loss-prevention (DLP) monitoring on evidence entries.

**Residual risk:** Free-text fields (`evidence.description`, `escalation.detail`) can carry arbitrary text. Deployments processing sensitive data SHOULD implement content scanning on these fields. The same exfiltration risk applies to all free-text and URI fields in the protocol: `escalation.detail`, `routing_decision.reason`, `schema_validation` error messages, notification content, and audit record annotations. Deployments processing sensitive data SHOULD implement content scanning or field-length limits on all free-text fields, and SHOULD classify protocol fields by sensitivity level (public, internal, restricted) with access controls matching the classification.

<a id="section-17-2-8"></a>
### Timing Side Channels

**Threat:** An attacker infers information about Service internals from timing data in the audit trail (e.g., a fast Z3 response implies a trivially satisfiable formula, revealing information about the formula's structure).

**CCDP mitigations:** None at the protocol level. This is an inherent property of any system that exposes latency data.

**Residual risk:** Deployments processing highly sensitive data SHOULD restrict access to detailed timing data in audit records (e.g., aggregate to coarser time buckets in external-facing audit exports), apply field-level access controls on `compute_seconds` and latency fields, and limit who can query per-request audit records. Adding noise to audit records is NOT RECOMMENDED as it undermines audit accuracy.

<a id="section-17-3"></a>
## NSA/CISA Recommendations Applied to CCDP

The NSA/CISA MCP Security Assessment [NSA MCP 2026] made specific recommendations. CCDP's response to each:

| NSA Recommendation | CCDP Response | Requirement Level |
|---|---|---|
| Mandatory authentication | Mutual TLS (Section 15.2) | REQUIRED (Core) |
| Lifecycle-managed tokens | Bearer tokens with expiration and scope (Section 15.3) | REQUIRED (Core) |
| Cryptographic message signing | Application-level signing (Section 15.4.2) | REQUIRED (Full), RECOMMENDED (Core) |
| Replay protection metadata | Request ID + timestamp validation (Section 15.5) | REQUIRED (Core) |
| Sandboxing for code execution | Isolation requirements in Registry (Section 15.6) | REQUIRED (Core, declaration); deployment-enforced |
| Structured (non-text) responses | Typed Content with schema validation (Section 7.4) | REQUIRED (Core) |
| Audit logging | Mandatory audit trail (Section 11) | REQUIRED (Core) |

<a id="section-17-4"></a>
## Honest Limitations

Three security concerns that CCDP does not fully address, stated without softening because the credibility of the security design depends on not overclaiming:

**Content-level attacks are the Service's problem.** CCDP protects the protocol layer — routing, audit, provenance. It does not protect the content layer. A prompt injection that causes an LLM to produce wrong output is invisible to CCDP unless the output fails schema validation or provenance verification. The protocol provides the infrastructure for detecting such failures (provenance grades, cross-checking, auditing) but does not perform the detection.

**The trust model is single-fault.** CCDP is designed to detect and contain compromise of a single component. If both a Service and the Registry are compromised, the attacker can redirect traffic and falsify provenance without detection. Multi-component compromise requires organizational security measures beyond the protocol's scope.

**Provenance grades are claims, not proofs.** A provenance grade is a structured assertion by the Service about its own output's epistemic status. While evidence entries make some grades independently verifiable (proof objects can be checked, test results can be re-run), the protocol fundamentally trusts that Services honestly report their grades. Systematic dishonesty requires organizational and auditing countermeasures, not just protocol design.

<a id="section-18"></a>
# References

<a id="section-18-1"></a>
## Normative References

These references are essential to the implementation of this specification.

**[RFC 2119]** Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels," BCP 14, RFC 2119, March 1997. https://www.rfc-editor.org/rfc/rfc2119

**[RFC 8174]** Leiba, B., "Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words," BCP 14, RFC 8174, May 2017. https://www.rfc-editor.org/rfc/rfc8174

**[RFC 8259]** Bray, T., Ed., "The JavaScript Object Notation (JSON) Data Interchange Format," STD 90, RFC 8259, December 2017. https://www.rfc-editor.org/rfc/rfc8259

**[RFC 9562]** Davis, K., Peabody, B., and P. Leach, "Universally Unique IDentifiers (UUIDs)," RFC 9562, May 2024. https://www.rfc-editor.org/rfc/rfc9562

**[RFC 9126]** Lodderstedt, T., Campbell, B., Sakimura, N., Tonge, D., and F. Skokan, "OAuth 2.0 Pushed Authorization Requests," RFC 9126, September 2021. https://www.rfc-editor.org/rfc/rfc9126

**[RFC 6901]** Bryan, P., Ed., Zyp, K., and M. Nottingham, Ed., "JavaScript Object Notation (JSON) Pointer," RFC 6901, April 2013. https://www.rfc-editor.org/rfc/rfc6901

**[RFC 7519]** Jones, M., Bradley, J., and N. Sakimura, "JSON Web Token (JWT)," RFC 7519, May 2015. https://www.rfc-editor.org/rfc/rfc7519

**[RFC 7636]** Sakimura, N., Bradley, J., and N. Agarwal, "Proof Key for Code Exchange by OAuth Public Clients," RFC 7636, September 2015. https://www.rfc-editor.org/rfc/rfc7636

**[RFC 7662]** Richer, J., Ed., "OAuth 2.0 Token Introspection," RFC 7662, October 2015. https://www.rfc-editor.org/rfc/rfc7662

**[RFC 7800]** Jones, M., Bradley, J., and H. Tschofenig, "Proof-of-Possession Key Semantics for JSON Web Tokens (JWTs)," RFC 7800, April 2016. https://www.rfc-editor.org/rfc/rfc7800

**[RFC 8785]** Rundgren, A., Jordan, B., and S. Erdtman, "JSON Canonicalization Scheme (JCS)," RFC 8785, June 2020. https://www.rfc-editor.org/rfc/rfc8785

**[RFC 9207]** Meyer zu Selhausen, K. and D. Fett, "OAuth 2.0 Authorization Server Issuer Identification," RFC 9207, March 2022. https://www.rfc-editor.org/rfc/rfc9207

**[JSON-RPC]** JSON-RPC Working Group, "JSON-RPC 2.0 Specification," 2010. https://www.jsonrpc.org/specification

**[JSON-SCHEMA-2020-12]** Wright, A., Andrews, H., Hutton, B., and G. Dennis, "JSON Schema: A Media Type for Describing JSON Documents," draft-bhutton-json-schema-01, June 2022. https://json-schema.org/draft/2020-12/json-schema-core

**[W3C-TC]** W3C, "Trace Context," W3C Recommendation, February 2020. https://www.w3.org/TR/trace-context/

**[SemVer]** Preston-Werner, T., "Semantic Versioning 2.0.0." https://semver.org/

<a id="section-18-2"></a>
## Informative References — Protocol Design Foundations

### TCP/IP and the End-to-End Principle

**[Saltzer-Reed-Clark 1984]** Saltzer, J.H., Reed, D.P., and D.D. Clark, "End-to-End Arguments in System Design," *ACM Transactions on Computer Systems*, 2(4):277–288, 1984. https://web.mit.edu/saltzer/www/publications/endtoend/endtoend.pdf

The foundational paper for CCDP's principle that the Dispatcher verifies protocol correctness while content correctness is the Service's responsibility.

**[E2E-Four-Decades]** "The End-to-End Argument, Four Decades Later," HackerNoon. https://hackernoon.com/the-end-to-end-argument-four-decades-later

### RPC and Schema Evolution

**[Kleppmann 2012]** Kleppmann, M., "Schema evolution in Avro, Protocol Buffers and Thrift," 2012. https://martin.kleppmann.com/2012/12/05/schema-evolution-in-avro-protocol-buffers-thrift.html

The basis for CCDP's schema versioning and compatibility rules in the Capability Registry.

**[Connect-gRPC]** Buf, "Connect: A Better gRPC." https://buf.build/blog/connect-a-better-grpc

Demonstrated that typed contracts and code generation are achievable without the full gRPC operational overhead. CCDP's HTTP-native approach is informed by Connect's design.

### Existing Protocols (Critical Analysis)

**[MCP-2026-07-28]** Model Context Protocol, "Release Candidate: The next generation of MCP," July 2026. https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/ (Blog post published May 21, 2026, announcing the July 28, 2026 release candidate.) (accessed 2026-08-03)

**[NSA-MCP-2026]** National Security Agency / Cybersecurity and Infrastructure Security Agency, "Deploying AI Systems Securely: Best Practices for Deploying Secure and Resilient AI Systems," April 2024. https://media.defense.gov/2024/Apr/15/2003439257/-1/-1/0/CSI-DEPLOYING-AI-SYSTEMS-SECURELY.PDF

The security findings that drove CCDP's "security by default" principle.

**[MCP-Faults-2026]** "Real Faults in MCP Software: A Comprehensive Taxonomy," arXiv:2603.05637, 2026. https://arxiv.org/html/2603.05637v1

Analysis of 407 MCP-specific issues from 385 repositories documenting the consequences of loose protocol contracts.

**[A2A]** Linux Foundation / Google, "Agent2Agent (A2A) Protocol Specification," 2025. https://a2a-protocol.org/latest/ (accessed 2026-08-03; the specification has moved from its original google.github.io/A2A/ location) — For background: Galileo AI, "Google Agent2Agent A2A Protocol Guide." https://galileo.ai/blog/google-agent2agent-a2a-protocol-guide (accessed 2026-08-03)

**[Zylos-Interop]** Zylos Research, "Agent Interoperability Protocols 2026." https://zylos.ai/research/2026-03-26-agent-interoperability-protocols-mcp-a2a-acp-convergence/ (accessed 2026-08-03)

**[Zylos-A2A]** Zylos Research, "Agent-to-Agent Communication Protocols." https://zylos.ai/research/2026-02-15-agent-to-agent-communication-protocols/ (accessed 2026-08-03)

**[FIPA-ACL]** SmythOS, "FIPA Agent Communication Language." https://smythos.com/developers/agent-development/fipa-agent-communication-language/ — See also: SmythOS, "Agent Communication Languages Comparison." https://smythos.com/developers/agent-development/agent-communication-languages-and-protocols-comparison/

**[arXiv-Agent-Comms]** "AI Agent Communication from an Internet Architecture Perspective," arXiv:2509.02317. https://arxiv.org/html/2509.02317

The most substantive academic survey of the agent communication landscape. CCDP drew from its FIPA-ACL historical analysis and two-layer standardization strategy while addressing a different problem space (supervised specialists under a dumb router, not autonomous peers at internet scale).

**[Mitra-Stack]** Mitra, S., "The Agent Protocol Stack: MCP + A2A + A2UI as TCP/IP Moment," 2026. https://subhadipmitra.com/blog/2026/agent-protocol-stack/ (accessed 2026-08-03)

**[DEV-Standards]** "The State of Agentic AI Standards in 2026," DEV Community. https://dev.to/alexmercedcoder/the-state-of-agentic-ai-standards-in-2026-mcp-a2a-webmcp-osi-and-the-protocol-stack-taking-3o2l (accessed 2026-08-03)

<a id="section-18-3"></a>
## Informative References — Theoretical Foundations

### Market Economics and Quality Under Asymmetry

**[Akerlof 1970]** Akerlof, G.A., "The Market for Lemons: Quality Uncertainty and the Market Mechanism," *Quarterly Journal of Economics*, 84(3):488–500, 1970.

The lemons-market model for why cognitive output without quality signals degrades. Grounds the case for provenance grades as quality-discriminating signals.

**[Spence 1973]** Spence, M., "Job Market Signaling," *Quarterly Journal of Economics*, 87(3):355–374, 1973.

Signaling theory: a quality signal works only if it is expensive to fake. Grounds the provenance grade taxonomy — each grade represents increasing cost-to-fake.

**[Goodhart 1975]** Goodhart, C.A.E., "Monetary Relationships," 1975. Reformulated by Strathern, M., "'Improving Ratings': Audit in the British University System," *European Review*, 5(3):305–321, 1997.

"When a measure becomes a target, it ceases to be a good measure." Grounds the specification-recursion caveat for FORMALLY_VERIFIED grades and the rate-limiting-as-security design for verification services.

**[Howard 1966]** Howard, R.A., "Information Value Theory," *IEEE Transactions on Systems Science and Cybernetics*, 2(1):22–26, 1966.

Value of information as decision-relative. Grounds the resource-rational routing decisions and cost-budget design.

### Fault-Tolerant Composition

**[Armstrong 2003]** Armstrong, J., "Making reliable distributed systems in the presence of software errors," PhD thesis, KTH Royal Institute of Technology, 2003. https://erlang.org/download/armstrong_thesis_2003.pdf

The supervision-tree architecture. Build reliable systems from unreliable components through strong isolation, message-passing-only interaction, supervision, and "let it crash." Grounds CCDP's overall architectural model.

**[Hewitt-1973]** Hewitt, C., Bishop, P., and R. Steiger, "A Universal Modular ACTOR Formalism for Artificial Intelligence," IJCAI 1973.

The actor model: isolated actors interacting only by asynchronous messages. Grounds the "typed protocols on the wires" between Dispatcher and Services.

**[Simon 1962]** Simon, H.A., "The Architecture of Complexity," *Proceedings of the American Philosophical Society*, 106(6):467–482, 1962.

Near-decomposability: complex systems that survive are hierarchic with strong intra-module and weak inter-module interactions. Grounds the modular Service architecture and the decomposition model.

### Cognitive Architecture and Limits

**[Merrill-Sabharwal 2023]** Merrill, W. and Sabharwal, A., "The Parallelism Tradeoff: Limitations of Log-Precision Transformers," *TACL*, 2023. arXiv:2207.00729.

The TC⁰ result: transformers in a single pass cannot compute inherently sequential functions. Grounds the structural case for external cognitive organs.

**[Huang-2024]** Huang, J., et al., "Large Language Models Cannot Self-Correct Reasoning Yet," ICLR 2024. arXiv:2310.01798.

Self-correction without external feedback is unreliable. Grounds the requirement for external verification services and the escalation-over-silent-failure principle.

**[PlanBench]** Valmeekam, K., Kambhampati, S., et al., "On the Planning Abilities of Large Language Models," NeurIPS 2023. — Updated: Valmeekam, K., Stechly, K., and S. Kambhampati, arXiv:2409.13373, 2024.

LLMs do not plan reliably; they pattern-match and hallucinate plans for unsolvable problems. Grounds the Decomposition Service design — decomposition is a cognitive act performed by a dedicated service, not by the Dispatcher.

**[LLM-Modulo]** Kambhampati, S., et al., "LLMs Cannot Plan, But Can Help Planning in LLM-Modulo Frameworks," ICML 2024, PMLR v235:22895.

The constructive pattern for external planning organs: LLM as idea generator inside a generate-test loop with sound external verifiers. Grounds the Mode 3 (LLM + service composite) architecture.

**[ARC-AGI-2]** Chollet, F., et al., "ARC-AGI-2," arXiv:2505.11831, 2025.

Broad abstraction remains unsolved: ARC-AGI-2 scores ~3% for frontier models vs ~66% for humans. Grounds the HUMAN_ATTESTED grade as the highest grade and the human supervisor's irreducible role.

### Neurosymbolic Integration

**[PAL]** Gao, L., et al., "PAL: Program-aided Language Models," arXiv:2211.10435, 2022.

Offloading computation to a deterministic engine reliably beats chain-of-thought. Grounds the Mode 2 and Mode 3 service architectures.

**[Vericoding]** Bursuc, R., et al., "Vericoding," arXiv:2509.22908, 2025.

LLMs game weak specifications into vacuous proofs (~9%). Grounds the specification-recursion caveat on FORMALLY_VERIFIED grades and the `scope` requirement.

**[FunSearch]** Romera-Paredes, B., et al., "Mathematical discoveries from program search with large language models," *Nature*, 625:468, 2023.

LLM-in-a-loop discovery produces verifiable novel value, but only with a fast, sound, hard-to-game evaluator. Grounds the verification service architecture and Goodhart-aware rate limiting.

### Operations Research

**[Bullwhip]** Lee, H.L., Padmanabhan, V., and S. Whang, "The Bullwhip Effect in Supply Chains," *Management Science*, 43(4):546–558, 1997.

Variance amplification across serial stages. Referenced in Section 12.7 as a warning about error amplification in serial cognitive operations.

**[Little-1961]** Little, J.D.C., "A Proof for the Queuing Formula: L = λW," *Operations Research*, 9(3):383–387, 1961.

Distribution-free queueing invariant relating occupancy, throughput, and latency. Informs the capacity advertisement and load-aware routing design.

<a id="section-18-4"></a>
## Informative References — Additional Sources

The references in this section are secondary or journalistic sources used for context and historical framing. Protocol-level claims in this specification are grounded in the primary references (Sections 18.1–18.3). Secondary sources provide useful context but are not evidence for protocol design decisions.

**[MCP-Roadmap]** Model Context Protocol, "The 2026 MCP Roadmap." https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/ (accessed 2026-08-03)

**[Scalifi-Flaws]** Scalifi AI, "Six Fatal Flaws of MCP," 2025. https://www.scalifiai.com/blog/model-context-protocol-flaws-2025 (accessed 2026-08-03)

**[Sivaro-MCP]** Sivaro, "Is MCP Outdated? A 2026 Reality Check." https://sivaro.in/articles/is-model-context-protocol-outdated-a-2026-reality-check/ (accessed 2026-08-03)

**[A2A-Adoption]** Glukhov, "A2A Protocol 2026 Adoption and Reality." https://www.glukhov.org/ai-systems/comparisons/a2a-protocol-2026-adoption/ (accessed 2026-08-03)

**[AlphaProof]** DeepMind, "AlphaProof," *Nature*, 651:607, 2025. https://www.nature.com/articles/s41586-025-09833-y

**[DreamCoder]** Ellis, K., et al., "DreamCoder: Bootstrapping Inductive Program Synthesis with Wake-Sleep Library Learning," PLDI 2021. https://dl.acm.org/doi/10.1145/3453483.3454080

**[Dehaene-GW]** Dehaene, S., Kerszberg, M., and J.P. Changeux, "A neuronal model of a global workspace in effortful cognitive tasks," *PNAS*, 95(24):14529, 1998. https://www.pnas.org/doi/10.1073/pnas.95.24.14529

**[ACT-R]** Anderson, J.R., et al., "An integrated theory of the mind," *Psychological Review*, 111(4):1036, 2004.

**[Wagner-Altenberg]** Wagner, G.P. and Altenberg, L., "Complex Adaptations and the Evolution of Evolvability," *Evolution*, 50(3):967–976, 1996. https://academic.oup.com/evolut/article/50/3/967/6870900

**[Bullmore-Sporns]** Bullmore, E. and Sporns, O., "The economy of brain network organization," *Nature Reviews Neuroscience*, 13(5):336–349, 2012. https://www.nature.com/articles/nrn3214

**[Lieder-Griffiths]** Lieder, F. and Griffiths, T.L., "Resource-rational analysis: Understanding human cognition as the optimal use of limited computational resources," *Behavioral and Brain Sciences*, 43:e1, 2020.

<a id="section-19"></a>
# Version History

This section records notable changes between published draft versions of this
specification. It is informative and intended to help reviewers understand the
shape of each revision.

<a id="section-19-1"></a>
## Version 0.2.0

Version 0.2.0 is the second reviewed draft of CCDP. It incorporates feedback
from the v0.1 review pass and focuses on resolving architectural consistency,
wire-format precision, conformance clarity, and security/audit semantics. The
wire protocol version remains `"1.0"` during this draft cycle because CCDP has
not yet committed to implementation compatibility.

<a id="section-19-1-1"></a>
### Document Status and Conventions

- Updated the draft status from v0.1 to v0.2 and marked the specification as
  reviewed but not yet implementation-ready.
- Replaced private or machine-local source references with repository-relative
  source and assembler references.
- Added an explicit distinction between the document version (`0.2.0`) and the
  wire protocol version (`"1.0"`).
- Clarified that `trace_id` and `span_id` use W3C Trace Context formatting, not
  UUID formatting.
- Clarified the status of JSON examples that use comments, content type,
  UTF-8 encoding, enum casing, numeric precision, and the normative status of
  examples, tables, diagrams, and design notes.

<a id="section-19-1-2"></a>
### Dispatcher Model

- Replaced the "dumb dispatcher" framing with the Coordinator Dispatcher model:
  the Dispatcher is a constrained protocol enforcement and execution
  coordinator, not a cognitive reasoner.
- Added the distinction between Structural Validation and Semantic
  Interpretation.
- Clarified that schema validation, DAG execution, typed-reference resolution,
  structural result assembly, audit logging, health monitoring, and
  deadline/budget enforcement are structural operations permitted to the
  Dispatcher.
- Clarified that natural-language understanding, logical reasoning, and
  content-meaning-based decisions remain the responsibility of Services.
- Added high-availability caveats for shared Dispatcher state, including replay
  caches, circuit-breaker state, health tables, and audit-store consistency.

<a id="section-19-1-3"></a>
### Message Format and Wire Semantics

- Reworked the JSON-RPC message-type table so RESPONSE and HEALTH_RESPONSE are
  represented as JSON-RPC responses rather than methods.
- Clarified how JSON-RPC notification messages relate to `request_id`.
- Clarified `span_id` ownership: top-level request originators create the
  initial span; the Dispatcher creates hop spans; Services reuse the request
  span on their responses.
- Added a per-message required-field matrix for REQUEST, RESPONSE, ESCALATION,
  NOTIFICATION, HEALTH_REQUEST, HEALTH_RESPONSE, and DECOMPOSITION_RESULT.
- Normalized monetary budget naming toward `max_monetary_cost` and
  `monetary_cost`.
- Clarified the canonical location for Escalation partial results: the
  ESCALATION message Content, with accumulated partial-result references in
  forwarded request metadata.
- Changed oversized-message handling to use HTTP 413 when the payload exceeds
  transport or implementation limits.
- Added metadata directionality conventions for request-directional,
  response-directional, and bidirectional metadata.
- Added a placeholder requirement for companion machine-readable JSON Schemas
  covering envelopes, content wrappers, provenance, escalation, health,
  decomposition plans, and audit records.

<a id="section-19-1-4"></a>
### Capability Registry

- Added typed Escalation Chain entries (`service_id` or `capability_type`) to
  remove ambiguity from string-only escalation targets.
- Added the `cacheable` Capability Record field referenced by the Dispatcher
  caching rules.
- Clarified that Registry lookup results are ranked by the Dispatcher, not the
  Registry.
- Added a Registry API binding note: the current specification defines logical
  operations and the data model, but not a required Registry wire protocol.
- Added schema-selection rules for Dispatcher content validation.
- Added an enforceability caveat for JSON Schema compatibility checking:
  general equivalence/subset checking is not assumed to be decidable, and
  Registries may rely on a practical subset plus operator attestation.
- Added static-vs-dynamic Capability Record guidance for health and capacity
  data freshness.

<a id="section-19-1-5"></a>
### Routing, Flow Control, and Errors

- Replaced ambiguous "MUST either" routing outcomes with deployment-configured
  policies where behavior can legitimately vary.
- Tightened deadline routing so the Dispatcher does not silently route to a
  Service that cannot plausibly meet the deadline.
- Tightened provenance routing so the Dispatcher does not silently route to a
  Service below the requester's provenance requirement.
- Added detailed routing-audit requirements, including candidate scoring
  factors and deployment policy version.
- Added full target checks for escalation routing: capability, health,
  authorization, provenance, deadline, budget, isolation, and cycle detection.
- Renamed the previous `UNSOLVABLE` escalation reason to `SEARCH_EXHAUSTED` to
  distinguish indeterminate search exhaustion from a proven-unsolvable result.
- Clarified HTTP 429 handling as a Dispatcher-observed rate-limit event rather
  than a raw response passed through to the requester.
- Added capacity freshness handling and Dispatcher-measured deadline accounting
  to reduce clock-skew effects.

<a id="section-19-1-6"></a>
### Provenance and Evidence

- Added an explicit caveat that the Provenance Grade ordering is a policy order
  for routing and conformance, not a universal epistemic hierarchy.
- Clarified database query provenance as COMPUTED relative to database state,
  with stored-data provenance tracked separately.
- Clarified that back-translation only counts as VALIDATED when the process is
  independent and the consistency criterion is defined.
- Added independence levels for CROSS_CHECKED evidence and clarified
  common-mode-error risks.
- Added reproducibility guidance for FORMALLY_VERIFIED evidence, including
  proof checker, specification version, artifact hash, and verification
  environment.
- Added a verifier-authority rule: Services report the strongest verification
  actually performed, not the strongest verification they are capable of.
- Added worked examples showing when HUMAN_ATTESTED is required despite formal
  verification and when FORMALLY_VERIFIED is required despite human review.
- Added audit-retention guidance for provenance artifact references.

<a id="section-19-1-7"></a>
### Audit

- Added an `audit_schema_version` independent of both document and wire
  protocol versions.
- Added per-message-type audit-field requirements.
- Added audit-store failure behavior through `audit_failure_policy`, including
  `fail_closed`, `buffer`, and non-production `degrade` modes.
- Added Full-conformance tamper-evidence requirements for audit records.
- Added Trace Context `tracestate` size and sanitization guidance.
- Clarified that audit trails are supervision inputs as well as compliance
  records.

<a id="section-19-1-8"></a>
### Decomposition and Composition

- Replaced string-template result references with typed JSON Pointer result
  references.
- Made `depends_on` arrays the authoritative dependency representation and made
  any top-level dependency graph informative.
- Added a well-known `org.ccdp.composition` capability for custom composition
  that requires cognitive judgment.
- Clarified that the Dispatcher may perform only structural composition and
  must route semantic composition to a Composition Service.
- Added maximum decomposition depth, maximum plan width, and maximum total-node
  requirements to mitigate decomposition bombs.
- Clarified Dispatcher-initiated decomposition triggers as routing, policy, or
  structural size signals rather than semantic content inspection.

<a id="section-19-1-9"></a>
### Security

- Corrected OAuth-related references by adding PKCE, JWT, token introspection,
  proof-of-possession JWT semantics, JSON Canonicalization Scheme, and issuer
  identification references.
- Clarified bearer token format options and validation requirements.
- Added token lifecycle guidance for clock skew, revocation, introspection, and
  optional confirmation binding.
- Added JSON Canonicalization Scheme requirements for application-level message
  signing.
- Added mutable/immutable field rules for signed messages.
- Made message signing required for CCDP Full Services that produce
  FORMALLY_VERIFIED or HUMAN_ATTESTED responses, and required across untrusted
  administrative domains.
- Added shared replay-cache requirements for high-availability Dispatcher
  deployments.
- Clarified that Registry isolation declarations are policy inputs enforced by
  deployment infrastructure, with optional workload attestation for stronger
  assurance.
- Expanded security considerations for multi-component compromise, registry
  poisoning, data exfiltration through free-text fields, decomposition bombs,
  and timing side channels.

<a id="section-19-1-10"></a>
### Conformance

- Split Decomposition Plan validation from Decomposition Plan execution:
  validation is Core, execution is Full.
- Clarified Response Content validation as recommended for Core and required
  for Full.
- Added metadata directionality to Dispatcher conformance requirements.
- Added preliminary conformance-testing guidance and a minimum self-test list.
- Added Registry compatibility enforcement language that acknowledges the
  practical JSON Schema subset and operator attestation for edge cases.

<a id="section-19-2"></a>
## Version 0.1.0

Version 0.1.0 was the initial reviewed draft of CCDP. It introduced the core
architecture:

- Star topology centered on a Dispatcher.
- Heterogeneous cognitive Services behind typed Capability Records.
- Provenance Grades from OPAQUE through HUMAN_ATTESTED.
- Escalation as a first-class protocol operation.
- Mandatory structured audit trail.
- Capability Registry with schema versioning.
- Cost budgets, capacity advertisements, deadlines, retries, and circuit
  breakers.
- Decomposition as a first-class Service.
- Security baseline covering mTLS, bearer tokens, message signing, replay
  protection, isolation, credential handling, and rate limiting.

The v0.1 review identified the main issues that v0.2 addresses: ambiguity in
the Dispatcher role, JSON-RPC response semantics, document vs wire versioning,
single-ladder provenance overclaiming, routing ambiguity, JSON Schema
compatibility enforceability, audit failure behavior, decomposition safety, and
security/reference precision.

<a id="acknowledgements"></a>
# Acknowledgements

_Placeholder — to be completed._
