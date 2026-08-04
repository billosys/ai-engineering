use std::path::PathBuf;

use clap::{Parser, ValueEnum};

/// Output flavor for the assembled document.
#[derive(Debug, Clone, Copy, PartialEq, Eq, ValueEnum)]
pub enum Format {
    /// GitHub-Flavored Markdown: simple front matter, `<a id="...">` anchors,
    /// no kramdown-rfc section markers. Renders cleanly on GitHub.
    Gfm,
    /// kramdown-rfc-flavored markdown: full YAML reference blocks, `{#anchor}`
    /// IAL anchors, `--- abstract` / `--- middle` / `--- back` markers. Feed
    /// this to `kramdown-rfc` to produce RFC XML/HTML.
    KramdownRfc,
}

/// Assembles the CCDP chapter sources into a single document.
#[derive(Debug, Parser)]
#[command(name = "ccdp-assembler", version, about)]
pub struct Args {
    /// Chapter source directory.
    #[arg(short = 's', long = "src-dir", default_value = "protocols/ccdp/src")]
    pub src_dir: PathBuf,

    /// kramdown-rfc template, used as structural reference (--format kramdown-rfc only).
    #[arg(
        short = 't',
        long = "template",
        default_value = "protocols/ccdp/templates/draft-rfcxml-general-template-standard-00.xml-edited.md"
    )]
    pub template: PathBuf,

    /// Output path for the assembled document.
    #[arg(
        short = 'o',
        long = "output",
        default_value = "protocols/ccdp/composite-cognition-dispatch-protocol.md"
    )]
    pub output: PathBuf,

    /// Spec version string, used in the front matter.
    #[arg(short = 'v', long = "version", default_value = "0.1")]
    pub version: String,

    /// Publication date (YYYY-MM-DD). Defaults to today.
    #[arg(long = "date")]
    pub date: Option<String>,

    /// Output format.
    #[arg(long = "format", value_enum, default_value_t = Format::Gfm)]
    pub format: Format,

    /// Emit a Table of Contents after the front matter (--format gfm only; on by default).
    #[arg(long = "toc", action = clap::ArgAction::SetTrue)]
    pub toc: bool,

    /// Suppress the Table of Contents.
    #[arg(long = "no-toc", action = clap::ArgAction::SetTrue, conflicts_with = "toc")]
    pub no_toc: bool,

    /// Run cross-reference validation after assembly.
    #[arg(long = "validate")]
    pub validate: bool,

    /// Exit non-zero if validation reports any warnings.
    #[arg(long = "strict")]
    pub strict: bool,
}

impl Args {
    /// Whether the Table of Contents should be emitted (GFM only; on by default).
    pub fn want_toc(&self) -> bool {
        !self.no_toc
    }
}
