//! Discovery and loading of numbered chapter source files.

use std::fs;
use std::path::{Path, PathBuf};
use std::sync::LazyLock;

use anyhow::{Context, Result};
use regex::Regex;

static CHAPTER_FILENAME_RE: LazyLock<Regex> =
    LazyLock::new(|| Regex::new(r"^(\d{2})-([a-z0-9-]+)\.md$").expect("static regex is valid"));

/// A single loaded chapter: its number, source path, and raw content.
#[derive(Debug, Clone)]
pub struct Chapter {
    pub number: u32,
    pub path: PathBuf,
    pub content: String,
}

/// Discovers and loads every `NN-slug.md` chapter file in `src_dir`.
///
/// Files that don't match the `NN-slug.md` convention are skipped with a
/// warning to stderr, except `README.md`, which is expected to sit
/// alongside the chapters and is skipped silently. Chapters are returned
/// sorted by number.
pub fn load_chapters(src_dir: &Path) -> Result<Vec<Chapter>> {
    let entries = fs::read_dir(src_dir).with_context(|| {
        format!(
            "failed to read chapter source directory: {}",
            src_dir.display()
        )
    })?;

    let mut chapters = Vec::new();
    for entry in entries {
        let entry = entry
            .with_context(|| format!("failed to read directory entry in {}", src_dir.display()))?;
        let path = entry.path();
        if !path.is_file() {
            continue;
        }
        let Some(file_name) = path.file_name().and_then(|n| n.to_str()) else {
            continue;
        };
        if file_name.eq_ignore_ascii_case("README.md") {
            continue;
        }
        let Some(caps) = CHAPTER_FILENAME_RE.captures(file_name) else {
            eprintln!(
                "warning: {}: chapter filename does not match 'NN-slug.md', skipping",
                path.display()
            );
            continue;
        };
        let number: u32 = caps[1].parse().expect("regex guarantees two digits");
        let content = fs::read_to_string(&path)
            .with_context(|| format!("failed to read chapter: {}", path.display()))?;
        chapters.push(Chapter {
            number,
            path,
            content,
        });
    }

    chapters.sort_by_key(|c| c.number);
    Ok(chapters)
}

/// Finds the loaded chapter with the given number, if any.
pub fn find(chapters: &[Chapter], number: u32) -> Option<&Chapter> {
    chapters.iter().find(|c| c.number == number)
}

/// Filters chapters to the inclusive `[start, end]` number range, in order.
pub fn in_range(chapters: &[Chapter], start: u32, end: u32) -> Vec<&Chapter> {
    chapters
        .iter()
        .filter(|c| c.number >= start && c.number <= end)
        .collect()
}
