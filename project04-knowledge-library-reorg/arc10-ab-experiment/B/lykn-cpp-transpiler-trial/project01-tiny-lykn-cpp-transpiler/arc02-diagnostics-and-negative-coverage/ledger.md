# Arc 02 Ledger: Diagnostics and Negative Coverage

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A02-01 | Slice 01 closes with CDC verification and adds the planned diagnostic coverage matrix without widening accepted syntax. | Inspect `slice01-diagnostic-coverage-matrix/cdc-verification.md`; compare parser acceptance against project scope. | serious | arc plan | done | `slice01-diagnostic-coverage-matrix/cdc-verification.md`; reproduced | Slice 01 CDC-closed on 2026-09-05. |
| A02-02 | Negative fixtures and tests compose into a clear diagnostic surface for later audit. | Run invalid fixture tests and inspect test names/error variant assertions after Slice 01 closes. | correctness-grade | arc plan | done | `closing-report.md`; reproduced | Arc-scale close re-ran `cargo test --test diagnostic_matrix`, full tests, and C++ smoke verification. |
| A02-03 | Arc 02 bubble-up findings are reflected in this arc plan/version history or explicitly rejected with rationale. | Compare Slice 01 close report and CDC verification against this `arc-plan.md` version history. | serious | framework ledger discipline | done | `slice01-diagnostic-coverage-matrix/cdc-verification.md`; reproduced | No arc scope or sequencing change required beyond status update. |
