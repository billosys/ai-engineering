# Arc01 Slice06 Ledger

All rows start open. CC attestation is distinct from independent CDC closure.
CDC reviewed `6a6b1661` on 2026-09-13: two rows reproduced, five open.
Initial attestation remains in the CC report and Git; see cdc-verification.md.
Latest CDC review of `a416c2a2`: three rows reproduced, four open solely
for the remaining classification evidence and its integration under S6-R2.

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S6-1 | Inputs and comparison bases are exact and inspectable | Resolve registered paths/sections, hashes, versions and sample roles | correctness-grade | S4-1 | open | cdc-verification.md: Iteration 01 review | 25 registered hashes reproduced; census/dependency/historical classification evidence incomplete |
| S6-2 | Output covers exactly 37 selected pairs without overlap with accepted Batch01 | Derive expected set independently; compare sets and contextual variants | serious | S4-2 | done | cdc-verification.md: reproduced checks | CDC: exact 37, unique, in Slice01, disjoint from Batch01; not semantic acceptance |
| S6-3 | Record identities, revisions and type labels have contextual meanings and supported dispositions | Trace all kinds to definitions and available populated examples; inspect subject/target distinctions | serious | S4-3/S4-4 | done | cdc-verification.md: Iteration 01 review | CDC: current-record evidence and conditional disambiguation accepted with stated template-only limits |
| S6-4 | Legacy classification and tier comparison preserves vocabulary, pedagogy and observed anomalies | Check music/Erlang values, prompt definitions and named bodies/dependencies | serious | S4-3/S4-5 | open | cdc-verification.md: S6-R2 Iteration 01 disposition | Null/anomaly/absence distinctions improved; per-corpus vocabulary and historical comparison incomplete |
| S6-5 | Every meaning/evidence/disposition resolves and has concrete lookup or migration consequences | Inspect each contextual entry, citation and absence/equivalence claim | serious | S4-3/S4-5 | open | cdc-verification.md: Iteration 01 review | Current-record meanings accepted; remaining classification evidence must connect to dispositions |
| S6-6 | Validation and integration handoff are reproducible and complete | Run literal checks, input hashes and full seven-row close walk; inspect remainder ownership | correctness-grade | S4-6/S4-7 | open | cdc-verification.md: Iteration 01 review | Original replay fixes pass; classification query and complete input replay remain under S6-R2 |
| S6-7 | Diff preserves all source, corpus and prior evidence and follows approved tooling/commit scope | Inspect commit paths and source/prior-packet diffs, statuses and whitespace | serious | S4-8 | done | cdc-verification.md: reproduced checks | CDC: scoped six-file commit, prior packets unchanged from 285933a6, source clean |
