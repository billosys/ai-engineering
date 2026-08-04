# 16. Conformance

## 16.1. Conforming Dispatcher

A conforming Dispatcher MUST implement all of the following:

### 16.1.1. Message Processing

1. Parse all CCDP message types defined in Section 7.2.
2. Validate envelope structure: reject messages with missing REQUIRED fields or invalid field types (Section 7.3).
3. Validate `ccdp_version`: reject messages with unrecognized versions.
4. Preserve and forward all unknown `metadata` fields without modification (Section 7.7).

4a. Respect metadata directionality: keys in `org.ccdp.request.*` are request-directional (preserve on forwarded requests, do not copy to responses); keys in `org.ccdp.response.*` are response-directional (preserve on forwarded responses, do not copy to subsequent requests). Keys with sensitivity labels (defined by deployment policy) MUST be stripped at administrative domain boundaries. Keys without a directional prefix are bidirectional.
5. Never perform semantic interpretation of message Content — never reason about what content means, never make routing decisions based on content meaning. The Dispatcher MAY perform structural validation (JSON Schema checking) and structural operations (typed-reference resolution, template assembly, size checks) on Content as specified in Sections 7, 8, and 14. See the Structural Validation vs Semantic Interpretation definition in Section 4.
6. Never modify message Content.
7. Never modify Provenance grades, Evidence entries, or composition traces.

### 16.1.2. Authentication and Authorization

8. Authenticate all incoming messages (Section 15.2).
9. Reject unauthenticated messages with error `-32008`.
10. Enforce capability-based authorization: reject requests for unauthorized Capability Types with error `-32009` (Section 15.3).
11. Validate bearer token scopes, expiration, and cost limits.

### 16.1.3. Routing

12. Implement the routing algorithm defined in Section 9.2.
13. Query the Registry for service lookup (Section 8.4.2).
14. Filter candidates by health status, deadline, and provenance requirement.
15. Route escalations through the Escalation Chain (Section 13.4).
16. Log all routing decisions in the audit trail.

### 16.1.4. Schema Validation

17. Validate Request Content against the target Service's input schema before forwarding (Section 8.2.2).
18. Validate Response Content against the Service's output schema before forwarding to the requester. For CCDP Core conformance, this validation is RECOMMENDED. For CCDP Full conformance, this validation is REQUIRED.

### 16.1.5. Deadline Enforcement

19. Propagate deadline and `remaining_budget_ms` at every hop (Section 12.4).
20. Reject requests that have already exceeded their deadline with error `-32007`.

### 16.1.6. Audit

21. Generate a structured audit record for every message processed (Section 11.2).
22. Record all mandatory audit fields (Section 11.4).
23. Propagate W3C Trace Context (Section 11.3).

### 16.1.7. Health Monitoring

24. Probe Service health at the intervals specified in Capability Records (Section 13.6).
25. Maintain a routing table with health status and circuit breaker state (Section 9.7).
26. Implement circuit breaker logic (Section 9.6).

### 16.1.8. Security

27. Require TLS 1.3 or later for all Service communication (Section 15.2).
28. Implement replay protection (Section 15.5).
29. Never execute or interpret Content (Section 15.6.2).
30. Redact bearer tokens in audit logs (Section 15.7).

### 16.1.9. Decomposition Execution

31. Validate Decomposition Plans received from a Decomposition Service: acyclic dependency graph, valid capability types, valid resource allocations, width and total-node limits (Section 14). [CORE]
32. Execute Decomposition Plans: dispatch sub-requests, resolve typed result references, compose results using structural methods (template, concatenation, selection). Route custom composition to an `org.ccdp.composition` Service. [FULL]
33. Enforce maximum decomposition depth, width, and total-node limits (Section 14.6). [CORE for validation, FULL for execution]

## 16.2. Conforming Service

A conforming Service MUST implement all of the following:

### 16.2.1. Protocol Compliance

1. Accept CCDP Request messages and return CCDP Response, Escalation, or Error messages (Section 7).
2. Include the `ccdp_version` field on all messages.
3. Use the `request_id` from the Request on the corresponding Response.
4. Preserve and forward all unknown `metadata` fields from the Request to the Response.

### 16.2.2. Contract Compliance

5. Accept only Requests whose Content conforms to the registered input schema.
6. Produce Responses whose Content conforms to the registered output schema.
7. Reject malformed Requests with a CCDP error response rather than attempting to interpret them.

### 16.2.3. Provenance

8. Include a `provenance` field on every Response and Escalation (Section 10).
9. Assign an accurate Provenance Grade following the grade assignment rules (Section 10.3).
10. Include Evidence entries substantiating any grade above ASSERTED.
11. Include the `scope` field for FORMALLY_VERIFIED grades.
12. Report computational resource consumption in `provenance.computation`.

### 16.2.4. Escalation

13. Return an Escalation (not a low-provenance-grade Response) when the Service cannot meet the Request's `provenance_requirement.min_grade` (Section 13.3).
14. Return an Escalation when the Request would exceed the `cost_budget`.
15. Return an Escalation when the `remaining_budget_ms` is insufficient to complete the work.
16. Include `partial_result_available` on all Escalations.

### 16.2.5. Idempotency

17. For the same `request_id`, return the same Response without re-executing the request (Section 7.3.1). Implementations SHOULD maintain a response cache keyed by `request_id` with a configurable TTL (RECOMMENDED: 24 hours).

### 16.2.6. Health

18. Respond to HEALTH_REQUEST messages with accurate HEALTH_RESPONSE messages (Section 7.3.6).
19. Report accurate health status: HEALTHY, DEGRADED, or UNHEALTHY.
20. Report per-capability availability when implementing multiple Capability Types.

### 16.2.7. Security

21. Verify the Dispatcher's identity on incoming connections (mTLS certificate verification, Section 15.2.1).
22. Reject connections from unrecognized Dispatchers.

### 16.2.8. Deadline Compliance

23. Respect the `remaining_budget_ms` field.
24. Return an Escalation with reason `DEADLINE_INSUFFICIENT` or `DEADLINE_APPROACHING` rather than exceeding the deadline silently.

## 16.3. Conforming Registry

A conforming Registry MUST implement all of the following:

### 16.3.1. Operations

1. Support the Register operation (Section 8.4.1).
2. Support the Lookup operation (Section 8.4.2).
3. Support the Get operation (Section 8.4.3).
4. Support the Deregister operation (Section 8.4.4).
5. Support the List Schema Versions operation (Section 8.4.5).

### 16.3.2. Schema Management

6. Store and return input and output JSON Schemas for each Capability Record.
7. Track schema versions using Semantic Versioning [SemVer].
8. Enforce compatibility rules for PATCH and MINOR version updates (Section 8.5.2). Compatibility enforcement covers the practical subset defined in Section 8.5: additive properties for MINOR, identical structure for PATCH, and structural-breaking detection for MAJOR. General JSON Schema equivalence is undecidable; the Registry MAY require operator attestation for compatibility decisions that exceed automated checking capability (Section 8.5).
9. Support transition periods for MAJOR version updates (Section 8.5.4).

### 16.3.3. Security

10. Authenticate all Registry modification operations (register, update, deregister).
11. Log all modifications with the modifier's identity and timestamp.
12. Validate that registered schemas are well-formed JSON Schema before accepting.

### 16.3.4. Availability

13. Respond to Lookup queries within a bounded time (RECOMMENDED: 99th percentile under 100ms).
14. Retain deregistered records for audit purposes (Section 8.4.4).

## 16.4. Conformance Levels

Implementations MAY claim conformance at one of two levels:

**CCDP Core:** Implements all MUST requirements for the relevant component type (Dispatcher, Service, or Registry). This is the minimum for interoperability.

**CCDP Full:** Implements all MUST and SHOULD requirements. Includes application-level message signing, cryptographic audit integrity, and advanced routing features (provenance-aware ranking, decomposition execution, recursive decomposition).

Implementations MUST declare their conformance level in their documentation and in the Registry (for Services) via a `metadata` field: `"org.ccdp.conformance_level": "core"` or `"org.ccdp.conformance_level": "full"`.

## 16.5. Interoperability

A CCDP Core Dispatcher MUST be able to communicate with any CCDP Core Service. A CCDP Full Dispatcher MUST be able to communicate with both CCDP Core and CCDP Full Services. Differences in conformance level MUST NOT cause protocol errors — they MAY result in reduced functionality. A CCDP Core Dispatcher MUST validate Decomposition Plans but is not required to execute them. A Core Dispatcher MAY route decomposition requests to a human queue, an external orchestrator, or return error `-32002` (no service for capability) if no decomposition executor is available. A CCDP Full Dispatcher MUST execute valid Decomposition Plans.

Unknown metadata fields from a higher conformance level MUST be preserved and forwarded, ensuring that Full implementations can exchange extended metadata through a Core intermediary.

## 16.6. Conformance Testing

A future companion document will define a conformance test suite for CCDP Core and Full implementations. Each MUST requirement in this section is intended to correspond to one or more testable assertions. Implementations claiming conformance SHOULD publish their test results against the conformance suite when it becomes available.

Until the conformance suite is available, implementations SHOULD self-test against the following minimum verification:

1. Send a valid REQUEST and verify correct routing and RESPONSE.
2. Send a REQUEST with an invalid envelope and verify error `-32602`.
3. Send a REQUEST for an unauthorized capability and verify error `-32009`.
4. Trigger an escalation and verify correct escalation chain processing.
5. Submit a Decomposition Plan and verify sub-request dispatch and result composition (Full only).
6. Verify that unknown metadata keys survive a round-trip through the Dispatcher.
7. Verify that provenance fields are not modified by the Dispatcher.
