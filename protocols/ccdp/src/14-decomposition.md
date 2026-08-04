# 14. Decomposition

## 14.1. The Decomposition Problem

Most real cognitive work requires decomposition — breaking a complex request into sub-tasks that each route to a different Service. "Fix the bug in the auth module" decomposes into locate, diagnose, repair, verify. "Prove this theorem" decomposes into formalize, search for proof strategy, execute proof steps, check. Decomposition is itself a cognitive act, and one that LLMs are demonstrably weak at — PlanBench shows LLMs collapse on longer planning horizons and hallucinate plans for unsolvable problems [PlanBench].

CCDP resolves this by treating decomposition as a first-class Service: a dedicated Decomposition Service with Capability Type `org.ccdp.decomposition` that receives complex requests and emits structured Decomposition Plans. The Dispatcher routes to the Decomposition Service first, then routes each sub-request from the plan independently. The Dispatcher performs only structural operations — routing, dependency resolution, typed result-reference substitution; the decomposition intelligence lives in a dedicated, auditable Service behind a typed interface.

## 14.2. When Decomposition Occurs

The Dispatcher invokes the Decomposition Service in one of two ways:

**Explicit decomposition request.** The requester sets `capability_type` to `org.ccdp.decomposition`, indicating that the request should be decomposed rather than handled directly. The Dispatcher routes to the Decomposition Service, receives a plan, and executes it.

**Dispatcher-initiated decomposition.** The Dispatcher MAY route a request to the Decomposition Service when:
- No single Service is registered for the requested `capability_type`.
- The request's Content exceeds the target Service's declared input constraints (e.g., the input is too large or too complex).
- The Dispatcher's routing configuration includes a rule mapping certain capability types to automatic decomposition.

Dispatcher-initiated decomposition MUST be triggered by envelope-level signals, not by content inspection. The relevant signals are: (a) no single Service is registered for the requested `capability_type` (a routing-level signal), (b) the Request's `content.body` size exceeds the target Service's declared `max_input_size` in the Capability Record (a structural size check, not semantic), (c) the Dispatcher's routing configuration includes a decomposition rule for the capability type (a policy signal). The Dispatcher MUST NOT inspect content semantics to decide whether decomposition is needed.

In both cases, the decomposition step is visible in the audit trail — the routing decision records that decomposition was invoked and why.

## 14.3. Decomposition Plan Structure

A Decomposition Plan is the Content of a DECOMPOSITION_RESULT message. It specifies what sub-requests to create, how they depend on each other, how to allocate resources, and how to compose the results.

```json
{
  "content": {
    "type": "structured-data",
    "schema_ref": "org.ccdp.decomposition/output/v1",
    "body": {
      "plan_id": "plan-550e8400-...",
      "description": "Decompose theorem-proving request into formalization and proof search",

      "sub_requests": [
        {
          "sub_id": "sub-001",
          "capability_type": "org.ccdp.language.translation",
          "description": "Translate natural-language theorem statement into Lean 4 syntax",
          "content": {
            "type": "natural-language",
            "body": {
              "source_representation": "natural-language",
              "target_representation": "lean4",
              "text": "For all natural numbers n, if n > 1 then n has a prime factor"
            }
          },
          "constraints": {
            "deadline_fraction": 0.2,
            "cost_fraction": 0.1,
            "provenance_requirement": { "min_policy_grade": "VALIDATED" }
          },
          "depends_on": []
        },
        {
          "sub_id": "sub-002",
          "capability_type": "org.ccdp.deduction",
          "description": "Search for proof of formalized theorem",
          "content": {
            "type": "formal-logic",
            "body": {
              "logic": "lean4",
              "formula": {"$ref": "sub-001.result", "path": "/body/translation"}
            }
          },
          "constraints": {
            "deadline_fraction": 0.7,
            "cost_fraction": 0.8,
            "provenance_requirement": { "min_policy_grade": "FORMALLY_VERIFIED" }
          },
          "depends_on": ["sub-001"]
        },
        {
          "sub_id": "sub-003",
          "capability_type": "org.ccdp.language.translation",
          "description": "Translate proof back to natural language explanation",
          "content": {
            "type": "formal-logic",
            "body": {
              "source_representation": "lean4-proof",
              "target_representation": "natural-language",
              "proof": {"$ref": "sub-002.result", "path": "/body/proof"}
            }
          },
          "constraints": {
            "deadline_fraction": 0.1,
            "cost_fraction": 0.1,
            "provenance_requirement": { "min_policy_grade": "ASSERTED" }
          },
          "depends_on": ["sub-002"]
        }
      ],

      "composition": {
        "method": "template",
        "template": {
          "type": "multipart",
          "body": {
            "parts": [
              { "label": "formalization", "source": "sub-001.result" },
              { "label": "proof", "source": "sub-002.result" },
              { "label": "explanation", "source": "sub-003.result" }
            ]
          }
        },
        "provenance_rule": "weakest_link"
      },

      "fallback": {
        "on_sub_failure": "escalate_parent",
        "on_composition_failure": "return_partial"
      }
    }
  }
}
```

### 14.3.1. Sub-Request Specification

Each `sub_requests` entry contains:

**`sub_id`** (string, REQUIRED): A unique identifier within the plan, used for dependency references and result composition.

**`capability_type`** (string, REQUIRED): The Capability Type for this sub-request. The Dispatcher routes each sub-request independently.

**`description`** (string, OPTIONAL): Human-readable description of this sub-task.

**`content`** (object, REQUIRED): The Content payload for this sub-request. MAY reference results of previous sub-requests using typed result references (Section 14.3.3).

**`constraints`** (object, OPTIONAL): Resource constraints for this sub-request.
- `deadline_fraction`: Fraction of the parent's remaining deadline allocated to this sub-request (0.0 to 1.0).
- `cost_fraction`: Fraction of the parent's cost budget allocated to this sub-request.
- `provenance_requirement`: Minimum provenance grade for this sub-request.

**`depends_on`** (array of strings, REQUIRED): Sub-request IDs that must complete before this sub-request can be dispatched. Empty array means no dependencies (can run immediately).

### 14.3.2. Dependency Graph

The dependency graph is defined by the `depends_on` arrays on each sub-request entry. The Dispatcher constructs the DAG from these arrays and validates that:

1. All `depends_on` references point to valid `sub_id` values within the same plan.
2. The resulting graph is acyclic (a cyclic dependency is a malformed plan — reject with error `-32602`).
3. All sub-requests are reachable (no orphaned entries).

Sub-requests with empty `depends_on` arrays can execute in parallel. The Dispatcher SHOULD execute independent sub-requests concurrently when resources permit.

The `dependencies` top-level field is OPTIONAL and informative (e.g., for visualization tooling). If present, it SHOULD be consistent with the `depends_on` arrays. In case of conflict, the `depends_on` arrays are authoritative and the `dependencies` field is ignored.

### 14.3.3. Typed Result References

Sub-request content MAY reference results from completed dependencies using typed result references. A result reference is a JSON object (not a template string) that the Dispatcher resolves structurally:

```json
{
  "$ref": "sub-001.result",
  "path": "/body/translation",
  "fallback": null
}
```

**`$ref`** (string, REQUIRED): The sub-request ID whose result is referenced, suffixed with `.result` to refer to the Response Content.

**`path`** (string, REQUIRED): A JSON Pointer [RFC 6901] path into the referenced result's Content. The JSON Pointer path in a result reference is evaluated relative to the referenced sub-request's Response `content` object. For example, if sub-001's Response has `"content": {"type": "text", "body": {"translation": "..."}}`, the path `/body/translation` resolves to the translation string. The root is `content`, not the full Response envelope.

**`fallback`** (any, OPTIONAL): The value to use if the referenced path does not exist in the result. If omitted and the path does not exist, the Dispatcher follows the plan's `fallback` strategy.

The Dispatcher resolves result references by: (1) waiting for the referenced dependency to complete, (2) extracting the value at the JSON Pointer path from the dependency's Response Content, (3) substituting the reference object with the extracted value. This is a structural operation — the Dispatcher reads a typed path, not natural language. The Dispatcher MUST NOT perform string interpolation, template expansion, or any transformation on the extracted value.

If a referenced dependency failed or escalated, the Dispatcher follows the plan's `fallback` strategy.

### 14.3.4. Composition Specification

The `composition` field specifies how sub-results are assembled into the final result:

**`method`** (string, REQUIRED): One of:
- `"template"`: Assemble parts according to a template (most common).
- `"concatenation"`: Concatenate sub-results in dependency order.
- `"selection"`: Select the best sub-result by a criterion (useful for cross-checking). Allowed `selection` criteria are: `"highest_provenance"` (select the sub-result with the highest provenance grade in policy order), `"lowest_cost"` (select the sub-result with the lowest reported cost), `"first_completed"` (select the first sub-result to arrive — for latency-optimized redundant dispatch). Other selection criteria require routing to an `org.ccdp.composition` Service, as they may involve semantic judgment.
- `"custom"`: A custom composition function (specified as a Content payload routed to a composition Service).

When `method` is `"custom"`, the composition payload is routed to a Service with capability type `org.ccdp.composition`. This is a well-known capability type (added to Section 8.3's well-known types). The Composition Service receives the sub-results and the composition specification and returns the composed result. The Dispatcher does not perform custom composition itself — it delegates to the Composition Service and forwards the result.

**`template`** (object, conditional): REQUIRED when `method` is `"template"`. The template for the composed result, with `source` fields referencing sub-results.

**`provenance_rule`** (string, REQUIRED): How to compute the composed result's provenance grade. One of:
- `"weakest_link"`: Composed grade = min(sub-result grades, decomposition grade). Default.
- `"cross_check"`: If independent sub-results agree, upgrade to CROSS_CHECKED (per Section 10.5.2).
- `"explicit"`: The composition step assigns its own grade (used when the composition itself involves verification).

### 14.3.5. Fallback Strategy

The `fallback` field specifies what happens when sub-requests fail:

**`on_sub_failure`** (string, REQUIRED): One of:
- `"escalate_parent"`: Escalate the entire parent request through the parent's Escalation Chain. Any partial sub-results are included in the Escalation.
- `"skip_and_compose"`: Skip the failed sub-request and compose the result from successful sub-results only. The composition template must handle missing parts.
- `"retry_alternative"`: Retry the failed sub-request with a different Service (following normal routing with the failed Service excluded).

**`on_composition_failure`** (string, REQUIRED): One of:
- `"return_partial"`: Return the individual sub-results without composition as a multipart Response.
- `"escalate_parent"`: Escalate the entire request.

**Fallback behavior matrix.** The following matrix summarizes default Dispatcher behavior for common failure scenarios during plan execution, governed by the `$ref.fallback` field (Section 14.3.3) and the `on_sub_failure` / `on_composition_failure` fields (Section 14.3.5):

| Scenario | Governing Field | Default Behavior | Configurable Values |
|---|---|---|---|
| Result reference `path` does not resolve in an otherwise-successful dependency | `$ref.fallback` | Substitute the reference's `fallback` value if specified; otherwise follow `on_sub_failure` | Any JSON value, or omitted |
| Sub-request failed entirely, no result to reference | `on_sub_failure` | Escalate the parent request | `"escalate_parent"` (default), `"skip_and_compose"`, `"retry_alternative"` |
| Sub-request escalated with a partial result | `on_sub_failure` | Use the partial result if the `$ref` path resolves against it; otherwise apply `on_sub_failure` | Same as above |
| All sub-requests succeeded, composition fails | `on_composition_failure` | Escalate parent request with all sub-results as partial results | `"escalate_parent"` (default), `"return_partial"` |
| Width or node limit exceeded | — | Reject plan with error `-32012` before execution begins | Not configurable — always reject |

## 14.4. Dispatcher Execution of Decomposition Plans

When the Dispatcher receives a DECOMPOSITION_RESULT, it executes the plan:

1. **Validate the plan.** Check that the dependency graph is a DAG, all `capability_type` references exist in the Registry, all `sub_id` values are unique, all `depends_on` references are valid, and resource allocations sum to ≤ 1.0.

2. **Allocate resources.** Compute each sub-request's deadline and cost budget from the parent's constraints and the plan's `constraints` fractions.

3. **Dispatch independent sub-requests.** For each sub-request with no dependencies (or all dependencies satisfied), create a CCDP Request with:
   - A new `request_id`
   - The same `trace_id` as the parent
   - A new `span_id`
   - `parent_span_id` set to the parent request's `span_id`
   - The allocated deadline and cost budget
   - The resolved Content (typed result references resolved per Section 14.3.3)

4. **Process results as they arrive.** As each sub-request completes, check which dependent sub-requests are now unblocked and dispatch them.

5. **Handle failures.** Follow the plan's `fallback` strategy for failed sub-requests.

6. **Compose the final result.** When all sub-requests (or all non-skipped sub-requests) are complete, compose the final result according to the `composition` specification.

**Composition boundary.** For `template`, `concatenation`, and `selection` composition methods, the Dispatcher performs structural assembly: it places sub-results into the template slots, concatenates them in order, or selects by a typed criterion (highest provenance grade, lowest cost). These are mechanical operations on typed wrappers, consistent with the Coordinator Dispatcher model. The Dispatcher MUST NOT perform composition that requires reasoning about content meaning — such composition MUST be routed to an `org.ccdp.composition` Service.

7. **Compute composed provenance.** Apply the `provenance_rule` to derive the composed result's provenance grade. Include the full `composition_trace` (Section 10.5.4). The Dispatcher creates derived provenance for the composed response using the composition rules in Section 10.5. This is a new provenance value computed from the sub-results' grades — the Dispatcher does not modify any sub-result's received provenance. The derived provenance for the composed response MUST include evidence entries documenting which sub-results contributed and which composition rule was applied.

8. **Return the composed Response.** Send the final Response to the original requester with the composed Content and Provenance.

All steps are logged in the audit trail, creating a complete record of the decomposition execution.

## 14.5. Decomposition Service Contract

The Decomposition Service implements Capability Type `org.ccdp.decomposition` with:

**Input schema:** A CCDP Request (the request to be decomposed). The Decomposition Service receives the original Content and must emit a valid Decomposition Plan.

**Output schema:** A Decomposition Plan (Section 14.3).

**Provenance:** The Decomposition Plan carries its own provenance grade reflecting the evidence strength behind the decomposition. An LLM-only decomposition is graded ASSERTED or HEURISTIC. A decomposition validated by a plan checker is graded VALIDATED.

**Escalation:** If the Decomposition Service cannot decompose the request (it is atomic, it is outside the Service's domain, or the problem is ambiguous), it returns an Escalation with reason `CAPABILITY_EXCEEDED` or `AMBIGUOUS_INPUT`.

The Decomposition Service is a natural candidate for Mode 3 (LLM + validator): an LLM proposes a decomposition plan, and a validator checks structural consistency (valid capability types, acyclic dependencies, resource allocations sum correctly, all result references are valid). The validated plan carries a higher provenance grade than the raw LLM output.

## 14.6. Recursive Decomposition

A sub-request in a Decomposition Plan MAY itself have `capability_type: "org.ccdp.decomposition"`, producing a nested decomposition. The Dispatcher handles this recursively: the sub-decomposition produces its own plan, which the Dispatcher executes as a nested sub-tree of the parent plan.

To prevent unbounded recursion, the Dispatcher MUST enforce a maximum decomposition depth (RECOMMENDED: 5). If a decomposition exceeds the maximum depth, the Dispatcher returns error `-32012` (decomposition limit exceeded, Section 13.2) for the deepest sub-request, with `data.limit_type` set to `"depth"`.

The Dispatcher MUST also enforce maximum plan width (the number of sub-requests in a single plan) and maximum total node count (the total number of sub-requests across all recursion levels for a single top-level request). RECOMMENDED limits: maximum width 50 per plan, maximum total nodes 100 per top-level request. A plan that exceeds the width or total-node limit is rejected before execution begins with error `-32012`, with `data.limit_type` set to `"width"` or `"total_nodes"` respectively. These limits prevent decomposition bombs (Section 17.2.5) and are conformance requirements for both Core and Full Dispatchers.

The audit trail records the full tree of decompositions, enabling reconstruction of arbitrarily complex request execution paths.
