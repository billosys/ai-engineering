# Media Path Normalization

Use this shared guide when prepared or split documents need resolvable media
references. It supports standalone indexing, reading, source review, and
analysis, and supplies upstream provenance for `concept-cards`. Keep the
[output contract](./03-output-contract.md) and [readiness reporting](./10-validation-and-reports.md)
in scope; resolving a path and verifying the depicted content are separate
checks.

## Inventory Before Rewriting

Preserve original assets and text. Inventory references and files separately,
then join them through evidence. For each reference, record its containing
input file/snapshot, original syntax/target, resolution base, resolved resource,
asset identity, proposed output file/target, and result or caveat. For assets,
record original/local path, format, size/checksum when practical, and known
dependencies. List unreferenced assets without deleting them.

Inspect inline images, reference definitions, HTML/SVG references, and
attributes or resource mechanisms actually present in the input. HTML images
can have multiple `srcset` candidates; preserve candidate descriptors and
record which variants were captured rather than replacing the whole set with
one guessed file. See [HTML image candidates](https://html.spec.whatwg.org/multipage/images.html#srcset-attributes).
If CSS, SVG, or embedded content uses further assets, record that dependency
scope and any unsupported reference syntax.

## Resolve In The Correct Context

1. Classify the reference as a local path, relative web URL, absolute URL,
   fragment, embedded data, or another observed scheme. Do not treat remote or
   embedded resources as missing local files.
2. Resolve it using its actual original context: Markdown file location, EPUB
   resource location, or captured HTML base URL. Retain the original spelling
   alongside the interpreted target, including meaningful query/fragment parts.
3. Establish the corresponding captured asset. Check full resource identity;
   matching a basename is insufficient when directories or URLs differ.
4. Compute a relative reference from each final containing output file to its
   verified local target. Moving a chapter into a different directory changes
   this calculation even if its text is otherwise unchanged.
5. Validate the emitted reference as document syntax and against the filesystem
   or intended resource. Do not confuse URL encoding with literal filename
   bytes or rewrite a fragment into part of a filename.

Keep real nested paths such as `media/media/`. Normalize only what the observed
mapping requires; do not flatten directories or add `images/` merely because
a converter often uses that shape. Already-correct references remain unchanged.
Never resolve a collision by overwriting one of two different assets.

## Preserve Meaning And Handle Ambiguity

Change the target without discarding alt text, title, dimensions, classes,
IDs, or other relevant attributes. Preserve raw HTML/SVG unless a separately
scoped transformation accounts for its content and dependencies. When target
syntax is ambiguous, leave it intact and record the limitation.

Duplicate basenames can represent different content. Equal checksums support
byte identity but do not authorize deleting originals or merging distinct
provenance. If deduplication is requested, retain a many-to-one mapping and
preserved originals. Missing assets, corrupt files, uncertain identity, and
unsupported rendering need distinct caveats. Do not substitute a plausible
image or remove its reference to make validation pass.

## Human-Assisted Operation

Request the exact reference with its surrounding syntax, the containing file
path, and a bounded asset listing for the candidate target directories. Ask
for checksums or visual inspection of named candidates when identity is
ambiguous. For a split-path issue, ask the operator to check from the actual
output location, not only from the original monolith.

Return the proposed old-to-new mapping and the checks still needed. Distinguish
operator-reported existence/appearance from direct checks; a screenshot of an
image alone does not identify its file or verify every document reference.

## Agent-Direct Operation

Inspect references and asset paths directly, compute candidate mappings, and
apply supported changes to derived text only. Record changed, unchanged,
unresolved, and unchecked references. Do not fetch uncaptured remote assets
merely to hide gaps in the supplied bundle; retain their status unless capture
is part of the authorized task.

After [splitting](./08-structure-mapping-and-splitting.md), resolve every local
reference from its containing file. Check referenced definitions remain
available and validate fragments/dependencies where applicable. Use rendering
or source comparison for identity and appearance when available, and record
the scope of those checks separately from whole-output path resolution.

## Regeneration And Handoff

Reapply a recorded mapping to a fresh copy of the preserved input rather than
repeatedly prefixing an already-normalized path. Compare output inventories,
reference counts by disposition, and identities; record any intended asset
copies or relocations. Rerunning preparation should not accumulate nested
prefixes, duplicate assets, or unexplained filename changes.

Pass the media map and unresolved caveats to the manifest and readiness report.
Successful path checks establish reference resolution, not conversion fidelity,
visual equivalence, or the truth of a figure's claims. Name which requested
uses can proceed within the observed limits and which need further inspection.
