# message-health-request.json — field citations and derivation notes

Maximal HEALTH_REQUEST as a JSON-RPC 2.0 request (`method:
"ccdp/health.request"` — §7.2, §13.6.1). A HEALTH_REQUEST always targets a
specific Service; `destination_id` is REQUIRED (§7.3.6, §7.3.8).

| Field | Req. | Defining section |
|---|---|---|
| common fields | R | §7.3.1 |
| `destination_id` | R | §7.3.6, §7.3.8 |

**Content omitted deliberately.** §4 ("a Message consists of an Envelope and
a Content payload") and §7.1 (`params: {envelope, content}`) imply Content on
every message, but the spec never defines any Content for health messages —
health data travels in the *envelope* (`envelope.health`, §7.3.6). Rather than
invent a placeholder Content, this instance omits it; logged as FINDINGS F-06.

Derived values: `request_id`/`id` UUID, `span_id`, timestamp, `source_id`
(the Dispatcher probes health, §13.6.1). `destination_id` reuses the §7.3.6
example value.
