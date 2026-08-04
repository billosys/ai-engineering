# 20. Version History

This section records notable changes between published draft versions of this
specification. It is informative.

## 20.1. Version 0.2.0

Version 0.2.0 is the second reviewed draft, incorporating the unreleased v0.2 review iterations listed in the README.
The wire protocol version remains `"1.0"` during this draft cycle.

### 20.1.1. Document Status and Conventions

Distinguished document version (`0.2.0`) from wire protocol version (`"1.0"`).
Adopted W3C Trace Context formatting for `trace_id` and `span_id`. Clarified
normative status of examples, tables, and diagrams.

### 20.1.2. Terminology

Defined normative Evidence entry schema with structured `artifact_ref` (object),
`method` field, and `verified_by`. Clarified that Decomposition Plan result
references (typed JSON Pointer `$ref`) are distinct from Artifact References.

### 20.1.3. Dispatcher Model

Replaced "dumb dispatcher" with the Coordinator Dispatcher model: a constrained
protocol enforcement and execution coordinator, not a cognitive reasoner.
Distinguished Structural Validation from Semantic Interpretation (reserved for
Services).

### 20.1.4. Message Format

Added a per-message required-field matrix; made DECOMPOSITION_RESULT
`provenance` REQUIRED (participates in composed provenance, Section 10.5.3).
Clarified envelope opacity: the Dispatcher reads the Envelope for routing and
enforcement; Content is semantically opaque but structurally validated. Added
conditional `destination_id` signing: when non-null, included in
requester-outbound signing scope and immutable. Changed oversized-message
handling to HTTP 413.

### 20.1.5. Capability Registry

Split `supported_evidence_types` into `supported_evidence_methods` and
`supported_artifact_types` under `provenance_capabilities`. Added typed
Escalation Chain entries, the `cacheable` field, and schema-selection rules.

### 20.1.6. Routing

Replaced ambiguous routing outcomes with deployment-configured policies. Added
provenance-grade filtering, evidence-capability filtering, and post-receipt
provenance validation with explicit failure behavior (reroute or
`PROVENANCE_BELOW_REQUIREMENT` escalation). Added routing-audit requirements.

### 20.1.7. Provenance and Evidence

Made the grade ordering (0–7) explicitly numeric and a policy order, not a
universal epistemic hierarchy. Replaced `min_grade` with `min_policy_grade`,
`required_methods`, and `required_evidence_types`. Made FORMALLY_VERIFIED
evidence metadata mandatory. Added composed provenance rules for decomposition
results. Changed escalation provenance SHOULD to MUST for composed/rerouted
responses.

### 20.1.8. Audit

Introduced `audit_schema_version`. Split normative audit requirements into
record-level common fields (Table 11.1) and per-message-type fields (Table
11.2) using canonical JSON paths. Added `audit_failure_policy` (`fail_closed`,
`buffer`; `degrade` non-conformant outside development). Added Full-conformance
tamper-evidence requirements.

### 20.1.9. Flow Control and Errors

Renamed `CONFIDENCE_BELOW_THRESHOLD` to `PROVENANCE_BELOW_REQUIREMENT`,
covering grade, method, and artifact requirements. Required `trace_id`,
`request_id`, and `timestamp` in every error `data` object. Added
decomposition-limit diagnostics (`-32012`) and Dispatcher rate-limit error
(`-32014`). Distinguished Service-generated from Dispatcher-generated
`PROVENANCE_BELOW_REQUIREMENT` escalations via `escalation_origin`. Defined
deterministic routing for Dispatcher-generated provenance escalations:
post-receipt mismatch walks the responding Service's escalation chain;
no-candidate unavailability routes directly to `org.ccdp.human_review`.

### 20.1.10. Decomposition

Replaced string-template result references with typed JSON Pointer `$ref`
objects relative to Response `content`. Made `depends_on` arrays authoritative.
Added `org.ccdp.composition` capability for semantic composition. Added
decomposition-bomb mitigations (depth, width, total-node limits). Standardized
fallback matrix on `on_sub_failure`, `on_composition_failure`, and
`$ref.fallback`. Required derived provenance evidence for composed responses.

### 20.1.11. Security

Defined JCS signing input with requester-outbound and service-response profiles.
Made signing required for Full Services producing FORMALLY_VERIFIED or
HUMAN_ATTESTED responses, covering both `envelope` and `content` components.
Added conditional `destination_id` mutability: excluded from signing when null,
signed and immutable when requester-specified. Added PKCE, JWT introspection,
proof-of-possession, and shared HA replay-cache requirements.

### 20.1.12. Conformance

Reorganized Dispatcher conformance into stable requirement tables
(`DISP-CORE-NNN`, `DISP-FULL-NNN`, `DISP-OPT-NNN`). Service and Registry
stable-ID tables deferred (Section 18). Split Decomposition Plan validation
(Core) from execution (Full).

### 20.1.13. Security Considerations and Open Questions

Distinguished structural Content operations from semantic interpretation.
Expanded mitigations for Registry poisoning, decomposition bombs, and timing
side channels. Remapped security baseline to NSA/CISA AI deployment guidance.
Added Section 18 documenting five deferred design questions.

## 20.2. Version 0.1.0

Version 0.1.0 was the initial reviewed draft. It introduced the core
architecture: star topology centered on a Dispatcher, heterogeneous cognitive
Services behind typed Capability Records, Provenance Grades from OPAQUE through
HUMAN_ATTESTED, Escalation as a first-class operation, mandatory structured
audit trail, cost budgets, deadlines, retries, circuit breakers, Decomposition
as a first-class Service, and a security baseline covering mTLS, bearer tokens,
message signing, replay protection, and isolation.

The v0.1 review identified the main issues that v0.2 addresses: Dispatcher role
ambiguity, JSON-RPC response semantics, document vs wire versioning,
single-ladder provenance overclaiming, routing ambiguity, JSON Schema
compatibility enforceability, audit failure behavior, decomposition safety, and
security/reference precision.
