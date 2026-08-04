//! Cross-reference validation: `Section X.Y`, `[RFC XXXX]`, and named
//! (`[Author Year]`) citations, checked against the assembled header and
//! reference sets. Mismatches are reported as warnings to stderr with the
//! originating source file and line number.
//!
//! This runs against the raw chapter sources, not the rewritten output, so
//! it's identical for both `--format` values — it never inspects `{#anchor}`
//! vs. `<a id="anchor">` text, only the same numbered-heading convention
//! `headers::parse_numbered_header` reads to generate either one.

use std::collections::HashSet;
use std::sync::LazyLock;

use regex::Regex;

use crate::chapters::Chapter;
use crate::headers;
use crate::references::ReferenceSet;

static SECTION_RE: LazyLock<Regex> =
    LazyLock::new(|| Regex::new(r"\bSection\s+(\d+(?:\.\d+)*)\b").expect("static regex is valid"));
static BRACKET_RE: LazyLock<Regex> =
    LazyLock::new(|| Regex::new(r"\[([^\[\]]+)\]").expect("static regex is valid"));
static RFC_CITATION_RE: LazyLock<Regex> =
    LazyLock::new(|| Regex::new(r"^RFC[ -]?(\d+)$").expect("static regex is valid"));
// A "named reference" citation, e.g. `[Akerlof 1970]` or `[Huang et al. 2024]`:
// letters/spaces/punctuation ending in a four-digit year. Deliberately does
// not match compound `[A; B; C]` shorthand or bare keys like `[W3C-TC]` —
// those are a different citation style the spec doesn't ask us to validate.
static AUTHOR_YEAR_RE: LazyLock<Regex> = LazyLock::new(|| {
    Regex::new(r"^[A-Z][A-Za-z .,&'-]*\d{4}[a-z]?$").expect("static regex is valid")
});
static YEAR_RE: LazyLock<Regex> =
    LazyLock::new(|| Regex::new(r"\b\d{4}\b").expect("static regex is valid"));
static STOPWORDS: [&str; 4] = ["et", "al", "and", "the"];

fn header_number_index(chapters: &[Chapter]) -> HashSet<String> {
    chapters
        .iter()
        .flat_map(|c| c.content.lines())
        .filter_map(headers::parse_numbered_header)
        .map(|h| h.number.to_string())
        .collect()
}

fn rfc_number_index(refs: &ReferenceSet) -> HashSet<String> {
    refs.all()
        .filter_map(|r| RFC_CITATION_RE.captures(&r.key))
        .map(|c| c[1].to_string())
        .collect()
}

/// Splits a bracket citation like `Huang et al. 2024` into lowercase,
/// stopword-filtered name tokens and the trailing publication year.
fn citation_tokens(inner: &str) -> (Vec<String>, String) {
    let year = YEAR_RE
        .find_iter(inner)
        .last()
        .map(|m| m.as_str().to_string())
        .unwrap_or_default();
    let tokens = inner
        .split(|c: char| !c.is_alphanumeric())
        .map(str::to_lowercase)
        .filter(|w| w.len() >= 3 && !STOPWORDS.contains(&w.as_str()) && *w != year)
        .collect();
    (tokens, year)
}

fn named_reference_found(blobs: &[String], inner: &str) -> bool {
    let (tokens, year) = citation_tokens(inner);
    blobs.iter().any(|blob| {
        tokens.iter().all(|t| blob.contains(t.as_str()))
            && (year.is_empty() || blob.contains(&year))
    })
}

/// Scans every loaded chapter for cross-references and reports mismatches
/// to stderr as `path:line: warning: ...`. Returns the total warning count.
pub fn validate(chapters: &[Chapter], refs: &ReferenceSet) -> usize {
    let header_index = header_number_index(chapters);
    let rfc_index = rfc_number_index(refs);
    let named_blobs: Vec<String> = refs.all().map(|r| r.blob()).collect();

    let mut warnings = 0usize;
    for chapter in chapters {
        for (idx, line) in chapter.content.lines().enumerate() {
            let line_no = idx + 1;
            let path = chapter.path.display();

            for caps in SECTION_RE.captures_iter(line) {
                let number = &caps[1];
                if !header_index.contains(number) {
                    eprintln!(
                        "{path}:{line_no}: warning: 'Section {number}' has no matching header in the assembled document"
                    );
                    warnings += 1;
                }
            }

            for caps in BRACKET_RE.captures_iter(line) {
                let inner = &caps[1];
                if let Some(rfc_caps) = RFC_CITATION_RE.captures(inner) {
                    let number = &rfc_caps[1];
                    if !rfc_index.contains(number) {
                        eprintln!(
                            "{path}:{line_no}: warning: '[{inner}]' is not listed among the normative references"
                        );
                        warnings += 1;
                    }
                } else if AUTHOR_YEAR_RE.is_match(inner)
                    && !named_reference_found(&named_blobs, inner)
                {
                    eprintln!(
                        "{path}:{line_no}: warning: named reference '[{inner}]' was not found in the references chapter"
                    );
                    warnings += 1;
                }
            }
        }
    }
    warnings
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
    fn matching_section_and_rfc_citation_produce_no_warnings() {
        let chapters = vec![chapter(
            2,
            "# 2. Conventions\n\n## 2.1. Status\n\nSee [RFC 2119] and Section 2.1.\n",
        )];
        let refs = ReferenceSet {
            normative: vec![Reference {
                key: "RFC 2119".to_string(),
                body: String::new(),
            }],
            informative: vec![],
        };
        assert_eq!(validate(&chapters, &refs), 0);
    }

    #[test]
    fn dangling_section_reference_is_detected() {
        let chapters = vec![chapter(
            2,
            "# 2. Conventions\n\nSee Section 99.9 for details.\n",
        )];
        let refs = ReferenceSet::default();
        assert_eq!(validate(&chapters, &refs), 1);
    }

    #[test]
    fn dangling_rfc_citation_is_detected() {
        let chapters = vec![chapter(2, "# 2. Conventions\n\nSee [RFC 9999].\n")];
        let refs = ReferenceSet::default();
        assert_eq!(validate(&chapters, &refs), 1);
    }

    #[test]
    fn named_reference_matches_via_author_and_year_tokens() {
        let chapters = vec![chapter(
            3,
            "# 3. Introduction\n\nGrounded in [Huang et al. 2024].\n",
        )];
        let refs = ReferenceSet {
            normative: vec![],
            informative: vec![Reference {
                key: "Huang-2024".to_string(),
                body: "Huang, J., et al., \"Large Language Models Cannot Self-Correct Reasoning Yet,\" ICLR 2024.".to_string(),
            }],
        };
        assert_eq!(validate(&chapters, &refs), 0);
    }

    #[test]
    fn dangling_named_reference_is_detected() {
        let chapters = vec![chapter(3, "# 3. Introduction\n\nSee [Nobody 1999].\n")];
        let refs = ReferenceSet::default();
        assert_eq!(validate(&chapters, &refs), 1);
    }

    #[test]
    fn compound_and_bare_key_citations_are_out_of_scope() {
        let chapters = vec![chapter(
            5,
            "# 5. Architecture\n\nSee [PAL; Logic-LM; SatLM] and [W3C-TC].\n",
        )];
        let refs = ReferenceSet::default();
        assert_eq!(validate(&chapters, &refs), 0);
    }
}
