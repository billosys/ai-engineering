# Reports and reconstruction

A report states what the work supports and gives the reader a route to inspect
it. Use scientific-methods for interpreting comparisons and threats to validity;
this guide addresses the record that makes that interpretation reviewable.

## Build the evidence trail

Use the [report template](../templates/report.md). For each material finding,
provide:

```text
finding -> analysis recipe/output -> run IDs -> protocol, inputs,
code, configuration, environment, and raw observations
```

Figures link to underlying values, units, selection rules, and generating
code. Record which runs were included and excluded, with reasons and the full
attempt accounting. Keep observational results, interpretation, and decisions
separate. Cite contradicting evidence and unresolved discrepancies alongside
supporting evidence.

An abandoned or inconclusive experiment still deserves a short report when
it produced useful evidence or explains a decision. Mark pre-run reports as
drafts containing no results. Do not populate them with predicted findings.

## State the reconstruction status precisely

- **Documented:** instructions and dependencies have been recorded.
- **Artifacts inspected:** a named person/session inspected identified outputs.
- **Re-executed:** a new run record demonstrates an actual rerun; state who
  performed it, the conditions, and whether it was independent.
- **Compared:** the rerun was checked against stated expectations or tolerances,
  including differences and failures.

These are descriptions of evidence, not automatic approval levels. Packaging,
checksums, and a successful command exit do not establish a finding. A rerun
by the original author is useful but does not constitute independent review.
Define the operation rather than relying on ambiguous uses of “reproducible.”

CERN's reproducibility guidance highlights preserving executable workflows
and their environments. Our profile allows a plain documented command sequence;
workflow engines such as REANA are optional, not prerequisites.
[Source](https://openscience.cern/reproducibility/)

## Revisit without contaminating the record

A future reader should be able to find the original method, retrieve its
inputs, inspect its outputs, and attempt a reconstruction in a fresh location.
Record unavailable dependencies and manual interventions. Name the comparison
criterion before judging agreement; use domain-appropriate tolerances when
byte-identical results are not expected.

Preserve the new attempt even if it contradicts the report. Add a dated report
amendment or a linked successor report explaining what changed. Update the
experiment's current summary without concealing the earlier interpretation.

End with specific remaining questions: what was not measured, what was
excluded, which alternative explanations remain, and what next observation
would discriminate between them.
