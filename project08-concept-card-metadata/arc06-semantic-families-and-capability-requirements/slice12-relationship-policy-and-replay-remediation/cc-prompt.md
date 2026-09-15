# CC: Repair Historical Relationship Policy And Search Failure Handling

You are CC executing Arc06 Slice12 in Project08. The operator approved this
bounded remediation after Slice01 Iteration 05. Do not run an old corrective
prompt, create Iteration 06, or expand this into a fresh 35-pair investigation.

## Workspace And Authority

Source checkout (read-only): /Users/oubiwann/lab/billosys/ai-engineering
Planning checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
Project: project08-concept-card-metadata
Your slice: project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice12-relationship-policy-and-replay-remediation

Use the project's standing instructions and current collaboration-framework,
project-management and work-verification routes from the source checkout.
Read project-plan.md and ledger.md, Arc06 arc-plan.md and ledger.md, then this
slice's slice-plan.md and ledger.md. Inspect both worktrees and capture the
actual opening planning HEAD and status. Preserve other processes' changes.

The current independent review is Slice01 cdc-verification.md, section
"Iteration 05 Independent Review (2026-09-14)", reviewing 30d9815c.
Its R5/R6 findings define the remainder. Read only that review section, the
affected current evidence, and the focused source passages below. Prior
iteration prompts are historical, not cumulative reading requirements.
Retrieve additional context when a specific ambiguity requires it.

## What Must Remain True

Original Slice01 retains all 35 pairs; 115 remain accepted and 405 remain
outside this assignment. Its S1-1/S1-2/S1-4/S1-5/S1-6 are independently done;
S1-3 and S1-7 stay open pending CDC recomposition. This slice adds zero pairs.
Keep the existing census, 27 registered input hashes, native expected results,
body comparisons and limits. Do not rewrite unaffected semantics.

The operator has explicitly reserved schema review and discussion of a
specification before normative design adoption (project P-15). Neither repair
chooses the future schema, required fields, spec format or migration policy.

## Step A: Rule, Observation And Applicability

Inspect the actual historical files in the planning checkout:
- old/dev/concept-cards/0010-a-guide-for-parallel-concept-card-re-extraction-v3.2.md:
  template relationship lists at 380-389, rule/quality requirements at 585-610,
  required-field quick reference at 877-893.
- old/dev/concept-cards/0009-howto-concept-card-extraction-with-claude-code-v3.2.md:
  missing-field and template-conformance instructions at 573-592.

Use headings/surrounding text to establish scope; line numbers are aids.
The review identifies explicit prerequisite requiredness plus broader
all-frontmatter/template requirements. Verify that yourself and distinguish
those rule scopes. Do not merely agree with CDC or assume that every historical
card was generated under those instructions.

Create artifacts/historical-policy-comparison.md here: one bounded comparison
for prerequisites, extends, related and contrasts_with, including their item
lists. Separate documented rule, observed census states, lineage/conformance
limits and future-policy question. Preserve absent/null/empty differences.

Correct Slice01's affected shared meanings/member dispositions, evidence report
and handoff. Do not leave a blanket "no authority establishes requiredness"
claim beside citations that establish it. Conversely, do not claim unknown
individual-card lineage, universal conformance or future requiredness as fact.
Use existing registered sources and evidence IDs; changing interpretation
does not justify changing source hashes or frozen data.

## Step B: Fail Closed On A Search Error

Repair the support search in the current Slice01 validation route so that
match, no match and search failure are distinct. Search failure must make
the replay return nonzero, not produce the expected unavailable-support result.

Exercise the same lookup logic with:
- A successful match.
- A genuine successful search with no match.
- An injected exit-2 error.

Any temporary control fixture is synthetic and separate from corpus evidence.
Use an isolated temporary directory if needed, and record/clean only your own
fixtures. Capture actual command statuses. A blanket "! command" is not enough
to distinguish the intended mismatch from a tool error. Do not catch every
failure and report success.

Preserve all four existing native cases and the wrong-target/revision controls.
Keep query-cases.json unchanged; no expected-result edits to accommodate the
repair. Retain the bounded unavailable-support outcome on the real no-match
case without claiming global absence or source truth.

Publish one clearly designated current route in Slice01 validation-evidence.md,
reusing accepted checks with the repaired lookup and current scope/preservation
tail. Retain earlier recipes as explicitly historical, not alternative current
instructions. Include CDC's supplementary exact-reference/edge projections
with attribution, not as newly discovered CC semantics.

Record execution/results and literal route invocation in this slice's
artifacts/validation-evidence.md. Run from the declared cwd and capture output
and exit status. Reproduce all 27 registered hashes, exact 35-pair accounting,
the accepted full census/mapping checks, four native comparisons, projections
and controls. Use the frozen structured inventory, not ad hoc YAML parsing.

Keep fixed historical Git comparisons separate from current preservation:
compare the untouched Arc01/frozen inputs, project artifacts and other protected
paths with your actual opening planning HEAD. Later CDC changes are not your
commit scope. Replace the obsolete seven-file current-scope check with the
eight authorized files below, using explicit before/after endpoints for the
committed review. Preserve no-op/unavailable/error distinctions in the report.

## Files You May Change

Exactly these eight output paths are authorized, relative to planning root:

- project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice01-relationship-semantics-and-traversal/artifacts/semantic-membership.json
- project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice01-relationship-semantics-and-traversal/artifacts/semantic-evidence.md
- project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice01-relationship-semantics-and-traversal/artifacts/handoff.md
- project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice01-relationship-semantics-and-traversal/artifacts/validation-evidence.md
- project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice12-relationship-policy-and-replay-remediation/artifacts/historical-policy-comparison.md
- project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice12-relationship-policy-and-replay-remediation/artifacts/validation-evidence.md
- project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice12-relationship-policy-and-replay-remediation/ledger.md
- project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice12-relationship-policy-and-replay-remediation/closing-report.md

The four Slice01 artifact repairs are an explicit cross-slice output exception:
repair that original packet rather than create a competing registry. New
comparison, execution evidence and attestation belong in Slice12.

Do not edit Slice01's ledger, closing report, CDC review, query-cases.json,
plans or old iteration prompts. Do not create this slice's cdc-verification.md.
Do not edit source skills, packages, installed skills, corpora or accepted
baseline files. No new custom script/parser, Ruby or Python.

## Closure And Commit

Walk S12-1 through S12-4 in your own closing-report.md, with evidence strength,
limitations, actual checks and their outcomes. Map R5 repair to original S1-3,
R6 repair to S1-7, and explicitly retain the five done original rows.
Your result is CC proposed-done. CDC decides independent Slice12 closure and
original Slice01 recomposition before Slice02 can open.

Stop with a concrete sized finding if the two fixes expose wider work; do not
weaken criteria or expand the schema investigation. Record actual model/effort
and compaction only if available; otherwise say unknown. Do not change settings.

Run JSON checks, the complete declared current replay, deterministic controls,
preservation checks and whitespace checks. Package gates are inapplicable:
this is planning/evidence repair, not a source skill change.

Commit only the named outputs after inspecting staged scope. From planning cwd:

```bash
git add -- \
  project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice01-relationship-semantics-and-traversal/artifacts/semantic-membership.json \
  project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice01-relationship-semantics-and-traversal/artifacts/semantic-evidence.md \
  project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice01-relationship-semantics-and-traversal/artifacts/handoff.md \
  project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice01-relationship-semantics-and-traversal/artifacts/validation-evidence.md \
  project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice12-relationship-policy-and-replay-remediation/artifacts/historical-policy-comparison.md \
  project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice12-relationship-policy-and-replay-remediation/artifacts/validation-evidence.md \
  project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice12-relationship-policy-and-replay-remediation/ledger.md \
  project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice12-relationship-policy-and-replay-remediation/closing-report.md
git diff --cached --name-only
git diff --cached --check
git commit --only \
  -m "plan(project08): repair relationship policy and search evidence" \
  -m "Co-authored-by: Codex <noreply@openai.com>" \
  -m "Co-authored-by: Billo AI <ai-engineering@billo.systems>" -- \
  project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice01-relationship-semantics-and-traversal/artifacts/semantic-membership.json \
  project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice01-relationship-semantics-and-traversal/artifacts/semantic-evidence.md \
  project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice01-relationship-semantics-and-traversal/artifacts/handoff.md \
  project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice01-relationship-semantics-and-traversal/artifacts/validation-evidence.md \
  project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice12-relationship-policy-and-replay-remediation/artifacts/historical-policy-comparison.md \
  project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice12-relationship-policy-and-replay-remediation/artifacts/validation-evidence.md \
  project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice12-relationship-policy-and-replay-remediation/ledger.md \
  project08-concept-card-metadata/arc06-semantic-families-and-capability-requirements/slice12-relationship-policy-and-replay-remediation/closing-report.md
```

Do not use directory pathspecs, globs, git add ., commit -a or unrelated staged
files. Report the commit, repaired findings, validations, remaining limitations
and CC proposed-done status. Do not open or execute downstream work.
