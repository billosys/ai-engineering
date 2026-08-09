#!/usr/bin/env python3
"""Generate C++ guide chapters from the imported C++ Core Guidelines source."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
CPP_ROOT = ROOT / "knowledge" / "cpp"
SOURCE = CPP_ROOT / "sources" / "md" / "cpp-core-guidelines" / "CppCoreGuidelines.md"
GUIDES = CPP_ROOT / "guides"
ANALYSIS = CPP_ROOT / "extraction-metadata" / "cpp-core-guidelines-analysis.md"

TOP_HEADING = re.compile(r'^# <a name="(?P<anchor>[^"]+)"></a>(?P<title>.+)$')
RULE_HEADING = re.compile(
    r'^### <a name="(?P<anchor>[^"]+)"></a>(?P<rule>[A-Za-z]+(?:\.[A-Za-z]+)?\.\d+): (?P<title>.+)$'
)


@dataclass(frozen=True)
class GuideSpec:
    filename: str
    title: str
    purpose: str
    sections: tuple[str, ...]


GUIDES_BY_TOPIC: tuple[GuideSpec, ...] = (
    GuideSpec(
        "01-core-idioms.md",
        "Core C++ Idioms",
        "Load for any C++ task to ground design in modern C++, type safety, simplicity, immutability, naming, and guideline enforcement.",
        ("s-abstract", "s-introduction", "s-philosophy", "s-naming"),
    ),
    GuideSpec(
        "02-api-design.md",
        "API and Interface Design",
        "Load for public APIs, module boundaries, ownership contracts at interfaces, pre/postconditions, ABI, and Pimpl decisions.",
        ("s-interfaces",),
    ),
    GuideSpec(
        "03-functions.md",
        "Functions and Parameter Passing",
        "Load for function size, parameter passing, return values, lambdas, `constexpr`, `inline`, `noexcept`, and varargs avoidance.",
        ("s-functions",),
    ),
    GuideSpec(
        "04-classes-and-value-types.md",
        "Classes, Value Types, and Enumerations",
        "Load for class design, constructors/destructors, regular/value types, class hierarchies, operators, unions, and enumerations.",
        ("s-class", "s-enum"),
    ),
    GuideSpec(
        "05-resource-management.md",
        "Resource Management and Ownership",
        "Load for RAII, ownership, raw pointers/references, allocation, smart pointers, spans, `not_null`, and GSL ownership vocabulary.",
        ("s-resource", "s-gsl"),
    ),
    GuideSpec(
        "06-error-handling.md",
        "Error Handling",
        "Load for exceptions, `noexcept`, constructors that fail, error codes, failure contracts, and exception-safety decisions.",
        ("s-errors",),
    ),
    GuideSpec(
        "07-templates-and-generics.md",
        "Templates and Generic Programming",
        "Load for templates, concepts, generic constraints, template metaprogramming, variadic templates, and generic API design.",
        ("s-templates",),
    ),
    GuideSpec(
        "08-concurrency.md",
        "Concurrency and Parallelism",
        "Load for threads, data races, synchronization, joining/detaching, tasks, message passing, and shared state.",
        ("s-concurrency",),
    ),
    GuideSpec(
        "09-performance.md",
        "Performance",
        "Load for cost models, allocation, redundant work, indirection, false sharing, compact data, and performance-related tradeoffs.",
        ("s-performance",),
    ),
    GuideSpec(
        "10-expressions-and-statements.md",
        "Expressions, Statements, and Constants",
        "Load for initialization, scope, casts, macros, arithmetic, pointers, control flow, `const`, and `constexpr` use.",
        ("s-expr", "s-const"),
    ),
    GuideSpec(
        "12-project-structure-and-tooling.md",
        "Project Structure and Tooling",
        "Load for source files, headers, namespaces, build/tool support, profiles, enforcement, suppression, and codebase organization.",
        ("s-source", "s-profile", "s-tools"),
    ),
    GuideSpec(
        "13-standard-library.md",
        "Standard Library",
        "Load for standard-library usage, containers, algorithms, strings, views/spans, and library selection.",
        ("s-stdlib", "s-libraries"),
    ),
    GuideSpec(
        "14-c-style-and-modernization.md",
        "C-Style Code and Modernization",
        "Load for C interoperability, C-style idioms to contain or replace, legacy modernization, and gradual adoption strategy.",
        ("s-cpl", "s-modernizing"),
    ),
    GuideSpec(
        "15-reference-and-glossary.md",
        "Reference, FAQ, and Glossary",
        "Load for original references, FAQ entries, architectural notes, non-rules/myths, discussion material, and glossary terms.",
        ("s-a", "s-not", "s-references", "s-faq", "s-discussion", "s-glossary", "s-unclassified"),
    ),
)


NEGATIVE_TERMS = (
    "avoid",
    "don't",
    "do not",
    "never",
    "must not",
    "should not",
    "no naked",
)


def top_sections(lines: list[str]) -> dict[str, tuple[int, int, str]]:
    starts: list[tuple[str, int, str]] = []
    for i, line in enumerate(lines):
        match = TOP_HEADING.match(line)
        if match:
            starts.append((match.group("anchor"), i, match.group("title").strip()))

    sections: dict[str, tuple[int, int, str]] = {}
    for index, (anchor, start, title) in enumerate(starts):
        end = starts[index + 1][1] if index + 1 < len(starts) else len(lines)
        sections[anchor] = (start, end, title)
    return sections


def rules(lines: list[str]) -> list[dict[str, str | int]]:
    found: list[dict[str, str | int]] = []
    for i, line in enumerate(lines, start=1):
        match = RULE_HEADING.match(line)
        if match:
            found.append(
                {
                    "line": i,
                    "anchor": match.group("anchor"),
                    "rule": match.group("rule"),
                    "title": match.group("title").strip(),
                }
            )
    return found


def section_for_line(sections: dict[str, tuple[int, int, str]], line_number: int) -> str | None:
    offset = line_number - 1
    for anchor, (start, end, _title) in sections.items():
        if start <= offset < end:
            return anchor
    return None


def demote_headings(text: str) -> str:
    out: list[str] = []
    for line in text.splitlines():
        line = line.rstrip()
        if line.startswith("#"):
            out.append("#" + line)
        else:
            out.append(line)
    return "\n".join(out).rstrip() + "\n"


def rule_index_for_sections(
    all_rules: list[dict[str, str | int]],
    sections: dict[str, tuple[int, int, str]],
    anchors: tuple[str, ...],
) -> list[dict[str, str | int]]:
    wanted = set(anchors)
    return [rule for rule in all_rules if section_for_line(sections, int(rule["line"])) in wanted]


def write_guide(
    spec: GuideSpec,
    lines: list[str],
    sections: dict[str, tuple[int, int, str]],
    all_rules: list[dict[str, str | int]],
) -> None:
    selected_rules = rule_index_for_sections(all_rules, sections, spec.sections)
    parts = [
        f"# {spec.title}",
        "",
        spec.purpose,
        "",
        "Source: `knowledge/cpp/sources/md/cpp-core-guidelines/CppCoreGuidelines.md`.",
        "The imported source is authoritative; this guide preserves selected upstream sections with headings demoted one level.",
        "",
        "## Source Sections",
        "",
    ]
    for anchor in spec.sections:
        start, end, title = sections[anchor]
        parts.append(f"- `{anchor}` — {title} (source lines {start + 1}-{end})")
    parts.extend(["", "## Rule Index", ""])
    if selected_rules:
        for rule in selected_rules:
            parts.append(
                f"- `{rule['rule']}` — {rule['title']} "
                f"(`{rule['anchor']}`, source line {rule['line']})"
            )
    else:
        parts.append("- No numbered rule headings in these source sections.")
    parts.extend(["", "---", ""])

    for anchor in spec.sections:
        start, end, _title = sections[anchor]
        parts.append(demote_headings("".join(lines[start:end])))
    (GUIDES / spec.filename).write_text("\n".join(parts).rstrip() + "\n", encoding="utf-8")


def write_anti_patterns(
    all_rules: list[dict[str, str | int]],
    sections: dict[str, tuple[int, int, str]],
    section_to_guide: dict[str, str],
) -> None:
    selected = []
    for rule in all_rules:
        title = str(rule["title"])
        lowered = title.casefold()
        if any(term in lowered for term in NEGATIVE_TERMS):
            section = section_for_line(sections, int(rule["line"]))
            selected.append((rule, section))

    parts = [
        "# Anti-Patterns",
        "",
        "The cheap safety net for C++ work. Load this first on any C++ task, then load the home guide for each relevant rule.",
        "",
        "This file is an index of negative C++ Core Guidelines rules: `Avoid`, `Don't`, `Do not`, `Never`, `must not`, and close variants.",
        "It intentionally points back to the topic guides so the detailed upstream rationale, examples, and enforcement text stay in one place.",
        "",
        "## Anti-Pattern Index",
        "",
        "| Rule | Avoid | Home Guide | Source Anchor |",
        "|------|-------|------------|---------------|",
    ]
    for rule, section in selected:
        guide = section_to_guide.get(section or "", "15-reference-and-glossary.md")
        parts.append(f"| `{rule['rule']}` | {rule['title']} | `{guide}` | `{rule['anchor']}` |")
    parts.extend(
        [
            "",
            "## Review Routine",
            "",
            "1. Scan this table before writing or reviewing C++.",
            "2. Open the home guide for any rule family touched by the code.",
            "3. Prefer repairs that preserve C++ Core Guideline intent: type safety, resource safety, RAII, clear ownership, scoped lifetime, and simple interfaces.",
            "4. When project constraints force a violation, isolate it behind the smallest interface and document the reason, matching `I.30`.",
            "",
            "## Recurring Generated-Code Risks",
            "",
            "- Raw ownership transfer through `T*` or `T&` instead of RAII handles.",
            "- Uninitialized objects, reused variables, and hidden lifetime extension assumptions.",
            "- `new`/`delete`, `malloc`/`free`, `reinterpret_cast`, macros, and naked unions where safer standard-library or type-system alternatives exist.",
            "- Lambda reference captures that outlive their scope or cross threads.",
            "- Polymorphic base classes without virtual/protected destructors, missing `override`, or public copy/move.",
            "- Detached threads, data races, mutable shared state, or blocking work without lifecycle ownership.",
            "- Exception-safety drift: throwing destructors, broad catch-all handling, or missing `noexcept` on functions that must not throw.",
        ]
    )
    (GUIDES / "11-anti-patterns.md").write_text("\n".join(parts).rstrip() + "\n", encoding="utf-8")


def write_analysis(
    lines: list[str],
    sections: dict[str, tuple[int, int, str]],
    all_rules: list[dict[str, str | int]],
    section_to_guide: dict[str, str],
) -> None:
    by_guide: dict[str, int] = {}
    for rule in all_rules:
        section = section_for_line(sections, int(rule["line"]))
        guide = section_to_guide.get(section or "", "unmapped")
        by_guide[guide] = by_guide.get(guide, 0) + 1

    parts = [
        "# C++ Core Guidelines Split Analysis",
        "",
        "Generated by `knowledge/cpp/tools/split_cpp_core_guidelines.py` from the subtree-preserved upstream source.",
        "",
        "## Source",
        "",
        "- Upstream repository: `github.com/isocpp/CppCoreGuidelines`",
        "- Imported source: `knowledge/cpp/sources/md/cpp-core-guidelines/CppCoreGuidelines.md`",
        f"- Source line count: {len(lines)}",
        f"- Top-level sections detected: {len(sections)}",
        f"- Numbered rule headings detected: {len(all_rules)}",
        "",
        "## Split Strategy",
        "",
        "The upstream document is already structured by stable guideline IDs (`P`, `I`, `F`, `C`, `R`, `ES`, `Per`, `CP`, `E`, `T`, and related families).",
        "The guide layer keeps those IDs and original anchors intact, but groups top-level source sections into task-oriented chapters that match the Rust, Go, and Erlang knowledge packs.",
        "",
        "The original subtree remains the authoritative source. Generated guides demote headings and add a chapter purpose, source-section index, and rule index so an LLM can choose a small topic file before reading detailed rationale and examples.",
        "",
        "## Guide Map",
        "",
        "| Guide | Source Sections | Rule Count |",
        "|-------|-----------------|------------|",
    ]
    for spec in GUIDES_BY_TOPIC:
        names = ", ".join(f"`{anchor}`" for anchor in spec.sections)
        parts.append(f"| `{spec.filename}` | {names} | {by_guide.get(spec.filename, 0)} |")
    parts.append("| `11-anti-patterns.md` | Negative-rule index across all sections | derived index |")
    parts.extend(["", "## Top-Level Source Sections", ""])
    for anchor, (start, end, title) in sections.items():
        guide = section_to_guide.get(anchor, "not copied into a topic guide")
        parts.append(f"- `{anchor}` — {title}; lines {start + 1}-{end}; guide `{guide}`")
    ANALYSIS.write_text("\n".join(parts).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    lines = SOURCE.read_text(encoding="utf-8").splitlines(keepends=True)
    sections = top_sections(lines)
    all_rules = rules(lines)
    GUIDES.mkdir(parents=True, exist_ok=True)
    ANALYSIS.parent.mkdir(parents=True, exist_ok=True)

    section_to_guide = {
        anchor: spec.filename
        for spec in GUIDES_BY_TOPIC
        for anchor in spec.sections
    }

    for spec in GUIDES_BY_TOPIC:
        missing = [anchor for anchor in spec.sections if anchor not in sections]
        if missing:
            raise SystemExit(f"missing expected source sections for {spec.filename}: {missing}")
        write_guide(spec, lines, sections, all_rules)

    write_anti_patterns(all_rules, sections, section_to_guide)
    write_analysis(lines, sections, all_rules, section_to_guide)


if __name__ == "__main__":
    main()
