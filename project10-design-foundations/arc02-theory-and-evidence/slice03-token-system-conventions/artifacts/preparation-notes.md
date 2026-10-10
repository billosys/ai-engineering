# CDC preparation — token-system conventions

Prepared 2026-10-10 by Sofie, CDC. This is author preparation, not an accepted
CC result. Project13 T01 uses protocol revision 2 at
`23c77653feda2fafd88efce01e226ee1a35b8cff`; registration precedes issuance.
Slice02 closed at `c1c832647eb82b67f3acad0c72c00a817308ac34`.

## Source inspection and complete assigned contexts

SOURCE is `dffa504e851b03b8e4746f1941068e4cc850b612`. These 17 contexts cover
168 selected lines in five files. They are inspection windows, not 17 claims or
whole-file acceptance. CDC read all selected lines. CC inventories every
substantive assertion within these windows before judging the token assertions;
read additional qualifying context when a window cuts a sentence or explanation.

| Pinned path | Inclusive contexts | Full file lines | Whole-file SHA-256 |
|---|---|---:|---|
| `knowledge/design/SKILL.md` | 34, 56, 70, 102–115, 249, 270, 368 | 368 | `57833e7cecd5984bf1cd6c7b26def1194f7cbbdf83e24a4960bd739a6f26ff63` |
| `knowledge/design/guides/design.md` | 61–80, 158–180, 329–334, 371–376 | 425 | `e4953fd1452102c98df6f0fcf33bc17bd3732f011180475daa8fd256e70e687b` |
| `knowledge/design/guides/colour.md` | 14, 234–248, 564–567 | 581 | `7187dabc5ca00d5d7c48c2a70dd2155731cbf68716c7cb8b1a0d3579285a0aea` |
| `knowledge/design/guides/foundations-of-design.md` | 88–113, 465–503 | 647 | `f4cff1c1edc0ece2a368ff81f3bb1909db9b50c1767281300223f88b83f54aa4` |
| `knowledge/design/guides/layout.md` | 124–131 | 990 | `361ea7887a69870db6db7aa362455b00b5cf718d6c4ae0d49405785fd5c82aec` |

Token-system assertions are in scope: layer/role rules and analogy, DTCG format,
type/composite and conformance attributions, named-system architecture and
naming, theme/alias propagation and its conditions. C&B wording stays literal in
subjects; proposed portable guidance implements the already settled removal.
The layout window is a boundary witness: cascade layers are a different object
from token-alias tiers. Documentation's six categories are also a different object.
Inventory other assertions in the selected windows with an explicit boundary
and owner: typography/spacing mathematics, colour-format/browser-support/industry-trend
and empirical colour/perception claims
remain T/L; documentation organization and whole-file composition remain L/Arc04;
accessibility tests remain Arc03. Do not accept these through token comparisons.

## Primary evidence prepared for inspection

Public pages inspected 2026-10-10. These observations have no immutable original
capture or lineage. They support bounded technical comparison when independently
reinspected; they do not resolve P10-11. Publication/package versions are unknown
unless a source below explicitly supplies one. No copied palette is proposed.

| Primary source | Required sections / observed scope | Author observation and limit |
|---|---|---|
| [DTCG Format Module](https://www.designtokens.org/tr/2025.10/format/) | 2025.10, final Community Group report dated 28 October 2025; Abstract/Status, §1, §3.6–3.9, §4, §5.2.2, §6 introduction/6.1, §8 type headings, §9 introduction/9.2/9.8 and definitions needed by the assessed claims | Defines JSON interchange, grouping and typing. Published scope does not prescribe a universal three-tier role vocabulary. Typography's five required properties are defined; validate their types before promising conformance. This is not a W3C standards-track specification. |
| [Material Web theming](https://material-web.dev/theming/material-theming/) | Full short page: design tokens, reference, system and component tokens | Describes reference/system/component tokens; component tokens permit system aliases or concrete values. Palette/motion implementation limits appear on this page. Material Web documentation is bounded implementation evidence, not proof of every Material Design generation. |
| [Fluent 2 tokens](https://fluent2.microsoft.design/design-tokens) | Full short page, including global/alias and theming context | Names two layers. This counters a universal required-three-tier assertion; it does not establish every implementation's internals or superiority of two layers. |
| [Carbon colour overview](https://www.carbondesignsystem.com/building-blocks/foundations/color/overview) | What is a colour token; anatomy/themes; core/component tokens with surrounding definitions | Page displays last updated 25 September 2026 and a v11 design-kit reference. Roles, theme values, core/component categories and visual layering must not be collapsed into one tier vocabulary. Installed package version was not determined. |
| [Utopia type calculator](https://utopia.fyi/type/calculator/) | CSS Generator configuration and complete generated CSS example | The inspected default example uses numbered `step` properties and `clamp`; prefix and generation method are configurable. This is naming/example evidence, not proof that every configuration must use clamp or a new arithmetic check. |
| [Polaris React archive](https://github.com/Shopify/polaris-react-archive) | Repository README archive/deprecation notice | Historical React surface is archived. Historical token architecture still requires an accessible passage; repository status alone does not prove that architecture. |
| [Shopify migration](https://shopify.dev/docs/apps/build/app-home/migrate-from-polaris-react) | Introduction and Requirements, including the stated React comparison version and current web-component context | Separates legacy React comparison (13.9.5) from web-component guidance. Do not silently describe the archive as the current system. |

The Material 3 overview URL
`https://m3.material.io/foundations/design-tokens/overview` returned only a
JavaScript-required shell. Both `https://polaris-react.shopify.com/tokens/color`
and `https://shopify.github.io/polaris-react-archive/tokens/color` failed body
retrieval. Search snippets are not full passage reads. CC may recover read-only
access, record the actual scope, or leave that historical comparison blocked
with an owner and re-entry check. Do not infer a missing hierarchy from names.
The newer DTCG draft was not used to substitute for the published module.

## Four difficult author cases

1. **Format versus chosen architecture:** the complete example below keeps the
   original denial of a file format separate from proposed replacement. Inspect
   normative versus explanatory sections; do not call a JSON-shaped CSS example
   a conforming export. No export is produced in this slice.
2. **An actual local consistency pair:** `SKILL.md:114` and `design.md:175–177`
   both require semantic rather than primitive component references. They agree
   as local policy; Material Web's concrete-value permission is counterevidence
   to a universal industry restriction, not an internal conflict between those
   two local statements. Conversely, `colour.md:245` is a preview-chip style,
   not automatically a component-token binding. Compare the actual object/use.
3. **Fluent's two layers:** read the complete global/alias distinction. Reject
   the inference that all systems must have three tiers. Also reject the stronger
   unsupported inference that Fluent has no component-level choices anywhere.
4. **Polaris generations and inaccessible evidence:** archive status is known;
   historical token layering is not established by that notice. Preserve a gap
   rather than manufacture either agreement or contradiction. Current URL
   inspection cannot prove an earlier author's verification process.

## One complete author record and discriminating checks

The following standard-library example consumes pinned source bytes. The
technical verdict below is a human judgment from the stated primary sections;
the checker proves literal identity, reference shape and three specific invalid
upgrades. It does not mechanically prove the verdict or inspect the website.
Run from SOURCE root; print observations, not a generated result file.

```python
import copy, hashlib, json, subprocess
revision = "dffa504e851b03b8e4746f1941068e4cc850b612"
path = "knowledge/design/guides/design.md"
data = subprocess.check_output(["git", "show", revision + ":" + path])
line = data.decode().splitlines()[370]
literal = line.split(" It is a", 1)[0]
record = {
    "claim_id": "AUTHOR-EXAMPLE-FORMAT",
    "subject": {"revision": revision, "path": path, "sha256": hashlib.sha256(data).hexdigest(),
                "span": [371, 371], "assertion": literal},
    "evidence": [{"id": "E1", "type": "technical-source", "url": "https://www.designtokens.org/tr/2025.10/format/",
                  "version": "2025.10", "section": "Abstract and section 4",
                  "observed": "2026-10-10", "snapshot_sha256": None,
                  "observation": "The published module defines a JSON interchange format."}],
    "dimensions": {
        "source_faithfulness": {"outcome": "not assessed", "reason": "No original attribution/capture comparison performed.", "evidence_refs": []},
        "correctness": {"outcome": "contradicted", "reason": "The published format module expressly defines interchange syntax.", "evidence_refs": ["E1"]},
        "scope_attribution": {"outcome": "unsupported", "reason": "An architectural analogy does not replace the module's format scope.", "evidence_refs": ["E1"]},
        "consistency": {"outcome": "not assessed", "reason": "No opposing comparable local proposition supplied for this example.", "evidence_refs": []},
        "relationship_cq_coverage": {"outcome": "not assessed", "reason": "No card edge or CQ is assigned.", "evidence_refs": []}},
    "disposition": {"proposed": "correct", "replacement": "DTCG defines an interchange format for design tokens; semantic roles and token layering are chosen within each design system."},
    "actor": {"name": "Sofie", "role": "CDC", "method": "author preparation"},
    "independent_review": {"state": "pending"}}
def check(r):
    s = r["subject"]
    assert s["revision"] == revision and s["path"] == path and s["span"] == [371, 371]
    assert s["sha256"] == hashlib.sha256(data).hexdigest() and s["assertion"] == literal
    assert set(r["dimensions"]) == set(record["dimensions"])
    ids = {e["id"] for e in r["evidence"]}
    assert all(set(d["evidence_refs"]) <= ids for d in r["dimensions"].values())
    assert all(e["snapshot_sha256"] is None for e in r["evidence"])  # No capture supplied.
    c = r["dimensions"]["consistency"]
    assert c["outcome"] == "not assessed" or c.get("paired_subjects")  # No invented pairing.
check(record)
invalid = []
r = copy.deepcopy(record); r["subject"]["assertion"] = r["disposition"]["replacement"]; invalid.append(r)
r = copy.deepcopy(record); r["evidence"][0]["snapshot_sha256"] = "0" * 64; invalid.append(r)
r = copy.deepcopy(record); r["dimensions"]["consistency"]["outcome"] = "conflicts"; invalid.append(r)
for r in invalid:
    try: check(r)
    except AssertionError: pass
    else: raise AssertionError("invalid example passed")
print(json.dumps({"positive": 1, "invalid_rejected": len(invalid), "semantic_verdict": "human judgment; independent review pending"}))
```

## Preparation receipt and utility

CDC inspected all 17 source contexts, the accepted 83-line review procedure,
DES-008 at Project09 audit revision `795ac75b7d02536e0e95252457ac3282cd17d8d8`,
current parent plans/ledgers, prompt-authoring guidance and protocol revision 2.
The demo is replayed before issue; its actual result is recorded below.
Wrong guide-name lookup and an oversized parent-output read were recovered by
wayfinder navigation and focused reads. They are not successful full-read receipts.
Public-page access failures are retained above; no conversion/package/browser/
accessibility implementation or original capture preparation was performed.

One preparation record provides scope, cases and the bounded demo; no extra
comparison tree or maintained helper is introduced. The proposed CC packet
supports a concrete portable token policy and exact future edits. Its utility
and upkeep cost must be observed at review; actual elapsed effort/tokens are
unknown. File sizes alone will not establish efficiency.

Author demo replay before issuance: exit 0; one positive passed and all three
invalid records were rejected. The printed semantic-verdict limit remains.

Opening-author validation: exact nine-path scope (four new host files, four
parent records and the run register); all 13 project/eight arc criterion rows
and statuses unchanged; nine child rows open. Five pinned file hashes/extents
and 17/168 population bounds agree. Target-aware checks resolved 83 local links
and 24 fragments without failures; source pin/index/tracked bytes and frozen
protocol unchanged. LF/final-newline and `git diff --check` passed. Demo replay
again passed one positive/three invalids. These are author opening checks, not
independent semantic acceptance or a CC execution receipt.
