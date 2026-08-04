# 7. Message Format

## 7.1. Wire Encoding

Every CCDP message is encoded as a JSON-RPC 2.0 [JSON-RPC] request or response, transported over HTTP POST. The JSON-RPC `method` field identifies the CCDP message type. Method-bearing messages (REQUEST, ESCALATION, NOTIFICATION, HEALTH_REQUEST, DECOMPOSITION_RESULT) carry CCDP data in the JSON-RPC `params` object. Response messages (RESPONSE, HEALTH_RESPONSE) carry CCDP data in the JSON-RPC `result` object.

A CCDP Request encoded as JSON-RPC 2.0:

```json
{
  "jsonrpc": "2.0",
  "method": "ccdp/request",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "params": {
    "envelope": { /* ... Layer 2 and 3 fields ... */ },
    "content": { /* ... Layer 4 payload ... */ }
  }
}
```

A CCDP Response encoded as JSON-RPC 2.0:

```json
{
  "jsonrpc": "2.0",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "result": {
    "envelope": { /* ... Layer 2 and 3 fields ... */ },
    "content": { /* ... Layer 4 payload ... */ }
  }
}
```

The JSON-RPC `id` field MUST match the CCDP `envelope.request_id`. This enables correlation at both the JSON-RPC layer and the CCDP layer.

## 7.2. Message Types

The following CCDP message types are defined:

| Identifier | Type | Direction | JSON-RPC Encoding |
|---|---|---|---|
| `ccdp/request` | REQUEST | Requester → Dispatcher → Service | JSON-RPC request (`method`, `id`, `params`) |
| `ccdp/escalation` | ESCALATION | Service → Dispatcher → Escalation target | JSON-RPC request (`method`, `id`, `params`) |
| `ccdp/health.request` | HEALTH_REQUEST | Dispatcher → Service | JSON-RPC request (`method`, `id`, `params`) |
| `ccdp/decomposition.result` | DECOMPOSITION_RESULT | Decomposition Service → Dispatcher | JSON-RPC request (`method`, `id`, `params`) |
| `ccdp/notification` | NOTIFICATION | Any → Dispatcher → Any | JSON-RPC notification (`method`, `params`, no `id`) |
| *(n/a)* | RESPONSE | Service → Dispatcher → Requester | JSON-RPC response (`id`, `result`) |
| *(n/a)* | HEALTH_RESPONSE | Service → Dispatcher | JSON-RPC response (`id`, `result`) |

REQUEST, ESCALATION, HEALTH_REQUEST, and DECOMPOSITION_RESULT are encoded as JSON-RPC requests — they carry a `method` field, an `id`, and `params`. NOTIFICATION is encoded as a JSON-RPC notification — it carries a `method` and `params` but no `id`, and no response is expected. RESPONSE and HEALTH_RESPONSE are encoded as JSON-RPC responses — they carry an `id` correlating to a prior request and a `result` object containing the CCDP envelope and content. JSON-RPC responses do not carry a `method` field; the CCDP message type is identified by the `envelope.type` field within the `result` object.

## 7.3. Envelope Structure

The Envelope is the structured metadata portion of every CCDP message. The Dispatcher reads the Envelope for routing and enforcement; Content is semantically opaque, though structurally validated and resolved where specified (Section 6).

### 7.3.1. Common Envelope Fields (All Message Types)

The following fields are REQUIRED on every CCDP message envelope:

```json
{
  "envelope": {
    "ccdp_version": "1.0",
    "type": "REQUEST",
    "request_id": "550e8400-e29b-41d4-a716-446655440000",
    "trace_id": "4bf92f3577b34da6a3ce929d0e0e4736",
    "span_id": "00f067aa0ba902b7",
    "timestamp": "2026-08-03T14:30:00.000Z",
    "source_id": "client-app-01",
    "metadata": {}
  }
}
```

**`ccdp_version`** (string, REQUIRED): The CCDP protocol version. MUST be `"1.0"` for this specification. Implementations MUST reject messages with an unrecognized version. The wire protocol version is independent of the document version (Section 2.1). This specification document is version 0.2.0; the wire protocol version remains `"1.0"` because the on-the-wire message format has not changed.

**`type`** (string, REQUIRED): The message type. One of: `"REQUEST"`, `"RESPONSE"`, `"NOTIFICATION"`, `"ESCALATION"`, `"HEALTH_REQUEST"`, `"HEALTH_RESPONSE"`, `"DECOMPOSITION_RESULT"`. For method-bearing messages (REQUEST, ESCALATION, HEALTH_REQUEST, DECOMPOSITION_RESULT, NOTIFICATION), the `envelope.type` value MUST correspond to the JSON-RPC `method` field. For response messages (RESPONSE, HEALTH_RESPONSE), the `envelope.type` is carried inside the `result` object and is the sole identifier of the CCDP message type — JSON-RPC responses have no `method` field.

**`request_id`** (string, REQUIRED): A UUID v4 uniquely identifying this request. Used for idempotency, correlation, and replay protection. A Service that receives a Request with a `request_id` it has already processed MUST return the cached Response without re-executing the request. For NOTIFICATION messages (JSON-RPC notifications), the `request_id` field carries the identifier of the related request (e.g., the request whose progress is being reported) or a unique identifier for the notification itself. Since JSON-RPC notifications do not carry an `id` field, the JSON-RPC `id`-must-match-`request_id` rule does not apply to notifications.

**`trace_id`** (string, REQUIRED): A 32-character lowercase hexadecimal string identifying the entire request chain, compatible with W3C Trace Context `trace-id`. All messages spawned from the same top-level request — including decomposed sub-requests, escalations, and health checks triggered by the request — share the same `trace_id`.

**`span_id`** (string, REQUIRED): A 16-character lowercase hexadecimal string identifying this specific operation within the trace, compatible with W3C Trace Context `parent-id`. Each hop through the Dispatcher generates a new `span_id`. The originator of a top-level Request generates the initial `span_id`. For each subsequent hop — forwarding to a Service, dispatching a sub-request, or routing an escalation — the Dispatcher generates a new `span_id` and sets `parent_span_id` to the previous hop's `span_id`. Services MUST NOT generate new `span_id` values for their Response; the Response carries the same `span_id` as the Request it answers.

**`timestamp`** (string, REQUIRED): ISO 8601 timestamp with UTC timezone (`Z`). The time the message was created by its originator.

**`source_id`** (string, REQUIRED): The identifier of the component that originated this message. For Requests from external clients, this is the client identifier. For Responses, this is the Service identifier. For forwarded messages, this is the originator, not the Dispatcher. When the Dispatcher forwards a message, it does not overwrite `source_id`. The Dispatcher's identity is recorded in the `audit.dispatcher_id` field (Section 7.5), not in `source_id`. This means `source_id` always identifies the originator, and `audit.dispatcher_id` identifies the intermediary. If future extensions require explicit sender/forwarder identification, they SHOULD use metadata keys (e.g., `org.ccdp.forwarder_id`) rather than overloading `source_id`. For signature verification and authorization, implementations MUST use the Authenticated Sender identity established by the transport layer (Section 4, Section 15.2), not the `source_id` payload field. The `source_id` field is an unauthenticated originator claim; the Authenticated Sender is cryptographically verified.

**`metadata`** (object, REQUIRED but MAY be empty): Extensible key-value metadata. Unknown keys MUST be preserved and forwarded by all intermediaries, including the Dispatcher. Keys use reverse-domain notation for namespacing (e.g., `"com.example.custom_field": "value"`). Keys in the `org.ccdp.*` namespace are reserved for protocol-defined extensions.

### 7.3.2. REQUEST Envelope Fields

In addition to Common fields, REQUEST envelopes carry:

```json
{
  "envelope": {
    // ... common fields ...
    "type": "REQUEST",
    "capability_type": "org.ccdp.deduction",
    "destination_id": null,
    "parent_span_id": null,
    "deadline": "2026-08-03T14:31:00.000Z",
    "remaining_budget_ms": 60000,
    "cost_budget": {
      "max_compute_seconds": 120,
      "max_tokens": 50000,
      "max_monetary_cost": "0.50",
      "monetary_unit": "USD"
    },
    "provenance_requirement": {
      "min_policy_grade": "VALIDATED"
    },
    "priority": "NORMAL",
    "idempotency_key": null
  }
}
```

**`capability_type`** (string, REQUIRED): The Capability Type being requested, using reverse-domain notation. The Dispatcher uses this field, together with the Registry, to select the target Service. Well-known types are listed in Section 8.3.

**`destination_id`** (string or null, OPTIONAL): The specific Service to route to. If null, the Dispatcher selects a Service based on `capability_type` and routing rules (Section 9). If specified, the Dispatcher MUST route to that Service if it is healthy and registered for the given `capability_type`; otherwise the Dispatcher MUST return an error. When a requester specifies a non-null `destination_id`, the field is included in the requester-outbound signing scope (Section 15.4.4) and MUST NOT be modified by the Dispatcher.

**`parent_span_id`** (string or null, OPTIONAL): For sub-requests spawned by a Decomposition Plan, the `span_id` of the parent request. Null for top-level requests. Used for constructing the span tree in the audit trail.

**`deadline`** (string, REQUIRED): ISO 8601 timestamp. The absolute time by which the Response MUST arrive at the original requester. The Dispatcher MUST NOT forward a Request to a Service if the remaining time before `deadline` is insufficient for the Service's advertised latency (from its Capability Record).

**`remaining_budget_ms`** (integer, REQUIRED): Remaining time budget in milliseconds. At each hop, the Dispatcher subtracts elapsed time and sets this field to the updated value. Services SHOULD use `remaining_budget_ms` rather than computing from `deadline` to avoid clock-skew issues.

**`cost_budget`** (object, OPTIONAL): Resource constraints on the request. All sub-fields are optional; omitted fields indicate no constraint. `max_compute_seconds` caps wall-clock compute time. `max_tokens` caps token consumption (for LLM services). `max_monetary_cost` caps monetary cost. `monetary_unit` is the ISO 4217 currency code. The Dispatcher MAY use cost_budget for routing decisions (prefer cheaper services). Services MUST NOT exceed the cost_budget; if they would, they MUST return an Escalation with reason `BUDGET_EXCEEDED`. For backward compatibility with v0.1 implementations, Dispatchers SHOULD accept `max_monetary_units` as an alias for `max_monetary_cost` in request envelopes.

**`provenance_requirement`** (object, OPTIONAL on REQUEST/ESCALATION): Specifies the minimum evidence quality acceptable for the response.

- **`min_policy_grade`** (integer 0–7 or grade name, OPTIONAL): The minimum grade in the policy order. The Dispatcher filters candidate services whose maximum achievable grade is below this value. Replaces the former `min_grade` field.
- **`required_methods`** (array of strings, OPTIONAL): Evidence methods that MUST appear in the response's evidence entries. Values match the `method` field of the Evidence Entry schema (Section 4), e.g., `"formal_verification"`, `"human_review"`, `"independent_cross_check"`. When present, a response satisfies the requirement only if its evidence entries include at least one entry of each required method, regardless of the overall grade.
- **`required_evidence_types`** (array of strings, OPTIONAL): Specific evidence artifact types that MUST be present. Values match the `artifact_type` field of the Evidence Entry's `artifact_ref` object (Section 4), e.g., `"proof_certificate"`, `"signed_attestation"`. When present, a response satisfies the requirement only if its evidence entries include artifact references of each specified type.

When only `min_policy_grade` is set, the Dispatcher uses simple `>=` grade comparison (backward-compatible with earlier drafts' `min_grade`). When `required_methods` or `required_evidence_types` are also set, the Dispatcher uses them as additional filters: a candidate service's Capability Record MUST advertise matching `provenance_capabilities.supported_evidence_methods` and `supported_artifact_types` (Section 8.2.2), and the response's actual evidence entries are validated post-receipt against the requirement (Section 9.2, Step 5).

If the Service cannot meet the requirement, it MUST return an Escalation with reason `PROVENANCE_BELOW_REQUIREMENT` and the grade (and evidence types, if applicable) it could achieve. If `provenance_requirement` is omitted, no minimum grade or evidence is required.

**`priority`** (string, OPTIONAL): One of `"LOW"`, `"NORMAL"`, `"HIGH"`, `"CRITICAL"`. Defaults to `"NORMAL"`. Services MAY use priority for internal scheduling. The Dispatcher MAY use priority as a tiebreaker in routing decisions.

**`idempotency_key`** (string or null, OPTIONAL): If provided, a string that groups logically equivalent requests. Two Requests with the same `idempotency_key` SHOULD produce the same result. This is distinct from `request_id`-based idempotency (which is per-message): `idempotency_key` allows a requester to declare that a retried request with a new `request_id` is logically the same request.

### 7.3.3. RESPONSE Envelope Fields

In addition to Common fields, RESPONSE envelopes carry:

```json
{
  "envelope": {
    // ... common fields ...
    "type": "RESPONSE",
    "request_id": "550e8400-e29b-41d4-a716-446655440000",
    "status": "SUCCESS",
    "provenance": {
      "grade": "VALIDATED",
      "evidence": [
        {
          "method": "statistical_testing",
          "description": "All 47 unit tests passed",
          "service_id": "test-runner-01",
          "artifact_ref": {
            "uri": "urn:ccdp:artifact:test-results/run-2026-08-03-001.json",
            "artifact_type": "test_report",
            "integrity": {
              "algorithm": "sha-256",
              "digest": "e3b0c4..."
            }
          }
        }
      ],
      "scope": "Code conforms to specification spec-2026-001",
      "service_id": "code-verifier-01",
      "service_version": "2.3.1",
      "service_mode": 3,
      "computation": {
        "tokens_consumed": 12500,
        "compute_seconds": 4.7,
        "model_id": "claude-opus-4-20260801"
      },
      "composition_trace": null
    }
  }
}
```

**`request_id`** (string, REQUIRED): The `request_id` of the Request this Response answers. MUST match the `request_id` of the original Request.

**`status`** (string, REQUIRED): One of `"SUCCESS"`, `"PARTIAL"`, `"ERROR"`. `SUCCESS` indicates the request was fully completed. `PARTIAL` indicates the Service produced a result but could not fully satisfy the request (the response includes what was achieved). `ERROR` indicates a failure (see Section 13 for error handling).

**`provenance`** (object, REQUIRED): The epistemic metadata for this response. Provenance MUST be present on every RESPONSE. On ESCALATION messages, provenance MUST be present when the message carries partial results (cognitive outputs from the escalating service). ESCALATION messages that represent pure routing failures (no cognitive output was produced) MAY omit provenance; in this case, the provenance grade is implicitly OPAQUE. See the per-message-type matrix (Section 7.3.8) for the normative requirement. Structure defined in Section 10. Sub-fields:

- **`grade`** (string, REQUIRED): The Provenance Grade. One of the defined grades (Section 10.2).
- **`evidence`** (array, REQUIRED but MAY be empty): Evidence entries supporting the grade, using the normative Evidence Entry schema defined in Section 4 (`method`, `description`, `service_id`, `artifact_ref` object, `verified_by`).
- **`scope`** (string, OPTIONAL): What claim the grade applies to. REQUIRED when grade is `FORMALLY_VERIFIED` — it MUST identify the specification against which verification was performed.
- **`service_id`** (string, REQUIRED): The Service that produced this response.
- **`service_version`** (string, REQUIRED): The version of the Service.
- **`service_mode`** (integer, OPTIONAL): The Service Mode (1–4) if known.
- **`computation`** (object, OPTIONAL): Computational resources consumed. Sub-fields: `tokens_consumed` (integer), `compute_seconds` (number), `model_id` (string, the model used if LLM-based), and any additional fields the Service wishes to report.
- **`composition_trace`** (object or null, OPTIONAL): For responses composed from sub-request results, the composition trace documenting how the grade was derived (Section 10.5).

### 7.3.4. ESCALATION Envelope Fields

An Escalation is a structured response indicating that the originating actor — a Service or the Dispatcher — determined that the request cannot be fulfilled under the requested provenance or capability constraints. It shares the RESPONSE envelope structure with additional escalation-specific fields:

```json
{
  "envelope": {
    // ... common fields ...
    "type": "ESCALATION",
    "request_id": "550e8400-e29b-41d4-a716-446655440000",
    "escalation": {
      "reason": "PROVENANCE_BELOW_REQUIREMENT",
      "escalation_origin": "service",
      "detail": "LLM translation uncertainty too high for formal verification",
      "achieved_grade": "HEURISTIC",
      "requested_grade": "VALIDATED",
      "suggested_target": "human-review-queue-01",
      "partial_result_available": true
    },
    "provenance": {
      // ... provenance of the partial result, if any ...
    }
  }
}
```

**`escalation`** (object, REQUIRED):
- **`reason`** (string, REQUIRED): One of the defined escalation reasons (Section 13.3).
- **`escalation_origin`** (string, REQUIRED): Identifies who generated this Escalation. `"service"` when the Service returned an ESCALATION message; `"dispatcher"` when the Dispatcher generated an implicit Escalation from a routing-time or post-receipt provenance policy (Section 9.2). Services MUST set this to `"service"` in their ESCALATION messages. The Dispatcher MUST set this to `"dispatcher"` for implicit Escalations.
- **`detail`** (string, OPTIONAL): Human-readable explanation.
- **`achieved_grade`** (string, OPTIONAL): The Provenance Grade the Service could achieve, if it produced a partial result.
- **`requested_grade`** (string, OPTIONAL): The grade that was requested via `provenance_requirement.min_policy_grade`.
- **`suggested_target`** (string, OPTIONAL): A Service ID or Capability Type the Dispatcher should try next.
- **`partial_result_available`** (boolean, REQUIRED): Whether the Content of this message contains a partial result.

When `partial_result_available` is true, the Content contains whatever the Service was able to produce before escalating. The Dispatcher MUST include this partial result when forwarding the escalation. This is the canonical location for partial results. Partial results MUST be carried in the ESCALATION message's Content, not in metadata. When the Dispatcher forwards the original Request through the escalation chain, it accumulates partial results from prior Services in the Request's metadata under the key `org.ccdp.partial_results` (Section 13.4.1) for downstream Services' reference. The Content of the forwarded Request remains the original requester's Content. For Dispatcher-generated post-receipt mismatch Escalations (`provenance_mismatch_policy`, Section 9.2), the partial result is the original Service Response content that failed to meet the provenance requirement.

### 7.3.5. NOTIFICATION Envelope Fields

Notifications are one-way messages that do not expect a response. They use the Common envelope fields plus:

```json
{
  "envelope": {
    // ... common fields ...
    "type": "NOTIFICATION",
    "capability_type": "org.ccdp.notification",
    "notification_type": "STATUS_UPDATE",
    "destination_id": "client-app-01"
  }
}
```

**`notification_type`** (string, REQUIRED): The kind of notification. Well-known types include `"STATUS_UPDATE"` (progress on a long-running request), `"RESOURCE_ALERT"` (a Service's resource utilization has crossed a threshold), and `"HEALTH_CHANGE"` (a Service's health status has changed). Implementations MAY define additional notification types.

**`destination_id`** (string, REQUIRED): Where to send the notification.

### 7.3.6. HEALTH_REQUEST and HEALTH_RESPONSE Envelope Fields

Health messages are used by the Dispatcher to probe Service health (Section 13.6).

HEALTH_REQUEST:
```json
{
  "envelope": {
    // ... common fields ...
    "type": "HEALTH_REQUEST",
    "destination_id": "z3-prover-01"
  }
}
```

A HEALTH_REQUEST always targets a specific Service — the Dispatcher probes each registered Service's health endpoint individually (Section 13.6.1), it does not broadcast. `destination_id` is therefore REQUIRED on HEALTH_REQUEST.

HEALTH_RESPONSE:
```json
{
  "envelope": {
    // ... common fields ...
    "type": "HEALTH_RESPONSE",
    "health": {
      "status": "HEALTHY",
      "capabilities": {
        "org.ccdp.deduction": {
          "available": true,
          "current_load": 0.35,
          "queue_depth": 2,
          "estimated_latency_ms": 5000
        }
      },
      "capacity": {
        "max_concurrent_requests": 10,
        "current_concurrent_requests": 3
      },
      "detail": null
    }
  }
}
```

**`health.status`** (string, REQUIRED): One of `"HEALTHY"`, `"DEGRADED"`, `"UNHEALTHY"`.

**`health.capabilities`** (object, OPTIONAL): Per-capability status. Each key is a Capability Type; the value reports availability, current load (0.0–1.0), queue depth, and estimated latency for that capability.

**`health.capacity`** (object, OPTIONAL): Overall capacity information.

**`health.detail`** (string, OPTIONAL): Human-readable detail about the health status, particularly when DEGRADED or UNHEALTHY.

### 7.3.7. DECOMPOSITION_RESULT Envelope Fields

Decomposition results are sent by the Decomposition Service and carry the decomposition plan. The full structure is defined in Section 14; the envelope fields are:

```json
{
  "envelope": {
    // ... common fields ...
    "type": "DECOMPOSITION_RESULT",
    "request_id": "550e8400-e29b-41d4-a716-446655440000",
    "provenance": {
      // ... provenance of the decomposition itself ...
    }
  }
}
```

The Content of a DECOMPOSITION_RESULT message is the Decomposition Plan (Section 14.3).

### 7.3.8. Per-Message Required-Field Matrix

| Field | REQUEST | RESPONSE | ESCALATION | NOTIFICATION | HEALTH_REQ | HEALTH_RESP | DECOMP_RESULT |
|---|---|---|---|---|---|---|---|
| `ccdp_version` | R | R | R | R | R | R | R |
| `request_id` | R | R | R | R | R | R | R |
| `type` | R | R | R | R | R | R | R |
| `trace_id` | R | R | R | R | R | R | R |
| `span_id` | R | R | R | R | R | R | R |
| `source_id` | R | R | R | R | R | R | R |
| `capability_type` | R | S | S | O | — | — | R |
| `destination_id` | O | — | O | R | R | — | — |
| `priority` | O | — | O | — | — | — | — |
| `provenance_requirement` | O | — | O | — | — | — | — |
| `provenance` | — | R | R\* | — | — | — | R |
| `cost_budget` | O | — | O | — | — | — | O |
| `deadline` | R | — | O | — | — | — | O |
| `timestamp` | R | R | R | R | R | R | R |

R = REQUIRED, S = RECOMMENDED (SHOULD), O = OPTIONAL, — = not applicable. This matrix is normative. Where prose elsewhere in this section or other sections conflicts with this matrix, the matrix takes precedence.

\* `provenance` is REQUIRED on ESCALATION when the message carries partial results (Section 7.3.4); it MAY be omitted for escalations with no cognitive output (e.g., pure routing failures). `priority` and `provenance_requirement` are request-directional fields that do not apply to a Decomposition Service's plan output — DECOMPOSITION_RESULT carries neither. DECOMPOSITION_RESULT provenance is REQUIRED because the decomposition grade participates in composed provenance (Section 10.5.3).

## 7.4. Content Structure

The Content is the opaque payload of a CCDP message. Its structure is governed by the Capability Record's input schema (for Requests) or output schema (for Responses).

```json
{
  "content": {
    "type": "natural-language",
    "schema_ref": "org.ccdp.deduction/input/v2",
    "body": {
      // ... capability-specific payload ...
    }
  }
}
```

**`content.type`** (string, REQUIRED): The content format. Well-known types:
- `"natural-language"`: Free-text natural language
- `"formal-logic"`: Logical formulas (the specific logic is identified by the schema)
- `"proof-object"`: A machine-checkable proof
- `"validated-plan"`: A plan that has been validated by a sound validator
- `"structured-data"`: Generic structured data
- `"code"`: Source code (language identified by the schema)
- `"multipart"`: Multiple content parts (see below)

Custom content types MAY be defined in Capability Records using reverse-domain notation.

**`content.schema_ref`** (string, OPTIONAL): A reference to the JSON Schema governing this content's `body`, in the format `{capability_type}/{direction}/{version}`. If present, the Dispatcher MAY validate the body against this schema.

**`content.body`** (any, REQUIRED): The actual payload. Structure determined by the schema.

### 7.4.1. Multipart Content

When a response contains multiple distinct outputs (e.g., generated code plus a proof of correctness), the `content.type` is `"multipart"` and the body is an array of typed parts:

```json
{
  "content": {
    "type": "multipart",
    "body": {
      "parts": [
        {
          "type": "code",
          "label": "implementation",
          "body": { "language": "rust", "source": "fn verify(...) { ... }" }
        },
        {
          "type": "proof-object",
          "label": "correctness-proof",
          "body": { "prover": "verus", "proof": "..." }
        }
      ]
    }
  }
}
```

Each part carries its own `type` and `label`. The `label` field is a human-readable identifier that the Decomposition Plan's composition function can reference when assembling results from sub-requests.

## 7.5. Dispatcher Audit Annotation

When the Dispatcher forwards a message, it MUST annotate the envelope with audit metadata. These fields are written by the Dispatcher, not by the originator:

```json
{
  "envelope": {
    // ... existing fields ...
    "audit": {
      "dispatcher_id": "dispatcher-prod-01",
      "received_at": "2026-08-03T14:30:00.123Z",
      "routed_at": "2026-08-03T14:30:00.145Z",
      "routing_decision": {
        "selected_service": "z3-prover-01",
        "reason": "lowest_cost_healthy",
        "candidates_considered": 3,
        "registry_query_ms": 12
      },
      "schema_validation": {
        "input_valid": true,
        "schema_version": "v2"
      }
    }
  }
}
```

The `audit` field is detailed in Section 11.

## 7.6. Size Limits

Implementations MUST support messages of at least 16 MiB. Implementations SHOULD support messages of at least 64 MiB. Messages exceeding the implementation's size limit MUST be rejected with HTTP status 413 (Payload Too Large). If the message is small enough to parse but exceeds the CCDP implementation's processing limit, it MUST be rejected with CCDP error code `-32602` (Invalid params) with a `data.reason` of `"message_too_large"`.

For content payloads that exceed these limits (e.g., large proof objects, extensive code), implementations SHOULD use a reference-based approach: the `content.body` contains a reference (URI) to the full content stored in an external system, rather than the content inline.

## 7.7. Extensibility and Forward Compatibility

The `metadata` field on every envelope provides the extension point for protocol evolution:

1. Unknown keys in `metadata` MUST be preserved by all intermediaries (including the Dispatcher) when forwarding a message. An implementation that does not understand a metadata key MUST NOT strip it, modify it, or use it for routing decisions.

Metadata keys in the `org.ccdp.*` namespace that begin with `org.ccdp.request.*` are request-directional: they are meaningful on REQUEST and ESCALATION messages and SHOULD NOT be blindly copied to RESPONSE messages. Metadata keys beginning with `org.ccdp.response.*` are response-directional. Keys without a directional prefix are bidirectional and MUST be preserved in both directions. This prevents request-only control metadata (e.g., escalation history, routing hints) from leaking into responses.

2. New protocol features SHOULD be introduced as metadata keys in the `org.ccdp.*` namespace before being promoted to top-level envelope fields in a subsequent protocol version.

3. Implementation-specific metadata SHOULD use reverse-domain notation (e.g., `com.example.my_field`) to avoid collisions.

4. An implementation that receives an envelope with an unrecognized `type` field MUST reject the message with error code `-32600` (invalid request) rather than silently dropping it.

This approach follows the TCP/IP tradition of extensible headers: existing implementations continue to work as new fields are added, and the protocol evolves without version bumps for non-breaking changes.

## 7.8. Machine-Readable Schemas

A companion `schemas/` directory will contain normative JSON Schemas for each message type defined in this section. Until these schemas are published, the field definitions and per-message matrix in this section are the normative message specification. The planned schemas cover:

- `envelope.schema.json` — common envelope fields and per-message-type required/optional field sets
- `content.schema.json` — Content wrapper structure (type, body, schema_ref)
- `provenance.schema.json` — provenance grade, evidence entries, composition rules
- `escalation.schema.json` — escalation reason, detail, partial result
- `health.schema.json` — health request and response structures
- `decomposition-plan.schema.json` — plan structure, sub-requests, typed result references, composition spec
- `audit-record.schema.json` — audit record fields and per-message-type requirements

When published, the schemas will be normative, versioned with the document version. Implementations SHOULD validate messages against these schemas during development and testing. Creating the companion schemas is an implementation prerequisite tracked in the README.

## 7.9. HTTP Status Code Mapping

When CCDP messages are transported over HTTP, the following mapping applies:

| Scenario | HTTP Status | CCDP Behavior |
|---|---|---|
| Successful response | 200 OK | JSON-RPC result with CCDP envelope |
| JSON parse error | 400 Bad Request | JSON-RPC error `-32700` |
| Authentication failure | 401 Unauthorized | No JSON-RPC body; Dispatcher logs auth failure |
| Authorization failure (valid token, insufficient scope) | 403 Forbidden | JSON-RPC error `-32009` |
| Message too large to parse | 413 Payload Too Large | No JSON-RPC body |
| Rate limited by Dispatcher | 429 Too Many Requests | JSON-RPC error `-32014` (see Section 13.2) with `Retry-After` in error `data` |
| Rate limited by Service | (Dispatcher absorbs) | Dispatcher treats as DEGRADED, follows retry/reroute (Section 13.5) |
| Internal Dispatcher error | 500 Internal Server Error | JSON-RPC error `-32603` |

HTTP status codes in the 4xx range indicate client-side issues; 5xx indicate Dispatcher-side issues. The JSON-RPC error body, when present, carries the structured CCDP error with trace context for audit correlation.
