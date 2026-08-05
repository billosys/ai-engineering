# message-notification.json — field citations and derivation notes

Maximal NOTIFICATION as a JSON-RPC 2.0 *notification* — `method` + `params`,
**no `id`**, no response expected (§7.2). The `id`-must-match-`request_id`
rule does not apply (§7.3.1); `request_id` here carries the identifier of the
related request whose progress is reported (§7.3.1).

| Field | Req. | Defining section |
|---|---|---|
| common fields | R | §7.3.1 |
| `capability_type` | O per matrix §7.3.8; value `"org.ccdp.notification"` copied from the §7.3.5 example — **this capability type is not in the §8.3 well-known table; F-12** | §7.3.5 example |
| `notification_type` | R (`STATUS_UPDATE` / `RESOURCE_ALERT` / `HEALTH_CHANGE` well-known; open set) | §7.3.5 |
| `destination_id` | R | §7.3.5, §7.3.8 |

Content: no schema for notification content is defined anywhere in the spec;
`structured-data` body here is derived (invented) — flagged. `span_id`
value, timestamp, and progress body are derived; other identifiers reuse spec
example values.
