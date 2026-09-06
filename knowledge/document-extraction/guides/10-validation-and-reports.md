# Validation And Reports

Use this guide to make a prepared-source handoff inspectable for standalone
indexing, reading, source review, analysis, and downstream `concept-cards`
upstream provenance. Apply the [output contract](./03-output-contract.md);
records can be separate files or linked sections of one durable report.
Use the live [manifest](../templates/manifest.md),
[validation/readiness](../templates/validation-readiness.md) and
[caveat](../templates/caveat-record.md) templates, with the remaining
[templates and representative examples](../SKILL.md#templates-and-examples).
Fill observations and explicit unknowns rather than copying synthetic example
results as evidence. The optional
[concept-card handoff](../templates/concept-card-handoff.md) carries these
records to a requested downstream consumer.

## Assemble The Manifest

Record source, snapshot, and run IDs; raw/captured input paths and formats;
capture/conversion lineage and known settings; checksums where practical;
derived file inventory and reading order; normalization/manual edits; and
evidence-home paths. Identify unavailable originals, unknown tool versions,
and partial captures explicitly. Keep preserved inputs and prior runs intact.

Link the manifest to the [structure map](./08-structure-mapping-and-splitting.md),
[media records](./07-media-path-normalization.md),
[locator records](./09-locator-model.md), validation observations, caveats, and
per-use readiness decisions. Check that these references resolve to the same
run/snapshot. A record category may be inapplicable, but must have a reason;
missing, empty, unchecked, and successfully verified are different outcomes.

## Define And Perform Checks

Choose checks against the requested use and captured scope before assigning
readiness. For each, record the criterion, files/regions tested, method/tool
or observer, observed result, coverage, and evidence pointer. Use pass, fail,
not checked, or not applicable with a reason; do not turn unavailable checks
into passes. Separate direct inspection, operator reports, and inference.

| Area | Check and report |
| --- | --- |
| Preservation/identity | Raw and conversion inputs remain identifiable and unchanged; manifest paths, checksums if recorded, and snapshot/run associations agree. |
| Content/structure | Accepted spans cover intended content in order; front/back matter and unnumbered sections accounted for; omissions, overlap, and intentional duplication named. |
| Split integrity | Complete containers and definitions survive; metadata and original headings preserved; output names unique and map to intended units. |
| Media | References resolve from each output file; nested paths and attributes retained; asset identity/appearance checks distinguished from existence checks. |
| Locators | Types/bases explicit; targets exist in the named snapshot; source/output mappings checked with scope and ambiguous bases retained. |
| Conversion fidelity | Representative text, code, math, tables, figures, OCR, and reading order compared with available originals; damage and unchecked regions listed. |
| Capture completeness | Dynamic, paginated, embedded, or externally loaded material accounted for within the declared capture scope, including unavailable states. |
| Regeneration | Derived output produced from preserved inputs with recorded transformations; changed content, mappings, or settings identified rather than overwritten. |

Use whole-output checks for enumerated files/references where practical, plus
targeted source comparisons for fidelity. Record sampling locations and why
they cover the suspected risks; a sample cannot certify uninspected content.
Failed checks should point to the affected output and a reproducible next
inspection or repair. These are guidance-level checks, not a claim that an
executable validator ships with this skill.

## Caveat Records

Give each caveat a stable ID, category, affected source/output spans or files,
evidence/observation, current handling, downstream impact, and resolution or
re-entry check. Useful categories include:

- identity/lineage: missing original, uncertain edition, unknown converter;
- capture: omitted dynamic state, pagination, or embedded resources;
- structure: duplicate headings, missing sections, uncertain boundaries;
- media: missing, duplicate/ambiguous, corrupt, or unchecked assets;
- locator: unknown page basis, broken/duplicate anchor, ambiguous fragment,
  or snapshot/line-number drift;
- fidelity: OCR damage, layout/order loss, table/code/math conversion loss,
  unsupported HTML/SVG, or cropped/mismatched images;
- verification coverage: unavailable tools or only sampled comparisons.

Attach caveats to the records they affect, not only to a global summary. On
resolution, retain the old observation and record what evidence changed the
disposition. A later reader must be able to distinguish resolved damage from
an uncertainty that was merely omitted from a new report.

## Decide Readiness Per Use

Use the output contract's statuses for each requested use and scope:

| Status | Required justification |
| --- | --- |
| Ready | Relevant checks support the named use; no unresolved issue known to affect that use within the assessed scope. State the actual coverage. |
| Caveated | Use can proceed within specified limits; name excluded/affected content and implications. |
| Blocked | A required property is missing or unverifiable; name the required next check or repair. |
| Not assessed | This run did not evaluate that use; do not imply approval by omission. |

Judge indexing, reading/source review, analysis, and concept-card extraction
separately. An indexing task may require complete coverage and stable section
keys; reading may tolerate an unsplit document; analysis of a table depends
on its fidelity; provenance-bearing extraction may require verified source
locators. Derive requirements from the actual task, not a fixed rule that one
consumer is always less demanding.

There is no automatic readiness transition from converter exit status, file
creation, matching counts, successful path checks, or finishing this guide.
Do not silently narrow the requested scope to manufacture Ready. When a
limited scope is the only supported result, state that limit and assess the
original request accordingly. Source readability does not validate its claims;
preparation does not grade card evidence or authorize memory admission.

## Human-Assisted Operation

Ask for the specific evidence missing from a decision: an output inventory,
named failed reference, source/output excerpt pair, page/anchor spot check,
or screenshot of a damaged table or figure. Explain which criterion it tests.
Label results supplied by the operator and retain unverified coverage limits.

Provide report contents and intended evidence paths when unable to write
files. State that saving or checking those files remains unverified. Do not
call a draft report a durable handoff until its storage is established.

## Agent-Direct Operation

Inspect accessible generated files and preserved inputs; perform the relevant
checks and write observations, manifest, caveats, and readiness decisions to
the accepted evidence home. Re-open reports and follow their record/file
references, checking that all point to the intended snapshot. Capture failed
checks as evidence before repairing and rerunning affected checks.

Do not re-run conversion or broaden capture merely to avoid reporting an
unavailable check. Stop affected transformations when evidence is insufficient,
preserve current outputs, and name the next bounded action. Continue unrelated
checks whose inputs and criteria are available.

## Final Handoff

Report prepared file locations and reading order, source/snapshot/run IDs,
manifest and record paths, per-use statuses, unresolved caveats, coverage, and
next actions. Confirm that downstream consumers receive caveats with the
affected spans rather than only extracted text. Retain previous run reports;
regeneration produces a new record of what was checked, not a retroactive
upgrade of an earlier result. Hand off to `concept-cards` only when requested
and available; the same evidence is usable for standalone document work.
