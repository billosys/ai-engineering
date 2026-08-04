# 17. Security Considerations

## 17.1. Threat Model

CCDP operates in an environment where:

- Services are heterogeneous and may include LLM endpoints, which are susceptible to prompt injection, output manipulation, and confidential-data extraction.
- The Dispatcher is a high-value target: compromising it grants access to all Services and audit data.
- The Registry is a high-value target: a tampered Registry can redirect traffic to malicious Services.
- External requesters may be malicious, compromised, or negligent.
- Network links between components, while encrypted (TLS), traverse infrastructure that may be hostile.

The threat model assumes:

1. Attackers may attempt to compromise any single component (Dispatcher, Service, Registry, requester).
2. Attackers may attempt to intercept or modify messages in transit (mitigated by TLS).
3. Attackers may attempt to exploit protocol features (escalation chains, decomposition, provenance) for unauthorized access or quality degradation.
4. Insider threats: a Service operator may deliberately misreport provenance grades.

The threat model does NOT assume:

1. Multiple colluding compromised components (this is a single-fault model). While multi-component collusion is out of scope for protocol-level defense, it is a high-risk scenario for large-scale deployments. Deployments handling sensitive data or operating across organizational boundaries SHOULD implement defense-in-depth measures beyond the protocol: independent audit verification, cross-domain provenance spot-checking, and organizational access controls that limit the blast radius of a single compromised identity.
2. Compromise of the TLS infrastructure itself (CA compromise).
3. Quantum computing attacks on current cryptographic primitives.

## 17.2. Known Attack Vectors

### 17.2.1. Content Injection

**Threat:** A malicious requester crafts Content that, when processed by an LLM Service, causes the LLM to produce unintended output (prompt injection) or exfiltrate data from its context.

**CCDP mitigations:**
- The Dispatcher never processes Content, so injection cannot affect routing.
- Input schema validation (Section 8.2.2) constrains the structural shape of Content, reducing the protocol-level attack surface. Schema validation does not mitigate semantic prompt-injection attacks — a structurally valid string can still be a prompt injection. Content-level injection defense is the Service's responsibility (see Section 17.4).
- Services SHOULD implement their own input sanitization and output validation.

**Residual risk:** Content injection is fundamentally a Service-level concern. CCDP's contribution is ensuring that injection cannot affect protocol behavior (routing, audit, provenance) — only the Service's content processing.

### 17.2.2. Provenance Grade Inflation

**Threat:** A compromised or dishonest Service assigns higher Provenance Grades than its output merits (e.g., assigning FORMALLY_VERIFIED to unverified LLM output).

**CCDP mitigations:**
- Evidence entries must substantiate grades above ASSERTED (Section 10.3). A grade of FORMALLY_VERIFIED without a proof-object evidence entry is a protocol violation.
- The audit trail records all provenance claims, enabling retrospective detection of inflation patterns.
- Application-level message signing (Section 15.4.2) binds provenance claims to Service identity, creating accountability.
- The provenance auditing service pattern (Section 10.8) enables spot-checking by re-verifying evidence.

**Residual risk:** A sufficiently sophisticated attacker could forge evidence entries (e.g., generate a fake proof object). Full mitigation requires independent proof checking — the protocol makes evidence available for checking but does not perform the check itself.

### 17.2.3. Registry Poisoning

**Threat:** An attacker gains write access to the Registry and registers a malicious Service with a legitimate Capability Type, or modifies an existing Service's endpoint to redirect traffic.

**CCDP mitigations:**
- Registry access control: only authorized identities may register or update records (Section 15.6.3).
- Registration audit: all Registry modifications are logged with identity and timestamp.
- Namespaced capability types: reverse-domain notation prevents accidental shadowing.
- Schema validation at registration: the Registry validates schemas, preventing structurally malformed entries.

**Residual risk:** If an attacker compromises the Registry's authentication mechanism, they can redirect traffic. This is a single-point-of-failure risk inherent in a centralized registry. Deployments SHOULD implement Registry audit monitoring with alerts on unexpected modifications.

**Registry poisoning.** If an attacker compromises Registry write access (e.g., by obtaining a Registry administrator credential), they can inject malicious Capability Records — redirecting requests to attacker-controlled Services, lowering isolation requirements, or inflating provenance claims. Mitigations: Registry write operations SHOULD require multi-party approval for production registries. Capability Record changes SHOULD be audited with the same rigor as code deployments. Deployments SHOULD implement out-of-band record verification (a second system independently validates that registered service endpoints match expected infrastructure). Registry backup and rollback procedures MUST be documented.

### 17.2.4. Escalation Chain Exploitation

**Threat:** An attacker crafts a request that deliberately triggers escalation through a chain of increasingly expensive services, consuming resources without producing useful output (a cost-amplification attack).

**CCDP mitigations:**
- Cost budgets propagate through escalation: each escalation target receives the remaining cost budget, which decreases as resources are consumed.
- Per-requester rate limiting prevents sustained cost attacks.
- The Dispatcher logs each escalation, making the attack pattern visible.
- Cycle detection prevents infinite escalation loops (Section 13.4).

**Residual risk:** A single expensive escalation (e.g., triggering a human review that costs $50) is possible within the cost budget. Deployments SHOULD set per-request cost ceilings appropriate to their risk tolerance.

### 17.2.5. Decomposition Bomb

**Threat:** A malicious Decomposition Service returns a plan with exponentially many sub-requests (e.g., each sub-request decomposes into 10 more), overwhelming the Dispatcher and consuming unbounded resources.

**CCDP mitigations:**
- Maximum decomposition depth (Section 14.6, RECOMMENDED: 5).
- Cost budget partitioning: the parent's cost budget is divided among sub-requests. Exponential decomposition rapidly exhausts the budget.
- The Dispatcher validates plans before execution (Section 14.4), including resource allocation checks.

**Residual risk:** A plan with many sub-requests at a single level (wide but shallow) is valid and could be expensive. Section 14.6 now defines normative limits: maximum plan width of 50 sub-requests and maximum total nodes of 100 per top-level request. These limits are conformance requirements enforced by the Dispatcher.

### 17.2.6. Replay Attacks

**Threat:** An attacker captures a valid signed message and replays it to trigger duplicate service invocations, potentially consuming resources or duplicating side effects.

**CCDP mitigations:**
- Request ID uniqueness and replay cache (Section 15.5.1).
- Timestamp validation with bounded acceptance window (Section 15.5.2).
- Service idempotency: replayed requests with the same `request_id` return cached responses without re-execution.

**Residual risk:** Within the acceptance window (RECOMMENDED: 5 minutes), a replayed message with the original `request_id` will be handled via idempotency (cached response returned). Outside the window, it will be rejected.

### 17.2.7. Data Exfiltration via Provenance

**Threat:** A malicious Service embeds sensitive data in provenance Evidence entries (e.g., embedding confidential data in an `artifact_ref` field), which then flows through the audit trail and potentially to unauthorized consumers.

**CCDP mitigations:**
- Evidence `artifact_ref` fields are references (URIs), not inline data. Access to the referenced artifacts is governed by the artifact storage system's access controls, not by CCDP.
- The Dispatcher logs provenance but does not dereference artifact references.
- Deployments SHOULD implement data-loss-prevention (DLP) monitoring on evidence entries.

**Residual risk:** Free-text fields (`evidence.description`, `escalation.detail`) can carry arbitrary text. Deployments processing sensitive data SHOULD implement content scanning on these fields. The same exfiltration risk applies to all free-text and URI fields in the protocol: `escalation.detail`, `routing_decision.reason`, `schema_validation` error messages, notification content, and audit record annotations. Deployments processing sensitive data SHOULD implement content scanning or field-length limits on all free-text fields, and SHOULD classify protocol fields by sensitivity level (public, internal, restricted) with access controls matching the classification.

### 17.2.8. Timing Side Channels

**Threat:** An attacker infers information about Service internals from timing data in the audit trail (e.g., a fast Z3 response implies a trivially satisfiable formula, revealing information about the formula's structure).

**CCDP mitigations:** None at the protocol level. This is an inherent property of any system that exposes latency data.

**Residual risk:** Deployments processing highly sensitive data SHOULD restrict access to detailed timing data in audit records (e.g., aggregate to coarser time buckets in external-facing audit exports), apply field-level access controls on `compute_seconds` and latency fields, and limit who can query per-request audit records. Adding noise to audit records is NOT RECOMMENDED as it undermines audit accuracy.

## 17.3. NSA/CISA Recommendations Applied to CCDP

The NSA/CISA MCP Security Assessment [NSA MCP 2026] made specific recommendations. CCDP's response to each:

| NSA Recommendation | CCDP Response | Requirement Level |
|---|---|---|
| Mandatory authentication | Mutual TLS (Section 15.2) | REQUIRED (Core) |
| Lifecycle-managed tokens | Bearer tokens with expiration and scope (Section 15.3) | REQUIRED (Core) |
| Cryptographic message signing | Application-level signing (Section 15.4.2) | REQUIRED (Full), RECOMMENDED (Core) |
| Replay protection metadata | Request ID + timestamp validation (Section 15.5) | REQUIRED (Core) |
| Sandboxing for code execution | Isolation requirements in Registry (Section 15.6) | REQUIRED (Core, declaration); deployment-enforced |
| Structured (non-text) responses | Typed Content with schema validation (Section 7.4) | REQUIRED (Core) |
| Audit logging | Mandatory audit trail (Section 11) | REQUIRED (Core) |

## 17.4. Honest Limitations

Three security concerns that CCDP does not fully address, stated without softening because the credibility of the security design depends on not overclaiming:

**Content-level attacks are the Service's problem.** CCDP protects the protocol layer — routing, audit, provenance. It does not protect the content layer. A prompt injection that causes an LLM to produce wrong output is invisible to CCDP unless the output fails schema validation or provenance verification. The protocol provides the infrastructure for detecting such failures (provenance grades, cross-checking, auditing) but does not perform the detection.

**The trust model is single-fault.** CCDP is designed to detect and contain compromise of a single component. If both a Service and the Registry are compromised, the attacker can redirect traffic and falsify provenance without detection. Multi-component compromise requires organizational security measures beyond the protocol's scope.

**Provenance grades are claims, not proofs.** A provenance grade is a structured assertion by the Service about its own output's epistemic status. While evidence entries make some grades independently verifiable (proof objects can be checked, test results can be re-run), the protocol fundamentally trusts that Services honestly report their grades. Systematic dishonesty requires organizational and auditing countermeasures, not just protocol design.
