"""Exercise destination selection and the Make installer in temporary directories."""

import os
from pathlib import Path
import pty
import subprocess
import tempfile
import unittest
import zipfile


REPO = Path(__file__).resolve().parents[1]
RESOLVER = REPO / "scripts" / "resolve-skill-install-dir"


class SkillInstallTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="skill install ")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.zip_temp = tempfile.TemporaryDirectory(prefix="skill-install-zips-")
        self.addCleanup(self.zip_temp.cleanup)
        self.zips = Path(self.zip_temp.name)
        self.env = os.environ.copy()
        self.env.pop("CODEX_HOME", None)
        self.env.pop("INSTALL_DIR", None)
        self.env.pop("MAKEFLAGS", None)
        self.env.pop("MAKELEVEL", None)
        self.env["HOME"] = str(self.root)
        self.default = self.root / ".agents" / "skills"

    def run_command(self, command, terminal_input=None):
        if terminal_input is None:
            return subprocess.run(command, cwd=REPO, env=self.env,
                                  stdin=subprocess.DEVNULL, capture_output=True,
                                  text=True, timeout=20)
        master, slave = pty.openpty()
        try:
            process = subprocess.Popen(command, cwd=REPO, env=self.env, stdin=slave,
                                       stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                       text=True)
            try:
                os.write(master, terminal_input.encode())
                stdout, stderr = process.communicate(timeout=20)
            finally:
                if process.poll() is None:
                    process.kill()
                    process.wait()
            return subprocess.CompletedProcess(command, process.returncode, stdout, stderr)
        finally:
            os.close(master)
            os.close(slave)

    def resolve(self, origin="file", destination=None, terminal_input=None):
        return self.run_command(["bash", str(RESOLVER),
                                 str(self.default if destination is None else destination),
                                 origin], terminal_input)

    def test_existing_default_is_preserved(self):
        self.default.mkdir(parents=True)
        self.env["CODEX_HOME"] = str(self.root / "other profile")
        result = self.resolve()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), str(self.default))
        self.assertEqual(result.stderr, "")

    def test_existing_default_symlink_is_preserved(self):
        target = self.root / "codex" / "skills"
        target.mkdir(parents=True)
        self.default.parent.mkdir()
        self.default.symlink_to(target)
        result = self.resolve()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), str(self.default))
        self.assertEqual(result.stderr, "")

    def test_explicit_missing_destination_skips_prompt(self):
        for origin in ("environment", "command line"):
            with self.subTest(origin=origin):
                result = self.resolve(origin)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(result.stdout.strip(), str(self.default))
                self.assertEqual(result.stderr, "")

    def test_empty_override_fails(self):
        result = self.resolve("environment", destination="")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("must not be empty", result.stderr)

    def test_missing_default_requires_explicit_noninteractive_choice(self):
        self.env["CODEX_HOME"] = str(self.root / "profile home")
        result = self.resolve()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("INSTALL_DIR=", result.stderr)
        self.assertIn("profile\\ home/skills", result.stderr)
        self.assertFalse(self.default.exists())

    def test_dangling_symlink_is_diagnosed_and_preserved(self):
        self.default.parent.mkdir()
        self.default.symlink_to(self.root / "missing codex" / "skills")
        result = self.resolve()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("dangling symlink", result.stderr)
        self.assertIn("/path/to/profile/skills", result.stderr)
        self.assertTrue(self.default.is_symlink())

    def test_interactive_profile_suggestion(self):
        self.env["CODEX_HOME"] = str(self.root / "profile home")
        result = self.resolve(terminal_input="\n")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), str(self.root / "profile home" / "skills"))

    def test_interactive_fresh_standard_install(self):
        result = self.resolve(terminal_input="\n")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), str(self.default))

    def test_interactive_custom_path_and_cancel(self):
        result = self.resolve(terminal_input="~/custom skills\n")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), str(self.root / "custom skills"))
        result = self.resolve(terminal_input="cancel\n")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")

    def install(self, destination=None, terminal_input=None, archive=None):
        if archive is None:
            archive = self.zips / "example.zip"
            with zipfile.ZipFile(archive, "w") as bundle:
                bundle.writestr("example/SKILL.md", "fresh skill bytes\n")
        # Supply a fixture archive and skip rebuilding all real packages in the
        # recursive invocation; selection and installation use the real Makefile.
        command = ["make", "--no-print-directory", "-j4", "install",
                   "MAKE=make --no-print-directory -o all",
                   f"INSTALL_ZIPS={archive}", "INSTALL_SKILLS=example"]
        if destination is not None:
            command.append(f"INSTALL_DIR={destination}")
        return self.run_command(command, terminal_input)

    def assert_installed(self, destination):
        self.assertEqual((destination / "example" / "SKILL.md").read_text(),
                         "fresh skill bytes\n")

    def test_make_environment_override_creates_path_with_spaces(self):
        destination = self.root / "explicit profile" / "skills"
        self.env["INSTALL_DIR"] = str(destination)
        result = self.install()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assert_installed(destination)

    def test_make_command_override_replaces_only_owned_skill(self):
        destination = self.root / "explicit profile" / "skills"
        (destination / "example").mkdir(parents=True)
        (destination / "example" / "stale").write_text("old")
        (destination / "unrelated").write_text("keep")
        self.env["INSTALL_DIR"] = str(self.root / "ignored environment")
        result = self.install(destination)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assert_installed(destination)
        self.assertFalse((destination / "example" / "stale").exists())
        self.assertEqual((destination / "unrelated").read_text(), "keep")
        self.assertFalse((self.root / "ignored environment").exists())

    def test_make_interactive_redirect_preserves_broken_default(self):
        self.default.parent.mkdir()
        self.default.symlink_to(self.root / "missing codex" / "skills")
        profile = self.root / "active profile"
        self.env["CODEX_HOME"] = str(profile)
        result = self.install(terminal_input="\n")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assert_installed(profile / "skills")
        self.assertTrue(self.default.is_symlink())

    def test_make_noninteractive_failure_preserves_profile_contents(self):
        profile = self.root / "active profile"
        (profile / "skills" / "example").mkdir(parents=True)
        marker = profile / "skills" / "example" / "original"
        marker.write_text("keep")
        self.env["CODEX_HOME"] = str(profile)
        result = self.install()
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(marker.read_text(), "keep")
        self.assertFalse(self.default.exists())

    def test_make_invalid_archive_preserves_installed_skill(self):
        destination = self.root / "profile skills"
        (destination / "example").mkdir(parents=True)
        marker = destination / "example" / "original"
        marker.write_text("keep")
        archive = self.zips / "invalid.zip"
        archive.write_text("invalid archive")
        result = self.install(destination, archive=archive)
        self.assertNotEqual(result.returncode, 0)
        self.assertNotIn(">> installed skills", result.stdout)
        self.assertEqual(marker.read_text(), "keep")

    def test_make_missing_archive_preserves_installed_skill(self):
        destination = self.root / "profile skills"
        (destination / "example").mkdir(parents=True)
        marker = destination / "example" / "original"
        marker.write_text("keep")
        result = self.run_command([
            "make", "-o", "all", "_install-skills", f"INSTALL_DIR={destination}",
            f"INSTALL_ZIPS={self.zips / 'missing.zip'}", "INSTALL_SKILLS=example"])
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("missing zip", result.stderr)
        self.assertEqual(marker.read_text(), "keep")

    def test_make_build_failure_preserves_installed_skill(self):
        destination = self.root / "profile skills"
        (destination / "example").mkdir(parents=True)
        marker = destination / "example" / "original"
        marker.write_text("keep")
        failure = self.root / "failure.mk"
        failure.write_text("all: fail-build\n.PHONY: fail-build\nfail-build:\n\t@false\n")
        result = self.run_command([
            "make", "-j4", "-f", "Makefile", "-f", str(failure),
            "-o", "skills", "-o", "collab-framework", "_install-skills",
            f"INSTALL_DIR={destination}", "INSTALL_SKILLS=example"])
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(marker.read_text(), "keep")


if __name__ == "__main__":
    unittest.main()
