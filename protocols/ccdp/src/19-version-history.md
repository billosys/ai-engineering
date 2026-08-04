# 19. Version History

This section records notable changes between published draft versions of this
specification. It is informative and intended to help reviewers understand the
shape of each revision.

## 19.1. Version 0.2.0

Version 0.2.0 is the second reviewed draft of CCDP. It incorporates feedback
from the v0.1 review pass and focuses on resolving architectural consistency,
wire-format precision, conformance clarity, and security/audit semantics. The
wire protocol version remains `"1.0"` during this draft cycle because CCDP has
not yet committed to implementation compatibility.

### 19.1.1. Document Status and Conventions

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

### 19.1.2. Dispatcher Model

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

### 19.1.3. Message Format and Wire Semantics

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

### 19.1.4. Capability Registry

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

### 19.1.5. Routing, Flow Control, and Errors

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

### 19.1.6. Provenance and Evidence

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

### 19.1.7. Audit

- Added an `audit_schema_version` independent of both document and wire
  protocol versions.
- Added per-message-type audit-field requirements.
- Added audit-store failure behavior through `audit_failure_policy`, including
  `fail_closed`, `buffer`, and non-production `degrade` modes.
- Added Full-conformance tamper-evidence requirements for audit records.
- Added Trace Context `tracestate` size and sanitization guidance.
- Clarified that audit trails are supervision inputs as well as compliance
  records.

### 19.1.8. Decomposition and Composition

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

### 19.1.9. Security

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

### 19.1.10. Conformance

- Split Decomposition Plan validation from Decomposition Plan execution:
  validation is Core, execution is Full.
- Clarified Response Content validation as recommended for Core and required
  for Full.
- Added metadata directionality to Dispatcher conformance requirements.
- Added preliminary conformance-testing guidance and a minimum self-test list.
- Added Registry compatibility enforcement language that acknowledges the
  practical JSON Schema subset and operator attestation for edge cases.

## 19.2. Version 0.1.0

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
