# 4. Terminology

This section defines terms used throughout this specification. Terms defined here are capitalized when used in their technical sense.

**Artifact Reference.** The `artifact_ref` object within an Evidence entry (see Evidence Entry below), pointing to a verifiable artifact (proof object, test result, signed attestation) stored outside the CCDP message. Artifact References appear in Evidence entries. The `uri` form, dereference authority, and access-control requirements are deployment-defined. Artifact References SHOULD include an `integrity` hash for content verification (REQUIRED at grades VALIDATED and above — see Evidence Entry). Artifact References that appear in audit records are subject to the audit retention policy (Section 11.5). Deployments MUST ensure that referenced artifacts remain resolvable for the configured audit retention period. Decomposition Plan result references (Section 14.3.3) are typed JSON Pointer `$ref` objects and are not Artifact References.

**Audit Record.** A structured log entry created by the Dispatcher for each message processed. Audit Records are defined in Section 11. Each Audit Record carries an `audit_schema_version` field independent of the CCDP document and wire versions.

**Authenticated Sender.** The identity of the immediate sender of a message, as established by the transport layer (mTLS certificate Common Name, or bearer-token subject claim). The Authenticated Sender is distinct from the Requester (`source_id`), which identifies the original originator across hops. For a Request arriving from the Requester, the Authenticated Sender and the Requester are the same entity. For a forwarded message, the Authenticated Sender is the Dispatcher, while the Requester remains the original originator. Signature verification and authorization checks MUST use the Authenticated Sender identity, not `source_id`, because `source_id` is an unauthenticated claim carried in the message payload.

**Capability.** A typed cognitive function that a Service can perform, identified by a Capability Type and described by a Capability Record in the Registry. Examples: "deduction," "planning," "language-generation," "human-review." A Capability is an interface contract, not an implementation — multiple Services MAY implement the same Capability Type with different backing implementations (Section 5.3).

**Capability Record.** The Registry entry for a Capability, containing: the Capability Type identifier, input and output JSON Schemas, cost hints, health-check endpoint, isolation requirements, supported Provenance Grades, and schema version metadata (Section 8).

**Capability Scope.** The set of capability types a bearer token or identity is authorized to access, expressed as a list of exact capability-type strings or wildcard patterns (Section 15.3.2). Scopes are evaluated during routing authorization.

**Capability Type.** A string identifier for a class of cognitive function, using reverse-domain notation (e.g., `org.ccdp.deduction`, `org.ccdp.planning`). The protocol defines a set of well-known Capability Types (Section 8.3); implementations MAY define additional types through the Registry.

**Conformance Level.** The level of protocol compliance claimed by an implementation: Core (all Core requirements) or Full (all Core requirements plus all Full requirements). Conformance is defined by explicit, stably-identified requirement tables (e.g. `DISP-CORE-NNN`, `DISP-FULL-NNN` for the Dispatcher), not by the sum of all SHOULD statements in the specification. Service and Registry stable IDs are an open item (Section 18). See Section 16.4.

**Content.** The payload of a CCDP message — the actual cognitive input or output. Content is opaque to the Dispatcher: the Dispatcher MUST NOT interpret, transform, or make routing decisions based on Content. The Dispatcher MAY perform structural validation of Content against JSON Schemas and MAY resolve typed references within Content wrappers during decomposition plan execution (Section 14). These are structural operations, not semantic interpretation (see Structural Validation vs Semantic Interpretation below). Content structure is governed by the Capability Record's input and output schemas.

**Cost Budget.** The resource constraints on a Request, carried in the `cost_budget` envelope field. Includes optional limits on compute time, token consumption, and monetary cost. Propagated and partitioned through decomposition and escalation.

**Decomposition.** The process of breaking a complex request into a set of typed sub-requests, each routable to a different Service. Decomposition is performed by a Decomposition Service — a Service whose Capability Type is `org.ccdp.decomposition` — and produces a Decomposition Plan (Section 14).

**Decomposition Plan.** A structured description of how a complex request has been decomposed: the set of sub-requests, their dependency ordering, and the composition function that assembles sub-results into the final result (Section 14).

**Dispatcher.** The central routing component of a CCDP system. The Dispatcher receives messages, reads their Envelopes, makes routing decisions based on Envelope metadata and Registry lookups, forwards messages to Services, and manages audit logging, health monitoring, and escalation routing. The Dispatcher is a constrained protocol enforcement and execution coordinator. It performs structural operations — routing, schema validation, decomposition plan execution, typed-reference resolution, structural result assembly, audit logging, health monitoring, and deadline/budget enforcement — but has no cognitive capability. It never reasons about what content means. A conforming Dispatcher MUST NOT reason about message Content (Section 16.1).

**Envelope.** The structured metadata portion of a CCDP message, containing all information the Dispatcher needs for routing, audit, and protocol enforcement. The Envelope includes message type, identity and tracing fields, routing fields, constraint fields, provenance fields, audit fields, and extensible metadata. The Dispatcher reads the Envelope and selected structural Content fields (schema shapes, typed references) to route and process messages (Section 7).

**Escalation.** A structured protocol response indicating that the originating actor (a Service or the Dispatcher) determined that a request cannot be fulfilled at the required provenance grade or capability level. An Escalation is a first-class message type (not an error), carrying the reason for escalation, the achieved provenance grade (if any), a partial result (if available), and a suggested routing target. The Dispatcher routes Escalations according to the Escalation Chain (Section 13). The `escalation_origin` field (Section 7.3.4) distinguishes Service-generated from Dispatcher-generated Escalations.

**Escalation Chain.** An ordered list of fallback targets for a given Capability Type, defined in the Registry. When a Service returns an Escalation, the Dispatcher routes to the next target in the chain. Dispatcher-generated implicit Escalations use either the responding Service's chain or route directly to human review, depending on the triggering policy (Section 9.2, Section 13.4). The chain typically terminates at a human review queue (Section 13.4).

**Evidence Entry.** A structured record of one piece of evidence supporting a provenance grade claim. Evidence entries appear in the `evidence` array within a message's Provenance (Section 10). The normative schema:

```json
{
  "method": "formal_verification",
  "description": "Coq proof of theorem T against spec S",
  "service_id": "svc-formal-01",
  "artifact_ref": {
    "uri": "urn:ccdp:artifact:abc123",
    "artifact_type": "proof_certificate",
    "integrity": {
      "algorithm": "sha-256",
      "digest": "a1b2c3..."
    },
    "media_type": "application/json",
    "access": "audit-archive"
  },
  "verified_by": "coq-8.18.0"
}
```

- **`method`** (string, REQUIRED): The evidence method used. Examples: `"formal_verification"`, `"human_review"`, `"independent_cross_check"`, `"statistical_testing"`, `"computed"`. This replaces the former `type` field used in earlier drafts. Matched by `provenance_requirement.required_methods` (Section 7.3.2).
- **`description`** (string, OPTIONAL): Human-readable description of the evidence.
- **`service_id`** (string, REQUIRED): Identifier of the Service that produced this evidence.
- **`artifact_ref`** (object, CONDITIONAL): Evidence artifact reference — an object, not a string, when present. MUST be present at grades VALIDATED (4) and above when a supporting artifact exists. RECOMMENDED for grades OPAQUE through COMPUTED.
  - **`uri`** (string, REQUIRED): URI or identifier for the evidence artifact. Subject to the audit retention policy (Section 11.5) — referenced artifacts MUST remain resolvable for the configured retention period.
  - **`artifact_type`** (string, REQUIRED): Type of artifact. Examples: `"proof_certificate"`, `"signed_attestation"`, `"test_report"`, `"counterexample"`, `"review_record"`. Matched by `provenance_requirement.required_evidence_types` (Section 7.3.2).
  - **`integrity`** (object, REQUIRED at VALIDATED+ grades): Cryptographic integrity hash. Sub-fields: `algorithm` (string, REQUIRED, e.g., `"sha-256"`) and `digest` (string, REQUIRED, hex-encoded hash value).
  - **`media_type`** (string, OPTIONAL): MIME type of the artifact.
  - **`access`** (string, OPTIONAL): Retrieval hint (e.g., `"audit-archive"`, `"inline"`, `"external-url"`).
- **`verified_by`** (string, OPTIONAL): Identity and version of the verification tool or reviewer (e.g., `"coq-8.18.0"`, `"reviewer:alice@example.com"`).

The Dispatcher MUST NOT dereference artifact references.

**Health Status.** A Service's self-reported operational state, communicated through Health messages: HEALTHY (fully operational), DEGRADED (partially operational with reduced capability or capacity), or UNHEALTHY (not accepting requests). The Dispatcher maintains a Health Table and uses Health Status for routing decisions (Section 13.6).

**Message.** The atomic unit of CCDP communication. A Message consists of an Envelope and a Content payload, encoded as a JSON-RPC 2.0 request or response. Messages are typed by the `envelope.type` field (Section 7).

**Message Type.** The classification of a CCDP Message by its protocol function. The defined Message Types are: REQUEST, RESPONSE, NOTIFICATION, ESCALATION, HEALTH_REQUEST, HEALTH_RESPONSE, and DECOMPOSITION_RESULT (Section 7.2).

**Priority.** The scheduling priority of a Request: LOW, NORMAL, HIGH, or CRITICAL. Carried in the `priority` envelope field. Used by Services for internal scheduling and by the Dispatcher as a routing tiebreaker.

**Provenance.** Structured metadata documenting the epistemic status of a cognitive output: the Provenance Grade, the Evidence supporting it, the Service that produced it, and the computational resources consumed. Provenance is REQUIRED on RESPONSE messages, DECOMPOSITION_RESULT messages (because decomposition grades participate in composed provenance — Section 10.5.3), and ESCALATION messages that carry partial cognitive output. See Section 10.

**Provenance Grade.** An ordinal classification of the evidence strength behind a cognitive output. The defined grades, from weakest to strongest, are: OPAQUE, ASSERTED, HEURISTIC, COMPUTED, VALIDATED, CROSS_CHECKED, FORMALLY_VERIFIED, and HUMAN_ATTESTED. Grades propagate through composed operations according to defined composition rules (Section 10).

**Received vs Derived.** *Received* Content and Provenance are values supplied by a Service in a Response, an Escalation, or by a Requester in a Request. The Dispatcher MUST NOT mutate received values — it forwards them as-is (modulo Dispatcher-mutable envelope fields listed in Section 15.4.4). *Derived* Content and Provenance are values the Dispatcher constructs during decomposition plan execution: sub-request Content assembled from plan templates and resolved `$ref` references, and composed Provenance computed from sub-result grades using the composition rules in Section 10.5. Creating derived values from a plan specification is a structural operation; the Dispatcher never generates derived content through cognitive reasoning. Where this specification says "MUST NOT modify Content" or "MUST NOT modify Provenance," it means received values. Derived values are created, not modified.

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
