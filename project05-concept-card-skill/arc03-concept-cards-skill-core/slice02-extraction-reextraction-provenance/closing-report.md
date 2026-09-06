# Arc03 Slice02 Closing Report: Extraction, Re-Extraction, And Provenance

```yaml
project: project05-concept-card-skill
arc: arc03-concept-cards-skill-core
slice: slice02-extraction-reextraction-provenance
status: cc-proposed-done
reported-by: Codex CC
reported-on: 2026-09-06
source-commit: 79664fc8751f5fe33d28a4221431caccc4222d37
planning-commit: the commit containing this report and the slice ledger
evidence-strength: attested
```

## Outcome

Added detailed source-faithful extraction and source-primary re-extraction/
preservation guides. Made guides 03/04 live in the entrypoint and advanced
`metadata.version` to `1.1.0` with a sibling history entry.

All seven ledger rows are CC proposed-done with attested evidence. Independent
CDC verification remains pending. No live corpus extraction was performed.
The implemented procedures do not claim later evidence, verification,
reconciliation, admission, support or package surfaces have been delivered.

## Source Scope

Implementation checkout: `/Users/oubiwann/lab/billosys/ai-engineering`, branch
`main`, opening commit `31d96b1`. Initial source status was clean.
Source commit: `79664fc8751f5fe33d28a4221431caccc4222d37`.

Exactly these paths were staged, inspected and committed explicitly:

```text
knowledge/concept-cards/SKILL.md
knowledge/concept-cards/version-history.md
knowledge/concept-cards/guides/03-extraction.md
knowledge/concept-cards/guides/04-re-extraction-preservation.md
```

The commit contains 430 insertions and six deletions and has both required
co-author trailers. Source status is clean after commit; the skill matches
HEAD. No unrelated source work was present or included. Guides 01/02 remain
byte-identical to their pre-slice committed contents, verified by Git diff.

No guide 05 or later guide, support directory, schema, template, example,
executable validator, runtime, package/Makefile/README/docs/install surface,
or adjacent skill was changed. The historical source roots remain absent.

## Design Evidence

Read the current source AGENTS.md, Project05 project/Arc03/slice plans and
ledgers, predecessor CDC verification, and current entrypoint/load/workflow
guides. Revisited the accepted Project03 conceptual model at
`artifacts/project03-concept-card-method/arc03-conceptual-model/slice04-model-synthesis/artifacts/v40-conceptual-model.md`.
The architecture and source-edit sequence inspected in Slice01 remain relevant
historical evidence; current Project05 names, layout and slice scope govern.
The document-extraction output contract was checked for the upstream handoff.

Guide 03 has 205 lines of procedures covering source/prepared identity,
extraction run identity and actual worker provenance, concept-boundary
selection, qualified claims, excerpt discipline, typed locators and spans,
claim/span comparison before support assertions, inference labels, extraction
confidence, output checks, both operating modes and handoff.

Guide 04 has 195 lines covering inventory of prior cards and dependent
constructs/results, old/new source and run identity, a source-first candidate
set before prior-card integration, changed and unchanged claims, new coverage,
source drift, unavailable or damaged sources, unsupported prior material,
preservation dispositions, dependency/result applicability, both operating
modes and handoff.

Content review confirmed these decision boundaries:

- A prepared-source manifest or Ready status identifies preparation evidence;
  it does not supply claim-level source support or semantic verification.
- A source locator addresses material, a source span selects it, and support
  states its relation to a particular assertion after comparison. Run
  provenance describes production context; it cannot replace that comparison.
- Qualifications, modality, units, scope and source-statement/inference labels
  survive synthesis. A span supporting only part of a claim cannot warrant the
  entire compound assertion.
- Prior inventory precedes rewriting, but prior prose does not become the
  source for new claims. Source-derived candidates remain identifiable before
  integration with prior cards.
- Missing support, inaccessible support and inspected material that does not
  support a claim are different findings. No match in a sample does not prove
  the old claim false or justify silent deletion.
- Preserved, superseded, rejected and unresolved dispositions identify the
  prior value, source basis/uncertainty, destination, rationale and actor/run.
  Historical retention does not confer support or admission.
- Source drift, changed conversion, changed claims, unchanged text and changed
  locators are distinguished. Old result records remain tied to old revisions;
  their applicability to new outputs must be checked rather than inherited.
- Extraction confidence, evidence grade, validation result, verification
  result/state, reconciliation result/state, preservation decision and memory
  admission remain separate. Worker agreement and same-context checking are
  not automatically independent verification.

These are source-guidance and model-consistency observations, not behavioral
results from extracting cards against a real corpus.

## Validation Results

Commands ran in the implementation checkout unless stated otherwise. All
results are doer-attested, not independently reproduced.

| Check | Observed result |
| --- | --- |
| `scripts/check-skill-description.sh knowledge/concept-cards/SKILL.md` | Exit 0, no output. |
| `python3 /Users/oubiwann/.codex/skills/.system/skill-creator/scripts/quick_validate.py knowledge/concept-cards` | Exit 0, `Skill is valid!`. |
| `git diff --check` | Exit 0. |
| `make check-skills` | Exit 0, `>> all skill descriptions within limit`. |
| `make check-skill-versions` | Exit 0; source phase: 22 source skills, 0 packages, 0 errors; final phase: 22 source skills, 20 existing packages, 0 errors. |
| Exact owned-tree inventory | Six Markdown files: entrypoint, sibling history, guides 01–04; no support directories or executable files. |
| Local Markdown links/anchors | Six files, 19 local links/anchors, zero errors. Inline-code future routes excluded. |
| Version/history inspection | Nested metadata string `1.1.0` and matching sibling entry; no top-level version, guide-local histories or duplicate current skill-version prose. |
| Whitespace/newlines | All six files have final newlines and no trailing whitespace. |
| Scope exclusions | `knowledge/concept-card-method/` and `knowledge/source-preparation/` absent; guides 01/02 unchanged. |
| `git diff --cached --check` | Exit 0 over the exact four-file staged diff. |
| Post-commit status / HEAD comparison | Clean source; `git diff --exit-code HEAD -- knowledge/concept-cards` exits 0. |

The version gate rebuilt ignored archives for existing targets. It does not
build a concept-cards package; package work remains Arc05. No archive was
committed and no package surface changed, so package-path checks were not run.
No real extraction, executable validator, memory operation or runtime behavior
was added or exercised.

Executable ledger content verifiers returned:

```text
S2-1: exit 0; 5 stdout lines; 0 stderr lines
S2-2: exit 0; 31 stdout lines; 0 stderr lines
S2-3: exit 0; 54 stdout lines; 0 stderr lines
S2-4: exit 0; 38 stdout lines; 0 stderr lines
S2-5: exit 0; 44 stdout lines; 0 stderr lines
```

S2-7's component gates all passed as listed; the version gate ran separately
because it writes ignored build output. Content inspection supplements the
keyword verifiers, particularly for S2-3 through S2-5.

Local link reproduction, from the source checkout:

```python
from pathlib import Path
import re

root = Path("knowledge/concept-cards")
count = 0
for path in root.rglob("*.md"):
    text = re.sub(r"`[^`\n]*`", "", path.read_text())
    for dest in re.findall(r"\]\(([^)\s]+)\)", text):
        name, _, anchor = dest.partition("#")
        target = (path.parent / name).resolve() if name else path
        assert target.is_file(), (path, dest)
        if anchor:
            headings = re.findall(r"^#+ (.+)$", target.read_text(), re.M)
            slugs = [re.sub(r"[^a-z0-9 -]", "", h.lower()).replace(" ", "-")
                     for h in headings]
            assert anchor in slugs, (path, dest)
        count += 1
print(count, "local links/anchors; 0 errors")
```

This covers this tree's simple relative links and heading anchors; it does
not validate unavailable inline-code future paths or implement a general
Markdown parser or a shipped concept-card validator.

## Row Walk

| Row | CC proposed status | Evidence |
| --- | --- | --- |
| S2-1 | done | Guides 03/04 exist and are linked as Live in the entrypoint; current route map explicitly governs availability. |
| S2-2 | done | Nested metadata version 1.1.0, corresponding sibling history, no guide-local histories; version gate passes. |
| S2-3 | done | Guide 03 covers every requested extraction/provenance topic with stepwise instructions and both operating modes; see Design Evidence. |
| S2-4 | done | Guide 04 covers prior inventory, source-first comparison, drift and evidence gaps, all preservation dispositions, unique prior value, run/worker provenance and handoff in both modes. |
| S2-5 | done | Both guides retain required construct/lifecycle distinctions and explicitly leave later guide, Arc04 support, Arc05 package and runtime work unimplemented. |
| S2-6 | done | Exact four-file source commit; clean source before/after; no excluded roots, support/package/runtime edits or live corpus extraction. |
| S2-7 | done | All five source gates pass, plus 19 local links/anchors across six Markdown files. |

Rows: 7. CC proposed-done: 7. Deferred: 0. No-op: 0.
Independently verified: 0.

## Planning Scope And Artifact Inventory

Planning worktree: `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`,
branch `planning`, opening commit `be76ba3`. Project05 was clean before edits;
11 unrelated untracked Project06 paths were present. Their content hashes were
captured as a preservation baseline; none was edited or staged by this work.
Only this slice's `ledger.md` and `closing-report.md` are changed. CC does not
write `cdc-verification.md` or modify parent plans/ledgers.

No separate durable planning artifacts were produced, matching the slice plan.
Implementation output is the four source files. This report and the ledger are
durable CC evidence; temporary drafts and logs are not needed for reproduction.
Ignored existing package output is a gate side effect, not a new deliverable.

## Bubble-Up To Arc03

The assigned extraction, re-extraction and provenance capability is delivered
subject to independent CDC reproduction. No change to Arc03's capability,
slice breakdown or sequence is proposed. No assigned criterion was weakened,
dropped or deferred; source scope matches the explicit four-file authorization.

Residual caller wording needs a later authorized cleanup: guide 01's final
availability paragraph still calls routes 03–10 future. Guide 02's introduction,
guide-04 reference and closing paragraph still describe extraction/preservation
or routes 03–10 as unavailable. These foundation files were explicitly outside
this slice's edit list and remain unchanged. The entrypoint now states that
its map is current even when foundation wording calls 03/04 future, and the
new guides link each other as live. CDC should carry this bounded caller-text
cleanup into the next appropriate slice's source scope, removing the temporary
entrypoint qualification once the callers agree.

This is disclosed residual routing language, not missing extraction or
preservation guidance. The detailed guide boundaries remain 05–10 future,
Arc04 support future and Arc05 package/docs/install future. Independent CDC
verification is the next closure step; this report does not close Arc03 or
Project05 or open a new slice.
