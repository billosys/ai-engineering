# Execution notes — CC evidence assignment

## Intake and pins

- Issuing prompt commit: 8c0e4e897e79a9ecddd07da34fd0f2eb1dfb119d.
- Planning: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning,
  branch planning, opening HEAD a5f94fcf5db30dc7231a2a2ff01c5aa79324d2a1;
  status showed ahead 6 and unrelated untracked project12-chcd-protocol/.
- SOURCE: /Users/oubiwann/lab/billosys/ai-engineering at pinned main
  dffa504e851b03b8e4746f1941068e4cc850b612; unrelated untracked knowledge/lfe/.
  Neither checkout was edited.
- Planning predecessor 23c77653feda2fafd88efce01e226ee1a35b8cff; Slice02
  closure c1c832647eb82b67f3acad0c72c00a817308ac34; method pin
  759ce2dd116a4cfe03b72d43fd2791f48486251c; DES-008 audit pin
  795ac75b7d02536e0e95252457ac3282cd17d8d8.
- No source, Project13, prompt, preparation note, plan, parent ledger or prior
  record was edited. Project13 protocol/register was not opened for this
  execution; operative trial steps came from the prompt and host plan.

## Required-read receipts

SOURCE AGENTS.md was read completely (216 lines) in two bounded reads after
an opening combined output was truncated. PLANNING AGENTS.md and Project10
AGENTS.md were read. Current collaboration-framework, project-management and
work-verification guidance was applied. The source project-management skill and
guide README, complete design skill entrypoint, 03 planning top-down open-set/
handoff section, full 01 ledger-discipline guide, accepted 83-line review
procedure and DES-008 lines 99–105 were read.

Project10 plan, Arc02 plan, both parent ledgers, slice plan, ledger, prompt and
preparation notes were read fully. All 17 contexts (168 lines) were read at
SOURCE pin with file hashes/extents checked against preparation notes. The
design.md:158–180 continuation was included. No whole-file acceptance or
expanded source population is claimed.

Contract readback: scope is selected token assertions and explicit boundaries;
C&B literals remain evidence while portable proposals remove those defaults.
Original attribution/fidelity remains unavailable and current Git bytes do not
upgrade it. Literal, evidence observation, warrant and replacement stay
separate. Consistency requires a same-object local pair: SKILL.md:114 and
design.md:175–177 agree locally; Material Web's concrete-value allowance is
counterevidence to universalizing the rule. The colour.md:245 preview chip is
not itself evidence of component binding. Seven outputs only; ledger rows remain
open for CDC independent review.

## Example and comparison exercise

The preparation demo ran from SOURCE root against pinned Git bytes before batch
judgments. It exited 0: one positive and three invalid records rejected, with
semantic verdict explicitly “human judgment; independent review pending.” This
checks declared identity/reference/capture/comparison predicates for those
inputs, not web claims or semantic truth.

The local pair addresses component token references and agrees as local policy.
Material Web permits component values to be system tokens or concrete values;
that counters a universal ban but does not conflict with the local pair. The
.sem-chip preview at colour.md:245 is a different object/use and was not used as
a paired contradiction.

## Source access and recovery

Seven accessible primary rows and three unavailable URLs are recorded with
extents, observation date, unknown versions, no immutable capture, and scope
limits in source-comparison.md. Direct retries on 2026-10-10: Material 3 yielded
a one-line JavaScript shell; both old Polaris color URLs returned internal
errors. No search snippet judged a claim.

One initial source query used knowledge/design/design.md. git ls-tree showed
the actual path knowledge/design/guides/design.md. The query was corrected and
all contexts were loaded at the pin. One inventory-generation attempt targeted
the implementation checkout for a planning output and failed before writing;
it was rerun at the planning root. An early extraction draft did not preserve
apostrophe escaping and wrote no output. Later identity checks used exact
pinned Git bytes. These failures were recovered without protected-data changes. One ledger-preservation audit initially matched the supplemental evidence table as if it were a second criterion table; the check was corrected to compare the canonical nine opening rows only.

## Current inline checker and limits

The current checker is standard-library Python, embedded here; no helper script
or dependency was added. It parses JSONL with duplicate-key rejection; joins
every assigned result to an inventory token unit; re-hashes pinned SOURCE paths;
checks literal offsets/spans; checks five dimensions and evidence references;
and verifies any consistency pair has two pinned subjects. The actual run used
these predicates plus the negative mutations below.

    import hashlib, json, subprocess
    from pathlib import Path
    def strict(line):
        def pairs(items):
            d = {}
            for k, v in items:
                if k in d: raise ValueError("duplicate JSON key")
                d[k] = v
            return d
        return json.loads(line, object_pairs_hook=pairs)
    inventory = [strict(x) for x in Path("artifacts/occurrence-inventory.jsonl").read_text().splitlines()]
    results = [strict(x) for x in Path("artifacts/claim-results.jsonl").read_text().splitlines()]
    by_id = {r["unit_id"]: r for r in inventory}
    assert len(by_id) == len(inventory)
    assert {r["unit_id"] for r in results} == {r["unit_id"] for r in inventory if r["unit_kind"] == "token"}
    for row in inventory:
        s = row["source"]
        data = subprocess.check_output(["git", "show", s["revision"] + ":" + s["path"]])
        assert hashlib.sha256(data).hexdigest() == s["sha256"]
        line = data.decode().splitlines()[s["span"][0]-1]
        a, b = s["literal_offset_0based"]
        assert line[a:b] == s["literal"] and s["span"][0] == s["span"][1]
    for row in results:
        assert row["unit_id"] in by_id and by_id[row["unit_id"]]["unit_kind"] == "token"
        assert set(row["dimensions"]) == {"source_faithfulness","correctness","scope_attribution","consistency","relationship_cq_coverage"}
        evidence_ids = {e["id"] for e in row["evidence"]}
        for dim in row["dimensions"].values(): assert set(dim["evidence_refs"]) <= evidence_ids
        if row["dimensions"]["consistency"]["outcome"] == "agrees":
            paired = row["dimensions"]["consistency"].get("paired_subjects", [])
            assert len(paired) == 1 and paired[0]["revision"] == "dffa504e851b03b8e4746f1941068e4cc850b612"
    # Discriminating controls against the same positive predicates:
    assert not ({r["unit_id"] for r in results[:-1]} == {r["unit_id"] for r in inventory if r["unit_kind"] == "token"})
    bad = dict(inventory[0]); bad["source"] = dict(bad["source"], path="knowledge/design/missing.md")
    try: subprocess.check_output(["git", "show", bad["source"]["revision"] + ":" + bad["source"]["path"]])
    except subprocess.CalledProcessError: pass
    else: raise AssertionError("bad source join passed")
    false_pair = dict(results[0]); false_pair["dimensions"] = dict(results[0]["dimensions"])
    false_pair["dimensions"]["consistency"] = {"outcome":"agrees","paired_subjects":[],"evidence_refs":[]}
    assert len(false_pair["dimensions"]["consistency"]["paired_subjects"]) != 1
    false_capture = dict(results[0]); false_capture["evidence"] = [dict(results[0]["evidence"][0], snapshot_sha256="0"*64)]
    assert any(e["snapshot_sha256"] is not None for e in false_capture["evidence"])

Run the code from the slice root. It checks output shape and identity, not source
applicability or semantic correctness.

Precommit results: strict JSONL parsing and uniqueness/join checks passed;
all pinned file hashes, one-line spans and offsets passed; all five dimensions
and evidence references were present; local output links/fragments resolved;
LF/final-newline and git diff --check passed. Removing a result unit, changing a
source path/hash, and asserting an unpaired comparison or fabricated capture
were rejected by join/identity/pair/snapshot predicates. The demo again accepted
one positive and rejected three supplied corruptions.

These checks prove shape/identity only. They do not prove that compound claims
were optimally atomized, a primary passage warrants its result, or a replacement
is semantically complete. Human review must inspect records, passages, scopes,
qualifiers, and handoff. Historical pages, original capture, full 233-card/
eight-live-file evidence, actual export validation and P10-11 remain blocked or
unrun. Trial utility and elapsed effort were not measured independently; no
improvement is claimed.


## Candidate commit and committed-byte replay

Candidate commit: 208524724295391a3fc4d2650c7165e857758ed3. Its tree changes
exactly the seven authorized paths and includes both required Co-authored-by
trailers. The prompt, preparation notes, slice plan and all paths outside that
allowlist are absent from its path list; prompt/preparation/plan bytes were
compared between parent and candidate and are identical. The canonical nine
ledger criterion rows remain byte-identical/open. Project12 remains untracked
and outside the commit. SOURCE remains at dffa504e851b03b8e4746f1941068e4cc850b612
with its pre-existing knowledge/lfe/ untracked directory.

Committed-byte replay passed: all 145 inventory source identities, 51 exact
result joins, five dimensions and evidence references, 51 handoff IDs,
evidence snapshot-null checks, local links/final newlines, and exact seven-path
tree check. Missing-unit, bad-source-path, empty paired-subject, and fabricated
snapshot mutations were rejected. The author demo still passes one positive and
rejects three corruptions. This replay establishes committed shape and identity,
not semantic acceptance.

One first replay harness invocation incorrectly double-prefixed HEAD while
reading protected paths and failed at that final comparison; the candidate
checks before that point had passed. The lookup was corrected to compare explicit
parent:path and candidate:path blobs, and the full replay then passed. No files
were changed by the failed lookup.
