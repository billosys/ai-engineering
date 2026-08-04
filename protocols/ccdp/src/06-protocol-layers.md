# 6. Protocol Layers

## 6.1. Layering Rationale

CCDP follows the TCP/IP tradition of layered protocol design: each layer provides a specific abstraction, relies only on the layer below, and can evolve independently. The layering is deliberate — it separates transport concerns (how bytes move) from routing concerns (where messages go) from epistemic concerns (how much to trust the result).

Unlike TCP/IP, where the application layer is unspecified by the transport, CCDP's upper layers carry load-bearing protocol semantics. Provenance grades, audit metadata, and escalation semantics are not application concerns delegated to the endpoints — they are protocol-layer features enforced at the Dispatcher. This is the sense in which "the protocol is smart": the layers above transport carry intelligence that a Dispatcher with no cognitive capability of its own can enforce mechanically.

## 6.2. Layer Architecture

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

### 6.2.1. Layer 1: Transport

The Transport Layer provides reliable, encrypted, authenticated byte delivery between the Dispatcher and Services.

**HTTP is REQUIRED** as the base transport protocol. CCDP messages are HTTP POST requests to defined endpoints. HTTP was chosen for ubiquity: it works with all Service types (LLM endpoints, web services, queue systems), is supported by all programming languages, and composes with existing infrastructure (load balancers, proxies, monitoring).

**JSON-RPC 2.0 is REQUIRED** as the wire format. Every CCDP message is a JSON-RPC 2.0 request or response, with CCDP-specific method names and parameter structures. JSON-RPC was chosen for simplicity: its specification fits on one page, it is transport-agnostic, and it imposes minimal parsing overhead on a Dispatcher with no cognitive capability of its own. Both MCP and A2A chose JSON-RPC 2.0 for the same reasons.

**TLS 1.3 (or later) is REQUIRED** for all Dispatcher-to-Service communication. Plaintext HTTP MUST NOT be used in production deployments. Self-signed certificates MAY be used in development environments.

**Authentication** is performed at this layer. The REQUIRED mechanism is mutual TLS (mTLS) for Dispatcher-to-Service authentication. Bearer tokens with scoped permissions MAY be used as an additional authorization mechanism (Section 15). Bearer-token validation is logically an application-level concern (it checks CCDP-scoped authorization, not transport-level connectivity). It is placed in the Transport Layer for implementation convenience: tokens are typically carried in HTTP headers and checked before message parsing begins. This is a pragmatic layer crossing, not a design error.

Implementations MAY support additional transports (e.g., QUIC for latency-critical paths, WebSocket for long-lived connections) as protocol extensions, provided they satisfy the same reliability, encryption, and authentication guarantees. The Transport Layer is the most substitutable layer in the stack.

### 6.2.2. Layer 2: Routing and Audit

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

### 6.2.3. Layer 3: Epistemic

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

The Dispatcher reads selected Layer 3 fields for routing and enforcement purposes: `provenance_requirement.min_policy_grade` for candidate filtering, `cost_budget` for cost-aware routing, and `deadline`/`remaining_budget_ms` for deadline enforcement. This is structural use of typed metadata, not semantic interpretation of content. It MAY enforce structural rules (e.g., reject a Response missing the `provenance` field) but MUST NOT interpret their content (e.g., the Dispatcher does not evaluate whether a Provenance Grade is accurate — that is the Service's responsibility, subject to audit).

### 6.2.4. Layer 4: Content

The Content Layer carries the actual cognitive input and output — the problem to be solved, the proof to be checked, the text to be drafted, the plan to be validated. Content is entirely opaque to the Dispatcher.

Content structure is governed by the Capability Record's input and output JSON Schemas, stored in the Registry. The Dispatcher MAY validate Content against these schemas (structural schema validation is a Layer 2 enforcement function), but MUST NOT interpret the Content's meaning — the Structural Validation vs Semantic Interpretation distinction (Section 4) is what separates the two.

Content is typed by the `content.type` field, which indicates the format of the payload: `natural-language`, `formal-logic`, `proof-object`, `validated-plan`, `structured-data`, or a custom type defined in the Capability Record.

## 6.3. Layer Independence

Each layer can evolve independently:

- **Transport substitution**: Replace HTTP with QUIC or WebSocket without changing routing, provenance, or content semantics. The only constraint is that the new transport must provide reliable, encrypted, authenticated byte delivery. Non-HTTP transports MUST provide equivalent mechanisms for message signing (Section 15.4), bearer-token authentication (Section 15.2), trace-context propagation (Section 11.3), and status/error signaling (Section 13.2). A transport-binding specification for non-HTTP transports is out of scope for this document but is needed before non-HTTP deployments can claim conformance.
- **Routing evolution**: Add new routing strategies (content-hash routing, geographic routing) without changing transport or epistemic semantics. New routing fields are added as metadata extensions.
- **Epistemic evolution**: Add new Evidence types or new composition rules without changing transport or routing. Adding new Provenance Grades is a protocol extension that requires a document version increment. New grades affect the ordering used for routing, conformance checking, and policy evaluation. The grade set is versioned through the Registry; deployments MUST ensure that all components recognize the grade vocabulary before grades are used in production. New epistemic fields are added as metadata extensions. Existing implementations that do not understand the new fields MUST preserve and forward them (Section 7.7).
- **Content evolution**: Service-specific schemas evolve through the Registry's schema versioning mechanism (Section 8.5) without affecting any lower layer.

This independence is a direct application of the end-to-end principle: each layer does only what it must, and correctness guarantees that belong to a higher layer are not duplicated at a lower layer. The Dispatcher enforces protocol correctness (Layer 2); Services enforce content correctness (Layer 4); the Epistemic Layer (Layer 3) carries the metadata that connects them.

## 6.4. Comparison to the Emerging Agent Protocol Stack

Several sources describe a layered agent protocol stack forming: MCP for tool integration, A2A for agent coordination, WebMCP for browser interaction. CCDP's layering differs in three respects:

**The Epistemic Layer has no counterpart.** The emerging stack has no protocol-level concept of provenance, evidence strength, or epistemic status. This is the gap CCDP fills — the recognition that cognitive outputs are claims with pedigree, not data with types.

**The Dispatcher is a protocol enforcer, not a capable agent.** In the emerging stack, the "client" or "orchestrator" is assumed to be an intelligent agent. CCDP's Dispatcher is closer to a policy-enforcing message coordinator: it reads headers and structural metadata, applies routing policies, executes decomposition plans, validates schemas, and forwards processed messages — all without cognitive capability. The protocol carries the intelligence; the Dispatcher enforces it.

**Audit is a layer concern, not an extension.** In the emerging stack, observability comes from bolting on OpenTelemetry or similar frameworks. In CCDP, audit fields are mandatory Layer 2 elements — the Dispatcher writes them as part of its core function, not as an opt-in integration.

## 6.5. Structural Operations Across Layers

The Dispatcher's structural operations cross layer boundaries by design. Schema validation reads Layer 4 (Content) structure against Layer 2 (Capability Record) definitions. Decomposition plan execution resolves typed references in Layer 4 Content using Layer 2 sub-request identifiers. Budget and deadline propagation reads Layer 3 constraints and writes updated values on forwarded messages. These crossings are explicitly allowed: the Dispatcher operates on typed metadata and structural shapes, not on semantic meaning — the Structural Validation vs Semantic Interpretation distinction (Section 4). Section 16 lists these as conformance requirements rather than layer violations.
