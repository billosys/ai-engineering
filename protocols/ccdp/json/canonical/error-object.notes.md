# error-object.json — field citations and derivation notes

Maximal CCDP error as a JSON-RPC 2.0 error response, using code `-32010`
(the spec's own worked example, §13.2, reproduced with no changes — it is
already maximal for that code).

| Field | Req. | Defining section |
|---|---|---|
| `error.code` | R | §13.2 (code table); JSON-RPC 2.0 |
| `error.message` | R | §13.2; JSON-RPC 2.0 |
| `error.data.trace_id` | R for every CCDP error code | §13.2 |
| `error.data.request_id` | R | §13.2 |
| `error.data.timestamp` | R (ISO 8601) | §13.2 |
| `error.data.dispatcher_id` | shown in the §13.2 example; not in the required minimum | §13.2 example |
| `error.data.validation_errors[].{path, message, schema_ref}` | code `-32010` detail | §13.2 example |

## Per-code `data` extensions (not representable on one instance)

| Code | Extra `data` fields | Defining section |
|---|---|---|
| `-32012` | `limit_type` (`"depth"`/`"width"`/`"total_nodes"`), `limit_value`, `actual_value` | §13.2, §14.6 |
| `-32014` | `retry_after_ms` (integer) — §7.9 instead says "`Retry-After` in error `data`"; naming inconsistency, F-23 | §13.2, §12.5.2 |
| `-32602` | `data.reason: "message_too_large"` (oversize-but-parseable case) | §7.6 |
| `-32603` | `data.reason: "audit_unavailable"` (audit-store failure, fail_closed) | §11.6 |

The full error-code table (standard JSON-RPC `-32700`…`-32603` plus CCDP
`-32001`…`-32012`, `-32014` — note `-32013` is skipped, F-24) is captured in
inventory/enums.md. HTTP status mapping: §7.9.

Derived values: none — this is the §13.2 example verbatim.
