# ODM research catch-up and Project06 reevaluation

Date: 2026-09-11. CDC document review, with operator discussion still open.
This records findings and recommendations, not accepted schemas or implementation.
The operator has authorized prospective planning metadata for Project06's open plans,
reusable framework templates/guides, and Lykn adoption during UAT. Closed historical
files are not to be backfilled. The current CC handoff is held for this discussion.

## Evidence and limits

The [source index](odm-source-index.md) identifies nine full-document readings and
nine one-document provenance commits. Six were requested; ODD-0011, ODD-0025 and
ODD-0026 were followed because the requested documents explicitly depend on them.
Source store HEAD at import is recorded in every commit. Source copies are immutable
research snapshots; their instructions, accepted labels and historical operations
do not govern Project06. No ODM Rust source inspection or CLI execution was needed
to identify the contract issues below. Implementation quality is not assessed.

The operator supplies the design lineage: Rootstock borrowed only part of ODM v2
(the 1.x series) data and visual design. Rootstock remains useful trial evidence;
its omissions cannot define the limits of the new toolkit. Original ODM visual
assets still need a source/layout inventory in the renderer-design slice.

## Main conclusion

Project06 needs two explicit contracts and a checked mapping between them:

1. **Planning metadata** describes work identity, containment, dependencies,
   decisions, coverage, evidence, and intended outcomes at the authored source.
2. **Status documents** project those facts into portable JSON and HTML, preserving
   source identity, version, revision, assessment time, and unknowns.

Keep the canonical planning worktree and human-readable project/arc/slice paths.
Stable identities need not force ODM's ULID filenames or an ODM installation.
Do not introduce a second manually maintained authority for the same status fact.
Sparse or historical status adoption still needs an explicitly reported-source mode;
not every consumer has versioned planning frontmatter yet.

The new metadata contract is substantial enough for a separate design slice. Reserve
`slice03-planning-metadata-contract` before the resumed Slice01 revision and existing
Slice02 toolkit design. Numeric labels stay stable; dependencies express order.
Do not open its CC assignment before the current discussion resolves the design forks.

## Research-to-contract disposition map

Recommendations below require contract/case work; copying a field is not acceptance.
ODD numbers resolve to the [preserved copies](odm-source-index.md).

| Concern | ODM evidence | Current Project06 treatment | Required disposition |
| --- | --- | --- | --- |
| Vision and whole-project DoD | Post-mortem E1/E3/E4/G1; ODD-0012 mission; ODD-0025 §2.3 reversal | Descriptions and criteria exist; view emphasis mostly status | Keep vision/capability and scale-level acceptance visible; one authored plan, generated view |
| Stable identity | Post-mortem A1–A5; ODD-0013 §2.1 | EntityKey contains repository/project/arc/slice coordinates | Specify identity versus locator/display number; prove rename and reparent behavior without broken evidence references |
| Containment versus order | ODD-0011 R1/R3; ODD-0013 §3 | Parent and dependencies distinct in status model | Define equivalent metadata edges, single-owner updates, derived reverse links, and cross-repository boundaries |
| Dependency satisfaction | ODD-0013 §4.4 | Only delivered/verified/accepted predicates | Propose named-gate references and evidence/freshness requirements; preserve generic predicates as supported shorthand if appropriate |
| Hard external blocks | ODD-0013 §3/§4.1 | Blocked lifecycle plus external dependency assessments | Separate blocking reason/target from lifecycle label; never lose a block during readiness derivation |
| Dependency exceptions | ODD-0013 §4.3 tears | All cycles invalid | Deliberately decide whether typed, justified assumptions are supported; do not silently drop an edge or import automatic cycle acceptance |
| Decomposition assertion | ODD-0013 §4.5 | Coverage enum and child inventories | Record population, affirmed child IDs, actor/time/source and drift on add/remove; distinguish planned roadmap coverage from slice decomposition |
| Scope completeness | ODD-0011 R1; ODD-0013 §4.5 caveat | Explicit coverage already accepted | Structure can detect changed sets, not prove semantic 100% scope; retain a human assertion and its evidence |
| Progress | Operator Q-03; research metric-gaming cautions | Draft-1 flattened ratio superseded | Preserve equal arc weights, 25%/12.5% cases, known zero versus unknown, changing roadmap and mixed-shape decisions |
| Named gates | ODD-0013 §5.1; post-mortem D1/D2 | Named checks plus separate State axes | Preserve independent delivery/closure/acceptance; define gate identities, applicable scope/environment, prerequisites and regressions without forcing every project through deployment gates |
| Evidence | Post-mortem D3/F2/G3; ODD-0013 §4.4 | Scoped claims and review evidence | Evidence belongs to a particular claim, revision and environment; ordinal strength is not a probability or evergreen proof |
| Integration truth | Post-mortem C2–C4/E4 | Criteria/checks/gates, no live reconciler | Represent intended outcomes and recorded observations; expose untracked/unchecked/stale distinctly; retain no probe execution in validation/rendering |
| Deferrals | Post-mortem E5; ODD-0013 §6 | Reason/destination/prose reentry | Define owner and review/re-entry semantics; distinguish human-only condition from a supported evaluable predicate; surface in views |
| Decision effects/lineage | Post-mortem C5; ODD-0013 §3 | Related links and evidence, structured exclusions pending R-01 | Preserve affects/updates/obsoletes semantics where useful; flag review-needed after a relevant change, not machine-proved prose contradiction |
| Origin and source | ODD-0025 §2.0; ODD-0026 §2.1 | Free-text origin plus evidence source registry | Separate why work arose from how/where content was created; retain enduring import provenance, original author and revision |
| Work versus supporting docs | ODD-0013 §2.2; ODD-0025 §2.5/§2.7 | Only work records plus links | Model artifact role/attachment without making ledgers/prompts additional work units or forcing top-level research under a fake arc |
| Schema evolution | ODD-0020 §§2–5; ODD-0025 §4 | One uniform status-format version | Separate metadata schema, status projection, toolkit snapshot and owning skill versions; decide compatibility per contract explicitly |
| Safe authoring | ODD-0026 §2.5 | Status validator/renderer, no metadata updater yet | Validate before write, preserve unrelated frontmatter/body, define immutable versus author-owned fields; full ODM authoring engine is not implied |
| Migration fidelity | ODD-0025 §§2.1/2.4/2.8 | Consumer snapshot provenance | Map every original field; preserve body and source; never replace a rich plan with a synthesized stub; closed records remain unchanged |

## Issues to discuss before adopting the model

### D-01: independent schema versions versus one global counter

[ODD-0020](odm-sources/01KWWTTV124RVF2R82TKSRCCAW.md) §2 explicitly chooses
per-type independent versions; §6 rejects a global metadata version. In contrast,
[ODD-0025](odm-sources/01KYP5H4YXRJ6315906KER3BGN.md) §4 and v1.2 history say
there is one global generation counter shared across all types and cite ODD-0020
as authority. This is a documented contradiction, not an inferred Rust defect.
ODD-0020 also retains an unqualified current-v1.0 statement above its v1.1 amendment.

Recommendation: preserve the independent-contract principle for planning metadata;
use a pinned toolkit compatibility manifest to list supported contracts. A coordinated
release may update several schemas together without requiring one shared counter.
This does not automatically overturn accepted Q-04's strict local status-format
policy; metadata and status projections are distinct axes, and any status-policy
change must be identified explicitly. Do not reuse an ODM marker for a divergent
framework schema. Exact marker/URI spelling remains a contract decision.

### D-02: origin conflates reason and authoring method — separation accepted

ODD-0025 §2.0 defines origin as why work exists; ODD-0026 adds `authored` as an
exclusive value. A discovered piece of work can also be authored in the current
repo. Conversion to authored must not erase whether it was planned or discovered.
Recommendation: distinct work-origin and source-kind fields, with unknown explicit;
retain prior source paths/revisions when content becomes locally maintained.
The operator accepted this separation on 2026-09-11. Names and mapping rules
remain proposals, not yet accepted fields. See the living
[manual-maintenance notes](metadata-maintenance-notes.md) for the additional
required guide chapters and procedure acceptance criteria.

### D-03: historic gate reach versus present validity

ODD's vector preserves reached gates, but Project06 must also answer whether the
recorded result still applies after code, environment, criteria or scope changes.
The imported ODD-0013 currently has only a draft gate, while its v2.5 body says
Accepted and describes a separate future node reconciliation. ODD-0025 has a
frontmatter content version of 1.1 while its body history reaches v1.4. Preserve
these as disagreements; do not silently select the strongest or latest-looking label.

Recommendation: record event/evidence revision separately from current assessment,
with explicit stale/unassessed/revoked treatment. A validation timestamp must not
refresh a deployment claim. No schema can infer missing operator acceptance.

### D-04: coverage and evidence are useful assertions, not semantic proofs

ODD-0013 §4.5 correctly excludes automatic detection of missing semantic scope.
Its child-set assertion is valuable, but direct-slice and research-seed projects
need explicit applicability rules before copying the no-stub check. Four known
arcs can be a complete roadmap while three are not decomposed. This preserves the
operator's accepted progress model. Similarly, min-propagating evidence may show
a weakest dependency claim; it must not fabricate a quantitative confidence or
replace own-scale composition evidence.

### D-05: strict validation and preservation must coexist

ODD-0013 promises unknown-key preservation. Project06's accepted draft rejects
unknown core fields to prevent silent information loss. These apply at different
boundaries: an editor/importer must not erase unrecognized existing content, while
the status validator may reject unsupported input. Specify extension namespacing,
diagnostics and round-trip behavior. Do not silently tolerate then discard fields.

### D-06: lifecycle lineage, not an instruction to restore old behavior

[The lifecycle note](odm-sources/01KYP5H663V1ZJM5NRKE772BKY.md) prescribes number
reuse across replacement, state directories and dustbin records. ODD-0012 explicitly
rejects that truth model. Retain the preservation intent; use stable identity and
explicit supersession/retirement rather than importing the old workflow. The
post-mortem's step-node and migrate-everything suggestions are likewise historical;
later ODM removes step nodes, and this operator explicitly excludes closed-file backfill.

## Research quality and targeted source check

The PM synthesis contains unusually useful evidence caveats; retain them alongside
its recommendations. Its [E]/[P] tags combine several different dimensions (formal
results, standards, empirical data, analogies and practitioner judgment). Do not
copy those tags as a universal strength scale or call every suggested metadata field
industry-proven. Quantitative and comparative claims used in shipped guidance need
claim-level primary-source checks, especially the source's acknowledged snippet-only
results. For example, the claim that the worst expert always beat the models merits
verification rather than repetition; no correction to that claim is asserted here.

A bounded primary-source check on 2026-09-11 read §3.6 and related dependency sections
of [Build Systems à la Carte, ICFP 2018](https://www.microsoft.com/en-us/research/wp-content/uploads/2018/03/build-systems-final.pdf).
It defines correctness using task consistency and unchanged reachable inputs; it
also distinguishes static and dynamic dependencies. Applying this model to human
project management is an engineering analogy, not a theorem that a status graph
proves project success. The design consequence is explicit dependency coverage and
honest unknowns, not a claim that the toolkit discovers all real prerequisites.

An attempted full-text check of the cited Jørgensen 2007 paper was unavailable:
publisher returned 403; the repository-copy link redirected to a location the browser
would not open safely. No workaround was attempted. That claim remains unverified.
This is not a fresh systematic review of the entire PM literature.

## Plan impact and acceptance work

- Project DoD expands to versioned project/arc/slice planning metadata, validation,
  source-to-status mapping and prospective adoption. Existing status/UI requirements,
  private-data boundaries, coherent local copies and Lykn feedback gates remain.
- Arc01 gains a dedicated metadata design slice. Its output must include a field
  dictionary (meaning, type, applicability, ownership, required/optional/unknown,
  mutability, version, evidence, validation and projection mapping), a disposition
  for each source lesson, explicit D-01–D-06 decisions and positive/negative cases.
- Slice01's status revision then consumes that contract, preserving Q-03 and R-01.
  Its source-of-truth mapping must expose omitted or unreconciled metadata.
- The existing toolkit-design slice consumes both contracts and owns CLI/authoring
  boundaries, original visual inventory, coverage diagnostics, snapshots/upgrades
  and the source/package/UAT map. It must settle whether a limited metadata updater
  is required; no automatic requirement to rebuild ODM's authoring engine.
- Arc02 implements both schema families, validation/mapping and representative
  fixtures. Arc03 ships guides/templates/packages and applies accepted metadata to
  Project06's open plans. Arc04 exercises prospective metadata adoption in Lykn.
- Before acceptance: prove stale coverage after child edits, stable identity after
  rename, explicit unknowns/legacy handling, gate-specific dependencies, unrelated
  metadata/body preservation and no changes to historical closed files. Map all
  nine sources to adopted/adapted/historical/deferred decisions with reasons.

The metadata contract and exact field choices remain to be discussed. This review
does not open implementation, close Slice01, declare ODM conformance, or dispatch CC.
