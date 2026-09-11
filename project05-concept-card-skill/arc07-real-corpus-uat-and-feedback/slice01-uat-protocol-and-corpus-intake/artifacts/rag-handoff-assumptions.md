# Retrieval And Graph Handoff Assumptions

## Purpose

This document names the minimum information a later retrieval, graph, or MCP
projection would need from the pilot. It does not authorize, design, or
implement any runtime component.

## Minimum Projection Inputs

| Input | Required boundary |
| --- | --- |
| Corpus identity | Repository URL, pinned commit, license, attribution information, preparation manifest, and caveats travel with every projected item. |
| Record identity | Stable record IDs and a separate lifecycle/review state are retained; neither is inferred from vector similarity. |
| Claim and support | Claim text, exact source locator, evidence role, qualifications, and unresolved dependencies remain inspectable. |
| Relationships | Typed links retain their source basis and do not turn proximity or co-occurrence into an asserted relation. |
| Competency questions | Questions remain linked to the record(s) and support that justify them. |
| Review provenance | Operator decisions, revisions, rejections, and unresolved items remain distinguishable from independent verification. |

The projected representation may add chunks, embeddings, index identifiers, or
transport metadata later, but it may not replace claim-level source support
with those operational fields.

## Downstream Query Expectations

A future retrieval or graph evaluation should define real operator questions
before choosing retrieval metrics. At minimum, it should test whether results:

1. return a claim with its source locator and qualifications;
2. distinguish direct support from contextual citations, cross-references, and
   uninspected figures; and
3. let an operator trace a proposed relationship or competency question back to
   the reviewed record and source basis.

Those questions are handoff criteria, not evidence that retrieval works. Any
recall, ranking, latency, or usability conclusion requires a separate runtime
evaluation with its own corpus snapshot and measures.

## Explicit Runtime Boundary

Project05 Slice01 creates no graph database, GraphRAG flow, vector database,
embedding pipeline, retrieval endpoint, ingestion service, MCP server or tool,
or memory-store write. Concept cards remain source and review artifacts; graphs
and MCP resources are downstream projections. They must retain record IDs and
provenance rather than becoming a replacement source of truth.

## Re-entry Criteria

Before a later project crosses the runtime boundary, it should have the actual
corpus preparation evidence, reviewed record set, unresolved-dependency list,
projection schema, operator retrieval questions, and an explicit decision about
admission/retention. Missing any of these is a reason to return to corpus
preparation or record review, not to infer readiness from the existence of this
handoff note.
