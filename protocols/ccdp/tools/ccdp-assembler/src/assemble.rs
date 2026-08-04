//! Assembly of the `--- abstract` / `--- middle` / `--- back` sections.

use anyhow::{Context, Result, bail};

use crate::chapters::{self, Chapter};
use crate::frontmatter;
use crate::headers;
use crate::references::ReferenceSet;

const MIDDLE_FIRST: u32 = 2;
const MIDDLE_LAST: u32 = 16;
const SECURITY_CONSIDERATIONS: u32 = 17;
const REFERENCES: u32 = 18;

/// Extracts the abstract body: everything after the first `## ` header in
/// `01-abstract.md`, which drops the document title and the version/date
/// lines that now live in the YAML front matter.
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
    for number in MIDDLE_FIRST..=MIDDLE_LAST {
        if chapters::find(chapters, number).is_none() {
            eprintln!(
                "warning: chapter {number:02} is missing from the source directory, skipping"
            );
        }
    }
    chapters::in_range(chapters, MIDDLE_FIRST, MIDDLE_LAST)
        .iter()
        .map(|c| headers::rewrite_content(&c.content).trim().to_string())
        .collect::<Vec<_>>()
        .join("\n\n")
}

const REFERENCES_NOTE: &str = "<!-- Note: kramdown-rfc auto-generates a normative/informative \
References section from the YAML front matter. The section below is a \
human-readable companion for readers outside the RFC toolchain. -->";

const ACKNOWLEDGEMENTS: &str = "# Acknowledgements {#Acknowledgements}\n\
{: numbered=\"false\"}\n\
\n\
_Placeholder — to be completed._";

/// Concatenates the Security Considerations and References chapters, adds
/// a note about YAML/markdown reference redundancy, and appends an
/// Acknowledgements placeholder.
pub fn back_body(chapters: &[Chapter]) -> Result<String> {
    let mut parts = Vec::new();

    match chapters::find(chapters, SECURITY_CONSIDERATIONS) {
        Some(chapter) => parts.push(
            headers::rewrite_content(&chapter.content)
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
        headers::rewrite_content(&references_chapter.content).trim()
    ));

    parts.push(ACKNOWLEDGEMENTS.to_string());

    Ok(parts.join("\n\n"))
}

/// Assembles the full kramdown-rfc document: front matter, abstract,
/// middle, and back sections.
pub fn assemble(
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

    let front_matter = frontmatter::render(version, date, refs);
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
    fn end_to_end_two_chapter_assembly() {
        let chapters = vec![
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
        ];
        let refs = ReferenceSet {
            normative: vec![Reference {
                key: "RFC 2119".to_string(),
                body: String::new(),
            }],
            informative: vec![],
        };
        let doc = assemble(&chapters, &refs, "0.1", "2026-08-03").unwrap();

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
    fn missing_abstract_chapter_is_an_error() {
        let chapters = vec![chapter(
            18,
            "# 18. References\n\n## 18.1. Normative References\n",
        )];
        let refs = ReferenceSet::default();
        assert!(assemble(&chapters, &refs, "0.1", "2026-08-03").is_err());
    }

    #[test]
    fn missing_references_chapter_is_an_error() {
        let chapters = vec![chapter(1, "# Title\n\n## 1. Abstract\n\nText.\n")];
        assert!(back_body(&chapters).is_err());
    }
}
