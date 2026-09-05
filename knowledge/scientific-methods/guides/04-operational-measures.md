# Operational Measures

Operational measures turn the question into observable evidence. They do not
need to make every judgment numerical; they need to make evaluation stable
enough that someone else can inspect it.

## Types Of Measures

**Counts.** Number of tests, defects, missing rows, broken links, artifacts, or
accepted criteria.

**Binary gates.** Pass/fail checks such as tests, linters, build commands,
package validation, or presence/absence of files.

**Ordinal ratings.** Scales such as poor/adequate/good/excellent, with a
definition for each level.

**Qualitative findings.** Written observations with source references and
examples.

**Time or effort.** Wall-clock time, number of iterations, number of prompts,
or amount of manual intervention.

## Measure What Matters

Pick measures that connect to the decision. For a framework comparison, useful
measures might include:

- completeness of plan;
- clarity of scope and non-goals;
- contamination control;
- quality of acceptance criteria;
- implementation readiness;
- audit readiness;
- validation discipline;
- number and severity of review findings;
- amount of operator correction needed.

Avoid measures that are easy to count but irrelevant to the decision.

## Define Scoring Before Results

For any rating, define the scale before the run. A rubric should say what each
score means and what evidence supports it.

Example:

- 0: absent or contradicted by the output.
- 1: present but vague or not actionable.
- 2: actionable but incomplete or partially evidenced.
- 3: complete, specific, and supported by evidence.

## Measures Checklist

- What will be counted, checked, rated, or described?
- Are the measures defined before the run?
- Can another evaluator apply the rubric?
- Do the measures connect to the decision?
- What important quality cannot be reduced to a score?
