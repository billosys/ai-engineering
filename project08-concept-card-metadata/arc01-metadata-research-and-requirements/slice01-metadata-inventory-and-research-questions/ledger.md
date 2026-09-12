# Arc01 Slice01 Ledger

CDC review requires Iteration 02; Iteration 01 is committed as e2ea1e68. The original seven CC attestations remain in
closing-report.md; this ledger records the current reviewed state. S1-8 was added
for the operator's language preference and commit hold.

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1-1 | Inputs and released/current method identities are pinned without rewriting history | Check input register against Git, metadata and hashes | correctness-grade | Baseline continuity | done | Attested: input-register.md and validation-evidence.md | Iteration 02 refresh records the present CompCogNeuro pin; CDC reproduction pending. |
| S1-2 | Ignored workbench comparison evidence is durably preserved | Compare copied/original bytes and registered hashes | correctness-grade | Reproducible UAT | done | Reproduced: cdc-verification.md; 54 SHA-256 manifest entries pass and both diff -rq comparisons match | 27 files total (14 rich, 13 teaching); committed in e2ea1e68; retain unchanged |
| S1-3 | Inventory covers available corpus frontmatter, nested shapes, failures and both v3.2 prompts | Reproduce counts/key unions; review full-prompt observations | serious | P-1 | done | Attested: Fennel inventory, 308-path index, validation-evidence.md | Typed parser and path assertions require CDC reproduction. |
| S1-4 | Every discovered field and capability has an evidence-backed crosswalk disposition | Walk inventory entries to crosswalk and real values | serious | No-loss requirement | done | Attested: field-dispositions.json and capability-crosswalk.md | 308 normalized paths have context evidence and observed meanings; no schema selected. |
| S1-5 | Metadata/body interactions and operator concerns are represented without a fixed schema assumption | Review crosswalk against planning brief and sample bodies | serious | Generality and body scope | done | Attested: crosswalk and field-specific operator/coverage/endpoint observations | CDC semantic sampling remains pending. |
| S1-6 | Research agenda gives Slice02 concrete questions and acceptance probes | Trace questions to gaps and candidate primary sources | correctness-grade | Arc01 handoff | done | Attested: research-agenda.md reconciled to crosswalk | Standards remain research candidates. |
| S1-7 | Close packet is reproducible and preserves unrelated/source work | Inspect validation record, diff and per-row proposed-done report | correctness-grade | Work verification | done | Attested: validation-evidence.md and revised closing report | Commit-time and prior states are explicitly distinguished. |
| S1-8 | Helper uses approved tooling and no Ruby source enters history | Inspect Fennel implementation/dependencies and deliverables; verify empty index and unchanged planning HEAD | serious | Operator 2026-09-12 tooling preference and commit hold | done | Attested: inventory-frontmatter.fnl; no Ruby source | Fennel owns framing/hash/shape/path/report/index logic; YAML::XS only parses blocks. |
