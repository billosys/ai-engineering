# Storage and preservation

Preserve a result's dependencies, not only its final figure. CERN Analysis
Preservation treats an analysis as data plus the code, workflow, configuration,
environment, and context needed to understand it. Our adaptation is an explicit
dependency trail in ordinary files and inventories.
[Source](https://analysispreservation.cern.ch/docs/general/faq.html)

## Decide what goes where

| Material | Default treatment |
| --- | --- |
| Notes, protocols, code, small inputs and observations | Version in Git with useful names and links. |
| Large or numerous captures, model weights, instrument data | Use an identified external store; retain an inventory and retrieval instructions in Git. |
| Derived tables, figures, readable exports | Retain useful reader-facing results and the exact recipe and sources that generated them. |
| Temporary caches and local environment files | Ignore only named, understood categories; document any required regeneration. |
| Restricted or nonredistributable material | Retain a permitted locator and access conditions; make unavailable evidence explicit. |

An [evidence inventory](../templates/evidence-inventory.md) records logical
identity, role, producer, acquisition time, source/location, revision, format,
size, checksum algorithm/value, access/license information, and retention owner.
Small in-repository inputs can use a compact table; expand it for external or
fragile dependencies. A checksum verifies identity against a reference value,
not correctness, authenticity, accessibility, or scientific validity.

The collection names an independent backup destination and a retrieval-check
cadence when real evidence arrives. Git hosting alone is not a complete backup
for external data, LFS objects, or local-only files. Record retrieval checks
and failures. If storage has not been provisioned, say so before a run depends
on it. Do not record a backup as existing merely because it is planned.

## Computational notebooks and mathematical work

Retain native sources and identify the authoritative file: for example, a
Maxima batch file or wxMaxima notebook, or an Octave script. Include readable
text/HTML/PDF exports where native rendering would obstruct inspection.
Exports carry their generation command, source revision, tool version, and
date; stale exports must not masquerade as current computations.

Record assumptions, units, precision, tolerances, random state, package
versions, initialization, execution order, and manual steps when relevant.
Symbolic derivations should distinguish assumptions, transformations, and
claimed identities. Numerical agreement at sampled points does not establish
a general symbolic identity. Preserve failed calculations and solver limits.

Avoid editing a live notebook to regenerate historical results in place.
Execute a copy into a new run or analysis output, then compare explicitly.

## Retirement and publication

Before pausing or retiring a lab, reconcile its indexes and inbox, identify
missing evidence, assign retention responsibility, and record the last known
retrieval state. Keep original paths or forwarding records. Record any deletion
decision and its effect on reconstructability; never clean away failed runs
just to make the collection look orderly.

A public repository's license covers only material its contributors can
license. Preserve source-specific terms in inventories. Publish the permitted
records and state access limits concretely. Storage and preservation choices
are local adaptations, not a claim of compliance with CERN institutional policy.
