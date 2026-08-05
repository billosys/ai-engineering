# CCDP Closed Vocabularies (Enums)

Every closed (or nominally closed) value set in CCDP draft v0.2 (document
version 0.2.0), with citations. Sets marked **open** admit
implementation-defined extensions (usually via reverse-domain notation).
Sets marked **unenumerated** are used by the spec without a defining value
list — extraction findings.

## 1. Message types (§7.2, §7.3.1) — closed (7)

`REQUEST`, `RESPONSE`, `NOTIFICATION`, `ESCALATION`, `HEALTH_REQUEST`,
`HEALTH_RESPONSE`, `DECOMPOSITION_RESULT`. Unrecognized `type` → reject with
`-32600` (§7.7).

## 2. JSON-RPC methods (§7.2) — closed (5)

`ccdp/request`, `ccdp/escalation`, `ccdp/health.request`,
`ccdp/decomposition.result`, `ccdp/notification`. (RESPONSE and
HEALTH_RESPONSE have no method — JSON-RPC responses.)

## 3. Provenance grades (§10.2, §10.4) — closed (8, ordered 0–7)

| # | Grade |
|---|---|
| 0 | `OPAQUE` |
| 1 | `ASSERTED` |
| 2 | `HEURISTIC` |
| 3 | `COMPUTED` |
| 4 | `VALIDATED` |
| 5 | `CROSS_CHECKED` |
| 6 | `FORMALLY_VERIFIED` |
| 7 | `HUMAN_ATTESTED` |

Policy order, not universal epistemic hierarchy (§10.2.1). Integer codes MAY
be used programmatically (§10.4); `min_policy_grade` and
`provenance_capabilities.max_grade`/`typical_grade` accept integer **or**
name (§7.3.2, §8.2.2). Earlier-draft names `GENERATED`, `CITED` superseded
(§18.2). Adding grades requires a document version increment (§6.3).

## 4. Response `status` (§7.3.3) — closed (3)

`SUCCESS`, `PARTIAL`, `ERROR`.

## 5. `priority` (§7.3.2, §4) — closed (4)

`LOW`, `NORMAL` (default), `HIGH`, `CRITICAL`.

## 6. Escalation reasons (§13.3) — open (9 defined)

`PROVENANCE_BELOW_REQUIREMENT` (renamed from v0.1
`CONFIDENCE_BELOW_THRESHOLD`, §21.1.9), `CAPABILITY_EXCEEDED`,
`DEADLINE_INSUFFICIENT`, `DEADLINE_APPROACHING`, `BUDGET_EXCEEDED`,
`SEARCH_EXHAUSTED`, `AMBIGUOUS_INPUT`, `INTERNAL_DEGRADATION`,
`REQUIRES_HUMAN`. Extensions use reverse-domain notation (§13.3).

## 7. `escalation_origin` (§7.3.4) — closed (2)

`service`, `dispatcher`.

## 8. Error codes (§13.2) — closed table

| Code | Name |
|---|---|
| `-32700` | Parse error (JSON-RPC standard) |
| `-32600` | Invalid request |
| `-32601` | Method not found |
| `-32602` | Invalid params |
| `-32603` | Internal error |
| `-32001` | Service unavailable |
| `-32002` | No service for capability |
| `-32003` | All services unhealthy |
| `-32004` | Deadline not achievable |
| `-32005` | Provenance not achievable (§9.2 phrases it "provenance requirement not satisfiable" — F-23) |
| `-32006` | Escalation chain exhausted |
| `-32007` | Deadline exceeded |
| `-32008` | Authentication failed |
| `-32009` | Authorization denied |
| `-32010` | Schema validation failed |
| `-32011` | Replay detected |
| `-32012` | Decomposition limit exceeded |
| `-32014` | Rate limited |

`-32013` is skipped without comment (F-24). Every CCDP error's `data` MUST
include `trace_id`, `request_id`, `timestamp` (§13.2).

### 8.1 `-32012 data.limit_type` — closed (3)

`depth`, `width`, `total_nodes` (§13.2, §14.6).

### 8.2 `data.reason` values — unenumerated

`"message_too_large"` (§7.6), `"audit_unavailable"` (§11.6). No general
vocabulary defined.

## 9. HTTP status mapping (§7.9) — closed table

200, 400 (→`-32700`), 401, 403 (→`-32009`), 413, 429 (→`-32014`), 500
(→`-32603`).

## 10. Content types (§7.4) — open (7 well-known)

`natural-language`, `formal-logic`, `proof-object`, `validated-plan`,
`structured-data`, `code`, `multipart`. Custom types via Capability Records,
reverse-domain notation. **Note:** §6.2.4's parallel list omits `code` and
`multipart` (F-28).

## 11. Well-known capability types (§8.3) — open (13 defined)

`org.ccdp.deduction`, `org.ccdp.planning`, `org.ccdp.language.generation`,
`org.ccdp.language.translation`, `org.ccdp.language.analysis`,
`org.ccdp.verification`, `org.ccdp.selection`, `org.ccdp.retrieval`,
`org.ccdp.decomposition`, `org.ccdp.human_review`, `org.ccdp.code.generation`,
`org.ccdp.code.execution`, `org.ccdp.composition`.
**`org.ccdp.notification` is used in the §7.3.5 example but is not in this
table (F-12).** Wildcards (`org.ccdp.language.*`) are valid only in token
scopes and routing configuration, never in Capability Records or Registry
lookups (§9.7, §15.3.2).

## 12. Health status (§7.3.6, §4) — closed (3)

`HEALTHY`, `DEGRADED`, `UNHEALTHY`.

## 13. Capability Record `status` (§8.2.2) — closed (4)

`ACTIVE`, `DRAINING`, `INACTIVE`, `DEPRECATED`.

## 14. Notification types (§7.3.5) — open (3 well-known)

`STATUS_UPDATE`, `RESOURCE_ALERT`, `HEALTH_CHANGE`.

## 15. Service modes (§5.3) — closed (4)

1 = LLM alone, 2 = deterministic service alone, 3 = LLM + deterministic
composite, 4 = human queue. Carried as integer `provenance.service_mode`
(§7.3.3).

## 16. Evidence methods (§4 `method`) — open (examples)

`formal_verification`, `human_review`, `independent_cross_check`,
`statistical_testing`, `computed` (§4); `method_selection` (§10.3 rule 7).

## 17. Evidence artifact types (§4 `artifact_type`) — open (examples)

`proof_certificate`, `signed_attestation`, `test_report`, `counterexample`,
`review_record`.

## 18. Artifact `access` hints (§4) — open (examples)

`audit-archive`, `inline`, `external-url`.

## 19. Evidence `independence` (§10.2 Grade 5) — closed (3)

`full`, `partial`, `replicated` (replicated does NOT qualify for
CROSS_CHECKED). Defined in prose only; not in the §4 schema (F-26).

## 20. Escalation-chain entry `kind` (§8.2.2) — closed (2)

`service_id`, `capability_type`.

## 21. Composition vocabularies (§14.3.4, §14.3.5)

| Set | Values | Status |
|---|---|---|
| `composition.method` | `template`, `concatenation`, `selection`, `custom` | closed (4) |
| `selection` criteria | `highest_provenance`, `lowest_cost`, `first_completed` | closed (3); others require `org.ccdp.composition` routing |
| `provenance_rule` | `weakest_link` (default), `cross_check`, `explicit` | closed (3) |
| `fallback.on_sub_failure` | `escalate_parent`, `skip_and_compose`, `retry_alternative` | closed (3) |
| `fallback.on_composition_failure` | `return_partial`, `escalate_parent` | closed (2) |

## 22. `composition_trace.method` (§10.5.4) — unenumerated

Example shows `"sequential"`; §10.5 implies sequential / parallel /
decomposition, but no value list is defined (F-20).

## 23. Signing vocabularies (§15.4.2, §15.4.4)

| Set | Values | Status |
|---|---|---|
| `signature.profile` | `requester-outbound`, `service-response` | closed (2) |
| `signature.signed_fields` values | `envelope`, `content` | closed (2) |
| `signature.algorithm` | example `Ed25519` | unenumerated/open |

## 24. Circuit breaker states (§9.6, §13.6.2) — closed (3)

`CLOSED`, `OPEN`, `HALF_OPEN`. (Dispatcher-internal, not wire values.)

## 25. Conformance levels (§16.4) — closed (2)

`core`, `full` (lowercase, in `org.ccdp.conformance_level`). Requirement ID
namespaces: `DISP-CORE-NNN` (001–033), `DISP-FULL-NNN` (001–008),
`DISP-OPT-NNN` (001–006) (§16.1); Service/Registry stable IDs deferred (§18).

## 26. Deployment policy vocabularies (config-level, not wire) — closed

| Policy | Values | Defining section |
|---|---|---|
| `all_unhealthy_policy` | `error` (default), `escalate`, `queue` | §9.2 Step 3 |
| `provenance_mismatch_policy` | `reroute` (default), `escalate` | §9.2 Step 5 |
| `provenance_unavailable_policy` | `error` (default), `escalate` | §9.2 Step 5 |
| `audit_failure_policy` | `fail_closed` (recommended), `buffer`, `degrade` (non-conformant) | §11.6 |

## 27. Audit-record vocabularies (§11)

| Set | Values | Status |
|---|---|---|
| `provenance_policy.policy_field` | `provenance_mismatch_policy`, `provenance_unavailable_policy` | closed (2), from §11.2.2–11.2.3 examples + §9.2 |
| `provenance_policy.selected_action` | `escalate`, `reroute`, `error` | closed (3), Table 11.3 |
| `provenance_policy.trigger` | `grade_below_requirement`, `no_candidate_meets_requirement` | **unenumerated — example values only (F-14)** |
| `escalation_routing.chain_source` | `responding_service`, `human_review` | closed (2), §11.4 |
| `routing.registry_source` | `live` (example); §8.6 implies cached/static-fallback values | **unenumerated (F-14)** |
| `routing.decision` / `routing_decision.reason` | examples: `lowest_cost_healthy`, `only_candidate`, `explicit_destination`, `error`, `queued` | open |
| queued-request audit status | `queued` | §9.2 Step 3 |
| Registry compatibility record | auto-verified vs operator-attested | §8.5.3 (values unenumerated — F-25) |

## 28. Wire constants

| Constant | Value | Defining section |
|---|---|---|
| `ccdp_version` | `"1.0"` | §2.1, §7.3.1 |
| `audit_schema_version` | `"1.0"` | §11.1 |
| Content-Type | `application/json`; charset UTF-8 | §2.3 |
| `traceparent` format | `00-{trace_id}-{span_id}-{trace_flags}` | §11.3 |
| `tracestate` entry | `ccdp=<dispatcher_id>`; 512-byte truncation rule | §11.3 |
| Minimum message size support | 16 MiB MUST / 64 MiB SHOULD | §7.6 |
