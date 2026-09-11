---
version: "1.0.0"
---

# Skill, planning-document and schema versioning

Date: 2026-09-11. Operator clarification during Project06 design discussion.
This planning note predates the new metadata schemas; no schema-conformance marker
is claimed. Its own content version above is independent of future schema adoption.

## Accepted model

| Version | What it identifies | Authority and history |
| --- | --- | --- |
| Skill/knowledge version | The complete user-facing skill, including entrypoint, guides and supporting material | The owning SKILL.md metadata.version; sibling version-history.md records changes |
| Planning-document version | One developer-facing document's evolution | The document's own version; its own in-document version history at the end |
| Schema version | A formal named contract for file metadata or dedicated data | Schema name plus semantic version uniquely identifies the contract |

The operator's current rule is that any change to a skill's owned material results
in a semantic version bump, with major/minor/micro chosen for the change. This is
stronger than older repository wording limited to significant changes; preserve it
in the implementation's maintenance-instruction reconciliation. Do not copy
repository-maintenance rules into distributed guides as end-user obligations.

Guides, templates and other skill-owned prose do not gain independent document
versions or histories. A schema's semantic version identifies the data contract,
not a competing version of the containing skill. Changing a schema in a skill
therefore affects that skill's version as well; the two values need not match.
Schema-version identifiers may occur in schemas and conforming examples without
becoming duplicated skill-version declarations. Checker design must distinguish
these cases rather than either banning valid schema markers or permitting hidden
per-guide release sequences.

An adopted planning document carries two distinct versions: its own content version
and the version of its named schema. A bare schema version such as 1.0.0 cannot
select among project-plan, ledger, prompt, or status-data contracts. Exact field
names/encoding remain to be designed; combined markers and structured name/version
pairs can both express the accepted model.

Updating document content does not itself upgrade its schema. Upgrading a schema
requires a deliberate compatibility/migration operation, not changing a marker and
assuming the data now conforms. Changing installed skills cannot rewrite vendored
consumer schemas. A document may remain valid against its pinned schema after a
new skill or schema version is published.

## Coverage correction

The earlier planning-metadata scope focused too narrowly on project/arc/slice plans.
The operator says **all planning documents** have their own versions and histories
and, upon adoption, schema-described frontmatter. Inventory plan-of-record files,
ledgers, CC prompts, closing reports, CDC verification, decisions, research, notes
and other authored planning artifacts. Define common metadata and type/role-specific
requirements; this does not require one separately named schema for every filename.
Document-role classification must not turn supporting documents into work units.

Dedicated JSON data also has a named schema/version. Whether it needs a separate
content-version field, rather than source revision/assessment/generation metadata,
has not been specified by the planning-document rule and must not be assumed.

Prospective adoption remains in force: new/authored and explicitly adopted open
planning records first; no blanket retrospective backfill of old/closed files.
The preserved ODM sources stay byte-for-byte snapshots, even where they do not
conform. The inventory/adoption report must distinguish reference snapshots from
maintained planning records so validators do not rewrite source evidence.

## Remaining decisions and recommendations

1. **Version cadence per named schema.** The clarified axes are accepted. The
   natural interpretation is independent semantic versions for each named schema,
   but the operator has not expressly settled independent versus synchronized
   increments across schema types. Recommend independent contracts, with shared
   definitions pinned and dependent schemas bumped when their effective contract
   changes. This is the remaining part of ODM discrepancy D-01.
2. **Compatibility rules.** Define major/minor/micro in terms of validation and
   reader/writer behavior, including strict unknown-field rejection. An optional
   field can preserve validity of old instances yet produce new instances an old
   reader rejects. Recommend exact schema identity in each instance, an explicit
   supported-contract inventory, and deliberate upgrades; never infer compatibility
   from major-version equality alone. Immutable published name/version identities
   and pinned shared dependencies prevent silent contract drift.
3. **Planning-document revision rules.** The operator requires own versions and
   end-of-file histories; the precise numbering/bump policy still needs defining.
   Propose semantic document versions with examples of changed commitments, additive
   detail, correction and routine status/evidence updates. Do not automatically
   reuse software-API compatibility wording without explaining its document meaning.
4. **Representation details.** Decide schema naming/namespace, exact instance fields,
   schema catalog/resolution, and which metadata is common versus document-role
   specific. These can be developed in the metadata-contract slice. Do not assign
   additional independent script/template/toolkit release sequences by assumption;
   a toolkit copy can be identified by source revision and file manifest.

The existing Q-04 uniform status-format policy must be reconciled explicitly with
these schema contracts. The accepted strict validation, local resolution and
explicit-upgrade principles remain; a single synchronized counter is not implied
by those principles alone. Preserve earlier accepted decisions unless the operator
actually changes them.

## Required manual-guide examples

- Edit planning content: update its own version/history, leave schema selection
  unchanged, validate and recheck affected evidence/status projections.
- Adopt a new schema: select the named contract, inspect changes, transform only
  the adopted record, update content version/history for the migration, validate.
- Read an older schema: distinguish supported old data from unknown/unsupported
  data; no blind restamp or silent field drop.
- Change a schema or shared definition: explain instance/consumer compatibility
  and preserve pinned contracts in existing consumer copies.
- Keep planning-document histories inside planning documents, while shipped guides
  explain the consumer procedure without acquiring their own release histories.

See [manual-maintenance notes](metadata-maintenance-notes.md) for chapter coverage
and [ODM reevaluation](odm-reevaluation.md) for source discrepancies.

## Version history

### 1.0.0 — 2026-09-11

Recorded the operator's three version axes and named-schema identity; broadened
prospective metadata coverage to all planning-document roles. Kept schema cadence,
compatibility and detailed document-bump rules explicitly open.
