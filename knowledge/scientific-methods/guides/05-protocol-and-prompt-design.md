# Protocol And Prompt Design

Use protocol and prompt design when another person or LLM session must run the
same procedure without hidden context.

## Protocol Contents

A practical protocol includes:

- purpose;
- run label;
- condition or intervention;
- exact input artifacts;
- allowed references and tools;
- disallowed references and contamination boundaries;
- task instructions;
- output format;
- evidence to capture;
- validation commands or checks;
- stop condition;
- reporting format.

## Prompt Discipline

For LLM experiments:

- Put run-specific variables in a small setup section.
- Keep task text identical across conditions except for the independent
  variable.
- Require the session to list files, references, assumptions, and tools used.
- State what not to use, especially installed skills, memory, or other
  condition outputs when those would contaminate the result.
- Ask for artifacts that can be inspected later, not only a conversational
  summary.

## Avoid Leading The Result

Do not tell a run which condition is expected to win. If the operator must know
the hypothesis, keep it out of the prompt unless the hypothesis itself is part
of the tested intervention.

## Protocol Checklist

- Could a fresh session run this without asking what was meant?
- Is the independent variable isolated?
- Are allowed and disallowed references explicit?
- Is the output format inspectable?
- Does the prompt preserve enough evidence for later analysis?
