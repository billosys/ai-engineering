# Worked contract acceptance cases

Revision notice, 2026-09-10: these draft-1 cases remain the reviewed historical
baseline. The [operator's progress decision](progress-decision.md) supersedes
flattened slice-based headline project progress and requires revised/expanded
cases. Do not implement the old numeric expectations without that revision.

Date: 2026-09-06. Candidate for [status-contract.md](status-contract.md), draft 1.
These are design examples and expected outcomes, not executable toolkit tests.
Only fictional repository/work content appears in the JSON. The Lykn table
records structural observations separately; it is not consumer status data.
[Verification record](verification-record.md) distinguishes author checks from
future schema, renderer and independent acceptance gates.

## C-01: Complete mixed hierarchy, sparse page adoption

The virtual status tree below has three documents and two leaf slices. Assume
the three named vendored schema files and the three planning source targets
exist in its virtual planning checkout. No runtime/schema implementation exists
yet. Each JSON block is a whole input document, not a fragment.

Expected: valid candidate data, with coverage warnings for unassessed closure
criteria if displayed. Saga View and project show **1/2 slices reported delivered,
50%**. Arc shows **1/1, 100% reported delivered**, six pending named gates and an
open finding; it remains active, closure open, acceptance pending. The direct
slice appears under the project without an arc or slice page. No count or pip
upgrades any parent to verified/accepted. Child array order is preserved.

### Input `status.json`

```json
{
  "$schema": "schemas/status.schema.json",
  "format_version": "1.0.0",
  "kind": "collection",
  "repository": {
    "id": "example",
    "name": "Example Catalog"
  },
  "as_of": "2026-09-06T12:00:00Z",
  "sources": [
    {
      "id": "plan",
      "kind": "planning",
      "label": "Fictional planning record",
      "locator": {
        "path": "README.md"
      }
    }
  ],
  "evidence": [],
  "entity": {
    "id": "example",
    "kind": "collection",
    "title": "example",
    "parent": null,
    "description": "All projects in the Example Catalog repository.",
    "source_refs": [
      "plan"
    ],
    "children": {
      "coverage": "complete",
      "scope": "All currently planned immediate units in the fictional snapshot.",
      "source_refs": [
        "plan"
      ],
      "items": [
        {
          "id": "project01-catalog",
          "kind": "project",
          "detail": "project01-catalog/project-status.json"
        }
      ]
    },
    "progress": {
      "mode": "computed",
      "coverage": "complete",
      "scope": "All current descendant slices."
    }
  }
}
```

### Input `project01-catalog/project-status.json`

```json
{
  "$schema": "../schemas/project-status.schema.json",
  "format_version": "1.0.0",
  "kind": "project",
  "repository": {
    "id": "example",
    "name": "Example Catalog"
  },
  "as_of": "2026-09-06T12:00:00Z",
  "sources": [
    {
      "id": "plan",
      "kind": "planning",
      "label": "Fictional planning record",
      "locator": {
        "path": "project01-catalog/project-plan.md"
      }
    }
  ],
  "evidence": [],
  "entity": {
    "id": "project01-catalog",
    "kind": "project",
    "title": "project01-catalog",
    "parent": {
      "repository": "example",
      "project": null,
      "arc": null,
      "slice": null
    },
    "description": "Make a small searchable catalog.",
    "source_refs": [
      "plan"
    ],
    "state": {
      "lifecycle": "active",
      "delivery": "in-progress",
      "closure": "open",
      "acceptance": "pending",
      "reported_label": "active",
      "note": "Fictional authored assessment; independent acceptance remains pending.",
      "evidence_refs": [],
      "criteria": [],
      "criteria_coverage": "unknown"
    },
    "children": {
      "coverage": "complete",
      "scope": "All currently planned immediate units in the fictional snapshot.",
      "source_refs": [
        "plan"
      ],
      "items": [
        {
          "id": "arc01-index",
          "kind": "arc",
          "detail": "project01-catalog/arc01-index/arc-status.json"
        },
        {
          "id": "slice02-labels",
          "kind": "slice",
          "detail": null,
          "record": {
            "id": "slice02-labels",
            "kind": "slice",
            "title": "slice02-labels",
            "parent": {
              "repository": "example",
              "project": "project01-catalog",
              "arc": null,
              "slice": null
            },
            "description": "Review catalog labels.",
            "source_refs": [
              "plan"
            ],
            "state": {
              "lifecycle": "active",
              "delivery": "in-progress",
              "closure": "open",
              "acceptance": "pending",
              "reported_label": "active",
              "note": "Fictional authored assessment; independent acceptance remains pending.",
              "evidence_refs": [],
              "criteria": [],
              "criteria_coverage": "unknown"
            },
            "depends_on": []
          }
        }
      ]
    },
    "progress": {
      "mode": "computed",
      "coverage": "complete",
      "scope": "All current descendant slices."
    },
    "depends_on": [],
    "planned_release": null,
    "release_note": "No release assigned to this fictional example."
  }
}
```

### Input `project01-catalog/arc01-index/arc-status.json`

```json
{
  "$schema": "../../schemas/arc-status.schema.json",
  "format_version": "1.0.0",
  "kind": "arc",
  "repository": {
    "id": "example",
    "name": "Example Catalog"
  },
  "as_of": "2026-09-06T12:00:00Z",
  "sources": [
    {
      "id": "plan",
      "kind": "planning",
      "label": "Fictional planning record",
      "locator": {
        "path": "project01-catalog/arc01-index/slice01-import/closing-report.md"
      }
    }
  ],
  "evidence": [
    {
      "id": "import-result",
      "label": "Import result",
      "claim": "The fictional import capability is reported delivered.",
      "subject": {
        "repository": "example",
        "project": "project01-catalog",
        "arc": "arc01-index",
        "slice": "slice01-import"
      },
      "scope": "delivery",
      "kind": "command-result",
      "strength": "attested",
      "source_refs": [
        "plan"
      ],
      "actor": "Example implementer",
      "observed_at": "2026-09-06T11:00:00Z"
    }
  ],
  "entity": {
    "id": "arc01-index",
    "kind": "arc",
    "title": "arc01-index",
    "parent": {
      "repository": "example",
      "project": "project01-catalog",
      "arc": null,
      "slice": null
    },
    "description": "Index composition remains under review.",
    "source_refs": [
      "plan"
    ],
    "state": {
      "lifecycle": "active",
      "delivery": "in-progress",
      "closure": "open",
      "acceptance": "pending",
      "reported_label": "active",
      "note": "Fictional authored assessment; independent acceptance remains pending.",
      "evidence_refs": [],
      "criteria": [],
      "criteria_coverage": "unknown"
    },
    "children": {
      "coverage": "complete",
      "scope": "All currently planned immediate units in the fictional snapshot.",
      "source_refs": [
        "plan"
      ],
      "items": [
        {
          "id": "slice01-import",
          "kind": "slice",
          "detail": null,
          "record": {
            "id": "slice01-import",
            "kind": "slice",
            "title": "slice01-import",
            "parent": {
              "repository": "example",
              "project": "project01-catalog",
              "arc": "arc01-index",
              "slice": null
            },
            "description": "Import a fictional catalog fixture.",
            "source_refs": [
              "plan"
            ],
            "state": {
              "lifecycle": "active",
              "delivery": "complete",
              "closure": "open",
              "acceptance": "pending",
              "reported_label": "implemented; review pending",
              "note": "Fictional authored assessment; independent acceptance remains pending.",
              "evidence_refs": [
                "import-result"
              ],
              "criteria": [],
              "criteria_coverage": "unknown"
            },
            "depends_on": []
          }
        }
      ]
    },
    "progress": {
      "mode": "computed",
      "coverage": "complete",
      "scope": "All current descendant slices."
    },
    "depends_on": [],
    "gates": [
      {
        "id": "g1",
        "label": "Named check 1",
        "state": "pending",
        "evidence_refs": []
      },
      {
        "id": "g2",
        "label": "Named check 2",
        "state": "pending",
        "evidence_refs": []
      },
      {
        "id": "g3",
        "label": "Named check 3",
        "state": "pending",
        "evidence_refs": []
      },
      {
        "id": "g4",
        "label": "Named check 4",
        "state": "pending",
        "evidence_refs": []
      },
      {
        "id": "g5",
        "label": "Named check 5",
        "state": "pending",
        "evidence_refs": []
      },
      {
        "id": "g6",
        "label": "Named check 6",
        "state": "pending",
        "evidence_refs": []
      }
    ],
    "findings": {
      "coverage": "complete",
      "scope": "Fictional design review",
      "items": [
        {
          "id": "F-01",
          "title": "Review the index ordering",
          "detail": "The import is delivered; ordering still needs a composition demonstration.",
          "severity": "correctness-grade",
          "disposition": "open",
          "evidence_refs": []
        }
      ]
    }
  }
}
```

## Worked variations on C-01

Each variation starts from a fresh copy of C-01, unless it explicitly names
another case. A replacement object is a field value, not a whole document.
“Remove” means remove the key/file, not set it to null. Fixtures in Slice02
must apply all the stated prerequisites, not copy a fragment out of context.

### C-02: Archive with unknown historical slices

Keep the project identity but replace its state with the value below. Remove
its adopted arc document and replace project children with an unknown empty
inventory, note “Historical slice population was not reconstructed.” Replace
project progress as shown; remove collection progress because computed coverage
is no longer available. The existing plan source is the archive provenance.

```json
{
  "lifecycle": "archived",
  "delivery": "unknown",
  "closure": "unassessed",
  "acceptance": "unassessed",
  "reported_label": "historical-archive",
  "note": "Approximate capability grouping; no reconstructed historical slice or acceptance census.",
  "evidence_refs": [],
  "criteria": [],
  "criteria_coverage": "unknown"
}
```

```json
{
  "mode": "reported",
  "scope": "Historical descendant slices, population unknown.",
  "coverage": "unknown",
  "done": null,
  "total": null,
  "source_refs": ["plan"],
  "note": "Retained history does not establish a slice denominator."
}
```

Expected: valid with `W-COVERAGE`; unknown counts, no percent or green closure.
No slices are fabricated. For an archive retaining approximate arc records,
list those as inline arcs with unknown children; a complete known arc inventory
still does not create a complete slice inventory.

### C-03: Mechanical completion while acceptance is pending

At the project, keep children but replace progress with reported 1/2, complete,
source `plan`, note “Current leaf delivery census.” Add source `mechanical-log`
(planning path `project01-catalog/artifacts/mechanical-check.md`) and evidence
`composition-check` with subject project key, scope composition, kind review,
strength reproduced, source_refs `["mechanical-log"]`, actor “Example doer”,
observed_at `2026-09-06T10:00:00Z`, and review:

```json
{
  "actor": "Example independent reviewer",
  "at": "2026-09-06T11:00:00Z",
  "method": "Re-ran the fictional structural check and reviewed the scope exclusion.",
  "source_refs": ["mechanical-log"]
}
```

Set project lifecycle active, delivery complete, closure verified, acceptance
pending. Its evidence refs are `composition-check` plus a new attested delivery
claim for the project. Criteria coverage is complete; criterion M-01 is done
with composition-check. Include criterion M-02 as deferred with reason
“Label redesign is outside the mechanical restructuring acceptance scope,”
destination source_ref `plan`, reentry “Resume when the label research decision
is approved,” and a reproduced decision claim `scope-decision` naming the
excluded direct slice. Both criterion and deferral refer to scope-decision.
All new claim dates precede document as_of, and each has nonempty label/claim,
actor and source refs as required by the contract.

Expected: valid reported mechanical verification with **acceptance pending**;
project remains active. 1/2 delivered is not inconsistent with scoped mechanical
completion plus explicit exclusion. Changing only lifecycle to closed fails
`E-EVIDENCE`. Accepting the project later needs its own named acceptance claim;
child or mechanical evidence is not that claim. This fictional variation models
the separation seen in migration work; it does not describe Lykn's actual rows.

### C-04: Deferred closure after delivery

Start from C-01. At the imported slice, set closure deferred; add a decision
claim `defer-review` (same subject, scope decision, kind operator-report,
strength attested, source_refs `["plan"]`, named actor and non-null time).
Keep delivery complete and acceptance pending. Add this State deferral:

```json
{
  "reason": "Independent review awaits a retained sample.",
  "destination": {"source_ref": "plan"},
  "reentry": "Review when the sample is attached to the fictional plan.",
  "evidence_refs": ["defer-review"]
}
```

Expected: valid; still 1/2 delivered at project, explicitly deferred closure at
slice. Removing destination/reentry is `E-FIELD`; changing closure to verified
without own-scale criteria/review is `E-EVIDENCE`.

### C-05: Sparse optional detail

Replace the project's arc ChildEntry with detail null and `record` equal to
C-01's full arc entity. Move the arc's source/evidence definitions into the
project document, renaming local source ID `plan` to `arc-plan` within that
moved entity/evidence and registry so source ownership stays unambiguous.
Remove the arc document. Expected: valid; same 1/2 counts, no arc link; all inline
facts remain available. Keeping the old detail document is `E-IDENTITY`.
Keeping detail non-null and merely removing its file is `E-DETAIL`.

### C-06: A future research seed, zero current slices

Remove the direct slice, empty the arc's children with complete coverage and
scope “All currently approved slice units; none opened yet.” Remove its finding
and leaf evidence (the subject would no longer exist). Set arc and project
lifecycle research, delivery not-started, closure open, acceptance unassessed,
reported_label research-seed. Keep complete computed progress up the tree.
Expected: valid; 0/0 “no slices planned,” no percentage, no completion. Current
zero planned slices does not promise that the research has no future work.

### C-07: Dirty physical-evidence snapshot

In C-01's arc document add this source; change import-result to kind measurement,
strength attested and source_refs `["bench-snapshot"]`. Its claim describes a
fictional observed signal, not a software verification or hardware instruction.

```json
{
  "id": "bench-snapshot",
  "kind": "snapshot",
  "label": "Fictional retained bench observation",
  "locator": {
    "repository": "example",
    "base_revision": "1111111111111111111111111111111111111111",
    "working_tree": "dirty",
    "observed_at": "2026-09-06T11:00:00Z",
    "paths": ["project01-catalog/artifacts/bench-observation.md"]
  },
  "note": "Base commit does not contain the edited observation; no immutable digest supplied."
}
```

Expected: `W-MUTABLE-SOURCE`, explicitly attested measurement and dirty/unpinned
snapshot. No hardware command, network access or reading of a secret payload is
needed. Claiming reconciled without independent review and broader evidence is
`E-EVIDENCE`.

## Positive and negative fixture matrix

All mutations start from C-01 unless the row says otherwise. IDs C-01 through
C-38 are stable case identifiers for the implementation handoff. Diagnostic
names are the candidate contract's families; exact CLI wording is Slice02 work.
Validation of authored JSON and actual world truth are separate throughout.

| ID | Input / mutation | Expected outcome and display obligation |
| --- | --- | --- |
| C-08 | Rename arc to `arc16.1-index` everywhere: ID, path, parent keys, detail ref, evidence subject and source path; repeat with `arc16.2-index`. | Valid; literal decimal ID; no inferred chronology or dependency. Prefix sorting cannot supply an acceptance claim. |
| C-09 | Project contains only three inline slices; remove arc page/ref and move any needed sources/evidence with renamed IDs. | Valid; zero arc pages and three direct slice rows. Whole-project progress is the leaf sum once each. |
| C-10 | Reported project count done 2, total 3, coverage complete, same all-descendant scope, plan source/note; C-01 leaves remain 1/2. | `E-PROGRESS`; names authored 2/3 and derived 1/2. A cosmetic percentage cannot conceal the mismatch. |
| C-11 | Project reports 1/null with unknown coverage, source and note; make the arc's child coverage unknown with a note; remove computed arc/collection progress. | Valid warning; “1 reported delivered; total unknown.” No ratio or implicit zero. |
| C-12 | Reported progress 0/0 and complete zero current leaf inventory as C-06. Then try 1/0, negative done, 0.5 total, and done > total separately. | First valid, percentage unavailable; each impossible/type variant fails `E-PROGRESS` or `E-FIELD`. |
| C-13 | Keep computed project/collection progress while arc coverage becomes partial, with a note. Separately set any leaf delivery unknown. | `E-PROGRESS`; cannot compute exhaustive delivery from either incomplete population or unknown delivery. |
| C-14 | Partial children retain only the known delivered slice; no direct slice. Report project 1/1 partial, source/note; remove collection computed progress. | Valid, “100% of reported subset”; no whole-project completion. Known leaf count exceeding a claimed complete total fails. |
| C-15 | Duplicate sibling child ID, duplicate inline entity plus detail document, duplicate evidence/source ID, duplicate JSON object key (four separate variants). | `E-IDENTITY`, `E-IDENTITY`, `E-REFERENCE`/`E-FIELD`, `E-DOCUMENT` respectively; no last-writer-wins. |
| C-16 | Referenced arc file absent, detail-kind mismatch, wrong parent key or existing parent omits discovered arc. | Each error identifies the offending file/key: `E-DETAIL`, `E-DOCUMENT`/`E-IDENTITY`, `E-IDENTITY`, `E-DETAIL`. |
| C-17 | Remove collection document only; then also remove project document, leaving arc document. | Each valid standalone adoption; absent parent page has no generated link. Parent EntityKey still identifies ancestry. This is not a duplicate hierarchy. |
| C-18 | Add `old-status.json`, `slice-status.json`, broken JSON, symlinked status file/directory, unreadable status file, or correctly named file at wrong depth (separate variants). | `E-DOCUMENT`; discovery must not skip any input. Selected-page rendering also fails on malformed siblings. |
| C-19 | Project delivery complete with only child evidence; or closure verified with no criteria, partial criteria, no own composition, or wrong-subject evidence. | `E-EVIDENCE`; parent cannot inherit closure or delivery evidence from its children. |
| C-20 | At leaf supply complete own criteria and independently reviewed verification evidence for proposed closure; keep acceptance pending. Then change acceptance to accepted without a claim. | Proposed remains proposed-done even with strong evidence; second variant `E-EVIDENCE`. State changes require author judgment, not automatic upgrade. |
| C-21 | At a leaf add complete done criteria with reproduced own verification, set closure verified, add attested operator acceptance claim and delivery claim, set lifecycle closed. | Valid reported verified/accepted closure with pointers. Parent stays active/open. Remove review or substitute only attested verification and closure fails. |
| C-22 | Use C-21 for a parent while a child is open, with no explicit criterion/decision addressing exclusion. Then add complete exclusion/deferral decision evidence naming that child. | First `E-EVIDENCE`; second can validate under section 3, but excludes that child's delivery from delivered numerator unless actually delivered. |
| C-23 | Six pending gates (C-01); switch one to passed with attested scoped gate evidence, another waived with decision evidence/note. | Six visible slots, one passed, one waived, four pending. No clipped gates or 2/6 passes. Remove evidence and fail `E-EVIDENCE`. |
| C-24 | Finding with title/detail/severity/disposition; then replace title/detail with legacy `text`, omit disposition, or add `disp_cls`. | Valid case renders all content; each bad variant fails `E-FIELD`. No silent finding loss or styling from data. |
| C-25 | No checks; unknown check; dated passing check with scoped evidence; failing check with evidence (separate variants). | Unassessed, unknown, dated scoped pass, dated scoped fail respectively. No “no drift/check green” fallback; undated/evidenceless pass fails. |
| C-26 | A local dependency on delivered imported slice; then require verified; then omit depends_on. | Direct slice eligible from declared data, then ineligible, then readiness unknown. It is not “live reconciled.” |
| C-27 | Local self-edge, cycle between direct and arc slice, dangling EntityKey, duplicate edge; reciprocal related links (separate variants). | Dependencies error (`E-CYCLE`, `E-REFERENCE`/`E-FIELD`); related cycle valid and does not affect readiness. |
| C-28 | External dependency uses source target, assessment unknown; then satisfied with attested check/decision evidence. | Unknown then reported satisfied, never an independently computed external fact. No fetch; unmet prerequisites are valid blocked work. |
| C-29 | Git source at immutable commit with `ref_hint: release/example`; HTTPS source in another repository. | Valid qualified references; no host-local absolute checkout needed. A branch name instead of revision fails `E-FIELD`. Missing local planning path is visible warning, not false availability. |
| C-30 | Source absolute/traversal path; detail escapes selected tree; URL uses javascript/data/file scheme. Plain title contains quotes and `<example>`. | Bad references fail `E-REFERENCE`; plain title valid and escaped as literal text, never interpreted as HTML. |
| C-31 | Duplicate a project under a distinct ID, correct ancestry and inline children; assign same planned_release to both. Repeat with one null and one absent target. | Distinct projects; shared target is metadata. Null says no release assigned; absent says not supplied. Saga remains a collection. |
| C-32 | `format_version` unsupported/mixed; schema path targets installed skill, remote URL or wrong kind. | `E-DOCUMENT`; no runtime fetching or compatible-version guessing. |
| C-33 | Old consumer retains its data/toolkit while installed skill changes; explicit upgrade changes required field. | Old copy behavior is unchanged by design; explicit upgrade requires reviewed all-document migration and retest. This is a future isolated-copy integration test, not demonstrated by JSON. |
| C-34 | Render twice with identical data/toolkit; render after evidence is old; modify referenced child but retain old HTML. | Future deterministic output/freshness checks; status as_of/evidence dates unchanged by render. Stale generated parent detected. Exact protocol awaits Slice02. |
| C-35 | Add links relation lessons and port-ledger to existing source refs; add unrecognized namespaced extension. | Valid adjacent links; extension warning makes non-rendered custom content visible. No fabricated lesson/port counts. Full optional modules remain Q-05. |
| C-36 | Nineteen arcs; include unphased rows, long titles/findings, four/six/zero gates, archived unknown counts; narrow/offline display. | All rows and qualifications reachable across Frontier/Instrument/Spine/arc views. Future browser/UAT case; zero gates is not a green all-clear. |
| C-37 | Null as_of and observation date; then as_of earlier than a referenced review; then evidence source ID missing. | Unknown dates valid and visible; inconsistent date `E-FIELD`; dangling ID `E-REFERENCE`. Render time does not repair any case. |
| C-38 | Known counts 199/200 in an otherwise sparse reported complete population, with no contradictory descendants. | Rounded display may be 100%, but counts remain 199/200 and state unchanged. Unreconciled-detail warning remains; no completion inference from rounding. |

## Observed Lykn shapes and proposed representation

Read-only refresh on 2026-09-06: planning HEAD
`ef0a1155cb65884456c5eaf52bdaa49af0d50055`. Hardware has nine modified tracked
files plus an untracked artifacts directory. Counts are current top-level
directories, **not a census of open arcs or independent completion**. Source
headers and selected wrapper/research/migration prose were read; no historical
verification was rerun. See the verification record for exact read routes.

| Current project / observed shape | Proposed representation and case coverage | Adoption judgment still needed |
| --- | --- | --- |
| `project01-mvp`: historical-archive, 18 approximate arcs, no reconstructed slices | C-02: archived/reported original label; inline or optional-detail arcs, unknown slice populations, provenance qualification. Do not fabricate slices or verified closure. | Which arc records have enough evidence for anything beyond unassessed status; no inference from missing files. |
| `project02-language-toolchain-alignment`: active, 19 arc directories | C-08/C-36: dense complete project view once inventoried; literal `arc16.1` and `arc16.2` wrappers, origin note; dependency order only from explicit edges. | Read current ledgers and decide open-arc page census; wrapper organization does not add a new acceptance claim. |
| `project03-language-evolution`: research, 0 arcs, 3 direct slices | C-09: inline slices directly under project, source label research. Research completion and later language-design disposition stay separate. | Assess each slice's delivery/verification/acceptance from its records; no assumed three-open or three-closed count. |
| `project04-c-lang`: research-seed, 1 arc, no current slice implementation | C-06: research and zero currently planned slices, with source scope; no delivery date promise or completion from 0/0. | Confirm the current inventory at adoption and distinguish candidate research from approved implementation. |
| `project05-hardware`: active, 7 arcs, dirty records | C-07/C-29: attested measurement or operator report with dirty snapshot provenance; evidence may live in source branches. No hardware operations. | Preserve/refer to actual then-current mutable bytes; operator owns physical and acceptance judgments. |
| `project06-planning-reorg`: implemented-awaiting-operator-review, 3 arcs | C-03: reported delivery/mechanical verification and pending acceptance, qualified own-scale evidence. Planned release null. | Populate real criteria/claims from actual records; do not copy the fictional exclusion or mark accepted from prior mechanical results. |

C-31 additionally covers shared planned release `0.8.0` for the research and
hardware tracks, and explicit null for maintenance. C-29 covers evidence on
release branches or in another repository. Adoption must refresh all projects
and open arcs from current plans/ledgers/verification and record unresolved
classifications. The 48 arc directories are not automatically 48 required
arc-status pages. Toolkit validity cannot settle that census on the operator's
behalf, and pending grouping review does not block use of Lykn's planning tree.

## Ledger-to-case coverage and verification limits

| Slice row | Relevant cases | Review route |
| --- | --- | --- |
| S-01 | C-01, C-05, C-08–09, C-15–18, C-29–32 | Full records against envelope/entity/reference tables at every scale. |
| S-02 | C-02–04, C-06–07, C-19–22, C-37–38 | Try unsupported closure/acceptance and verify unknown/partial/dated qualifiers. |
| S-03 | C-01–02, C-05–06, C-10–17, C-38 | Recalculate leaf populations once; vary coverage and duplicate ownership. |
| S-04 | C-02–03, C-06–09, C-29, C-31, C-36; six-project table | Match observed shapes without asserting new historical truth. |
| S-05 | C-23–28, C-34–36 | Review extraction map against union of trial field keys and template reads. |
| S-06 | C-32–34 | Explicit version rejection/copy isolation/migration requirements; future integration tests. |
| S-07 | C-01–38 and Q-01–06 | Author consistency checks plus separate independent design/operator review. |

The checks actually run in this slice are JSON syntax on fenced examples,
worked arithmetic, reference/identity checks on the three full example records,
local Markdown links and whitespace, and a seven-row scope walk. These do not
execute the proposed schema, negative fixtures, copy-isolation test, browser
views, freshness logic or Lykn UAT. Those checks are specified here for the
later implementation/design acceptance sequence, not claimed as passing tests.
