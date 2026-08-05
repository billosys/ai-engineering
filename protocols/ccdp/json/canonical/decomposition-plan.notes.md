# decomposition-plan.json — field citations and derivation notes

Maximal Decomposition Plan, presented as the Content of a DECOMPOSITION_RESULT
message (§14.3: "A Decomposition Plan is the Content of a DECOMPOSITION_RESULT
message"). Based on the §14.3 example, completed with every defined field.

## Plan body

| Field | Req. | Defining section |
|---|---|---|
| `plan_id` | **example-only — never defined in prose; F-10** | §14.3 example |
| `description` (plan-level) | **example-only; F-10** | §14.3 example |
| `sub_requests[]` | — (the plan's core; also named in §6.2.3) | §14.3, §14.3.1 |
| `sub_requests[].sub_id` | R | §14.3.1 |
| `sub_requests[].capability_type` | R | §14.3.1 |
| `sub_requests[].description` | O | §14.3.1 |
| `sub_requests[].content` | R | §14.3.1 |
| `sub_requests[].constraints.deadline_fraction` | O (0.0–1.0) | §14.3.1, §12.2.2 |
| `sub_requests[].constraints.cost_fraction` | O | §14.3.1, §12.2.2 |
| `sub_requests[].constraints.provenance_requirement` | O | §14.3.1 |
| `sub_requests[].depends_on` | R (empty array = no dependencies; authoritative for the DAG) | §14.3.1, §14.3.2 |
| `dependencies` (top-level) | O, informative only; ignored on conflict with `depends_on` — shape not specified, rendered here as a sub_id → depends-on map (derived; F-10) | §14.3.2 (named as a field in §6.2.3) |
| `composition.method` | R (`template`/`concatenation`/`selection`/`custom`) | §14.3.4 |
| `composition.template` | R when method `template`; `parts[].{label, source}` — **`source` is a bare `"sub-001.result"` string, unlike the typed `$ref` objects §14.3.3 requires for result references; F-15** | §14.3.4, §14.3 example |
| `composition.provenance_rule` | R (`weakest_link`/`cross_check`/`explicit`) | §14.3.4 |
| `fallback.on_sub_failure` | R (`escalate_parent`/`skip_and_compose`/`retry_alternative`) | §14.3.5 |
| `fallback.on_composition_failure` | R (`return_partial`/`escalate_parent`) | §14.3.5 |

## Typed result references (§14.3.3)

| Field | Req. | Defining section |
|---|---|---|
| `$ref` | R (`{sub_id}.result`) | §14.3.3 |
| `path` | R (RFC 6901 JSON Pointer, relative to the referenced Response `content`) | §14.3.3 |
| `fallback` | O | §14.3.3 |

## Derived (invented) values

The `fallback: null` members on both `$ref` objects (the §14.3 example omits
them; shape from §14.3.3), the `dependencies` map rendering, and
`composition.method` selection-criteria alternatives (documented in
inventory/enums.md, not instantiable simultaneously). Everything else is the
§14.3 example verbatim, including its deliberate `"return_partial"` choice.
Plan validation limits (depth 5, width 50, total nodes 100 — RECOMMENDED
defaults) are Dispatcher-side configuration, not plan fields (§14.6).
