# Validation And Readiness Report Template

Apply [validation and reports](../guides/10-validation-and-reports.md) to
observed outputs. A filled template, converter exit, file count, or successful
path check does not automatically establish readiness. See the
[HTML/Markdown example](../examples/html-markdown-handoff.md).

## Identity And Criteria

- Report ID / manifest: <id / reference>.
- Source / raw or supplied snapshot / prepared snapshot / run: <IDs>.
- Requested uses and original scope: <specific uses, content, required properties>.
- Criteria chosen before assessment: <criterion IDs and rationale for each use>.
- Operating mode / observer / report storage: <actor, direct or operator-reported
  evidence; saved path verified or draft storage unverified>.

## Check Records

Repeat for each meaningful check. Cover preservation, content/structure,
split integrity, media, locators, fidelity, capture completeness and
regeneration, or give explicit not-applicable/not-checked reasons.

| Field | Value |
| --- | --- |
| Check ID / area / criterion | <ID; required property and acceptance condition> |
| Inspected files, spans, snapshots | <exact scope> |
| Method / tool and version if known / observer | <actual procedure; direct, operator-reported, or inference> |
| Observed result / evidence pointer | <observation and retrievable log, excerpt, or record> |
| Coverage / omissions | <all enumerated items or exact samples with selection rationale; untested regions> |
| Outcome | <pass, fail, not checked, not applicable; reason for each non-pass> |
| Affected output / caveat IDs / next action | <record references and bounded resolution check> |

## Per-Use Decisions

Assess each requested use independently. Include other common uses as Not
assessed if helpful; do not silently narrow the original request.

| Use / original requested scope | Status | Criteria and check IDs supporting decision | Limitations / caveat IDs | Next action |
| --- | --- | --- | --- | --- |
| <indexing and scope> | <Ready, Caveated, Blocked, Not assessed> | <IDs and actual coverage> | <limits; state whether original request is unmet> | <action> |
| <reading/source review and scope> | <status> | <IDs> | <limits> | <action> |
| <analysis and scope> | <status> | <IDs> | <limits> | <action> |
| <concept-cards and scope> | <status> | <IDs> | <limits> | <action> |

Ready needs checks supporting the named use with no known affecting issue
within that scope. Caveated permits named limits. Blocked names a required
property still missing or unverifiable. Not assessed means no readiness
decision was made; it is not approval. These statuses concern preparation,
not truth, card evidence grading, or memory admission.

## Handoff And Follow-Up

- Prepared files / reading order: <inventory reference>.
- Structure, media and locator records: <references with same-run checks>.
- Caveats: <IDs, affected spans and effects; use the [caveat template](./caveat-record.md)>.
- Unavailable checks / tools / originals: <why unavailable and practical next step>.
- Recipient and durable delivery evidence: <locations, supplied record set,
  checked references, or explicit storage/delivery not verified>.
- Re-entry: <new inspection or repair, checks to rerun, new snapshot/run needed>.
