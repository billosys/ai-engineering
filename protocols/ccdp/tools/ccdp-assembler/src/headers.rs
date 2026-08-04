//! Header rewriting for the assembled document.
//!
//! Source chapters number their headers (`# 10. Title`, `## 10.1. Title`).
//! Both output formats auto-number sections themselves, so the numeric
//! prefix is stripped and replaced with a stable anchor that preserves the
//! ability to resolve bare `Section N.M` prose references — as a `{#anchor}`
//! kramdown IAL for `--format kramdown-rfc`, or a `<a id="anchor"></a>` tag
//! on the line before the heading for `--format gfm` (GitHub doesn't render
//! kramdown IALs; they'd show up as literal text).

use std::sync::LazyLock;

use regex::Regex;

use crate::cli::Format;

static NUMBERED_HEADER_RE: LazyLock<Regex> = LazyLock::new(|| {
    Regex::new(r"^(#{1,6})\s+(\d+(?:\.\d+)*)\.\s+(.+?)\s*$").expect("static regex is valid")
});

/// A parsed numbered header: hash level, dotted section number, and title text.
pub struct NumberedHeader<'a> {
    pub level: usize,
    pub number: &'a str,
    pub title: &'a str,
}

/// Parses a line as a numbered header (`# N. Title`, `## N.M. Title`, ...).
///
/// Returns `None` for headers that don't follow the numeric-prefix
/// convention (e.g. `### Grade 0: OPAQUE`) — those are left untouched by
/// the assembler.
pub fn parse_numbered_header(line: &str) -> Option<NumberedHeader<'_>> {
    let caps = NUMBERED_HEADER_RE.captures(line)?;
    let level = caps.get(1).expect("group 1 always matches").as_str().len();
    let number = caps.get(2).expect("group 2 always matches").as_str();
    let title = caps.get(3).expect("group 3 always matches").as_str();
    Some(NumberedHeader {
        level,
        number,
        title,
    })
}

/// Converts a dotted section number (`10.5.1`) into its anchor slug (`10-5-1`).
pub fn anchor_slug(number: &str) -> String {
    number.replace('.', "-")
}

/// Rewrites a single line: numbered headers lose their numeric prefix and
/// gain a format-appropriate anchor; every other line passes through
/// unchanged. For GFM, the anchor is a separate `<a id="...">` line
/// prepended before the heading, so the result may itself contain a newline.
pub fn rewrite_line(line: &str, format: Format) -> String {
    match parse_numbered_header(line) {
        Some(header) => {
            let hashes = "#".repeat(header.level);
            let anchor = anchor_slug(header.number);
            match format {
                Format::KramdownRfc => format!("{hashes} {} {{#section-{anchor}}}", header.title),
                Format::Gfm => {
                    format!("<a id=\"section-{anchor}\"></a>\n{hashes} {}", header.title)
                }
            }
        }
        None => line.to_string(),
    }
}

/// Rewrites every line of a chapter's content.
pub fn rewrite_content(content: &str, format: Format) -> String {
    content
        .lines()
        .map(|line| rewrite_line(line, format))
        .collect::<Vec<_>>()
        .join("\n")
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn kramdown_strips_chapter_prefix_and_anchors() {
        assert_eq!(
            rewrite_line("# 10. Provenance and Evidence Grades", Format::KramdownRfc),
            "# Provenance and Evidence Grades {#section-10}"
        );
    }

    #[test]
    fn kramdown_strips_subsection_prefix_and_anchors() {
        assert_eq!(
            rewrite_line("## 10.1. Rationale", Format::KramdownRfc),
            "## Rationale {#section-10-1}"
        );
    }

    #[test]
    fn kramdown_handles_three_level_numbers() {
        assert_eq!(
            rewrite_line(
                "### 10.5.1. Sequential Composition (Weakest-Link Rule)",
                Format::KramdownRfc
            ),
            "### Sequential Composition (Weakest-Link Rule) {#section-10-5-1}"
        );
    }

    #[test]
    fn gfm_prepends_anchor_tag_and_strips_prefix() {
        assert_eq!(
            rewrite_line("# 10. Provenance and Evidence Grades", Format::Gfm),
            "<a id=\"section-10\"></a>\n# Provenance and Evidence Grades"
        );
    }

    #[test]
    fn gfm_subsection_anchor_uses_dashed_number() {
        assert_eq!(
            rewrite_line("## 10.1. Rationale", Format::Gfm),
            "<a id=\"section-10-1\"></a>\n## Rationale"
        );
    }

    #[test]
    fn leaves_unnumbered_headers_untouched_in_both_formats() {
        for format in [Format::KramdownRfc, Format::Gfm] {
            assert_eq!(
                rewrite_line("### Grade 0: OPAQUE", format),
                "### Grade 0: OPAQUE"
            );
            assert_eq!(
                rewrite_line("### Step 1: Explicit Destination", format),
                "### Step 1: Explicit Destination"
            );
        }
    }

    #[test]
    fn leaves_non_header_lines_untouched_in_both_formats() {
        for format in [Format::KramdownRfc, Format::Gfm] {
            assert_eq!(
                rewrite_line("Section 10.1 discusses rationale.", format),
                "Section 10.1 discusses rationale."
            );
            assert_eq!(rewrite_line("", format), "");
        }
    }

    #[test]
    fn anchor_slug_replaces_dots_with_dashes() {
        assert_eq!(anchor_slug("10"), "10");
        assert_eq!(anchor_slug("10.5.4"), "10-5-4");
    }

    #[test]
    fn gfm_rewrite_content_keeps_anchor_and_heading_on_adjacent_lines() {
        let out = rewrite_content(
            "# 10. Provenance and Evidence Grades\n\nBody text.",
            Format::Gfm,
        );
        assert_eq!(
            out,
            "<a id=\"section-10\"></a>\n# Provenance and Evidence Grades\n\nBody text."
        );
    }
}
