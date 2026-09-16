# Arc06 Slice03 Ledger

All five rows are CC-attested/proposed-done; this slice accepts no new semantic
membership pairs. Independent CDC verification remains required.

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S3-1 | Evidence convention distinguishes role, identity, snapshot and live status | Inspect contract against accepted Slice01/02/12 failure modes and example inputs | correctness-grade | A6-3/A6-7 | done (CC-attested) | artifacts/evidence-replay-contract.md | CC proposed-done; CDC must reproduce; local planning evidence only; no concept-card schema adoption |
| S3-2 | Pinned authority case reproduces and rejects invalid digest/input | Run committed-byte comparisons and both controls without changing prior packets | correctness-grade | Slice02 R4 | done (CC-attested) | artifacts/worked-replay.md | CC proposed-done; CDC must reproduce; historical authority remains separate from current status |
| S3-3 | Native query case compares structured results and rejects wrong values/errors | Run exact query/tuple, reordered-key positive, wrong question, wrong ID/revision and missing-input controls | serious | Slice01/Slice02 native replay findings | done (CC-attested) | artifacts/worked-replay.md | CC proposed-done; CDC must reproduce; no invented observations or inferred answer warrant |
| S3-4 | One literal route preserves inputs and exact output scope | Execute route; inspect hashes/references, statuses, pre/committed scope and whitespace | correctness-grade | A6-7 | done (CC-attested) | artifacts/worked-replay.md; closing-report.md | CC proposed-done; CDC must reproduce; five CC output files only; no parser/helper implementation |
| S3-5 | Handoff preserves and sizes the original provenance responsibilities | Trace actor/run/preparation/shared-reference roles to Slice13 and cross-family owners | serious | A6-3/A6-6/P-15 | done (CC-attested) | artifacts/handoff.md | CC proposed-done; CDC must reproduce; all 375 remaining pairs stay owned; no semantic assignment or acceptance here |
