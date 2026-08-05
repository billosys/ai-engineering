# 11. Audit Trail

## 11.1. Audit as Core Protocol

Audit records carry an `audit_schema_version` field (string, REQUIRED) independent of the CCDP document version and wire protocol version. The current audit schema version is `"1.0"`. Changes to audit record structure increment this version. Audit consumers MUST check `audit_schema_version` and handle unknown versions gracefully (log a warning and preserve the record without interpretation).

Audit is not an extension, an integration, or a best practice. It is a REQUIRED protocol behavior. Every Message that passes through the Dispatcher MUST generate a structured audit record. This requirement is grounded in a practical lesson: general NSA/CISA AI deployment guidance [NSA-CISA-2024] and CCDP's analysis of MCP's audit limitations (Section 3) both point to the risk of leaving audit to implementation discipline — protocols without mandatory audit leave security and reliability to "implementation discipline," which fails unpredictably across deployments.

In the supervision-tree model, the audit trail is the equivalent of Erlang/OTP's error logger — the mechanism by which failures, routing decisions, and system behavior become visible to the supervisor (ultimately, the human). Without it, the human cannot supervise.

## 11.2. Audit Record Structure

An audit record is generated for every Message that the Dispatcher processes. The record is a structured JSON object with the following fields:

```json
{
  "audit_record": {
    "record_id": "audit-550e8400-e29b-41d4-a716-446655440000",
    "audit_schema_version": "1.0",
    "timestamp": "2026-08-03T14:30:00.145Z",

    "trace_context": {
      "trace_id": "4bf92f3577b34da6a3ce929d0e0e4736",
      "span_id": "00f067aa0ba902b7",
      "parent_span_id": null
    },

    "message_summary": {
      "type": "REQUEST",
      "request_id": "550e8400-e29b-41d4-a716-446655440000",
      "capability_type": "org.ccdp.deduction",
      "source_id": "client-app-01",
      "destination_id": "z3-prover-01",
      "priority": "NORMAL"
    },

    "routing": {
      "decision": "lowest_cost_healthy",
      "candidates_considered": 3,
      "candidates_filtered": {
        "health": 0,
        "deadline": 1,
        "provenance": 0
      },
      "selected_service": "z3-prover-01",
      "registry_source": "live",
      "registry_query_ms": 12
    },

    "validation": {
      "envelope_valid": true,
      "content_schema_valid": true,
      "schema_version": "v2",
      "authentication_verified": true,
      "authorization_verified": true
    },

    "timing": {
      "received_at": "2026-08-03T14:30:00.123Z",
      "validated_at": "2026-08-03T14:30:00.130Z",
      "routed_at": "2026-08-03T14:30:00.145Z",
      "dispatcher_overhead_ms": 22
    },

    "constraints": {
      "deadline": "2026-08-03T14:31:00.000Z",
      "remaining_budget_ms": 59877,
      "cost_budget": { "max_monetary_cost": "0.50", "monetary_unit": "USD" },
      "provenance_requirement": { "min_policy_grade": "VALIDATED" }
    },

    "dispatcher_id": "dispatcher-prod-01",
    "ccdp_version": "1.0"
  }
}
```

### 11.2.1. Response Audit Records

When the Dispatcher receives a Response from a Service and forwards it to the requester, a second audit record is generated:

```json
{
  "audit_record": {
    "record_id": "audit-resp-550e8400-...",
    "audit_schema_version": "1.0",
    "timestamp": "2026-08-03T14:30:04.850Z",

    "trace_context": { /* ... */ },

    "message_summary": {
      "type": "RESPONSE",
      "request_id": "550e8400-e29b-41d4-a716-446655440000",
      "status": "SUCCESS",
      "source_id": "z3-prover-01",
      "destination_id": "client-app-01"
    },

    "provenance_summary": {
      "grade": "FORMALLY_VERIFIED",
      "evidence_count": 1,
      "evidence_methods": ["formal_verification"],
      "scope": "Formula satisfiability in QF_LIA",
      "grade_meets_requirement": true,
      "composition_method": null
    },

    "resource_consumption": {
      "service_compute_seconds": 4.7,
      "service_tokens_consumed": null,
      "total_latency_ms": 4727,
      "cost_budget_remaining": { "monetary_units": "0.499", "monetary_unit": "USD" }
    },

    "validation": {
      "output_schema_valid": true,
      "provenance_present": true,
      "provenance_grade_valid": true
    },

    "timing": {
      "service_invoked_at": "2026-08-03T14:30:00.145Z",
      "response_received_at": "2026-08-03T14:30:04.840Z",
      "response_forwarded_at": "2026-08-03T14:30:04.850Z",
      "service_latency_ms": 4695,
      "dispatcher_overhead_ms": 32
    },

    "dispatcher_id": "dispatcher-prod-01",
    "ccdp_version": "1.0"
  }
}
```

### 11.2.2. Escalation Audit Records

Escalation audit records include the escalation context and the routing chain:

```json
{
  "audit_record": {
    // ... standard fields ...
    "message_summary": {
      "type": "ESCALATION",
      "request_id": "550e8400-...",
      "source_id": "llm-verifier-01",
      "escalation_reason": "PROVENANCE_BELOW_REQUIREMENT",
      "escalation_origin": "service",
      "achieved_grade": "HEURISTIC",
      "requested_grade": "VALIDATED"
    },
    "escalation_routing": {
      "original_service": "llm-verifier-01",
      "escalation_chain_position": 1,
      "next_target": "z3-prover-01",
      "chain_remaining": ["z3-prover-01", "human-review-math-01"],
      "partial_result_forwarded": true
    }
  }
}
```

For Dispatcher-generated implicit Escalations, the audit record includes provenance-policy diagnostics in a `provenance_policy` object:

```json
{
  "audit_record": {
    // ... standard fields ...
    "message_summary": {
      "type": "ESCALATION",
      "request_id": "550e8400-...",
      "source_id": "dispatcher-01",
      "escalation_reason": "PROVENANCE_BELOW_REQUIREMENT",
      "escalation_origin": "dispatcher",
      "achieved_grade": "HEURISTIC",
      "requested_grade": "VALIDATED"
    },
    "provenance_policy": {
      "policy_field": "provenance_mismatch_policy",
      "selected_action": "escalate",
      "trigger": "grade_below_requirement",
      "expected_grade": "VALIDATED",
      "actual_grade": "HEURISTIC",
      "missing_methods": [],
      "missing_artifact_types": [],
      "non_conformant_service_id": "llm-translator-02"
    },
    "escalation_routing": {
      "original_service": "llm-translator-02",
      "escalation_chain_position": 0,
      "next_target": "llm-verifier-01",
      "chain_remaining": ["llm-verifier-01", "human-review-translation-01"],
      "partial_result_forwarded": true,
      "chain_source": "responding_service"
    }
  }
}
```

### 11.2.3. Non-Escalation Provenance-Policy Audit Records

When `provenance_mismatch_policy` evaluates to `"reroute"`, the Dispatcher creates a RESPONSE audit record for the received non-conforming Response. The record includes `provenance_policy.*` diagnostics explaining the policy decision:

```json
{
  "audit_record": {
    "// ... standard fields ...": "",
    "message_summary": {
      "type": "RESPONSE",
      "request_id": "550e8400-...",
      "source_id": "llm-translator-02"
    },
    "provenance_summary": {
      "grade": "HEURISTIC",
      "grade_meets_requirement": false
    },
    "provenance_policy": {
      "policy_field": "provenance_mismatch_policy",
      "selected_action": "reroute",
      "trigger": "grade_below_requirement",
      "expected_grade": "VALIDATED",
      "actual_grade": "HEURISTIC",
      "missing_methods": [],
      "missing_artifact_types": [],
      "non_conformant_service_id": "llm-translator-02"
    },
    "validation": {
      "provenance_present": true,
      "provenance_grade_valid": false
    }
  }
}
```

When `provenance_unavailable_policy` evaluates to `"error"`, the Dispatcher records the policy decision on the REQUEST audit record for the request that could not be routed:

```json
{
  "audit_record": {
    "// ... standard fields ...": "",
    "message_summary": {
      "type": "REQUEST",
      "request_id": "550e8400-...",
      "capability_type": "translation"
    },
    "routing": {
      "decision": "error",
      "candidates_considered": 3,
      "selected_service": null
    },
    "provenance_policy": {
      "policy_field": "provenance_unavailable_policy",
      "selected_action": "error",
      "trigger": "no_candidate_meets_requirement",
      "expected_grade": "VALIDATED",
      "actual_grade": null,
      "missing_methods": ["formal_verification"],
      "missing_artifact_types": [],
      "non_conformant_service_id": null
    }
  }
}
```

## 11.3. Trace Context Propagation

CCDP uses W3C Trace Context [W3C-TC] for distributed tracing. The `trace_id` and `span_id` fields in the CCDP envelope map directly to the W3C `traceparent` header fields:

```
traceparent: 00-{trace_id}-{span_id}-{trace_flags}
```

The Dispatcher MUST:

1. Propagate `trace_id` unchanged through all Messages in the same request chain.
2. Generate a new `span_id` for each hop through the Dispatcher.
3. Set `parent_span_id` on forwarded messages to the incoming message's `span_id`.
4. Include the W3C `traceparent` header on HTTP requests to Services.
5. Preserve the `tracestate` header if present, appending a CCDP-specific entry: `ccdp=dispatcher_id`. The Dispatcher appends `ccdp=<dispatcher_id>` to the `tracestate` header. If the `tracestate` header would exceed 512 bytes after appending, the Dispatcher MUST truncate the oldest entries (leftmost) to make room, per W3C Trace Context [W3C-TC] §3.3.2.1. W3C Trace Context §3.3.2.1 specifies that the rightmost entries are the most recently added. Truncating leftmost entries removes the oldest vendor data, which is the least likely to be needed by downstream components. However, some vendors may depend on ordering semantics. If the Dispatcher cannot safely truncate, it SHOULD omit its own `ccdp=<dispatcher_id>` entry rather than truncating other vendors' entries, and log the omission. The Dispatcher MUST sanitize `tracestate` values: strip control characters and validate against the W3C tracestate grammar before forwarding.

This ensures that CCDP traces are compatible with standard distributed tracing infrastructure (OpenTelemetry, Jaeger, Zipkin). Services that use tracing internally can link their internal spans to the CCDP trace.

## 11.4. Mandatory Audit Fields

**Table 11.1: Audit Record Common Fields (required on every audit record)**

| Field | Type | Description |
|---|---|---|
| `record_id` | string (UUID v4) | Unique identifier for this audit record |
| `audit_schema_version` | string | Audit schema version (independent of document and wire versions) |
| `timestamp` | string (ISO 8601) | When the Dispatcher created this record |
| `dispatcher_id` | string | Identity of the Dispatcher that created this record |
| `ccdp_version` | string | CCDP wire protocol version from the processed message envelope |
| `trace_context.trace_id` | string | W3C Trace Context trace identifier |
| `trace_context.span_id` | string | W3C Trace Context span identifier for this hop |
| `message_summary.type` | string | CCDP message type that triggered this record |

The per-message-type matrix (Table 11.2 below) specifies additional fields required for each message type. A conforming audit record includes all common fields from Table 11.1 plus the message-type-specific fields from Table 11.2.

Audit data is also organized into the following informal categories, covering the message-type-specific fields (not the record-level common fields above). Implementations MUST NOT make any field marked REQUIRED in the per-message-type matrix below optional or configurable for the message types where it applies:

| Category | Fields | Typical applicability |
|----------|--------|---------------|
| Identity | `record_id`, `trace_id`, `span_id`, `parent_span_id`, `request_id` | Most message types |
| Message | `type`, `capability_type`, `source_id`, `destination_id` | Varies by type — see matrix |
| Routing | `decision`, `selected_service`, `candidates_considered`, `registry_source` | Requests and escalations |
| Validation | `envelope_valid`, `content_schema_valid`, `authentication_verified` | Requests |
| Timing | `received_at`, `routed_at`, `dispatcher_overhead_ms` | Most message types |
| Constraints | `deadline`, `remaining_budget_ms` | Requests |
| Provenance | `grade`, `grade_meets_requirement` | Responses and escalations |
| Resources | `service_latency_ms`, `cost_budget_remaining` | Responses |
| Errors | `error_code`, `error_detail`, `retry_count` | Errors and retries |
| Dispatcher | `dispatcher_id`, `ccdp_version` | Most message types |

Not all audit fields are meaningful for every message type. The per-message-type audit requirements matrix below is the normative source for which message-type-specific audit fields are REQUIRED (R), RECOMMENDED (S), or not applicable (—) for each message type; the category table above is informative summary only. This matrix covers message-type-specific fields only — the common fields in Table 11.1 are required on every message type regardless of this matrix.

**Table 11.2: Per-Message-Type Audit Requirements**

| Field | REQUEST | RESPONSE | ESCALATION | NOTIFICATION | HEALTH_REQ | HEALTH_RESP | DECOMP_RESULT |
|---|---|---|---|---|---|---|---|
| `trace_context.trace_id` | R | R | R | R | R | R | R |
| `trace_context.span_id` | R | R | R | R | R | R | R |
| `message_summary.request_id` | R | R | R | S | R | R | R |
| `message_summary.capability_type` | R | S | S | S | — | — | R |
| `message_summary.destination_id` | S | — | S | S | R | — | — |
| `message_summary.source_id` | R | R | R | R | R | R | R |
| `routing.decision` | R | — | R | — | — | — | R |
| `provenance_summary` | — | R | R | — | — | — | R |
| `message_summary.escalation_origin` | — | — | R | — | — | — | — |
| `message_summary.escalation_reason` | — | — | R | — | — | — | — |
| `message_summary.achieved_grade` | — | — | S | — | — | — | — |
| `message_summary.requested_grade` | — | — | S | — | — | — | — |
| `provenance_policy.policy_field` | — | — | S | — | — | — | — |
| `provenance_policy.selected_action` | — | — | S | — | — | — | — |
| `provenance_policy.trigger` | — | — | S | — | — | — | — |
| `provenance_policy.expected_grade` | — | — | S | — | — | — | — |
| `provenance_policy.actual_grade` | — | — | S | — | — | — | — |
| `provenance_policy.missing_methods` | — | — | S | — | — | — | — |
| `provenance_policy.missing_artifact_types` | — | — | S | — | — | — | — |
| `provenance_policy.non_conformant_service_id` | — | — | S | — | — | — | — |
| `escalation_routing.chain_source` | — | — | S | — | — | — | — |
| `validation.content_schema_valid` | R | S | — | — | — | — | R |
| `health_summary.status` | — | — | — | — | — | R | — |

Field names above are canonical JSON paths into the audit record structure shown in Section 11.2's examples (e.g., `trace_context.trace_id`, not a bare `trace_id`), so that a conformance test can locate each field unambiguously.

The `provenance_policy.*` and `escalation_routing.chain_source` fields are marked RECOMMENDED (S) in Table 11.2 under the ESCALATION column because they are conditional — they apply only when a provenance policy is evaluated, not to all ESCALATION records. Section 9.2 normatively requires `provenance_policy.*` diagnostics for every `provenance_mismatch_policy` and `provenance_unavailable_policy` decision, regardless of the selected action. A conforming Dispatcher MUST record the policy field, selected action, trigger, grade comparison, and — when applicable — missing methods, missing artifact types, and non-conformant Service identity. The audit-record type on which these fields appear depends on the selected action (Table 11.3 below; worked examples in Section 11.2.3). `escalation_routing.chain_source` applies only to escalation outcomes and indicates whether the chain was sourced from the responding Service's capability record (`"responding_service"`) or routed directly to human review (`"human_review"`).

**Table 11.3: Provenance-Policy Conditional Audit Placement**

| Outcome | Triggering Policy | Audit Record Type | `provenance_policy.*` | `escalation_routing.chain_source` |
|---|---|---|---|---|
| `"escalate"` | Either | ESCALATION (Section 11.2.2) | REQUIRED | REQUIRED |
| `"reroute"` | `provenance_mismatch_policy` | RESPONSE for the non-conforming Response (Section 11.2.3) | REQUIRED | — |
| `"error"` | `provenance_unavailable_policy` | REQUEST for the failed request (Section 11.2.3) | REQUIRED | — |

Table 11.2 marks `provenance_policy.*` as RECOMMENDED (S) under ESCALATION because that is the unconditional per-message-type default. Table 11.3 is the normative source for conditional placement on RESPONSE and REQUEST records when a non-escalation action is selected.

## 11.5. Audit Storage and Retention

This specification does not mandate a specific audit storage mechanism. Implementations MAY use structured log files, a database, an event stream (e.g., Kafka), or any other storage that satisfies these requirements:

1. **Immutability.** Audit records, once written, MUST NOT be modified or deleted during the retention period. Append-only storage is RECOMMENDED.
2. **Queryability.** The audit store MUST support queries by `trace_id` (retrieve all records for a request chain), `request_id` (retrieve records for a specific request), `service_id` (retrieve records for a specific service), and time range.
3. **Retention.** Audit records MUST be retained for a minimum period configured per deployment. The RECOMMENDED minimum retention period is 90 days for production deployments.
4. **Integrity.** Audit records MUST be written to a tamper-evident store for CCDP Full conformance. CCDP Core conformance REQUIRES structured audit records but permits deployment-configured integrity mechanisms. For Full conformance, tamper evidence means either cryptographic chaining (each record includes a hash of the previous record), append-only storage with integrity verification, or a write-once medium. The specific mechanism is deployment-defined.

## 11.6. Audit Store Failure Behavior

If the audit store is unavailable, the Dispatcher MUST follow its deployment-configured `audit_failure_policy`:

- **`fail_closed`** (RECOMMENDED for production): The Dispatcher MUST reject incoming requests with error `-32603` (internal error) and `data.reason` of `"audit_unavailable"` until the audit store recovers. No messages are processed without audit.
- **`buffer`**: The Dispatcher buffers audit records locally (in memory or on local disk) and continues processing messages. Buffered records MUST be flushed to the audit store when it recovers. The buffer MUST have a bounded size; when the buffer is full, the Dispatcher falls back to `fail_closed`.
- **`degrade`**: The Dispatcher continues processing messages without audit. The `degrade` policy is non-conformant — a Dispatcher operating in `degrade` mode does not meet CCDP Core conformance requirements. It exists solely as a development/debugging mode. Implementations MUST NOT enable `degrade` in any deployment that claims CCDP conformance. If used, the Dispatcher MUST set a metadata flag `org.ccdp.audit_gap: true` on all messages processed during the gap, and MUST log the gap duration and message count when the audit store recovers.

The audit failure policy MUST be declared in the Dispatcher's deployment configuration and MUST be discoverable via the Dispatcher's own health endpoint.

## 11.7. Audit as Supervision Input

The audit trail is not just a compliance mechanism — it is the Human Supervisor's primary input for understanding system behavior. Deployments SHOULD provide tooling that enables:

- **Request tracing:** Given a `trace_id`, reconstruct the full journey of a request — every routing decision, every service invocation, every escalation, every provenance grade.
- **Provenance verification:** Given a Response, verify its provenance chain by re-checking evidence entries against the audit trail.
- **Performance analysis:** Identify latency bottlenecks, cost outliers, and routing inefficiencies from audit timing data.
- **Health monitoring:** Detect Service degradation patterns from audit error and escalation data.
- **Grade distribution analysis:** Monitor the distribution of provenance grades over time to detect grade inflation, systematic under-verification, or changes in service quality.

This tooling is outside the scope of this specification but is essential for the supervision-tree architecture to function. The audit trail provides the data; the tooling makes it actionable.
