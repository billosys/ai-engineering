//! kramdown-rfc YAML front matter for the CCDP specification.

use crate::references::{self, ReferenceSet};

/// Renders the YAML front matter, opened by `---` but left unterminated:
/// kramdown-rfc treats the `--- abstract` section marker that follows as
/// both the YAML close and the abstract section's start (see the template).
pub fn render(version: &str, date: &str, refs: &ReferenceSet) -> String {
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

#[cfg(test)]
mod tests {
    use super::*;
    use crate::references::Reference;

    #[test]
    fn renders_well_formed_front_matter() {
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
        let out = render("0.1", "2026-08-03", &refs);
        assert!(out.starts_with("---\n"));
        assert!(out.contains("docname: ccdp-spec-v0.1\n"));
        assert!(out.contains("date: 2026-08-03\n"));
        assert!(out.contains("email: oubiwann@gmail.com\n"));
        assert!(out.contains("normative:\n  RFC2119:\n"));
        assert!(out.contains("informative:\n  Akerlof1970:\n"));
    }
}
