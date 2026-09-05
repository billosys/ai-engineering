# Experiment Design

Use experiment design to choose the comparison shape before the work starts.
The design should be just strong enough for the decision being made.

## Common Designs

**A/B comparison.** Two conditions receive the same task. Use when comparing
prompts, framework versions, tool settings, documentation layouts, or process
changes.

**Baseline/regression trial.** A current result is compared against a known
baseline. Use when deciding whether a change preserved, improved, or weakened
behavior.

**Ablation.** Remove one component while holding the rest steady. Use when
testing whether a guide, prompt section, tool, data source, or process step is
actually load-bearing.

**Before/after.** Run the same task before and after a change. Use when exact
parallel conditions are not practical, but watch for order effects and memory
contamination.

**Case series.** Run several bounded examples and look for repeated patterns.
Use when the task is too varied for one example to carry the conclusion.

## Define Conditions

Each condition needs:

- label;
- instruction source or intervention;
- task input;
- allowed tools and references;
- output format;
- stop condition;
- evidence to preserve.

## Sequence The Work

Choose an order that reduces bias:

- Prefer parallel or independent sessions when comparing LLM behavior.
- If one person must run both conditions, blind the expected result where
  possible.
- If order cannot be balanced, record the order as a limitation.
- Keep setup text identical except for the planned variable.

## Keep The Trial Small

Design the smallest task that still creates observable evidence. For software
work, "tiny but real" is often ideal: enough planning, implementation, tests,
and review surface to compare behavior without turning the experiment into the
main project.

## Design Checklist

- What design type is this?
- What is the independent variable?
- What is held constant?
- What evidence will each condition produce?
- What is the stop condition?
- What would make the comparison unfair?
