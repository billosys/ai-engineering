---
id: 01KWWGS8HD7T0FXYB88KKKCC07
number: 16
type: research
schema: research/v1.1
name: Research — SWE project- & epic-level PM failures and best practices
created: 2026-06-20
updated: 2026-06-20
tags:
- research
- project-management
- agile
- failure-modes
- evidence
- pm-skill
component: All
author: topological sort
origin: planned
reserved: false
source:
  paths:
  - docs/design/06-final/0016-research-swe-project-and-epic-pm-failures-and-practices.md
  class: odd
  normalization: trim+lf
  migrated_by: odm-migrate/1.0.0
  migrated_on: 2026-07-29
status:
  accepted:
    reached: 2026-06-20
    evidence: asserted
    evidence_dates:
      asserted: 2026-06-20
  active:
    reached: 2026-06-20
    evidence: asserted
    evidence_dates:
      asserted: 2026-06-20
  draft:
    reached: 2026-06-20
    evidence: asserted
    evidence_dates:
      asserted: 2026-06-20
  final:
    reached: 2026-06-20
    evidence: asserted
    evidence_dates:
      asserted: 2026-06-20
  revised:
    reached: 2026-06-20
    evidence: asserted
    evidence_dates:
      asserted: 2026-06-20
  under-review:
    reached: 2026-06-20
    evidence: asserted
    evidence_dates:
      asserted: 2026-06-20
---

# Research — SWE project- & epic-level PM failures and best practices

_Evidence-first synthesis to populate the project-management SKILL, broadening
beyond one project's experience (ODD-0001, the project-x post-mortem) into the
actual literature. Compiled 2026-06-20 from five parallel research streams (CHAOS
critiques & failure-cause taxonomies; DORA/Accelerate; the Agile/SAFe/estimation
evidence base; empirically-supported practices; contested/non-replicating
claims). Companion to ODD-0011 (the planning-system research) — this document
does not re-derive ODD-0011; it supplies the **organizational/PM** evidence layer
that ODD-0011's **mechanical/formal** layer sits inside._

**Stance (inherited, load-bearing).** Trust the formal/empirical; treat
consultative frameworks (SAFe, CCPM, story-point velocity, the Standish CHAOS
success rates) as **practitioner-lore unless controlled evidence supports them.**
Every load-bearing claim is tagged **[E]** (empirical / peer-reviewed /
large-dataset / formal) or **[P]** (practitioner-lore / consultative /
weak-or-absent controlled evidence). Where a popular claim is actively contested
in peer review, the critique is cited beside it.

---

## 0. Convergent findings (the ones that matter)

1. **The most-cited "software crisis" statistics are not evidence.** The Standish
   CHAOS success/challenged/failed figures (the famous "16% success," "189%
   overrun," "agile is 3× more successful than waterfall") were demolished in
   peer review: a project's CHAOS label depends on the *direction of its
   estimation bias*, not its actual accuracy or value. A best-in-class
   forecaster can score 35% "success"; flipping only the *sign* of the bias (same
   accuracy) flips the success rate from 5.8% to 94.2% **[E]**
   (Eveleens & Verhoef 2010). **Do not seed the skill with any CHAOS number.**

2. **What actually predicts project failure is large-dataset and boring:**
   estimation optimism (systematic, ~30–40% mean effort overrun), requirements
   volatility / scope creep, supplier-selection-by-low-bid, and a **fat-tailed
   (power-law) overrun distribution** where the danger lives in the outliers, not
   the average — driven by *interdependencies among components cascading* **[E]**
   (Flyvbjerg et al. 2022, n=5,392; Jørgensen reviews; vWorker n=785,325). This
   directly corroborates project-x's two structural failures: an *undeclared
   dependency edge* (the prod-DB wiring, ODD-0001 §C2) is exactly the kind of
   interdependency that produces a cascade, and *vision/scope drift* (§E) is
   requirements volatility by another name.

3. **The strongest organizational result of the decade undercuts framework
   shopping.** A 4,000+-team empirical comparison found the *choice of scaling
   framework* (SAFe, LeSS, …) is **not** a meaningful predictor of effectiveness;
   small differences vanish once you control for team experience and org size.
   What predicted effectiveness was **technical practice** (CI, automated
   testing, clean architecture) **[E]** (arXiv 2310.06599, 2023). Translation:
   buy the *practices*, not the *brand*.

4. **DORA's defensible core is the method, not the multipliers.** The
   psychometric construct validation + SEM modeling on a 23k+ multi-year dataset
   is real and respectable **[E]**. The dramatic "elite teams deploy 182× more /
   recover 2,293× faster" figures are **between-cluster ratios on self-reported,
   cross-sectional data where the clusters are defined by the very metrics being
   compared** — partly circular, year-unstable, and not causal **[P]**.

5. **Evidence strength is inverted relative to industry attention.** The
   best-evidenced practices (software inspection / code review, pair programming,
   small batches via the *proven* Little's Law identity, psychological safety as a
   construct) get less marketing than the worst-evidenced ones (SAFe epic
   predictability, CCPM buffers, WSJF economics, velocity-as-productivity, the
   "10× developer"). The skill should track evidence, not attention.

6. **The broad literature CONFIRMS project-x's taxonomy more than it contradicts
   it** — and *extends* it on three points: estimation optimism is a named,
   measured cognitive bias (not just local sloppiness); overruns are fat-tailed
   (so "it was only a little behind on average" is a trap); and metric-gaming
   (Goodhart) is the predictable failure mode of any status number turned into a
   target — a guardrail project-x didn't need yet but the skill will.

---

## 1. Evidence strength — what to trust vs. lore (contested claims adjudicated)

**Formally / empirically grounded — build on these:**

- **Estimation is systematically over-optimistic**, ~30–40% mean effort overrun,
  60–80% of projects overrun; *not improving over time*; "90%-confident"
  intervals capture actuals only ~60–70% of the time **[E]** (Jørgensen &
  Moløkken-Østvold reviews).
- **Irrelevant/misleading information biases estimates** (a client's stated budget
  anchors the estimate); the fix is to *isolate biasing information from the
  estimator* — a randomized controlled field experiment, not opinion **[E]**
  (Jørgensen & Grimstad 2011).
- **Expert judgment ≥ formal estimation models** in 10 of 16 studies; "no
  substantial evidence in favour of estimation models" — but the *worst* expert
  beat the models every time, so expert quality is decisive **[E]** (Jørgensen
  2007, *Int. J. Forecasting*).
- **IT cost overruns follow a power law, not a normal distribution** (n=5,392);
  assuming normality makes managers severely underestimate the probability of
  catastrophic overruns; proposed mechanism = interdependent components cascading
  **[E]** (Flyvbjerg et al. 2022, *JMIS*).
- **"Black Swan" tail**: across 1,471 IT projects, mean overrun 27% but ~1 in 6 was
  a 200%-cost / 70%-schedule outlier **[E]** (Flyvbjerg & Budzier 2011).
- **Planning fallacy** (inside vs outside view; anchoring on the best case) is a
  replicated cognitive finding **[E]** (Kahneman & Tversky 1979; Buehler et al.
  1994). **Reference-class forecasting** (budget by comparison to similar
  completed projects) is the mandated correction in several national governments
  **[E]** (Flyvbjerg 2006/2008).
- **Little's Law (L = λW) is a proven theorem** — strongest possible support — but
  *only for stable systems* (long-run arrival rate = departure rate). Transferring
  it to forecast variable, unstable knowledge work violates its core assumptions;
  that transfer is an engineering assumption, **not** a theorem **[E/theory]**
  (Vacanti; Little's-Law stability literature). (This matches ODD-0011's calibration.)
- **Software inspection / code review** is among the best-evidenced practices:
  controlled experiments *plus* decades of industrial measurement; review
  effectiveness degrades with patch size (robust finding) **[E]** (Fagan 1976;
  McIntosh et al. 2016; Bosu et al. 2015, Microsoft).
- **Pair programming**: meta-analysis of controlled experiments — small positive
  effect on quality, medium *negative* effect on effort (pairs cost more), best
  when task complexity is high **[E]** (Hannay et al. 2009).
- **Psychological safety → team learning** is peer-reviewed **[E]** (Edmondson
  1999); Google's Project Aristotle (180+ teams) ranks it the #1 differentiator
  of effective teams — large but *company-reported, not peer-reviewed* **[E-ish]**.

**Peer-reviewed method, but descriptive / correlational, not causal:**

- **DORA/Accelerate**: real psychometrics (factor analysis, AVE, Cronbach's α,
  latent-class clustering, SEM) on 23k+ respondents **[E]** — but the data are
  cross-sectional self-report; SEM *models* hypothesized causal paths, the design
  cannot *establish* them. The instrument and raw data are not public, limiting
  replication (the single strongest reproducibility critique) **[E-critique]**
  (Keunwoo Lee; only partially answered by Humble's rebuttal).
- **Continuous integration**: systematic review of 101 studies finds real effects
  but a *nuanced/unclear* quality link; one study found internal-quality
  indicators "remained stable" after CI adoption **[E]** (EMSE 2021). CI is
  observational-correlational, not RCT-proven.
- **Agile efficacy generally**: the strongest pro-agile empirical study (Serrador
  & Pinto 2015, *IJPM*) finds a positive association — but practice-specific and
  *not universal* (one n=60 outsourced-project study found *negative* effects)
  **[E]**. "Agile helps" is context-dependent, not a law.

**Lore — useful framing, weak/absent controlled evidence (don't let it drive structure):**

- **SAFe**: no RCT exists; "strong need for more empirical research"; existing case
  studies "not rigorous enough and hard to generalize"; ~5% of surveyed "SAFe"
  orgs were pure adopters; the one large comparative study finds framework choice
  has *no effect* **[E-on-the-weakness]** (multivocal review 2019; arXiv
  2310.06599).
- **CCPM (Critical Chain)**: controlled CCPM-vs-CPM trials are *explicitly noted as
  missing*; proponents "fail to provide scientific evidence" for the
  overestimation/Parkinson assumptions; "no clear scientific basis for sizing the
  buffers." Weakest-supported item in the set **[E-on-the-weakness]** (PMI
  literature reviews). (Consistent with ODD-0011.)
- **WSJF / Cost-of-Delay economics**: no empirical validation of WSJF
  *effectiveness* found; the math is sound *given* a known Cost of Delay and job
  size, but the empirical question — can teams estimate CoD reliably? — is
  unaddressed; SAFe's Fibonacci proxy is not genuine economic CoD and is gameable
  (deflate job size to inflate priority) **[P]** (Yip; Black Swan Farming).
- **Story points / velocity as productivity**: weak-to-absent correlation between
  story points and cycle time across large datasets; no cross-team validity;
  "the correct use of velocity is never as a productivity measure" **[E/P]**
  (arXiv 1301.5964; Jellyfish 400+-team data; Vacanti).
- **ADRs / RFDs, blameless postmortems**: influential convention; ADR adoption is
  *descriptively* studied (MSR mining) but **no controlled study shows ADRs improve
  outcomes**; blameless postmortems are practitioner doctrine justified by the
  (real) psych-safety literature, not directly trialed **[P]** (Nygard 2011;
  Google SRE book). Adopt for sound reasons; don't overclaim the evidence.

**Contested claims adjudicated (find the critique before repeating the number):**

| Popular claim | Verdict | Why |
|---|---|---|
| CHAOS "16% / 31% fail" etc. | **Reject** [E] | Label tracks bias *direction*, not accuracy; Standish itself redefined "success" in 2015 (Eveleens & Verhoef 2010) |
| "Agile 3× / 350% more successful than waterfall" | **Reject** [E] | Rides on the *same* discredited CHAOS definitions (Eveleens & Verhoef) |
| "189% average cost overrun" | **Reject** [E] | Sampling-on-failure bias; "probably much too high" (Jørgensen & Moløkken 2006) |
| DORA "elite deploy 182× / recover 2,293×" | **Demote to [P]** | Self-report, cross-sectional, between-cluster, partly circular, year-unstable |
| "10× developer" | **Demote to [P]** | Origin study n=12 with a language confound (Sackman 1968); "individuals vary" is fine, "10× as a hire-for-it constant" is not (Bossavit, *Leprechauns*) |
| LOC / Function Points as productivity | **Reject** [E] | FP is not a true ratio scale; LOC is gameable & not cross-comparable (Nesma) |
| CMMI maturity → performance | **Reject** [E] | "Minimal evidence" maturity gains map to performance gains |
| "Detailed estimation improves accuracy" | **Reject** [E] | Overruns ~30% and *not* decreasing; intervals badly miscalibrated (Jørgensen) |

---

## 2. Project-level failure taxonomy (with evidence calibration)

Mapped to project-x categories (ODD-0001) where they correspond.

1. **Estimation optimism & planning fallacy** **[E]** — systematic, cognitive,
   measured (~30–40% overrun; anchoring on budgets/best-cases). *Corrective:*
   reference-class forecasting (outside view), isolate biasing info from
   estimators. → Extends ODD-0001 §G5 (clarifying-question calibration) and the
   whole estimation-avoidance posture; project-x sidestepped this by *deriving
   order from dependencies rather than estimates* (ODD-0011) — a defensible move
   given how bad estimation is.

2. **Requirements volatility / scope creep** **[E]** — among the most common
   failure causes (scope-management failures cited in ~82% of cases; schedule
   constraints ~86%); churn raises defect density. → Directly maps to ODD-0001 §E
   (scope/vision drift, amendments accreting, plan-vs-stakeholder mismatch
   surfacing late).

3. **Interdependency cascades / fat-tailed overruns** **[E]** — the power-law
   mechanism: a problem in one component cascades into an extreme overrun. → This
   is the *literature's name* for ODD-0001 §C2 (the prod-DB wiring edge that no
   graph tracked) and the general thesis of ODD-0011 (incomplete dependency graph
   ⇒ silent out-of-order failure). **The broad literature confirms project-x's
   marquee failure is a known, dangerous, fat-tailed class — not a fluke.**

4. **Supplier / work-selection by wrong signal** **[E]** — selecting by *low bid*
   raised failure risk; by *past performance* lowered it (n=785,325). → Analogue
   of ODD-0001 §B5 (recency/streetlight bias in work selection): choosing by the
   wrong, cheap-to-observe signal.

5. **Measurement-definition failure** **[E]** — "success" defined as
   estimation-adherence (CHAOS) measures the wrong thing and *perverts* practice
   (managers pad estimates to score "success"). → Maps to ODD-0001 §D (status
   semantics): a status label that means the wrong thing produces false
   confidence. **The CHAOS critique is the macro-scale version of "store-layer:
   done" masking "not wired in prod."**

6. **Optimism bias vs strategic misrepresentation** **[E]** — two *distinct*
   overrun drivers: cognitive (planning fallacy) and deliberate (padding numbers
   to win approval). The skill should not assume all bad estimates are honest
   mistakes. → New beyond ODD-0001 (a blameless single-team post-mortem didn't
   surface incentive-driven misrepresentation; multi-stakeholder PM must).

---

## 3. Epic / program level (Agile) — failures & practices

**Empirically supported at scale:**

- **Small batch size / high deployment frequency** correlates with delivery
  performance; deployment frequency is a *proxy for batch size* (Lean) — supported
  by DORA self-report **[P→E-ish]** *plus* queueing-theory framing **[E/theory,
  with the stability caveat in §1]**. → Reinforces ODD-0001 §B (sequence/flow) and
  the "do the ready thing, small" posture.
- **WIP limits** rest on the *proven* Little's Law identity **[E]**; that imposing
  WIP limits improves real team outcomes is supported mostly by practitioner
  reports + theory, not controlled software trials **[P on the practice]**.
- **Continuous integration / trunk-based development** correlate with performance
  (DORA) and have some independent comparative study; trunk-based suits
  experienced/smaller teams, branch-based suits larger/less-experienced ones —
  *context-dependent*, not universal **[E/P]**.
- **Technical practices beat frameworks** (the §0.3 finding) **[E]**.

**Lore at the epic/program level (treat as [P]):**

- **SAFe epic predictability / WSJF prioritization** — no controlled evidence; the
  framework choice shows no effect; WSJF unvalidated and gameable **[P]**.
- **Story-point estimation accuracy & velocity-as-productivity** — weak/no
  correlation with effort; no cross-team validity; gameable (point inflation,
  story-splitting) **[E/P]**. **#NoEstimates** (Duarte) argues predictability comes
  from *task-size stability and release frequency*, not the estimation method —
  the empirical backing is the same throughput-vs-points evidence, i.e. it is a
  *reasonable inference from the estimation literature*, but the movement itself is
  advocacy **[P]**. The defensible synthesis: **count small, equally-sized items
  and forecast with throughput/Monte-Carlo rather than summing story points.**
- **CCPM buffers** — unvalidated assumptions, no controlled trials **[P]**.

**Estimation literature, condensed for the skill:** estimates are optimistic,
overconfident, anchored, and don't get better with more effort; expert judgment
beats models but only if the expert is good; the cheapest robust forecast is
*small uniform items + empirical throughput*, and the cheapest robust *ordering*
is *dependency-derived* (ODD-0011), not estimate-derived. **This is why
project-x's "order by dependency, not by estimate" instinct was correct.**

---

## 4. Best practices, ranked by evidence strength

| Rank | Practice | Best evidence | Strength | Note |
|---|---|---|---|---|
| 1 | **WIP limits / small batch (Little's Law)** | formal theorem [E] | Identity proven; practice-outcome link weaker | Law holds only for stable systems |
| 2 | **Software inspection / code review** | controlled exps + decades of industrial data [E] | Strong, consistent | Effectiveness drops with patch size |
| 3 | **Pair programming** | meta-analysis of RCTs [E] | Real but small; effort cost; some pub bias | Best on complex tasks |
| 4 | **Modern code review** | large-dataset mining (MS/Google) [E] | Strong correlational | Coverage+participation+expertise → fewer defects |
| 5 | **Psychological safety (construct)** | peer-reviewed field study + Google obs [E] | Construct solid | Google study company-reported |
| 6 | **Continuous integration** | SLR of 101 studies [E] | Real but quality link nuanced | Not RCT-proven |
| 7 | **Small batch / deploy freq / trunk-based** | DORA self-report + Lean theory [P/E-ish] | Correlational self-report | No independent RCT |
| 8 | **Blameless postmortems** | SRE doctrine [P] | Lore justified by psych-safety lit | Not directly trialed |
| 9 | **TDD** | conflicting SLRs [E] | **Genuinely mixed** | Modest quality gain shrinks under rigor; no productivity gain — do NOT over-rank |
| 10 | **ADRs / RFDs** | adoption-only mining [P] | Convention | No outcome-improvement study; adopt for sound reasons |

---

## 5. Lift-ready synthesis for the PM skill

Cross-referenced to project-x (ODD-0001 finding IDs) and odm capabilities. Tags
indicate the evidence behind the *rule*.

### SHOULD

- **Derive order from a complete dependency graph, not from estimates** **[E]** —
  because estimates are systematically optimistic/overconfident (Jørgensen) and
  the danger is fat-tailed interdependency cascades (Flyvbjerg). → ODD-0001 §B1–B3,
  §C2; odm `link` / `next` / `blocked` / `check`.
- **Track integration-level desired-state facts and reconcile against reality on a
  schedule** **[E-mechanism: interdependency cascade is the dominant overrun
  driver]**. → ODD-0001 §C2–C4; odm `reconcile`, `desired_facts`.
- **Forecast with small uniform items + empirical throughput (Monte-Carlo), not
  summed story points** **[E/P]** (estimation literature; #NoEstimates synthesis).
  → ODD-0001 §G5; odm slice-granularity discipline.
- **Use the outside view (reference-class forecasting) for any program-level time/
  cost call** **[E]** (Kahneman/Tversky; Flyvbjerg). → ODD-0001 §E3 (stakeholder
  expectation mismatch); odm program-level acceptance facts.
- **Use multi-gate status with explicit evidence levels; never let one scalar mean
  "done"** **[E-by-analogy: CHAOS measurement-definition failure]**. → ODD-0001
  §D1–D3; odm `set-gate`, status vectors.
- **Invest in technical practices (CI, code review, small batches, trunk-based)
  over framework adoption** **[E]** (arXiv 2310.06599; DORA; inspection lit). →
  ODD-0001 §F3 (continuous integration-level checks); odm `check` as a gate.
- **Run blameless postmortems and protect psychological safety** **[E construct /
  P practice]** (Edmondson; SRE). → ODD-0001's own blameless framing; this skill's
  posture layer.
- **Read one cheap, generated global state first each session** **[P, but the
  decisive LLM-collaboration affordance]**. → ODD-0001 §G1, §G6; odm `orient`.

### SHOULDN'T

- **Don't cite or target any CHAOS success/overrun figure** (incl. "agile 3×")
  **[E: refuted]** (Eveleens & Verhoef). → guards ODD-0001 §D (false status).
- **Don't treat velocity / story points as productivity, and don't make any metric
  a target** **[E/P; Goodhart]** — point inflation and story-splitting follow. →
  ODD-0001 §B5, §D.
- **Don't lean on SAFe epic predictability, WSJF economics, or CCPM buffers as
  *structural* drivers** **[P: no controlled evidence]** — use them, if at all, as
  *advisory priority on top of* dependency order (ODD-0011 guardrail). → ODD-0001 §B.
- **Don't read DORA's "Nx faster" multipliers as causal or stable** **[P]** — the
  method is sound, the multipliers are self-report cluster ratios.
- **Don't measure individuals by LOC / function points or chase the "10× hire"**
  **[E/P: invalid / weak origin]** (Nesma; Bossavit). → ODD-0001 §G (people aren't
  the failure mode; information architecture is).
- **Don't assume more estimation effort buys accuracy** **[E]** (Jørgensen). →
  ODD-0001 §G5.

### GOOD / BAD table

| # | BAD | GOOD | Evidence | x-ref |
|---|---|---|---|---|
| 1 | "CHAOS says 70% of projects fail — we must adopt SAFe" | "Overruns are fat-tailed; we manage interdependencies and order by dependency" | [E] Eveleens & Verhoef; Flyvbjerg | §C2, ODD-0011 |
| 2 | Sum story points → "velocity 42, so we'll finish in 3 sprints" | Count small uniform items → Monte-Carlo throughput forecast | [E/P] Jørgensen; Vacanti | §G5 |
| 3 | "Estimate carefully and we'll hit the date" | Reference-class forecast (outside view); pad with the *historical* overrun, not optimism | [E] Kahneman/Tversky; Flyvbjerg | §E3 |
| 4 | "Elite teams deploy 182× more — mandate 10 deploys/day" | Small batches + WIP limits because the *flow theorem* and *technical-practice* evidence support them; don't target the metric | [E] Little's Law; arXiv 2310.06599 | §B, §F3 |
| 5 | "store-layer: done" | `built✓ tested✓ deployed(dev)✓ verified-live(prod)✗ [evidence: reconciled]` | [E-analogy] CHAOS measurement failure | §D1–D3 |
| 6 | Pick the SAFe/LeSS brand to fix delivery | Invest in CI, code review, trunk-based, small batches | [E] arXiv 2310.06599; inspection lit | §F3 |
| 7 | "Bob is our 10× dev, route everything through him" | Pair on complex work; protect psychological safety; blameless postmortems | [E] Hannay; Edmondson | §G |
| 8 | WSJF Fibonacci scores drive the roadmap | Dependency-derived order; advisory priority *on top*, never as the order | [P on WSJF] Yip; ODD-0011 | §B |

---

## 6. What the evidence does NOT support (guardrails)

- **CHAOS methodology** — labels track estimation-bias *direction*, not accuracy or
  value; the "agile 3×" claim inherits the same flaw; Standish silently redefined
  "success" in 2015. *Never cite a CHAOS figure.* **[E]**
- **CCPM buffer theory** — no controlled trials; unvalidated Parkinson/overestimation
  assumptions; no scientific basis for buffer sizing. **[E-on-weakness]**
- **WSJF / SAFe economic claims** — no validation of effectiveness; relative
  Fibonacci proxy ≠ real Cost of Delay; gameable. **[P]**
- **Story-point / velocity validity** — weak/no correlation with effort; no
  cross-team validity; invalid as productivity. **[E/P]**
- **DORA multipliers as causal/stable** — sound method, over-claimed numbers
  (self-report, cross-sectional, partly circular, year-unstable). **[P]**
- **"10× developer" as a hire-for-it constant** — origin study n=12 with a language
  confound; "individuals vary" survives, the slogan doesn't. **[P]**
- **LOC / Function Points / CMMI maturity** as productivity or performance
  predictors — invalid / minimal evidence. **[E]**
- **Framework adoption as the lever** — framework choice shows no effect at scale;
  technical practice does. **[E]**
- **ADRs / blameless postmortems improving outcomes** — sound conventions, but
  *outcome* evidence is absent (ADR) or indirect (postmortems). Adopt for sound
  reasons; don't overclaim. **[P]**
- **Replication caveat (meta-guardrail)** — empirical SE has a documented
  replication-fragility problem (NHST misuse, "garden of forking paths," unpublished
  artifacts). Treat *any* single SE study (including some cited here) as suggestive,
  not settled; the claims above that survive are the ones with *multiple independent
  lines* or a *formal proof*. **[E]** (CACM "Threats of a Replication Crisis").

---

## Sources

**CHAOS critiques & failure causes:** Eveleens & Verhoef, "The Rise and Fall of
the Chaos Report Figures," *IEEE Software* 27(1), 2010
(https://www.cs.vu.nl/~x/the_rise_and_fall_of_the_chaos_report_figures.pdf ;
https://dl.acm.org/doi/abs/10.1109/MS.2009.154); Jørgensen & Moløkken-Østvold,
"How Large Are Software Cost Overruns? A Review of the 1994 CHAOS Report,"
*Information & Software Technology* 48(8), 2006
(https://www.umsl.edu/~sauterv/analysis/Standish/standish-IST.pdf ;
https://www.simula.no/research/how-large-are-software-cost-overruns-critical-comments-standish-groups-chaos-reports);
Glass, "The Standish Report: Does It Really Describe a Software Crisis?" *CACM*
49(8), 2006 (https://dl.acm.org/doi/10.1145/1145287.1145301); Standish 2015
redefinition summary (https://www.scrum.org/resources/blog/key-lessons-standishs-2015-chaos-report).

**Flyvbjerg / planning fallacy:** Flyvbjerg & Budzier, "Why Your IT Project May Be
Riskier Than You Think," *HBR*, 2011 (https://hbr.org/2011/09/why-your-it-project-may-be-riskier-than-you-think ;
https://arxiv.org/abs/1304.0265); Flyvbjerg et al., "The Empirical Reality of IT
Project Cost Overruns: Discovering a Power-Law Distribution," *JMIS*, 2022
(https://arxiv.org/abs/2210.01573 ;
https://www.tandfonline.com/doi/abs/10.1080/07421222.2022.2096544); Flyvbjerg,
"Curbing Optimism Bias … Reference Class Forecasting in Practice," *European
Planning Studies*, 2008 (https://www.researchgate.net/publication/233258056);
"From Nobel Prize to Project Management," *PMJ*, 2006
(https://arxiv.org/pdf/1302.3642); Kahneman & Tversky, "Intuitive Prediction,"
*TIMS Studies in Management Science* 12, 1979; Buehler, Griffin & Ross,
*JPSP* 67(3), 1994 (https://web.mit.edu/curhan/www/docs/Articles/biases/67_J_Personality_and_Social_Psychology_366,_1994.pdf);
Flyvbjerg & Gardner, *How Big Things Get Done*, 2023.

**Failure-cause datasets:** "Failure factors of small software projects at a global
outsourcing marketplace," *JSS*, 2014
(https://www.sciencedirect.com/science/article/abs/pii/S0164121214000429); "The
Impact of Scope Creep on Project Success," IEEE, 2020
(https://ieeexplore.ieee.org/document/9133081/); requirements-volatility
(https://www.cs.vu.nl/~x/qrv/qrv.pdf ;
https://www.sciencedirect.com/science/article/abs/pii/S0164121209000557).

**DORA / Accelerate:** *Accelerate* (Forsgren, Humble, Kim, 2018,
https://itrevolution.com/product/accelerate/); DORA four/five keys
(https://dora.dev/guides/dora-metrics-four-keys/ ;
https://cd.foundation/blog/2025/10/16/dora-5-metrics/); 2022 & 2024 State of
DevOps reports (https://dora.dev/research/2022/dora-report/2022-dora-accelerate-state-of-devops-report.pdf ;
https://dora.dev/research/2024/dora-report/); Forsgren research
(https://nicolefv.com/research ; https://queue.acm.org/detail.cfm?id=3182626);
Keunwoo Lee review (https://keunwoo.com/notes/accelerate-devops/) and Humble's
rebuttal (https://medium.com/@jezhumble/response-to-keunwoo-lees-review-of-accelerate-611ef75cad3);
DORA self-critique on targeting metrics (https://dora.dev/guides/dora-metrics/);
limitations (https://www.aviator.co/blog/everything-wrong-with-dora-metrics/ ;
https://www.infoq.com/articles/dora-metrics-anti-patterns); causal-analysis
backdrop (https://arxiv.org/pdf/2301.07524).

**Agile / SAFe / estimation:** "Do Agile Scaling Approaches Make A Difference?"
arXiv 2310.06599, 2023 (https://arxiv.org/pdf/2310.06599); "Adopting SAFe: a
multivocal literature review" (https://www.researchgate.net/publication/332852931);
Laanti & Kettunen, "SAFe Adoptions in Finland," XP 2019
(https://researchportal.helsinki.fi/en/publications/safe-adoptions-in-finland-a-survey-research/);
Geraghty, "A Critique of SAFe" (https://tomgeraghty.co.uk/index.php/a-short-critique-of-safe/);
Jørgensen, "Forecasting … Expert Judgement and Formal Models," *Int. J.
Forecasting*, 2007 (https://www.sciencedirect.com/science/article/abs/pii/S016920700700074X);
Jørgensen & Grimstad (irrelevant-information RCT, IEEE TSE 2011, via
https://arxiv.org/abs/1804.03919); "On the Current Measurement Practices in Agile
SD," arXiv 1301.5964 (https://arxiv.org/pdf/1301.5964); Jellyfish story-points
analysis (https://jellyfish.co/blog/do-story-points-work/); Vacanti / Monte-Carlo
(https://www.scrum.org/resources/blog/monte-carlo-forecasting-scrum); Duarte
*NoEstimates* (https://www.infoq.com/articles/book-review-noestimates/); Serrador
& Pinto, "Does Agile work?" *IJPM*, 2015
(https://www.sciencedirect.com/science/article/abs/pii/S0263786315000071);
Reinertsen, *Principles of Product Development Flow*, 2009
(http://lpd2.com/wp-content/uploads/2013/06/ReinertsenFLOWChap1.pdf); Little's Law
stability (https://www.leanability.com/en/blog/2017/08/littles-law-and-system-stability/);
CCPM reviews (https://www.pmi.org/learning/library/critical-chain-project-management-investigation-6380 ;
https://www.researchgate.net/publication/335679770); WSJF critiques
(https://jchyip.medium.com/problems-i-have-with-safe-style-wsjf-772df2beaf02 ;
https://blackswanfarming.com/safe-and-weighted-shortest-job-first-wsjf/).

**Supported practices:** CI SLR, *EMSE*, 2021
(https://link.springer.com/article/10.1007/s10664-021-10114-1 ;
https://arxiv.org/pdf/2103.05451); trunk-based comparison
(https://arxiv.org/html/2507.08943v1 ;
https://dora.dev/capabilities/trunk-based-development/); modern code review —
McIntosh et al., *EMSE*, 2016
(https://rebels.cs.uwaterloo.ca/papers/emse2016_mcintosh.pdf); Bosu et al.
(Microsoft), MSR 2015
(https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/bosu2015useful.pdf);
Sadowski et al. (Google), ICSE-SEIP 2018
(https://www.researchgate.net/publication/325730783); Fagan 1976, via "A History
of Software Inspections" (https://www.researchgate.net/publication/234811007);
pair programming meta-analysis — Hannay et al., *IST*, 2009
(https://www.sciencedirect.com/science/article/abs/pii/S0950584909000123);
Cockburn & Williams, 2000
(https://www.researchgate.net/publication/2333697); Edmondson, *ASQ*, 1999
(via https://psychsafety.com/googles-project-aristotle/); Google Project
Aristotle (https://rework.withgoogle.com/intl/en/guides/understand-team-effectiveness);
Google SRE "Postmortem Culture" (https://sre.google/sre-book/postmortem-culture/);
TDD SLR (https://www.researchgate.net/publication/372832171) and SLR-reliability
critique (https://www.sciencedirect.com/science/article/abs/pii/S0950584925001016);
ADRs — Nygard 2011 (https://adr.github.io/) and MSR adoption study
(https://www.researchgate.net/publication/371709784).

**Guardrails / contested:** Bossavit, *The Leprechauns of Software Engineering*
(https://leanpub.com/leprechauns); Construx, "The Origins of 10x"
(https://www.construx.com/blog/the-origins-of-10x-how-valid-is-the-underlying-research/);
"Agile 3×" promo (https://www.mountaingoatsoftware.com/blog/agile-succeeds-three-times-more-often-than-waterfall);
Goodhart's Law in SE (https://axify.io/blog/goodhart-law);
Nesma, "Measuring Programmer Productivity is a waste of time"
(https://nesma.org/2015/01/programmer-productivity-is-waste-of-time/); LOC critique
(https://workweave.dev/blog/why-lines-of-code-are-a-bad-measure-of-developer-productivity);
CMMI study (https://www.researchgate.net/publication/326634687); "Move fast and
break things" critique (https://www.capacitas.co.uk/insights/why-move-fast-and-break-things-doesnt-work);
estimation-as-waste (https://rclayton.silvrback.com/software-estimation-is-a-losing-game ;
https://en.wikipedia.org/wiki/Software_development_effort_estimation); replication
crisis — *CACM* "Threats of a Replication Crisis in Empirical Computer Science"
(https://cacm.acm.org/research/threats-of-a-replication-crisis-in-empirical-computer-science/);
Mair & Shepperd, "Replication Studies Considered Harmful" (https://arxiv.org/pdf/1802.04580).

## Source-quality caveats

- **Read in full (highest confidence):** Eveleens & Verhoef 2010 — *all* CHAOS
  year-figures, the four flaws, the EQF case numbers, and the 1/Landmark sign-flip
  (5.8%↔94.2%) come from the full text. This is the single most load-bearing
  source and it was verified directly.
- **Snippet-level (accurate at summary level; verify exact effect sizes against the
  primary PDFs before any formal citation):** the Jørgensen estimation papers
  (Jørgensen & Grimstad 2011, Jørgensen 2007 — captured via secondary citation),
  the Flyvbjerg power-law specifics, the DORA 2024 multipliers and AI/platform
  trade-off figures, the SAFe survey "~5% pure adopters" figure (from the multivocal
  review, not the Laanti abstract), and most of the supported-practices effect sizes
  (Fagan's 38-vs-8 defects/KLOC, pair-programming "~15%").
- **Vendor / non-peer-reviewed but quantitative:** Jellyfish (400+-team story-point
  analysis), Google Project Aristotle (company-reported, large but not peer-reviewed),
  Vacanti's "no correlation" dataset (not peer-reviewed). Treated as [P]/[E-ish]
  accordingly above.
- **Year-unstable by nature:** the DORA elite-vs-low multipliers shift every report
  (e.g., the recalled "106×/2604×" vs 2024's "127×/2,293×"); this instability is
  itself part of why they are demoted to [P].
- **No domains were blocked**; where a primary PDF was not fetched in full it is
  flagged above. Per protocol, no restrictions were worked around.
