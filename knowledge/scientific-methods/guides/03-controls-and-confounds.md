# Controls And Confounds

Use controls and confounds when a comparison could be explained by something
other than the variable being tested.

## Independent Variable

Name the one planned difference between conditions. Examples:

- framework version;
- prompt text;
- model;
- tool availability;
- documentation layout;
- workflow rule;
- data source.

If more than one thing changes, either split the experiment or call it a bundle
comparison.

## Controlled Constants

Hold these steady when they are not under test:

- task prompt;
- repository state;
- input files and references;
- model and reasoning setting, if possible;
- tool permissions;
- time budget or stop condition;
- output format;
- evaluation rubric;
- evaluator.

If a constant cannot be held steady, record it as a limitation.

## Common Confounds

**Contamination.** A session imports knowledge from the other condition,
installed skills, memory, prior conclusions, or operator hints.

**Order effects.** The second run benefits from what the operator learned in
the first run.

**Task drift.** Each condition receives subtly different instructions or
artifacts.

**Evaluator drift.** The scoring rubric changes after the results are known.

**Tool drift.** One condition has access to different tools, permissions,
dependencies, or network state.

**Scope drift.** One run does more work than the other and looks better because
it had a larger assignment.

## Controls Checklist

- What exactly changes?
- What exactly stays fixed?
- How will contamination be prevented?
- What could explain the result besides the variable?
- Which confounds are accepted because they cannot be controlled?
