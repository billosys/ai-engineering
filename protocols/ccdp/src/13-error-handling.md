# 13. Error Handling and Escalation

## 13.1. Error Philosophy

CCDP distinguishes three categories of failure, each with different protocol behavior:

1. **Protocol errors** — the message is malformed, the route is invalid, the authentication fails. These are dispatcher-detected and produce immediate error responses. They never reach a Service.

2. **Service errors** — the Service itself fails: crashes, times out, returns garbage. These are infrastructure failures. The Dispatcher retries, reroutes, or errors.

3. **Epistemic insufficiency** — the Service operates correctly but cannot meet the Request's epistemic requirements: the achieved provenance grade is below threshold, capability is exceeded, or the search space is exhausted without a determination. These are *not errors*. They are Escalations — structured routing events that the Dispatcher handles as normal protocol operations.

The distinction between service errors and epistemic insufficiency is load-bearing. An HTTP 500 means something broke. An Escalation with reason `PROVENANCE_BELOW_REQUIREMENT` means the originating actor — a Service or the Dispatcher — determined that the response does not or cannot meet the requested provenance standard. The protocol handles these differently: errors trigger retries and circuit breakers; escalations trigger the Escalation Chain.

This is the "let it crash" principle applied to cognitive systems: a Service that cannot meet the standard *should* escalate rather than silently producing low-quality output that poisons everything built on it.

## 13.2. Protocol Error Codes

Protocol errors are returned as JSON-RPC 2.0 error responses. CCDP defines the following error codes in addition to the standard JSON-RPC error codes:

| Code | Name | Meaning |
|------|------|---------|
| `-32700` | Parse error | Invalid JSON |
| `-32600` | Invalid request | Not a valid JSON-RPC request or unrecognized CCDP message type |
| `-32601` | Method not found | Unrecognized CCDP method |
| `-32602` | Invalid params | Malformed CCDP envelope (missing required fields, invalid types) |
| `-32603` | Internal error | Dispatcher internal error |
| `-32001` | Service unavailable | Explicit destination Service is not registered, not ACTIVE, or not healthy |
| `-32002` | No service for capability | No Service registered for the requested Capability Type |
| `-32003` | All services unhealthy | All Services for the Capability Type are unhealthy |
| `-32004` | Deadline not achievable | No Service can plausibly respond within the remaining deadline |
| `-32005` | Provenance not achievable | No Service can meet the requested provenance requirement |
| `-32006` | Escalation chain exhausted | All targets in the Escalation Chain have been tried and failed or escalated |
| `-32007` | Deadline exceeded | The deadline has passed before the Request could be processed |
| `-32008` | Authentication failed | The sender's identity could not be verified |
| `-32009` | Authorization denied | The sender is authenticated but not authorized for this Capability Type |
| `-32010` | Schema validation failed | The Content does not conform to the Capability Record's input or output schema |
| `-32011` | Replay detected | A message with this `request_id` and a different payload has already been processed |
| `-32012` | Decomposition limit exceeded | A decomposition plan exceeds the configured depth, width, or total-node limit (Section 14.6). The `data` object MUST include `limit_type` (`"depth"`, `"width"`, or `"total_nodes"`), `limit_value` (the configured maximum), and `actual_value` (the plan's value). |
| `-32014` | Rate limited | The Dispatcher is rate-limiting the requester. The `data` object MUST include `retry_after_ms` (integer). |

For every CCDP error code, the `data` object MUST include at minimum: `trace_id` (string), `request_id` (string), and `timestamp` (ISO 8601). Error-specific fields are defined per code in the table above. This ensures that errors are audit-correlatable even when the full envelope is unavailable.

Error responses include structured detail:

```json
{
  "jsonrpc": "2.0",
  "id": "550e8400-...",
  "error": {
    "code": -32010,
    "message": "Schema validation failed",
    "data": {
      "validation_errors": [
        {
          "path": "$.content.body.formula",
          "message": "required field missing",
          "schema_ref": "org.ccdp.deduction/input/v2"
        }
      ],
      "trace_id": "4bf92f3577b34da6a3ce929d0e0e4736",
      "request_id": "550e8400-e29b-41d4-a716-446655440000",
      "timestamp": "2026-08-03T14:30:00.145Z",
      "dispatcher_id": "dispatcher-prod-01"
    }
  }
}
```

All protocol errors MUST be logged in the audit trail.

## 13.3. Escalation Reasons

Escalation is a first-class message type, not an error. The following escalation reasons are defined:

| Reason | Meaning | Typical Next Step |
|--------|---------|-------------------|
| `PROVENANCE_BELOW_REQUIREMENT` | The originating actor determined that the requested `provenance_requirement` (Section 7.3.2) is not or cannot be met: the achievable or achieved grade is below `min_policy_grade`, or the required methods or artifact types are not or cannot be satisfied. **Service-generated:** the Service reports that its best achievable grade falls below the requirement before or during processing. **Dispatcher-generated:** the Dispatcher detects a post-receipt provenance mismatch (`provenance_mismatch_policy`, Section 9) or a routing-time no-candidate failure (`provenance_unavailable_policy`, Section 9). The `escalation_origin` field (Section 13.4.1) distinguishes the two sources. The escalation includes the best grade achieved (if any) and the requirement that was not met. | Route to higher-capability Service or human |
| `CAPABILITY_EXCEEDED` | The request exceeds the Service's capability (too complex, wrong domain) | Route to different Service with broader capability |
| `DEADLINE_INSUFFICIENT` | Remaining deadline budget is insufficient for this Service to complete | Route to faster Service or return partial result |
| `DEADLINE_APPROACHING` | Service started work but cannot finish before deadline; partial result available | Forward partial result; route remainder to faster Service |
| `BUDGET_EXCEEDED` | The request would exceed the cost budget | Route to cheaper Service or request budget increase |
| `SEARCH_EXHAUSTED` | The Service has explored its search space without finding a solution and cannot determine whether the problem is solvable. This is distinct from a proven-unsolvable result (which is a RESPONSE, not an Escalation). | Route to a Service with a larger search budget or different method, or to a human |
| `AMBIGUOUS_INPUT` | The input is ambiguous and the Service cannot safely interpret it | Route to human for clarification, or to an LLM for disambiguation |
| `INTERNAL_DEGRADATION` | The Service is experiencing internal degradation and prefers not to handle this request | Route to alternative Service |
| `REQUIRES_HUMAN` | The Service explicitly requests human involvement (e.g., for specification review) | Route to human review queue |

When a Service returns a Response that fails the request's `provenance_requirement` post-receipt, the Dispatcher's `provenance_mismatch_policy` (Section 9.2) determines whether to reroute or escalate.

**Design note on SEARCH_EXHAUSTED:** A proven-unsolvable result is information, not failure. If a theorem prover determines that a formula is unsatisfiable, that is a correct, valuable result — it should be returned as a RESPONSE with grade FORMALLY_VERIFIED, not as an Escalation. An Escalation with reason SEARCH_EXHAUSTED is appropriate when the Service *cannot determine* whether the problem is solvable (e.g., the search space is too large) and is returning the problem rather than a result.

Implementations MAY define additional escalation reasons using reverse-domain notation (e.g., `com.example.custom_reason`).

## 13.4. Escalation Chain Processing

When the Dispatcher receives an Escalation, it processes the Escalation Chain:

```
┌───────────┐    Escalation   ┌───────────┐    Escalation  ┌──────────┐
│ Service A │────────────────▶│ Service B │───────────────▶│  Human   │
│  (LLM)    │  PROVENANCE_    │ (Prover)  │  CAPABILITY_   │  Queue   │
│           │  BELOW_REQ.*    │           │  EXCEEDED      │          │
└───────────┘                 └───────────┘                └──────────┘
      ▲                             ▲                            ▲
      │         Dispatcher          │        Dispatcher          │
      │         routes to           │        routes to           │
      │         next in chain       │        next in chain       │
```
\* Abbreviated for diagram width; full reason name is `PROVENANCE_BELOW_REQUIREMENT`.

The following algorithm applies to **Service-originated Escalations** (where a Service returned an ESCALATION message). For **Dispatcher-generated implicit Escalations**, the chain source depends on the triggering policy — see "Dispatcher-generated implicit Escalations" below.

The algorithm:

1. Receive Escalation from Service A.
2. Log the Escalation in the audit trail with full context.
3. If `escalation.suggested_target` is set and the target is healthy, route to it. Suggested targets from the escalating Service MUST pass the same full routing checks as chain targets (Step 5): authorization, capability match, provenance feasibility, deadline, budget, and isolation. A Service's suggestion is a routing hint, not a policy override.
4. Otherwise, walk Service A's `escalation_chain` in order.
5. For each chain target:
   a. If the target is a Service ID, check health and route if healthy.
   b. If the target is a Capability Type, query the Registry and route per normal routing (Section 9.2).
   c. If the target has already been tried for this `request_id` (cycle detection), skip it.
   d. Verify the requester is authorized for the target's Capability Type (or the token scope covers it).
   e. Verify the remaining cost budget is sufficient for the target's cost hints.
   f. Verify the target can meet the request's data-class/isolation requirements (from Registry metadata).
   g. If any check fails, skip the target and continue to the next in the chain. Log the skip reason in the audit trail.
6. If all chain targets are exhausted, route to `org.ccdp.human_review` as the terminal target. The human-review fallback MUST still pass authorization and data-class checks. If the requester's token does not authorize `org.ccdp.human_review`, or if the request's data-class/isolation requirements cannot be met by the human queue, the Dispatcher MUST return error `-32006` (escalation chain exhausted) rather than silently routing to an unauthorized or non-compliant target.
7. If no human review Service is available, return error `-32006`.

The Dispatcher MUST forward the original Request (not the Escalation) to the next target in the chain. The Dispatcher accumulates partial results from prior escalation targets in the forwarded Request's metadata under `org.ccdp.partial_results`. The most recent escalating Service's partial result is in that Service's ESCALATION message Content (the canonical location per Section 7.3.4). The metadata accumulation provides downstream Services and human reviewers with the full escalation history.

**Dispatcher-generated implicit Escalations.** Section 9.2 defines two deployment policies that produce implicit `PROVENANCE_BELOW_REQUIREMENT` escalations without a Service-originated ESCALATION message:

- `provenance_mismatch_policy="escalate"`: the Dispatcher received a Response whose provenance did not meet the requirement. The responding Service's `escalation_chain` is used as the chain source, since a specific Service record is available.
- `provenance_unavailable_policy="escalate"`: no candidate Service could satisfy the provenance requirement at routing time. No originating Service record is available, so the implicit escalation routes directly to `org.ccdp.human_review` (bypassing chain walk).

Both cases MUST set `envelope.escalation.escalation_origin` to `"dispatcher"` (Section 7.3.4) and MUST be audit-logged with the same fidelity as Service-originated Escalations.

### 13.4.1. Escalation Metadata Accumulation

As a Request traverses the Escalation Chain, the Dispatcher accumulates escalation history in the Request's metadata:

```json
{
  "metadata": {
    "org.ccdp.escalation_history": [
      {
        "service_id": "llm-verifier-01",
        "reason": "PROVENANCE_BELOW_REQUIREMENT",
        "escalation_origin": "service",
        "achieved_grade": "HEURISTIC",
        "timestamp": "2026-08-03T14:30:05.000Z"
      },
      {
        "service_id": "z3-prover-01",
        "reason": "CAPABILITY_EXCEEDED",
        "escalation_origin": "service",
        "detail": "Formula exceeds solver timeout",
        "timestamp": "2026-08-03T14:30:35.000Z"
      }
    ],
    "org.ccdp.partial_results": [
      {
        "service_id": "llm-verifier-01",
        "provenance": { "grade": "HEURISTIC" },
        "content": { /* ... */ }
      }
    ]
  }
}
```

This history enables downstream Services (and the Human Supervisor) to understand what has already been tried and what partial results are available.

The `escalation_origin` field is REQUIRED in each escalation-history entry. Its value MUST match the `envelope.escalation.escalation_origin` from the Escalation message (Section 7.3.4): `"service"` when the Escalation originated from a Service's ESCALATION message, or `"dispatcher"` when the Dispatcher generated an implicit Escalation from a routing-time or post-receipt provenance policy (Section 9.2).

## 13.5. Service Error Handling

When a Service fails (as opposed to escalating), the Dispatcher follows a retry-and-reroute strategy:

### 13.5.1. Transient Failures

Network errors, HTTP 5xx responses, and timeouts are treated as transient failures:

1. **Retry** the same Service if `remaining_budget_ms` permits, using exponential backoff (RECOMMENDED: initial delay 100ms, multiplier 2, max 3 retries).
2. **Reroute** to an alternative Service if one is available and the retry budget is exhausted.
3. **Error** if no alternative is available and retries are exhausted.

Each retry and reroute is logged in the audit trail.

### 13.5.2. Permanent Failures

A Service that returns a CCDP error response (a JSON-RPC error with a CCDP error code) is treated as a permanent failure for this Request:

1. Do NOT retry the same Service for this Request.
2. Reroute to an alternative Service if the error suggests it (e.g., `-32010` schema validation failed may succeed with a different Service version). Rerouting after schema validation failure is appropriate only when the alternative Service supports a compatible schema version. The Dispatcher SHOULD check schema version compatibility in the Registry before rerouting, rather than blindly forwarding to another Service. Automatic rerouting to a different service version after a schema validation failure is permitted only when the request includes `org.ccdp.allow_schema_version_fallback: true` in the request metadata. This flag defaults to `false`. When absent or `false`, schema validation failures are permanent errors — the Dispatcher MUST return the error to the requester rather than attempting version fallback.
3. Error if no alternative is available.

### 13.5.3. Malformed Responses

If a Service returns a response that is valid JSON-RPC but invalid CCDP (missing required envelope fields, missing provenance, content does not match output schema), the Dispatcher:

1. Logs the malformed response in the audit trail with full detail.
2. Treats it as a service error and follows the retry/reroute strategy.
3. Increments the Service's failure count in the circuit breaker.
4. Does NOT forward the malformed response to the requester.

## 13.6. Health Monitoring and Circuit Breakers

### 13.6.1. Health Check Protocol

The Dispatcher probes each Service's health at the interval specified in the Service's Capability Record (`health_check.interval_seconds`). Health checks use the `ccdp/health.request` method. The response is a HEALTH_RESPONSE — a JSON-RPC result (not a method-bearing message) whose `envelope.type` is `"HEALTH_RESPONSE"`. The Dispatcher interprets the structured result to update its health table. (Section 7.3.6)

A health check probe:
1. Sends a HEALTH_REQUEST to the Service's health endpoint.
2. Waits for a HEALTH_RESPONSE within `health_check.timeout_ms`.
3. If no response within the timeout, marks the Service as UNHEALTHY.
4. If a response arrives, updates the Service's Health Status, capacity, and per-capability load in the Routing Table.

### 13.6.2. Health and Circuit Breaker State Transitions

The Dispatcher tracks two related but distinct state machines for each Service: the Service's **Health Status** (HEALTHY, DEGRADED, UNHEALTHY) as reported by the Service itself, and the **circuit breaker state** (CLOSED, OPEN, HALF_OPEN) as maintained by the Dispatcher based on observed failures (Section 9.6). These two machines interact — a CLOSED circuit breaker can open when an otherwise-HEALTHY service has too many observed failures — but they are tracked independently: Health Status is Service-reported (via HEALTH_RESPONSE messages), while circuit breaker state is Dispatcher-maintained (from observed request outcomes). The diagram below is an illustrative combined view showing the typical co-occurrence of states; the per-state-machine transition rules that follow are the normative definitions.

```
                ┌──────────────────────────┐
                │                          │
     ┌──────────▼──┐  failure threshold   ┌┴───────────┐
     │   HEALTHY   │─────────────────────▶│  DEGRADED  │
     │  (CLOSED)   │                      │  (CLOSED)  │
     └──────┬──────┘                      └──────┬─────┘
            │                                    │
            │              ┌─────────────────────┘
            │              │  continued failures
            │              ▼
            │        ┌───────────┐
            │        │ UNHEALTHY │
            │        │  (OPEN)   │
            │        └─────┬─────┘
            │              │
            │              │  health probe succeeds
            │              ▼
            │        ┌───────────┐
            └────────┤ UNHEALTHY │
             success │(HALF_OPEN)│
                     └───────────┘
```

Health Status transitions (Service-reported or Dispatcher-inferred):

- **HEALTHY → DEGRADED:** The Service reports DEGRADED status, or the failure rate exceeds a configurable threshold (RECOMMENDED: 3 failures in 60 seconds).
- **DEGRADED → UNHEALTHY:** The Service reports UNHEALTHY status, or the failure rate exceeds a higher threshold, or the Service fails to respond to health probes.
- **UNHEALTHY → HEALTHY:** The Service reports HEALTHY status in a health probe response, and a configurable number of subsequent requests succeed (RECOMMENDED: 3).

Circuit breaker transitions (Dispatcher-maintained, per Section 9.6):

- **CLOSED → OPEN:** Failure count exceeds `failure_threshold` within `failure_window_seconds`. The Dispatcher stops routing requests to this Service.
- **OPEN → HALF_OPEN:** A configurable recovery period elapses (RECOMMENDED: 30 seconds). The Dispatcher allows a limited number of probe requests.
- **HALF_OPEN → CLOSED:** A configurable number of requests succeed (RECOMMENDED: 3).
- **HALF_OPEN → OPEN:** Any request fails in the half-open state.

### 13.6.3. Circuit Breaker Configuration

Circuit breaker parameters are implementation-defined but SHOULD include:

- `failure_threshold`: Number of failures before opening the circuit (RECOMMENDED: 5).
- `failure_window_seconds`: Time window for counting failures (RECOMMENDED: 60).
- `recovery_probe_interval_seconds`: How often to probe an UNHEALTHY Service (RECOMMENDED: 30).
- `half_open_request_limit`: Number of requests to allow in HALF_OPEN state (RECOMMENDED: 3).

All circuit breaker state transitions MUST be logged in the audit trail.

## 13.7. Graceful Degradation

A Service MAY signal partial capability through the DEGRADED health status with per-capability availability:

```json
{
  "health": {
    "status": "DEGRADED",
    "capabilities": {
      "org.ccdp.deduction": { "available": true, "current_load": 0.95 },
      "org.ccdp.verification": { "available": false }
    },
    "detail": "Verification subsystem undergoing maintenance"
  }
}
```

A DEGRADED Service with `available: true` for a specific capability remains eligible for routing to that capability, but is deprioritized relative to HEALTHY Services. A DEGRADED Service with `available: false` for a capability is treated as UNHEALTHY for that capability only.

This enables finer-grained routing than binary healthy/unhealthy — a Service can shed its most expensive capability while continuing to serve cheaper ones.
