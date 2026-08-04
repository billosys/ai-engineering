//! Parsing of the References chapter into kramdown-rfc `normative`/`informative`
//! YAML blocks.
//!
//! References are line-oriented: `**[KEY]** rest of the citation text...`.
//! Which bucket a reference falls into is tracked by the nearest `## `
//! section header containing "Normative" or "Informative".

use std::fs;
use std::path::Path;
use std::sync::LazyLock;

use anyhow::{Context, Result};
use regex::Regex;

use crate::yaml;

static REF_ENTRY_RE: LazyLock<Regex> =
    LazyLock::new(|| Regex::new(r"^\*\*\[([^\]]+)\]\*\*\s*(.*)$").expect("static regex is valid"));
static RFC_KEY_RE: LazyLock<Regex> =
    LazyLock::new(|| Regex::new(r"^RFC[ -]?(\d+)$").expect("static regex is valid"));
static TITLE_RE: LazyLock<Regex> =
    LazyLock::new(|| Regex::new("\"([^\"]+)\"").expect("static regex is valid"));
static URL_RE: LazyLock<Regex> =
    LazyLock::new(|| Regex::new(r"https?://\S+").expect("static regex is valid"));
static YEAR_RE: LazyLock<Regex> =
    LazyLock::new(|| Regex::new(r"\b\d{4}\b").expect("static regex is valid"));

/// One `**[KEY]** ...` reference entry from the References chapter.
#[derive(Debug, Clone)]
pub struct Reference {
    pub key: String,
    pub body: String,
}

impl Reference {
    /// The key and body concatenated, for substring-based citation matching.
    pub fn blob(&self) -> String {
        format!("{} {}", self.key, self.body).to_lowercase()
    }
}

/// Normative and informative references, in source order within each bucket.
#[derive(Debug, Clone, Default)]
pub struct ReferenceSet {
    pub normative: Vec<Reference>,
    pub informative: Vec<Reference>,
}

impl ReferenceSet {
    /// Iterates every reference, normative first.
    pub fn all(&self) -> impl Iterator<Item = &Reference> {
        self.normative.iter().chain(self.informative.iter())
    }
}

/// Parses the references chapter into normative and informative buckets.
pub fn parse(path: &Path) -> Result<ReferenceSet> {
    let content = fs::read_to_string(path)
        .with_context(|| format!("failed to read references chapter: {}", path.display()))?;
    Ok(parse_str(&content))
}

/// Parses reference-chapter content already in memory. Split out from
/// [`parse`] so tests can exercise the parsing logic with inline strings
/// instead of real files.
pub fn parse_str(content: &str) -> ReferenceSet {
    let mut set = ReferenceSet::default();
    let mut in_normative = false;

    for line in content.lines() {
        if let Some(rest) = line.strip_prefix("## ") {
            let lower = rest.to_lowercase();
            if lower.contains("normative") {
                in_normative = true;
            } else if lower.contains("informative") {
                in_normative = false;
            }
            continue;
        }

        let Some(caps) = REF_ENTRY_RE.captures(line) else {
            continue;
        };
        let reference = Reference {
            key: caps[1].to_string(),
            body: caps[2].to_string(),
        };
        if in_normative {
            set.normative.push(reference);
        } else {
            set.informative.push(reference);
        }
    }

    set
}

fn sanitize_id(key: &str) -> String {
    let mut id: String = key.chars().filter(|c| c.is_ascii_alphanumeric()).collect();
    if id.chars().next().is_none_or(|c| c.is_ascii_digit()) {
        id = format!("Ref{id}");
    }
    id
}

fn extract_title(body: &str) -> Option<String> {
    TITLE_RE.captures(body).map(|c| c[1].to_string())
}

fn extract_author(body: &str) -> Option<String> {
    let idx = body.find('"')?;
    let author = body[..idx].trim().trim_end_matches(',').trim();
    (!author.is_empty()).then(|| author.to_string())
}

fn extract_target(body: &str) -> Option<String> {
    URL_RE.find(body).map(|m| {
        m.as_str()
            .trim_end_matches(['.', ',', ')', ';'])
            .to_string()
    })
}

fn extract_date(body: &str) -> Option<String> {
    // Search only the prose before the URL: reference URLs routinely embed
    // 4-digit runs of their own (arXiv IDs, dated paths) that would
    // otherwise be mistaken for the publication year.
    let prose = match URL_RE.find(body) {
        Some(m) => &body[..m.start()],
        None => body,
    };
    YEAR_RE
        .find_iter(prose)
        .last()
        .map(|m| m.as_str().to_string())
}

fn render_full_entry(reference: &Reference, out: &mut String) {
    let id = sanitize_id(&reference.key);
    out.push_str(&format!("  {id}:\n"));
    if let Some(target) = extract_target(&reference.body) {
        out.push_str(&format!("    target: {}\n", yaml::quote(&target)));
    }
    let title = extract_title(&reference.body).unwrap_or_else(|| reference.body.trim().to_string());
    out.push_str(&format!("    title: {}\n", yaml::quote(&title)));
    if let Some(author) = extract_author(&reference.body) {
        out.push_str("    author:\n");
        out.push_str(&format!("      - name: {}\n", yaml::quote(&author)));
    }
    if let Some(date) = extract_date(&reference.body) {
        out.push_str(&format!("    date: {date}\n"));
    }
}

/// Renders a slice of references as a kramdown-rfc YAML block (the body
/// under `normative:` or `informative:`). RFC references are emitted as
/// bare keys so kramdown-rfc resolves them from its own bibxml database;
/// everything else is emitted as a full `target`/`title`/`author`/`date`
/// entry parsed from the citation text.
pub fn render_yaml_block(refs: &[Reference]) -> String {
    let mut out = String::new();
    for reference in refs {
        if let Some(caps) = RFC_KEY_RE.captures(&reference.key) {
            out.push_str(&format!("  RFC{}:\n", &caps[1]));
        } else {
            render_full_entry(reference, &mut out);
        }
    }
    out
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn splits_normative_and_informative_buckets() {
        let content = "\
# 18. References

## 18.1. Normative References

**[RFC 2119]** Bradner, S., \"Key words for use in RFCs,\" BCP 14, RFC 2119, March 1997. https://www.rfc-editor.org/rfc/rfc2119

## 18.2. Informative References

**[Akerlof 1970]** Akerlof, G.A., \"The Market for Lemons,\" QJE, 84(3):488-500, 1970.
";
        let refs = parse_str(content);
        assert_eq!(refs.normative.len(), 1);
        assert_eq!(refs.normative[0].key, "RFC 2119");
        assert_eq!(refs.informative.len(), 1);
        assert_eq!(refs.informative[0].key, "Akerlof 1970");
    }

    #[test]
    fn renders_rfc_as_bare_key() {
        let refs = vec![Reference {
            key: "RFC 2119".to_string(),
            body: String::new(),
        }];
        let yaml = render_yaml_block(&refs);
        assert_eq!(yaml, "  RFC2119:\n");
    }

    #[test]
    fn renders_informative_entry_with_parsed_fields() {
        let refs = vec![Reference {
            key: "Akerlof 1970".to_string(),
            body: "Akerlof, G.A., \"The Market for Lemons: Quality Uncertainty and the Market Mechanism,\" QJE, 84(3):488-500, 1970.".to_string(),
        }];
        let yaml = render_yaml_block(&refs);
        assert!(yaml.contains("  Akerlof1970:\n"));
        assert!(yaml.contains(
            "title: \"The Market for Lemons: Quality Uncertainty and the Market Mechanism,\"\n"
        ));
        assert!(yaml.contains("author:\n      - name: \"Akerlof, G.A.\"\n"));
        assert!(yaml.contains("date: 1970\n"));
    }

    #[test]
    fn extracts_target_url() {
        let refs = vec![Reference {
            key: "SemVer".to_string(),
            body: "Preston-Werner, T., \"Semantic Versioning 2.0.0.\" https://semver.org/"
                .to_string(),
        }];
        let yaml = render_yaml_block(&refs);
        assert!(yaml.contains("target: \"https://semver.org/\"\n"));
    }

    #[test]
    fn date_ignores_digits_embedded_in_the_url() {
        // The arXiv id (2603.05637) and the URL's own dated path both
        // contain four-digit runs; only the "2026" in the prose is the
        // publication year.
        let refs = vec![Reference {
            key: "MCP-Faults-2026".to_string(),
            body: "\"Real Faults in MCP Software: A Comprehensive Taxonomy,\" arXiv:2603.05637, 2026. https://arxiv.org/html/2603.05637v1".to_string(),
        }];
        let yaml = render_yaml_block(&refs);
        assert!(
            yaml.contains("date: 2026\n"),
            "expected date: 2026, got:\n{yaml}"
        );
    }
}
