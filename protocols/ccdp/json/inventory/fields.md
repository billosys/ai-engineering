# CCDP Field Census

Every JSON field the specification defines, with type, requirement level, and
defining section. Extracted from CCDP draft v0.2 (document version 0.2.0).

Requirement codes follow §7.3.8: **R** = REQUIRED, **S** = RECOMMENDED
(SHOULD), **O** = OPTIONAL, **C** = conditional, **—** = not applicable.
Message-type columns: REQ = REQUEST, RSP = RESPONSE, ESC = ESCALATION,
NOT = NOTIFICATION, HRQ = HEALTH_REQUEST, HRS = HEALTH_RESPONSE,
DEC = DECOMPOSITION_RESULT.

Fields marked **[prose-only]** are defined in prose (or a table) but appear in
no JSON example anywhere in the spec — extraction findings, cross-referenced
to FINDINGS.md. Fields marked **[example-only]** appear in examples but are
never defined in prose.

## 1. JSON-RPC wire wrapper (§7.1, §7.2)

| Field | Type | Requirement | Defining section |
|---|---|---|---|
| `jsonrpc` | string `"2.0"` | R on every message | §7.1 |
| `method` | string (`ccdp/request`, `ccdp/escalation`, `ccdp/health.request`, `ccdp/decomposition.result`, `ccdp/notification`) | R on method-bearing messages; absent on RESPONSE/HEALTH_RESPONSE | §7.1, §7.2 |
| `id` | string; MUST equal `envelope.request_id` | R except NOTIFICATION (no `id`) | §7.1, §7.2 |
| `params` | object `{envelope, content}` | R on method-bearing messages | §7.1 |
| `result` | object `{envelope, content}` | R on JSON-RPC responses | §7.1 |
| `error` | object (JSON-RPC error) | on error responses | §13.2 |

## 2. Envelope — common fields (§7.3.1; matrix §7.3.8)

| Field | Type | REQ | RSP | ESC | NOT | HRQ | HRS | DEC | Defining section |
|---|---|---|---|---|---|---|---|---|---|
| `ccdp_version` | string (`"1.0"`) | R | R | R | R | R | R | R | §7.3.1, §2.1 |
| `type` | string enum (7 values) | R | R | R | R | R | R | R | §7.3.1 |
| `request_id` | string UUID v4 | R | R | R | R | R | R | R | §7.3.1 |
| `trace_id` | string, 32-char lowercase hex | R | R | R | R | R | R | R | §7.3.1, §2.3 |
| `span_id` | string, 16-char lowercase hex | R | R | R | R | R | R | R | §7.3.1, §2.3 |
| `timestamp` | string ISO 8601 UTC `Z` | R | R | R | R | R | R | R | §7.3.1 |
| `source_id` | string | R | R | R | R | R | R | R | §7.3.1 |
| `metadata` | object (may be empty; unknown keys preserved) | R | R | R | R | R | R | R | §7.3.1, §7.7 — **absent from the §7.3.8 matrix (F-02)** |

## 3. Envelope — per-message-type fields

Requirement letters from the §7.3.8 matrix (normative, takes precedence);
divergences from prose are flagged.

| Field | Type | REQ | RSP | ESC | NOT | HRQ | HRS | DEC | Defining section |
|---|---|---|---|---|---|---|---|---|---|
| `capability_type` | string, reverse-domain | R | S | S | O | — | — | R | §7.3.2; **RSP/ESC/NOT/DEC appearances defined only by the matrix, never in those types' prose (F-04)** |
| `destination_id` | string or null | O | — | O | R | R | — | — | §7.3.2 (REQ), §7.3.5 (NOT), §7.3.6 (HRQ) |
| `parent_span_id` | string or null | O | — | — | — | — | — | — | §7.3.2 — **absent from matrix (F-02)** |
| `deadline` | string ISO 8601 | R | — | O | — | — | — | O | §7.3.2; matrix §7.3.8 |
| `remaining_budget_ms` | integer | R (prose) | — | — | — | — | — | — | §7.3.2, §12.4.1 — **absent from matrix (F-02)** |
| `cost_budget` | object | O | — | O | — | — | — | O | §7.3.2, §12.2.1 |
| `provenance_requirement` | object | O | — | O | — | — | — | — | §7.3.2 |
| `priority` | string enum (4) | O | — | O | — | — | — | — | §7.3.2 |
| `idempotency_key` | string or null | O | — | — | — | — | — | — | §7.3.2 — **absent from matrix (F-02)** |
| `status` | string (`SUCCESS`/`PARTIAL`/`ERROR`) | — | R (prose) | ambiguous | — | — | — | — | §7.3.3 — **absent from matrix (F-02); ESCALATION inheritance ambiguous (F-05)** |
| `provenance` | object | — | R | R\* | — | — | — | R | §7.3.3, §7.3.8 (\* R when partial results carried; omissible for pure routing failures → implicit OPAQUE) |
| `escalation` | object | — | — | R (prose) | — | — | — | — | §7.3.4 — **absent from matrix (F-02)** |
| `notification_type` | string | — | — | — | R (prose) | — | — | — | §7.3.5 — **absent from matrix (F-02)** |
| `health` | object | — | — | — | — | — | R (prose) | — | §7.3.6 — **absent from matrix (F-02)** |
| `audit` | object (Dispatcher-written) | on forwarded messages | | | | | | | §7.5 — **absent from matrix (F-02)** |

## 4. `cost_budget` (§7.3.2, §12.2.1)

| Field | Type | Req. | Defining section |
|---|---|---|---|
| `max_compute_seconds` | integer | O | §7.3.2, §12.2.1 |
| `max_tokens` | integer | O | §7.3.2, §12.2.1 |
| `max_monetary_cost` | string decimal (v0.1 alias: `max_monetary_units`) | O | §7.3.2, §2.3 |
| `monetary_unit` | string ISO 4217 | O | §7.3.2 |

## 5. `provenance_requirement` (§7.3.2)

| Field | Type | Req. | Defining section |
|---|---|---|---|
| `min_policy_grade` | integer 0–7 **or** grade name (replaces v0.1 `min_grade`) | O | §7.3.2 |
| `required_methods` | array of strings (Evidence `method` values) | O | §7.3.2 **[prose-only — no example anywhere; F-14]** |
| `required_evidence_types` | array of strings (Evidence `artifact_type` values) | O | §7.3.2 **[prose-only; F-14]** |

## 6. `provenance` object (§7.3.3, §10)

| Field | Type | Req. | Defining section |
|---|---|---|---|
| `grade` | string enum (8) | R | §7.3.3, §10.2 |
| `evidence` | array of Evidence Entries (may be empty) | R | §7.3.3, §4 |
| `scope` | string | O; R at FORMALLY_VERIFIED | §7.3.3, §10.3 rule 3 |
| `service_id` | string | R | §7.3.3 |
| `service_version` | string | R | §7.3.3 |
| `service_mode` | integer 1–4 | O | §7.3.3, §5.3 |
| `computation` | object | O per §7.3.3 — **conflicts with §12.2.3's "Every Response MUST report" (F-08)** | §7.3.3, §12.2.3 |
| `composition_trace` | object or null | O | §7.3.3, §10.5.4 |

### 6.1 `computation` sub-fields

| Field | Type | Defining section |
|---|---|---|
| `tokens_consumed` | integer | §7.3.3 |
| `compute_seconds` | number | §7.3.3 |
| `model_id` | string | §7.3.3 |
| `monetary_cost` | string decimal | §12.2.3 example only ("any additional fields" per §7.3.3) |
| `monetary_unit` | string | §12.2.3 example only |

### 6.2 Evidence Entry (normative schema §4)

| Field | Type | Req. | Defining section |
|---|---|---|---|
| `method` | string (replaces earlier-draft `type`) | R | §4 |
| `description` | string | O | §4 |
| `service_id` | string | R | §4 |
| `artifact_ref` | object | C — MUST at VALIDATED+ when artifact exists; RECOMMENDED below | §4 |
| `verified_by` | string | O | §4 |
| `independence` | string (`"full"`/`"partial"`/`"replicated"`) | MUST for CROSS_CHECKED | §10.2 Grade 5 **[prose-only; not in the §4 normative schema; F-26]** |
| `confidence`, `false_positive_rate` | number | shown inline for HEURISTIC | §10.2 Grade 2 **[prose-only inline snippet; not in the §4 schema; F-26]** |

### 6.3 `artifact_ref` (§4)

| Field | Type | Req. | Defining section |
|---|---|---|---|
| `uri` | string | R | §4 |
| `artifact_type` | string | R | §4 |
| `integrity` | object `{algorithm: string R, digest: string R}` | R at VALIDATED+ | §4 |
| `media_type` | string MIME | O | §4 |
| `access` | string hint | O | §4 |

### 6.4 `composition_trace` (§10.5.4)

| Field | Type | Defining section |
|---|---|---|
| `method` | string (example: `"sequential"`; vocabulary never enumerated — F-20) | §10.5.4 |
| `components[]` | array of `{span_id, service_id, grade, role}` | §10.5.4 |
| `composed_grade` | string grade | §10.5.4 |
| `rule_applied` | string (example: `"weakest_link"`) | §10.5.4 |

## 7. `escalation` object (§7.3.4)

| Field | Type | Req. | Defining section |
|---|---|---|---|
| `reason` | string enum (§13.3, extensible) | R | §7.3.4 |
| `escalation_origin` | `"service"` / `"dispatcher"` | R | §7.3.4 |
| `detail` | string | O | §7.3.4 |
| `achieved_grade` | string grade | O | §7.3.4 |
| `requested_grade` | string grade | O | §7.3.4 |
| `suggested_target` | string (Service ID *or* Capability Type — untyped; F-13) | O | §7.3.4 |
| `partial_result_available` | boolean | R | §7.3.4 |
| `budget_exceeded` | object | R when reason `BUDGET_EXCEEDED` | §12.2.1 — **defined outside §7.3.4's field list (F-09)** |

### 7.1 `budget_exceeded` (§12.2.1)

| Field | Type | Defining section |
|---|---|---|
| `dimension` | `"monetary"` / `"compute_seconds"` / `"tokens"` | §12.2.1 |
| `budget_limit` | string decimal | §12.2.1 |
| `actual_or_estimated` | string decimal | §12.2.1 |
| `is_estimate` | boolean | §12.2.1 |

## 8. `health` object (§7.3.6, §12.3, §13.7)

| Field | Type | Req. | Defining section |
|---|---|---|---|
| `status` | `HEALTHY`/`DEGRADED`/`UNHEALTHY` | R | §7.3.6 |
| `capabilities` | object: capability type → per-capability status | O | §7.3.6 |
| `capabilities.<type>.available` | boolean | — | §7.3.6, §12.3.2 |
| `capabilities.<type>.current_load` | number 0.0–1.0 | — | §7.3.6, §12.3.2 |
| `capabilities.<type>.queue_depth` | integer | — | §7.3.6, §12.3.2 |
| `capabilities.<type>.estimated_latency_ms` | integer | — | §7.3.6, §12.3.2 |
| `capacity` | object | O | §7.3.6 |
| `capacity.max_concurrent_requests` | integer | — | §7.3.6, §12.3.1 |
| `capacity.current_concurrent_requests` | integer | — | §7.3.6, §12.3.1 |
| `capacity.queue_depth` | integer | — | §12.3.1 only |
| `capacity.estimated_drain_time_ms` | integer | — | §12.3.1 only |
| `detail` | string or null | O | §7.3.6 |

## 9. Content wrapper (§7.4)

| Field | Type | Req. | Defining section |
|---|---|---|---|
| `content.type` | string (7 well-known + custom) | R | §7.4 |
| `content.schema_ref` | string `{capability_type}/{direction}/{version}` | O | §7.4 |
| `content.body` | any | R | §7.4 |
| multipart `body.parts[].type` | string | — | §7.4.1 |
| multipart `body.parts[].label` | string | — | §7.4.1 |
| multipart `body.parts[].body` | any | — | §7.4.1 |

## 10. Dispatcher `audit` envelope annotation (§7.5)

| Field | Type | Defining section |
|---|---|---|
| `audit.dispatcher_id` | string | §7.5, §6.2.2 |
| `audit.received_at` | string ISO 8601 | §7.5, §6.2.2 |
| `audit.routed_at` | string ISO 8601 | §7.5, §6.2.2 |
| `audit.routing_decision.selected_service` | string | §7.5, §9.2 Step 7 |
| `audit.routing_decision.reason` | string (open vocabulary; examples §9.2) | §7.5, §9.2 Step 7 |
| `audit.routing_decision.candidates_considered` | integer | §7.5, §9.2 Step 7 |
| `audit.routing_decision.registry_query_ms` | integer | §7.5, §9.2 Step 7 |
| `audit.routing_decision.filters_applied` | array of strings | §9.2 Step 7 **[prose-only; F-14]** |
| `audit.schema_validation.input_valid` | boolean | §7.5 |
| `audit.schema_validation.schema_version` | string | §7.5 |
| `audit.schema_validation` (as string `"permissive"`) | string | §8.4.7 — **type conflict with §7.5's object form (F-11)** |

## 11. Capability Record (§8.2)

See canonical/capability-record.notes.md for the full per-field table (all 24
top-level fields with citations). Summary of requirement levels: R —
`service_id`, `capability_type`, `version`, `endpoint`, `status`,
`input_schema`, `output_schema`, `cost_hints`, `provenance_capabilities`
(`max_grade` R; `typical_grade`, `supported_evidence_methods`,
`supported_artifact_types` O), `health_check`, `isolation`,
`escalation_chain` (may be empty), `registered_at`, `updated_at`. O —
`cacheable` (default false), `max_input_size`, `tags`, `description`,
`metadata`. Escalation-chain entries are typed `{kind, value}` objects;
string-only entries MUST NOT be used (§8.2.2).

## 12. Decomposition Plan (§14.3)

See canonical/decomposition-plan.notes.md for the full table. Top-level:
`plan_id` **[example-only; F-10]**, `description` **[example-only; F-10]**,
`sub_requests[]` (fields §14.3.1), `dependencies` (O, informative, shape
unspecified — F-10), `composition` (§14.3.4), `fallback` (§14.3.5). Typed
result references `{$ref R, path R, fallback O}` (§14.3.3).

## 13. Audit Record (§11)

See canonical/audit-record.notes.md for the full per-field tables (Table 11.1
common fields; Table 11.2 per-message-type fields; §11.2 example
substructures). Fields defined **only** in Table 11.2 / the §11.4 category
table with no definition or example anywhere: `health_summary.status`,
`error_code`, `error_detail`, `retry_count` **[prose-only; F-22]**.

## 14. Error object `data` (§13.2)

| Field | Type | Req. | Defining section |
|---|---|---|---|
| `trace_id` | string | R (every CCDP error) | §13.2 |
| `request_id` | string | R | §13.2 |
| `timestamp` | string ISO 8601 | R | §13.2 |
| `dispatcher_id` | string | example-only | §13.2 example |
| `validation_errors[].{path, message, schema_ref}` | — | `-32010` | §13.2 example |
| `limit_type`, `limit_value`, `actual_value` | — | R on `-32012` | §13.2, §14.6 |
| `retry_after_ms` | integer | R on `-32014` | §13.2 (§7.9 says "`Retry-After`" — F-23) |
| `reason` | string (`"message_too_large"`, `"audit_unavailable"`) | per-code | §7.6, §11.6 |

## 15. Protocol-defined metadata keys (`org.ccdp.*`)

| Key | Type | Defining section |
|---|---|---|
| `org.ccdp.escalation_history` | array of history entries | §13.4.1 |
| — entry `service_id` | string; R when origin `"service"` | §13.4.1 |
| — entry `dispatcher_id` | string; R when origin `"dispatcher"` | §13.4.1 |
| — entry `responding_service_id` | string; R for post-receipt mismatch, MUST be absent for no-candidate | §13.4.1 |
| — entry `reason` | string; R | §13.4.1 |
| — entry `escalation_origin` | string; R | §13.4.1 |
| — entry `achieved_grade`, `detail` | O | §13.4.1 |
| — entry `timestamp` | string; R | §13.4.1 |
| `org.ccdp.partial_results` | array of `{service_id, provenance, content}` | §13.4.1, §7.3.4 |
| `org.ccdp.signature` | object `{algorithm, key_id, profile, signed_fields, value, timestamp}` | §15.4.2, §15.4.4 |
| `org.ccdp.allow_schema_version_fallback` | boolean, default false | §13.5.2 |
| `org.ccdp.audit_gap` | boolean (`degrade` mode only — non-conformant) | §11.6 |
| `org.ccdp.conformance_level` | `"core"` / `"full"` (Registry metadata) | §16.4 |
| `org.ccdp.request.*` / `org.ccdp.response.*` prefixes | directional key classes | §7.7 |
| `org.ccdp.dispatcher.*` prefix | Dispatcher-mutable keys excluded from signing | §15.4.4 |
| `org.ccdp.forwarder_id` | named only as a hypothetical future extension | §7.3.1 **[not a defined field]** |

## 16. Informative/non-wire structures with JSON shape

| Structure | Fields | Defining section |
|---|---|---|
| Bearer-token scope claims (format-agnostic; example shape) | `sub`, `scope` (array, wildcards allowed), `max_priority`, `max_cost_usd` (number — violates §2.3 string-monetary convention; F-27), `exp` | §15.3.2 |
| Registry Lookup inputs | `capability_type`, `status_filter`, `min_provenance_grade` (≠ `min_policy_grade`; F-19), `max_cost`, `tags` | §8.4.2 |
| List Schema Versions output entries | `{version, compatibility, registered_at}` | §8.4.5 |
| Deployment policies (config, not wire) | `all_unhealthy_policy`, `queue_timeout_ms`, `provenance_mismatch_policy`, `provenance_unavailable_policy`, `audit_failure_policy`, circuit-breaker params (`failure_threshold`, `failure_window_seconds`, `recovery_probe_interval_seconds`, `half_open_request_limit`) | §9.2, §11.6, §13.6.3 |
