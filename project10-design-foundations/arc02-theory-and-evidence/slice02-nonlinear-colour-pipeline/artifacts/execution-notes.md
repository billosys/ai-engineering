# CC execution notes and intake receipts

## Worktree, issuing set, and authority

- Planning checkout: `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`, branch `planning`; issuing/open-set HEAD `208b12239cd59ccc6877b2edc0358054b27652c2`. The initial prompt at that commit has blob `fa2ba34a41d6f05df63ec0093c8ca0cd01b5b154` and current SHA-256 `25c7805ccc9e0b5f7d0813252e04cccbcf1314a64d0fdcb4f3c96fd9662d1baa`. Slice-plan SHA-256 `51912a554b6d6bb81f36d71ce928c1580b960b7c27059c7532d223f3c0fc69cd`; opening ledger SHA-256 `9cfe66d95324d8353866aa520db5bd07a7c5dd183db9ab2eda1792c39f19dd3c`.
- SOURCE/main: `dffa504e851b03b8e4746f1941068e4cc850b612`, branch `main`, tracked/index clean at opening and at recheck. Existing untracked SOURCE `knowledge/lfe/` and planning `project12-chcd-protocol/` were preserved without inspection. No SOURCE or prompt/plan edits were made.
- The nine opening ledger rows remain open. This is CC-proposed evidence returned for CDC review; it is not acceptance, closure, or authority to open Slice03.
- Assignment authority is the exact initial `cc-prompt.md` above, interpreted under slice-plan §§1–7 and its seven-path contract. Slice01 predecessor `9a306c6f49d61b9350e6b84d454da449deca5891` and independent closure `c3d68d7d` were checked as retained evidence; their arithmetic was not replayed as this slice’s proof.

## Required reading receipts

All listed SOURCE inputs were read from the pinned Git worktree. Hashes below identify local pinned files; specified historical artifacts were read from their named Git revisions.

| Input | Actual scope loaded | Identity / receipt |
|---|---|---|
| SOURCE `AGENTS.md` | Full 216 lines | SHA-256 `cf56f5e91c923811c6a620edb125dffcbc44be2980783c7deec5bf2a2ce258cc` |
| Installed collaboration-framework skill | Full 538 lines | `/Users/oubiwann/.agents/skills/collaboration-framework/SKILL.md`; SHA-256 `63a924ef9fb841b01f1013f0e1e73fc13a95d76de2bd4ff8c1f1a024cbdeecae`; required framework posture and methodology routes followed |
| Project-management skill and guide README | Full files | `knowledge/project-management/SKILL.md` (65 lines); `knowledge/project-management/guides/README.md` (178 lines); Expedited Mode and slice close/bubble-up route loaded |
| Engineering-methodology guide | Required sections | `knowledge/engineering-methods/guides/01-engineering-methodology.md`: Notes for Codex, Roles and Shared Invariants, full Two-Contributor Workflow up to Three-Contributor heading |
| Ledger/closure and validation guides | Required scopes | `knowledge/work-verification/guides/01-ledger-discipline.md` full 96 lines; `03-row-closure.md` Final Statuses through CC working protocol; `knowledge/testing/guides/03-validation-gates.md` Gate Selection and Proportionate Proof |
| Prompt authoring | Required sections | `knowledge/engineering-methods/guides/07-implementation-prompt-authoring.md`, Required Reading and CC Intake, including readback/receipts/truncation recovery |
| Active project, arc and slice authority | Current project/arc/slice plans and ledgers; initial prompt | Project10 plan and ledger; Arc02 plan and ledger; this slice plan/ledger/prompt. Exact prompt, slice-plan and ledger identities appear above. Arc02 includes the T-family boundary and preserves the complete R/T/C/L/G and 233-card/eight-live-file obligations. |
| Design skill and assigned live spans | Full `knowledge/design/SKILL.md` (368 lines); all six assigned spans (89 lines) across `foundations-of-design.md`, `design.md`, and `colour.md` | SKILL SHA-256 `57833e7cecd5984bf1cd6c7b26def1194f7cbbdf83e24a4960bd739a6f26ff63`; foundations `f4cff1c1edc0ece2a368ff81f3bb1909db9b50c1767281300223f88b83f54aa4`; design `e4953fd1452102c98df6f0fcf33bc17bd3732f011180475daa8fd256e70e687b`; colour `7187dabc5ca00d5d7c48c2a70dd2155731cbf68716c7cb8b1a0d3579285a0aea` |
| Contextual counterwitness card | Full 147 lines; only assigned conversion teaching claims inventoried | `knowledge/design/concept-cards/posts/matrix-transformation-colour.md`, SHA-256 `872e8c6c5e360401d1f5332ae755a5c21542d09536221e28652e305f136fc680` |
| Prepared Oklab article | Required lines 75–113 and 115–163, including XYZ equations, four examples, actual C++ forward/inverse code and generation/use-case note | `knowledge/design/sources/md/posts/a-perceptual-colour-space.md`, SHA-256 `ffe5494da6f0d040fb341d8e1f03d3e396600f6787088b6d57e32613798375f4` |
| Accepted composition contract | Required Authority/Evidence, Claim Categories/Evidence Boundary, and complete Source-readiness/claim-result procedure | Git revision `38b66d0de7d5e8cba98e7d588075f5c6d4ede90f`; `artifacts/composed-contract.md` |
| Accepted review procedure | Full 83 lines, EOF verified | Git revision `759ce2dd116a4cfe03b72d43fd2791f48486251c`; SHA-256 `a72c820ddfe4804e6056f1785b01e572473186e91a33ee87b757085c984752db` |
| Accepted Arc02 handoff | Required S02-08/P10-11 through proposed stage order and final paragraph, including all eight action rows | Git revision `38b66d0de7d5e8cba98e7d588075f5c6d4ede90f`; `artifacts/arc02-handoff.md` |
| DES-002 / DES-007 audit | Complete assigned sections | Git revision `795ac75b7d02536e0e95252457ac3282cd17d8d8`; `audit-results-design.md` DES-002 and DES-007 |
| Current CSS Color 4 technical text | §9.2, §9.4–9.6, §10.2–10.3, §19 non-normative notice and named functions | W3C CSS Color 4 Candidate Recommendation Draft dated 2026-10-09, retrieved 2026-10-10: https://www.w3.org/TR/2026/CRD-css-color-4-20261009/ . Public page inspection only; no local immutable snapshot hash. |
| Oklab public article | “Converting from XYZ to Oklab” through end of “Converting from linear sRGB to Oklab”, before “Motivation and derivation of Oklab” | https://bottosson.github.io/posts/oklab/ retrieved 2026-10-10. No immutable snapshot hash or complete archival capture. Prepared local copy is the pinned calculation input, not proof of original fidelity. |

Relationship/CQ components, GPU/ICC application assertions, other unassigned card claims, unrelated type/unit/neuroscience assertions, the remainder of the design files, source acquisition, and empirical perception evidence were not assessed. No conditional extension requiring another normative source was triggered. Decorative prepared heading anchors were used only to locate the assigned passages.

## Readback of the binding contract

- **Bounded result (slice-plan §§1–2; S02-01/02):** establish a mathematical correction basis for DES-007 and only the overlapping colour/uniformity/temperament assertions in DES-002. Inventory all six live spans plus assigned counterwitness teaching claims. Keep other card dimensions, relationships/CQs, full guide/card populations, and the arc’s remaining R/C/L/G work outside this result.
- **Actual-source interpretation (slice-plan §§2–4; S02-03/04):** use pinned prepared bytes. Keep the 2021-01-25 linear-sRGB combined matrix A and inverse separate from the article’s standalone XYZ M1/M2 examples. Decode encoded sRGB, use signed real roots and inverse cubes, avoid clipping, and compare the fixed complete populations with unrounded values. Matrix composition applies to adjacent linear stages only.
- **Evidence limits (slice-plan §§5–6; S02-02/06):** identify source spans and five separate outcomes. A numerical/model result does not supply missing original capture fidelity; public technical reading is not an immutable archival original. Arithmetic does not establish universal perceptual brightness, accessibility, contrast, palette quality, or equal-temperament identity. Treat CSS powerless hue separately from analytic polar coordinates.
- **Authority (prompt; S02-07/09):** CC proposes the occurrence-linked evidence and corrections; CDC independently reviews and decides row acceptance; Operator retains the recorded gates. All nine rows remain open here. No live edits, source acquisition, next slice, or C&B defaults.
- **Output/validation gate (slice-plan §Results and seven-path contract; S02-08):** produce only the five assigned artifacts plus ledger Evidence/Notes updates and closing report; check exact joins, case/control coverage, references, paths and bytes; commit those exact seven paths with both required trailers. No Make/package/browser test is assigned; retain those gates for later applicable implementation.

## Calculation method and recovery log

The assigned calculation used a one-off Python 3 standard-library script in `/tmp/make_slice02.py`; it is not a repository artifact or maintained tool. It reads the pinned Markdown bytes and extracts matrix rows by the displayed `\begin{pmatrix}` boundaries. For C++ expressions it captures each signed decimal coefficient and variable term from the three `float l/m/s` forward lines, three inverse LMS-prime lines (adding the printed `c.L` coefficient 1), and three returned inverse-A lines. Assertions check three rows of three coefficients in each matrix. It uses binary64, `math.copysign(abs(x)**(1/3), x)` for signed real roots, the stated piecewise sRGB functions, and full precision for comparisons; presentation values have at least 12 fractional digits. Inputs and outputs are generated directly from extracted actual coefficients; printed expected outputs are not used to compute them.

Recorded failed/recovered operations:

1. First matrix locator was over-escaped and raised `ValueError: substring not found`; the next query used the literal single-backslash Markdown marker and found one row block for each matrix.
2. The first inverse coefficient regex dropped signs separated by spaces and asserted; inspection of actual C++ lines exposed this. A sign-aware coefficient parser was used and the inverse matrices were confirmed as `[[4.0767416621,-3.3077115913,0.2309699292],[-1.2684380046,2.6097574011,-0.3413193965],[-0.0041960863,-0.7034186147,1.7076147010]]` and inverse LMS-prime rows `[[1,0.3963377774,0.2158037573],[1,-0.1055613458,-0.0638541728],[1,-0.0894841775,-1.2914855480]]`.
3. A selector initially searched inverse return rows by coefficient variable position and raised `StopIteration`; actual initializer showed each variable appears in every row. Selection was corrected to the literal `return { ... };` block and retained row order.
4. A standalone sanity print indexed the one-eighth linear-white row while labelling it middle grey; this was caught against case IDs. The final artifact selects `middle-gray` by its actual row ID/index (the twelfth encoded case (zero-based index 11)) and reports correct L `0.598180726623`, not the one-eighth value.
5. A command used slice-relative shorthand without the `project10-design-foundations/` prefix and returned three “No such file” errors. The correct paths were then read; no writes occurred from the failed command.

The LF/EOF validator first found doubled terminal blank lines in `closing-report.md` and `correction-handoff.md`; both were reduced to one LF before rerunning the validator. A population-check draft then counted `linear-*` names in both RGB and polar tables and returned 32 instead of 16; the query was scoped to the RGB section headings before rerun (the artifacts contain 16 RGB rows and 20 separate polar rows). None of these attempts changed or weakened the model, case set, controls, or tolerances. No scope-dependent input was blocked. Missing original capture remains a blocked fidelity dependency.

## Check status and independent boundary

The numerical artifact records 16 round trips, four XYZ rows/12 comparisons, 20 polar returns, and all three contrary controls. Calculated maxima: encoded `1.6839126291304935e-6` (corner-7 blue); linear `2.6128459884589006e-7` (linear white blue); XYZ printed-table difference `0.00039741995991940393` (Z-basis L); polar `1.734723475976807e-16`. Fixed tolerances passed. CSS and article statements were read for technical context, not used to claim browser behavior or archival fidelity.

No Make, package, browser automation, accessibility certification, empirical study, complete card/live-file review, or source-fidelity replay was run or assigned. There is no standalone maintained runtime to validate. `git diff --check`, JSONL parse/join checks, exact-path diff, line/link/EOF review and commit-tree verification are performed at finalization and recorded in the closing report. No test suite is being added.


## Iteration01 — fresh intake and corrected evidence (2026-10-10)

### Authority, pins, and read receipts

- Issuing planning revision: `1a1fb44b25f7558f46b9395e9cf6e4b3bc71f145`; issued prompt blob `fd73d993e69c0e6fc6607d6c8d0032c7ef605fe0`, SHA-256 `0cf78fcb28bfbc975d899c8088441367e7f3eef7c608a48487b5ea6d7282d4d3`. This execution follows its F01–F05 and exact six-path allowlist. Source remains `dffa504e851b03b8e4746f1941068e4cc850b612`; no SOURCE writes.
- Planning status at intake was clean tracked state with one unrelated untracked `project12-chcd-protocol/`; preserved and not inspected. Main/source checkout was pinned and clean for tracked files with unrelated untracked `knowledge/lfe/`; preserved and not inspected. Worktree list confirmed `planning` and `main` locations.
- Required workflow sources were freshly read: installed `collaboration-framework/SKILL.md` (538 lines, SHA-256 `63a924ef9fb841b01f1013f0e1e73fc13a95d76de2bd4ff8c1f1a024cbdeecae`); source `AGENTS.md` (216 lines, `cf56f5e91c923811c6a620edb125dffcbc44be2980783c7deec5bf2a2ce258cc`); project-management skill (65 lines, `3b60b8bf6b407465da80c9d00ecb2700d2bccca3716b120cbaccb3a1f5822d19`) and guide README (178 lines, `5de496704990ba211f31707f2bfaaa467b66e51555d1232c19420284ae6a4280`); engineering-methodology guide (427 lines, `7a768d90d3bc4d41302a6fcd91cbe831bda177020833b5b94d7d7fe3c1854672`); ledger discipline (96 lines, `06892429a188bdc4e70236a5ac430e5f04cae1a9690a4c025d291ed6d417d09a`); row closure (81 lines, `8947d3ab72d59422d0f90f7fb041f7e3131ce85e190c04985937e63ef1737a5b`); validation gates (107 lines, `3862c66eaa5614099d62a3ee0c3aa296fc66de2a605876cac98a7fbfd01a88aa`); prompt authoring (475 lines, `890fdc8e83aff3f130524d8f3af3f0614d41c63e221e90348bc7493c23c75d6f`). Relevant authority/workflow and intake sections were read in full; the project-management guide confirms CC proposal versus independent CDC row acceptance.
- Current Project10 project plan/ledger, Arc02 arc-plan/ledger, Slice02 plan/ledger, initial and iteration prompts, and CDC review were read from the planning worktree. Existing CDC acceptance is retained only for S02-03 and S02-05; its seven findings remain open. The exact review method is `project10-design-foundations/arc01-portable-contract/slice02-source-and-review-readiness/artifacts/review-procedure.md`, revision `759ce2dd116a4cfe03b72d43fd2791f48486251c`, SHA-256 `a72c820ddfe4804e6056f1785b01e572473186e91a33ee87b757085c984752db`. The composed contract and Arc02 handoff were read at `38b66d0de7d5e8cba98e7d588075f5c6d4ede90f`; DES-002/DES-007 audit sections at `795ac75b7d02536e0e95252457ac3282cd17d8d8`.
- Design `SKILL.md` (368 lines, `57833e7cecd5984bf1cd6c7b26def1194f7cbbdf83e24a4960bd739a6f26ff63`), all six original live passages (89 lines total), the added foundations continuation 451–456, and contextual ranges were checked against pinned source. The card is 147 lines (`872e8c6c5e360401d1f5332ae755a5c21542d09536221e28652e305f136fc680`); new required card reads include 33–35, 67–68, 81–88, 92–93, 121, 125–129, and 142–147. Prepared article is 504 lines, SHA-256 `ffe5494da6f0d040fb341d8e1f03d3e396600f6787088b6d57e32613798375f4`; exact calculation extents are 75–113 excluding decorative line 100, and 115–163. The source ranges expose XYZ M1 line 91, M2 line 93; printed table 107–110; combined RGB A lines 126–128, roots 130–132, B 135–137; inverse LMS-prime 143–145, cubes 147–149, inverse A 152–154; generation/use note 159–161.
- Public technical context was reread on 2026-10-10: CSS Color 4 Candidate Recommendation Draft dated 2026-10-09, §§9.2, 9.4–9.6, 10.2–10.3, and §19 named functions; URL `https://www.w3.org/TR/2026/CRD-css-color-4-20261009/`. It is a work-in-progress public draft, not an immutable source capture or endorsement. The original public Oklab article was read through the linear-sRGB conversion section, URL `https://bottosson.github.io/posts/oklab/`; no immutable snapshot hash is asserted. Neither public read supplies original-to-prepared fidelity lineage.
- Historical ranges and receipts in the preceding initial section are retained as historical, including old prepared XYZ M2 and C++ locator errors and the initial seven-output scope. They are not silently relabeled as current reads. This intake corrects the coefficient locators and expands the allowlist to the issued six paths.

### Iteration results and recovery record

- F01: 42 clause-level result records cover the six original live spans / 89 source lines, substantive foundations lines 451–455 plus contextual continuation line 456, 18 original ID/span envelopes, and the required contextual card teaching spans. The full 147-line card and prepared-source 88-line assigned ranges are separate contextual reads. The 18 original IDs remain directly recoverable and every split clause names its origin ID. The card’s full 147-line inventory is contextual; unassigned claims, relationships/CQs, GPU/ICC behavior, and the rest of the source population remain out of scope. No “all other claims” completion statement is used.
- F02: each of 42 clauses has five separately reasoned dimensions. It distinguishes the subject witness, exact prepared model, supporting/qualifying/contradicting evidence, and paired context. Source-history attribution remains separate from numeric truth. Grassmann attribution and universal perception claims are not falsely disproved by arithmetic. Blocked fidelity clauses name the missing capture/manifest, owner, and falsifiable re-entry; independent math is not held for unrelated originals.
- F03: the prior 16 RGB, four XYZ, and 20 polar table values are preserved verbatim. Corrected XYZ M1/M2 locators and exact A/B/inverse spans are stated. New tables expose the 16 forward/inverse RGB stages, four XYZ stages, and 20 polar conversions. Candidate values are checked from full precision with the original tolerances and without clipping.
- F04: the handoff now contains literal proposed replacement text for every assessed clause, with exact IDs and spans, plus DES-007, limited DES-002, R/T/C/L/G, Arc03–05, P10-11 and Operator responsibilities. Fidelity is gated per dependent result. Practical input space/white point, output gamut, alpha/background/compositing and foreground/background/state pair are retained as future requirements. No C&B-specific default is proposed.
- Failed/recovered attempts during this iteration: an RGB-variable regex was first applied to the differently written B-row expressions; it returned no terms. The parser was corrected to capture the actual `l_`, `m_`, `s_` operators. A whitespace sign token then failed float parsing and was normalized without dropping signs. A generator typo passed a scalar into `map`; corrected before values were written. A replay draft attempted matrix composition with a vector-only multiplication helper; replaced with explicit 3×3 multiplication. The polar-stage parser initially missed the negative-lightness row; it now accepts signed values and checks all 20 rows. A rerun was detected to duplicate the appended stage section; numerical output was reset from the immutable fd73 baseline and regenerated once. These were local tooling errors, not model changes. The earlier initial-attempt failures remain documented above.

### Self-contained replay

Save the fenced program as `/tmp/replay_iter01.py`, change to the planning worktree, and run `python3 /tmp/replay_iter01.py`. It reads source bytes from the pinned SOURCE Git revision and candidate tables/claim records from this slice; it compares the candidate’s printed vectors and stage rows to recalculation, checks all original tolerances, and exercises each negative control through its positive predicate. The code is reproduced here in full.

```python
from pathlib import Path
import subprocess, hashlib, json, math, re
ROOT=Path.cwd(); SRC=Path('/Users/oubiwann/lab/billosys/ai-engineering')
BASE=Path('project10-design-foundations/arc02-theory-and-evidence/slice02-nonlinear-colour-pipeline')
ART=ROOT/BASE/'artifacts'; REV='dffa504e851b03b8e4746f1941068e4cc850b612'
def git(path): return subprocess.check_output(['git','-C',str(SRC),'show',f'{REV}:{path}']).decode()
def sha(b): return hashlib.sha256(b).hexdigest()
def mv(M,v): return tuple(sum(a*b for a,b in zip(row,v)) for row in M)
def mm(X,Y): return tuple(tuple(sum(X[i][k]*Y[k][j] for k in range(3)) for j in range(3)) for i in range(3))
def cbrt(x): return math.copysign(abs(x)**(1/3),x)
def dec(x): return x/12.92 if x<=.04045 else ((x+.055)/1.055)**2.4
def enc(x): return 12.92*x if x<=.0031308 else 1.055*x**(1/2.4)-.055
prep=git('knowledge/design/sources/md/posts/a-perceptual-colour-space.md').splitlines()
assert len(prep)==504 and 'M_1' in prep[90] and 'M_2' in prep[92]
assert '0.4122214708f * c.r' in prep[125] and 'cbrtf' in prep[129] and '0.2104542553f*l_' in prep[134]
assert '0.3963377774f * c.a' in prep[142] and 'l_*l_*l_' in prep[146] and '4.0767416621f' in prep[151]
assert '2021-01-25' in prep[158] and 'sRGB matrices' in prep[160]
def nums(line, pattern): return [float(x.replace(' ','').rstrip('f')) for x in re.findall(pattern,line)]
def terms(line, pattern): return nums(line,pattern)
A=[terms(prep[i],r'([+-]?\s*\d+\.\d+f?)\s*\*\s*c\.[rgb]') for i in (125,126,127)]
B=[terms(prep[i],r'([+-]?\s*\d+\.\d+f?)\s*\*\s*[lms]_') for i in (134,135,136)]
IL=[[1.0]+terms(prep[i],r'([+-]?\s*\d+\.\d+f?)\s*\*\s*c\.[ab]') for i in (142,143,144)]
IA=[terms(prep[i],r'([+-]?\s*\d+\.\d+f?)\s*\*\s*[lms]') for i in (151,152,153)]
assert all(len(row)==3 for M in (A,B,IL,IA) for row in M)
def mat(name,line):
 body=prep[line-1].split(r'\begin{pmatrix}',1)[1].split(r'\end{pmatrix}',1)[0]
 rows=[[float(x) for x in re.findall(r'([+-]?\d+\.\d+)',r)] for r in body.split(r'\\')]
 assert len(rows)==3 and all(len(x)==3 for x in rows); return rows
M1=mat('M1',91); M2=mat('M2',93)
text=(ART/'numerical-reconciliation.md').read_text()
claimtext=(ART/'claim-results.jsonl').read_text().splitlines()
records=[json.loads(x) for x in claimtext]
clauses={r['claim_id']:r for r in records if 'dimensions' in r}
# Parse prior printed RGB candidate values; recalculate every full-precision forward/inverse case.
section=text.split('## 16 RGB forward and inverse cases',1)[1].split('## Four published XYZ examples',1)[0]
rows=re.findall(r'^\| ([^|]+) \| (encoded|linear) \| `\(([^)]*)\)` \| `\(([^)]*)\)` \| `\(([^)]*)\)` \| `\(([^)]*)\)` \|$',section,re.M)
assert len(rows)==16
rgb=[]; max_encoded=(0,None); max_linear=(0,None)
for name,kind,ins,lab_s,ret_s,err_s in rows:
 v=tuple(map(float,ins.split(', '))); lab0=tuple(map(float,lab_s.split(', '))); ret0=tuple(map(float,ret_s.split(', '))); err0=tuple(map(float,err_s.split(', ')))
 lin=tuple(dec(x) for x in v) if kind=='encoded' else v
 lms=mv(A,lin); roots=tuple(cbrt(x) for x in lms); lab=mv(B,roots)
 ip=mv(IL,lab); cubes=tuple(x**3 for x in ip); backlin=mv(IA,cubes); back=tuple(enc(x) for x in backlin) if kind=='encoded' else backlin
 e=max(abs(x-y) for x,y in zip(back,v)); tol=2e-6 if kind=='encoded' else 1e-6
 assert e<=tol and max(abs(x-y) for x,y in zip(lab,lab0))<6e-13 and max(abs(x-y) for x,y in zip(back,ret0))<6e-13
 assert max(abs(x-y) for x,y in zip(tuple(a-b for a,b in zip(back,v)),err0))<6e-13
 if kind=='encoded' and e>max_encoded[0]: max_encoded=(e,(name, max(range(3),key=lambda i:abs(back[i]-v[i]))))
 if kind=='linear' and e>max_linear[0]: max_linear=(e,(name,max(range(3),key=lambda i:abs(back[i]-v[i]))))
 rgb.append((name,kind,v,lin,lms,roots,lab,ip,cubes,backlin,back))
assert sum(k=='encoded' for _,k,*_ in rgb)==13 and sum(k=='linear' for _,k,*_ in rgb)==3
# Stage tables are consumed as candidate outputs; exact names/populations and parsed vectors are checked.
stage=text.split('### RGB forward and inverse stages',1)[1].split('### XYZ example stages',1)[0]
stagerows=re.findall(r'^\| ([^|]+) \| (encoded|linear) \| `\(([^)]*)\)` \| `\(([^)]*)\)` \| `\(([^)]*)\)` \| `\(([^)]*)\)` \| `\(([^)]*)\)` \| `\(([^)]*)\)` \| `\(([^)]*)\)` \| `\(([^)]*)\)` \|$',stage,re.M)
assert len(stagerows)==16
by={r[0]:r for r in stagerows}
for n,k,v,lin,lms,roots,lab,ip,cubes,backlin,back in rgb:
 r=by[n]; assert r[1]==k
 vectors=[lin,lms,roots,lab,ip,cubes,backlin,back]
 got=[tuple(map(float,r[i].split(', '))) for i in range(2,10)]
 assert all(max(abs(a-b) for a,b in zip(x,y))<5.1e-13 for x,y in zip(vectors,got)),n
# XYZ population and pinned table rows, using XYZ M1/M2 only.
xyzrows=re.findall(r'^\| (XYZ-[1-4]) \| `\(([^)]*)\)` \| `\(([^)]*)\)` \| `\(([^)]*)\)` \| `\(([^)]*)\)` \| `\(([^)]*)\)` \| `\(([^)]*)\)` \|$',text.split('### XYZ example stages',1)[1].split('### Polar output stages',1)[0],re.M)
assert len(xyzrows)==4
xyz_full_errors=[]
for n,ins,lms_s,roots_s,lab_s,printed_s,err_s in xyzrows:
 x=tuple(map(float,ins.split(', '))); lms=mv(M1,x); roots=tuple(cbrt(v) for v in lms); lab=mv(M2,roots); printed=tuple(map(float,printed_s.split(', ')))
 assert max(abs(a-b) for a,b in zip(lab,printed))<=.0005
 assert max(abs(a-b) for a,b in zip(lms,map(float,lms_s.split(', '))))<5.1e-13
 assert max(abs(a-b) for a,b in zip(roots,map(float,roots_s.split(', '))))<5.1e-13
 assert max(abs(a-b) for a,b in zip(lab,map(float,lab_s.split(', '))))<5.1e-13
 for channel,(actual,expected) in enumerate(zip(lab,printed)): xyz_full_errors.append((abs(actual-expected),n,channel))
assert len(re.findall(r'^\| XYZ-[1-4] \|',text.split('## Four published XYZ examples',1)[1].split('## Twenty analytic polar',1)[0],re.M))==4
# 20 polar candidates checked against the same full-precision Lab population.
polarrows=re.findall(r'^\| ([^|]+) \| ([0-9.]+) \| ([^|]+) \| `\(([^)]*)\)` \|$',text.split('## Twenty analytic polar round trips',1)[1].split('## Replayed intermediate',1)[0],re.M)
assert len(polarrows)==20
labs={n:lab for n,k,v,lin,lms,roots,lab,ip,cubes,bl,b in rgb}
for n,x,lms,roots,lab,p in []: pass
# XYZ computed Lab from actual source table inputs.
for row in xyzrows:
 n,ins,*_=row; x=tuple(map(float,ins.split(', '))); labs[n]=mv(M2,tuple(cbrt(v) for v in mv(M1,x)))
polar_errors=[]
for n,cstr,hstr,errs in polarrows:
 L,a,b=labs[n]; c=math.hypot(a,b); h=None if c==0 else math.degrees(math.atan2(b,a))%360
 assert abs(c-float(cstr))<6e-13
 if h is None: assert hstr=='undefined'
 else: assert abs(h-float(hstr))<6e-10
 pe=(0.0,abs(c*math.cos(math.radians(h or 0))-a),abs(c*math.sin(math.radians(h or 0))-b)); polar_errors.append((max(pe),n,('L','a','b')[pe.index(max(pe))]))
assert max(e for e,n,c in polar_errors)<=1e-12
polstage=text.split('### Polar output stages',1)[1].split('## Named sanity witnesses',1)[0]
polstage_rows=re.findall(r'^\| ([^|]+) \| (-?[0-9.]+) \| (-?[0-9.]+) \| (-?[0-9.]+) \| ([0-9.]+) \| ([^|]+) \| (-?[0-9.]+) \| (-?[0-9.]+) \| `\(([^)]*)\)` \|$',polstage,re.M)
assert len(polstage_rows)==20
for n,Ls,as_,bs,Cs,Hs,ar,br,es in polstage_rows:
 L,a,b=labs[n]; C=math.hypot(a,b); H=None if C==0 else math.degrees(math.atan2(b,a))%360
 assert abs(float(Ls)-L)<5.1e-13 and abs(float(as_)-a)<5.1e-13 and abs(float(bs)-b)<5.1e-13 and abs(float(Cs)-C)<5.1e-13
 if H is None: assert Hs=='undefined'
 else: assert abs(float(Hs)-H)<5.1e-10
 assert max(abs(x) for x in map(float,es.split(', ')))<=1e-12
# Original numerical controls use same positive predicates: matrix-only scaling, skipped decode, unsigned root.
white=tuple(mv(B,tuple(cbrt(x) for x in mv(A,(1,1,1)))))
one8=tuple(mv(B,tuple(cbrt(x) for x in mv(A,(.125,.125,.125)))))
correct_ratio=abs(one8[0]-.5*white[0])
BA=mm(B,A); matwhite=mv(BA,(1,1,1)); matone8=mv(BA,(.125,.125,.125)); matrix_defect=abs(matone8[0]-.5*matwhite[0])
mid=next(r for r in rgb if r[0]=='middle-gray'); skipped=mv(B,tuple(cbrt(x) for x in mv(A,mid[2]))); skip_defect=abs(skipped[0]-mid[6][0])
xyz4=next(r for r in xyzrows if r[0]=='XYZ-4'); x=tuple(map(float,xyz4[1].split(', '))); lms=mv(M1,x)
try: naive=tuple(v**(1/3) for v in lms); unsigned_real=all(isinstance(v,float) and math.isfinite(v) for v in naive)
except (ValueError,TypeError): unsigned_real=False
assert correct_ratio<5e-10 and matrix_defect>1e-3 and skip_defect>1e-2 and not unsigned_real
# Evidence-inspection validators use source content and evidence applicability.
def coverage_ok(rs):
 return any(r.get('claim_id')=='LIVE-FOUND-005' and r.get('subject',{}).get('span')=={'start':451,'end':456,'basis':f'inclusive SOURCE/main {REV} line numbers'} and 'mathematical equivalence is unsupported' in r.get('subject',{}).get('assertion','') for r in rs)
def full_matrix_ok(r):
 literal='single matrix' in r['subject']['assertion']
 contradicted=r['dimensions']['correctness']['outcome']=='contradicted'
 return literal and contradicted and matrix_defect>1e-3 and 'linear-white' in ' '.join(str(x) for x in r['evidence'])
def coefficient_ok(r):
 app=[x for x in r.get('evidence',[]) if x.get('kind')=='prepared-technical-model' and x.get('span',{}).get('start')==124 and x.get('span',{}).get('end')==139]
 code='\n'.join(prep[123:139])
 has_rgb=all(v in code for v in ('c.r','c.g','c.b')) and 'cbrtf' in code and '0.4122214708f' in code
 return bool(app) and has_rgb and 'linear-sRGB' in r['subject'].get('assessed_clause','')
assert coverage_ok(records)
coverage_mut=[r for r in records if r.get('claim_id')!='LIVE-FOUND-005']
coverage_clip=json.loads(json.dumps(records)); next(r for r in coverage_clip if r.get('claim_id')=='LIVE-FOUND-005')['subject']['assertion']='**Colour harmony ↔ musical harmony (LOOSE to STRUCTURAL).** The 12-hue wheel / 12-semitone parallel is structurally suggestive.'
assert not coverage_ok(coverage_mut) and not coverage_ok(coverage_clip)
fm=clauses['LIVE-FOUND-004-MATRIX']; assert full_matrix_ok(fm)
fm_mut=json.loads(json.dumps(fm)); fm_mut['dimensions']['correctness']['outcome']='supported'; assert not full_matrix_ok(fm_mut)
card=clauses['CARD-007-NAMING']; assert coefficient_ok(card)
wrong=json.loads(json.dumps(card)); ev=next(x for x in wrong['evidence'] if x.get('kind')=='prepared-technical-model' and x.get('span',{}).get('start')==124);ev['span']={'start':93,'end':95,'inclusive':True};assert not coefficient_ok(wrong)
assert len(clauses)==42 and len([r for r in records if r.get('record_kind')=='literal-subject-provenance-envelope'])==18
print('PASS source coefficient/input-space and XYZ table predicates')
print('PASS RGB 13 encoded + 3 linear; 16 inverse; 12 XYZ table components; 4 XYZ inputs; 20 polar')
print('max encoded',format(max_encoded[0],'.16g'),max_encoded[1],'max linear',format(max_linear[0],'.16g'),max_linear[1])
xyzerrs=[(abs(float(v)),row[0],i) for row in xyzrows for i,v in enumerate(row[-1].strip('`()').split(', '))]; xe=max(xyzerrs)
xe=max(xyz_full_errors)
print('max XYZ',format(xe[0],'.16g'),xe[1],('L','a','b')[xe[2]],'published component tolerance 0.0005')
print('max polar',format(max(e for e,n,c in polar_errors),'.16g'),max(polar_errors))
print('PASS original numerical controls: matrix-only rejected, skipped decode rejected, unsigned root rejected; positive witnesses pass')
print('PASS evidence controls: required 451-456 coverage/clipping fail; full-matrix false support fails; wrong coefficient span/input fails')
```

Run command from the planning worktree: `python3 /tmp/replay_iter01.py`. Observed result before commit: exit 0; all positive populations/stages and all six contrary controls reported PASS. Required counts were 13 encoded + 3 linear, 16 inverse returns, 12 printed XYZ table components, four XYZ inputs, and 20 polar rows. Maxima/argmax were encoded `1.683912629130494e-6` at corner-7 channel 2; linear `2.612845988458901e-7` at linear-white channel 2; XYZ `0.000397419959919404` at XYZ-4 L; polar `1.734723475976807e-16` at corner-2 (a component). Three numerical controls: matrix-only, skipped decode, and unsigned root each failed the applicable positive predicate while positive witnesses passed. Three separate evidence controls: deleting the 451–456 occurrence and clipping its required qualification both fail occurrence coverage; falsely tagging the full-matrix claim supported fails its scaling-witness predicate; relabeling a correctly hashed source’s coefficient evidence to M2 lines 93–95 fails operator/input-space applicability. These controls aid review and are not semantic acceptance.

The self-contained program uses Python 3 standard library, binary64, no clipping, no persistent project script/package, and no tests. No Make, packaging, browser, accessibility, empirical perception, source-acquisition, or whole-card/CQ work was run or assigned. Their later gates remain open. Independent CDC must replay the committed blob and decide the seven open criteria.


## Iteration02 execution — 2026-10-10

**Fresh intake/readback.** Issuing prompt commit: `33766ea6a707e6107b236966d776c550108fea99`; prompt blob `f0e75fa00d597facd2e2e8f34dd0d171c223d4ef`, SHA-256 `615b4f2ed9e1bd5415a57aff4a064b9e207b138b6000d614b58291d4d5a978f5`. SOURCE/main remains `dffa504e851b03b8e4746f1941068e4cc850b612`. Required model, subject boundaries, exact six-path allowlist, proof/table values, three CDC-done/six open rows, per-result original-fidelity gate and Operator C&B removal decision are unchanged. Source and prompt pins were read from Git objects; current plan/ledger/prompt/CDC and prior candidate were read from the planning worktree. The two unrelated untracked directories were left untouched. The first authority-receipt pass omitted Project10 ledger lines 33–35 containing P10-11; those lines were then loaded and the recorded range corrected to include all eleven criteria.

### Current self-contained replay program — `ITERATION02_REPLAY_V1`

```python
from pathlib import Path
import subprocess, json, hashlib, math, re, ast, itertools, collections
P=Path.cwd(); S='project10-design-foundations/arc02-theory-and-evidence/slice02-nonlinear-colour-pipeline/'; C='9758f3f81c53272e88632202e12275cefe24a101'; SRC='dffa504e851b03b8e4746f1941068e4cc850b612'; PROC='project10-design-foundations/arc01-portable-contract/slice02-source-and-review-readiness/artifacts/review-procedure.md'; PR='759ce2dd116a4cfe03b72d43fd2791f48486251c'; PREV='fd73d993e69c0e6fc6607d6c8d0032c7ef605fe0'
def git(*a): return subprocess.check_output(['git',*a],cwd=P)
def obj(r,p): return git('show',f'{r}:{p}')
def H(b): return hashlib.sha256(b).hexdigest()
def close(a,b,tol=5.01e-13): return len(a)==len(b) and max((abs(x-y) for x,y in zip(a,b)),default=0)<=tol
def vec(s): return tuple(ast.literal_eval(s.strip().strip('`')))
def rows(section):
 out=[]; started=False
 for line in section.splitlines():
  if line.startswith('|'):
   started=True; c=[x.strip().strip('`') for x in line.split('|')[1:-1]]
   if c and not all(re.fullmatch(r':?-+:?',x) for x in c) and c[0] not in ('Case','Row'): out.append(c)
  elif started: break
 return out
assert git('rev-parse',C+'^').decode().strip()=='33766ea6a707e6107b236966d776c550108fea99'
assert git('rev-parse',SRC).decode().strip()==SRC
outputs=['artifacts/claim-results.jsonl','artifacts/numerical-reconciliation.md','artifacts/correction-handoff.md','artifacts/execution-notes.md','ledger.md','closing-report.md']
assert set(git('diff-tree','--no-commit-id','--name-only','-r',C).decode().splitlines())=={S+x for x in outputs}
msg=git('show','-s','--format=%B',C).decode(); assert 'Co-authored-by: Codex <noreply@openai.com>' in msg and 'Co-authored-by: Billo AI <ai-engineering@billo.systems>' in msg
for f in outputs: assert obj(C,S+f).endswith(b'\n') and b'\r' not in obj(C,S+f)
proof='project10-design-foundations/arc02-theory-and-evidence/slice02-nonlinear-colour-pipeline/artifacts/colour-conversion-proof.md'
assert git('rev-parse',f'{C}:{proof}').decode().strip()=='4171b18d2bf64dcff0a714499d98fb7cbe31df7a'
# Exact current local source and method identities, then literal source-line joins.
proc=obj(PR,PROC); assert len(proc.decode().splitlines())==83 and H(proc)== 'a72c820ddfe4804e6056f1785b01e572473186e91a33ee87b757085c984752db'
source_paths={'knowledge/design/SKILL.md','knowledge/design/guides/foundations-of-design.md','knowledge/design/guides/design.md','knowledge/design/guides/colour.md','knowledge/design/concept-cards/posts/matrix-transformation-colour.md'}
records=[json.loads(x) for x in obj(C,S+'artifacts/claim-results.jsonl').decode().splitlines()]
assert len(records)==70 and len({r['claim_id'] for r in records})==70
assessed=[r for r in records if r.get('record_kind') not in ('literal-subject-provenance-envelope','scope-boundary-decision','duplicate-occurrence-link')]
envelopes=[r for r in records if r.get('record_kind')=='literal-subject-provenance-envelope']
bounds=[r for r in records if r.get('record_kind')=='scope-boundary-decision']; aliases=[r for r in records if r.get('record_kind')=='duplicate-occurrence-link']
assert len(assessed)==49 and len(envelopes)==18 and len(bounds)==2 and len(aliases)==1
assert len({e['evidence_id'] for r in assessed for e in r.get('evidence',[])})==sum(len(r.get('evidence',[])) for r in assessed)
original=[json.loads(x) for x in obj(PREV,S+'artifacts/claim-results.jsonl').decode().splitlines()]
orig={r['claim_id']:r for r in original}; assert len(orig)==18 and {e['claim_id'] for e in envelopes}==set(orig)
for e in envelopes:
 oid=e['claim_id']; assert e['origin_claim_id']==oid and e['subject']==orig[oid]['subject'] and e['assessed_coverage'] is False
 assert all(x in {r['claim_id'] for r in assessed} for x in e['split_clause_ids'])
for r in assessed:
 assert r['method']['path']==PROC and r['method']['git_revision']==PR and r['method']['git_blob']==git('rev-parse',f'{PR}:{PROC}').decode().strip() and r['method']['sha256']==H(proc)
 s=r['subject']; assert s['path'] in source_paths
 b=obj(SRC,s['path']); lines=b.decode().splitlines(); a,z=s['span']['start'],s['span']['end']; assert H(b)==s['sha256'] and git('rev-parse',f'{SRC}:{s["path"]}').decode().strip()==s['git_blob']
 assert '\n'.join(lines[a-1:z])==s['assertion']
 assert set(r['dimensions'])=={'source_faithfulness','correctness','scope_attribution','consistency','relationship_cq_coverage'}
 valid={e['evidence_id'] for e in r.get('evidence',[])}
 for d in r['dimensions'].values(): assert set(d['evidence_refs'])<=valid
 assert all(e['evidence_id'].startswith(r['claim_id']+'::') for e in r.get('evidence',[]))
# The actual article inputs and exact coefficient/operator spans.
prep_path='knowledge/design/sources/md/posts/a-perceptual-colour-space.md'; prep=obj(SRC,prep_path).decode().splitlines()
assert len(prep)==504 and H(obj(SRC,prep_path))=='ffe5494da6f0d040fb341d8e1f03d3e396600f6787088b6d57e32613798375f4'
def coeff(line_numbers):
 out=[]
 for n in line_numbers:
  row=[float(sign+number) for sign,number in re.findall(r'([+-]?)\s*(\d+\.\d+)f',prep[n-1])]
  if len(row)==2: row.insert(0,1.0) # the C++ inverse rows begin with an implicit +1*c.L
  assert len(row)==3
  out.append(row)
 return out
A=coeff((126,127,128)); B=coeff((135,136,137)); BI=coeff((143,144,145)); AI=coeff((152,153,154))
assert all(len(r)==3 for m in (A,B,AI) for r in m) and all(len(r)==3 for r in BI)
def matvec(M,v): return tuple(sum(x*y for x,y in zip(row,v)) for row in M)
def mm(A,B): return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)) for i in range(3))
def cbrt(x): return math.copysign(abs(x)**(1/3),x)
def decode(x): return x/12.92 if abs(x)<=.04045 else math.copysign(((abs(x)+.055)/1.055)**2.4,x)
def encode(x): return 12.92*x if abs(x)<=.0031308 else math.copysign(1.055*abs(x)**(1/2.4)-.055,x)
def fwd(v,M=A): return matvec(B,tuple(cbrt(x) for x in matvec(M,v)))
def inv(v): return matvec(AI,tuple(x**3 for x in matvec(BI,v)))
assert abs(decode(-.5)-(-.21404114048223255))<1e-15 and abs(encode(-.125)-(-.3885728590463344))<1e-15
def determinant(m):
 a,b,c=m;return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])
def literal_matrix(line_no):
 v=[float(t) for t in re.findall(r'[+-]?\d+\.\d+',prep[line_no-1])];assert len(v)==9;return [v[j:j+3] for j in (0,3,6)]
M1=literal_matrix(91);M2=literal_matrix(93);assert abs(determinant(M1)-0.4722768434252936)<1e-15 and abs(determinant(M2)-1.6112316300395422)<1e-15
text=obj(C,S+'artifacts/numerical-reconciliation.md').decode()
# Primary table memberships and all displayed RGB values/errors.
rgbsec=text.split('## 16 RGB forward and inverse cases',1)[1].split('## Four published XYZ examples',1)[0]
rgbs=rows(rgbsec); expected_ids={f'corner-{i}' for i in range(1,9)}|{'neutral-0.04044','neutral-0.04045','neutral-0.04046','middle-gray','mixed','linear-white','linear-white-1/8','linear-negative-white'}
assert {r[0] for r in rgbs}==expected_ids and len(rgbs)==16
cases=[('corner-'+str(i+1),'encoded',v) for i,v in enumerate(itertools.product((0.,1.),repeat=3))]+[('neutral-0.04044','encoded',(.04044,)*3),('neutral-0.04045','encoded',(.04045,)*3),('neutral-0.04046','encoded',(.04046,)*3),('middle-gray','encoded',(.5,)*3),('mixed','encoded',(.2,.4,.6)),('linear-white','linear',(1.,)*3),('linear-white-1/8','linear',(.125,)*3),('linear-negative-white','linear',(-.125,)*3)]
rgbmap={r[0]:r for r in rgbs}; labs={}; maxima={'encoded':(0.,None),'linear':(0.,None)}
for name,kind,x in cases:
 r=rgbmap[name]; assert r[1]==kind and close(vec(r[2]),x,0)
 lin=tuple(decode(v) for v in x) if kind=='encoded' else x; lab=fwd(lin); back=inv(lab); back=tuple(encode(v) for v in back) if kind=='encoded' else back; err=tuple(u-v for u,v in zip(back,x)); labs[name]=lab
 assert close(vec(r[3]),lab) and close(vec(r[4]),back) and close(vec(r[5]),err),(name,r)
 for ch,v in enumerate(err):
  if abs(v)>maxima[kind][0]:maxima[kind]=(abs(v),(name,ch))
# XYZ oracle table is parsed from SOURCE lines 107-110; assert exact four unique source cases and all six printed fields.
table=[]
for line in prep[106:110]:
 if line.lstrip('> ').startswith('|'):
  line=line.lstrip('> ')
  cell=[x.strip() for x in line.split('|')[1:-1]]
  if len(cell)==6 and cell[0].replace('.','',1).isdigit(): table.append(tuple(float(x) for x in cell))
assert len(table)==4
xyzsec=text.split('## Four published XYZ examples',1)[1].split('## Twenty analytic polar round trips',1)[0]
xyzrows=rows(xyzsec); assert {r[0] for r in xyzrows}=={f'XYZ-{i}' for i in range(1,5)} and len(xyzrows)==4
xyzmap={r[0]:r for r in xyzrows}; xyz_labs={}; xyzmax=(0.,None)
for i,oracle in enumerate(table,1):
 name=f'XYZ-{i}'; row=xyzmap[name]; x=oracle[:3]; printed=oracle[3:]; lab=fwd(x,coeff((90,91,92))) if False else None
 # M1/M2 are parsed from their literal matrix rows, not the RGB coefficient set.
 m1rows=[]
 for line_no in (90,):
  nums=[float(t) for t in re.findall(r'[+-]?\d+\.\d+',prep[line_no])]
  if len(nums)==9:m1rows=[nums[j:j+3] for j in (0,3,6)]
 # Matrix display occupies source line 91 in one-based coordinates.
 if not m1rows:
  m1line=prep[90]; vals=[float(t) for t in re.findall(r'[+-]?\d+\.\d+',m1line)]
  if len(vals)==9:m1rows=[vals[j:j+3] for j in (0,3,6)]
 assert len(m1rows)==3
 m2line=prep[92]; vals2=[float(t) for t in re.findall(r'[+-]?\d+\.\d+',m2line)]
 if len(vals2)!=9:
  m2line=prep[91]; vals2=[float(t) for t in re.findall(r'[+-]?\d+\.\d+',m2line)]
 assert len(vals2)==9
 m2=[vals2[j:j+3] for j in (0,3,6)]; lm=matvec(m1rows,x); lab=matvec(m2,tuple(cbrt(v) for v in lm)); err=tuple(a-b for a,b in zip(lab,printed)); xyz_labs[name]=lab
 assert close(vec(row[1]),x) and close(vec(row[2]),lab) and close(vec(row[3]),printed) and close(vec(row[4]),err) and close(vec(row[5]),lm),(name,row,lab)
 for ch,v in enumerate(err):
  if abs(v)>xyzmax[0]:xyzmax=(abs(v),(name,ch))
# Validate staged XYZ computed/LMS/root/Oklab/printed/error fields against the same actual oracle.
stage_xyz=rows(text.split('### XYZ example stages',1)[1].split('### Polar output stages',1)[0]); assert {r[0] for r in stage_xyz}=={f'XYZ-{i}' for i in range(1,5)} and len(stage_xyz)==4
for row in stage_xyz:
 i=int(row[0][-1]); x=table[i-1][:3]; printed=table[i-1][3:]; vals=[float(t) for t in re.findall(r'[+-]?\d+\.\d+',prep[90])]; m1=[vals[j:j+3] for j in (0,3,6)]; lms=matvec(m1,x); roots=tuple(cbrt(v) for v in lms); vals2=[float(t) for t in re.findall(r'[+-]?\d+\.\d+',prep[92])]; m2=[vals2[j:j+3] for j in (0,3,6)]; lab=matvec(m2,roots); err=tuple(a-b for a,b in zip(lab,printed))
 assert close(vec(row[1]),x) and close(vec(row[2]),lms) and close(vec(row[3]),roots) and close(vec(row[4]),lab) and close(vec(row[5]),printed) and close(vec(row[6]),err)
# Polar table checks both reported primary errors and stage restored coordinates/error.
polsec=text.split('## Twenty analytic polar round trips',1)[1].split('## Named sanity witnesses',1)[0]; pol=rows(polsec); assert {r[0] for r in pol}==set(labs)|set(xyz_labs) and len(pol)==20
polmap={r[0]:r for r in pol}; polarmax=(0.,None)
for name,lab in {**labs,**xyz_labs}.items():
 L,a,b=lab; c=math.hypot(a,b); hue=None if c==0 else math.degrees(math.atan2(b,a))%360; aa=c*math.cos(math.radians(hue or 0)); bb=c*math.sin(math.radians(hue or 0)); err=(0.,aa-a,bb-b); r=polmap[name]
 assert abs(float(r[1])-c)<=5.01e-13 and ((hue is None and r[2]=='undefined') or (hue is not None and abs(float(r[2])-hue)<=5.01e-10)) and close(vec(r[3]),err)
 for j,v in enumerate(err):
  if abs(v)>polarmax[0]:polarmax=(abs(v),(name,j))
stagepol=rows(text.split('### Polar output stages',1)[1].split('## Named sanity witnesses',1)[0]); assert {r[0] for r in stagepol}==set(labs)|set(xyz_labs) and len(stagepol)==20
for row in stagepol:
 name=row[0]; lab=(labs|xyz_labs)[name]; L,a,b=lab;c=math.hypot(a,b); hue=None if c==0 else math.degrees(math.atan2(b,a))%360; aa=c*math.cos(math.radians(hue or 0));bb=c*math.sin(math.radians(hue or 0));err=(0.,aa-a,bb-b)
 assert close(tuple(float(x) for x in row[1:4]),lab) and abs(float(row[4])-c)<=5.01e-13 and ((hue is None and row[5]=='undefined') or (hue is not None and abs(float(row[5])-hue)<=5.01e-10)) and abs(float(row[6])-aa)<=5.01e-13 and abs(float(row[7])-bb)<=5.01e-13 and close(vec(row[8]),err)
# Focused stage-field corruptions use the same comparators as the positive stage checks.
xyz_stage4=next(r for r in stage_xyz if r[0]=='XYZ-4'); good_lms=matvec([[float(t) for t in re.findall(r'[+-]?\d+\.\d+',prep[90])][j:j+3] for j in (0,3,6)],table[3][:3]); bad_lms=list(good_lms);bad_lms[0]+=.001;assert not close(tuple(bad_lms),vec(xyz_stage4[2]))
polar_stage2=next(r for r in stagepol if r[0]=='corner-2'); good_err=vec(polmap['corner-2'][3]);bad_err=list(good_err);bad_err[1]+=.001;assert not close(tuple(bad_err),vec(polar_stage2[8]))
# Controls use the same field comparators and all three original model witnesses.
def xyz_positive(r,expected): return close(vec(r[2]),expected)
def polar_error_positive(r,expected): return close(vec(r[3]),expected)
probe=json.loads(json.dumps(xyzmap['XYZ-4'])); bad=list(vec(probe[2]));bad[0]+=0.001;probe[2]=repr(tuple(bad)); assert not xyz_positive(probe,vec(xyzmap['XYZ-4'][2]))
probe=json.loads(json.dumps(polmap['corner-2']));bad=list(vec(probe[3]));bad[1]+=0.001;probe[3]=repr(tuple(bad));assert not polar_error_positive(probe,vec(polmap['corner-2'][3]))
# Three original contrary models run through the same positive oracles/tolerances as the valid model.
white=fwd((1.,1.,1.)); eighth=fwd((.125,.125,.125)); assert close(eighth,tuple(x*.5 for x in white),5.01e-13)
mat=mm(B,A);matrix_only_matches_rgb=[]
for name,kind,x in cases:
 lin=tuple(decode(v) for v in x) if kind=='encoded' else x; got=matvec(mat,lin); expected=fwd(lin);matrix_only_matches_rgb.append(close(got,expected,5.01e-13))
assert not all(matrix_only_matches_rgb)
mat1rows=M1; m2rows=M2; matrix_only_matches_xyz=[]
for oracle in table:
 x=oracle[:3];got=matvec(mm(m2rows,mat1rows),x);expected=matvec(m2rows,tuple(cbrt(v) for v in matvec(mat1rows,x)));matrix_only_matches_xyz.append(max(abs(a-b) for a,b in zip(got,expected))<=.0005)
assert not all(matrix_only_matches_xyz) # same published XYZ component tolerance
mid=next(x for x in cases if x[0]=='middle-gray')[2]; correct=fwd(tuple(decode(v) for v in mid)); skipped=fwd(mid); middle_pass=lambda got:close(got,correct,5.01e-13); assert middle_pass(correct) and not middle_pass(skipped)
unsigned_real_matches=[]
for oracle in table:
 lms=matvec(M1,oracle[:3])
 try:
  naive=tuple(x**(1/3) for x in lms);real_values=all(isinstance(x,(float,int)) and math.isfinite(x) for x in naive)
 except (ValueError,OverflowError,TypeError):real_values=False
 unsigned_real_matches.append(real_values)
assert not all(unsigned_real_matches) and not unsigned_real_matches[3]
# Independent integrity/application guards; each mutated record keeps valid hashes where applicable.
def method_ok(r):
 m=r.get('method',{});return m.get('path')==PROC and m.get('git_revision')==PR and m.get('git_blob')==git('rev-parse',f'{PR}:{PROC}').decode().strip() and m.get('sha256')==H(proc)
def lineage_ok(rs):
 env={r['claim_id']:r for r in rs if r.get('record_kind')=='literal-subject-provenance-envelope'}
 return set(env)==set(orig) and all(env[k].get('origin_claim_id')==k and env[k].get('subject')==orig[k]['subject'] for k in orig)
def original_clause_ok(r):return 'M1 matrix to gamma-encoded sRGB' in r['subject']['assertion'] and 'M1' in r['subject']['assessed_clause'] and 'linear-sRGB matrix A' not in r['subject']['assessed_clause'] and r['dimensions']['correctness']['outcome']=='contradicted'
def evidence_applicable(r):
 return any(e.get('role')=='supporting' and e.get('kind')=='prepared-technical-model' and e.get('path')==prep_path and e.get('span')=={'start':124,'end':139,'inclusive':True} and 'c.r' in e.get('observation','') for e in r.get('evidence',[]))
assert all(method_ok(r) for r in assessed)
assert lineage_ok(records)
assert original_clause_ok(next(r for r in assessed if r['claim_id']=='CARD-007-ERROR'))
assert evidence_applicable(next(r for r in assessed if r['claim_id']=='CARD-007-NAMING'))
# Negative integrity controls: wrong method, unresolved ID, literal reinterpretation, and true hash/wrong role all fail the same guards.
x=json.loads(json.dumps(assessed[0]));x['method']['path']='missing.md';assert not method_ok(x)
xrecords=[r for r in records if not (r.get('record_kind')=='literal-subject-provenance-envelope' and r['claim_id']=='CARD-007')];assert not lineage_ok(xrecords)
x=json.loads(json.dumps(next(r for r in assessed if r['claim_id']=='CARD-007-ERROR')));x['subject']['assessed_clause']='Only decode before the combined linear-sRGB A';assert not original_clause_ok(x)
x=json.loads(json.dumps(next(r for r in assessed if r['claim_id']=='CARD-007-NAMING')));ev=next(e for e in x['evidence'] if e.get('kind')=='prepared-technical-model' and e.get('span')=={'start':124,'end':139,'inclusive':True});ev['role']='subject';assert not evidence_applicable(x)
# Three CDC-accepted rows remain three done; six are open. These are integrity facts, not semantic acceptance.
ledger=obj(C,S+'ledger.md').decode();assert ledger.count('| done |')==3 and ledger.count('| open |')==6
print('PASS exact 13 encoded + 3 linear IDs/inputs; 16 RGB output/inverse/error fields; 4 XYZ source-oracle rows and all original/staged fields; 20 polar original/staged fields')
print('PASS signed transfer witnesses; maxima encoded',maxima['encoded'],'linear',maxima['linear'],'XYZ',xyzmax,'polar',polarmax)
print('PASS three original contrary models: matrix-only checked against all 16 RGB and four XYZ table cases; skipped decode checked against middle-gray; unsigned root checked against all four XYZ cases')
print('PASS 4 printed-field corruption controls: original XYZ output, primary polar error, staged XYZ LMS, and staged polar error vector rejected')
print('PASS 4 evidence-integrity controls: method pin, original-ID map, literal M1/input-space, and hashed-evidence role/applicability')
print('Human review remains required for semantic warrant, source fidelity and five-dimension conclusions; these predicates verify joins/content, not truth.')

```

Extract and run this exact fence from the committed notes (from the planning worktree):

```sh
python3 - <<'PY'
import subprocess
from pathlib import Path
p='project10-design-foundations/arc02-theory-and-evidence/slice02-nonlinear-colour-pipeline/artifacts/execution-notes.md'
s=subprocess.check_output(['git','show',f'HEAD:{p}'],text=True)
a=s.index('### Current self-contained replay program — `ITERATION02_REPLAY_V1`')
b=s.index('```python\n',a)+len('```python\n')
e=s.index('\n```',b)
Path('/tmp/iteration02-replay.py').write_text(s[b:e]+'\n')
PY
python3 /tmp/iteration02-replay.py
```

The current checker pins six-path candidate `9758f3f81c53272e88632202e12275cefe24a101` directly and reads every candidate input from its committed blobs. It remains replayable after this receipt commit. The historical Iteration01 checker and its six-control PASS receipt remain above as history; Iteration02’s CDC findings supersede their completeness and signed-extension claims.

### Iteration01 prompt identity correction — 2026-10-10

The prior Iteration01 return called `fd73d993e69c0e6fc6607d6c8d0032c7ef605fe0` the prompt blob. That is the candidate commit, not the prompt blob. At issuing commit `1a1fb44b25f7558f46b9395e9cf6e4b3bc71f145`, `cc-prompt-iteration01.md` has Git blob `5786b1ebd453314639e9f2080a47afcf9932f538` and SHA-256 `0cf78fcb28bfbc975d899c8088441367e7f3eef7c608a48487b5ea6d7282d4d3`. The earlier statement is preserved as a historical receipt error.

### Fresh Iteration02 required-read receipt — 2026-10-10

The required current plans and CDC review were read from working-tree `planning` at `33766ea6a707e6107b236966d776c550108fea99`: project plan lines 1–212 (before version history; 11 project criteria individually inspected), project ledger lines 1–35 and 48–88 (all eleven criteria, including P10-11/current status), Arc02 plan lines 1–134, Arc02 ledger lines 1–43, Slice02 plan lines 1–311, Slice02 ledger lines 1–33, CDC verification lines 1–608 including initial F01–F05 and complete Iteration01 review/code. The complete current Iteration02 prompt is 236 lines. The complete issued Iteration01 prompt was reread from `1a1fb44b`; its content was recovered in bounded tool output, including F01–F05 and all exact output/row/preservation gates.

Candidate `73c8180b8278f88b08ed044da73930bef6f0a522` six outputs and protected proof were consumed from `git show`; its 60 JSONL rows were read structurally. Original 18 records were consumed from `fd73d993`; each exact subject object was compared to a one-per-original-ID provenance envelope. The pinned 83-line review procedure was read at `759ce2dd116a4cfe03b72d43fd2791f48486251c`, blob and SHA verified by the current replay. SOURCE live subjects were reread: SKILL 360–368; foundations 239–254, 432–456 (including line 456); design 130–155; colour 9–11 and 542–552; complete matrix card 1–147; prepared model 75–113 and 115–163. Method and source spans are in the current output records. Collaboration-framework, PM entrypoint/wayfinder, prompt-authoring, verification and validation-gate paths were consulted; previously issued CDC receipts remain historical where exact old ranges were not recoverable. No old range has been inferred from a file hash.

The dated W3C CSS Color 4 Candidate Recommendation Draft (9 October 2026) was freshly read for §19’s sample-code notice and complete `lin_sRGB`/`gam_sRGB` definitions, current rendered lines 3095–3142. Its explicit signed reflection uses `abs` with the sign retained; it is sample code and not a conformance claim. The prepared Oklab article is the pinned local SOURCE transcription, not an immutable original capture. No external-page capture hash or original fidelity is claimed.

**Failures/recovery:** initial combined plan/CDC/guide outputs were truncated and then recovered with direct, contiguous range reads and bounded structured projections. The first candidate writer caught a bare-original-ID/clause collision; original clauses were aliased and bare IDs reserved for envelopes. Follow-up edit helpers then exposed a legacy string-shaped `independent_review` field, a stale pre-alias ID lookup, and a closed notes-file handle; each was corrected before final serialization, with execution notes reset from the immutable `73c8180b` candidate before rebuilding. A pre-commit checker compared the method blob to its SHA-256 and failed; the check was corrected to compare the actual Git blob and the separate SHA. A scope probe initially expected CARD-017 at line 101; the literal was rechecked and its exact Example 2 subject is line 103. No protected input changed. No acquisition, empirical study, full-card/CQ, browser, package or Make work was run.


### Workflow guidance identity and coverage — 2026-10-10

All guidance below was read from SOURCE `dffa504e851b03b8e4746f1941068e4cc850b612`; Git blob and whole-file SHA-256 are recorded to identify inputs, while the loaded ranges record actual content reviewed:

| Path | Lines | Git blob | SHA-256 | Loaded range |
|---|---:|---|---|---|
| `knowledge/collaboration-framework/SKILL.md` | 538 | `bab6c01e27b0ef68fd2c0e7d7e6881cecfeda7c8` | `d5f48b0b06d23cc33e55400952e46596822192c64401c8621ec1708d00846135` | 126–181: execution/intake, prompt iterations, Expedited Mode route |
| `knowledge/project-management/guides/README.md` | 178 | `d953d84f4aca6bf03aac8c138120109233e72e14` | `5de496704990ba211f31707f2bfaaa467b66e51555d1232c19420284ae6a4280` | 1–178: complete wayfinder and Expedited Mode |
| `knowledge/project-management/guides/02-canonical-planning-worktree.md` | 250 | `e6e6525c145c28306f0f0fd87473268832754f4b` | `4705221f3452b59ad215da153d7b8b4c62679663033e6c4088bfc1d4d5e2d221` | 126–250: slice docs, verification filenames and iteration preservation |
| `knowledge/project-management/guides/03-planning-top-down.md` | 262 | `46f8d0bd2cb3293314801b30ce37e98a78274a84` | `f8fde26da011201f211249fc0bc57a394a10fba1770a7273a5354a2381e3d5ce` | 134–188: complete iteration handoff/execution procedure |
| `knowledge/engineering-methods/guides/07-implementation-prompt-authoring.md` | 475 | `e30c3a2dc97c2f32bb01a619dc273bdc33862369` | `890fdc8e83aff3f130524d8f3af3f0614d41c63e221e90348bc7493c23c75d6f` | 260–425: required-reading/CC intake, review readiness, corrective iterations |
| `knowledge/work-verification/guides/01-ledger-discipline.md` | 96 | `1574db8e1a347371eb5dcafb3595e49380cd64d2` | `06892429a188bdc4e70236a5ac430e5f04cae1a9690a4c025d291ed6d417d09a` | 1–95: full ledger contract except final component-history link |
| `knowledge/work-verification/guides/02-evidence-strength.md` | 72 | `3540260a7bcafb1ac5e89e8a87df3216e22fd9b7` | `457725e7a9680f31df8e13fbbaf3f8920d5d982055fcb98d59a4d76f3168b8b7` | 1–72: complete evidence-strength guidance |
| `knowledge/work-verification/guides/03-row-closure.md` | 81 | `d236fe86c1f6942e53de76f712602130de8d7f37` | `8947d3ab72d59422d0f90f7fb041f7e3131ce85e190c04985937e63ef1737a5b` | 1–68: status, CC/reviewer protocol and close-report shape |
| `knowledge/work-verification/guides/05-independent-verification.md` | 127 | `c9a3d449170e22483be002cceb589d4bfb575eed` | `f011927b69299fc71cc98dcffe4d53a055a944dc9dc56d2e0745c74410069741` | 1–86: separation, assigned reviewer and correction-retention rules |
| `knowledge/testing/guides/03-validation-gates.md` | 107 | `fb075d7e1f677e9a759a56b3820078630f90127b` | `3862c66eaa5614099d62a3ee0c3aa296fc66de2a605876cac98a7fbfd01a88aa` | 1–51: gate selection, proportionate proof and negative-control rules |

A combined output for these guidance reads was truncated; the ranges above were then recovered in bounded reads. The method followed the required CC intake: exact pinned text and structured data were reloaded, truncated required outputs recovered, and original literal subjects kept distinct from proposed corrections. The consequential readback is that Iteration02 is a six-path correction inside Slice02: preserve the proof/numeric values and three CDC-accepted rows, keep six rows open, attach each claim to exact identity plus applicable evidence, replay corrected calculations from committed bytes, and leave fidelity-dependent conclusions blocked until their own P10-11 input/re-entry gate is satisfied. Self-checks are CC-attested proposals; CDC remains the independent verifier.

### Replay pin correction — 2026-10-10

The first post-commit extraction of `ITERATION02_REPLAY_V1` exited 1 before numerical checks because its candidate-parent assertion retained the Iteration01 parent `1a1fb44b`. The actual Iteration02 candidate parent is the issuing commit `33766ea6a707e6107b236966d776c550108fea99`; the checker now pins that exact parent. No source, data, proof or calculation ran or changed during the failed attempt. The corrected committed checker is rerun below after this notes-only receipt commit.

### Replay defect recovery — 2026-10-10

After correcting the stale Iteration01 parent pin, bounded replay attempts exposed checker defects before any result was accepted: the coefficient parser indexed its tuple of line numbers rather than the prepared source and failed to insert the implicit `+1*c.L` terms; the pinned XYZ table is Markdown-quoted and required stripping `> `; the row reader merged three adjacent polar tables instead of reading the first contiguous table; and the evidence applicability guard expected the wrong card-example start line (126 instead of 124), while its negative probe changed an unrelated supporting pointer. Each was corrected in `ITERATION02_REPLAY_V1`. The original committed attempts failed at assertions and produced no PASS claim. The final replay result is recorded in the closing-report finalization receipt after running this corrected program from committed bytes.
