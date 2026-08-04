# 20. Version History

This section records notable changes between published draft versions of this
specification. It is informative and intended to help reviewers understand the
shape of each revision.

## 20.1. Version 0.2.0

Version 0.2.0 is the second reviewed draft of CCDP. It incorporates feedback
from the v0.1 review pass and focuses on resolving architectural consistency,
wire-format precision, conformance clarity, and security/audit semantics. The
wire protocol version remains `"1.0"` during this draft cycle because CCDP has
not yet committed to implementation compatibility.

### 20.1.1. Document Status and Conventions

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

### 20.1.2. Dispatcher Model

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

### 20.1.3. Message Format and Wire Semantics

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

### 20.1.4. Capability Registry

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

### 20.1.5. Routing, Flow Control, and Errors

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

### 20.1.6. Provenance and Evidence

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

### 20.1.7. Audit

- Added an `audit_schema_version` independent of both document and wire
  protocol versions.
- Added per-message-type audit-field requirements.
- Added audit-store failure behavior through `audit_failure_policy`, including
  `fail_closed`, `buffer`, and non-production `degrade` modes.
- Added Full-conformance tamper-evidence requirements for audit records.
- Added Trace Context `tracestate` size and sanitization guidance.
- Clarified that audit trails are supervision inputs as well as compliance
  records.

### 20.1.8. Decomposition and Composition

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

### 20.1.9. Security

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

### 20.1.10. Conformance

- Split Decomposition Plan validation from Decomposition Plan execution:
  validation is Core, execution is Full.
- Clarified Response Content validation as recommended for Core and required
  for Full.
- Added metadata directionality to Dispatcher conformance requirements.
- Added preliminary conformance-testing guidance and a minimum self-test list.
- Added Registry compatibility enforcement language that acknowledges the
  practical JSON Schema subset and operator attestation for edge cases.

### 20.1.11. Second-Round v0.2 Refinements

After the initial v0.2 revision, a second review-driven tightening pass made
the following additional changes:

- Replaced the ambiguous `provenance_requirement.min_grade` field with
  `min_policy_grade` and added `required_methods` and
  `required_evidence_types` so callers can require specific evidence methods or
  artifact types, not merely a point on the policy-order ladder.
- Added Capability Record `supported_evidence_types` and updated routing so the
  Dispatcher performs both provenance-grade filtering and declared
  evidence-capability filtering before dispatch, then validates actual response
  evidence after receipt.
- Made the Provenance Grade ladder explicitly numeric (`0` through `7`) for
  routing and conformance, promoted the policy-order caveat into its own
  subsection, rejected same-prompt/same-seed replications as CROSS_CHECKED
  evidence, and made FORMALLY_VERIFIED evidence metadata mandatory rather than
  advisory.
- Tightened audit semantics by aligning examples with `audit_schema_version`,
  string-valued monetary quantities, and `min_policy_grade`; by making the
  per-message-type audit matrix the normative source of required fields; and by
  declaring audit-store `degrade` mode non-conformant outside development and
  debugging.
- Refined Trace Context handling so Dispatchers may omit their own `tracestate`
  entry when truncating other vendors' entries would be unsafe.
- Replaced the old `CONFIDENCE_BELOW_THRESHOLD` escalation reason with
  `PROVENANCE_BELOW_REQUIREMENT`, expanded its meaning to cover evidence-method
  and evidence-artifact requirements, and required every CCDP error `data`
  object to include `trace_id`, `request_id`, and `timestamp`.
- Expanded error handling with structured decomposition-limit diagnostics for
  depth, width, and total-node failures under `-32012`, and added a Dispatcher
  rate-limit error code `-32014` with `retry_after_ms`.
- Clarified escalation routing so Service-suggested targets remain policy
  hints, not overrides, and so human-review fallback is used only when
  authorization and data-class or isolation checks pass.
- Clarified Decomposition Plan execution by making result-reference JSON
  Pointers relative to the referenced Response `content`, making top-level
  `dependencies` informative, defining allowed structural selection criteria,
  adding a fallback behavior matrix, and requiring derived provenance evidence
  for composed responses.
- Tightened decomposition-limit behavior so width and total-node excesses are
  rejected before execution, while depth excesses report the same
  decomposition-limit error with `limit_type: "depth"`.
- Clarified security boundaries by distinguishing protocol requirements from
  deployment enforcement, tightening OAuth/PAR/PKCE language to token issuance
  rather than token validation, defining the exact JCS signing input, adding
  requester and service signing profiles, and allowing bounded token-validation
  decision caching without retaining raw bearer tokens.
- Made high-grade signed responses stronger by requiring FORMALLY_VERIFIED and
  HUMAN_ATTESTED responses to sign both `content` and `provenance` for Full
  conformance.
- Reorganized Dispatcher conformance into stable requirement tables with
  `DISP-CORE-NNN`, `DISP-FULL-NNN`, and `DISP-OPT-NNN` identifiers, while
  clarifying that Full conformance is defined by explicit Full requirements
  rather than by all SHOULD statements in the document.
- Updated security considerations to distinguish structural Content operations
  from semantic interpretation, expand Registry poisoning mitigations, clarify
  decomposition-limit defaults as recommendations rather than fixed numeric
  requirements, and remap the security baseline to general NSA/CISA AI
  deployment guidance rather than an MCP-specific assessment.
- Completed a reference/link verification pass for this draft, renaming the
  NSA/CISA reference, updating the A2A specification URL, noting the normative
  dependency on Informational RFC 8785, and flagging bot-blocked reference URLs
  for human browser confirmation.
- Updated the source README to record the second-round status, current
  implementation blockers, and the fact that Dispatcher requirement IDs are now
  tabled while Service and Registry requirement IDs remain future work.

### 20.1.12. v0.2 Round 3 Refinements

- **Evidence object schema:** Defined normative Evidence entry schema with structured `artifact_ref` (object, not string), `method` field (replaces `type`), `verified_by`, and explicit artifact type/integrity fields. Applied consistently across Sections 4, 7, 8, 9, 10, 11, 14, 15, 16, and 17.
- **Registry evidence vocabulary:** Split flat `supported_evidence_types` into `supported_evidence_methods` and `supported_artifact_types` under `provenance_capabilities`.
- **Audit record tables:** Split normative audit requirements into record-level common fields (Table 11.1) and per-message-type fields (Table 11.2).
- **Signing grammar:** Standardized on top-level component signing (`["envelope", "content"]`) with mutable-field exclusion per profile.
- **Service/Registry conformance:** Scoped Full conformance stable-ID tables to the Dispatcher only for v0.2; Service and Registry Full conformance is recorded as an open item (Section 18).
- **Decomposition fallback matrix:** Rewritten to use defined `on_sub_failure`, `on_composition_failure`, and `$ref.fallback` fields only.
- **ESCALATION provenance:** Clarified conditional requirement (required with partial results, implicit OPAQUE for pure routing failures).
- **Schema-validation reroute:** Added `org.ccdp.allow_schema_version_fallback` metadata flag.
- **Open Questions section:** Added Section 18 documenting five deferred design questions.
- **Chapter renumbering:** References → Section 19, Version History → Section 20.
- **Citation label normalization:** Inline citations normalized to match reference keys, including two previously-unnoticed mismatches (FIPA-ACL, PlanBench).
- **Stale identifiers:** Removed remaining `CONFIDENCE_BELOW_THRESHOLD` references and `ccdp/health.response` method assumptions.

## 20.2. Version 0.1.0

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
