# Comparison And Regression Testing

Use comparison and regression testing when results must show whether a change
preserved, improved, or weakened behavior.

## Compare Like With Like

Before comparing conclusions, check that the runs were actually comparable:

- same task family;
- same scope limit;
- same input artifacts;
- same allowed references;
- same output requirements;
- same stop condition or known difference;
- same evaluation rubric.

If comparability fails, report that first. The result may still be useful, but
it is no longer a clean comparison.

## Baselines

A baseline is the result a new condition must preserve or improve. Record:

- baseline version or condition;
- baseline evidence;
- behaviors expected to remain stable;
- acceptable changes;
- unacceptable regressions.

## Regression Classes

Useful regression classes:

- correctness regression;
- coverage or validation regression;
- scope-control regression;
- usability or wayfinding regression;
- evidence-quality regression;
- performance or effort regression;
- safety or compliance regression.

## Comparison Report Shape

For each measure:

- condition A result;
- condition B result;
- difference observed;
- evidence reference;
- interpretation;
- confidence and limitation.

## Comparison Checklist

- Are the runs comparable enough for the claim?
- What changed in the desired direction?
- What regressed?
- What stayed unchanged?
- Which differences are ambiguous?
- What follow-up would reduce uncertainty?
