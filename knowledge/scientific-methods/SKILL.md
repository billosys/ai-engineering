---
name: scientific-methods
description: |
  Method skill for practical scientific inquiry, experiment planning, controlled
  comparisons, regression tests, evaluation rubrics, evidence capture, and
  threats-to-validity analysis. Use when a conversation asks to test whether a
  change helped, compare versions or prompts, design an A/B trial, make an
  investigation more rigorous, define operational measures, or turn a fuzzy
  question into an inspectable protocol. Not for ordinary implementation unless
  the work needs explicit experimental design.
version: 1.0.0
license: MIT
metadata:
  hermes:
    tags: [scientific-method, experiments, evaluation, ab-testing, regression, evidence]
    category: method-skills
---

# Scientific Methods

Use this skill when the work needs practical scientific discipline: a question
turned into a testable claim, a comparison made fair, an evaluation made
inspectable, or a result kept honest about its limits.

The skill is intentionally lightweight. It is for working sessions, prompt and
framework trials, software behavior comparisons, process experiments, teaching
studies, and other cases where self-deception is easy because the evidence is
messy. It is not a demand for academic ceremony.

## Trigger Signals

Load this skill when the user asks to:

- compare version A with version B;
- test whether a change improved or regressed behavior;
- make a prompt, framework, tool, process, or workflow evaluation more
  scientific;
- design an experiment, trial, benchmark, rubric, or A/B comparison;
- identify controls, confounds, variables, operational measures, or threats to
  validity;
- evaluate LLM behavior under multiple conditions;
- create a reproducible protocol for another session to run;
- separate observation, interpretation, and conclusion.

Do not load it for ordinary coding, documentation, or planning unless the task
explicitly needs experiment design or evidence comparison.

## Core Pattern

The method has seven moves:

1. Frame the inquiry as a question and a provisional claim.
2. Identify what changes and what must stay fixed.
3. Define observable measures before running the trial.
4. Write a protocol that another session can follow without hidden context.
5. Capture evidence as raw observations plus provenance.
6. Compare results against the predeclared measures.
7. State conclusions with limitations and next tests.

## Guide Routing

Read only what the current inquiry needs:

- [Inquiry Framing](./guides/01-inquiry-framing.md) - turn a fuzzy question
  into testable claims, scope, and decision use.
- [Experiment Design](./guides/02-experiment-design.md) - choose comparison
  shape, conditions, tasks, sampling, and execution sequence.
- [Controls And Confounds](./guides/03-controls-and-confounds.md) - isolate the
  independent variable and name likely contamination.
- [Operational Measures](./guides/04-operational-measures.md) - define what
  will be observed, counted, scored, or judged.
- [Protocol And Prompt Design](./guides/05-protocol-and-prompt-design.md) -
  write reproducible instructions for humans or LLM sessions.
- [Evidence Capture](./guides/06-evidence-capture.md) - record provenance, raw
  results, observations, and audit trails.
- [Comparison And Regression Testing](./guides/07-comparison-and-regression-testing.md)
  - compare outputs, detect regressions, and preserve baselines.
- [Analysis And Threats To Validity](./guides/08-analysis-and-threats-to-validity.md)
  - distinguish results, interpretation, limitations, and follow-up tests.
- [Anti-Patterns](./guides/09-anti-patterns.md) - catch common ways an
  experiment becomes theater instead of evidence.

Templates:

- [Experiment Protocol](./templates/experiment-protocol.md)
- [A/B Comparison Prompt](./templates/ab-comparison-prompt.md)
- [Evaluation Rubric](./templates/evaluation-rubric.md)

Version history:

- [Version History](./version-history.md)

## Minimum Useful Protocol

For a small experiment, capture at least:

- research question;
- decision the result is meant to inform;
- compared conditions;
- independent variable;
- controlled constants;
- task or stimulus;
- evidence to collect;
- scoring rubric or qualitative review criteria;
- known confounds and limitations;
- stop condition.

If those fields are missing, the result can still be useful exploration, but
do not call it a controlled comparison.

## LLM And Prompt Experiments

For LLM-facing tests, be especially strict about contamination:

- Use the same task, input artifacts, permissions, tools, and output format
  across conditions unless the difference is the variable under test.
- Pin the instruction source being tested, such as a prompt, skill, framework
  entrypoint, branch, or version.
- Tell each run not to borrow from the other condition, remembered conclusions,
  or installed alternatives unless that is intentionally part of the test.
- Record what the session actually loaded and what assumptions it made.
- Prefer shallow-but-real work over broad theater. A bounded implementation or
  review often yields better evidence than an ambitious simulated project.

## Using With Collaboration Framework

This skill composes well with the collaboration framework:

- Use collaboration-framework for project/arc/slice planning, ledgered
  execution, and independent verification.
- Use scientific-methods when the work itself is an experiment, comparison, or
  regression assessment.
- Use domain/tooling skills for the subject matter being tested.

Keep the layers distinct. The collaboration framework governs the engineering
work; this skill governs the inquiry design used to compare evidence.
