# FINDINGS — CCDP v0.2 JSON/JSON-RPC Extraction

Discrepancies, ambiguities, and gaps observed while extracting the complete
JSON surface of CCDP draft v0.2 (document version 0.2.0). **Descriptive, not
normative**: nothing here was "fixed" in the corpus — the spec text stands as
written, and these findings feed CCDP v0.3 and the ccdp-rs grammar audit.
IDs (F-NN) are cross-referenced from canonical/*.notes.md and inventory/*.

Severity key: **[conflict]** two normative statements disagree · **[gap]**
something used or implied but never specified · **[inconsistency]**
non-normative divergence (naming, examples) · **[note]** observation.

---

## A. Matrix-vs-prose conflicts (§7.3.8 is normative and "takes precedence")

**F-02 [conflict/gap] — The §7.3.8 matrix omits ten fields that prose defines,
including several REQUIRED ones, and the precedence rule doesn't say what
omission means.**
§7.3.8: "This matrix is normative. Where prose elsewhere in this section or
other sections conflicts with this matrix, the matrix takes precedence."
The matrix lists only 14 fields. Absent from it entirely: `metadata`
(REQUIRED on every message, §7.3.1), `remaining_budget_ms` (REQUIRED on
REQUEST, §7.3.2: "**`remaining_budget_ms`** (integer, REQUIRED)"), `status`
(REQUIRED on RESPONSE, §7.3.3), `escalation` (REQUIRED object, §7.3.4),
`notification_type` (REQUIRED, §7.3.5), `health` (with `health.status`
REQUIRED, §7.3.6), `parent_span_id`, `idempotency_key` (§7.3.2), the
Dispatcher-written `audit` block (§7.5), and `content` itself. If omission
from the matrix counts as a "conflict" that the matrix wins, `metadata` and
`remaining_budget_ms` would silently become non-required — almost certainly
unintended. The matrix needs either completion or an explicit statement that
it is non-exhaustive.

**F-04 [conflict] — The matrix marks `capability_type` S (RECOMMENDED) on
RESPONSE and ESCALATION, but no prose defines the field for those types.**
§7.3.3 and §7.3.4 field lists never mention `capability_type`; its
RESPONSE/ESCALATION appearance exists only as an "S" cell in §7.3.8. What
value it should carry on a RESPONSE (the request's capability type?
the responding service's?) is unstated.

**F-03 [inconsistency] — Table 11.2 marks `message_summary.destination_id`
"—" (not applicable) for RESPONSE audit records, but the §11.2.1 RESPONSE
example includes it** (`"destination_id": "client-app-01"`). Examples are
informative (§2.5), but the example demonstrates a field the normative table
says does not apply.

**F-05 [gap] — Does ESCALATION carry `status`?** §7.3.4: "It shares the
RESPONSE envelope structure with additional escalation-specific fields." The
RESPONSE structure includes REQUIRED `status` (§7.3.3), yet no escalation
example shows `status` and the matrix omits the field entirely. Undecidable
from the text.

## B. Prose-only fields (defined, but no example anywhere in the spec)

**F-14 [gap] — Fields with normative definitions but zero JSON examples:**
- `provenance_requirement.required_methods` and `required_evidence_types`
  (§7.3.2) — the two fields that drive routing Steps 5.2/5.3 never appear in
  any example envelope.
- `audit.routing_decision.filters_applied` (§9.2 Step 7: "`filters_applied`:
  which filters removed candidates") — absent from the §7.5 and §11.2
  examples (which instead show `candidates_filtered`, itself defined nowhere
  in prose — the two names appear to describe the same data; see also F-19).
- `provenance_policy.trigger` values: only `"grade_below_requirement"` and
  `"no_candidate_meets_requirement"` ever appear (examples §11.2.2–11.2.3);
  no vocabulary is defined despite §11.4 making `trigger` a required
  diagnostic.
- `routing.registry_source`: example value `"live"` only; §8.6 requires
  logging "whether they were made from live Registry data, cached data, or
  static fallback" but binds no values.
- Audit fields `health_summary.status`, `error_code`, `error_detail`,
  `retry_count` — see F-22.

**F-22 [gap] — Table-only audit fields.** `health_summary.status` appears
solely as a row in Table 11.2 (R for HEALTH_RESP); no `health_summary`
structure is defined or exemplified anywhere. `error_code`, `error_detail`,
`retry_count` appear solely in the §11.4 informal category table ("Errors"
category); no audit-record example or definition carries them.

**F-26 [conflict/gap] — Evidence-entry fields required by §10 but absent from
the §4 normative Evidence Entry schema.** §10.2 Grade 5: "A service assigning
CROSS_CHECKED MUST include evidence entries documenting the independence
level: `"independence": "full"` …" — `independence` is not in the §4 schema.
§10.2 Grade 2 shows `"method": "statistical_testing", "confidence": 0.92,
"false_positive_rate": 0.03` — `confidence`/`false_positive_rate` likewise
undefined in §4. The §4 schema is billed as "the normative schema" yet §10
mandates fields outside it.

## C. Malformed or non-JSON examples inside ```json fences

**F-01 [inconsistency] — Two fences contain non-JSON notation that is not
the sanctioned `// ...` elision style (§2.3).**
- §12.2.1 `budget_exceeded`: a bare key fragment whose `dimension` value is
  type-union notation — `"dimension": "monetary" | "compute_seconds" |
  "tokens"` — inside a ```json fence
  (examples/12-flow-control/002-budget-exceeded-fragment.json).
- §15.4.2 signing input: `JCS({"envelope": <envelope-value>, "content":
  <content-value>})` — pseudo-code in a ```json fence
  (examples/15-security/003-jcs-signing-input.json).
Seventeen further fences are non-parsing solely due to `// ...` / `/* ... */`
elision comments, which §2.3 explicitly sanctions — expected, not findings. Full
parse ledger in MANIFEST.md.

## D. Inconsistent field names across sections

**F-19 [inconsistency] — Same concept, different names:**
- Registry Lookup input `min_provenance_grade` (§8.4.2) vs envelope
  `provenance_requirement.min_policy_grade` (§7.3.2; §21.1.7 says
  `min_grade` was renamed to `min_policy_grade` — the Lookup parameter
  kept a third name).
- `cost_hints.estimated_cost_per_request.monetary_units` = *amount* (§8.2.2)
  vs envelope `cost_budget.max_monetary_cost` = amount with
  `max_monetary_units` as a deprecated alias (§7.3.2) vs audit
  `cost_budget_remaining.monetary_units` (§11.2.1). "monetary_units" is an
  amount in two places and a deprecated alias name in a third.
- `audit.routing_decision.*` on the envelope (§7.5) vs `routing.*` in the
  audit record (§11.2): `reason` ↔ `decision`, `filters_applied` (§9.2) ↔
  `candidates_filtered` (§11.2) — parallel structures with drifting names.

**F-23 [inconsistency] —**
- §13.2 requires `-32014` `data.retry_after_ms` (integer); §7.9's mapping row
  says "JSON-RPC error `-32014` … with `Retry-After` in error `data`" —
  header-style name vs field name.
- `-32005` is "Provenance not achievable" in the §13.2 table but "provenance
  requirement not satisfiable" in §9.2 Step 5.

**F-11 [conflict] — `schema_validation` is an object in §7.5**
(`{"input_valid": true, "schema_version": "v2"}`) **but a string in §8.4.7**:
"the Dispatcher logs `schema_validation: "permissive"` in the audit record."
Same field path, two types.

**F-21 [inconsistency] — `record_id` is "string (UUID v4)" per Table 11.1,
but every §11.2 example uses prefixed non-UUID values**
(`"audit-550e8400-e29b-41d4-a716-446655440000"`, `"audit-resp-550e8400-..."`)
— a prefixed UUID is not a UUID.

## E. Enum values used but never defined

**F-12 [gap] — `org.ccdp.notification`** appears as `capability_type` in the
§7.3.5 NOTIFICATION example but is not among the §8.3 well-known capability
types, and `org.ccdp.*` is a reserved namespace (§7.3.1).

**F-20 [gap] — `composition_trace.method`** — example value `"sequential"`
(§10.5.4); §10.5 discusses sequential/parallel/decomposition composition, but
no value set is bound to the field.

**F-24 [note] — Error code `-32013` is skipped** (§13.2 goes -32012 → -32014)
with no reservation note.

**F-25 [gap] — List Schema Versions output field `compatibility`** (§8.4.5)
has no defined value vocabulary (§8.5.3's backward/forward/full discussion is
not bound to this field).

**F-28 [inconsistency] — §6.2.4's content-type list omits `code` and
`multipart`**, both defined as well-known in §7.4 ("`natural-language`,
`formal-logic`, `proof-object`, `validated-plan`, `structured-data`, or a
custom type" vs §7.4's seven).

## F. Structures referenced but never specified

**F-06 [gap] — Content for HEALTH_REQUEST/HEALTH_RESPONSE (and NOTIFICATION)
is never specified.** §4 ("A Message consists of an Envelope and a Content
payload") and §7.1 (`params: {envelope, content}`) imply Content on every
message, but health payloads live in the *envelope* (`envelope.health`,
§7.3.6) and no health/notification content schema exists. Whether `content`
may be absent on these types is unstated. (Canonical health instances omit it;
the notification instance carries a derived `structured-data` body.)

**F-07 [gap] — DECOMPOSITION_RESULT reply semantics.** §7.2 encodes it as a
JSON-RPC *request* with an `id` (a reply is therefore due at the JSON-RPC
layer), but the spec never says what the Dispatcher answers, nor how this
message relates to the RESPONSE the Decomposition Service owes for the routed
decomposition REQUEST (§14.2 "The Dispatcher routes to the Decomposition
Service, receives a plan, and executes it" — via which of the two message
shapes?).

**F-09 [gap] — `escalation.budget_exceeded`** is mandated by §12.2.1 ("When
escalation reason is `BUDGET_EXCEEDED`, the `escalation` object MUST
include…") but §7.3.4's definition of the `escalation` object does not list
it, and no complete ESCALATION example carries it.

**F-10 [gap] — Decomposition Plan top-level fields defined only by example.**
`plan_id` and plan-level `description` appear in the §14.3 example but are
never defined in §14.3.1–14.3.5 prose (which defines only sub-request,
composition, and fallback fields). The informative `dependencies` field is
named (§14.3.2, §6.2.3) but its shape is never specified.

**F-18 [gap] — Response-side Dispatcher audit annotation shape.** §7.5 says
the Dispatcher "MUST annotate the envelope with audit metadata" when
forwarding any message, but the shown `audit` block (routing_decision,
schema_validation) is request-shaped; what the annotation looks like on a
forwarded RESPONSE/ESCALATION is unspecified.

**F-17 [gap] — Requester-outbound signature placement.** §15.4.4 defines the
requester-outbound signing profile, but the spec never shows where a
requester's signature travels; the `org.ccdp.signature` metadata key is
exemplified only for service responses (§15.4.2).

**F-22bis [note] — The Dispatcher's own health endpoint** (§11.6: the audit
failure policy "MUST be discoverable via the Dispatcher's own health
endpoint") is referenced but never specified.

## G. Cross-section semantic conflicts

**F-08 [conflict] — Is `provenance.computation` optional or mandatory?**
§7.3.3: "**`computation`** (object, OPTIONAL)". §12.2.3: "Every Response MUST
report actual resource consumption in the `provenance.computation` field."
§16.2.3 item 12 sides with §12.2.3 ("Report computational resource
consumption in `provenance.computation`"). Direct MUST-vs-OPTIONAL conflict,
and it is *not* resolved by §7.3.8 (the matrix doesn't cover sub-fields).

**F-16 [conflict] — Dispatcher metadata accumulation breaks requester
signatures.** §15.4.4 (requester-outbound profile) excludes from signing only
`audit`, `remaining_budget_ms`, conditionally `destination_id`, and "metadata
keys in `org.ccdp.dispatcher.*`". But §13.4.1 has the Dispatcher append
`org.ccdp.escalation_history` and `org.ccdp.partial_results` to the forwarded
Request's `metadata` — keys *not* under `org.ccdp.dispatcher.*`, hence inside
the signed scope. §15.4.2: "a signature covering a field the Dispatcher
subsequently modifies is invalid by construction — the verifier MUST reject
it." A signed request that traverses an escalation chain therefore arrives
with an invalid signature.

**F-15 [inconsistency] — Composition-template `source` references are bare
strings, not typed result references.** §14.3.3 defines result references as
typed objects ("A result reference is a JSON object (not a template string)")
with `$ref` + `path`, yet the §14.3 composition template's parts use
`{"label": "formalization", "source": "sub-001.result"}` — bare
`sub-NNN.result` strings with no `path` and no defined resolution rule for
`source`. The template mechanism thus reintroduces the untyped-string form
§14.3.3 abolishes, and how `source` maps to a part's `body` is unspecified.

**F-13 [inconsistency] — `escalation.suggested_target` is an untyped string**
that "MAY be a Service ID or Capability Type" (§7.3.4, §9.4), while §8.2.2
requires typed `{kind, value}` entries for exactly this disambiguation in
escalation chains: "string-only entries are ambiguous and MUST NOT be used."
The same ambiguity the chain fix eliminates survives in `suggested_target`.

**F-27 [inconsistency] — §15.3.2's token example uses a JSON number for
money** (`"max_cost_usd": 10.00`), contradicting §2.3: "All monetary-value
examples in this specification use string representations." (Arguably a JWT
claim rather than a CCDP message, but it is a monetary-value example in the
spec.)

## H. Notes

**F-29 [note] — Version labeling.** The extraction assignment referred to the
spec as "v0.2c"; the source says "Draft v0.2 — review iterations through
v0.2m incorporated" (README) and document version 0.2.0 (§2.1, §01). The
corpus was extracted against the files as found (see MANIFEST.md for
mtimes).

**F-30 [note] — `trace_flags`** appears in the `traceparent` format (§11.3)
but has no envelope field and no stated default; implementations must infer
its handling from W3C Trace Context.

**F-31 [note] — HEALTH_REQUEST is a method-bearing message with an `id`**
whose HEALTH_RESPONSE is the JSON-RPC response — consistent — but §13.6.1
also calls the probe target "the Service's health endpoint" (a distinct URL
in the Capability Record, §8.2.2) while §7.2's table routes `ccdp/
health.request` Dispatcher → Service like other messages. Whether health
probes go to `endpoint` or `health_check.endpoint` is implied (the latter)
but never stated as a requirement on the message flow.

---

Four prior review rounds each surfaced issues; this extraction pass adds the
register above (32 entries). The absence of any category from a future pass
should be treated with suspicion rather than celebration.
