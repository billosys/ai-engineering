# 15. Security

## 15.1. Security Posture

CCDP defines security requirements at the protocol level — authentication, authorization, token scoping, message signing, and replay protection. Some requirements (mutual TLS, bearer-token validation) are enforced by the protocol infrastructure. Others (isolation, workload attestation) are protocol requirements that depend on deployment infrastructure for enforcement. The protocol specifies what must be true; the deployment ensures it is true.

This design choice is a direct response to the MCP release-candidate retrospective [MCP-2026-07-28], which found that a security posture "highly dependent on implementation discipline rather than protocol guarantees" fails unpredictably across deployments.

Every CCDP deployment MUST implement the security requirements in this section. There are no "development mode" exceptions in the specification — while individual deployments MAY relax requirements in non-production environments, the protocol defines a security floor that conforming implementations MUST meet in production.

## 15.2. Authentication

### 15.2.1. Dispatcher-to-Service Authentication

All communication between the Dispatcher and Services MUST be mutually authenticated. The REQUIRED mechanism is mutual TLS (mTLS):

- The Dispatcher and each Service MUST hold X.509 certificates.
- The Dispatcher MUST verify the Service's certificate on every connection.
- The Service MUST verify the Dispatcher's certificate on every connection.
- Certificates MUST be issued by a trusted Certificate Authority (CA) configured per deployment. Self-signed certificates MUST NOT be used in production.

mTLS provides authentication at the transport layer — the Dispatcher knows it is talking to the real Service, and the Service knows it is talking to the real Dispatcher. This is the baseline that prevents Service impersonation and man-in-the-middle attacks.

### 15.2.2. Requester Authentication

External requesters (humans, applications, other systems) MUST be authenticated before the Dispatcher processes their requests. The REQUIRED mechanism is bearer tokens with the following properties:

- Tokens MUST be scoped to specific Capability Types. A token authorized for `org.ccdp.language.generation` MUST NOT be accepted for `org.ccdp.deduction`.
- Tokens MUST have a bounded lifetime (expiration timestamp). The Dispatcher MUST reject expired tokens.
- Tokens SHOULD be issued by an OAuth 2.0 authorization server using Pushed Authorization Requests [RFC 9126] with PKCE [RFC 7636]. Implementations requiring issuer validation SHOULD follow [RFC 9207]. PAR and PKCE apply to the authorization-code issuance flow — how tokens are obtained from the authorization server. They are best practices for token issuance, not requirements for token validation. The Dispatcher, acting as a resource server, validates tokens by checking signature/introspection, expiration, audience, and scope (Section 15.3). The issuance-flow recommendations apply to authorization-server deployments, not to CCDP Dispatchers.
- Tokens MUST be transmitted in the HTTP `Authorization` header.

**Token format.** This specification does not mandate a specific token format. Implementations MAY use JWT [RFC 7519] with the claims listed above, opaque tokens validated by introspection [RFC 7662], or any other bearer token format that supports the required properties (scope, expiration, audience binding). If JWT is used, the Dispatcher MUST validate the signature, expiration, audience (`aud` claim matching the Dispatcher's identifier), and scope claims. If opaque tokens are used, the Dispatcher MUST validate them via the authorization server's introspection endpoint.

**Token lifecycle.** Token clock-skew tolerance MUST be configurable (RECOMMENDED: 60 seconds). Implementations SHOULD support token revocation via revocation lists or introspection-based validity checks for long-lived sessions. Confirmation binding (proof-of-possession via `cnf` claim [RFC 7800]) is OPTIONAL but RECOMMENDED for high-security deployments where bearer-token theft is a concern.

### 15.2.3. Service-to-Service Authentication

When a Service makes a sub-request through the Dispatcher (e.g., a Mode 3 Service invoking a Mode 2 Service), the sub-request is authenticated by the Dispatcher using the originating Service's mTLS identity. The Dispatcher MUST verify that the originating Service is authorized to invoke the target Capability Type.

## 15.3. Authorization

### 15.3.1. Capability-Based Authorization

The Dispatcher MUST enforce capability-based authorization: a requester (human or Service) is authorized for a specific set of Capability Types, and requests for unauthorized types are rejected with error `-32009`.

Authorization mappings are maintained in the Registry or a dedicated authorization service (implementation-defined). The mapping specifies, for each authenticated identity:

- Which Capability Types they may invoke
- Which priority levels they may use
- What maximum cost budget they may specify
- Whether they may specify `destination_id` (direct routing)

### 15.3.2. Token Scoping

Bearer tokens MUST carry scope claims that the Dispatcher validates:

```json
{
  "sub": "client-app-01",
  "scope": ["org.ccdp.deduction", "org.ccdp.language.*"],
  "max_priority": "HIGH",
  "max_cost_usd": 10.00,
  "exp": 1722700800
}
```

The Dispatcher MUST reject:
- Requests for capability types not in the token's `scope`
- Requests with `priority` above the token's `max_priority`
- Requests with `cost_budget.max_monetary_cost` above the token's `max_cost_usd`

Wildcard scopes (e.g., `org.ccdp.language.*`) match all subtypes. Wildcard scope matching uses the following grammar: a scope pattern ending in `.*` matches any scope string that begins with the prefix (everything before `.*`) followed by a dot and one or more additional segments. `org.ccdp.language.*` matches `org.ccdp.language.generation` but not `org.ccdp.language` or `org.ccdp.*`. Exact-match scopes take precedence over wildcard matches. A token with scope `["org.ccdp.language.generation"]` is authorized for that specific capability; a token with scope `["org.ccdp.language.*"]` is authorized for any capability under that prefix.

## 15.4. Message Integrity

### 15.4.1. Transport-Level Integrity

TLS 1.3 provides message integrity at the transport level. This protects against tampering in transit between the Dispatcher and Services.

### 15.4.2. Application-Level Message Signing

For environments requiring end-to-end integrity (the requester must be able to verify that the Service's response was not modified by the Dispatcher or any intermediary), CCDP supports application-level message signing:

A Service MAY sign its Response envelope and content using a digital signature:

```json
{
  "metadata": {
    "org.ccdp.signature": {
      "algorithm": "Ed25519",
      "key_id": "svc-formal-01-signing-2026",
      "profile": "service-response",
      "signed_fields": ["envelope", "content"],
      "value": "base64-encoded-signature...",
      "timestamp": "2026-08-03T14:30:04.840Z"
    }
  }
}
```

The signature covers the specified components. The Dispatcher MUST preserve the signature in the metadata when forwarding (per the metadata preservation rule, Section 7.7). The requester can verify the signature using the Service's public key (obtained from the Registry or a key server).

**Signed components.** The `signed_fields` array identifies top-level components of the CCDP message to include in the signature. Valid values are `"envelope"` and `"content"`. The signature input is the JCS [RFC 8785] canonical form of a JSON object containing exactly those components:

```json
JCS({"envelope": <envelope-value>, "content": <content-value>})
```

**Mutable-field exclusion.** Before signing, the signer removes Dispatcher-mutable fields from the `envelope` value. The mutable fields are defined per signing profile (Section 15.4.4). After exclusion, the remaining envelope fields plus the content form the signature input. The Dispatcher MUST NOT modify any field remaining in a signed component after signing; a signature covering a field the Dispatcher subsequently modifies is invalid by construction — the verifier MUST reject it.

Message signing is OPTIONAL for CCDP Core conformance. For CCDP Full conformance, message signing is REQUIRED for Services that produce responses at grade FORMALLY_VERIFIED or HUMAN_ATTESTED, and RECOMMENDED for all other Services. For deployments spanning untrusted administrative domains (different organizations, different cloud regions), message signing is REQUIRED regardless of conformance level.

For responses at grade FORMALLY_VERIFIED or HUMAN_ATTESTED, the Service MUST sign the response using the service-response profile (Section 15.4.4), and the `signed_fields` array MUST include both `"envelope"` and `"content"` — since `provenance` is an envelope field (Section 7.3.3), signing `"envelope"` covers the response's evidence chain along with the cognitive output in `"content"`. For other grades, signing with both components is RECOMMENDED.

### 15.4.3. Provenance Integrity

Provenance grades and evidence entries are security-relevant — a tampered provenance grade can cause a consumer to over-trust a result. The Dispatcher MUST NOT modify received provenance fields. If application-level signing is used, provenance fields SHOULD be included in the signed fields.

### 15.4.4. Signing Profiles

CCDP defines two signing profiles with different mutable-field sets:

**Requester-outbound profile.** The requester signs before the Dispatcher processes the message. Mutable fields excluded from `envelope` before signing: `audit` (added by the Dispatcher on receipt; absent on the requester's outbound envelope), `remaining_budget_ms` (decremented by the Dispatcher at each subsequent hop, per Section 12.4), `destination_id` (excluded only when null or absent at signing time; a non-null requester-specified `destination_id` is part of the requester's routing intent and MUST remain in the signed envelope — see Section 7.3.2 and Section 9.2 Step 1), and metadata keys in `org.ccdp.dispatcher.*`. All other envelope fields are immutable after signing. The Dispatcher verifies the Requester's signature — computed over the envelope as the requester sent it — before processing.

**Service-response profile.** The service signs its response. Mutable fields excluded from `envelope` before signing: `audit` (added or updated by the Dispatcher when forwarding the response, per Section 7.5) and metadata keys in `org.ccdp.dispatcher.*`. The `remaining_budget_ms` field is not present on response messages. All other envelope fields, and the entire `content` object, are immutable after signing. The `signed_fields` array MUST include both `"envelope"` and `"content"`. The Dispatcher verifies the Service's signature before forwarding to the Requester.

The `signature` object carries a `profile` field (`"requester-outbound"` or `"service-response"`) identifying which signing profile was used. Verifiers MUST check the profile and reject signatures that include Dispatcher-mutable fields for the specified profile.

## 15.5. Replay Protection

### 15.5.1. Request ID Uniqueness

Every Request carries a unique `request_id` (UUID v4). The Dispatcher MUST maintain a replay cache of recently processed `request_id` values (RECOMMENDED: cache size covers at least 24 hours of traffic). In high-availability deployments with multiple Dispatcher instances, the replay cache MUST be shared across all instances. Implementation options include a shared cache service (Redis, Memcached), a distributed data structure, or a consensus-based replicated store. If the replay cache is partitioned (e.g., by `request_id` hash), the partition scheme MUST ensure that all instances handling the same `request_id` query the same partition. The replay cache is a source of shared state that complicates Dispatcher replication — deployments MUST plan for cache consistency, eviction, and failure.

If the Dispatcher receives a Request with a `request_id` it has already processed:
- If the payload is identical: return the cached response (idempotency).
- If the payload is different: reject with error `-32011` (replay detected).

### 15.5.2. Timestamp Validation

The Dispatcher MUST validate the `envelope.timestamp` field:
- Reject messages with timestamps more than a configurable window in the past (RECOMMENDED: 5 minutes).
- Reject messages with timestamps in the future (beyond a clock-skew tolerance, RECOMMENDED: 30 seconds).

These checks prevent replay attacks where an attacker captures and resubmits a valid message.

## 15.6. Isolation

### 15.6.1. Service Isolation Requirements

Each Capability Record declares the Service's isolation requirements (Section 8.2.2). The Dispatcher or deployment infrastructure MUST enforce these:

- **`executes_arbitrary_code: true`**: The Service MUST run in a sandboxed environment (container, VM, or equivalent) with restricted filesystem and network access.
- **`requires_sandbox: true`**: Same as above, explicitly requested by the Service.
- **`network_access: false`**: The Service MUST NOT have network access beyond the Dispatcher endpoint.
- **`filesystem_access: false`**: The Service MUST NOT have filesystem access beyond its designated working directory.

Isolation requirements declared in Registry metadata are *policy inputs*, not protocol-enforceable guarantees. The Dispatcher trusts that the deployment infrastructure enforces isolation as declared. For deployments requiring stronger assurance, implementations SHOULD support workload attestation — the Service provides a signed attestation (e.g., via a Trusted Platform Module or confidential-computing attestation service) that its runtime environment matches the declared isolation requirements. Attestation verification is an optional Full-conformance feature.

### 15.6.2. Content Isolation

The Dispatcher MUST NOT execute, evaluate, or interpret Content from any Message. Content is treated as opaque data. This prevents content injection attacks where a malicious payload in the Content could influence Dispatcher behavior.

Specifically:
- The Dispatcher MUST NOT pass Content through an eval, template engine, or interpreter.
- Schema validation of Content MUST use a JSON Schema validator that does not execute code (no `$code` or `$eval` extensions).
- Log entries that include Content excerpts MUST sanitize or truncate them to prevent log injection.

The typed result-reference mechanism in Section 14.3.3 is not a template engine — it performs JSON Pointer extraction and structural substitution without interpreting content values. This satisfies the content-isolation requirement.

### 15.6.3. Tool Naming and Registry Security

The MCP fault taxonomy study identified tool naming collisions as an attack vector — malicious entries in public registries with names that shadow legitimate tools. CCDP mitigates this through:

- **Namespaced capability types:** Reverse-domain notation prevents accidental collisions.
- **Registry access control:** Only authorized identities may register or update Capability Records.
- **Registration audit:** All Registry modifications are logged with the modifier's identity and timestamp.
- **Schema validation at registration:** The Registry MUST validate that input and output schemas are well-formed JSON Schema before accepting a registration.

## 15.7. Credential Handling

Services that require credentials (API keys, database passwords, etc.) MUST NOT receive them through the CCDP protocol. Credentials are provisioned through out-of-band mechanisms (environment variables, secret managers, key vaults). The CCDP protocol carries authentication tokens for *protocol-level* identity, not application-level credentials.

The Dispatcher MUST NOT log, cache, or inspect bearer tokens beyond what is necessary for authentication. Token values MUST be redacted in audit logs.

Implementations MAY cache token validation decisions (the result of signature verification or introspection) for the token's remaining lifetime, subject to a deployment-configured maximum cache TTL (RECOMMENDED: 300 seconds). Caching the validation decision is distinct from caching the token value itself. The Dispatcher SHOULD NOT retain raw token strings beyond the request-processing lifetime.

## 15.8. Rate Limiting as Security

Rate limiting (Section 12.5) serves a security function in addition to its resource management role:

- **Denial of service prevention:** Per-requester rate limits prevent a single requester from exhausting Service capacity.
- **Cost abuse prevention:** Per-token cost budgets (Section 15.3.2) prevent a compromised token from incurring unlimited cost.
- **Goodhart-style gaming prevention:** Rate limits on verification services prevent gaming where an attacker submits many weak proofs hoping one trivially passes.

Rate limiting parameters are deployment-configured, not protocol-specified.
