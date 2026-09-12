# Arc01 Slice01 Ledger

CDC review requires Iteration 01. The original seven CC attestations remain in
closing-report.md; this ledger records the current reviewed state. S1-8 was added
for the operator's language preference and commit hold.

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1-1 | Inputs and released/current method identities are pinned without rewriting history | Check input register against Git, metadata and hashes | correctness-grade | Baseline continuity | done | `attested`: revised input register pins prompts, skill, corpora and refreshed source snapshot | CDC reproduction pending. |
| S1-2 | Ignored workbench comparison evidence is durably preserved | Compare copied/original bytes and registered hashes | correctness-grade | Reproducible UAT | done | Reproduced: cdc-verification.md; 54 SHA-256 manifest entries pass and both diff -rq comparisons match | 27 files total (14 rich, 13 teaching); uncommitted; retain unchanged |
| S1-3 | Inventory covers available corpus frontmatter, nested shapes, failures and both v3.2 prompts | Reproduce counts/key unions; review full-prompt observations | serious | P-1 | done | `attested`: Fennel inventory, fixtures, corrected totals and field-path index | CDC must rerun parser. |
| S1-4 | Every discovered field and capability has an evidence-backed crosswalk disposition | Walk inventory entries to crosswalk and real values | serious | No-loss requirement | done | `attested`: 169/169 top-level and 307 path index plus readable crosswalk | Arc02 disposition decisions remain open. |
| S1-5 | Metadata/body interactions and operator concerns are represented without a fixed schema assumption | Review crosswalk against planning brief and sample bodies | serious | Generality and body scope | done | `attested`: crosswalk references v3.2 body, current references and handoff contract | No schema selected. |
| S1-6 | Research agenda gives Slice02 concrete questions and acceptance probes | Trace questions to gaps and candidate primary sources | correctness-grade | Arc01 handoff | done | `attested`: refreshed evidence/corrected populations in reports | CDC review pending. |
| S1-7 | Close packet is reproducible and preserves unrelated/source work | Inspect validation record, diff and per-row proposed-done report | correctness-grade | Work verification | done | `attested`: exact commands, fixtures, two-run determinism and no-Ruby check | Uncommitted by instruction. |
| S1-8 | Helper uses approved tooling and no Ruby source enters history | Inspect Fennel implementation/dependencies and deliverables; verify empty index and unchanged planning HEAD | serious | Operator 2026-09-12 tooling preference and commit hold | done | `attested`: Fennel helper; no `.rb` deliverable; no staging/commit | CDC must inspect helper/dependency bridge. |
