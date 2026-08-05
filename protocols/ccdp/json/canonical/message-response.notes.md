# message-response.json — field citations and derivation notes

Maximal RESPONSE as a JSON-RPC 2.0 response (no `method`; `envelope.type` is
the sole CCDP type identifier — §7.2). Scenario chosen for coherence: a Mode 3
verification service whose grade composes translation (VALIDATED) with formal
verification (FORMALLY_VERIFIED) via the §10.5.1 verified-translation
exception, so `composition_trace`, LLM `computation` fields, and full evidence
entries can coexist on one valid instance.

## Wire wrapper

| Field | Requirement | Defining section |
|---|---|---|
| `jsonrpc`, `id`, `result.{envelope,content}` | RESPONSE carried in JSON-RPC `result` | §7.1, §7.2 |
| `id` matches `envelope.request_id` | MUST | §7.1 |

## Envelope

| Field | Req. | Defining section |
|---|---|---|
| common fields | R | §7.3.1 (see message-request.notes.md) |
| `capability_type` | S on RESPONSE per matrix §7.3.8 — **never defined in §7.3.3 prose; F-04** | §7.3.8 |
| `request_id` (= Request's) | R | §7.3.3 |
| `status` | R (`SUCCESS`/`PARTIAL`/`ERROR`) | §7.3.3 — **absent from matrix; F-02** |
| `provenance` | R | §7.3.3, §7.3.8 |

## Provenance object (§7.3.3, §10)

| Field | Req. | Defining section |
|---|---|---|
| `grade` | R | §7.3.3, §10.2 |
| `evidence[]` | R (may be empty) | §7.3.3; entry schema normative in §4 |
| `evidence[].method` | R | §4 |
| `evidence[].description` | O | §4 |
| `evidence[].service_id` | R | §4 |
| `evidence[].artifact_ref` | CONDITIONAL (MUST at VALIDATED+ when artifact exists) | §4 |
| `artifact_ref.uri` | R | §4 |
| `artifact_ref.artifact_type` | R | §4 |
| `artifact_ref.integrity.{algorithm,digest}` | R at VALIDATED+ | §4 |
| `artifact_ref.media_type` | O | §4 |
| `artifact_ref.access` | O | §4 |
| `evidence[].verified_by` | O | §4 |
| `method_selection` meta-evidence entry | SHOULD | §10.3 rule 7 |
| `scope` | O; R when grade FORMALLY_VERIFIED | §7.3.3, §10.3 rule 3 |
| `service_id` | R | §7.3.3 |
| `service_version` | R | §7.3.3 |
| `service_mode` | O (1–4) | §7.3.3, §5.3 |
| `computation.{tokens_consumed, compute_seconds, model_id}` | O per §7.3.3 — **but §12.2.3 says every Response MUST report consumption; conflict F-08** | §7.3.3, §12.2.3 |
| `computation.{monetary_cost, monetary_unit}` | shown only in §12.2.3's example ("any additional fields" per §7.3.3) | §12.2.3 |
| `composition_trace` | O (object or null) | §7.3.3, §10.5.4 |
| `composition_trace.{method, components[], composed_grade, rule_applied}` | — | §10.5.4 (component fields `span_id`, `service_id`, `grade`, `role`); `method` vocabulary never enumerated — F-20 |

## Metadata / audit

| Field | Defining section |
|---|---|
| `org.ccdp.signature` (service-response profile; `signed_fields` MUST include both components at FORMALLY_VERIFIED/HUMAN_ATTESTED, shown here as the RECOMMENDED practice for other grades) | §15.4.2, §15.4.4 |
| `audit.{dispatcher_id, received_at, routed_at}` | §7.5 ("when the Dispatcher forwards a message" — response-side annotation shape is not separately specified; F-18) |

## Content

Multipart content per §7.4.1 (`parts[].{type,label,body}`); `schema_ref` per §7.4.

## Derived (invented) values

`schema_ref` value for verification output, Verus evidence entry and
`verified_by` values, second evidence entry's `media_type`/`access`/`verified_by`
(spec's §7.3.3 example omits them), `method_selection` entry text, signature
`key_id`/`value`, `capability_type` value, `service_version` reuse of 2.3.1.
IDs, timestamps, digests, computation figures, composition-trace span/service
IDs reuse spec example values (§7.3.3, §10.5.4, §12.2.3).
