# Slice01 Handoff

CC proposes 35 relationship meanings only. Preserve list orientation and
edge-support distinctions. Predicate naming, target anchors, revisions and
reciprocal storage remain architecture questions.

For the next Arc06 work, retain these interface facts: legacy typed lists are
relationship assertions and support reader navigation, but are not independently
identified current edge records; `from_ref`/`to_ref` validity is not edge
support; `source_support_refs` is edge-scoped; and `symmetry` or an
inverse reading does not require a second stored edge. The 405 other frozen
pairs are outside this assignment, not accepted coverage. Slice02 should use
the four preserved query cases to size CQ behavior; later research should
decide predicate-name migration and explicit target-anchor/revision policy.

The migration reader must preserve historical `contrasts_with` as commonly
confused concepts, rather than silently replacing it with the current guide's
qualified comparison. A resolver can expose legacy assertions and bounded
filename results while separately reporting missing revision, warrant and
support-path components.
