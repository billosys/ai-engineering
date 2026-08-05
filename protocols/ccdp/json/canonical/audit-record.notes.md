# audit-record.json — field citations and derivation notes

The audit record's shape varies by message type (Table 11.2); no single
instance can coherently carry every substructure. This canonical instance is
the *richest coherent* case: a **Dispatcher-generated ESCALATION record**
(post-receipt provenance mismatch, `provenance_mismatch_policy="escalate"`),
which is the only record type that carries `provenance_policy.*`,
`escalation_routing.*` (incl. `chain_source`), and `provenance_summary`
together (Table 11.3). Substructures specific to other record types are listed
at the bottom with citations; completed examples of those live in
`examples/11-audit-trail/`.

## Common fields — required on every audit record (Table 11.1)

| Field | Defining section |
|---|---|
| `record_id` (UUID v4) | Table 11.1 — note the spec's own examples use `audit-`-prefixed values, not bare UUIDs; F-21 |
| `audit_schema_version` (`"1.0"`) | §11.1, Table 11.1 |
| `timestamp` | Table 11.1 |
| `dispatcher_id` | Table 11.1 |
| `ccdp_version` | Table 11.1 |
| `trace_context.trace_id`, `trace_context.span_id` | Table 11.1, §11.3 |
| `trace_context.parent_span_id` | §11.2 example (Identity category, §11.4) |
| `message_summary.type` | Table 11.1 |

## Message-type-specific fields shown (Table 11.2, ESCALATION column + §11.2.2)

| Field | Req. (ESCALATION) | Defining section |
|---|---|---|
| `message_summary.request_id` | R | Table 11.2 |
| `message_summary.capability_type` | S | Table 11.2 |
| `message_summary.destination_id` | S | Table 11.2 |
| `message_summary.source_id` | R | Table 11.2 |
| `message_summary.priority` | (from §11.2 example) | §11.2 |
| `message_summary.escalation_reason` | R | Table 11.2, §11.2.2 |
| `message_summary.escalation_origin` | R | Table 11.2, §11.2.2 |
| `message_summary.achieved_grade` | S | Table 11.2 |
| `message_summary.requested_grade` | S | Table 11.2 |
| `routing.decision` | R | Table 11.2; sub-fields §11.2 example, §9.2 Step 7 |
| `routing.candidates_considered`, `candidates_filtered.{health,deadline,provenance}`, `selected_service`, `registry_source`, `registry_query_ms` | — | §11.2 example |
| `provenance_summary.{grade, evidence_count, evidence_methods, scope, grade_meets_requirement, composition_method}` | R (object) | Table 11.2; sub-fields §11.2.1 example |
| `provenance_policy.{policy_field, selected_action, trigger, expected_grade, actual_grade, missing_methods, missing_artifact_types, non_conformant_service_id}` | REQUIRED when a provenance policy fired (Table 11.3; marked S in Table 11.2 because conditional) | §11.2.2, §11.4, §9.2 |
| `escalation_routing.{original_service, escalation_chain_position, next_target, chain_remaining, partial_result_forwarded, chain_source}` | — (`chain_source` REQUIRED for escalate outcomes, Table 11.3) | §11.2.2, §11.4 |
| `timing.{received_at, routed_at, dispatcher_overhead_ms}` | Timing category | §11.2 example, §11.4 |

## Substructures NOT representable on this record type

| Substructure | Applies to | Defining section |
|---|---|---|
| `validation.{envelope_valid, content_schema_valid, schema_version, authentication_verified, authorization_verified}` | REQUEST (R for `content_schema_valid`), RESPONSE (S) | §11.2, Table 11.2 |
| `constraints.{deadline, remaining_budget_ms, cost_budget, provenance_requirement}` | REQUEST | §11.2 |
| `resource_consumption.{service_compute_seconds, service_tokens_consumed, total_latency_ms, cost_budget_remaining}` | RESPONSE | §11.2.1 |
| `validation.{output_schema_valid, provenance_present, provenance_grade_valid}` | RESPONSE | §11.2.1 |
| `timing.{service_invoked_at, response_received_at, response_forwarded_at, service_latency_ms}` | RESPONSE | §11.2.1 |
| `health_summary.status` | HEALTH_RESP (R) | Table 11.2 — **never defined or exemplified anywhere else; F-22** |
| `error_code`, `error_detail`, `retry_count` | Errors category | §11.4 category table only — **never defined or exemplified; F-22** |

## Derived (invented) values

`record_id` value, timestamps at :35, `destination_id`/`priority` on this
record, `routing.decision: "escalate"` (decision vocabulary is open — §9.2
Step 7 gives examples), `dispatcher_overhead_ms`. Other values reuse the
§11.2.2 examples.
