# 3. Introduction

## 3.1. The Problem

A composite cognition system assembles engineering-grade cognitive output by routing requests to specialized services — each operating in its domain of competence — rather than relying on a single monolithic model to simulate all cognitive faculties. The architectural claim is grounded in a structural result: a single forward pass of a transformer (or state-space model) sits in the complexity class TC⁰ and cannot compute inherently sequential functions in a single pass (that is, functions outside TC⁰ require either multiple passes or external state — the formal justification for external cognitive organs, not a claim that LLMs cannot perform any sequential reasoning) [Merrill & Sabharwal 2023]. Chain-of-thought mitigates this by externalizing serial state into the token stream, but an LLM cannot reliably verify its own reasoning by introspection — self-correction without external feedback often leaves accuracy flat or makes it worse [Huang et al. 2024]. The error floor is architectural, not a reliability defect.

The consequence is that a language model is best understood as a *language organ* — superb at natural-language understanding, generation, translation between representations, and fuzzy pattern completion — composed with *external organs* that provide the faculties it lacks: deduction (theorem provers, SMT solvers), planning (classical planners with sound validators), durable state (typed ledger with provenance), and selection/verification (calibrated verifiers, process-reward models). A human supervisor provides the faculties for which no working external organ exists: broad abstraction, specification, and open-ended value judgment [ARC-AGI-2; Chollet et al. 2025].

This architecture requires a protocol. Requests must flow from humans (and from services making sub-requests) through a central point — the dispatcher — to the appropriate service, with responses flowing back. The dispatcher must route correctly, and every link in the chain must be auditable. The protocol must carry enough structure for routing decisions to be classification rather than reasoning — the dispatcher reads envelopes, not content.

No existing protocol jointly satisfies these requirements: typed envelope routing through a non-cognitive coordinator, mandatory structured audit, provenance grades with composition rules, first-class escalation, cost and deadline signals, and a capability registry with schema versioning.

## 3.2. Why Existing Protocols Are Insufficient

### 3.2.1. MCP (Model Context Protocol)

MCP is the closest existing protocol to CCDP's problem space — it connects language models to external capabilities. Its core abstraction (tools, resources, prompts) covers most LLM-to-service interactions.

[Informative] Its ecosystem velocity — a large and fast-growing community of server implementations — is further evidence the abstraction is useful, though this is a qualitative ecosystem observation rather than a claim grounded in a primary source.

MCP's July 2026 stateless pivot [MCP 2026-07-28 RC] is a significant operational improvement: self-contained requests, routing headers, W3C Trace Context propagation. But MCP has five structural shortcomings that its architectural evolution does not address:

**Designed for smart consumers, not dumb dispatchers.** MCP assumes the client (the LLM/host) is the intelligent party — it interprets natural-language tool descriptions, decides which tools to invoke, and manages conversation flow. Tool descriptions are free-text strings meant for LLM consumption. For CCDP's dispatcher — a protocol enforcement and execution coordinator that operates on envelope metadata — MCP carries insufficient routing structure. The protocol intelligence lives in the consumer, not the envelope.

**No mandatory audit.** MCP does not mandate structured logging of tool invocations. Audit trails are implementation concerns. For a supervision-tree architecture where every link must be inspectable, audit metadata must be a core protocol field, not an afterthought.

**No cost or resource signals.** MCP provides no mechanism for a service to communicate resource consumption, latency expectations, or cost. A dispatcher cannot make resource-rational routing decisions without this information. TCP has congestion signals (ECN, window advertisements); a cognitive dispatch protocol needs cognitive-resource signals.

**Security by implementation discipline.** The NSA/CISA assessment [NSA MCP 2026] found MCP's security posture "highly dependent on implementation discipline rather than protocol guarantees" — no mandated authentication, tool parameter injection enabling arbitrary code execution, tool naming collisions exploitable from public registries. The 2026-07-28 spec adds OAuth 2.0 authorization with Pushed Authorization Requests [RFC 9126] and PKCE [RFC 7636], but the "security by convention" orientation persists.

**No epistemic dimension.** Most fundamentally, MCP treats service outputs as data. CCDP treats them as *claims with epistemic status*. A prover's output and an LLM's output are structurally different kinds of evidence, and the protocol must carry that distinction. MCP has no concept of provenance grades, evidence strength, or provenance-grade-below-threshold escalation (CCDP's `CONFIDENCE_BELOW_THRESHOLD` escalation reason).

### 3.2.2. A2A (Agent-to-Agent Protocol)

A2A [Google 2025] fills the peer-to-peer coordination gap MCP leaves. Its Agent Cards provide capability discovery; its task lifecycle (submitted → working → completed/failed) suits long-running operations; and its opacity principle — agents collaborate on capabilities without exposing internals — is architecturally sound.

A2A's limitation for CCDP is that it assumes both sides of a link are *agents* — capable, autonomous entities that negotiate and decide. CCDP's dispatcher is deliberately not an agent. It is a protocol enforcement and execution coordinator. A2A's complexity (Agent Card infrastructure, multi-transport support, autonomous negotiation) is overkill for a system where one side is a constrained coordinator, not an autonomous agent, and its peer-to-peer topology does not match CCDP's star topology.

### 3.2.3. gRPC and Protocol Buffers

gRPC provides the right *ideas*: typed contracts via protobuf schemas, streaming, interceptor chains for cross-cutting concerns. Industry-proven at Google scale.

gRPC's *implementation complexity* works against the constrained-coordinator principle. Schema version management is a chronic operational wound — the discipline of never reusing field numbers, managing `.proto` file distribution, and coordinating the protoc toolchain across heterogeneous services creates friction that compounds. gRPC's full implementation stack is substantial, and its operational overhead (protoc toolchain, `.proto` file distribution, field-number management) works against the constrained-coordinator principle. A dispatcher should not need a protoc toolchain. CCDP adopts gRPC's design principles (typed contracts, deadline propagation, interceptor-style audit) without its implementation weight, using JSON Schema for runtime-validatable contracts and JSON-RPC 2.0 for the wire format.

### 3.2.4. FIPA-ACL: The Cautionary Tale

FIPA-ACL [1990s–2000s] established the concept of typed communicative acts — messages typed by performative (request, inform, query, escalate) with sender/receiver/content/ontology metadata. This concept is exactly right for cognitive dispatch.

FIPA-ACL never escaped the lab. It lacked verifiable identity, governance frameworks, runtime tooling, and practical deployment paths. It was described in a comprehensive survey as having limited practical deployment despite its formal elegance [arXiv:2509.02317]. CCDP inherits FIPA's insight — speech acts as message types — while designing explicitly against its failure modes: every protocol feature must be practically deployable with minimal tooling, not formally elegant in isolation.

## 3.3. What Is Different About Cognitive Dispatch

The distinction between cognitive dispatch and data routing — the reason CCDP cannot be a thin layer over an existing RPC framework — lies in three properties unique to cognitive output:

**Cognitive outputs are claims, not data.** A database query returns a fact. A theorem prover returns a proof. An LLM returns a plausible completion. These are structurally different kinds of evidence, and a protocol that treats them identically forces the consumer to reconstruct epistemic status from scratch at every boundary. CCDP makes provenance a first-class protocol field: every response carries a grade indicating the evidence strength behind it, with defined composition rules for multi-service operations (Section 10).

**Provenance-grade insufficiency is a routing event, not an error.** When a cognitive service cannot produce output at the requested provenance grade, this is not a failure — it is information. "I can generate candidate solutions but cannot verify them" is a legitimate, structured response that the dispatcher should route to a verification service or escalate to a human. CCDP defines escalation as a protocol message type with structured routing semantics (Section 13).

**The specification-recursion problem.** Formal verification relocates error rather than eliminating it: "did we build it right?" becomes "did we specify the right thing?" [Vericoding; Goodhart 1975]. An LLM that games a weak specification into a vacuous proof is not a verification failure — it is a Goodhart failure. CCDP's provenance system is designed with this recursion in mind: a grade of FORMALLY_VERIFIED carries a scope field binding it to a specific specification, and the specification's own provenance is separately tracked (Section 10).

## 3.4. Design Principles

CCDP is governed by eight principles, each grounded in the research base:

1. **The dispatcher is a constrained coordinator, not a reasoner — it performs structural operations (validation, routing, plan execution, audit) without cognitive capability.** Routing decisions MUST be possible from envelope metadata alone, without understanding message content. (From: the networking-switch concept — a switch reads headers and forwards packets.)

2. **The end-to-end principle applies.** The dispatcher verifies *protocol* correctness (well-formed envelopes, valid routing, schema compliance, timeout enforcement) — structural validation, not semantic interpretation (Section 4). *Content* correctness is the service's responsibility. (From: Saltzer, Reed & Clark 1984.)

3. **Audit is mandatory, not optional.** Every message passing through the dispatcher gets structured audit metadata. This is core protocol behavior, not an extension. (From: NSA/CISA MCP assessment — "security by implementation discipline" fails.)

4. **Provenance grades are first-class.** Every response carries an evidence-strength field. This is the protocol's novel contribution. (From: the Spence signaling theory — quality signals work only when expensive to fake.)

5. **Escalation is a protocol operation, not an error.** Services can return "I cannot handle this at the required provenance grade" as a structured escalation that the dispatcher routes upward. (From: OTP supervision — escalation through the supervision tree is normal operation.)

6. **Typed contracts in a registry.** Services register their capabilities (input/output schemas, cost hints, health endpoints, isolation requirements) in a capability registry. Schema evolution is enforced at the registry. (From: Avro schema registry — centralized version management with compatibility checking.)

7. **Extensibility without breakage.** Unknown metadata fields are preserved and forwarded. New capabilities are added as metadata keys without protocol version bumps. (From: TCP options field, HTTP headers, protobuf unknown-field forwarding.)

8. **Security by default.** Mutual authentication, message signing, token scoping per service. Not opt-in. (From: NSA/CISA findings — security as a protocol guarantee, not an implementation choice.)

## 3.5. Scope

CCDP specifies the message format, routing semantics, registry interface, provenance system, audit requirements, and security baseline for communication between a dispatcher and cognitive services. It does not specify:

- The internal implementation of any service
- The storage backend of the capability registry
- The training or architecture of any language model
- The human interface for supervision or escalation review
- The specific set of capability types (which are registry-managed, not protocol-defined; the protocol defines a set of well-known Capability Types as extension points in Section 8.3; the registry manages the open-ended set of deployment-specific types)

CCDP is transport-layer agnostic in principle but specifies HTTP as the REQUIRED base transport and JSON-RPC 2.0 as the REQUIRED wire format. Future specifications MAY define bindings for other transports.
