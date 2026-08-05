# capability-record.json — field citations and derivation notes

Maximal Capability Record. The §8.2.1 example is itself near-maximal — this
instance is that example verbatim, plus one addition: the
`org.ccdp.conformance_level` metadata key (§16.4).

| Field | Req. | Defining section |
|---|---|---|
| `service_id` | R | §8.2.2 |
| `capability_type` | R | §8.2.2 |
| `version` | R (SemVer; `major_version` for record identity is *derived* from it, not a field — §8.4.1) | §8.2.2, §8.5.1 |
| `endpoint` | R | §8.2.2 |
| `status` | R (`ACTIVE`/`DRAINING`/`INACTIVE`/`DEPRECATED`) | §8.2.2 |
| `input_schema` | R (JSON Schema 2020-12) | §8.2.2 |
| `output_schema` | R | §8.2.2 |
| `cost_hints.estimated_latency_ms.{p50,p95,p99}` | R | §8.2.2 |
| `cost_hints.estimated_cost_per_request.{monetary_units, monetary_unit}` | R | §8.2.2 — note `monetary_units` here is the *amount* (string decimal) while the envelope's cost field is `max_monetary_cost`; naming divergence logged as F-19 |
| `cost_hints.token_cost` | R (null for non-LLM) | §8.2.2 |
| `cost_hints.compute_intensive` | R | §8.2.2 |
| `provenance_capabilities.max_grade` | R (integer 0–7 or grade name) | §8.2.2 |
| `provenance_capabilities.typical_grade` | O (same grammar) | §8.2.2 |
| `provenance_capabilities.supported_evidence_methods` | O | §8.2.2 |
| `provenance_capabilities.supported_artifact_types` | O | §8.2.2 |
| `health_check.{endpoint, interval_seconds, timeout_ms}` | R | §8.2.2 |
| `isolation.{executes_arbitrary_code, requires_sandbox, network_access, filesystem_access}` | R | §8.2.2, §15.6.1 |
| `escalation_chain[]` | R (may be empty); typed entries `{kind: "service_id"\|"capability_type", value}` — string-only entries MUST NOT be used | §8.2.2 |
| `cacheable` | O, default false | §8.2.2 (referenced §5.2.1) |
| `max_input_size` | O (bytes; structural decomposition trigger) | §8.2.2, §14.2 |
| `tags` | O | §8.2.2 |
| `description` | O | §8.2.2 |
| `registered_at` | R | §8.2.2 |
| `updated_at` | R | §8.2.2 |
| `metadata` | O (envelope-metadata semantics) | §8.2.2, §7.7 |
| `metadata["org.ccdp.conformance_level"]` | `"core"` / `"full"` — Services MUST declare | §16.4 |

Derived values: only the `org.ccdp.conformance_level` value choice (`"full"`).
All other values are the §8.2.1 example verbatim.
