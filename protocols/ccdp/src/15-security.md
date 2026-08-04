# 15. Security

## 15.1. Security Posture

Security in CCDP is a protocol guarantee, not an implementation recommendation. This design choice is a direct response to the NSA/CISA assessment of MCP, which found that MCP's security posture is "highly dependent on implementation discipline rather than protocol guarantees" — a dependency that fails unpredictably across deployments.

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
- Tokens SHOULD be issued by an OAuth 2.1 authorization server with PKCE [RFC 9126].
- Tokens MUST be transmitted in the HTTP `Authorization` header.

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
- Requests with `cost_budget.max_monetary_units` above the token's `max_cost_usd`

Wildcard scopes (e.g., `org.ccdp.language.*`) match all subtypes.

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
      "key_id": "z3-prover-01-signing-key-2026",
      "signature": "base64-encoded-signature",
      "signed_fields": ["envelope.request_id", "envelope.provenance", "content"],
      "timestamp": "2026-08-03T14:30:04.840Z"
    }
  }
}
```

The signature covers the specified fields. The Dispatcher MUST preserve the signature in the metadata when forwarding (per the metadata preservation rule, Section 7.7). The requester can verify the signature using the Service's public key (obtained from the Registry or a key server).

Message signing is OPTIONAL for conforming implementations but RECOMMENDED for Services that produce FORMALLY_VERIFIED output — the signature binds the provenance claim to the Service's identity.

### 15.4.3. Provenance Integrity

Provenance grades and evidence entries are security-relevant — a tampered provenance grade can cause a consumer to over-trust a result. The Dispatcher MUST NOT modify provenance fields. If application-level signing is used, provenance fields SHOULD be included in the signed fields.

## 15.5. Replay Protection

### 15.5.1. Request ID Uniqueness

Every Request carries a unique `request_id` (UUID v4). The Dispatcher MUST maintain a replay cache of recently processed `request_id` values (RECOMMENDED: cache size covers at least 24 hours of traffic).

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

### 15.6.2. Content Isolation

The Dispatcher MUST NOT execute, evaluate, or interpret Content from any Message. Content is treated as opaque data. This prevents content injection attacks where a malicious payload in the Content could influence Dispatcher behavior.

Specifically:
- The Dispatcher MUST NOT pass Content through an eval, template engine, or interpreter.
- Schema validation of Content MUST use a JSON Schema validator that does not execute code (no `$code` or `$eval` extensions).
- Log entries that include Content excerpts MUST sanitize or truncate them to prevent log injection.

### 15.6.3. Tool Naming and Registry Security

The MCP fault taxonomy study identified tool naming collisions as an attack vector — malicious entries in public registries with names that shadow legitimate tools. CCDP mitigates this through:

- **Namespaced capability types:** Reverse-domain notation prevents accidental collisions.
- **Registry access control:** Only authorized identities may register or update Capability Records.
- **Registration audit:** All Registry modifications are logged with the modifier's identity and timestamp.
- **Schema validation at registration:** The Registry MUST validate that input and output schemas are well-formed JSON Schema before accepting a registration.

## 15.7. Credential Handling

Services that require credentials (API keys, database passwords, etc.) MUST NOT receive them through the CCDP protocol. Credentials are provisioned through out-of-band mechanisms (environment variables, secret managers, key vaults). The CCDP protocol carries authentication tokens for *protocol-level* identity, not application-level credentials.

The Dispatcher MUST NOT log, cache, or inspect bearer tokens beyond what is necessary for authentication. Token values MUST be redacted in audit logs.

## 15.8. Rate Limiting as Security

Rate limiting (Section 12.5) serves a security function in addition to its resource management role:

- **Denial of service prevention:** Per-requester rate limits prevent a single requester from exhausting Service capacity.
- **Cost abuse prevention:** Per-token cost budgets (Section 15.3.2) prevent a compromised token from incurring unlimited cost.
- **Goodhart-style gaming prevention:** Rate limits on verification services prevent gaming where an attacker submits many weak proofs hoping one trivially passes.

Rate limiting parameters are deployment-configured, not protocol-specified.
