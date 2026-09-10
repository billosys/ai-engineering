# Independent Command Evidence and Parent Review

Updated 2026-09-10 after integrating main `c8909905` and planning `361cdc6f`.
Independent context: Mencius, `01a08c8e-c8e6-7681-9cc9-64f6b6323608`.
This context was assigned mechanical evidence collection only, with no source
edits, approval decisions, design judgment or semantic-routing evaluation.
The prior verification record is preserved in artifacts/pre-sync/.

## Independently Reproduced

| Command/evidence | Result |
|---|---|
| make test-skill-tools test-skill-versions check-skills | exit 0; 18 description tests, 18 version tests; 20 source descriptions pass |
| Current project07 proposal review without --apply | exit 0; 15 valid, 0 unresolved, 0 applied |
| git diff --check | exit 0, no output |
| git diff --cached --check | exit 0, no output |
| source-inventory.json | re-read 20 skills, 9,868 description chars |
| all-source-inventory.json | re-read 22 skills, 10,598 chars |
| installed-inventory.json | re-read 70 files, 22,970 chars |
| live-catalog.json | re-read 43 skills, 0 changed, 0 removed chars |

The initial installed-validator assertion failure did not repeat in this
independent run. Its original cause remains unknown; failure evidence is in
artifacts/initial-test-checks.log. The parent strengthened diagnostic assertions
to require rejection exit1 and include stderr, without relaxing test criteria.

## Parent Review and Evidence Boundaries

The parent reviewed the conflict resolutions, current parser/replacement code,
new metadata-version regression, updated preservation fixture, workflow changes,
and current proposal validation. Make keeps both the description and upstream
version/path gates. Four original slice ledger rows map to four dispositions;
there are no dropped rows. Scope and current evidence are recorded in the
updated closing report and evaluation. No skill source descriptions changed.

The live diagnostic was rerun by the parent with approved normal cache access,
not independently rerun by the evidence collector. Package validation was also
parent-run: 22 source skills, 20 packages, zero version errors, zero hard path
failures, 529 existing-category warnings. Both workflow YAML files parsed
locally; remote CI is unverified. Documentation and architectural judgments are
parent-attested, not independent signoff.

## Bubble-Up Check

The project has one slice and no arc wrapper. Project07 and the slice plan now
record the source-only/package scope split, retained upstream version gates,
refreshed proposals and historical archive. No new implementation slice or
changes to Project05's packaging plan are required by this tooling integration.
All durable reports/proposals are under the slice artifacts directory.

Command-level claims have independent reproduction as listed. Full independent
semantic/design acceptance has not occurred and is not inferred from this
record. The project remains ready for operator review, not formally accepted.
Actual candidate approval, application, installation and skill-routing quality
assessment remain separate decisions.
