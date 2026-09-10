# Slice Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
|---|---|---|---|---|---|---|---|
| S1 | Current source and installed descriptions are measured with scope and limitations recorded | Inventory reports and real Codex diagnostic | correctness-grade | User item 1 | done | attested: artifacts/evaluation.md and four inventory JSON files | 22 source, 20 packaged, 70 installed files; live 43 with zero shortened |
| S2 | YAML-aware checks expose per-skill and aggregate pressure through Make | Real unit tests; make check-skills; make audit-skills | correctness-grade | User item 2 | done | artifacts/test-checks.log; cdc-verification.md | 18 description tests, 18 version tests; aggregate policy is description-only |
| S3 | LLM prompt and concrete proposals are reviewable before per-edit approval; stale edits fail | Unit tests and proposal dry-run | serious | User item 3 | done | artifacts/proposal-review.log; cdc-verification.md | 15 valid, 0 unresolved, 0 applied; version-only stale edits tested |
| S4 | Usage, findings, and verification evidence are documented | Documentation and focused tests | correctness-grade | Integration | done | attested: docs/skill-description-tooling.md, artifacts/evaluation.md, package-check.log | New version gate preserved; initial transient test failure disclosed; remote CI not run |

Rows are implementation dispositions, not operator acceptance of rewrites or
independent semantic-routing verification. See cdc-verification.md for evidence
strength and the project plan's version history for this integration update.
