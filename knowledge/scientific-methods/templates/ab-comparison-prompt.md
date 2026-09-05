# A/B Comparison Prompt Template

You are participating in a controlled comparison.

## Run Setup

Run label: `<RUN_LABEL>`

Condition under test: `<CONDITION_DESCRIPTION>`

Instruction source or intervention:

`<ENTRYPOINT_OR_PROMPT_PATH>`

## Controls

- Use only the instruction source or intervention named above for the condition
  under test.
- Do not inspect or borrow from the other condition.
- Do not substitute installed, cached, remembered, newer, or older variants
  unless the protocol explicitly allows it.
- Keep the task, allowed references, tools, output format, and stop condition
  fixed unless this condition says otherwise.

## Task

`<TASK_TEXT>`

## Evidence To Report

At the start, report:

- run label;
- instruction source loaded;
- supporting files loaded;
- references used;
- assumptions made.

At the end, report:

- artifacts created or changed;
- commands/checks run;
- validation results;
- deviations from protocol;
- limitations.

## Output Format

`<OUTPUT_FORMAT>`
