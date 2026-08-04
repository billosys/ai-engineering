//! Minimal YAML string quoting for hand-emitted front matter.

/// Wraps a string in double quotes, escaping backslashes and quotes.
///
/// This is sufficient for the plain prose (titles, author names) that
/// populates the CCDP front matter; it is not a general-purpose YAML
/// encoder.
pub fn quote(s: &str) -> String {
    let escaped = s.replace('\\', "\\\\").replace('"', "\\\"");
    format!("\"{escaped}\"")
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn quotes_plain_strings() {
        assert_eq!(quote("hello"), "\"hello\"");
    }

    #[test]
    fn escapes_embedded_quotes() {
        assert_eq!(quote("say \"hi\""), "\"say \\\"hi\\\"\"");
    }

    #[test]
    fn escapes_backslashes() {
        assert_eq!(quote(r"a\b"), "\"a\\\\b\"");
    }
}
