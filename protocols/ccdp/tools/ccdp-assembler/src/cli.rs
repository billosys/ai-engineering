use std::path::PathBuf;

use clap::Parser;

/// Assembles the CCDP chapter sources into a single kramdown-rfc document.
#[derive(Debug, Parser)]
#[command(name = "ccdp-assembler", version, about)]
pub struct Args {
    /// Chapter source directory.
    #[arg(short = 's', long = "src-dir", default_value = "protocols/ccdp/src")]
    pub src_dir: PathBuf,

    /// kramdown-rfc template, used as structural reference.
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

    /// Spec version string, used in the YAML `docname` field.
    #[arg(short = 'v', long = "version", default_value = "0.1")]
    pub version: String,

    /// Publication date (YYYY-MM-DD). Defaults to today.
    #[arg(long = "date")]
    pub date: Option<String>,

    /// Run cross-reference validation after assembly.
    #[arg(long = "validate")]
    pub validate: bool,

    /// Exit non-zero if validation reports any warnings.
    #[arg(long = "strict")]
    pub strict: bool,
}
