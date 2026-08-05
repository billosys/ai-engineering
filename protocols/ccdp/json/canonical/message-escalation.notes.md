# message-escalation.json — field citations and derivation notes

Maximal Service-originated ESCALATION as a JSON-RPC 2.0 *request*
(`method: "ccdp/escalation"` — §7.2). Scenario: reason
`PROVENANCE_BELOW_REQUIREMENT` with a partial result, so `provenance` is
REQUIRED (§7.3.8 footnote) and every escalation-object field is coherently
present.

## Envelope

| Field | Req. | Defining section |
|---|---|---|
| common fields | R | §7.3.1 |
| `capability_type` | S per matrix | §7.3.8 — **not defined in §7.3.4 prose; F-04** |
| `destination_id` | O per matrix | §7.3.8 — not defined in §7.3.4 prose |
| `priority` | O per matrix | §7.3.8 — not defined in §7.3.4 prose |
| `provenance_requirement` | O per matrix | §7.3.8 (interpreted as the unmet requirement carried forward) |
| `cost_budget` | O per matrix | §7.3.8 |
| `deadline` | O per matrix | §7.3.8 |
| `request_id` (of escalated Request) | R | §7.3.4 |
| `status` | **ambiguous** — §7.3.4 says ESCALATION "shares the RESPONSE envelope structure", which would include `status` (R on RESPONSE), but no escalation example carries it and the matrix omits it; excluded here. F-05 | §7.3.4 vs §7.3.3/§7.3.8 |

## Escalation object (§7.3.4)

| Field | Req. | Defining section |
|---|---|---|
| `escalation.reason` | R | §7.3.4; vocabulary §13.3 |
| `escalation.escalation_origin` | R (`"service"` / `"dispatcher"`) | §7.3.4 |
| `escalation.detail` | O | §7.3.4 |
| `escalation.achieved_grade` | O | §7.3.4 |
| `escalation.requested_grade` | O | §7.3.4 |
| `escalation.suggested_target` | O — a bare string that may be a Service ID *or* a Capability Type (untyped, unlike `escalation_chain` entries; F-13) | §7.3.4, §9.4 |
| `escalation.partial_result_available` | R | §7.3.4 |
| `escalation.budget_exceeded` | CONDITIONAL — REQUIRED when `reason` is `BUDGET_EXCEEDED`; **excluded here** because this instance's reason differs. Shape (§12.2.1): `{"dimension": "monetary"\|"compute_seconds"\|"tokens", "budget_limit": str, "actual_or_estimated": str, "is_estimate": bool}`. Never defined in §7.3.4's escalation-object field list — F-09. | §12.2.1 |

## Provenance / content

`provenance` REQUIRED here because `partial_result_available: true` (§7.3.4,
§7.3.8 footnote, §16.2.3 item 8). Field citations as in
message-response.notes.md. Partial result carried in Content — the canonical
location (§7.3.4).

## Derived (invented) values

Evidence description text, `service_version` 1.4.0, computation figures,
partial-result text, timestamp at :05 (aligned with the §13.4.1 history
example). Other identifiers reuse spec example values (§7.3.4).
