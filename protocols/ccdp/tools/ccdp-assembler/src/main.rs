mod assemble;
mod chapters;
mod cli;
mod frontmatter;
mod headers;
mod references;
mod toc;
mod validate;
mod yaml;

use std::fs;
use std::io;
use std::process::ExitCode;

use anyhow::{Context, Result};
use chrono::Local;
use clap::Parser;

use cli::{Args, Format};

fn main() -> ExitCode {
    let args = Args::parse();
    match run(&args) {
        Ok(warnings) if args.strict && warnings > 0 => ExitCode::from(1),
        Ok(_) => ExitCode::SUCCESS,
        Err(err) => {
            eprintln!("error: {err:#}");
            ExitCode::from(1)
        }
    }
}

/// Runs the assembler end to end. Returns the number of validation
/// warnings reported (`0` when `--validate` was not passed).
fn run(args: &Args) -> Result<usize> {
    if args.format == Format::KramdownRfc && !args.template.exists() {
        eprintln!(
            "error: template not found at {}; proceeding with built-in defaults",
            args.template.display()
        );
    }

    let loaded_chapters = chapters::load_chapters(&args.src_dir)
        .with_context(|| format!("failed to load chapters from {}", args.src_dir.display()))?;

    let references_path = args.src_dir.join("18-references.md");
    let refs = references::parse(&references_path)?;

    let date = match &args.date {
        Some(date) => date.clone(),
        None => Local::now().format("%Y-%m-%d").to_string(),
    };

    let document = match args.format {
        Format::KramdownRfc => {
            assemble::assemble_kramdown_rfc(&loaded_chapters, &refs, &args.version, &date)?
        }
        Format::Gfm => {
            assemble::assemble_gfm(&loaded_chapters, &args.version, &date, args.want_toc())?
        }
    };

    if let Some(parent) = args.output.parent().filter(|p| !p.as_os_str().is_empty()) {
        fs::create_dir_all(parent)
            .with_context(|| format!("failed to create output directory: {}", parent.display()))?;
    }
    // `--output /dev/stdout | head` closes the pipe once head has enough
    // lines; that's a clean downstream exit, not a failure (CLI-56).
    if let Err(err) = fs::write(&args.output, &document)
        && err.kind() != io::ErrorKind::BrokenPipe
    {
        return Err(err)
            .with_context(|| format!("failed to write output: {}", args.output.display()));
    }

    if args.validate {
        let warnings = validate::validate(&loaded_chapters, &refs);
        if warnings > 0 {
            eprintln!("validate: {warnings} warning(s) reported");
        }
        return Ok(warnings);
    }

    Ok(0)
}
