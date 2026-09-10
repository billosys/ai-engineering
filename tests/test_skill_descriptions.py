"""Exercise the real parser and CLI against temporary files and a real PTY."""

import copy
import json
import os
from pathlib import Path
import pty
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import skill_descriptions as skills


class SkillDescriptionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()

    def skill(self, scalar='"A detailed description for testing edits."', name="example", extra="", newline="\n"):
        path = self.root / name / "SKILL.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes((f"---\nname: {name}\ndescription: {scalar}\n{extra}---\n# Body\nKeep body bytes.\n").replace("\n", newline).encode())
        return path

    def proposal(self, *paths):
        return {"schema_version": 1, "target_chars": 30, "changes": [
            {"path": str(path), "name": skills.parse_skill(path).name,
             "sha256": skills.digest(path.read_bytes()), "before": skills.parse_skill(path).description,
             "after": "Test description edits.", "rationale": "Keeps the task trigger."}
            for path in paths]}

    def run_cli(self, *args, terminal_input=None):
        command = [sys.executable, str(Path(skills.__file__)), *map(str, args)]
        if terminal_input is None:
            return subprocess.run(command, stdin=subprocess.DEVNULL, capture_output=True, text=True, timeout=10)
        master, slave = pty.openpty()
        try:
            process = subprocess.Popen(command, stdin=slave, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            try:
                os.write(master, terminal_input.encode())
                stdout, stderr = process.communicate(timeout=10)
            finally:
                if process.poll() is None:
                    process.kill()
                    process.wait()
            return subprocess.CompletedProcess(command, process.returncode, stdout, stderr)
        finally:
            os.close(master)
            os.close(slave)

    def write_proposal(self, proposal):
        path = self.root / "proposal.json"
        path.write_text(json.dumps(proposal), encoding="utf-8")
        return path

    def test_yaml_scalars_normalize_to_same_description(self):
        for scalar in ['"First second."', "'First second.'", "First second.",
                       "|\n  First\n  second.", ">-\n  First\n  second.",
                       '"First\\nsecond."', "First\n  second."]:
            with self.subTest(scalar=scalar):
                self.assertEqual(skills.parse_skill(self.skill(scalar)).description, "First second.")

    def test_quotes_comments_and_unicode_counts(self):
        path = self.skill('"caf\\u00e9: \\"quote\\"" # excluded')
        row = skills.inventory([path], 300)["skills"][0]
        self.assertEqual(row["description"], 'caf\u00e9: "quote"')
        self.assertEqual(row["chars"], 13)
        self.assertEqual(row["utf8_bytes"], 14)

    def test_missing_empty_duplicate_and_invalid_metadata_fail(self):
        invalid = [b"name: a\n", b"---\nname: a\ndescription: text\n",
                   b"---\nname: a\ndescription: ''\n---\n",
                   b"---\nname: a\ndescription: 42\n---\n",
                   b"---\nname: a\ndescription: one\ndescription: two\n---\n",
                   b"---\nname: a\ndescription: bad: scalar\n---\n"]
        for raw in invalid:
            with self.subTest(raw=raw), self.assertRaises((skills.SkillError, skills.yaml.YAMLError)):
                skills.parse_skill(self.root / "SKILL.md", raw)

    def test_policy_boundary_and_catalog_total(self):
        path = self.skill(json.dumps("x" * 1023))
        self.assertEqual(self.run_cli("audit", path, "--max-chars", 1023, "--json").returncode, 0)
        self.skill(json.dumps("x" * 1024))
        result = self.run_cli("audit", path, "--max-chars", 1023, "--json")
        self.assertEqual(result.returncode, 1)
        self.assertTrue(json.loads(result.stdout)["policy_failures"])
        result = self.run_cli("audit", path, "--max-total-chars", 1000, "--json")
        self.assertEqual(result.returncode, 1)

    def test_discovery_follows_links_without_cycles_and_keeps_distinct_duplicates(self):
        first = self.skill(name="first")
        second = self.root / ".system" / "second" / "SKILL.md"
        second.parent.mkdir(parents=True)
        second.write_bytes(first.read_bytes())
        (self.root / "alias").symlink_to(first.parent, target_is_directory=True)
        (first.parent / "loop").symlink_to(self.root, target_is_directory=True)
        report = skills.inventory([self.root, first], 300)
        self.assertEqual(report["count"], 2)
        self.assertEqual(len(report["duplicate_names"]["first"]), 2)

    def test_source_variants_discovered_and_generated_trees_excluded(self):
        path = self.skill()
        path.rename(path.with_name("SKILL-js-linter.md"))
        generated = self.root / "build" / "SKILL.md"
        generated.parent.mkdir()
        generated.write_text("invalid", encoding="utf-8")
        self.assertEqual(len(skills.discover([self.root])), 1)
        self.assertEqual(skills.discover([generated]), [generated])

    def test_metadata_fields_are_reported_separately(self):
        path = self.skill(extra="metadata:\n  short-description: Frontmatter short\n")
        interface = path.parent / "agents" / "openai.yaml"
        interface.parent.mkdir()
        interface.write_text("interface:\n  short_description: UI short\npolicy:\n  allow_implicit_invocation: false\n")
        row = skills.record(skills.parse_skill(path), 300)
        self.assertEqual(row["frontmatter_short_description"], "Frontmatter short")
        self.assertEqual(row["ui_short_description"], "UI short")
        self.assertFalse(row["allow_implicit_invocation"])

    def test_replacement_preserves_other_bytes_and_modes(self):
        for scalar in ['"A long description for testing." # keep comment',
                       "|- # retained header\n  A long description\n  for testing."]:
            for newline in ("\n", "\r\n"):
                with self.subTest(scalar=scalar, newline=newline):
                    path = self.skill(scalar, extra='# Keep this comment\nmetadata:\n  version: "1.2.3"\n', newline=newline)
                    path.chmod(0o640)
                    original = skills.parse_skill(path)
                    updated = skills.replacement(original, 'Test "edits": safely.')
                    if "retained header" in scalar:
                        self.assertIn(b"# retained header", updated)
                    self.assertIn(('# Keep this comment\nmetadata:\n  version: "1.2.3"'.replace("\n", newline)).encode(), updated)
                    skills.apply_one(original, updated)
                    self.assertEqual(skills.parse_skill(path).body, original.body)
                    self.assertEqual(path.stat().st_mode & 0o777, 0o640)
                    self.assertFalse(list(path.parent.glob(".skill-description-*")))

    def test_alias_that_would_change_other_field_is_rejected(self):
        path = self.skill('&desc "A long description for testing."', extra="other: *desc\n")
        with self.assertRaises((skills.SkillError, skills.yaml.YAMLError)):
            skills.replacement(skills.parse_skill(path), "Short.")

    def test_stale_source_and_late_change_rejected(self):
        path = self.skill()
        proposal = self.proposal(path)
        before = skills.parse_skill(path)
        path.write_bytes(path.read_bytes() + b"New body\n")
        with self.assertRaisesRegex(skills.SkillError, "stale"):
            skills.validate_proposal(proposal, self.root)
        with self.assertRaisesRegex(skills.SkillError, "changed during review"):
            skills.apply_one(before, skills.replacement(before, "Short."))

    def test_metadata_version_change_invalidates_proposal(self):
        path = self.skill(extra='metadata:\n  version: "1.2.3"\n')
        proposal = self.proposal(path)
        path.write_bytes(path.read_bytes().replace(b'"1.2.3"', b'"1.2.4"'))
        self.assertEqual(skills.parse_skill(path).description, proposal["changes"][0]["before"])
        with self.assertRaisesRegex(skills.SkillError, "stale"):
            skills.validate_proposal(proposal, self.root)

    def test_outside_root_and_duplicate_proposals_rejected(self):
        path = self.skill()
        proposal = self.proposal(path)
        with self.assertRaisesRegex(skills.SkillError, "outside"):
            skills.validate_proposal(proposal, self.root / "another-root")
        proposal["changes"] *= 2
        with self.assertRaisesRegex(skills.SkillError, "duplicate"):
            skills.validate_proposal(proposal, self.root)

    def test_invalid_candidates_rejected_and_null_is_unresolved(self):
        path = self.skill()
        original = self.proposal(path)
        for after in ["", "same " * 10, "a" * 31, "two\nlines", 42]:
            proposal = copy.deepcopy(original)
            proposal["changes"][0]["after"] = after
            with self.subTest(after=after), self.assertRaises(skills.SkillError):
                skills.validate_proposal(proposal, self.root)
        original["changes"][0]["after"] = None
        self.assertEqual(skills.validate_proposal(original, self.root), [])

    def test_prepare_and_review_are_read_only_and_outputs_do_not_overwrite(self):
        path = self.skill()
        before = path.read_bytes()
        output = self.root / "draft"
        result = self.run_cli("prepare", path, "--target-chars", 30, "--output-dir", output)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIsNone(json.loads((output / "proposal.json").read_text())["changes"][0]["after"])
        self.assertTrue((output / "prompt.md").is_file())
        again = self.run_cli("prepare", path, "--target-chars", 30, "--output-dir", output)
        self.assertEqual(again.returncode, 1)
        proposal = self.write_proposal(self.proposal(path))
        result = self.run_cli("review", proposal, "--root", self.root)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("0 applied", result.stdout)
        self.assertEqual(path.read_bytes(), before)

    def test_apply_rejects_noninteractive_input(self):
        path = self.skill()
        original = path.read_bytes()
        result = self.run_cli("review", self.write_proposal(self.proposal(path)), "--root", self.root, "--apply")
        self.assertEqual(result.returncode, 1)
        self.assertIn("interactive terminal", result.stderr)
        self.assertEqual(path.read_bytes(), original)

    def test_real_terminal_approval_applies_only_selected_file(self):
        first, second = self.skill(name="first"), self.skill(name="second")
        original = first.read_bytes()
        proposal = self.write_proposal(self.proposal(first, second))
        result = self.run_cli("review", proposal, "--root", self.root, "--apply", terminal_input="n\ny\n")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("1 applied", result.stdout)
        self.assertEqual(first.read_bytes(), original)
        self.assertEqual(skills.parse_skill(second).description, "Test description edits.")

    def test_quit_and_default_no_leave_files_unchanged(self):
        first, second = self.skill(name="first"), self.skill(name="second")
        originals = [p.read_bytes() for p in (first, second)]
        proposal = self.write_proposal(self.proposal(first, second))
        result = self.run_cli("review", proposal, "--root", self.root, "--apply", terminal_input="\nq\n")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual([p.read_bytes() for p in (first, second)], originals)

    def test_all_candidates_validated_before_any_write(self):
        first, second = self.skill(name="first"), self.skill(name="second")
        original = first.read_bytes()
        proposal = self.proposal(first, second)
        proposal["changes"][1]["after"] = "x" * 100
        result = self.run_cli("review", self.write_proposal(proposal), "--root", self.root, "--apply", terminal_input="y\n")
        self.assertEqual(result.returncode, 1)
        self.assertEqual(first.read_bytes(), original)


if __name__ == "__main__":
    unittest.main()
