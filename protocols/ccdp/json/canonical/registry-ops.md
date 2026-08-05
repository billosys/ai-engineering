# Registry Operations — Logical Interface (§8.4)

**No wire binding exists.** §8.4 defines these as *logical operations, not
specific API endpoints*: "implementations MAY expose them as REST APIs, gRPC
services, function calls, or any other mechanism." §8.4.6 explicitly defers a
standard Registry wire protocol to a future CCDP extension, and §18.5 tracks
the question as open. Nothing below is a wire format; no JSON-RPC methods,
paths, or message envelopes are defined for the Registry, and none are
invented here.

The five operations a conforming Registry MUST support (§8.4, §16.3.1):

## 1. Register (§8.4.1)

| | |
|---|---|
| **Input** | A Capability Record (canonical/capability-record.json) |
| **Behavior** | Create if no record exists for (`service_id`, `capability_type`); else update subject to compatibility rules (§8.5). Record identity is the tuple (`service_id`, `capability_type`, `major_version`), where `major_version` is *derived* from the `version` field's major component. Records differing only in major version coexist during transitions (§8.5.4). Incompatible updates are rejected with an error. |
| **Output** | The stored record with server-assigned timestamps, or an error with incompatibility details |

## 2. Lookup (§8.4.2)

| | |
|---|---|
| **Input** | `capability_type` (required); `status_filter` (optional, default `["ACTIVE"]`); `min_provenance_grade` (optional — note the envelope-side field is named `min_policy_grade`; naming divergence logged as FINDINGS F-19); `max_cost` (optional); `tags` (optional) |
| **Behavior** | Return matching Capability Records. Sorting/ranking is the Dispatcher's job (§9.2), not the Registry's; the Registry MAY return results in any order and MAY filter on the optional parameters |
| **Output** | Array of Capability Records; empty array if no matches |

## 3. Get (§8.4.3)

| | |
|---|---|
| **Input** | `service_id`, `capability_type`, `version?` (optional; omitted → latest) |
| **Output** | The Capability Record, or an error if not found |

## 4. Deregister (§8.4.4)

| | |
|---|---|
| **Input** | `service_id`, `capability_type`, `version?` (optional; omitted → all versions) |
| **Behavior** | Set status to `INACTIVE`. Records SHOULD be retained for audit and SHOULD NOT be permanently deleted |
| **Output** | Confirmation, or an error if not found |

## 5. List Schema Versions (§8.4.5)

| | |
|---|---|
| **Input** | `capability_type`, `major_version?` (optional filter) |
| **Output** | Array of `{version, compatibility, registered_at}` entries, ordered by version. The `compatibility` value's vocabulary is never defined (§8.5.3 discusses backward/forward/full compatibility but does not bind values to this output field) — FINDINGS F-25 |

## Adjacent normative behavior (not operations)

- **Compatibility enforcement** at registration: PATCH = semantically
  equivalent; MINOR = input superset / output superset; MAJOR = no constraint
  but transition support (§8.5.2–8.5.4). The Registry MUST record whether an
  update was auto-verified or operator-attested (§8.5.3).
- **Security**: authenticated modifications, modification audit logging,
  well-formed-schema validation at registration (§15.6.3, §16.3.3).
- **Availability**: Dispatcher-side caching, staleness tolerance, static
  fallback are implementation strategies, with data-freshness logging required
  in the audit trail (§8.6).
