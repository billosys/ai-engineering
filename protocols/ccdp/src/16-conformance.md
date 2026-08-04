# 16. Conformance

## 16.1. Conforming Dispatcher

Dispatcher conformance requirements are organized by conformance level rather than by function. Each requirement has a stable identifier (`DISP-CORE-NNN`, `DISP-FULL-NNN`, or `DISP-OPT-NNN`) for cross-reference and conformance testing. The `Source Section` column identifies where the requirement's substantive rules are defined.

### 16.1.1. Core Dispatcher Requirements

A CCDP Core Dispatcher MUST satisfy all requirements in this table.

| ID | Requirement | Source Section |
|---|---|---|
| DISP-CORE-001 | Parse all CCDP message types. | 7.2 |
| DISP-CORE-002 | Validate envelope structure: reject messages with missing REQUIRED fields or invalid field types. | 7.3 |
| DISP-CORE-003 | Validate `ccdp_version`: reject messages with unrecognized versions. | 7.3.1 |
| DISP-CORE-004 | Preserve and forward all unknown `metadata` fields without modification. | 7.7 |
| DISP-CORE-005 | Respect metadata directionality: `org.ccdp.request.*` keys are request-directional, `org.ccdp.response.*` keys are response-directional, keys without a directional prefix are bidirectional. Strip sensitivity-labeled keys at administrative domain boundaries. | 7.7 |
| DISP-CORE-006 | Never perform semantic interpretation of message Content. MAY perform structural validation and structural operations (typed-reference resolution, template assembly, size checks). | 4, 7, 8, 14 |
| DISP-CORE-007 | Never mutate received Content. Derived Content constructed during Decomposition Plan execution is a structural operation, not a modification of received values. | 4 (Received vs Derived) |
| DISP-CORE-008 | Never mutate received Provenance grades, Evidence entries, or composition traces. Derived Provenance computed from sub-result grades during plan execution is a structural operation, not a modification of received values. | 4 (Received vs Derived), 10.5 |
| DISP-CORE-009 | Authenticate all incoming messages. | 15.2 |
| DISP-CORE-010 | Reject unauthenticated messages with error `-32008`. | 15.2 |
| DISP-CORE-011 | Enforce capability-based authorization: reject requests for unauthorized Capability Types with error `-32009`. | 15.3 |
| DISP-CORE-012 | Validate bearer token scopes, expiration, and cost limits. | 15.3.2 |
| DISP-CORE-013 | Implement the routing algorithm. | 9.2 |
| DISP-CORE-014 | Query the Registry for service lookup. | 8.4.2 |
| DISP-CORE-015 | Filter candidates by health status, deadline, and provenance requirement (`min_policy_grade`, `required_methods`, `required_evidence_types`). | 9.2 |
| DISP-CORE-016 | Route escalations through the Escalation Chain, including authorization/budget/isolation checks on suggested and chain targets. | 13.4, 9.4 |
| DISP-CORE-017 | Log all routing decisions in the audit trail. | 9.2 |
| DISP-CORE-018 | Propagate deadline and `remaining_budget_ms` at every hop. | 12.4 |
| DISP-CORE-019 | Reject requests that have already exceeded their deadline with error `-32007`. | 13.2 |
| DISP-CORE-020 | Generate a structured audit record for every message processed. | 11.2 |
| DISP-CORE-021 | Record all mandatory audit fields per the per-message-type matrix. | 11.4 |
| DISP-CORE-022 | Propagate W3C Trace Context. | 11.3 |
| DISP-CORE-023 | Probe Service health at the intervals specified in Capability Records. | 13.6 |
| DISP-CORE-024 | Maintain a routing table with health status and circuit breaker state. | 9.7 |
| DISP-CORE-025 | Implement circuit breaker logic. | 9.6, 13.6.2 |
| DISP-CORE-026 | Require TLS 1.3 or later for all Service communication. | 15.2 |
| DISP-CORE-027 | Implement replay protection. | 15.5 |
| DISP-CORE-028 | Never execute or interpret Content. | 15.6.2 |
| DISP-CORE-029 | Redact bearer tokens in audit logs. | 15.7 |
| DISP-CORE-030 | Validate Decomposition Plans received from a Decomposition Service: acyclic dependency graph, valid capability types, valid resource allocations, and depth/width/total-node limits. A Core Dispatcher validates plans but is not required to execute them (Section 16.5). | 14, 14.6 |

### 16.1.2. Full Dispatcher Requirements

A CCDP Full Dispatcher MUST satisfy all Core requirements plus all requirements in this table.

| ID | Requirement | Source Section |
|---|---|---|
| DISP-FULL-001 | Validate Request Content against the target Service's input schema before forwarding. | 8.2.2 |
| DISP-FULL-002 | Validate Response Content against the Service's output schema before forwarding to the requester. | 8.2.2 |
| DISP-FULL-003 | Execute Decomposition Plans: dispatch sub-requests, resolve typed result references, compose results using structural methods (template, concatenation, selection). Route custom composition to an `org.ccdp.composition` Service. | 14.4 |
| DISP-FULL-004 | Enforce maximum decomposition depth, width, and total-node limits during recursive execution. | 14.6 |
| DISP-FULL-005 | Support recursive decomposition (nested Decomposition Plans). | 14.6 |
| DISP-FULL-006 | Verify application-level message signatures on responses at grade FORMALLY_VERIFIED or HUMAN_ATTESTED before forwarding. | 15.4.2 |
| DISP-FULL-007 | Write audit records to a tamper-evident store (cryptographic chaining, integrity-verified append-only storage, or write-once medium). | 11.5 |
| DISP-FULL-008 | Support provenance-aware ranking in routing, including grade thresholds (where `typical_grade` meets or exceeds `min_policy_grade`) and declared support for required evidence methods and artifact types. | 9.2 |

### 16.1.3. Optional Capabilities

The following capabilities are optional at any conformance level. Implementations that support them MUST follow the specified behavior.

| ID | Capability | Behavior | Source Section |
|---|---|---|---|
| DISP-OPT-001 | Message signing for responses below grade FORMALLY_VERIFIED/HUMAN_ATTESTED | RECOMMENDED; when implemented, follows the same canonicalization and signing-profile rules as required signing. | 15.4.2, 15.4.4 |
| DISP-OPT-002 | Workload attestation | When implemented, the Service provides a signed attestation that its runtime matches declared isolation requirements. | 15.6.1 |
| DISP-OPT-003 | Registry query caching and stale-cache fallback | When implemented, cached results MAY be used during brief Registry outages; staleness MUST be logged in the audit trail. | 8.6 |
| DISP-OPT-004 | Static routing table fallback | When implemented, used only if both the Registry and its cache are unavailable; MUST be logged in the audit trail. | 8.6 |
| DISP-OPT-005 | Per-Service rate limiting based on capacity advertisements | When implemented, follows the load-shedding behavior described in Section 12.5; all rate-limiting decisions MUST be logged. | 12.5 |
| DISP-OPT-006 | Token validation decision caching | When implemented, bounded by a deployment-configured maximum TTL (RECOMMENDED: 300 seconds); raw token strings MUST NOT be retained beyond the request-processing lifetime. | 15.7 |

## 16.2. Conforming Service

A conforming Service MUST implement all of the following:

### 16.2.1. Protocol Compliance

1. Accept CCDP Request messages and return CCDP Response, Escalation, or Error messages (Section 7).
2. Include the `ccdp_version` field on all messages.
3. Use the `request_id` from the Request on the corresponding Response.
4. Preserve and forward all unknown `metadata` fields from the Request to the Response. Services MUST respect metadata directionality: keys in `org.ccdp.request.*` are request-directional and SHOULD NOT be copied to Response messages. Keys in `org.ccdp.response.*` are response-directional. Keys without a directional prefix are bidirectional and MUST be preserved.

### 16.2.2. Contract Compliance

5. Accept only Requests whose Content conforms to the registered input schema.
6. Produce Responses whose Content conforms to the registered output schema.
7. Reject malformed Requests with a CCDP error response rather than attempting to interpret them.

### 16.2.3. Provenance

8. Include a `provenance` field on every Response and on every Escalation that carries partial cognitive output (`partial_result_available: true`). Escalations representing pure routing failures (no cognitive output) MAY omit provenance; the implicit grade is OPAQUE. See Section 7.3.8.
9. Assign an accurate Provenance Grade following the grade assignment rules (Section 10.3).
10. Include Evidence entries substantiating any grade above ASSERTED.
11. Include the `scope` field for FORMALLY_VERIFIED grades.
12. Report computational resource consumption in `provenance.computation`.

### 16.2.4. Escalation

13. Return an Escalation (not a low-provenance-grade Response) when the Service cannot meet the Request's `provenance_requirement` (Section 13.3).
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

**CCDP Core:** Implements all MUST requirements applicable to the relevant component type (Dispatcher, Service, or Registry) throughout this specification. For the Dispatcher, the Core requirements table (Section 16.1.1) is the authoritative checklist. For Services and Registries, Core conformance is assessed against all normative MUST requirements applicable to their component type — particularly the explicit lists in Sections 16.2 and 16.3, but also applicable requirements in Sections 7, 8, 10, 12, 13, and 15. This is the minimum for interoperability.

**CCDP Full:** Full conformance requires all Core requirements plus all Full requirements listed in Section 16.1.2. Full conformance tables with stable requirement IDs are defined for the Dispatcher (Section 16.1) only. Service and Registry Full conformance tables are an open item — see Section 18 (Open Questions). Until those tables are defined, Services and Registries conform to all normative MUST requirements applicable to their component type, without a Core/Full distinction. SHOULD-level recommendations throughout the specification are best practices, not Full conformance obligations. Full conformance is defined by the explicit Full requirements tables, not by the sum of all SHOULD statements.

Implementations MUST declare their conformance level in their documentation and in the Registry (for Services) via a `metadata` field: `"org.ccdp.conformance_level": "core"` or `"org.ccdp.conformance_level": "full"`.

## 16.5. Interoperability

A CCDP Core Dispatcher MUST be able to communicate with any CCDP Core Service. A CCDP Full Dispatcher MUST be able to communicate with both CCDP Core and CCDP Full Services. Differences in conformance level MUST NOT cause protocol errors — they MAY result in reduced functionality. A CCDP Core Dispatcher MUST validate Decomposition Plans but is not required to execute them. A Core Dispatcher MAY route decomposition requests to a human queue, an external orchestrator, or return error `-32002` (no service for capability) if no decomposition executor is available. A CCDP Full Dispatcher MUST execute valid Decomposition Plans.

Unknown metadata fields from a higher conformance level MUST be preserved and forwarded, ensuring that Full implementations can exchange extended metadata through a Core intermediary.

## 16.6. Conformance Testing

**Implementation note.** Several Dispatcher conformance requirements reference evidence filtering (DISP-CORE-015), mandatory audit fields, and message signatures. The testability of these requirements depends on the normative Evidence object schema (Section 4), the audit record tables (Section 11), and the signing grammar (Section 15). Conformance test suites SHOULD be developed after those schemas are finalized.

A future companion document will define a conformance test suite for CCDP Core and Full implementations. Each Dispatcher requirement identifier in Section 16.1, and each prose-numbered Service and Registry requirement in Sections 16.2 and 16.3, is intended to correspond to one or more testable assertions. Implementations claiming conformance SHOULD publish their test results against the conformance suite when it becomes available.

The conformance test suite and companion schemas are implementation prerequisites not yet published. Section 7.8 lists the planned schema inventory. Until both are available, implementations SHOULD self-test against the verification checklist below.

1. Send a valid REQUEST and verify correct routing and RESPONSE.
2. Send a REQUEST with an invalid envelope and verify error `-32602`.
3. Send a REQUEST for an unauthorized capability and verify error `-32009`.
4. Trigger an escalation and verify correct escalation chain processing.
5. Submit a Decomposition Plan and verify sub-request dispatch and result composition (Full only).
6. Verify that unknown metadata keys survive a round-trip through the Dispatcher.
7. Verify that provenance fields are not modified by the Dispatcher.
