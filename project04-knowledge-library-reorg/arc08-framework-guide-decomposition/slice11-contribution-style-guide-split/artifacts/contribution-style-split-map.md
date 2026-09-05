# Contribution-Style Split Map

```yaml
project: project04-knowledge-library-reorg
arc: arc08-framework-guide-decomposition
slice: slice11-contribution-style-guide-split
artifact: contribution-style-split-map
created-by: CC
created-on: 2026-09-05
```

## Accepted Target Guides

Slice11 implemented the accepted two-guide layout:

- `knowledge/contribution-style/guides/01-contribution-style.md`
- `knowledge/contribution-style/guides/02-upstream-ticket-workflow.md`

The split is semantic rather than heading-only. The first guide owns
maintainer-facing voice and contribution discipline. The second guide owns the
practical workflow for local draft artifacts, filing, line-reference checks,
blockquote headers, paste boundaries, cross-linking, one-ticket-per-problem
discipline, and template use.

## Semantic Preservation Map

| Current material | New owner | Preservation claim |
|---|---|---|
| Friendly, specific, calibrated, maintainer-owned voice | `01-contribution-style.md` | Preserved as the primary voice contract. |
| Confidence marking | `01-contribution-style.md` | Preserved as calibrated honesty. |
| Bias disclosure | `01-contribution-style.md` | Preserved as preference labelling. |
| Red-herring pre-emption | `01-contribution-style.md` | Preserved as reader-effort reduction. |
| Question tickets for unconfirmed findings | `01-contribution-style.md`, `02-upstream-ticket-workflow.md`, template | Preserved as a calibrated question/draft workflow. |
| No severity overclaim | `01-contribution-style.md` | Preserved under what to leave out. |
| No pressure on timing | `01-contribution-style.md`, `02-upstream-ticket-workflow.md` | Preserved as voice and closing discipline. |
| One ticket per problem | `02-upstream-ticket-workflow.md` | Preserved as a workflow rule. |
| Local draft locations | `02-upstream-ticket-workflow.md` | Preserved with operator-confirmed location guidance. |
| File-line reference checking | `02-upstream-ticket-workflow.md` | Preserved as a pre-filing gate. |
| Blockquote header and paste boundary | `02-upstream-ticket-workflow.md`, template | Preserved as local-header and tracker-paste guidance. |
| Cross-linking related tickets | `01-contribution-style.md`, `02-upstream-ticket-workflow.md` | Preserved as ownership-respecting cluster legibility. |
| Ticket sizing | `01-contribution-style.md`, template | Preserved as shape-specific size guidance. |
| Template role | `02-upstream-ticket-workflow.md`, template | Preserved as reusable package-local authoring shape. |

## Selective Loading

The new load order is:

1. Load `01-contribution-style.md` when the work needs maintainer-facing voice,
   calibrated claims, specificity, ownership, severity, or pressure guidance.
2. Load `02-upstream-ticket-workflow.md` when the work needs draft, filing,
   line-reference, blockquote-header, paste-boundary, cross-link, or template
   mechanics.
3. Use `templates/CONTRIBUTION-TICKET.md` when writing the actual ticket.

The split keeps external-facing voice separate from repository-local
draft/file/template workflow while preserving the original contribution-style
contract.
