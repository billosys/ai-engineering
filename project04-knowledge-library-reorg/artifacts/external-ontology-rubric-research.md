# External Ontology Rubric Research

Project: `project04-knowledge-library-reorg`
Status: research input
Created: 2026-09-01
Source role: project-level artifact for Arc01 Slice03 and Arc05 vocabulary work

## Purpose

Project04 needs a way to distinguish knowledge substrate, skills, atomic
skills, and composite skills without defining those terms only from this
repository's current layout. This note captures external conventions from
ontology engineering, knowledge organization, interdisciplinary research, and
bodies of knowledge, then translates them into a practical rubric for the
`docs/` to `knowledge/` reorganization.

This artifact is not a final public taxonomy. It is an input for:

- Arc01 Slice03 skill kind and topology classification.
- Arc02 target directory contract decisions.
- Arc05 public vocabulary and README/docs wording.

## Source Anchors

### Ontology as explicit conceptualization

Tom Gruber's ontology definition is the useful lowest-level anchor: in
computer and information science, an ontology defines representational
primitives used to model a domain of knowledge or discourse, such as classes,
properties, relations, meanings, and constraints. Gruber also frames ontology
as a semantic-level specification for interoperability across independently
developed systems.

Project04 translation: a knowledge area should be assessed by its explicit
concepts, relations, constraints, and discourse boundary, not by the folder it
happens to live in today.

Source: <https://tomgruber.org/writing/definition-of-ontology/>

### Domain ontology

The IAOA domain-ontology entry defines a domain ontology as describing and
categorizing a domain. It includes vocabulary about concepts and relationships,
activities in the domain, and the theories or elementary principles governing
that domain.

Project04 translation: a core or atomic knowledge skill is plausible when it
owns the vocabulary, activities, theories, principles, idioms, and failure modes
of one bounded domain.

Source: <https://wiki.iaoa.org/index.php/Edu:Domain_Ontology>

### Application ontology

The IAOA application-ontology entry defines application ontology around a
particular domain plus task. It may extend or specialize both domain and task
ontologies for a local application.

Project04 translation: a skill or document can be task-specific without being a
core domain. If it exists to make domain knowledge usable for a local workflow,
it may be an application/task bundle or a bridge layer rather than an atomic
domain skill.

Source: <https://wiki.iaoa.org/index.php/Edu:Application_Ontology>

### Ontology networks and reuse

The NeOn Methodology treats ontology development as networked, collaborative,
and reuse-heavy. Its scenarios include reuse of ontological and
non-ontological resources, reengineering, merging, collaboration, and dynamic
evolution.

Project04 translation: composite skills need not be suspect. A composite skill
can be the correct structure when the capability is precisely to reuse,
sequence, merge, route, or reconcile multiple knowledge resources.

Source: <https://oeg.etsiinf.upm.es/index.php/en/methodologies/59-neon-methodology/index.html>

### Domain analysis

Hjorland and Albrechtsen's domain-analysis work frames knowledge domains as
thought or discourse communities, embedded in social division of labor rather
than only individual cognition.

Project04 translation: an atomic skill is not merely a small topic. It should
map to a coherent discourse community, professional practice, or school of
work, with shared terms and relevance judgments.

Source: <https://asistdl.onlinelibrary.wiley.com/doi/abs/10.1002/(SICI)1097-4571(199507)46:6%3C400::AID-ASI2%3E3.0.CO;2-Y>

### Interdisciplinary integration

The National Academies define interdisciplinary research as integrating
information, data, techniques, tools, perspectives, concepts, or theories from
two or more disciplines or specialized bodies of knowledge to solve problems
beyond one discipline's scope.

Project04 translation: a composite skill is strongly indicated when the load
reason is integration across multiple specialized bodies of knowledge, not
mastery of one body.

Source: <https://www.nationalacademies.org/read/11153/chapter/12>

### Bodies of knowledge

The IEEE Computer Society describes SWEBOK as generally accepted,
consensus-driven knowledge derived from software-engineering theory and
practice, with knowledge areas that summarize key concepts and point to deeper
references.

Project04 translation: a domain/tooling skill can stand on a body-of-knowledge
pattern. It does not need to contain every source; it should provide a reliable
map of generally accepted knowledge, current practice, and references.

Source: <https://www.computer.org/education/bodies-of-knowledge/software-engineering>

### Core ideas, crosscutting concepts, and practices

The National Academies' Framework for K-12 Science Education separates
disciplinary core ideas, crosscutting concepts, and scientific/engineering
practices.

Project04 translation: "knowledge" is not only facts. A useful repository model
should distinguish core subject concepts, cross-domain concepts, and practices
or methods. This supports a kind axis separate from an atomic/composite
topology axis.

Source: <https://nap.nationalacademies.org/resource/13165/reportbrief.html>

## Proposed Two-Axis Model

Project04 should avoid a single binary question like "is this skill or
knowledge?" That question collapses too many things. Use two independent axes.

### Axis 1: Knowledge or skill kind

The kind axis asks what the material is about.

- Domain/tooling: a bounded field, language, platform, toolchain, or practice
  community, such as Rust, Go, Erlang/OTP, C++, Cobalt, Tailwind, or Visual
  Design.
- Framework/operational: a way of coordinating work, verification, planning,
  collaboration, review, or quality control.
- Method: a reusable procedure for producing or transforming knowledge, such
  as concept-card extraction or component-boundary analysis.
- Protocol/package: an interoperable protocol or separately distributed
  specification, such as CCDP.
- Support/template: reusable scaffolding that supports work but is not itself
  a full domain or method.
- Source/provenance: primary or derived reference material preserved because it
  substantiates the knowledge substrate.

### Axis 2: Composition topology

The topology axis asks how the material is put together.

- Atomic: one bounded load reason, one primary discourse/practice community,
  and a coherent vocabulary, constraints, and failure model. It may cite or
  route to adjacent material, but its core contract stands alone.
- Composite: an orchestrator over multiple atomic or semi-independent
  components. Its identity depends on sequencing, routing, merging,
  reconciling, or governing multiple knowledge sources or practices.
- Bridge/integration layer: a connector between domains, tasks, or package
  surfaces. It may not own a full domain; its value is translation.
- Application/task bundle: a local arrangement of domain plus task knowledge
  for one workflow or product need.

The axes should not be collapsed. A domain skill is often atomic, but it can
be composite. A framework skill is often composite, but a narrow operational
method can be atomic. A method skill may be atomic or composite depending on
whether it teaches one bounded method or orchestrates several methods and
systems.

## Atomic Skill Rubric

A candidate skill is likely atomic when most of these are true:

1. It has one primary load reason that can be explained without naming several
   other skills as required parts.
2. It maps to one discourse community, profession, field, toolchain, language,
   school, or practice tradition.
3. It owns a coherent vocabulary and set of distinctions.
4. It has recognizable activities, idioms, constraints, and failure modes.
5. It can satisfy its main user need without acting as a router over multiple
   independently loadable components.
6. Its source/provenance materials mostly deepen the same domain rather than
   integrate several domains.
7. Its public explanation can say "load this when working in X" rather than
   "load this to decide which X/Y/Z components to combine."

Atomic does not mean small, simple, or isolated. Rust is broad, but still a
candidate atomic skill because "working in Rust" is a bounded load reason with
an established discourse community, concepts, practices, idioms, tooling, and
failure modes.

## Composite Skill Rubric

A candidate skill is likely composite when most of these are true:

1. Its core value is selecting, sequencing, routing, composing, or reconciling
   multiple loadable units.
2. It integrates concepts, practices, methods, tools, or theories from more
   than one discourse community or specialized body of knowledge.
3. It needs an internal route table, component map, orchestration contract, or
   governance model to be understandable.
4. Removing the composition behavior would remove the skill's identity rather
   than merely simplify it.
5. It solves problems whose correct handling is beyond one domain's scope.
6. Its public explanation naturally says "this framework coordinates..." or
   "this skill composes..." rather than "this skill teaches one domain."
7. It may preserve a compact local posture or adapter, but relies on specialist
   components for depth.

Composite does not mean messy or overgrown. It is appropriate when the real
capability is interdisciplinary or multi-component coordination.

## Edge Cases

### Rust programming-language skill

Rust is the anchor candidate for an atomic domain/tooling skill. The domain is
large, but the load reason is coherent: load it when writing, reviewing,
debugging, or documenting Rust. It has a stable discourse community, shared
terminology, language semantics, tooling, idioms, and known failure modes.

Rust can compose with other skills in a particular task, such as packaging,
coverage, or web UI work. That does not make the Rust skill composite unless
the Rust skill itself becomes an orchestrator whose identity is routing across
multiple independent components.

### Collaboration framework

The collaboration framework is the anchor candidate for a composite
framework/operational skill. Its accepted Project02 architecture treats it as a
daily-driver composer over specialist components: methodology, project
management, ledger discipline, code audit, coverage, subagent delegation, and
contribution style.

The compact local posture in its entrypoint does not make it atomic. Its main
job is to decide which operational component to load, in what order, and under
what quality discipline.

### Concept-card method

The concept-card method is the useful middle case.

It should be classified as an atomic method skill if its load reason is "apply
the concept-card method" and the skill owns one coherent procedure end to end:
extract concepts, preserve provenance, assign strength, attach examples, and
emit reusable cards.

It should be classified as composite if its identity depends on orchestrating
several independent bodies of practice, such as ontology engineering, source
extraction, validation/audit, memory admission, CCDP routing, and reconciliation
across a graph or protocol.

The classification should be evidence-based. Do not infer "atomic" from the
word method, and do not infer "composite" merely because ontology vocabulary
appears in the method.

## Anti-Tautology Discipline

When classifying repo materials, use this order:

1. Start from external criteria: domain ontology, application ontology, domain
   analysis, interdisciplinary integration, body-of-knowledge structure, and
   practice/core-idea separation.
2. Inspect the actual material's load reason, vocabulary, relations,
   constraints, activities, failure modes, sources, package behavior, and
   routing behavior.
3. Classify kind and topology separately.
4. Treat current folder placement as evidence only after content and load
   reason have been assessed.
5. Record borderline cases explicitly, including what evidence would change
   the classification.
6. Avoid naming final public categories until the current library has been
   tested against the rubric.

## Project04 Implications

- `docs/` should explain the library and its categories to users.
- `knowledge/` should house the underlying knowledge substrate and skill source
  material when the material is the thing itself rather than documentation
  about the thing.
- A skill is an operationally loadable use of knowledge, not identical to the
  raw knowledge materials that support it.
- Atomic/composite topology should affect loading and wayfinding language, but
  it should not automatically decide package roots or directory roots.
- Composite skills should be allowed when composition is the real capability.
  The cleanup target is clarity, not forced atomization.
- Arc01 Slice03 should turn this research note into a classification
  instrument and test it against every current and planned skill surface.

## Candidate Future Homes

This artifact can remain as Project04 planning evidence. If Project04 promotes
the analysis into reusable framework guidance, likely future homes are:

- `knowledge/engineering-methods/guides/05-component-boundary-analysis.md`,
  if it becomes part of the reusable method for component and skill boundary
  analysis.
- `docs/skill-library.md` or similar, if only the user-facing explanation of
  the accepted taxonomy is needed.
- A future `knowledge/<method>/guides/` file, if Arc05 decides atomic/composite
  classification is itself a reusable method skill rather than a subsection of
  component-boundary analysis.

