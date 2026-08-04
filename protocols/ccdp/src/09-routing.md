# 9. Routing

## 9.1. Routing Principles

Routing is the Dispatcher's core function: given a Request with a `capability_type`, select the Service best suited to handle it. CCDP routing is *envelope-based* — the Dispatcher makes routing decisions from envelope metadata and Registry data, never from Content.

Three principles govern routing:

1. **Capability-type dispatch.** The primary routing key is `envelope.capability_type`. The Dispatcher queries the Registry for Services that implement this type and are ACTIVE.

2. **Cost-aware selection.** Among eligible Services, the Dispatcher selects based on cost hints (latency, monetary cost, compute intensity), health status, current load, and the Request's constraints (deadline, cost_budget, provenance_requirement).

3. **Deterministic tiebreaking.** When multiple Services are equally suitable, the Dispatcher applies a deterministic tiebreaking rule (e.g., round-robin, lowest-load, consistent hashing by request_id). The specific tiebreaking strategy is implementation-defined but MUST be logged.

## 9.2. Routing Algorithm

The Dispatcher MUST implement the following routing algorithm. Steps are ordered; the Dispatcher proceeds to the next step only if the current step does not resolve the routing decision.

### Step 1: Explicit Destination

If `envelope.destination_id` is non-null, route to the specified Service. If the Service is not registered, not ACTIVE, or not healthy, return error `-32001` (service unavailable). Do not fall through to capability-based routing. Explicit destinations MUST also pass authorization, provenance feasibility, deadline, budget, and isolation checks — the same policy filters applied to normal routing (Steps 2–6). An explicit destination is a routing hint, not a bypass of protocol enforcement. If any check fails, the Dispatcher MUST return the appropriate error, not silently fall through to normal routing.

### Step 2: Capability Lookup

Query the Registry for all ACTIVE Services implementing `envelope.capability_type`. If no Services are found, return error `-32002` (no service for capability type).

### Step 3: Health Filter

Remove Services with Health Status UNHEALTHY from the candidate set. Services with Health Status DEGRADED remain eligible but are deprioritized (Step 6).

If all Services are UNHEALTHY, the Dispatcher MUST follow its deployment-configured `all_unhealthy_policy` for the requested capability type. The policy MUST be one of: `"error"` (return error `-32003`), `"escalate"` (treat as an escalation with reason `INTERNAL_DEGRADATION` and walk the escalation chain), or `"queue"` (hold the request for up to `queue_timeout_ms` milliseconds, configurable per capability type, default 30000ms; retry routing when a service becomes healthy or when the timeout expires). If the request has a deadline and the remaining deadline budget is less than `queue_timeout_ms`, the effective queue timeout is the remaining deadline budget. If the timeout expires without a healthy service, the Dispatcher returns error `-32003`. Queued requests are audit-logged with status `"queued"` and a follow-up audit entry when dequeued (routed or timed out). The default policy is `"error"`. The chosen policy MUST be recorded in the audit trail.

### Step 4: Deadline Filter

Remove Services whose `cost_hints.estimated_latency_ms.p95` exceeds `envelope.remaining_budget_ms`. A Service that is unlikely to respond within the deadline is not a viable candidate.

If all candidate services are filtered out by deadline, the Dispatcher MUST return error `-32004` (deadline not achievable). The Dispatcher MUST NOT silently route to a service that cannot plausibly meet the deadline. The audit record MUST include the remaining budget, the fastest candidate's estimated latency, and the filtering decision.

### Step 5: Provenance Filter

The Dispatcher applies the `provenance_requirement` fields (Section 7.3.2) in two stages:

1. **`min_policy_grade` (fast filter).** If set, remove Services whose `provenance_capabilities.max_grade` is below the required grade — a direct comparison against the Capability Record.
2. **`required_methods` and `required_evidence_types` (capability filter).** If set, remove Services whose Capability Record `supported_evidence_types` (Section 8.2.2) does not include every required method and evidence type. This is a Registry-declared capability check performed at routing time; the Dispatcher validates the actual response against the requirement post-receipt (Section 10.3), since a Service's declared `supported_evidence_types` is not a per-response guarantee.

If no candidate service can meet the Request's `provenance_requirement`, the Dispatcher MUST NOT silently route to a service that cannot meet it. The Dispatcher MUST follow its deployment-configured `provenance_unavailable_policy` for the requested capability type. The policy MUST be one of: `"error"` (return error `-32005`) or `"escalate"` (treat as implicit escalation with reason `PROVENANCE_BELOW_REQUIREMENT`, routing through the escalation chain to find a service that can meet the requirement). The default policy is `"error"`. The chosen policy MUST be recorded in the audit trail. The Dispatcher MUST NOT forward a request to a service that cannot meet the provenance requirement without the requester's knowledge.

### Step 6: Cost-Aware Ranking

Rank the remaining candidates using a scoring function that considers:

- **Health status:** HEALTHY Services are preferred over DEGRADED Services.
- **Current load:** Services with lower `health.capabilities[type].current_load` are preferred.
- **Estimated latency:** Lower latency is preferred, weighted against the remaining deadline budget.
- **Monetary cost:** Lower cost is preferred, weighted against the Request's `cost_budget`.
- **Provenance grade:** If the Request specifies a `provenance_requirement`, Services whose `typical_grade` meets or exceeds the requirement are preferred.
- **Queue depth:** Services with lower `health.capabilities[type].queue_depth` are preferred.

The specific scoring function is implementation-defined. This specification does not mandate weights or formulas — implementations SHOULD tune their scoring function to their deployment's priorities (latency-sensitive, cost-sensitive, quality-sensitive).

### Step 7: Selection and Logging

Select the highest-ranked candidate. Log the routing decision in the `audit.routing_decision` field (Section 7.5), including:
- `selected_service`: the Service ID selected
- `reason`: why this Service was selected (e.g., `"lowest_cost_healthy"`, `"only_candidate"`, `"explicit_destination"`)
- `candidates_considered`: how many candidates were evaluated
- `registry_query_ms`: how long the Registry query took
- `filters_applied`: which filters removed candidates (e.g., `["health", "deadline"]`)

The audit record for a routing decision MUST include at minimum: the list of candidate services considered, the normalized scoring factors (health weight, cost weight, latency weight, provenance weight), the deployment policy version used, the computed score for each candidate, and the tiebreaker (if any). This enables retrospective routing analysis and debugging.

Detailed scoring traces (candidate lists, weights, per-candidate scores) MAY contain cost and capacity information that is sensitive across administrative boundaries. Deployments SHOULD classify routing audit fields by access level and redact sensitive fields in audit exports to external parties.

## 9.3. Routing for Decomposed Sub-Requests

When the Dispatcher processes a Decomposition Plan (Section 14), it routes each sub-request independently through the same routing algorithm. Sub-requests inherit the parent's `trace_id` and `deadline` (with elapsed time subtracted) but have their own `capability_type`, `request_id`, and `span_id`.

The Dispatcher MUST respect the Decomposition Plan's dependency ordering: sub-requests with unresolved dependencies MUST NOT be dispatched until their dependencies are fulfilled. Sub-requests with no dependencies MAY be dispatched in parallel.

## 9.4. Escalation Routing

When a Service returns an Escalation, the Dispatcher routes to the next target in the Escalation Chain. Escalation routing follows a defined sequence:

1. **Suggested target.** If `escalation.suggested_target` is set and the target is healthy, route to it.
2. **Escalation chain.** If the suggested target is unavailable or not set, walk the `escalation_chain` from the Service's Capability Record. Route to the first healthy target. Escalation targets MUST be checked using the full routing algorithm (Section 9.2): capability match, health status, authorization, provenance capability, deadline feasibility, budget feasibility, isolation requirements, and cycle detection. A health-only check is insufficient — an escalation target that is healthy but unauthorized, over-budget, or incapable of the requested provenance grade MUST be skipped.
3. **Capability fallback.** If the escalation chain is exhausted, query the Registry for other Services implementing the same Capability Type (excluding the Service that escalated) and route to the best available.
4. **Human queue.** If no automated Service can handle the request, route to a Service of type `org.ccdp.human_review`. This is the terminal escalation target.
5. **Failure.** If no human review Service is available, return error `-32006` (escalation chain exhausted) to the requester.

Each escalation routing decision is logged in the audit trail with the full escalation context: which Service escalated, why, what targets were tried, and where the request ultimately landed.

## 9.5. Retry Policy

The Dispatcher SHOULD implement a retry policy for transient failures (network errors, timeouts, HTTP 503 responses). The retry policy:

- MUST respect idempotency: retries of the same `request_id` are safe because Services MUST be idempotent.
- MUST respect the deadline: no retry should be attempted if the remaining deadline budget is insufficient.
- SHOULD use exponential backoff with jitter for retries to the same Service.
- SHOULD try a different Service (if available) before retrying the same Service.
- MUST log each retry attempt in the audit trail.
- MUST limit total retries to a configurable maximum (RECOMMENDED: 3) to prevent retry storms.

## 9.6. Circuit Breaker Integration

The Dispatcher MUST implement circuit breaker logic for each Service (Section 13.6). A Service's circuit breaker has three states:

- **CLOSED** (normal operation): Requests are forwarded. Failures are counted.
- **OPEN** (tripped): Requests are NOT forwarded. The Service is excluded from routing. Periodic health probes test recovery.
- **HALF_OPEN** (testing recovery): A limited number of requests are forwarded. If they succeed, the circuit breaker returns to CLOSED. If they fail, it returns to OPEN.

The circuit breaker state is an input to routing: OPEN circuit breakers effectively remove a Service from the candidate set. The transition logic (failure thresholds, recovery probe intervals) is implementation-defined.

## 9.7. Routing Table

The Dispatcher maintains a Routing Table — a runtime data structure combining Registry data, health status, circuit breaker state, and load metrics. The Routing Table is the Dispatcher's view of the world:

```
┌──────────────────────┬────────────┬──────────┬─────────────┬──────────┐
│ Capability Type      │ Service ID │ Health   │ Circuit     │ Load     │
│                      │            │ Status   │ Breaker     │ (0.0-1.0)│
├──────────────────────┼────────────┼──────────┼─────────────┼──────────┤
│ org.ccdp.deduction   │ z3-prover  │ HEALTHY  │ CLOSED      │ 0.35     │
│ org.ccdp.deduction   │ isabelle   │ DEGRADED │ CLOSED      │ 0.80     │
│ org.ccdp.planning    │ fd-planner │ HEALTHY  │ CLOSED      │ 0.10     │
│ org.ccdp.language.*  │ llm-pool   │ HEALTHY  │ CLOSED      │ 0.55     │
│ org.ccdp.human_review│ review-q   │ HEALTHY  │ CLOSED      │ 0.20     │
│ org.ccdp.verification│ verifier   │ UNHEALTHY│ OPEN        │ —        │
└──────────────────────┴────────────┴──────────┴─────────────┴──────────┘
```

The Routing Table is refreshed from the Registry at a configurable interval (RECOMMENDED: every 30 seconds) and updated in real-time by health check responses. It is an internal Dispatcher structure, not a protocol element — its format is implementation-defined.

**Wildcard capability matching.** Capability type patterns ending in `.*` match any capability type that shares the prefix up to the wildcard. `org.ccdp.language.*` matches `org.ccdp.language.generation`, `org.ccdp.language.translation`, etc., but not `org.ccdp.language` itself (the wildcard requires at least one additional segment). Wildcard patterns are valid only in token scopes (Section 15.3.2) and routing configuration; they MUST NOT appear in Capability Records or Registry lookups. The routing table format is implementation-defined and MAY support pattern matching (e.g., glob or prefix wildcards). Pattern syntax, if supported, is not part of the CCDP wire protocol — it is a deployment-local routing configuration concern. The `org.ccdp.language.*` entry in the example above illustrates implementation flexibility, not a normative capability identifier.
