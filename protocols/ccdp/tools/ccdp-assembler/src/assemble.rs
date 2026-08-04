//! Assembly of the full document, in either output flavor.
//!
//! `--format kramdown-rfc` keeps the original `--- abstract` / `--- middle`
//! / `--- back` section markers. `--format gfm` drops them entirely: every
//! chapter already carries a numbered heading, so the document is one
//! continuous flow from Section 1 through Section 18 plus an
//! Acknowledgements placeholder (see [`assemble_gfm`]).

use anyhow::{Context, Result, bail};

use crate::chapters::{self, Chapter};
use crate::cli::Format;
use crate::frontmatter;
use crate::headers;
use crate::references::ReferenceSet;
use crate::toc;

const MIDDLE_FIRST: u32 = 2;
const MIDDLE_LAST: u32 = 16;
const SECURITY_CONSIDERATIONS: u32 = 17;
const REFERENCES: u32 = 18;

fn warn_missing_in_range(chapters: &[Chapter], start: u32, end: u32) {
    for number in start..=end {
        if chapters::find(chapters, number).is_none() {
            eprintln!(
                "warning: chapter {number:02} is missing from the source directory, skipping"
            );
        }
    }
}

/// Extracts the abstract body: everything after the first `## ` header in
/// `01-abstract.md`, which drops the document title and the version/date
/// lines that now live in the front matter.
pub fn abstract_body(chapter: &Chapter) -> Result<String> {
    let start = chapter
        .content
        .lines()
        .position(|line| line.starts_with("## "))
        .with_context(|| format!("{}: no '## ' abstract header found", chapter.path.display()))?;
    let body: Vec<&str> = chapter.content.lines().skip(start + 1).collect();
    Ok(body.join("\n").trim().to_string())
}

/// Concatenates chapters 2–16 with header-rewritten content, blank-line
/// separated. Missing chapters in the range are warned about and skipped.
pub fn middle_body(chapters: &[Chapter]) -> String {
    warn_missing_in_range(chapters, MIDDLE_FIRST, MIDDLE_LAST);
    chapters::in_range(chapters, MIDDLE_FIRST, MIDDLE_LAST)
        .iter()
        .map(|c| {
            headers::rewrite_content(&c.content, Format::KramdownRfc)
                .trim()
                .to_string()
        })
        .collect::<Vec<_>>()
        .join("\n\n")
}

const REFERENCES_NOTE: &str = "<!-- Note: kramdown-rfc auto-generates a normative/informative \
References section from the YAML front matter. The section below is a \
human-readable companion for readers outside the RFC toolchain. -->";

const ACKNOWLEDGEMENTS_KRAMDOWN: &str = "# Acknowledgements {#Acknowledgements}\n\
{: numbered=\"false\"}\n\
\n\
_Placeholder — to be completed._";

const ACKNOWLEDGEMENTS_GFM: &str =
    "<a id=\"acknowledgements\"></a>\n# Acknowledgements\n\n_Placeholder — to be completed._";

/// Concatenates the Security Considerations and References chapters, adds
/// a note about YAML/markdown reference redundancy, and appends an
/// Acknowledgements placeholder.
pub fn back_body(chapters: &[Chapter]) -> Result<String> {
    let mut parts = Vec::new();

    match chapters::find(chapters, SECURITY_CONSIDERATIONS) {
        Some(chapter) => parts.push(
            headers::rewrite_content(&chapter.content, Format::KramdownRfc)
                .trim()
                .to_string(),
        ),
        None => eprintln!(
            "warning: chapter {SECURITY_CONSIDERATIONS:02} (Security Considerations) is missing, skipping"
        ),
    }

    let references_chapter = chapters::find(chapters, REFERENCES)
        .with_context(|| format!("chapter {REFERENCES:02} (References) is required but was not found in the source directory"))?;
    parts.push(format!(
        "{REFERENCES_NOTE}\n\n{}",
        headers::rewrite_content(&references_chapter.content, Format::KramdownRfc).trim()
    ));

    parts.push(ACKNOWLEDGEMENTS_KRAMDOWN.to_string());

    Ok(parts.join("\n\n"))
}

/// Assembles the full kramdown-rfc document: front matter, abstract,
/// middle, and back sections, joined by `--- abstract` / `--- middle` /
/// `--- back` markers.
pub fn assemble_kramdown_rfc(
    chapters: &[Chapter],
    refs: &ReferenceSet,
    version: &str,
    date: &str,
) -> Result<String> {
    let abstract_chapter = chapters::find(chapters, 1).with_context(|| {
        "chapter 01 (Abstract) is required but was not found in the source directory".to_string()
    })?;
    let abstract_text = abstract_body(abstract_chapter)?;
    if abstract_text.is_empty() {
        bail!(
            "{}: abstract body is empty after header stripping",
            abstract_chapter.path.display()
        );
    }

    let front_matter = frontmatter::render_kramdown_rfc(version, date, refs);
    let middle = middle_body(chapters);
    let back = back_body(chapters)?;

    Ok(format!(
        "{front_matter}\n\
         \n\
         --- abstract\n\
         \n\
         {abstract_text}\n\
         \n\
         --- middle\n\
         \n\
         {middle}\n\
         \n\
         --- back\n\
         \n\
         {back}\n"
    ))
}

/// Rewrites a chapter's content for GFM: drops any title-block lines before
/// its first numbered heading (only chapter 1 has any — the document H1 and
/// the bold version/date lines, now redundant with the front matter), then
/// applies GFM header rewriting.
fn gfm_chapter_body(chapter: &Chapter) -> String {
    let lines: Vec<&str> = chapter.content.lines().collect();
    let start = lines
        .iter()
        .position(|line| headers::parse_numbered_header(line).is_some())
        .unwrap_or(0);
    let body = lines[start..].join("\n");
    headers::rewrite_content(&body, Format::Gfm)
        .trim()
        .to_string()
}

/// Assembles the full GFM document: front matter, an optional Table of
/// Contents, chapters 1–18 as one continuous flow (each already carries a
/// numbered heading, so no section markers are needed), and an
/// Acknowledgements placeholder.
pub fn assemble_gfm(
    chapters: &[Chapter],
    version: &str,
    date: &str,
    include_toc: bool,
) -> Result<String> {
    chapters::find(chapters, 1).with_context(|| {
        "chapter 01 (Abstract) is required but was not found in the source directory".to_string()
    })?;
    chapters::find(chapters, REFERENCES)
        .with_context(|| format!("chapter {REFERENCES:02} (References) is required but was not found in the source directory"))?;
    warn_missing_in_range(chapters, MIDDLE_FIRST, SECURITY_CONSIDERATIONS);

    let body = chapters::in_range(chapters, 1, REFERENCES)
        .iter()
        .map(|c| gfm_chapter_body(c))
        .collect::<Vec<_>>()
        .join("\n\n");

    let mut out = format!("{}\n", frontmatter::render_gfm(version, date));
    if include_toc {
        out.push_str(&toc::generate(chapters));
        out.push('\n');
    }
    out.push_str(&body);
    out.push_str("\n\n");
    out.push_str(ACKNOWLEDGEMENTS_GFM);
    out.push('\n');
    Ok(out)
}

#[cfg(test)]
mod tests {
    use std::path::PathBuf;

    use super::*;
    use crate::references::Reference;

    fn chapter(number: u32, content: &str) -> Chapter {
        Chapter {
            number,
            path: PathBuf::from(format!("{number:02}-test.md")),
            content: content.to_string(),
        }
    }

    fn sample_chapters() -> Vec<Chapter> {
        vec![
            chapter(1, "# Title\n\n## 1. Abstract\n\nAn abstract.\n"),
            chapter(
                2,
                "# 2. Conventions\n\n## 2.1. Status\n\nSome text about Section 2.1.\n",
            ),
            chapter(17, "# 17. Security Considerations\n\nSecurity text.\n"),
            chapter(
                18,
                "# 18. References\n\n## 18.1. Normative References\n\n**[RFC 2119]** Bradner, S., \"Key words,\" RFC 2119, 1997.\n",
            ),
        ]
    }

    fn sample_refs() -> ReferenceSet {
        ReferenceSet {
            normative: vec![Reference {
                key: "RFC 2119".to_string(),
                body: String::new(),
            }],
            informative: vec![],
        }
    }

    #[test]
    fn abstract_body_strips_title_and_dates() {
        let ch = chapter(
            1,
            "# CCDP: Composite Cognition Dispatch Protocol\n\
             \n\
             **Draft Specification — Version 0.1**\n\
             **August 2026**\n\
             \n\
             ---\n\
             \n\
             ## 1. Abstract\n\
             \n\
             First paragraph.\n\
             \n\
             Second paragraph.\n",
        );
        let body = abstract_body(&ch).unwrap();
        assert_eq!(body, "First paragraph.\n\nSecond paragraph.");
    }

    #[test]
    fn kramdown_rfc_end_to_end_assembly() {
        let chapters = sample_chapters();
        let refs = sample_refs();
        let doc = assemble_kramdown_rfc(&chapters, &refs, "0.1", "2026-08-03").unwrap();

        assert!(doc.starts_with("---\n"));
        let abstract_idx = doc.find("--- abstract").unwrap();
        let middle_idx = doc.find("--- middle").unwrap();
        let back_idx = doc.find("--- back").unwrap();
        assert!(abstract_idx < middle_idx);
        assert!(middle_idx < back_idx);
        assert!(doc.contains("An abstract."));
        assert!(doc.contains("# Conventions {#section-2}"));
        assert!(doc.contains("## Status {#section-2-1}"));
        assert!(doc.contains("# Security Considerations {#section-17}"));
        assert!(doc.contains("# References {#section-18}"));
        assert!(doc.contains("# Acknowledgements {#Acknowledgements}"));
    }

    #[test]
    fn kramdown_rfc_missing_abstract_chapter_is_an_error() {
        let chapters = vec![chapter(
            18,
            "# 18. References\n\n## 18.1. Normative References\n",
        )];
        let refs = ReferenceSet::default();
        assert!(assemble_kramdown_rfc(&chapters, &refs, "0.1", "2026-08-03").is_err());
    }

    #[test]
    fn kramdown_rfc_missing_references_chapter_is_an_error() {
        let chapters = vec![chapter(1, "# Title\n\n## 1. Abstract\n\nText.\n")];
        assert!(back_body(&chapters).is_err());
    }

    #[test]
    fn gfm_end_to_end_assembly_has_no_section_markers() {
        let chapters = sample_chapters();
        let doc = assemble_gfm(&chapters, "0.1", "2026-08-03", true).unwrap();

        assert!(doc.starts_with("---\n"));
        assert!(!doc.contains("--- abstract"));
        assert!(!doc.contains("--- middle"));
        assert!(!doc.contains("--- back"));
        assert!(doc.contains("An abstract."));
        assert!(doc.contains("<a id=\"section-1\"></a>\n## Abstract"));
        assert!(doc.contains("<a id=\"section-2\"></a>\n# Conventions"));
        assert!(doc.contains("<a id=\"section-2-1\"></a>\n## Status"));
        assert!(doc.contains("<a id=\"section-17\"></a>\n# Security Considerations"));
        assert!(doc.contains("<a id=\"section-18\"></a>\n# References"));
        assert!(doc.contains("<a id=\"acknowledgements\"></a>\n# Acknowledgements"));
        // Chapter 1's document title and bold version/date lines are dropped.
        assert!(!doc.contains("# Title"));
    }

    #[test]
    fn gfm_includes_toc_by_default_and_can_be_suppressed() {
        let chapters = sample_chapters();
        let with_toc = assemble_gfm(&chapters, "0.1", "2026-08-03", true).unwrap();
        assert!(with_toc.contains("## Table of Contents"));
        assert!(with_toc.contains("- [1. Abstract](#section-1)"));

        let without_toc = assemble_gfm(&chapters, "0.1", "2026-08-03", false).unwrap();
        assert!(!without_toc.contains("## Table of Contents"));
    }

    #[test]
    fn gfm_missing_abstract_chapter_is_an_error() {
        let chapters = vec![chapter(
            18,
            "# 18. References\n\n## 18.1. Normative References\n",
        )];
        assert!(assemble_gfm(&chapters, "0.1", "2026-08-03", true).is_err());
    }

    #[test]
    fn gfm_missing_references_chapter_is_an_error() {
        let chapters = vec![chapter(1, "# Title\n\n## 1. Abstract\n\nText.\n")];
        assert!(assemble_gfm(&chapters, "0.1", "2026-08-03", true).is_err());
    }
}
