//! Header rewriting for kramdown-rfc compatibility.
//!
//! Source chapters number their headers (`# 10. Title`, `## 10.1. Title`).
//! kramdown-rfc auto-numbers sections, so the numeric prefix is stripped and
//! replaced with a stable `{#section-N-M}` IAL anchor that preserves the
//! ability to resolve bare `Section N.M` prose references.

use std::sync::LazyLock;

use regex::Regex;

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
/// gain a `{#section-N-M}` anchor; every other line passes through unchanged.
pub fn rewrite_line(line: &str) -> String {
    match parse_numbered_header(line) {
        Some(header) => {
            let hashes = "#".repeat(header.level);
            let anchor = anchor_slug(header.number);
            format!("{hashes} {} {{#section-{anchor}}}", header.title)
        }
        None => line.to_string(),
    }
}

/// Rewrites every line of a chapter's content.
pub fn rewrite_content(content: &str) -> String {
    content
        .lines()
        .map(rewrite_line)
        .collect::<Vec<_>>()
        .join("\n")
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn strips_chapter_prefix_and_anchors() {
        assert_eq!(
            rewrite_line("# 10. Provenance and Evidence Grades"),
            "# Provenance and Evidence Grades {#section-10}"
        );
    }

    #[test]
    fn strips_subsection_prefix_and_anchors() {
        assert_eq!(
            rewrite_line("## 10.1. Rationale"),
            "## Rationale {#section-10-1}"
        );
    }

    #[test]
    fn handles_three_level_numbers() {
        assert_eq!(
            rewrite_line("### 10.5.1. Sequential Composition (Weakest-Link Rule)"),
            "### Sequential Composition (Weakest-Link Rule) {#section-10-5-1}"
        );
    }

    #[test]
    fn leaves_unnumbered_headers_untouched() {
        assert_eq!(rewrite_line("### Grade 0: OPAQUE"), "### Grade 0: OPAQUE");
        assert_eq!(
            rewrite_line("### Step 1: Explicit Destination"),
            "### Step 1: Explicit Destination"
        );
    }

    #[test]
    fn leaves_non_header_lines_untouched() {
        assert_eq!(
            rewrite_line("Section 10.1 discusses rationale."),
            "Section 10.1 discusses rationale."
        );
        assert_eq!(rewrite_line(""), "");
    }

    #[test]
    fn anchor_slug_replaces_dots_with_dashes() {
        assert_eq!(anchor_slug("10"), "10");
        assert_eq!(anchor_slug("10.5.4"), "10-5-4");
    }
}
