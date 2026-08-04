# 18. Open Questions

This section documents design questions that have been identified during the v0.2 review process but are intentionally deferred. They are recorded here so that future revisions can address them with full context. None of the questions listed in this section, by themselves, represent known contradictions. Each represents a point where a different design choice could improve the protocol.

## 18.1. Epistemic Layer Cost-Field Placement

**Context.** Section 6 places cost, deadline, and resource fields in Layer 3 (Epistemic Layer), but Section 9's routing algorithm uses these fields as routing inputs, which means the Dispatcher must read selected Layer 3 fields. The current text acknowledges this layer crossing explicitly (Section 6.2.2), making the behavior coherent but architecturally impure.

**Question.** Should cost and resource fields migrate to Layer 2 (Routing/Audit Layer), or should Layer 3 be formally split into "Dispatcher-interpretable Epistemic fields" (provenance, cost, deadline) and "opaque Epistemic fields" (evidence details, composition metadata)?

**Trade-offs.** Moving fields to Layer 2 is cleaner architecturally but blurs the distinction between structural routing data and epistemic metadata. Splitting Layer 3 preserves the four-layer model but adds complexity. The current explicit acknowledgment is adequate for v0.2.

## 18.2. Grade Name Taxonomy

**Context.** The provenance grade names (OPAQUE, ASSERTED, HEURISTIC, COMPUTED, VALIDATED, CROSS_CHECKED, FORMALLY_VERIFIED, HUMAN_ATTESTED — earlier draft names such as GENERATED and CITED were superseded during the v0.2 review process) combine method-descriptive names (COMPUTED, CROSS_CHECKED, FORMALLY_VERIFIED) with accountability-descriptive names (HUMAN_ATTESTED). Some grade names describe an evidence method; others describe a trust-boundary status.

**Question.** Should grade names be uniformly method-descriptive (e.g., COMPUTED, CROSS_CHECKED, FORMALLY_VERIFIED, HUMAN_REVIEWED) or uniformly trust-boundary-descriptive (e.g., UNVERIFIED, INDEPENDENTLY_CONFIRMED, PROVABLE, ACCOUNTABLE)?

**Trade-offs.** Renaming grades has wire-compatibility implications. The numeric grade values (0–7) are the protocol-level identifiers for routing and conformance; names are human-readable labels. The current mixed naming is well-understood by the intended audience. A rename would be a breaking change for any pre-1.0 implementations but is feasible before the first stable release.

## 18.3. Capacity Reservation and Admission Control

**Context.** Section 12 defines capacity advertisements as best-effort snapshots with no freshness guarantee, lease, or admission-control semantics. At high scale, routing on stale capacity information can amplify overload (the bullwhip effect noted in Section 12).

**Question.** Should CCDP define capacity-reservation tokens, admission-control handshakes, or lease-based capacity semantics?

**Trade-offs.** Reservation and admission control would improve routing accuracy under load but add significant protocol complexity (reservation lifecycle, timeout, cancellation, partial-use accounting). The current snapshot model with staleness guidance is adequate for moderate-scale deployments. High-scale deployments can add infrastructure-level admission control without protocol changes.

## 18.4. Wire Identity Fields

**Context.** Section 4 defines the Authenticated Sender as the transport-verified identity (mTLS CN or bearer-token subject), distinct from `source_id` (originator) and `audit.dispatcher_id` (intermediary). This is a conceptual definition — there is no explicit `authenticated_sender`, `originator_id`, `sender_id`, or `forwarder_id` wire field in the message envelope.

**Question.** Should the protocol add explicit identity wire fields (e.g., `originator_id`, `sender_id`, `forwarder_id`) to the message envelope, or is the current lighter approach (a defined term plus transport-layer verification) sufficient?

**Trade-offs.** Explicit fields make identity unambiguous in audit records and allow identity verification without access to transport-layer state. The lighter approach avoids wire-format expansion and is adequate when all messages pass through a single Dispatcher. Multi-Dispatcher chains (not currently specified) would benefit from explicit fields.

## 18.5. Registry Wire Binding

**Context.** Section 8 defines Registry operations as a logical interface. The API describes what operations exist (register, query, update, deregister, health) but does not specify a wire binding (REST, gRPC, embedded).

**Question.** Should CCDP define a normative Registry wire binding for multi-implementation interoperability, or should Registry interoperability remain deployment-defined?

**Trade-offs.** A normative binding enables Registry interoperability across implementations but constrains deployment flexibility. Many deployments will embed the Registry in the Dispatcher process, making a wire binding unnecessary. A binding could be defined as an optional companion specification rather than a core protocol requirement.
