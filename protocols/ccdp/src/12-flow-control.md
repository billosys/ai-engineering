# 12. Flow Control and Resource Signals

## 12.1. The Resource Problem

Cognitive services have wildly heterogeneous resource characteristics. An LLM inference may cost $0.50 and take 10 seconds. A Z3 solver may cost $0.001 and take 500 milliseconds — or 30 minutes for a hard problem. A human review may cost $50 and take 2 days. A classifier may cost $0.0001 and take 20 milliseconds.

Without resource signals, the Dispatcher cannot make resource-rational decisions. TCP solved this problem with congestion control — window advertisements, ECN, slow start, AIMD. CCDP solves it with explicit resource signals at the protocol level: cost budgets on requests, resource consumption on responses, and capacity advertisements from services.

## 12.2. Cost Budgets

A Request MAY carry a `cost_budget` field constraining the resources the Service may consume (Section 7.3.2). The cost budget is an envelope field, readable by the Dispatcher without Content inspection.

### 12.2.1. Budget Fields

```json
{
  "cost_budget": {
    "max_compute_seconds": 120,
    "max_tokens": 50000,
    "max_monetary_cost": "0.50",
    "monetary_unit": "USD"
  }
}
```

All fields are OPTIONAL. Omitted fields indicate no constraint on that dimension. Monetary values are strings to avoid IEEE 754 floating-point precision issues (Section 2.3). Implementations MUST parse monetary strings as decimal values, not floating-point. A Service MUST NOT exceed any specified constraint. Services SHOULD implement preflight estimation where feasible — estimating resource consumption before beginning work and returning an Escalation with reason `BUDGET_EXCEEDED` if the estimate exceeds the budget. For services where cost is unpredictable (LLM generation with variable output length), the Service MUST monitor consumption during execution and abort with an Escalation if any budget limit is reached. If a Service would exceed a constraint to produce a meaningful result, it MUST return an Escalation with reason `BUDGET_EXCEEDED`, reporting the resources consumed so far and an estimate of resources needed.

When escalation reason is `BUDGET_EXCEEDED`, the `escalation` object MUST include:

```json
"budget_exceeded": {
  "dimension": "monetary" | "compute_seconds" | "tokens",
  "budget_limit": "4.50",
  "actual_or_estimated": "2.80",
  "is_estimate": true
}
```

The `detail` field MAY contain a human-readable explanation in addition to the structured fields.

### 12.2.2. Budget Propagation

When the Dispatcher routes a Request, it MAY adjust the cost budget based on routing overhead:

- `max_compute_seconds`: No adjustment (this constrains the Service, not the Dispatcher).
- `max_monetary_cost`: The Dispatcher MAY subtract its own routing cost (if any) before forwarding.
- `max_tokens`: No adjustment (this constrains token-consuming services).

For Decomposition (Section 14), the Dispatcher partitions the parent Request's cost budget across sub-requests according to the Decomposition Plan's budget allocation. If the plan does not specify allocation, the Dispatcher SHOULD divide the budget equally among sub-requests, reserving a configurable fraction (RECOMMENDED: 10%) for composition overhead. Equal allocation is a safe default but ignores DAG shape, service cost hints, critical-path length, and task heterogeneity. Decomposition Plans SHOULD include per-sub-request `cost_fraction` and `deadline_fraction` allocations (Section 14.3.1) that reflect the expected cost profile. When allocations are not specified, the Dispatcher MUST use equal partitioning and log a warning in the audit trail.

### 12.2.3. Budget Consumption Reporting

Every Response MUST report actual resource consumption in the `provenance.computation` field:

```json
{
  "computation": {
    "tokens_consumed": 12500,
    "compute_seconds": 4.7,
    "monetary_cost": "0.003",
    "monetary_unit": "USD",
    "model_id": "claude-opus-4-20260801"
  }
}
```

The Dispatcher records these figures in the audit trail. Over time, the audit data enables increasingly accurate cost estimation for routing decisions.

## 12.3. Capacity Advertisements

Services advertise their current capacity through Health responses (Section 7.3.6). Capacity signals enable the Dispatcher to route away from overloaded services before they fail.

### 12.3.1. Capacity Fields

```json
{
  "capacity": {
    "max_concurrent_requests": 10,
    "current_concurrent_requests": 7,
    "queue_depth": 3,
    "estimated_drain_time_ms": 15000
  }
}
```

**`max_concurrent_requests`** (integer): The maximum number of requests the Service can process simultaneously.

**`current_concurrent_requests`** (integer): How many requests the Service is currently processing.

**`queue_depth`** (integer): How many requests are queued but not yet processing.

**`estimated_drain_time_ms`** (integer): Estimated time to clear the current queue at current processing rates.

### 12.3.2. Per-Capability Load

For Services implementing multiple Capability Types, the Health response provides per-capability load information:

```json
{
  "capabilities": {
    "org.ccdp.deduction": {
      "available": true,
      "current_load": 0.70,
      "queue_depth": 2,
      "estimated_latency_ms": 8000
    },
    "org.ccdp.verification": {
      "available": false,
      "current_load": 1.0,
      "queue_depth": 5,
      "estimated_latency_ms": 30000
    }
  }
}
```

A `current_load` of 1.0 indicates the Service is at capacity for that capability. A `current_load` above 0.8 SHOULD trigger the Dispatcher to prefer alternative Services.

Capacity data in health responses is a point-in-time snapshot. The Dispatcher MUST record the timestamp of each capacity update and SHOULD treat capacity data older than the Service's `health_check.interval_seconds` as stale. For high-priority or high-cost requests, the Dispatcher SHOULD perform a synchronous health probe before routing if the cached capacity data is stale. Stale capacity data used for a routing decision MUST be noted in the audit record.

## 12.4. Deadline Propagation

Deadlines prevent unbounded latency in multi-hop request chains. The deadline mechanism is modeled on gRPC's deadline propagation [gRPC-Deadlines] and Google's `context.Context`.

### 12.4.1. Deadline Mechanics

Every Request carries a `deadline` (absolute UTC timestamp) and `remaining_budget_ms` (remaining time budget in milliseconds). At each hop through the Dispatcher:

1. The Dispatcher computes `elapsed_ms = now() - audit.received_at` (its own receive timestamp — see the clock-skew note below).
2. The Dispatcher sets `remaining_budget_ms = envelope.remaining_budget_ms - elapsed_ms`.
3. If `remaining_budget_ms <= 0`, the Dispatcher returns error `-32007` (deadline exceeded) without forwarding the Request.
4. If `remaining_budget_ms` is positive but less than the target Service's `cost_hints.estimated_latency_ms.p50`, the Dispatcher logs a warning and either forwards (optimistically) or returns error `-32004` (deadline not achievable).

**Relationship to the routing deadline filter.** The deadline filter in Section 9.2 Step 4 uses the Service's p95 estimated latency as the feasibility threshold: if `remaining_budget_ms < p95_latency_ms`, the service is filtered out of candidacy entirely. This step's p50 check applies to a Service that already survived that filter — it is re-evaluating margin at actual dispatch time, after further elapsed time has accrued hop-by-hop since the routing decision was made. Section 12.4.1 permits optimistic forwarding when remaining time has degraded below the Service's p50 but has not yet fallen below p95, on the grounds that the request may still succeed. These two rules are consistent: the routing filter removes candidates that almost certainly cannot meet the deadline (below p95), while flow control allows the best remaining candidate to attempt the request even with tight margins (between p50 and p95).

**Clock skew.** The Dispatcher MUST compute `remaining_budget_ms` from its own receive timestamp (`audit.received_at`), not from the originator's `envelope.timestamp`. The originator's timestamp is used for replay protection and freshness validation (Section 15.5), not for hop-by-hop deadline accounting. This avoids clock-skew errors between the originator and the Dispatcher.

### 12.4.2. Service Deadline Behavior

A Service that receives a Request with `remaining_budget_ms` SHOULD:

1. Check whether it can plausibly complete within the budget.
2. If not, return an Escalation with reason `DEADLINE_INSUFFICIENT` immediately, rather than starting work it cannot finish.
3. If it starts work and approaches the deadline, return a partial result (if possible) with Escalation reason `DEADLINE_APPROACHING` and `partial_result_available: true`.
4. Never exceed the deadline silently — either complete in time, escalate, or error.

### 12.4.3. Decomposition and Deadlines

For decomposed requests, the Dispatcher allocates the parent's deadline budget across sub-requests:

- Sequential sub-requests share the remaining budget serially — each sub-request gets the remaining budget after previous sub-requests complete.
- Parallel sub-requests share the remaining budget — each parallel sub-request gets the same `remaining_budget_ms` (they all must complete before the parent's deadline).
- The Decomposition Plan MAY specify per-sub-request time allocations that override the default allocation.

## 12.5. Back-Pressure

When a Service is overloaded, it needs a way to signal the Dispatcher to slow down. CCDP supports back-pressure through three mechanisms:

### 12.5.1. Health-Based Back-Pressure

The primary back-pressure mechanism. When a Service's `health.status` transitions to DEGRADED, the Dispatcher deprioritizes it in routing (Section 9.6). When it transitions to UNHEALTHY, the Dispatcher stops routing to it entirely.

This is the "let it crash" principle: a Service under unsustainable load declares itself degraded, and the Dispatcher routes around it rather than continuing to add load.

### 12.5.2. HTTP 429 (Too Many Requests)

A Service MAY respond to a CCDP Request with HTTP 429 instead of a CCDP Response. The `Retry-After` header (in seconds) tells the Dispatcher when to retry. The Dispatcher:

1. MUST NOT retry before the `Retry-After` period.
2. SHOULD route to an alternative Service if one is available.
3. MUST log the 429 response in the audit trail.
4. SHOULD increment the Service's failure count in the circuit breaker.

More precisely: when a Service returns HTTP 429 (Too Many Requests) instead of a CCDP Response, the Dispatcher MUST: (a) log the 429 in the audit trail as a rate-limit event with the Service's `Retry-After` header value if present, (b) treat the Service as temporarily at capacity (equivalent to health status DEGRADED for the requested capability), (c) follow the retry/reroute strategy in Section 13.5.1, and (d) if the Dispatcher itself rate-limits a requester, it MUST return a CCDP error response with code `-32014` (rate limited) and include the `Retry-After` value in the error `data` field. Error `-32003` is reserved for all-services-unhealthy conditions (Section 9.2 Step 3); it is distinct from Dispatcher-side rate limiting. HTTP 429 MUST NOT be passed through to the requester as a raw HTTP response.

### 12.5.3. Capacity-Based Rate Limiting

The Dispatcher MAY implement rate limiting per Service based on capacity advertisements. If a Service reports `current_load > 0.9`, the Dispatcher SHOULD limit new requests to that Service to no more than one per `estimated_latency_ms` period, allowing the queue to drain.

The specific rate-limiting algorithm is implementation-defined. The Dispatcher MUST log all rate-limiting decisions in the audit trail.

## 12.6. Resource-Aware Routing

The Dispatcher uses resource signals for routing decisions (Section 9.2, Step 6). The interaction between resource signals and routing:

- **Cost budget constrains candidates:** A Request with `max_monetary_cost: "0.10"` eliminates Services with `estimated_cost_per_request > "0.10"` (compared as decimal values, not floating-point).
- **Deadline constrains candidates:** A Request with 5 seconds remaining eliminates Services with `estimated_latency_ms.p95 > 5000`.
- **Load influences ranking:** Among eligible candidates, lower-load Services are preferred.
- **Cost influences ranking:** Among eligible candidates, lower-cost Services are preferred (unless a higher-cost Service offers a better provenance grade that the Request requires).

This produces a natural resource-rational routing behavior: cheap, fast, lightly-loaded Services are preferred, with expensive or slow Services used only when cheaper alternatives are unavailable, unhealthy, or insufficient for the requested provenance level.

## 12.7. Bullwhip Effect Warning

The operations research literature documents the "bullwhip effect" [Bullwhip]: in serial supply chains, demand variance amplifies upstream — a small fluctuation at the consumer end creates violent oscillations at the supplier end.

In CCDP, the analog is error amplification across serial cognitive operations. A small uncertainty in Decomposition can produce large errors in downstream sub-results, which compound when composed. The protocol does not solve this problem directly — it is a content-level concern, not a protocol-level one — but it provides the tools for detecting it:

- The composition trace (Section 10.5.4) makes the propagation path visible.
- Provenance grades on each sub-result quantify uncertainty at each stage.
- The audit trail records the full decomposition and composition chain.

Deployments SHOULD monitor for bullwhip patterns: systematically decreasing provenance grades in downstream sub-requests, or decomposition chains where the composed grade is consistently much lower than any individual sub-result grade.
