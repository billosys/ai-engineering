//! Front matter for the assembled document, in either output flavor.

use crate::references::{self, ReferenceSet};

/// Renders kramdown-rfc YAML front matter, opened by `---` but left
/// unterminated: kramdown-rfc treats the `--- abstract` section marker that
/// follows as both the YAML close and the abstract section's start (see the
/// template).
pub fn render_kramdown_rfc(version: &str, date: &str, refs: &ReferenceSet) -> String {
    format!(
        "---\n\
         title: \"Composite Cognition Dispatch Protocol\"\n\
         abbrev: \"CCDP\"\n\
         cat: std\n\
         docname: ccdp-spec-v{version}\n\
         date: {date}\n\
         area: \"Cognitive Architecture\"\n\
         workgroup: \"Composite Cognition\"\n\
         \n\
         author:\n\
         \x20 - ins: D. Guthrie\n\
         \x20   name: Duncan McGreggor\n\
         \x20   email: oubiwann@gmail.com\n\
         \n\
         normative:\n\
         {normative}\
         \n\
         informative:\n\
         {informative}",
        normative = references::render_yaml_block(&refs.normative),
        informative = references::render_yaml_block(&refs.informative),
    )
}

/// Renders minimal GFM-compatible front matter: a self-terminated `---`
/// block simple enough for GitHub's front matter parser to render as a
/// metadata table (or hide) rather than dumping as body text. The full
/// reference bibliography stays in Section 18 as body content — no
/// `normative`/`informative` YAML blocks here.
pub fn render_gfm(version: &str, date: &str) -> String {
    format!(
        "---\n\
         title: \"CCDP: Composite Cognition Dispatch Protocol\"\n\
         description: >\n\
         \x20 A message-envelope protocol for routing cognitive requests through a\n\
         \x20 deliberately simple dispatcher to heterogeneous cognitive services under\n\
         \x20 human supervision.\n\
         version: \"{version}\"\n\
         date: {date}\n\
         author: Duncan McGreggor\n\
         status: Draft Specification\n\
         ---\n"
    )
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::references::Reference;

    #[test]
    fn renders_well_formed_kramdown_rfc_front_matter() {
        let refs = ReferenceSet {
            normative: vec![Reference {
                key: "RFC 2119".to_string(),
                body: String::new(),
            }],
            informative: vec![Reference {
                key: "Akerlof 1970".to_string(),
                body: "Akerlof, G.A., \"The Market for Lemons,\" QJE, 1970.".to_string(),
            }],
        };
        let out = render_kramdown_rfc("0.1", "2026-08-03", &refs);
        assert!(out.starts_with("---\n"));
        assert!(out.contains("docname: ccdp-spec-v0.1\n"));
        assert!(out.contains("date: 2026-08-03\n"));
        assert!(out.contains("email: oubiwann@gmail.com\n"));
        assert!(out.contains("normative:\n  RFC2119:\n"));
        assert!(out.contains("informative:\n  Akerlof1970:\n"));
    }

    #[test]
    fn renders_well_formed_gfm_front_matter() {
        let out = render_gfm("0.1", "2026-08-03");
        assert!(out.starts_with("---\n"));
        assert!(out.trim_end().ends_with("---"));
        assert!(out.contains("version: \"0.1\"\n"));
        assert!(out.contains("date: 2026-08-03\n"));
        assert!(out.contains("author: Duncan McGreggor\n"));
        // GFM front matter carries no reference bibliography.
        assert!(!out.contains("normative:"));
        assert!(!out.contains("informative:"));
    }
}
