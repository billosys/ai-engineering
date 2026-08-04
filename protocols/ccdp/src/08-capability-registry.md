# 8. Capability Registry

## 8.1. Role and Scope

The Capability Registry is the central source of truth for what Services exist, what they can do, and how to interact with them. The Dispatcher consults the Registry for every routing decision. The Registry enforces schema versioning to ensure that Services evolve without breaking consumers.

This section specifies the Registry's *interface* — the queries it must answer and the records it must maintain. It does not specify the storage backend, replication strategy, or deployment topology. A conforming Registry MAY be a database, a configuration file, a distributed key-value store, an in-memory data structure, or any mechanism that satisfies the interface contract.

## 8.2. Capability Records

A Capability Record describes one Service's implementation of one Capability Type. A Service that implements multiple Capability Types has one record per type.

### 8.2.1. Record Structure

```json
{
  "capability_record": {
    "service_id": "z3-prover-01",
    "capability_type": "org.ccdp.deduction",
    "version": "2.1.0",
    "endpoint": "https://z3-prover-01.internal:8443/ccdp",
    "status": "ACTIVE",

    "input_schema": {
      "$schema": "https://json-schema.org/draft/2020-12/schema",
      "type": "object",
      "properties": {
        "logic": { "type": "string", "enum": ["propositional", "first-order", "smt-lib2"] },
        "formula": { "type": "string" },
        "timeout_ms": { "type": "integer", "minimum": 100 }
      },
      "required": ["logic", "formula"]
    },

    "output_schema": {
      "$schema": "https://json-schema.org/draft/2020-12/schema",
      "type": "object",
      "properties": {
        "result": { "type": "string", "enum": ["sat", "unsat", "unknown", "timeout"] },
        "model": { "type": ["object", "null"] },
        "proof": { "type": ["string", "null"] }
      },
      "required": ["result"]
    },

    "cost_hints": {
      "estimated_latency_ms": { "p50": 500, "p95": 5000, "p99": 30000 },
      "estimated_cost_per_request": { "monetary_units": 0.001, "monetary_unit": "USD" },
      "token_cost": null,
      "compute_intensive": true
    },

    "provenance_capabilities": {
      "max_grade": "FORMALLY_VERIFIED",
      "typical_grade": "FORMALLY_VERIFIED",
      "evidence_types": ["proof-object", "counterexample"]
    },

    "health_check": {
      "endpoint": "https://z3-prover-01.internal:8443/ccdp/health",
      "interval_seconds": 30,
      "timeout_ms": 5000
    },

    "isolation": {
      "executes_arbitrary_code": false,
      "requires_sandbox": false,
      "network_access": false,
      "filesystem_access": false
    },

    "escalation_chain": [
      "isabelle-prover-01",
      "human-review-math-01"
    ],

    "tags": ["formal-methods", "smt", "sat"],
    "description": "Z3 SMT solver for propositional and first-order logic",
    "registered_at": "2026-07-15T10:00:00Z",
    "updated_at": "2026-08-01T14:00:00Z",

    "metadata": {}
  }
}
```

### 8.2.2. Field Definitions

**`service_id`** (string, REQUIRED): Unique identifier for the Service instance.

**`capability_type`** (string, REQUIRED): The Capability Type this record describes.

**`version`** (string, REQUIRED): Semantic version of this record's schema contract. Used for schema versioning (Section 8.5).

**`endpoint`** (string, REQUIRED): The HTTPS endpoint where the Service accepts CCDP messages.

**`status`** (string, REQUIRED): One of `"ACTIVE"` (accepting requests), `"DRAINING"` (completing in-flight requests but not accepting new ones), `"INACTIVE"` (not accepting requests), `"DEPRECATED"` (will be removed; consumers should migrate).

**`input_schema`** (object, REQUIRED): JSON Schema [JSON-SCHEMA-2020-12] describing the valid structure of `content.body` for Requests to this Service. The Dispatcher MUST validate incoming Request content against this schema before forwarding.

**`output_schema`** (object, REQUIRED): JSON Schema describing the structure of `content.body` for Responses from this Service. The Dispatcher SHOULD validate Response content against this schema before forwarding to the requester.

**`cost_hints`** (object, REQUIRED): Resource consumption estimates for routing decisions. Fields:
- `estimated_latency_ms`: Object with percentile keys (`p50`, `p95`, `p99`), values in milliseconds.
- `estimated_cost_per_request`: Monetary cost estimate with `monetary_units` (number) and `monetary_unit` (ISO 4217 string).
- `token_cost`: For LLM-based services, estimated tokens per request. Null for non-LLM services.
- `compute_intensive`: Boolean indicating whether the service consumes significant compute resources.

**`provenance_capabilities`** (object, REQUIRED): What Provenance Grades this Service can produce.
- `max_grade`: The highest grade this Service can assign to its output.
- `typical_grade`: The grade most responses will carry.
- `evidence_types`: Array of Evidence types this Service can produce (e.g., `"proof-object"`, `"test-result"`, `"human-signature"`).

**`health_check`** (object, REQUIRED): Health monitoring configuration.
- `endpoint`: URL for health check probes.
- `interval_seconds`: How often the Dispatcher should probe.
- `timeout_ms`: How long to wait for a health response before marking UNHEALTHY.

**`isolation`** (object, REQUIRED): Security and isolation requirements.
- `executes_arbitrary_code`: Whether the Service executes user-provided code.
- `requires_sandbox`: Whether the Service should run in a sandboxed environment.
- `network_access`: Whether the Service requires network access beyond the Dispatcher.
- `filesystem_access`: Whether the Service requires filesystem access.

**`escalation_chain`** (array of strings, REQUIRED but MAY be empty): Ordered list of Service IDs or Capability Types to try if this Service returns an Escalation. The Dispatcher processes the chain in order. An empty chain means escalation goes directly to the Human Supervisor's queue.

**`tags`** (array of strings, OPTIONAL): Descriptive tags for search and categorization.

**`description`** (string, OPTIONAL): Human-readable description of the Service and its capabilities.

**`registered_at`** (string, REQUIRED): ISO 8601 timestamp of initial registration.

**`updated_at`** (string, REQUIRED): ISO 8601 timestamp of last record update.

**`metadata`** (object, OPTIONAL): Extensible metadata. Same semantics as envelope metadata (Section 7.7).

## 8.3. Well-Known Capability Types

The following Capability Types are defined by this specification. Implementations MAY define additional types.

| Capability Type | Description | Typical Mode |
|----------------|-------------|--------------|
| `org.ccdp.deduction` | Logical deduction, theorem proving, SMT solving | Mode 2 or 3 |
| `org.ccdp.planning` | Task planning, decomposition into action sequences | Mode 2 or 3 |
| `org.ccdp.language.generation` | Natural language generation, drafting, summarization | Mode 1 |
| `org.ccdp.language.translation` | Translation between natural languages or representations | Mode 1 or 3 |
| `org.ccdp.language.analysis` | Natural language understanding, classification, extraction | Mode 1 |
| `org.ccdp.verification` | Verification of code, proofs, plans against specifications | Mode 2 or 3 |
| `org.ccdp.selection` | Ranking, scoring, best-of-N selection | Mode 1, 2, or 3 |
| `org.ccdp.retrieval` | Information retrieval, database query, knowledge lookup | Mode 2 |
| `org.ccdp.decomposition` | Request decomposition into typed sub-requests | Mode 1 or 3 |
| `org.ccdp.human_review` | Human review, judgment, attestation | Mode 4 |
| `org.ccdp.code.generation` | Source code generation | Mode 1 or 3 |
| `org.ccdp.code.execution` | Code execution in a sandboxed environment | Mode 2 |

Custom Capability Types SHOULD use reverse-domain notation (e.g., `com.example.custom_capability`) to avoid collisions with well-known types.

## 8.4. Registry Interface

The Registry MUST support the following query operations. These are defined as logical operations, not specific API endpoints — implementations MAY expose them as REST APIs, gRPC services, function calls, or any other mechanism.

### 8.4.1. Register

Register a new Capability Record or update an existing one.

**Input:** A Capability Record.
**Behavior:** If no record exists for the given (`service_id`, `capability_type`) pair, create one. If a record exists, update it subject to schema compatibility rules (Section 8.5). If the update would break compatibility, reject it with an error.
**Output:** The stored record with server-assigned timestamps, or an error with the incompatibility details.

### 8.4.2. Lookup

Look up Services that implement a given Capability Type.

**Input:** `capability_type` (required), `status_filter` (optional, defaults to `["ACTIVE"]`), `min_provenance_grade` (optional), `max_cost` (optional), `tags` (optional).
**Output:** An array of matching Capability Records, sorted by the Dispatcher's routing preference (Section 9). Empty array if no matches.

### 8.4.3. Get

Retrieve a specific Capability Record.

**Input:** `service_id`, `capability_type`.
**Output:** The Capability Record, or an error if not found.

### 8.4.4. Deregister

Remove a Capability Record.

**Input:** `service_id`, `capability_type`.
**Behavior:** Set the record's status to `INACTIVE`. The record SHOULD be retained for audit purposes (the `registered_at` and `updated_at` fields are part of the audit trail). The record SHOULD NOT be permanently deleted.
**Output:** Confirmation, or an error if not found.

### 8.4.5. List Schema Versions

List all schema versions for a Capability Type.

**Input:** `capability_type`.
**Output:** An array of `{version, compatibility, registered_at}` entries, ordered by version.

## 8.5. Schema Versioning and Compatibility

Schema evolution is the chronic wound of typed protocols. CCDP addresses it through the Registry, which enforces compatibility rules at registration time — not at the Dispatcher, which should not need to understand schema evolution.

### 8.5.1. Versioning Model

Capability Record versions follow semantic versioning (MAJOR.MINOR.PATCH):

- **PATCH** increments indicate backward-compatible clarifications to the schema (e.g., updated descriptions, examples). The schema's structural validation rules are unchanged.
- **MINOR** increments indicate backward-compatible additions (e.g., new optional fields in the output schema). Existing consumers continue to work; new consumers can use the new fields.
- **MAJOR** increments indicate breaking changes (e.g., removed required fields, changed field types). Existing consumers will break.

### 8.5.2. Compatibility Rules

The Registry MUST enforce the following compatibility rules when a Service registers or updates a Capability Record:

**PATCH update:** The new schema MUST be semantically equivalent to the previous schema. The Registry SHOULD verify that the JSON Schema validates the same set of documents.

**MINOR update:** The new input schema MUST accept a *superset* of the documents accepted by the previous schema (backward-compatible input). The new output schema MUST produce documents that are a *superset* of the previous schema — i.e., new fields may be added, but existing fields MUST NOT be removed or have their types changed (forward-compatible output).

**MAJOR update:** No compatibility constraint. The Registry MUST retain the previous version's schema for the transition period. Services SHOULD support both the old and new versions concurrently during the transition.

### 8.5.3. Compatibility Checking

The Registry SHOULD perform structural compatibility checking at registration time. The recommended approach follows Avro's compatibility model [Kleppmann 2012]:

- **Backward compatibility** (new schema reads old data): the new input schema must accept everything the old schema accepted.
- **Forward compatibility** (old schema reads new data): the old output schema must be able to parse output produced under the new schema (by ignoring unknown fields).
- **Full compatibility** (both directions): required for MINOR updates.

Implementations MAY use JSON Schema tooling to automate compatibility checking. The Registry SHOULD reject incompatible updates with a detailed error message identifying the specific incompatibility.

### 8.5.4. Transition Period

When a Service registers a MAJOR version update, the Registry MUST support a transition period during which both the old and new versions are available. During this period:

- The old version's record has status `DEPRECATED`.
- The new version's record has status `ACTIVE`.
- The Dispatcher routes to the new version by default but MAY route to the old version if a Request's `metadata` specifies a version constraint.
- After the transition period (configured per deployment), the old version's record is set to `INACTIVE`.

## 8.6. Registry Availability

The Registry is a critical infrastructure component — if the Registry is unavailable, the Dispatcher cannot route. Implementations SHOULD address this through:

- **Caching:** The Dispatcher SHOULD cache Registry query results with a configurable TTL. Cached results allow routing to continue during brief Registry outages.
- **Staleness tolerance:** The Dispatcher SHOULD accept stale cache entries (beyond TTL) if the Registry is unreachable, with a warning logged to the audit trail.
- **Static fallback:** The Dispatcher MAY maintain a static routing table as a fallback for critical Capability Types, used when both the Registry and the cache are unavailable.

The specific availability strategy is an implementation concern, not a protocol requirement. The protocol requires only that routing decisions are logged (including whether they were made from live Registry data, cached data, or static fallback), so that the audit trail reflects the data freshness of each routing decision.
