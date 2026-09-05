# Evidence Capture

Use evidence capture to keep results inspectable after the conversation has
moved on.

## Preserve Raw Evidence

Capture raw outputs before writing conclusions:

- prompts and protocol text;
- run labels and timestamps;
- files loaded or inspected;
- generated artifacts;
- command outputs or summaries with exit status;
- validation logs;
- evaluator notes;
- deviations from protocol.

Summaries are useful, but they are not a substitute for the artifacts they
summarize.

## Separate Observation And Interpretation

Write observations as what happened:

- "Run A created three arcs and six slices."
- "Run B omitted the audit-readiness criterion."
- "The package validator exited 0."

Write interpretations as what the observation may mean:

- "Run B may have weaker future-audit planning."
- "This supports, but does not prove, that the new route table improved
  planning completeness."

## Evidence Strength

Use stronger language only when the evidence supports it:

- asserted: stated by a run but not checked;
- observed: visible in the artifact or transcript;
- reproduced: independently rerun or recalculated;
- reconciled: compared across sources and conflicts resolved.

## Evidence Checklist

- Where is the raw output?
- What files or artifacts prove the claim?
- What was observed versus inferred?
- What protocol deviations occurred?
- What evidence would a skeptical reviewer ask for?
