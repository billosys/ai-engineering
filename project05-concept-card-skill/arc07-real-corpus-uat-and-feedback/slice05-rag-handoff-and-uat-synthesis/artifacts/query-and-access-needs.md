# Query And Access Needs

## Design Inputs, Not Demonstrated Queries

These are downstream operator needs inferred from the UAT protocol and the
candidate-set boundary. They are not test results, supported API calls, or a
claim that any query is answerable from this candidate set.

| Need | Expected result shape | Required traceability |
| --- | --- | --- |
| Locate a candidate by concept or source wording | Candidate card plus its lifecycle state and candidate status | Original path, ID, revision, pinned snapshot, and locator |
| Inspect a claim before relying on it | Claim, boundary, qualifications, support comparison, and caveats | Source file, heading, line range, and dependency disposition |
| Separate direct support from context | Direct source span distinguished from citations, figures, and cross-chapter references | Evidence grade and the record-specific caveat |
| Review a candidate | Accept, revise, reject, or unresolved decision with rationale | Reviewer, reviewed revision/span, dependency check, and decision record |
| Explore an asserted relation or competency question | Only an explicit, source-based relation/CQ, linked to its support | Record and source basis; absence remains absence |
| Audit corpus scope | Included and excluded units, plus reasons and re-entry conditions | Coverage artifact and pinned corpus identity |

## Access Requirements

An operator or downstream reviewer needs read access to the canonical card,
its linked support record where applicable, the Slice01 corpus identity and
license handling, the prepared-source and dependency records, and the pinned
checkout or an equivalently identified reconstruction. Access to a generated
projection alone is insufficient for source review.

The later project must define authorization, update handling, attribution
display, and whether candidate records are visible outside a review workflow.
Those decisions are intentionally absent here; no MCP tool or endpoint is
defined by this artifact.

## Evaluation Prerequisite

Before choosing ranking, recall, latency, or usability metrics, a later UAT
must convert these needs into actual operator questions, a reviewed eligible
record set, an evaluation corpus snapshot, measures, and comparison protocol.
The current ten candidates provide no retrieval-quality baseline.
