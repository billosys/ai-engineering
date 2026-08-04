# 10. Provenance and Evidence Grades

## 10.1. Rationale

Provenance grades are CCDP's novel contribution — the feature that distinguishes it from every existing protocol for service communication. The core insight: cognitive outputs are not data; they are *claims with epistemic status*. A database query returns a fact. A theorem prover returns a proof. An LLM returns a plausible completion. These are structurally different kinds of evidence, and a protocol that treats them identically forces every consumer to reconstruct epistemic status from scratch.

The provenance system is grounded in two theoretical foundations:

**Spence's signaling theory [Spence 1973]:** A quality signal works only when it is *expensive to fake*. Each provenance grade represents an increasing cost-to-fake — an LLM can cheaply assert anything (ASSERTED), but producing a machine-checkable proof (FORMALLY_VERIFIED) requires actual computation that cannot be faked without doing the work. The grade taxonomy is designed so that each level requires materially more effort to produce fraudulently than the level below it.

**The specification-recursion problem [Vericoding; Goodhart 1975]:** Formal verification relocates error rather than eliminating it. A proof guarantees code-meets-spec but is silent on whether the spec captures intent. Empirically, LLMs game weak specifications into vacuous proofs (~9% of "verified" specs in the Vericoding benchmark were too weak). CCDP addresses this by requiring the `scope` field on FORMALLY_VERIFIED grades — binding the grade to a specific specification whose own provenance is separately trackable.

## 10.2. Grade Taxonomy

Eight provenance grades are defined, ordered from weakest to strongest epistemic standing. The grades are numbered 0–7. For routing and conformance purposes, a higher-numbered grade satisfies any request requiring a lower-numbered grade (the policy-order property defined in Section 10.2.1). This ordering is a protocol convention, not a claim about universal epistemic subsumption — see the caveat below.

### 10.2.1. Policy Order

This ordering is a *policy order* for routing and conformance, not a universal epistemic truth. The ordering holds for the protocol's primary use case — selecting services and evaluating whether a response meets a requester's quality threshold. It does not hold in all epistemic contexts: HUMAN_ATTESTED does not imply deterministic COMPUTED (a human reviewer may not have performed the computation); CROSS_CHECKED does not imply VALIDATED against an external criterion unless validation was part of each independent process. The ordering reflects the protocol's design judgment that grades higher on the ladder are harder to achieve and more expensive to fake (the Spence signaling criterion), not that every higher grade subsumes every lower grade's specific method. Consumers with domain-specific epistemic requirements SHOULD inspect the `evidence` entries rather than relying solely on grade comparison.

### Grade 0: OPAQUE

No provenance information is available. The service did not report how it produced this result, or the result's origin is unknown. This grade is assigned when:
- A service does not implement provenance reporting
- A result passes through a system boundary that strips provenance
- Legacy data is ingested without epistemic metadata

OPAQUE is not an error; it is an honest statement of ignorance. Consumers SHOULD treat OPAQUE results with maximum skepticism.

### Grade 1: ASSERTED

The service claims this result but provides no verification evidence. The result reflects the service's output as-is, with no external check.

Typical sources: raw LLM output without verification, unvalidated human opinion, unchecked database entries.

A service MUST assign ASSERTED (not a higher grade) when it has performed no verification step — even if the service is highly confident. Confidence without verification evidence is assertion.

### Grade 2: HEURISTIC

The result was produced by a method with known error characteristics — a statistical model, a heuristic algorithm, a classifier with measured precision/recall, or a fuzzy search with a relevance score. The evidence includes error bounds or confidence metrics.

Typical sources: classifier output with confidence scores, statistical estimates with error bars, pattern matching with a known false-positive rate.

The distinction from ASSERTED: a HEURISTIC result carries *quantified uncertainty*, while an ASSERTED result carries no uncertainty information. A service assigning HEURISTIC MUST include evidence entries with measurable error characteristics (e.g., `"method": "statistical_testing", "confidence": 0.92, "false_positive_rate": 0.03`).

### Grade 3: COMPUTED

The result was deterministically computed from the inputs. Given the same inputs, any correct implementation of the same algorithm would produce the same result. The computation itself is not in question; only the correctness of the inputs is.

Typical sources: arithmetic calculations, database queries (the data is what the database contains), hash computations, sorting, compilation.

A database query result is COMPUTED relative to the database's current state. The provenance of the stored data is a separate question — if the data was loaded from an unverified source, the query result is COMPUTED (the query was executed correctly) but the underlying data may be OPAQUE or ASSERTED. The `scope` field SHOULD note "computed relative to database state as of [timestamp]" when this distinction matters.

The distinction from HEURISTIC: a COMPUTED result has no uncertainty in the computation — the potential error is in the inputs, not the processing. A database query result is COMPUTED because the query was executed correctly against the data; whether the data itself is correct is a separate provenance question.

### Grade 4: VALIDATED

The result was checked against an external criterion and found consistent. The external criterion is independent of the process that produced the result — it is not self-review.

Typical sources: code that passes a test suite, a plan accepted by an external validator, output that passes a schema check, a translation verified by back-translation.

Back-translation is validation only when the back-translation process is independent of the forward translation and the consistency criterion is formally defined. A back-translation using the same LLM with the same prompt is self-review, not validation — it SHOULD be graded HEURISTIC, not VALIDATED.

The distinction from COMPUTED: VALIDATED results have been checked by an independent verification step, not just deterministically produced. A service assigning VALIDATED MUST include evidence entries identifying the validation method and its scope (what was validated, and what was not).

**Design note (a judgment call):** Test-suite validation and formal verification are separated into different grades because they have structurally different failure modes. A test suite samples — it checks finitely many cases and says nothing about unchecked cases. A formal proof exhausts — it checks all cases within the scope of the specification. The gap between "all tested cases pass" and "all possible cases are covered" is real and load-bearing in safety-critical contexts. We acknowledge that some software engineering traditions would group these together, and that the boundary between extensive testing and lightweight formal methods (property-based testing, coverage-guided fuzzing) is blurry. The separation is a design choice favoring precision over convenience.

### Grade 5: CROSS_CHECKED

The result was independently produced by multiple services using different methods, and the results are consistent. The services did not share intermediate state, prompts, or reasoning — they arrived at the same conclusion independently. Independence has degrees. Full independence means different algorithms, different training data, different infrastructure. Partial independence (same model family but different prompts, or same algorithm with different seeds) provides weaker cross-checking. A service assigning CROSS_CHECKED MUST include evidence entries documenting the independence level: `"independence": "full"` (different methods/implementations), `"independence": "partial"` (same method family, different instances/seeds), or `"independence": "replicated"` (identical replicas — this does NOT qualify for CROSS_CHECKED and MUST be graded at the individual replica's level).

Partial independence qualifies for CROSS_CHECKED only when the independent components differ in at least one of: algorithm/method, training data source, or implementation. Same-seed or same-prompt variations of the same model are `"replicated"` and MUST NOT be graded CROSS_CHECKED. The evidence entry MUST document which independence dimension(s) differ.

Typical sources: multiple LLMs generating the same answer without seeing each other's work, a symbolic solver and a numerical solver agreeing, independent human reviewers reaching the same conclusion.

The distinction from VALIDATED: CROSS_CHECKED results are checked not just by one external criterion but by independent *production processes*. Cross-checking detects errors that no single validation method would catch — the error would need to be shared across independent processes, which is unlikely when the processes use different algorithms or representations.

A service (or the Dispatcher, when composing results) assigning CROSS_CHECKED MUST include evidence entries identifying each independent source, confirming they did not share state, and documenting the consistency criterion.

### Grade 6: FORMALLY_VERIFIED

The result has been machine-checked against a formal specification. A proof object is available and can be independently verified by any conforming proof checker.

Typical sources: theorem prover output (Lean, Isabelle, Coq), SMT solver proofs (Z3), verified-correct-by-construction code (Dafny, Verus).

A service assigning FORMALLY_VERIFIED MUST include the `scope` field identifying the specification against which verification was performed, and MUST include evidence entries (Section 4, Evidence Entry) with:

- `method`: `"formal_verification"`
- `artifact_ref.artifact_type`: the type of proof artifact (e.g., `"proof_certificate"`)
- `artifact_ref.integrity`: hash of the proof artifact
- `artifact_ref.uri`: resolvable reference to the proof artifact
- `verified_by`: proof checker identifier and version (e.g., `"coq-8.18.0"`, `"lean4-4.3.0"`)
- `description`: SHOULD include the specification identifier/version and verification environment

A FORMALLY_VERIFIED claim whose evidence entries do not include a resolvable, integrity-checked artifact reference is, for conformance purposes, VALIDATED.

**The specification-recursion caveat:** FORMALLY_VERIFIED means "this result is correct *relative to this specification*." It does not mean the specification is correct. The grade is silent on whether the specification captures the intended behavior. Consumers of FORMALLY_VERIFIED results SHOULD examine the `scope` field to understand what claim is actually being made and SHOULD track the specification's own provenance separately.

This caveat is not a weakness of the grade — it is an honest statement of what formal verification can and cannot do. The alternative — a grade that claims "provably correct" without binding to a specific specification — would be misleading.

### Grade 7: HUMAN_ATTESTED

The result has been reviewed and attested by a human with domain expertise. The human's identity is recorded in the provenance chain.

Typical sources: human code review with sign-off, expert judgment, specification review, value/novelty assessment.

A service assigning HUMAN_ATTESTED MUST include evidence entries identifying the human reviewer (by a verified identifier, not a free-text name) and the scope of their attestation.

**Why HUMAN_ATTESTED is the highest grade:** This is a judgment call, and we state our reasoning explicitly. In the composite cognition architecture, the human occupies the top of the supervision tree because the human provides the faculties for which no external organ exists: specification correctness, broad abstraction, and open-ended value judgment. HUMAN_ATTESTED is highest because the specification-recursion problem terminates at human judgment — someone must decide whether the specification captures intent, and that someone is a person with domain expertise.

This does not mean human judgment is infallible. It means that within the CCDP architecture, human attestation is the terminal verification step — the point where epistemic responsibility is explicitly assigned to a named individual. The provenance chain makes this assignment visible and auditable rather than implicit.

## 10.3. Grade Assignment Rules

A Service MUST follow these rules when assigning a Provenance Grade to a Response:

1. **Accuracy over aspiration.** Assign the grade that *accurately describes* the epistemic status of the result, not the grade the requester asked for. If the requester wanted VALIDATED but the Service could only achieve ASSERTED, the Response MUST carry grade ASSERTED (and the Service MUST escalate if the request's `provenance_requirement` is not satisfied — whether due to `min_policy_grade`, `required_methods`, or `required_evidence_types`).

2. **Evidence required.** A grade above ASSERTED MUST be accompanied by evidence entries that substantiate it. A grade without supporting evidence MUST NOT be assigned — the Service MUST fall back to ASSERTED.

3. **Scope binding for FORMALLY_VERIFIED.** The `scope` field is REQUIRED for FORMALLY_VERIFIED. A claim of formal verification without identifying the specification is not formally verified.

4. **Independence required for CROSS_CHECKED.** Cross-checking requires that the independent sources did not share intermediate state. If the Service cannot confirm independence, it MUST assign VALIDATED (not CROSS_CHECKED).

5. **Identity required for HUMAN_ATTESTED.** The human's identity MUST be recorded in a verifiable form. Anonymous attestation is ASSERTED, not HUMAN_ATTESTED.

6. **Monotonicity.** A Service MUST NOT assign a higher grade to a result that has less epistemic support. If a Service's verification step fails or is inconclusive, the grade reflects the actual achieved level, not the attempted level.

7. **Verifier authority.** The grade reflects the strongest verification actually performed, not the strongest verification the service is capable of performing. A service with formal verification capability that skips verification for performance reasons MUST report the grade of the method actually used. Services SHOULD include an evidence entry with `method: "method_selection"` documenting what verification method was chosen and why, especially when a lower-than-maximum grade is assigned. This meta-evidence entry explains the Service's method choice; it is distinct from the primary evidence entries that substantiate the grade.

## 10.4. Grade Comparison and Ordering

Grades are strictly ordered: OPAQUE < ASSERTED < HEURISTIC < COMPUTED < VALIDATED < CROSS_CHECKED < FORMALLY_VERIFIED < HUMAN_ATTESTED.

A grade *meets* a requirement if it is equal to or greater than the required grade. FORMALLY_VERIFIED meets a requirement of VALIDATED. ASSERTED does not meet a requirement of COMPUTED.

Implementations MUST use the defined ordering for all grade comparisons. The integer codes (0–7) from Section 10.2 MAY be used for programmatic comparison.

## 10.5. Grade Composition

When a result is composed from multiple sub-results — whether through Decomposition (Section 14), chained service calls, or Mode 3 internal composition — the composed result's grade must reflect the epistemic status of the whole, not just the strongest part.

### 10.5.1. Sequential Composition (Weakest-Link Rule)

When a result is produced by a chain of operations (A feeds into B, which feeds into C), the composed grade is the **minimum** of the component grades:

```
composed_grade = min(grade_A, grade_B, grade_C)
```

Rationale: the chain is only as strong as its weakest link. If an LLM (ASSERTED) translates a request that a prover (FORMALLY_VERIFIED) checks, the composed result is ASSERTED — the correctness of the proof depends on the correctness of the translation, which is only asserted.

**Exception — verified translation:** If the translation itself is validated (e.g., by back-translation or by the prover rejecting mistranslations), the translation step's grade is VALIDATED, and the composed grade becomes min(VALIDATED, FORMALLY_VERIFIED) = VALIDATED. The Service MUST provide evidence for the translation validation.

### 10.5.2. Parallel Composition (Cross-Check Upgrade)

When a result is independently produced by multiple services and the results agree, the composed grade may be *upgraded* to CROSS_CHECKED, provided:

1. The services used different methods or implementations (not replicas of the same service).
2. The services did not share intermediate state.
3. The results agree according to a defined consistency criterion.

The upgrade applies only if every component grade is at least ASSERTED. OPAQUE results cannot be cross-checked.

```
if all independent results agree AND independence confirmed:
  composed_grade = max(CROSS_CHECKED, min(component_grades))
else:
  composed_grade = min(component_grades)
```

Cross-check upgrade improves confidence in agreement — it does not establish truth. If all independent sources share a common-mode error (e.g., the same incorrect training data, the same flawed specification), their agreement is meaningless. The evidence entries MUST document what was cross-checked and what common-mode risks remain.

### 10.5.3. Decomposition Composition

When a result is assembled from sub-results via a Decomposition Plan (Section 14), the composed grade considers three factors:

1. The grade of the Decomposition Plan itself (how confident are we in the decomposition?)
2. The grades of the sub-results
3. The grade of the composition step (how confident are we in the assembly?)

```
composed_grade = min(decomposition_grade, min(sub_result_grades), composition_grade)
```

If the composition step is trivial (concatenation, simple aggregation), it may be graded COMPUTED. If it requires judgment (synthesizing sub-results into a coherent narrative), it is graded according to the method used.

### 10.5.4. Composition Trace

The `provenance.composition_trace` field documents how a composed grade was derived:

```json
{
  "composition_trace": {
    "method": "sequential",
    "components": [
      {
        "span_id": "00f067aa0ba902b7",
        "service_id": "llm-translator-01",
        "grade": "ASSERTED",
        "role": "translation"
      },
      {
        "span_id": "5b8aa5a2d2c21ea0",
        "service_id": "z3-prover-01",
        "grade": "FORMALLY_VERIFIED",
        "role": "verification"
      }
    ],
    "composed_grade": "ASSERTED",
    "rule_applied": "weakest_link"
  }
}
```

The composition trace provides full transparency into how the final grade was derived. Consumers can inspect it to understand which component limited the overall confidence.

## 10.6. Worked Examples [Informative]

**Example 1: When HUMAN_ATTESTED is required despite formal verification.** A legal compliance check requires that a human compliance officer reviewed and signed off on the determination. Even if a formal verifier proves the logic correct, the regulatory requirement mandates human attestation. The requester sets `min_policy_grade: HUMAN_ATTESTED`; a FORMALLY_VERIFIED response would not satisfy the requirement.

**Example 2: When FORMALLY_VERIFIED is required despite human attestation.** A cryptographic protocol implementation requires machine-checkable correctness proofs. A human expert's review (HUMAN_ATTESTED) provides confidence but not the reproducible, automated verification the deployment requires. The requester sets `required_methods: ["formal_verification"]` — HUMAN_ATTESTED alone, despite ranking higher in the policy order, would not satisfy this requirement because it lacks a machine-checkable proof.

These examples illustrate why the grade ordering is a policy order, not a universal epistemic hierarchy — and why consumers with specific needs should inspect evidence entries.

## 10.7. Provenance in the Audit Trail

Every Response's provenance is recorded in the audit trail (Section 11). The audit system records:

- The grade assigned by the Service
- The evidence entries
- The composition trace (if composed)
- Whether the grade met the Request's `provenance_requirement`
- If the grade did not meet the requirement, whether an Escalation was triggered

This enables retrospective provenance analysis: given any past result, the audit trail shows exactly what evidence supported it, how it was derived, and whether it met the requester's expectations.

Audit records store provenance summaries (grade, evidence types, service IDs) rather than full evidence artifacts. For retrospective verification, the audit record MUST include artifact references (URIs with integrity hashes) that allow independent retrieval and verification of the evidence. If durable evidence retention is required, deployments MUST configure an artifact store with appropriate retention policies. The audit record's artifact references MUST remain resolvable for the configured retention period.

## 10.8. Provenance and Trust

A provenance grade is a *claim by the service about its own output*. The grade is only as trustworthy as the service that assigned it. A compromised or misconfigured service could assign FORMALLY_VERIFIED to unverified output.

CCDP mitigates this through three mechanisms:

1. **Evidence as checkable claims.** Evidence entries (especially `artifact_ref` entries pointing to proof objects or test results) are independently checkable. A grade of FORMALLY_VERIFIED with a proof-object reference can be verified by any conforming proof checker — the grade is not trusted on authority alone.

2. **Audit trail correlation.** The audit system records which service assigned which grade. Patterns of grade inflation (a service consistently assigning grades higher than its `provenance_capabilities.typical_grade`) can be detected and flagged.

3. **Provenance auditing service.** Deployments SHOULD include a provenance auditing service — a Service whose capability type is `org.ccdp.verification` — that spot-checks provenance claims by re-verifying evidence. This is the supply-chain inspection model applied to cognitive provenance.

The trust model is not that services are assumed honest. The trust model is that provenance claims are structured, checkable, and auditable — and that dishonest claims are detectable through the audit trail and independent verification.
