# Slice01 completion report — Fennel guidelines

Date: 2026-10-17. Status: **closed**, under the Operator-selected single-contributor
workflow. Primary contributor: Sofie. The user-required fresh-context audit and its
correction verification are complete; no further Operator or CDC gate applies.

## Assignment and source state

Completed the Operator's original seven-part request, preserved in initial
`cc-prompt.md`, with the explicitly recorded single-contributor transition.
Planning/source separation and scope remained binding. Source baseline was
`4e635bb3`; unrelated design work subsequently committed as `7b20ccc3` was preserved.
Imported sources in non-squashed merge `c6a089ba8f0809d9147ea60d66e3d78f02bd4792`.
Final skill implementation commit: `c9d98a3ec3d0a24c30a18431d7aeaa13f6451872` on main. All 36 files in the corrected
candidate manifest match that committed tree byte-for-byte. The planning close
commit is identified by Git history for this report, without a self-hash placeholder.

The source commit paths are exactly Makefile, README.md, docs/skill-library.md,
knowledge/fennel/SKILL.md, knowledge/fennel/version-history.md, all twelve authored
guides, and the five provenance/support files under sources/. The earlier merge
contains only the fourteen original docs/license files under sources/md/. No source
file was modified after import. No push or profile skill installation was requested.
The planning commit is restricted to project14-fennel/.

## Outcome and use

`knowledge/fennel/SKILL.md` routes writing, review, debugging, API/macro design and
embedding tasks into eleven focused chapters with 56 rules, paired examples,
strengths, rationale, summaries and pinned primary-source references. Sources and
licenses are retained and indexed. `make fennel` builds the installable
`target/skills/fennel-guidelines.zip`; aggregate build/install inventories include it.
The actual zip has fourteen files and eighty resolving local links, with no local
source-corpus dependency. Adapted prose uses CC BY-NC-SA 3.0; original source
licenses and Calvin Rose/Campbell/Hagelberg attribution remain distinct.

## Row walk — 7 opening rows, 7 accounted for

| ID | Disposition | Outcome and evidence | Strength |
|---|---|---|---|
| S01 | done | Requested source chain and selection pinned: sources/README.md and retained-paths.json; fresh audit source-chain checks | reproduced |
| S02 | done | History and original attribution preserved: c6a089ba; 749 commits, 679 selected non-merge changes, 7,493 historical blobs and 14 originals; independent ancestry comparison | reproduced |
| S03 | done | Formatter and executable behavior verified: toolchain.json; example-results.json 112/112; integration-results.json 13/13; fresh reruns/native specimens | reproduced |
| S04 | done | Complete source-grounded teaching guides delivered: 56/56 rule-body review, 6/6 requested docs fully read; final-audit.md correction verdict resolves FEN-001 | reproduced |
| S05 | done | Wayfinder and sole skill history delivered: SKILL.md, sibling history; skill-creator validator and source/package version gate; FEN-003 resolved | reproduced |
| S06 | done | Package/library wiring complete and valid: Makefile, README, skill-library; Make gates; 14 source-equal files, 80 local links, isolated zero warnings; FEN-002 resolved | reproduced |
| S07 | done | Scoped records and evidence returned: This report, exact artifact inventory, source commit and named-path commit scope; single-contributor workflow record | attested |

## Validation and limitations

- `make check-skills`: pass. Skill-creator `quick_validate.py` with repository
  `.venv/bin/python`: pass. The system Python attempt lacked PyYAML; no dependency
  was installed or validation skipped.
- `make check-package-paths`: pass after fresh rebuilding, independently rerun after
  corrections; 25 source skills and 25 packages, zero version errors, 402 Markdown
  files and zero hard path failures. The other catalog packages produce 596 warnings
  at 594 locations plus three explicit exceptions; these remain visible. The isolated
  Fennel package has zero failures, zero warnings and zero exceptions.
- `check-examples.py`: 112/112 pass, with 104 executable snippets run through both
  the launcher and emitted Lua (208 runtime invocations); eight compile-negatives
  check their intended diagnostic. 103 formatter checks exclude the deliberately
  ugly layout example and eight compile-negatives. The first draft's 43 delimiter
  failures are retained in the initial log/JSON; corrected runs replace no failure
  with an ignored test.
- `check-integration.py`: 13/13 expected outcomes; genuine module/macro loading,
  embedded Lua, strict versus bare AOT, clean bundled distribution, relocation and
  native cleanup positive/negative checks. The fresh reviewer additionally tested
  native nil/false/file resources and a realistic small settings module.
- `verify-import.py`: pass on 749 retained commits, 679 selected non-merge changes,
  7,493 historical blobs and fourteen current originals. Fresh reviewer independently
  verified all retained-ancestor relationships, merge parents and original filenames.
  Rewritten hashes and invalidated upstream signatures are disclosed, not relabelled.
- Whole owned-tree version review and actual zip inspection passed. No additional
  path exception or second skill history was introduced. `git diff --check` passed;
  scoped staging/commit preserved unrelated untracked knowledge/lfe/.

These checks use Fennel 1.6.1, fnlfmt 0.3.2 and PUC Lua 5.5. The full defined 56-rule
set and six requested upstream docs received independent body-level review; this is
not a universal correctness or all-host compatibility guarantee. Exact unread
supplemental ranges, external URL checks and other limits remain in final-audit.md.

## Fresh audit and findings dispositions

Reviewer `/root/fennel_final_audit` began with `fork_turns=none`, a full purpose,
contract, reading, source and evidence packet, and no suggested findings. Its initial
verdict and entire source/rule coverage map are preserved in `artifacts/final-audit.md`.
A dated correction-verification section is the current verdict: no remaining
actionable findings in scope. The exact corrected candidate was then committed.

| Finding | Severity | Disposition and proof |
|---|---|---|
| FEN-001 | Medium | Resolved: ER-04 and LI-03 distinguish protected :close from native __close. Four added integration checks and independent native file/nil/false witnesses pass. Retained upstream prose stays unchanged. |
| FEN-002 | Medium | Resolved: general MIT copyright correctly names 2016–2025 Calvin Rose and contributors in source provenance and the shipped index; pinned README supports it. Style-specific notices remain. |
| FEN-003 | Low | Resolved: all eleven guide-map labels match chapter titles; accurate counts and useful topic descriptions were independently checked. |

The primary inspected each cited finding against actual source before correction.
All fourteen originals and all 112 example blocks remain unchanged between the
initial and corrected candidate; evidence retention is explicit in the follow-up.

## What worked

Tracing the website build to its language submodule avoided importing generated
HTML. Historical --follow inspection caught README as the API's ancestor. Full
historical tree/metadata checks and an independent ancestor comparison established
import fidelity. Executable paired examples exposed draft syntax defects; the fresh
semantic review found a native-cleanup contract gap that default-mode tests missed.

## Bubble-up to project

This is the project's single slice, so no arc wrapper exists. The slice delivers the
whole capability: a usable authoring skill and package, preserved source history,
checked examples and reviewed provenance. The additional README is within the
Operator-authorized useful source scope and necessary for API lineage. The style
license and native-closing protocol findings were resolved within the requested
scope. All seven requested obligations are covered; no deferred or silently dropped
work, successor slice or additional arc is required. The project ledger closes on
this delivered composition plus the fresh final audit and addressed findings.

## Artifact inventory

All durable supporting artifacts are inside this slice's artifacts/ directory.
Source provenance under knowledge/fennel/sources/ is part of the shipped-source
repository deliverable, not a planning-home override. The zip is an ignored,
reproducible build artifact. First-class plans, ledger, preserved prompt and this
report remain at slice/project level.

- `artifacts/audit-specimens/README.md`
- `artifacts/audit-specimens/app/test.fnl`
- `artifacts/audit-specimens/app/vendor/settings/init.fnl`
- `artifacts/audit-specimens/boundaries.fnl`
- `artifacts/audit-specimens/macrodebug.fnl`
- `artifacts/audit-specimens/native-protocol.fnl`
- `artifacts/candidate-manifest.json`
- `artifacts/check-examples.py`
- `artifacts/check-integration.py`
- `artifacts/corrected-candidate-manifest.json`
- `artifacts/description-checks.log`
- `artifacts/example-checks-initial.log`
- `artifacts/example-results-initial.json`
- `artifacts/example-results.json`
- `artifacts/execution-notes.md`
- `artifacts/final-audit-prompt.md`
- `artifacts/final-audit.md`
- `artifacts/integration-results.json`
- `artifacts/package-checks-final.log`
- `artifacts/package-checks.log`
- `artifacts/package-inspection-final.json`
- `artifacts/package-inspection.json`
- `artifacts/toolchain.json`
