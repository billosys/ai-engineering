# message-decomposition-result.json — field citations and derivation notes

Maximal DECOMPOSITION_RESULT as a JSON-RPC 2.0 *request*
(`method: "ccdp/decomposition.result"` — §7.2), sent Decomposition Service →
Dispatcher. Content is the canonical Decomposition Plan
(decomposition-plan.json, embedded structurally identically — same keys,
same order, same values; only indentation depth differs).

| Field | Req. | Defining section |
|---|---|---|
| common fields | R | §7.3.1 |
| `request_id` | R (correlates to the decomposed Request) | §7.3.7 |
| `capability_type` | R per matrix (`org.ccdp.decomposition`) | §7.3.8, §8.3 |
| `deadline` | O per matrix | §7.3.8 — not mentioned in §7.3.7 prose |
| `cost_budget` | O per matrix | §7.3.8 — not mentioned in §7.3.7 prose |
| `provenance` | R — the decomposition's own grade participates in composed provenance | §7.3.7, §7.3.8, §10.5.3, §14.5 |
| (`priority`, `provenance_requirement`) | — carried by neither, per the §7.3.8 footnote | §7.3.8 |

Provenance scenario: Mode 3 decomposition (LLM proposes, validator checks —
§5.4, §14.5), graded VALIDATED with a plan-checker evidence entry.

**Reply semantics gap.** §7.2 encodes DECOMPOSITION_RESULT as a method-bearing
JSON-RPC request with an `id`, implying a JSON-RPC response is due, but the
spec never says what answers it — nor how this message relates to the RESPONSE
the Decomposition Service owes for the routed decomposition REQUEST. Logged as
FINDINGS F-07.

## Derived (invented) values

`span_id`, timestamp, `source_id`/`service_id` "decomposer-01",
`service_version`, evidence entry (method `"computed"` from the §4 examples
list), artifact URI/digest, computation figures. `request_id`, `trace_id`,
deadline, and cost_budget reuse spec example values.
