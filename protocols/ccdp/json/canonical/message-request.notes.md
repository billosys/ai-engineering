# message-request.json — field citations and derivation notes

Maximal REQUEST as a JSON-RPC 2.0 request, shown *after* Dispatcher annotation
(i.e., as forwarded to a Service), so the Dispatcher-written `audit` block and
Dispatcher-accumulated escalation metadata can be shown on one instance.

## Wire wrapper

| Field | Requirement | Defining section |
|---|---|---|
| `jsonrpc` | `"2.0"` fixed | §7.1 |
| `method` | `"ccdp/request"` | §7.1, §7.2 |
| `id` | MUST match `envelope.request_id` | §7.1 |
| `params.envelope`, `params.content` | carrier of CCDP data for method-bearing messages | §7.1 |

## Envelope — common fields (§7.3.1; matrix §7.3.8)

| Field | Req. | Defining section |
|---|---|---|
| `ccdp_version` | R | §7.3.1 (value `"1.0"` per §2.1) |
| `type` | R | §7.3.1 |
| `request_id` | R | §7.3.1 |
| `trace_id` | R | §7.3.1 (format §2.3, §11.3) |
| `span_id` | R | §7.3.1 (format §2.3, §11.3) |
| `timestamp` | R | §7.3.1 |
| `source_id` | R | §7.3.1 |
| `metadata` | R (may be empty) | §7.3.1, §7.7 — **absent from the §7.3.8 matrix; see FINDINGS F-02** |

## Envelope — REQUEST fields (§7.3.2; matrix §7.3.8)

| Field | Req. | Defining section |
|---|---|---|
| `capability_type` | R | §7.3.2 |
| `destination_id` | O (null → Dispatcher selects) | §7.3.2 |
| `parent_span_id` | O (null for top-level; sub-request usage §14.4 step 3) | §7.3.2 — **absent from matrix; F-02** |
| `deadline` | R | §7.3.2 |
| `remaining_budget_ms` | R | §7.3.2, §12.4.1 — **absent from matrix; F-02** |
| `cost_budget` (+4 sub-fields) | O; all sub-fields optional | §7.3.2, §12.2.1 (monetary strings §2.3) |
| `provenance_requirement.min_policy_grade` | O | §7.3.2 |
| `provenance_requirement.required_methods` | O | §7.3.2 — **prose-only: no example anywhere in spec; F-14** |
| `provenance_requirement.required_evidence_types` | O | §7.3.2 — **prose-only; F-14** |
| `priority` | O (default `"NORMAL"`) | §7.3.2 |
| `idempotency_key` | O | §7.3.2 — **absent from matrix; F-02** |

## Metadata keys shown

| Key | Defining section |
|---|---|
| `com.example.custom_field` | §7.3.1 / §7.7 (namespacing convention) |
| `org.ccdp.allow_schema_version_fallback` | §13.5.2 (default false) |
| `org.ccdp.signature` (object: `algorithm`, `key_id`, `profile`, `signed_fields`, `value`, `timestamp`) | §15.4.2 (structure), §15.4.4 (`"requester-outbound"` profile). **Placement of the requester-outbound signature in metadata is inferred from §15.4.2's service-response example — the spec never shows a requester-signed message; F-17** |
| `org.ccdp.escalation_history[]` (`service_id` / `dispatcher_id` + `responding_service_id`, `reason`, `escalation_origin`, `achieved_grade`, `detail`, `timestamp`) | §13.4.1 |
| `org.ccdp.partial_results[]` (`service_id`, `provenance`, `content`) | §13.4.1, §7.3.4 |

Coherence caveat: a requester-outbound signature covers `metadata` (only
`audit`, `remaining_budget_ms`, conditional `destination_id`, and
`org.ccdp.dispatcher.*` keys are excluded, §15.4.4), yet §13.4.1 has the
Dispatcher append `org.ccdp.escalation_history` / `org.ccdp.partial_results`
to Request metadata — which would invalidate the signature. Logged as
FINDINGS F-16; both are shown here because both are spec-defined.

## Dispatcher audit annotation

| Field | Defining section |
|---|---|
| `audit.dispatcher_id`, `received_at`, `routed_at` | §7.5 (Layer-2 audit fields §6.2.2) |
| `audit.routing_decision.{selected_service, reason, candidates_considered, registry_query_ms}` | §7.5, §9.2 Step 7 (Step 7 also names `filters_applied`) |
| `audit.schema_validation.{input_valid, schema_version}` | §7.5 (cf. §8.4.7 `"permissive"` string form — F-11) |

## Content (§7.4)

`content.type` (R), `content.schema_ref` (O, format `{capability_type}/{direction}/{version}`), `content.body` (R) — §7.4.
Body fields follow the §8.2.1 example `input_schema` for `org.ccdp.deduction`.

## Derived (invented) values

`idempotency_key` value, SMT formula text, partial-result body text, signature
`key_id`/`value`, escalation-history timestamps at :05/:35. All identifiers,
trace/span IDs, and timestamps otherwise reuse the spec's own example values.
