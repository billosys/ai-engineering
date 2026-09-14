# Arc01 Slice09 Ledger

CDC reviewed 6eb034a1 on 2026-09-13. S9-2/S9-7 are independently
reproduced; five criteria remain open under S9-R1/R2/R3. CC's earlier done
labels were attestation, not independent closure. The original criteria stand.

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S9-1 | Inspected definitions and concrete contexts have exact registered identities and roles | Resolve sections, all hashes, input family and baseline-copy mapping | correctness-grade | S4-1 | open | cdc-verification.md; artifacts/semantic-membership.json | R2: hashes pass, target/prior registration and exact copy mapping incomplete |
| S9-2 | Registry covers exactly 21 selected pairs with no accepted overlap | Table-derived equality, uniqueness, frozen inclusion and accepted-94 disjointness | serious | S4-2 | done (CDC reproduced) | cdc-verification.md | Exact 21 unique frozen pairs, disjoint accepted 94; 440 others |
| S9-3 | Selected fields retain actual presence, types and contextual meanings | Full 32-root selected-field census; malformed-input accounting; templates and named body samples | serious | S4-3 | open | cdc-verification.md; artifacts/semantic-evidence.md | R1/R3: full value/shape census and component meanings |
| S9-4 | Assertion and source/support linkage consequences match inspected targets | Card/claim/support trace and requested-versus-declared reference matrix | serious | S4-3/S4-5 | open | cdc-verification.md; artifacts/semantic-evidence.md | R2: rerun source targets and complete reference evidence |
| S9-5 | Every pair has evidence-backed historical/current and body/lookup consequences | Review both registry layers and named music/OTP comparisons | serious | S4-3/S4-5 | open | cdc-verification.md; artifacts/semantic-membership.json | R3: effective component definitions and concrete assertion/body comparison |
| S9-6 | Literal replay and complete handoff preserve remaining obligations | Execute every documented block; seven-row close report and 94/21/440 accounting | correctness-grade | S4-6/S4-7 | open | cdc-verification.md; artifacts/validation-evidence.md | R1: literal replay fails and omits checks; attestation needs reconciliation |
| S9-7 | Work stays scoped, input-preserving and uses approved tooling | Explicit commit files, source/prior packet checks and whitespace | serious | S4-8 | done (CDC reproduced) | cdc-verification.md; closing-report.md | Six-file scope; fixed prior-packet preservation, clean source and whitespace |
