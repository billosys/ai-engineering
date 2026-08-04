//! Table of Contents generation for GFM output.
//!
//! GitHub doesn't auto-generate a TOC for long documents, so `--format gfm`
//! emits an explicit one built from the same numbered headers the header
//! rewriter turns into anchors — chapter-level and immediate-subsection
//! entries only, to keep a 20-chapter spec's TOC navigable.

use crate::chapters::Chapter;
use crate::headers;

/// Depth of a section number: `10` is depth 1, `10.5` is depth 2, `10.5.1` is depth 3.
fn depth(number: &str) -> usize {
    number.matches('.').count() + 1
}

/// Renders a `## Table of Contents` block linking to every chapter- and
/// subsection-level (depth 1 and 2) heading anchor, in document order.
pub fn generate(chapters: &[Chapter]) -> String {
    let mut out = String::from("## Table of Contents\n\n");
    for chapter in chapters {
        for line in chapter.content.lines() {
            let Some(header) = headers::parse_numbered_header(line) else {
                continue;
            };
            if depth(header.number) > 2 {
                continue;
            }
            let indent = if depth(header.number) == 1 { "" } else { "  " };
            let anchor = headers::anchor_slug(header.number);
            out.push_str(&format!(
                "{indent}- [{}. {}](#section-{anchor})\n",
                header.number, header.title
            ));
        }
    }
    out
}

#[cfg(test)]
mod tests {
    use std::path::PathBuf;
    use std::sync::LazyLock;

    use regex::Regex;

    use super::*;
    use crate::cli::Format;

    fn chapter(number: u32, content: &str) -> Chapter {
        Chapter {
            number,
            path: PathBuf::from(format!("{number:02}-test.md")),
            content: content.to_string(),
        }
    }

    #[test]
    fn includes_chapter_and_subsection_entries_with_indentation() {
        let chapters = vec![
            chapter(1, "## 1. Abstract\n\nText.\n"),
            chapter(2, "# 2. Conventions\n\n## 2.1. Status\n\nText.\n"),
        ];
        let toc = generate(&chapters);
        assert!(toc.starts_with("## Table of Contents\n\n"));
        assert!(toc.contains("- [1. Abstract](#section-1)\n"));
        assert!(toc.contains("- [2. Conventions](#section-2)\n"));
        assert!(toc.contains("  - [2.1. Status](#section-2-1)\n"));
    }

    #[test]
    fn omits_entries_deeper_than_subsection_level() {
        let chapters = vec![chapter(
            10,
            "# 10. Provenance\n\n## 10.5. Composition\n\n### 10.5.1. Sequential\n\nText.\n",
        )];
        let toc = generate(&chapters);
        assert!(!toc.contains("10.5.1"));
    }

    #[test]
    fn every_toc_anchor_matches_a_generated_gfm_anchor() {
        let chapters = vec![
            chapter(1, "## 1. Abstract\n\nText.\n"),
            chapter(
                2,
                "# 2. Conventions\n\n## 2.1. Status\n\n## 2.2. Requirements\n\nText.\n",
            ),
        ];
        let toc = generate(&chapters);

        static LINK_RE: LazyLock<Regex> =
            LazyLock::new(|| Regex::new(r"\(#(section-[a-z0-9-]+)\)").expect("valid"));
        let anchors: Vec<&str> = LINK_RE
            .captures_iter(&toc)
            .map(|c| c.get(1).unwrap().as_str())
            .collect();
        assert!(!anchors.is_empty());

        let rewritten: String = chapters
            .iter()
            .map(|c| headers::rewrite_content(&c.content, Format::Gfm))
            .collect::<Vec<_>>()
            .join("\n");
        for anchor in anchors {
            let needle = format!("<a id=\"{anchor}\"></a>");
            assert!(
                rewritten.contains(&needle),
                "TOC links to {anchor} but no matching anchor tag was generated"
            );
        }
    }
}
