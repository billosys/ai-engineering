# CCDP JSON / JSON-RPC Corpus — MANIFEST

**What this is.** The complete descriptive extraction of the JSON and
JSON-RPC surface of the CCDP specification: every fenced JSON example
verbatim (`examples/`), one maximal derived instance per structure
(`canonical/`, with per-field citations in sidecar `.notes.md` files), the
flattened field and enum census (`inventory/`), and the discrepancy register
(`FINDINGS.md`). This corpus is the evidence base the future normative §7.8
JSON Schemas (ccdp-rs) will be checked against. Nothing in the spec was
altered or "improved"; discrepancies are reported, not repaired.

**Spec revision extracted against.** CCDP Draft v0.2, document version 0.2.0
(§2.1), wire protocol version `"1.0"`; README states "review iterations
through v0.2m incorporated." (The extraction assignment referred to "v0.2c" —
see FINDINGS F-29.) Source: `src/README.md` + `src/01-abstract.md` …
`src/21-version-history.md`, 22 files, newest source mtime 2026-08-05
(20-previous-versions.md).

**Extraction date.** 2026-08-05.

**Method.** All 22 section files read in full, in order (README and
02-conventions first). Fenced ```json blocks extracted mechanically and
verified byte-identical against the source (each extracted file's bytes
re-located verbatim in its section, fence counts compared per section).
Canonical instances derived by hand from the field definitions, with the
§7.3.8 per-message matrix taking precedence over prose where they conflict
(conflicts logged in FINDINGS.md). Every file in `canonical/` and
`examples/` run through a JSON parser; results below.

---

## A. Per-section extraction reconciliation

"Fences" = count of ```json fences in the source file (`grep -c '^```json'`);
"Extracted" = files under `examples/<section>/`. The two columns MUST be
equal — verified equal for every row, and every extracted file verified
byte-identical to its source block.

| Section file | Fences | Extracted | Status |
|---|---|---|---|
| README.md | 0 | 0 | — |
| 01-abstract.md | 0 | 0 | — |
| 02-conventions.md | 0 | 0 | — |
| 03-introduction.md | 0 | 0 | — |
| 04-terminology.md | 1 | 1 | ✓ reconciled |
| 05-architecture-overview.md | 0 | 0 | — |
| 06-protocol-layers.md | 0 | 0 | — |
| 07-message-format.md | 13 | 13 | ✓ reconciled |
| 08-capability-registry.md | 1 | 1 | ✓ reconciled |
| 09-routing.md | 0 | 0 | — |
| 10-provenance-grades.md | 1 | 1 | ✓ reconciled |
| 11-audit-trail.md | 6 | 6 | ✓ reconciled |
| 12-flow-control.md | 5 | 5 | ✓ reconciled |
| 13-error-handling.md | 3 | 3 | ✓ reconciled |
| 14-decomposition.md | 2 | 2 | ✓ reconciled |
| 15-security.md | 3 | 3 | ✓ reconciled |
| 16-conformance.md | 0 | 0 | — |
| 17-security-considerations.md | 0 | 0 | — |
| 18-open-questions.md | 0 | 0 | — |
| 19-references.md | 0 | 0 | — |
| 20-previous-versions.md | 0 | 0 | — |
| 21-version-history.md | 0 | 0 | — |
| **Total** | **35** | **35** | **✓ fully reconciled** |

Fence-language sweep: the sources contain only bare ``` fences (diagrams,
53 occurrences incl. closers) and ```json fences — no ```jsonc, ```json5,
indented, or otherwise-tagged JSON blocks exist to miss.

## B. Structure checklist

| Structure | Canonical file | Status |
|---|---|---|
| REQUEST message | canonical/message-request.json | derived; spec examples extracted |
| RESPONSE message | canonical/message-response.json | derived; spec examples extracted |
| ESCALATION message | canonical/message-escalation.json | derived; spec examples extracted |
| NOTIFICATION message | canonical/message-notification.json | derived; spec example extracted |
| HEALTH_REQUEST message | canonical/message-health-request.json | derived; spec example extracted |
| HEALTH_RESPONSE message | canonical/message-health-response.json | derived; spec example extracted |
| DECOMPOSITION_RESULT message | canonical/message-decomposition-result.json | derived; envelope example extracted |
| Capability Record | canonical/capability-record.json | derived (≈ §8.2.1 example + conformance metadata) |
| Decomposition Plan | canonical/decomposition-plan.json | derived (≈ §14.3 example completed) |
| Audit Record | canonical/audit-record.json | derived (richest coherent type; variants in examples/11-audit-trail/) |
| Error object | canonical/error-object.json | derived (= §13.2 example; per-code data in sidecar) |
| Registry operations | canonical/registry-ops.md | documented I/O only — **no wire binding exists in the spec** (§8.4.6, §18.5); none invented |
| Evidence Entry | embedded in provenance instances; verbatim in examples/04-terminology/001 | extracted + derived |
| Envelope common fields | embedded in every message instance | extracted + derived |
| Content wrapper / multipart | embedded; verbatim in examples/07-message-format/011–012 | extracted + derived |
| Token scope claims (informative, format-agnostic) | examples/15-security/001 only — deliberately **not** canonicalized (§15.2.2: token format not mandated) | extracted; absent from canonical by design |

Absent from spec (nothing to extract): Registry wire messages (§8.4.6),
Service/Registry stable conformance-ID tables (§18), §7.8 companion schemas
(explicitly not yet published), Dispatcher health endpoint (F-22bis),
non-HTTP transport bindings (§6.3).

## C. Validation ledger

**canonical/**: 11 of 11 JSON files parse. (Sidecar `.notes.md` files carry
the per-field citations and derived-value disclosures.)

**examples/** (35 files): 16 parse as strict JSON; 17 are non-parsing due to
`// ...` / `/* ... */` elision comments — sanctioned by §2.3, expected, not
findings; 2 are malformed-in-spec beyond elision (FINDINGS F-01):

| File | Classification |
|---|---|
| 04-terminology/001 · 07/003, 012 · 08/001 · 10/001 · 11/001 · 12/001, 003, 004, 005 · 13/001, 003 · 14/001, 002 · 15/001, 002 | parse (16) |
| 07/001–002, 004–011, 013 · 11/002–006 · 13/002 | elision-non-parsing (17) |
| 12-flow-control/002-budget-exceeded-fragment.json | **malformed-in-spec** — type-union notation (F-01) |
| 15-security/003-jcs-signing-input.json | **malformed-in-spec** — JCS pseudo-code (F-01) |

## D. Tree

```
json/
  MANIFEST.md               ← this file (entry point)
  FINDINGS.md               ← 32-entry discrepancy register (F-01 … F-31 + F-22bis)
  examples/                 ← 35 verbatim blocks, one subdir per source section
  canonical/                ← 11 derived maximal instances + .notes.md sidecars
                              + registry-ops.md
  inventory/
    fields.md               ← full field census with R/S/O and citations
    enums.md                ← 28 vocabulary groups with citations
```

## E. Reconciliation statement

All 22 source files read in full; 35/35 JSON blocks extracted and verified
byte-identical; per-section counts equal in every row; all 7 message types
plus all named structures present in `canonical/` and parsing; inventory
complete with citations; FINDINGS.md populated (32 entries). No count in
this manifest is unreconciled.
