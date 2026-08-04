# 4. Terminology

This section defines terms used throughout this specification. Terms defined here are capitalized when used in their technical sense.

**Capability.** A typed cognitive function that a Service can perform, identified by a Capability Type and described by a Capability Record in the Registry. Examples: "deduction," "planning," "language-generation," "human-review." A Capability is an interface contract, not an implementation — multiple Services MAY implement the same Capability Type with different backing implementations (Section 5.3).

**Capability Record.** The Registry entry for a Capability, containing: the Capability Type identifier, input and output JSON Schemas, cost hints, health-check endpoint, isolation requirements, supported Provenance Grades, and schema version metadata (Section 8).

**Capability Type.** A string identifier for a class of cognitive function, using reverse-domain notation (e.g., `org.ccdp.deduction`, `org.ccdp.planning`). The protocol defines a set of well-known Capability Types (Section 8.3); implementations MAY define additional types through the Registry.

**Content.** The payload of a CCDP message — the actual cognitive input or output. Content is opaque to the Dispatcher: the Dispatcher MUST NOT interpret, transform, or make routing decisions based on Content. Content structure is governed by the Capability Record's input and output schemas.

**Decomposition.** The process of breaking a complex request into a set of typed sub-requests, each routable to a different Service. Decomposition is performed by a Decomposition Service — a Service whose Capability Type is `org.ccdp.decomposition` — and produces a Decomposition Plan (Section 14).

**Decomposition Plan.** A structured description of how a complex request has been decomposed: the set of sub-requests, their dependency ordering, and the composition function that assembles sub-results into the final result (Section 14).

**Dispatcher.** The central routing component of a CCDP system. The Dispatcher receives messages, reads their Envelopes, makes routing decisions based on Envelope metadata and Registry lookups, forwards messages to Services, and manages audit logging, health monitoring, and escalation routing. The Dispatcher is deliberately simple — it is a classifier/router, not a reasoner. A conforming Dispatcher MUST NOT reason about message Content (Section 16.1).

**Envelope.** The structured metadata portion of a CCDP message, containing all information the Dispatcher needs for routing, audit, and protocol enforcement. The Envelope includes message type, identity and tracing fields, routing fields, constraint fields, provenance fields, audit fields, and extensible metadata. The Dispatcher reads only the Envelope (Section 7).

**Escalation.** A structured protocol response indicating that a Service cannot fulfill a request at the required confidence or capability level. An Escalation is a first-class message type (not an error), carrying the reason for escalation, the achieved confidence level (if any), a partial result (if available), and a suggested routing target. The Dispatcher routes Escalations according to the Escalation Chain (Section 13).

**Escalation Chain.** An ordered list of fallback targets for a given Capability Type, defined in the Registry. When a Service returns an Escalation, the Dispatcher routes to the next target in the chain. The chain typically terminates at a human review queue (Section 13.4).

**Evidence.** A structured record within a Provenance field documenting a specific piece of support for a response's epistemic status. Evidence entries carry a type (e.g., "proof-object," "test-result," "human-signature"), a reference to the supporting artifact, and the Service that produced it (Section 10).

**Health Status.** A Service's self-reported operational state, communicated through Health messages: HEALTHY (fully operational), DEGRADED (partially operational with reduced capability or capacity), or UNHEALTHY (not accepting requests). The Dispatcher maintains a Health Table and uses Health Status for routing decisions (Section 13.6).

**Message.** The atomic unit of CCDP communication. A Message consists of an Envelope and a Content payload, encoded as a JSON-RPC 2.0 request or response. Messages are typed by the `envelope.type` field (Section 7).

**Message Type.** The classification of a CCDP Message by its protocol function. The defined Message Types are: REQUEST, RESPONSE, NOTIFICATION, ESCALATION, HEALTH_REQUEST, HEALTH_RESPONSE, and DECOMPOSITION_RESULT (Section 7.2).

**Provenance.** Structured metadata on a RESPONSE or ESCALATION message documenting the epistemic status of the result: the Provenance Grade, the Evidence supporting it, the Service that produced it, and the computational resources consumed. Provenance is a REQUIRED field on all responses (Section 10).

**Provenance Grade.** An ordinal classification of the evidence strength behind a cognitive output. The defined grades, from weakest to strongest, are: OPAQUE, ASSERTED, HEURISTIC, COMPUTED, VALIDATED, CROSS_CHECKED, FORMALLY_VERIFIED, and HUMAN_ATTESTED. Grades propagate through composed operations according to defined composition rules (Section 10).

**Registry.** The Capability Registry — a service that stores Capability Records, enforces schema versioning and compatibility, and answers routing queries from the Dispatcher. The Registry is a CCDP infrastructure component, not a cognitive Service. Its interface is defined in Section 8; its implementation is not specified.

**Request.** A CCDP Message of type REQUEST, carrying a cognitive task from a requester (human or Service) to the Dispatcher for routing to an appropriate Service.

**Response.** A CCDP Message of type RESPONSE, carrying the result of a cognitive task from a Service back through the Dispatcher to the requester. Every Response MUST carry Provenance metadata (Section 10).

**Service.** Any component that implements one or more Capabilities and communicates with the Dispatcher using the CCDP protocol. Services are heterogeneous: they may be LLM endpoints, theorem provers, classical planners, databases, human review queues, composite LLM+service hybrids, or Decomposition Services. From the Dispatcher's perspective, all Services expose the same typed interface — the Dispatcher does not know or care what implementation backs a Service (Section 5.3).

**Service Mode.** The implementation pattern behind a Service. Four modes are recognized (though the Dispatcher is agnostic to mode): Mode 1 (LLM alone), Mode 2 (deterministic service alone), Mode 3 (LLM + deterministic service composite), and Mode 4 (human queue). The same Capability Type MAY be implemented in different modes by different Services (Section 5.3).

**Span.** A single unit of work within a Trace, corresponding to one hop through the Dispatcher (one Service invocation). Spans carry a unique `span_id` and reference their parent via `parent_span_id`, forming a tree of operations within a Trace (Section 11).

**Trace.** The complete audit trail of a top-level request and all operations it spawns, identified by a unique `trace_id`. A Trace spans the lifetime of a request through routing, service invocation, possible decomposition into sub-requests, escalation, and final response. Trace context propagation follows W3C Trace Context [W3C-TC] (Section 11).

**Trace Context.** The W3C Trace Context fields (`traceparent` and `tracestate`) propagated through CCDP messages to enable distributed tracing across the system. CCDP maps these to Envelope fields (Section 11.3).
