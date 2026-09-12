# Arc01 Slice01 Ledger

CDC review requires Iteration 03; Iteration 02 is committed as e554d74c.
Prior CC attestations are preserved in Git; this ledger records the current reviewed state. S1-8 was added
for the operator's language preference and commit hold.

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1-1 | Inputs and released/current method identities are pinned without rewriting history | Check input register against Git, metadata and hashes | correctness-grade | Baseline continuity | open | CDC Iteration 02 review in cdc-verification.md | R4: exact prose-input identities and registration remain incomplete |
| S1-2 | Ignored workbench comparison evidence is durably preserved | Compare copied/original bytes and registered hashes | correctness-grade | Reproducible UAT | done | CDC Iteration 02 review in cdc-verification.md | Reproduced again: all 54 baseline checksum entries pass |
| S1-3 | Inventory covers available corpus frontmatter, nested shapes, failures and both v3.2 prompts | Reproduce counts/key unions; review full-prompt observations | serious | P-1 | open | CDC Iteration 02 review in cdc-verification.md | R6/R7 fixed: census/type/308-path checks reproduced; R8/R9 JSON/framing failures remain |
| S1-4 | Every discovered field and capability has an evidence-backed crosswalk disposition | Walk inventory entries to crosswalk and real values | serious | No-loss requirement | open | CDC Iteration 02 review in cdc-verification.md | R2: incomplete and sometimes incorrect semantic descriptions/dispositions |
| S1-5 | Metadata/body interactions and operator concerns are represented without a fixed schema assumption | Review crosswalk against planning brief and sample bodies | serious | Generality and body scope | open | CDC Iteration 02 review in cdc-verification.md | R2: concrete contextual evidence still required for the semantic comparison |
| S1-6 | Research agenda gives Slice02 concrete questions and acceptance probes | Trace questions to gaps and candidate primary sources | correctness-grade | Arc01 handoff | open | CDC Iteration 02 review in cdc-verification.md | R2/R4: reconcile research agenda with completed semantic families and exact inputs |
| S1-7 | Close packet is reproducible and preserves unrelated/source work | Inspect validation record, diff and per-row proposed-done report | correctness-grade | Work verification | open | CDC Iteration 02 review in cdc-verification.md | R4: documented coverage command exits 5; source clean and committed packet recognized |
| S1-8 | Helper uses approved tooling and no Ruby source enters history | Inspect Fennel implementation/dependencies and deliverables; verify empty index and unchanged planning HEAD | serious | Operator 2026-09-12 tooling preference and commit hold | done | CDC Iteration 02 review in cdc-verification.md | Fennel owns inventory logic, narrow established YAML bridge; no Ruby; commit hold released |
