# Slice01 execution notes

Date: 2026-10-09. Assignment: initial `cc-prompt.md`, issued planning commit
`3e5fc9b089c95c5ab97aa25917644a7d83895f28`. Source pin:
`dffa504e851b03b8e4746f1941068e4cc850b612`. Shared Project09 audit pin:
`795ac75b7d02536e0e95252457ac3282cd17d8d8`. Project decisions before opening:
`290b21ffa084ed5b892e5b5c5dd295622b77c8bb`.

## Checkout and preservation preflight

- `git worktree list`: implementation checkout `/Users/oubiwann/lab/billosys/ai-engineering` on `main`; planning checkout at `.worktrees/planning` on `planning`.
- Source `git status --short --branch`: `## main...origin/main`, one pre-existing `?? knowledge/lfe/`. Source HEAD equals the pin. It was excluded and left untouched.
- Planning HEAD equals the issued-assignment commit above. Before outputs, `git status --short --branch` showed `## planning...origin/planning [ahead 4]` and no changes.
- Audit and synthesis were read from the shared planning tree; both input bytes remain untouched. Audit SHA-256 `4b2417ec2dd70690d360709a81d9bc2f13a64b4520cb36bf2063e25f2eb4d93e` was rechecked against planning commit `795ac75b7d02536e0e95252457ac3282cd17d8d8` and matches. Synthesis working SHA-256: `314035750f94e36d9d572cfb06f70bc6de20199a78f8872691bc965b38854bde`.
- No checkout was reset, cleaned or staged. No source, card, source-holding, Makefile, package, installation or Project09 file was edited.

## Required-reading coverage and contract readback

Required planning text was read in full: Project10 `project-plan.md` and
`ledger.md`; Arc01 `arc-plan.md` and `ledger.md`; Slice01 `slice-plan.md`,
`ledger.md`, this issued prompt, and `artifacts/author-reconnaissance.md`.
The Project09 `audit-results-design.md` (187 lines) was recovered in bounded
contiguous reads after the first combined output truncated; lines 1–98 and
99–186 were inspected. The audit records DES-001–016 and expressly limits its
card work to complete inventory/search plus targeted semantic checks. The
synthesis read covered lines 1–95, including all of “The central
recommendation” and all of “Proposed 1.5”; its 2.0 material was reference-only.

The current source entrypoint `knowledge/design/SKILL.md` (368 lines) and
`knowledge/design/version-history.md` (8 lines) were read completely. The six
guide files received a complete heading/brand/domain/font/palette/prescription
scan. Relevant surrounding sections were read for each change-map decision:

- `guides/design.md`: seven principles and deeper structure (95–385), tools
  and technology, including DTCG and variable-font claims.
- `guides/colour.md`: brand and neutral scales, site accents, semantic-token
  uses, site demonstrations and rationale (1–245, 234–474, 474–544,
  544–574).
- `guides/type.md`: typeface rationales, scale and specimens, per-site examples,
  axis settings, rejected alternative and scale rationale (1–135, 133–245,
  246–378, 379–499).
- `guides/layout.md`: identity and premises (1–75), fluid interpolation
  assertions (164–228), all seven precepts and their tests (263–486), token
  endpoints (487–530), and the `vi`/text-resize claim (913–950).
- `guides/foundations-of-design.md`: entry claims, source/empirical claims,
  mathematical models, cross-domain analogies, token assertions and source
  availability (1–90, 213–320, 321–410, 410–520, 550–591).
- `guides/breaking-the-layout-monoculture.md`: empirical/causal claims, CSS
  capability claims, all seven approaches and their interaction consequences,
  references (1–90, 82–170, 393–520, 537–589).

Required method texts were read completely or through each named section:

- Source `knowledge/concept-cards/SKILL.md` (158 lines), complete.
- `knowledge/concept-cards/guides/08-validation-verification.md` (231 lines),
  complete; includes the entire opening through review-actor provenance,
  `Perform Semantic Verification`, and `Prevent False Upgrades`.
- `knowledge/concept-cards/guides/07-reconciliation.md` (139 lines), required
  sections `Establish Targets And Conflict Scope`, `Compare Evidence Before
  Deciding`, and `Keep Lifecycle Results Separate`.
- `knowledge/document-extraction/guides/03-output-contract.md` (108 lines),
  required `Homes And Identity`, `Locator Semantics`, and `Readiness By
  Intended Use`.
- `knowledge/testing/guides/03-validation-gates.md` (107 lines), complete,
  including `Proportionate Proof`.
- Source `Makefile` lines 230–335 include the complete `pack_skill` definition
  and `design` target. The recipe selects `SKILL.md`, sibling history and the
  complete guides directory; it does not select cards or sources.

The collaboration-framework skill was loaded. Project-management wayfinder,
entrypoint and required active-work files (scales, canonical worktree and
planning-top-down guides) were read from its installed source. The referenced
`docs/PROJECT-MANAGEMENT.md` does not exist in the current main checkout; the
installed current framework guides supplied the applicable planning mechanics.

### Contract readback (CC self-attestation; not intake acceptance)

- **Outputs:** `baseline-files.tsv`, `card-source-index.jsonl`,
  `source-readiness.md`, `portability-contract.md`, these notes, slice-ledger
  evidence/disposition notes, and a row-by-row proposed closing report.
- **Immutable inputs:** pinned source tree at `dffa504e…`; Project09 audit and
  synthesis at planning pin `795ac75b…`; issued Project10 plans and this prompt.
  The local untracked LFE directory is excluded. The agreed card population,
  C&B removal decision, no-bridge decision, and `sources/md/` convention are
  binding.
- **Inventory versus semantics:** this slice hashes every tracked design file,
  projects literal top-level card fields and source-reference bodies, and
  assesses source availability. It does not verify card claims, relationships,
  competency-question coverage, or the 233-card corpus semantically.
- **Source-gap handling:** source availability is reported by exact asserted
  source identity, preserving missing originals, locator/edition ambiguity,
  and unassessed semantic support. Required gaps block dependent semantic
  readiness and Project10 completion; absence is not falsity. Slice02 owns
  source acquisition/preparation needs and review method; Slice03 owns accepted
  contract composition and Arc02 allocation.
- **Proposal authority:** source-derived observations and settled Operator
  decisions are separated from the seven-principle wording/configuration
  proposals. No teaching wording becomes normative until CDC/Operator adopts
  it. Contract cases are analytical checks, not performance trials.

## Exact population and card-query results

Enumeration query: `git ls-tree -r --full-tree -z
dffa504e851b03b8e4746f1941068e4cc850b612 -- knowledge/design/`. The complete
tree contained 402 regular tracked blobs. Classification predicates were
`concept-cards/ => card`, `sources/ => source`, and `SKILL.md`,
`version-history.md`, or `guides/ => live`; no unexpected path class or
non-regular entry occurred. Each working file was compared byte-for-byte with
`git show <pin>:<path>`; filesystem existence/addition/deletion and
`git ls-files --others --exclude-standard -- knowledge/design/` were checked.
Results: 233 cards, 161 source files, eight live files; no mismatches, missing
files, or untracked design paths. Exact paths, byte sizes and SHA-256 values
are in `baseline-files.tsv`.

Card query: take each manifest row with `scope == card`; read raw UTF-8 bytes;
SHA-256 those bytes; split frontmatter on exact `---` lines; for each required
key use the top-level expression `^<key>\\s*:\\s*(.*)$` and preserve the
trimmed literal right-hand side; find exact `# Source Reference` headings and
retain the exact decoded source substring after the heading through the line
before the next level-one heading, including original line endings/blank lines.
JSONL is one object per card, sorted by path. A second pass independently
reconstructed and compared every card hash, all eight projected fields,
source-reference status and exact body substring against source bytes.

Results: 233 JSONL rows, 233 unique paths, exact equality with the manifest card
path set, zero direct-comparison problems. All eight projected scalar keys
occur once in each card; no malformed frontmatter, repeated keys or
block-style multiline values were found. Explicit YAML `null` occurs for
`pdf_page` in 83 cards and `section` in 75; these remain literal `"null"`.
Every card has exactly one source-reference heading. The 233 cards group by
collection as Arnheim 112, Munsell 19, posts 46, Butterick 37, and Tschichold
19. They group by exact raw `source` + `authors` values into eight identities:
Arnheim 112; Cleland 19; Butterick 37; Tschichold 19; Working With Colors
Guide 12; More Meaningful Typography 10; A Perceptual Color Space for Image
Processing 13; Okhsv and Okhsl 11. Collection labels were not substituted for
source identity. The local JSONL output retains escapes and quotes exactly.

Atomic witness: source card SHA-256 is
`6893b56903b9b662a5b29c7abff176be6050159844ea6be166a4ae896ab639fa`. Literal
`pdf_page: 4` and `Source Reference` “Chapter 4: I. Hue, pp. 4-6.” preserve an
asserted locator, but neither establish a physical/printed PDF page basis. The
complete card's `Verification Notes` separately call the prose-based
construction source, modern OKLCH mapping not in the 1937 text, and an algebra
cross-reference checked against planned cards; these are card assertions, not
original-source verification in this slice. The card itself is not the
original-source witness.

Mapped-content query: the four posts files were read at their identifying
title/author passage and relevant section witnesses; the Butterick conversion
report and index were inspected, and every one of the 37 mapped cards' section
strings was checked against the complete 156-file prepared-content tree. Exact
title matches are not universal because converted heading/frontmatter forms
differ; those mapping ambiguities remain visible for Slice02. Observed post
witnesses include the Oklab article's title/introduction and XYZ-to-Oklab
section, Brown's title/author and explicit passage that scale values are
suggestions and may be optically adjusted, the Okhsv/Okhsl title and picker
sections, and Drasner's title/author, color-mixing and accessibility sections.
No full fidelity claim follows from these identifying passages.

## Checks not triggered or not run

- The prompt expressly does not trigger source metadata/version/package gates,
  build, install, browser, assistive-technology or usability checks. None was
  run for this assignment. The Project09 audit's prior build remains historical.
- No source acquisition, private-storage search, download, purchase, conversion,
  reusable validator, experiment harness, or 233-card semantic review was run.
- **Final direct checks:** an independent standard-library Python pass reran
  `git ls-tree -r --full-tree -z <source-pin> -- knowledge/design/`, compared
  all 402 manifest rows to working bytes and `git show <pin>:<path>`, and
  independently reconstructed every one of the 233 index objects including
  exact decoded body substrings. Result: exact path-set equality; all hashes,
  sizes, fields, collections and bodies match; zero discrepancies. A working
  scope check found exactly the seven allowlisted outputs and no other changed
  planning path. The same pass found zero trailing-whitespace issues and a
  final newline in every output.
- Planning `git diff --check`: exit 0, no output. Markdown local-file and
  heading-anchor check covered six Markdown records (including preserved
  author reconnaissance); zero unresolved local links/anchors.
- Final source status remained `## main...origin/main`, with only pre-existing
  `?? knowledge/lfe/`; source HEAD remained the pin. `git diff --exit-code --
  knowledge/design/ knowledge/concept-cards knowledge/design/sources` exited 0.
  Audit bytes matched the pinned blob as recorded above. No outside-scope path
  was staged. The closing report records the subsequent explicit-path commit.

## Iteration01 corrective pass 2026-10-09

Assignment: `cc-prompt-iteration01.md`, issued in planning commit
`fa0b2ad43527b8a1973c4848f291b82051aebc4c` (the actual assignment commit).
Reviewed initial CC commit: `0e0c1d0a6b9f451a9328036b0af035e5405cafa8`.
Source remained `dffa504e851b03b8e4746f1941068e4cc850b612`; audit remained
`795ac75b7d02536e0e95252457ac3282cd17d8d8`. Explicit working roots were SOURCE
`/Users/oubiwann/lab/billosys/ai-engineering`, PLANNING
`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`, and this
SLICE. On preflight, SOURCE was at its pin with only excluded pre-existing
`?? knowledge/lfe/`; PLANNING was at the assignment commit with unrelated
`?? project12-chcd-protocol/`. Both were left untouched.

### Fresh audit read and retained historical receipt

The initial receipt above recorded planning audit lines 1–98 and 99–186 of a
187-line required-full file. That receipt is incomplete: line 187 was not in its
recorded extents. It is retained as historical evidence, not silently upgraded.
For this corrective pass, from PLANNING, I freshly read the complete pinned blob
with three contiguous commands:

```sh
git show 795ac75b7d02536e0e95252457ac3282cd17d8d8:project09-design-audit/artifacts/audit-results-design.md | sed -n '1,65p'
git show 795ac75b7d02536e0e95252457ac3282cd17d8d8:project09-design-audit/artifacts/audit-results-design.md | sed -n '66,130p'
git show 795ac75b7d02536e0e95252457ac3282cd17d8d8:project09-design-audit/artifacts/audit-results-design.md | sed -n '131,187p'
```

Observed extents are 1–65, 66–130 and 131–187: all 187 lines including the
final sentence about independent acceptance, commits/releases/source edits, and
administrative relocation. SHA-256 of this pinned blob and the planning working
file was `4b2417ec2dd70690d360709a81d9bc2f13a64b4520cb36bf2063e25f2eb4d93e`.
The old receipt remains explicitly incomplete; this fresh read resolves current
intake coverage without asserting that line 187 was observed earlier.

### Population/hash and literal-field/body replay

Working directory SOURCE; excluded untracked `knowledge/lfe/`. The compact
queries below were run against the pinned tree and the unchanged original
manifest/index. No filesystem bytes were normalized.

```python
import csv, hashlib, json, pathlib, re, subprocess
SOURCE = pathlib.Path("/Users/oubiwann/lab/billosys/ai-engineering")
PLANNING = pathlib.Path("/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning")
SLICE = PLANNING / "project10-design-foundations/arc01-portable-contract/slice01-scope-and-portability-contract"
manifest = list(csv.DictReader((SLICE / "artifacts/baseline-files.tsv").open(), delimiter="\t"))
index = [json.loads(line) for line in (SLICE / "artifacts/card-source-index.jsonl").read_text().splitlines()]
pin = "dffa504e851b03b8e4746f1941068e4cc850b612"
tree = subprocess.check_output(["git", "ls-tree", "-r", "--full-tree", "-z", pin, "--", "knowledge/design/"])
tree_paths = set()
for entry in tree.split(b"\0"):
    if entry:
        meta, path = entry.split(b"\t", 1)
        tree_paths.add(path.decode())
assert tree_paths == {row["path"] for row in manifest}
for row in manifest:
    actual = (SOURCE / row["path"]).read_bytes()
    pinned = subprocess.check_output(["git", "show", f"{pin}:{row['path']}"])
    assert len(actual) == int(row["bytes"])
    assert hashlib.sha256(actual).hexdigest() == row["sha256"]
    assert actual == pinned
```

Actual result: 402 tree entries and 402 manifest rows; exact path-set equality;
scopes `card=233`, `source=161`, `live=8`; zero size/hash/pinned-blob
mismatches. The preexisting baseline was not rewritten.

For each of the 233 index objects, the direct comparison reread pinned working
card bytes; split the frontmatter on exact `---` lines; applied
`re.match(r"^" + re.escape(key) + r"\s*:\s*(.*)$", line)` for the eight
specified keys, preserving each trimmed right-hand side; extracted the exact
`# Source Reference` body through the next level-one heading; and compared the
path, SHA-256, collection, all raw field lists, heading status and body to the
JSONL object. The direct projection/comparison was:

```python
keys = ("concept", "slug", "source", "source_slug", "authors", "chapter", "pdf_page", "section")
for row in index:
    raw = (SOURCE / row["path"]).read_bytes()
    lines = raw.decode("utf-8").splitlines(keepends=True)
    close = next(i for i in range(1, len(lines)) if lines[i].rstrip("\r\n") == "---")
    fields = {key: [] for key in keys}
    for line in lines[1:close]:
        for key in keys:
            match = re.match(r"^" + re.escape(key) + r"\s*:\s*(.*)$", line)
            if match:
                fields[key].append(match.group(1).strip())
    headings = [i for i, line in enumerate(lines) if line.rstrip("\r\n") == "# Source Reference"]
    body = None if len(headings) != 1 else "".join(lines[headings[0] + 1:next(
        (j for j in range(headings[0] + 1, len(lines)) if re.match(r"^# ", lines[j])), len(lines))])
    status = "present" if len(headings) == 1 else "missing" if not headings else "ambiguous"
    assert row["sha256"] == hashlib.sha256(raw).hexdigest()
    assert row["collection"] == row["path"].split("/")[3]
    assert fields == row["source_fields_raw"]
    assert status == row["source_reference_status"] and body == row["source_reference_raw"]
```

Result: 233 unique index paths equal to the manifest card path
set; zero mismatches across hashes, collection names, eight literal fields,
heading statuses or exact bodies. A first diagnostic attempt used the wrong
path-component index for `collection` and falsely flagged all 233 rows; the
comparison was corrected to the immediate collection component (`path.split("/")[3]`)
and rerun, yielding zero discrepancies. This was a query defect, not an input
or artifact discrepancy.

### Raw source grouping and corrected membership oracle

The eight JSON records in `source-readiness.md` were read back from its fenced
JSON block, parsed with `json.loads`, and applied to all parsed index objects
using literal equality (no YAML decoding):

```python
report = (SLICE / "artifacts/source-readiness.md").read_text()
block = re.search(r"```json\s*(.*?)```", report, re.S).group(1)
parsed_json_records = json.loads(block)
members = [[r for r in index
    if r["source_fields_raw"]["source"][0] == g["source_raw"]
    and r["source_fields_raw"]["authors"][0] == g["authors_raw"]]
    for g in parsed_json_records]
expected = {
    ('"Art and Visual Perception: A Psychology of the Creative Eye"', '"Rudolf Arnheim"'): 112,
    ('"A Practical Description of The Munsell Color System"', '"T. M. Cleland"'): 19,
    ('"The New Typography"', '"Jan Tschichold"'): 19,
    ("\"Butterick's Practical Typography\"", "\"Matthew Butterick\""): 37,
    ('"Working With Colors Guide"', '"Sarah Drasner"'): 12,
    ('"More Meaningful Typography"', '"Tim Brown"'): 10,
    ('"A Perceptual Color Space for Image Processing"', '"Bj\\u00f6rn Ottosson"'): 13,
    ('"Okhsv and Okhsl"', '"Bj\\u00f6rn Ottosson"'): 11,
}
assert len(parsed_json_records) == len(set((g["source_raw"], g["authors_raw"]) for g in parsed_json_records)) == 8
assert {(g["source_raw"], g["authors_raw"]): len(v) for g, v in zip(parsed_json_records, members)} == expected
assert sum(map(len, members)) == 233
assert all(sum(r in v for v in members) == 1 for r in index)
display_by_pair = {}
for line in report.splitlines():
    if line.startswith("| `"):
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        title, author = cells[0].split(" — ", 1)
        author = author.split(" (literal metadata", 1)[0]
        display_by_pair[tuple(json.loads(cells[2].strip("`")))] = (title.strip("`"), author)
negative_control = [sum(1 for r in index
    if r["source_fields_raw"]["source"][0] == display_by_pair[(g["source_raw"], g["authors_raw"])][0]
    and r["source_fields_raw"]["authors"][0] == display_by_pair[(g["source_raw"], g["authors_raw"])][1])
    for g in parsed_json_records]
assert negative_control == [0] * 8
```

The required identity mapping, independent of table position, is: Arnheim 112;
Cleland 19; Tschichold 19; Butterick 37; Drasner 12; Brown 10; Oklab 13; Okhsv
and Okhsl 11. Result: eight distinct pairs; exact counts preserved; 233-card
union; each of 233 rows selected exactly once. Negative control: for each of
the eight groups, comparing the quoted raw field to its unquoted display title
and display author returned `[0, 0, 0, 0, 0, 0, 0, 0]` matches. The corrected
report keeps literal equality; it does not normalize display strings or decode
the literal `\\u00f6` author sequence.

### Mapped-content query replay and locator limits

Post capture checks searched case-insensitively for the previously recorded
identifying title/author/headings and witness phrases in exactly these four
pinned prepared files. For `working-with-colours.md`, all four checks were true:
`Working With Colors`, `Sarah Drasner`, `Color mixing`, `Accessibility and Other
Things to Note about Color`. For `more-meaningful-typography.md`, all three
checks were true: `More Meaningful Typography`, `Tim Brown`, `Modular scales
are a tool`. For `a-perceptual-colour-space.md`, all three checks were true:
`perceptual color space for image processing`, `Oklab in 2020`, and `Converting
from XYZ to Oklab`. For `okhsv-and-okhsl.md`, all three checks were true:
`Okhsv and Okhsl`, `Color picking before computers`, and `What makes a good
color picker?`. These are capture-identification/search witnesses only; they do
not prove capture fidelity or semantic support.

```python
posts = {
    "working-with-colours.md": ["Working With Colors", "Sarah Drasner", "Color mixing", "Accessibility and Other Things to Note about Color"],
    "more-meaningful-typography.md": ["More Meaningful Typography", "Tim Brown", "Modular scales are a tool"],
    "a-perceptual-colour-space.md": ["perceptual color space for image processing", "Oklab in 2020", "Converting from XYZ to Oklab"],
    "okhsv-and-okhsl.md": ["Okhsv and Okhsl", "Color picking before computers", "What makes a good color picker?"],
}
for filename, needles in posts.items():
    text = (SOURCE / "knowledge/design/sources/md/posts" / filename).read_text().casefold()
    print(filename, [needle.casefold() in text for needle in needles])

butterick = [r for r in index if
    r["source_fields_raw"]["source"][0] == '"Butterick\'s Practical Typography"' and
    r["source_fields_raw"]["authors"][0] == '"Matthew Butterick"']
files = sorted((SOURCE / "knowledge/design/sources/md/practical-typography").glob("*.md"))
corpus = [(path, path.read_text(errors="replace").casefold()) for path in files]
for row in butterick:
    raw = row["source_fields_raw"]["section"][0]
    section = raw[1:-1] if raw.startswith('"') and raw.endswith('"') else raw
    hits = [path.name for path, text in corpus if section.casefold() in text]
    print(row["path"].rsplit("/", 1)[-1], section, len(hits), hits)
```

For Butterick, from SOURCE, the query selected the 37 cards with exact raw pair
`"Butterick's Practical Typography"` / `"Matthew Butterick"`, removed only the
outer YAML double-quote delimiters from each raw `section` scalar, and searched
that case-folded substring in each of the 156 prepared `.md` files under
`knowledge/design/sources/md/practical-typography/`. It reported card slug,
section, hit count and candidate filenames. The compact table below omits only
the `.md` suffix from each returned basename; the query block above prints the
suffix. Results for every card:

| Card | Section | Matching `.md` files (substring candidates) |
|---|---|---|
| all-caps | All Caps | 30: all-caps, alternate-figures, are-two-spaces-better-than-one, block-quotations, bold-or-italic, century-supra, concourse, courier-alternatives, emoticons-and-emoji, equity, font-basics, headings, heliotrope, hermes-maia, how-to-use, letterspacing, mixing-fonts, one-space-between-sentences, opentype-features, paragraph-and-character-styles, point-size, rules-and-borders, small-caps, summary-of-key-rules, text-formatting, the-scorpion-express, triplicate, typewriter-habits, underlining, valkyrie |
| alternate-figures | Alternate Figures | 10: all-caps, alternate-figures, concourse, grids-of-numbers, heliotrope, hermes-maia, monospaced-fonts, opentype-features, ordinals, text-formatting |
| block-quotation | Block Quotations | 3: block-quotations, line-length, page-layout |
| body-text | Body Text | 42: all-caps, alternate-figures, are-two-spaces-better-than-one, billionaires-typewriter, body-text, bold-or-italic, calibri-alternatives, century-supra, charter, color, concourse, courier-alternatives, equity, font-basics, headings, heliotrope, how-to-use, letterhead, letterspacing, ligatures-in-programming-fonts-hell-no, ligatures, maxims-of-page-layout, metrics-vs-optical-spacing, mixing-fonts, monospaced-fonts, page-layout, parentheses-brackets-and-braces, point-size, presentations, research-papers, responsive-web-design, resumes, space-between-paragraphs, summary-of-key-rules, system-fonts, the-scorpion-express, triplicate, typewriter-habits, typography-2020, typography-in-ten-minutes, valkyrie, websites |
| columns | Columns | 10: alternate-figures, columns, grids, line-length, monospaced-fonts, page-break-before, page-layout, rules-and-borders, tables, tabs-and-tab-stops |
| curly-quotes | Straight and Curly Quotes | 8: apostrophes, foot-and-inch-marks, ligatures-in-programming-fonts-hell-no, straight-and-curly-quotes, summary-of-key-rules, type-composition, typewriter-habits, where-do-the-rules-come-from |
| em-unit | Em Sizing | 2: appendix, em-sizing |
| first-line-indent | First-Line Indents | 11: block-quotations, bulleted-and-numbered-lists, first-line-indents, grids, headings, letterhead, page-layout, paragraph-and-character-styles, research-papers, space-between-paragraphs, summary-of-key-rules |
| font-pairing | Mixing Fonts | 3: bulleted-and-numbered-lists, mixing-fonts, text-formatting |
| font | Font Basics | 2: font-basics, font-recommendations |
| good-typography | What Is Good Typography | 4: are-two-spaces-better-than-one, billionaires-typewriter, what-is-good-typography, why-typography-matters |
| headings | Headings | 23: all-caps, bold-or-italic, centered-text, hard-line-breaks, hard-page-breaks, headings, hierarchical-headings, hyphenation, keep-lines-together, keep-with-next-paragraph, letterspacing, mixing-fonts, page-break-before, paragraph-and-character-styles, point-size, research-papers, resumes, rules-and-borders, small-caps, space-above-and-below, text-formatting, underlining, websites |
| hyphenation | Hyphenation | 12: block-quotations, body-text, headings, hyphenation, hyphens-and-dashes, justified-text, ligatures, optional-hyphens, page-layout, research-papers, summary-of-key-rules, why-theres-no-e-book-or-pdf |
| hyphens-and-dashes | Hyphens and Dashes | 10: acknowledgments, ellipses, em-sizing, hyphens-and-dashes, math-symbols, point-size, rules-and-borders, summary-of-key-rules, type-composition, typewriter-habits |
| justified-text | Justified Text | 6: alternate-figures, hyphenation, justified-text, page-layout, research-papers, summary-of-key-rules |
| kerning | Kerning | 13: all-caps, color, font-basics, kerning, letterspacing, metrics-vs-optical-spacing, oscars-2020, parentheses-brackets-and-braces, small-caps, summary-of-key-rules, text-formatting, the-scorpion-express, typewriter-habits |
| letterspacing | Letterspacing | 17: all-caps, business-cards, century-supra, concourse, equity, headings, heliotrope, hermes-maia, kerning, letterspacing, paragraph-and-character-styles, small-caps, space-above-and-below, summary-of-key-rules, text-formatting, typewriter-habits, valkyrie |
| ligatures | Ligatures | 17: accented-characters, ampersands, are-two-spaces-better-than-one, commentary, concourse-index, emoticons-and-emoji, ligatures-in-programming-fonts-hell-no, ligatures, math-symbols, opentype-features, question-marks-and-exclamation-points, text-formatting, triplicate, type-composition, typewriter-habits, typography-2020, widow-and-orphan-control |
| line-length | Line Length | 16: block-quotations, body-text, columns, hyphenation, letterhead, line-length, maxims-of-page-layout, page-layout, page-margins, point-size, research-papers, responsive-web-design, resumes, summary-of-key-rules, typewriter-habits, typography-in-ten-minutes |
| line-spacing | Line Spacing | 16: are-two-spaces-better-than-one, block-quotations, body-text, columns, grids-of-numbers, line-spacing, maxims-of-page-layout, page-layout, page-margins, paragraph-and-character-styles, point-size, presentations, research-papers, summary-of-key-rules, typewriter-habits, typography-in-ten-minutes |
| opentype-features | OpenType Features | 18: advocate, all-caps, alternate-figures, bad-fonts, century-supra, concourse-index, concourse, equity, font-basics, heliotrope, hermes-maia, opentype-features, ordinals, small-caps, text-formatting, the-scorpion-express, triplicate, valkyrie |
| optical-vs-metric-spacing | Metrics vs. Optical Spacing | 6: introduction, justified-text, kerning, metrics-vs-optical-spacing, minion-alternatives, text-formatting |
| page-layout-maxims | Maxims of Page Layout | 8: business-cards, grids, how-to-use, identifying-fonts, letterhead, maxims-of-page-layout, page-layout, presentations |
| page-margins | Page Margins | 13: columns, grids, letterhead, line-length, page-layout, page-margins, research-papers, responsive-web-design, resumes, screen-reading-considerations, space-above-and-below, typewriter-habits, typography-in-ten-minutes |
| paragraph-flow-control | Widow and Orphan Control | 3: keep-lines-together, page-layout, widow-and-orphan-control |
| paragraph-spacing | Space Between Paragraphs | 11: carriage-returns, columns, first-line-indents, grids, letterhead, page-layout, page-margins, paragraph-and-section-marks, space-above-and-below, space-between-paragraphs, summary-of-key-rules |
| point-size | Point Size | 33: all-caps, are-two-spaces-better-than-one, block-quotations, body-text, bulleted-and-numbered-lists, business-cards, color, em-sizing, equity, first-line-indents, headings, letterspacing, line-length, line-spacing, maxims-of-page-layout, metrics-vs-optical-spacing, mixing-fonts, monospaced-fonts, page-margins, paragraph-and-character-styles, point-size, presentations, research-papers, responsive-web-design, screen-reading-considerations, space-above-and-below, space-between-paragraphs, summary-of-key-rules, text-formatting, typewriter-habits, typography-in-ten-minutes, underlining, websites |
| responsive-typography | Responsive Web Design | 4: appendix, introduction, line-length, responsive-web-design |
| rules-and-borders | Rules and Borders | 7: all-caps, grids-of-numbers, paragraph-and-character-styles, rules-and-borders, signature-lines, tables, typewriter-habits |
| sentence-spacing | One Space Between Sentences | 10: are-two-spaces-better-than-one, carriage-returns, one-space-between-sentences, research-papers, signature-lines, summary-of-key-rules, triplicate, type-composition, typewriter-habits, word-spaces |
| small-caps | Small Caps | 20: bold-or-italic, century-supra, concourse, courier-alternatives, equity, font-basics, heliotrope, hermes-maia, how-to-use, letterspacing, mixing-fonts, opentype-features, paragraph-and-character-styles, small-caps, summary-of-key-rules, text-formatting, the-scorpion-express, triplicate, underlining, valkyrie |
| tables | Tables | 9: bulleted-and-numbered-lists, grids-of-numbers, page-layout, rules-and-borders, space-above-and-below, tables, tabs-and-tab-stops, typewriter-habits, why-racket-why-lisp |
| typewriter-habits | Typewriter Habits | 12: all-caps, appendix, are-two-spaces-better-than-one, billionaires-typewriter, line-spacing, page-margins, research-papers, rules-and-borders, straight-and-curly-quotes, tables, typewriter-habits, websites |
| typographic-color | Color | 27: alternate-figures, are-two-spaces-better-than-one, bibliography, business-cards, color, grids-of-numbers, headings, kerning, letterhead, letterspacing, maxims-of-page-layout, metrics-vs-optical-spacing, mixing-fonts, oscars-2020, presentations, printers-and-paper, resumes, screen-reading-considerations, small-caps, space-above-and-below, text-formatting, the-cowardice-of-brave, the-scorpion-express, times-new-roman-alternatives, typography-2020, typography-2024, websites |
| typographic-emphasis | Bold or Italic | 14: bold-or-italic, color, headings, introduction, mixing-fonts, paragraph-and-character-styles, parentheses-brackets-and-braces, rules-and-borders, small-caps, space-above-and-below, straight-and-curly-quotes, summary-of-key-rules, text-formatting, underlining |
| typographic-grids | Grids | 14: alternate-figures, business-cards, columns, grids-of-numbers, grids, headings, introduction, maxims-of-page-layout, page-layout, paragraph-and-character-styles, presentations, sample-documents, tables, tabs-and-tab-stops |
| typography | What Is Typography | 4: acknowledgments, drowning-the-crystal-goblet, what-is-typography, why-typography-matters |

Result: 156 prepared Markdown files searched; 37 of 37 section strings had at
least one substring hit and all 37 had multiple candidates (range 2–42 files).
There were zero unmatched strings. Those hits are ambiguous locators, not
validated mappings or semantic/source verification; candidate paths above are
retained so Slice02 can resolve them. The five broken links remain as stated by
the pinned conversion report. An initial wrapper search command used the
planning-relative index path while cwd was SOURCE and failed before reading any
index rows; it was rerun from the correct explicit path. A first search summary
then raised an `AttributeError` after printing candidate rows because its
aggregation treated filename strings as path objects; it was rerun with corrected
aggregation and produced the complete 37-row result above. A first post-witness
probe used two nonmatching paraphrase needles for Brown/Oklab; exact report
witness phrases were substituted and the final four-file query returned all
stated checks true.

### Corrective output and preservation checks

The report JSON is independently parsed from its fenced block (not from the
index or an in-memory construction), then compared against the exact grouped
index strings. Corrected population/count/negative-control results are recorded
above. Preservation/output checks used these direct predicates:

```sh
SOURCE=/Users/oubiwann/lab/billosys/ai-engineering
PLANNING=/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
git -C "$SOURCE" rev-parse HEAD
git -C "$SOURCE" diff --exit-code dffa504e851b03b8e4746f1941068e4cc850b612 -- knowledge/design/ knowledge/concept-cards/
git -C "$PLANNING" show 795ac75b7d02536e0e95252457ac3282cd17d8d8:project09-design-audit/artifacts/audit-results-design.md | shasum -a 256
git -C "$PLANNING" diff --name-only
git -C "$PLANNING" diff --cached --name-only
git -C "$PLANNING" diff --check
```

Actual results: source HEAD and every design/concept-card working byte remained
at the source pin; audit working bytes equaled the pinned blob and SHA-256.
`baseline-files.tsv`, `card-source-index.jsonl`, and
`portability-contract.md` were byte-identical to reviewed commit `0e0c1d0a`.
Author reconnaissance, slice plan, both issued prompts and CDC verification were
byte-identical to assignment commit `fa0b2ad4`. The exact worktree diff was the
four allowed paths (this file, `source-readiness.md`, `closing-report.md`, and
`ledger.md`); no staged paths existed. All seven ledger statuses remained open.
All four changed files had final newlines and zero trailing-whitespace lines;
planning `git diff --check` exited 0. A target-aware local Markdown check found
25 local links, 19 fragment links, and zero unresolved files/anchors. Its first
version incorrectly checked every target fragment against the referring file,
reporting 19 false unresolved anchors; corrected validation loaded each target
file and resolved all 19. No source/card/package or shared Project09 file was
changed. The unrelated untracked SOURCE and PLANNING paths named above were
excluded.

The first execution of the retained query snippets found a syntax error in the
Butterick expected-pair string (unescaped apostrophe); the snippet was corrected,
then all four recorded Python blocks ran successfully, including the 37-row
Butterick query. This documentation defect did not change any source or index
bytes or the completed membership result.

## Iteration02 corrective pass 2026-10-09

### Intake and bounded disposition

This pass executes assignment commit
`bcc720753dae9eb7e96388890e85ead5e9fb115a`, issued after CDC review commit
`fa0b2ad4` and iteration01 proposed output `7000ff4df723dcf00728d1507ad63a118566651e`.
The active source pin remains
`dffa504e851b03b8e4746f1941068e4cc850b612`; the shared audit pin remains
`795ac75b7d02536e0e95252457ac3282cd17d8d8`. The initial prompt and iteration01
prompt remain binding. I reread the project, arc, and slice plans and ledgers,
the full CDC verification, this complete execution record, the closing report,
and the issued iteration02 prompt. The only output corrections were the
Butterick `headings` candidate basename and the two heading strings identified
by CDC-S01-03/04. The prior membership, population, metadata, audit, and source
evidence was retained because its pinned inputs and criteria are unchanged.

The reviewed iteration01 candidate row for `headings` had 23 entries but
substituted `summary-of-key-rules` for `text-formatting`. Replaying the recorded
query against the pinned raw membership index and all 156 prepared Markdown
files compared the exact candidate basename sets, section string, and count for
all 37 Butterick cards. Before correction the result was 36 exact rows and one
mismatch; for `Headings`, the query returned 23 and the recorded row returned
23, with symmetric difference `{summary-of-key-rules, text-formatting}`. The
corrected row now contains `text-formatting`, retains count 23, and excludes
`summary-of-key-rules`. The historical equal-count row is a negative control:
its set equality remains false. The post-correction replay is recorded below;
the comparison is by set, so display ordering does not affect the result.

```python
import json, re, subprocess
from pathlib import Path
SOURCE = Path("/Users/oubiwann/lab/billosys/ai-engineering")
PLANNING = Path("/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning")
SLICE = PLANNING / "project10-design-foundations/arc01-portable-contract/slice01-scope-and-portability-contract"
index = [json.loads(s) for s in (SLICE / "artifacts/card-source-index.jsonl").read_text().splitlines() if s]
cards = [r for r in index if r["source_fields_raw"]["source"][0] == '"Butterick\'s Practical Typography"' and r["source_fields_raw"]["authors"][0] == '"Matthew Butterick"']
files = sorted((SOURCE / "knowledge/design/sources/md/practical-typography").glob("*.md"))
corpus = [(p.stem, p.read_text(errors="replace").casefold()) for p in files]
query = {}
for r in cards:
    raw = r["source_fields_raw"]["section"][0]
    section = raw[1:-1] if raw.startswith('"') and raw.endswith('"') else raw
    query[r["path"].rsplit("/", 1)[-1].removesuffix(".md")] = (section, len([1 for _, t in corpus if section.casefold() in t]), {n for n, t in corpus if section.casefold() in t})
def candidate_rows(text):
    out = {}
    for line in text.splitlines():
        if not line.startswith("| ") or line.startswith(("| Card |", "|---")): continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 3: continue
        m = re.fullmatch(r"(\d+):\s*(.*)", cells[2])
        if m: out[cells[0].strip("`")] = (cells[1], int(m.group(1)), {x.strip().removesuffix(".md") for x in m.group(2).split(",") if x.strip()})
    return out
actual = candidate_rows((SLICE / "artifacts/execution-notes.md").read_text())
old_text = subprocess.check_output(["git", "show", "7000ff4df723dcf00728d1507ad63a118566651e:" + str((SLICE / "artifacts/execution-notes.md").relative_to(PLANNING))], cwd=PLANNING, text=True)
old = candidate_rows(old_text)
assert len(cards) == len(query) == len(actual) == len(old) == 37 and len(files) == 156
assert all(actual[k] == query[k] for k in query)
assert [k for k in query if old[k] != query[k]] == ["headings"]
assert old["headings"][:2] == query["headings"][:2] == ("Headings", 23)
assert old["headings"][2] ^ query["headings"][2] == {"summary-of-key-rules", "text-formatting"}
assert min(len(v[2]) for v in query.values()) == 2 and max(len(v[2]) for v in query.values()) == 42
```

The replay output was: **37 cards; 156 prepared files; 37 section/count/set
comparisons; corrected mismatches 0; historical mismatches 1; candidate range
2–42**. The negative-control `headings` row retained section `Headings` and
count 23, failed set equality, and differed only by
`summary-of-key-rules`/`text-formatting`. The corrected row includes
`text-formatting` and excludes `summary-of-key-rules`.

### Heading fragments and local links

CDC-S01-04 identified two headings whose em dash produced double hyphens under
the established anchor algorithm, while their existing links used one hyphen.
The prior heading strings, recorded here as prose, were “Iteration01 corrective
pass — 2026-10-09” and “Iteration01 corrective addendum — proposed done.” They
generated `iteration01-corrective-pass--2026-10-09` and
`iteration01-corrective-addendum--proposed-done`, respectively. The headings now
read `Iteration01 corrective pass 2026-10-09` and `Iteration01 corrective
addendum proposed done`; the body text and referring fragments are preserved.
The anchor rule removes punctuation, replaces each ordinary space with one
hyphen, and does not collapse consecutive hyphens. A target-aware replay over
execution notes, closing report, ledger, and preserved source-readiness found
25 local links, 19 fragment links, zero missing files, and zero unresolved
anchors. Both repaired headings now derive the single-hyphen fragments already
used by their links. The historical heading forms are a negative control: each
derives a double-hyphen anchor and fails its prior single-hyphen link.

```text
before: 25 local links / 19 fragments / 3 mismatched fragments
after:  25 local links / 19 fragments / 0 missing files / 0 mismatched fragments
```

The final link replay covered these three changed records and preserved
`artifacts/source-readiness.md`. The first attempted source-index lookup used a
nonexistent source-relative path; it failed before reading index rows and was
rerun against the planning artifact `artifacts/card-source-index.jsonl`. A
first comparator then retained the `.md` suffix in card keys and raised a
`KeyError`; the corrected comparator stripped the suffix and completed all 37
comparisons above. A first link pass after adding four extra ledger links found
29/23 links/fragments (all resolving); the ledger was narrowed to evidence-note
edits without adding links, and the required final pass returned 25/19. One
audit digest command initially named `design-synthesis.md`, which is not the
pinned artifact path; it was rerun with the exact `audit-modernization-synthesis.md`
path. These command corrections changed no protected inputs.

### Preservation, scope, and limits

The source checkout remains at the source pin and the scoped design/concept-card
working diff is empty. Both audit inputs remain byte-identical to the pinned
audit commit. Immutable reviewed files still match `7000ff4d`; issued prompt,
slice plan, and CDC record still match assignment commit `bcc7207`. The only
changed planning paths are this execution record, `closing-report.md`, and
`ledger.md`; there are no staged paths. All three files have final newlines, no
trailing whitespace, and `git diff --check` passes. The unrelated untracked
`project12-chcd-protocol/` and source `knowledge/lfe/` remain excluded.

Resolved findings: CDC-S01-03 is limited to the candidate-list transcription
`summary-of-key-rules` -> `text-formatting`, with the recorded count and all
other 36 candidate sets unchanged. CDC-S01-04 is limited to the two heading
punctuation edits; existing bodies and link text remain unchanged. All seven
ledger rows remain open for CDC. No unresolved data or validation failure
remains. Transient query/helper invocation errors and their corrected reruns
are recorded above.

Unrun or still blocked: no semantic review of the 233 cards, original-source
acquisition, browser/accessibility review, package/build validation, or source
implementation was performed. The 150 missing-original cards and unresolved
source fidelity remain assigned downstream. Candidate substring hits remain
ambiguous locators. Bubble-up: none; this correction requires no change to
project or arc scope. CC proposes this iteration done for independent CDC
review; it is not CDC acceptance, slice closure, or authorization to open
Slice02.
