# Arc01 Slice09 Ledger

CDC reviewed 0aeaf507 on 2026-09-13. Five criteria are independently
reproduced; only S9-1/S9-6 remain open under residual R1/R2. R3 is resolved.
All original criteria and parent obligations remain unchanged.

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S9-1 | Inspected definitions and concrete contexts have exact registered identities and roles | Resolve sections, all hashes, input family and baseline-copy mapping | correctness-grade | S4-1 | open | cdc-verification.md | R2 remainder: both mapping manifests need registered identities; 19 existing hashes and mapping pass |
| S9-2 | Registry covers exactly 21 selected pairs with no accepted overlap | Table-derived equality, uniqueness, frozen inclusion and accepted-94 disjointness | serious | S4-2 | done (CDC reproduced) | cdc-verification.md | Exact 21 unique frozen pairs, disjoint accepted 94; 440 others |
| S9-3 | Selected fields retain actual presence, types and contextual meanings | Full 32-root selected-field census; malformed-input accounting; templates and named body samples | serious | S4-3 | done (CDC reproduced) | cdc-verification.md | Full 224-row presence/value/shape/path census and three parse limitations |
| S9-4 | Assertion and source/support linkage consequences match inspected targets | Card/claim/support trace and requested-versus-declared reference matrix | serious | S4-3/S4-5 | done (CDC reproduced) | cdc-verification.md | Pilot/rerun source target and embedded-heading limitations independently inspected |
| S9-5 | Every pair has evidence-backed historical/current and body/lookup consequences | Review both registry layers and named music/OTP comparisons | serious | S4-3/S4-5 | done (CDC reproduced) | cdc-verification.md | R3 resolved: effective component meanings and concrete historical assertions |
| S9-6 | Literal replay and complete handoff preserve remaining obligations | Execute every documented block; seven-row close report and 94/21/440 accounting | correctness-grade | S4-6/S4-7 | open | cdc-verification.md | R1 remainder: cited-section reads and scoped repair-preservation replay |
| S9-7 | Work stays scoped, input-preserving and uses approved tooling | Explicit commit files, source/prior packet checks and whitespace | serious | S4-8 | done (CDC reproduced) | cdc-verification.md | Six-file repair scope and fixed b905290c-to-0aeaf507 prior-packet preservation |
