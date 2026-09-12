# Evaluation Rubric

## Decision Question

Does the post-Arc09 rich-profile extraction produce better candidate cards for
the same CompCogNeuro subset without weakening source support discipline?

## Conditions

| Condition | Description |
| --- | --- |
| Baseline | Project05 Arc07 ten-card candidate set. |
| Rerun | This workbench ten-card candidate set using `concept-cards` 1.8.0 rich-profile guidance. |

Both conditions use the same pinned book commit and the same subset boundary.

## Scoring

Use a 0-3 score for each measure.

- 0: absent, contradicted, or worse than baseline.
- 1: present but vague, incomplete, or weakly inspectable.
- 2: useful and mostly complete, with limitations.
- 3: strong, specific, source-tethered, and review-ready.

## Measures

| Measure | What To Inspect |
| --- | --- |
| Source fidelity | Does the card preserve the source's qualifications, modality, and scope? |
| Rich profile completeness | Are all required rich-body sections present with explicit unsupported-section reasons? |
| Evidence discipline | Are claims, locators, support limits, and lifecycle boundaries distinct? |
| Concept boundary | Is the card one concept rather than a heading dump or broad summary? |
| Examples and confusions | Are source-specific examples and common errors/confusions useful without generic filler? |
| Relationships and CQs | Does the card expose useful navigation and questions without overclaiming edges or answerability? |
| Review readiness | Could an operator efficiently accept, revise, reject, or request checks? |

## Scale-Up Gate

Recommend a full-book run only if the rerun is better than the Arc07 baseline
on rich profile completeness and review readiness, and not worse on source
fidelity or evidence discipline.
