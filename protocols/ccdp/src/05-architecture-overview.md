# 5. Architecture Overview

## 5.1. Topology

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

## 5.2. Component Roles

A CCDP system comprises four kinds of components. Each has a defined role and a defined boundary of responsibility.

### 5.2.1. The Dispatcher

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

### 5.2.2. Services

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

### 5.2.3. The Registry

The Capability Registry stores Capability Records and answers queries from the Dispatcher. Its responsibilities are:

- **Capability storage**: Maintain the current Capability Record for every registered Service, including schemas, cost hints, health endpoints, and isolation requirements.
- **Schema versioning**: Track schema versions for each Capability Type and enforce compatibility rules at registration time (Section 8.5).
- **Routing queries**: Answer Dispatcher queries of the form "which Services implement Capability Type X?" with a list of matching Services, their endpoints, cost hints, and health status.
- **Health aggregation**: Optionally aggregate Health Status from Services and include it in routing query responses.

The Registry interface is defined in Section 8. The storage backend is not specified — implementations MAY use a database, a configuration file, a distributed key-value store, or any other mechanism that satisfies the interface contract.

### 5.2.4. The Human Supervisor

The Human Supervisor occupies the top of the supervision tree. The Human Supervisor is not a CCDP component in the protocol sense — the protocol does not specify the human interface — but the protocol is designed to support human supervision:

- Escalation Chains terminate at a human review queue (a Service of Mode 4 — Section 5.3).
- Audit Trails provide the Human Supervisor with complete visibility into every routing decision, service invocation, and provenance grade (Section 11).
- The Dispatcher MAY be configured to require Human Supervisor approval for routing decisions above a cost threshold or below a provenance-grade threshold.
- The Provenance system's HUMAN_ATTESTED grade is the highest epistemic grade, reflecting the irreducible role of human judgment in specification and value assessment.

## 5.3. Service Modes

A Service's implementation is opaque to the Dispatcher — the Dispatcher routes to a typed interface, not to an implementation. However, this specification recognizes four implementation patterns (Service Modes) because they produce structurally different Provenance characteristics:

### 5.3.1. Mode 1: LLM Alone

The Service is an LLM endpoint. Requests are natural-language prompts (or structured prompts); responses are natural-language completions. Typical Provenance Grade: ASSERTED or HEURISTIC.

Mode 1 is appropriate for language-native tasks: drafting, brainstorming, translation, summarization, natural-language understanding. The LLM's native strength is the crystallize → serialize → deserialize → instantiate translation loop — getting concepts between representations.

Mode 1 is not appropriate for tasks requiring deductive correctness, sound planning, or verifiable selection — the forward-pass ceiling (TC⁰) and self-correction limits make these structurally unreliable without external verification.

### 5.3.2. Mode 2: Deterministic Service Alone

The Service is a theorem prover, SMT solver, classical planner, database, calculator, or other deterministic engine. Requests are formal inputs (logical formulas, PDDL domains, SQL queries); responses are verified outputs. Typical Provenance Grade: COMPUTED or FORMALLY_VERIFIED.

Mode 2 is appropriate for tasks with formal specifications: proof checking, plan validation, constraint solving, data retrieval. The output is correct by construction given correct input — the remaining failure mode is input correctness, not computation correctness.

### 5.3.3. Mode 3: LLM + Deterministic Service Composite

The most architecturally significant mode. An LLM sits in front of a deterministic service as a translator: it converts a natural-language request into the service's formal input language, passes it through, and converts the formal output back to natural language. From the Dispatcher's perspective, this is a single Service with a single typed interface — the internal LLM translation layer is not visible in the protocol.

This is the "LLM proposes, engine disposes" pattern [PAL; Logic-LM; SatLM; LLM-Modulo]. The Provenance Grade of the output depends on how much of the result rests on the deterministic engine versus the LLM translation: if the LLM's contribution is limited to translation and the engine verifies the result, the grade may be VALIDATED or FORMALLY_VERIFIED with an Evidence entry documenting the verification. If the translation itself is uncertain, the Provenance should reflect that uncertainty.

Mode 3 is the primary path for expanding the system's capabilities: tasks that cannot be handled by Mode 2 alone (because they require natural-language understanding at the input boundary) and cannot be trusted to Mode 1 alone (because they require correctness guarantees at the output boundary).

### 5.3.4. Mode 4: Human Queue

The Service is a human review queue. Requests are placed in a queue for human processing; responses arrive when a human completes the task and submits a result in the typed format. From the Dispatcher's perspective, the interface is identical — same envelope, same content schema, same provenance — just slower and more expensive.

Typical Provenance Grade: HUMAN_ATTESTED (the highest grade).

Mode 4 is appropriate for tasks requiring irreducible human judgment: specification review, value/novelty assessment, broad abstraction, and any task for which no external organ produces reliable output. Mode 4 is also the default Escalation target: when automated Services cannot meet the requested provenance grade, the Escalation Chain terminates at a human queue.

### 5.3.5. Mode Substitution and Progressive Automation

The four modes share a critical property: **modes are interchangeable without changing the Dispatcher's routing logic.** A Capability Type that starts as Mode 4 (human does everything behind a typed interface) can be progressively replaced with Mode 3 (LLM + deterministic service) and then Mode 2 (deterministic service alone) as tooling matures — without changing the Dispatcher, the Registry schemas, or any other Service's integration.

This is the architectural basis for incremental automation: start with everything in Mode 4 and the Dispatcher is trivially simple (a message router to human queues). Then, one Service at a time, substitute in a more automated implementation. The Dispatcher never gets smarter; the Services behind it get more capable.

Mode substitution has multiple protocol-visible effects: Provenance Grade, cost (different modes have different cost profiles), latency, evidence entries (different methods produce different evidence), signing (some modes may not support signing), and isolation properties. For example, a Mode 2 replacement will report FORMALLY_VERIFIED where the Mode 4 predecessor reported HUMAN_ATTESTED. Consumers of the output can use the Provenance Grade to calibrate their trust — the protocol ensures the change in backing implementation is transparent through the epistemic metadata. Mode substitution is transparent only when the consumer's `provenance_requirement.min_grade` is met by the replacement mode's typical grade. A consumer requiring `HUMAN_ATTESTED` cannot be served by a Mode 2 replacement reporting `FORMALLY_VERIFIED` unless the consumer's policy accepts formal verification as equivalent for that claim type. Deployments SHOULD configure mode-substitution policies per capability type that account for all these effects, not just provenance.

## 5.4. The Decomposition Service

Decomposition — breaking a complex request into typed sub-requests — is itself a cognitive act. Rather than requiring the Dispatcher to perform decomposition (which would violate the constrained-coordinator principle) or requiring the human to pre-decompose all requests (which does not scale), CCDP treats decomposition as a first-class Service with Capability Type `org.ccdp.decomposition`.

The Decomposition Service receives a complex Request and returns a Decomposition Plan: a set of typed sub-requests, their dependency ordering (which sub-requests can run in parallel, which must be sequential), and a composition function specifying how sub-results are assembled into the final result.

The Dispatcher then routes each sub-request independently through the normal routing process. Sub-requests carry the same `trace_id` as the parent and new `span_id` values, linking them in the audit trail. Results are composed according to the Decomposition Plan's composition specification.

Result composition is a structural operation: the Dispatcher assembles typed sub-results according to the plan's composition specification (template assembly, concatenation, or selection) without reasoning about what the sub-results mean. When composition requires cognitive judgment (e.g., synthesizing sub-results into a coherent narrative), the plan routes composition to a dedicated Composition Service with capability type `org.ccdp.composition` (Section 14.3.4).

Because the Decomposition Service is behind the same typed interface as every other Service, it is subject to the same audit, provenance, health-check, and escalation discipline. A Decomposition Plan carries its own Provenance Grade (reflecting the evidence strength behind the decomposition itself), and if the Decomposition Service cannot decompose a request, it returns an Escalation rather than producing a bad decomposition silently.

The Decomposition Service is a natural Mode 3 candidate: an LLM translates a natural-language request into a structured decomposition plan, which a validator then checks for consistency (all sub-requests have valid Capability Types, dependencies are acyclic, the composition function references all sub-results). The validated decomposition carries a higher Provenance Grade than the raw LLM decomposition.

Decomposition is detailed in Section 14.

## 5.5. Relationship to Supervision Trees

CCDP's architecture maps to the classic supervision-tree model:

- **The Human Supervisor is the top supervisor.** Holds the specification and value/novelty judgment — the irreducible inputs. Owns the restart policy: what counts as a known-good state.
- **The Dispatcher is the intermediate supervisor.** Routes messages to worker processes, monitors health, restarts (reroutes around) failed workers, and escalates to the top supervisor when no worker can handle the request.
- **Services are worker processes.** Each supervised, each with a typed protocol on its wire. They crash loudly (return structured errors or Escalations) rather than silently emitting corrupt output.
- **"Let it crash" is the failure discipline.** A Service that fails — an unsound plan, a vacuous proof, a mistranslation — crashes loudly and its failure is named, logged, and routed to the Escalation Chain. The output is not forwarded. This is the direct antidote to silent failures.
- **Typed protocols on the wires.** Every link between Dispatcher and Service is a typed contract enforced by the Registry. Malformed messages are rejected at the boundary. This is the supervision tree's process isolation principle expressed as protocol enforcement.

The key property inherited from OTP: you build reliable systems from unreliable components not by making the components correct, but by strong isolation, message-passing-only interaction, supervision, and restart from a known-good state [Armstrong 2003].
