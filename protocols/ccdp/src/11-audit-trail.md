# 11. Audit Trail

## 11.1. Audit as Core Protocol

Audit is not an extension, an integration, or a best practice. It is a REQUIRED protocol behavior. Every Message that passes through the Dispatcher MUST generate a structured audit record. This requirement is grounded in a practical lesson: the NSA/CISA assessment of MCP found that protocols without mandatory audit leave security and reliability to "implementation discipline" — which fails unpredictably across deployments.

In the supervision-tree model, the audit trail is the equivalent of Erlang/OTP's error logger — the mechanism by which failures, routing decisions, and system behavior become visible to the supervisor (ultimately, the human). Without it, the human cannot supervise.

## 11.2. Audit Record Structure

An audit record is generated for every Message that the Dispatcher processes. The record is a structured JSON object with the following fields:

```json
{
  "audit_record": {
    "record_id": "audit-550e8400-e29b-41d4-a716-446655440000",
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
      "cost_budget": { "max_monetary_units": 0.50, "monetary_unit": "USD" },
      "provenance_requirement": { "min_grade": "VALIDATED" }
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
      "evidence_types": ["proof-object"],
      "scope": "Formula satisfiability in QF_LIA",
      "grade_meets_requirement": true,
      "composition_method": null
    },

    "resource_consumption": {
      "service_compute_seconds": 4.7,
      "service_tokens_consumed": null,
      "total_latency_ms": 4727,
      "cost_budget_remaining": { "monetary_units": 0.499, "monetary_unit": "USD" }
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
      "escalation_reason": "CONFIDENCE_BELOW_THRESHOLD",
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
5. Preserve the `tracestate` header if present, appending a CCDP-specific entry: `ccdp=dispatcher_id`.

This ensures that CCDP traces are compatible with standard distributed tracing infrastructure (OpenTelemetry, Jaeger, Zipkin). Services that use tracing internally can link their internal spans to the CCDP trace.

## 11.4. Mandatory Audit Fields

The following audit data MUST be recorded for every Message processed by the Dispatcher. Implementations MUST NOT make any of these fields optional or configurable:

| Category | Fields | When recorded |
|----------|--------|---------------|
| Identity | `record_id`, `trace_id`, `span_id`, `parent_span_id`, `request_id` | Every message |
| Message | `type`, `capability_type`, `source_id`, `destination_id` | Every message |
| Routing | `decision`, `selected_service`, `candidates_considered`, `registry_source` | Requests and escalations |
| Validation | `envelope_valid`, `content_schema_valid`, `authentication_verified` | Every message |
| Timing | `received_at`, `routed_at`, `dispatcher_overhead_ms` | Every message |
| Constraints | `deadline`, `remaining_budget_ms` | Requests |
| Provenance | `grade`, `grade_meets_requirement` | Responses and escalations |
| Resources | `service_latency_ms`, `cost_budget_remaining` | Responses |
| Errors | `error_code`, `error_detail`, `retry_count` | Errors and retries |
| Dispatcher | `dispatcher_id`, `ccdp_version` | Every message |

## 11.5. Audit Storage and Retention

This specification does not mandate a specific audit storage mechanism. Implementations MAY use structured log files, a database, an event stream (e.g., Kafka), or any other storage that satisfies these requirements:

1. **Immutability.** Audit records, once written, MUST NOT be modified or deleted during the retention period. Append-only storage is RECOMMENDED.
2. **Queryability.** The audit store MUST support queries by `trace_id` (retrieve all records for a request chain), `request_id` (retrieve records for a specific request), `service_id` (retrieve records for a specific service), and time range.
3. **Retention.** Audit records MUST be retained for a minimum period configured per deployment. The RECOMMENDED minimum retention period is 90 days for production deployments.
4. **Integrity.** Audit records SHOULD be protected against tampering. Implementations SHOULD use cryptographic hashing (hash chains or Merkle trees) to detect unauthorized modifications.

## 11.6. Audit as Supervision Input

The audit trail is not just a compliance mechanism — it is the Human Supervisor's primary input for understanding system behavior. Deployments SHOULD provide tooling that enables:

- **Request tracing:** Given a `trace_id`, reconstruct the full journey of a request — every routing decision, every service invocation, every escalation, every provenance grade.
- **Provenance verification:** Given a Response, verify its provenance chain by re-checking evidence entries against the audit trail.
- **Performance analysis:** Identify latency bottlenecks, cost outliers, and routing inefficiencies from audit timing data.
- **Health monitoring:** Detect Service degradation patterns from audit error and escalation data.
- **Grade distribution analysis:** Monitor the distribution of provenance grades over time to detect grade inflation, systematic under-verification, or changes in service quality.

This tooling is outside the scope of this specification but is essential for the supervision-tree architecture to function. The audit trail provides the data; the tooling makes it actionable.
