---
record_type: validation-result
id: null
revision: null
target_refs: []
actor: {id: null, role: null, mode: null}
created_at: null
run_refs: []
contract_ref: null
validator_identity: null
method_and_settings: null
requested_scope: null
actual_coverage: null
evidence_refs: []
validation_result: unassessed
checks: []
findings: []
warnings: []
cannot_prove: null
prior_result_refs: []
applicability: null
---

# Validation Result: <targets and structural check>

Use the [template conventions](../SKILL.md#record-templates) and
[structural validation](../guides/08-validation-verification.md#perform-structural-validation).
This record captures checks; it is not an executable validator or final schema.

## Contract, Targets And Coverage

<Identify the representation contract/checklist revision, exact target revisions,
required properties, intended scope, actual subset/sample and exclusions.
Record tool/process identity and version/settings if used, or the manual method.
Do not claim schema conformance when no accepted schema was applied.>

## Check Observations

<For each checks entry record criterion, target, evidence, observer, actual
outcome and rationale. Cover requested field/section, identity/provenance,
source/support, relationship, CQ coverage, path and lifecycle-reference checks.
Distinguish pass, fail, not checked and not applicable with reasons. Report
inaccessible inputs separately from malformed or missing required structure.
Empty checks is not a passing result.>

## Findings, Warnings And Limits

<Record findings before repair, warnings and unavailable checks with locations.
Explain what cannot_prove excludes: semantic warrant, relationship meaning,
CQ answerability, reconciliation, preservation adequacy and memory admission.
Prepared-source provenance from document-extraction is not semantic support.>

## Revision Applicability And Handoff

<Identify prior results and repaired/new target revisions, checks needing rerun
and any explicit basis for continued applicability. Preserve earlier failures.
State direct versus operator-reported observations, actual tool evidence,
remaining work and storage limits. Route semantic review to a separate
[verification result](./verification-result.md); validation is not admission.>
