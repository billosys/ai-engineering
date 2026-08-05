# message-health-response.json — field citations and derivation notes

Maximal HEALTH_RESPONSE as a JSON-RPC 2.0 response (`result` object;
`envelope.type` identifies the CCDP type — §7.2, §13.6.1). Scenario: DEGRADED
with per-capability availability, so `detail` and `available: false` are
coherently present (§13.7).

| Field | Req. | Defining section |
|---|---|---|
| common fields | R | §7.3.1 |
| `health.status` | R (`HEALTHY`/`DEGRADED`/`UNHEALTHY`) | §7.3.6, §4 (Health Status) |
| `health.capabilities` | O; per-capability keys → `{available, current_load, queue_depth, estimated_latency_ms}` | §7.3.6, §12.3.2, §13.7 |
| `health.capacity.max_concurrent_requests` | — | §7.3.6, §12.3.1 |
| `health.capacity.current_concurrent_requests` | — | §7.3.6, §12.3.1 |
| `health.capacity.queue_depth` | — | §12.3.1 only (absent from the §7.3.6 capacity example) |
| `health.capacity.estimated_drain_time_ms` | — | §12.3.1 only |
| `health.detail` | O | §7.3.6, §13.7 |

Content omitted for the same reason as HEALTH_REQUEST (F-06).

Derived values: `request_id`/`id`/`span_id`/timestamp (correlated with
message-health-request.json). Health payload values merge the §7.3.6, §12.3.1,
§12.3.2, and §13.7 examples.
