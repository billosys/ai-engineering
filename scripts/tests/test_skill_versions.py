"""Regression fixtures for defects found during skill-version reconciliation."""
import importlib.machinery
import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile

SCRIPT = Path(__file__).resolve().parents[1] / 'check-skill-versions'
loader = importlib.machinery.SourceFileLoader('skill_versions', str(SCRIPT))
spec = importlib.util.spec_from_loader(loader.name, loader)
gate = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = gate
loader.exec_module(gate)


class VersionContract(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name)
        self.root = self.repo / 'knowledge/example'
        self.root.mkdir(parents=True)
        self.entry = self.root / 'SKILL.md'
        self.entry.write_text('---\nname: example\ndescription: Validate a skill fixture.\nmetadata:\n  version: 1.10.0\n---\n# Example\n')
        self.history = self.root / 'version-history.md'
        self.history.write_text('# History\n\n## Version 1.10.0 - 2026-09-06\n\nUpdated.\n\n## Version 1.9.0 - 2026-08-01\n\nEarlier.\n')

    def source(self):
        errors = []
        skills = gate.check_source(self.repo, errors)
        return skills, errors

    def package(self, edits=None):
        contents = {'example/SKILL.md': self.entry.read_text(), 'example/version-history.md': self.history.read_text()}
        for key, value in (edits or {}).items():
            if value is None:
                contents.pop(key, None)
            else:
                contents[key] = value
        archive = self.repo / 'example.zip'
        with zipfile.ZipFile(archive, 'w') as z:
            for key, value in contents.items():
                z.writestr(key, value)
        skills, errors = self.source()
        gate.check_package(archive, skills, self.repo, errors)
        return errors

    def test_source_and_package_accept_numeric_version_order(self):
        self.assertEqual(self.source()[1], [])
        self.assertEqual(self.package(), [])

    def test_reject_missing_top_level_duplicate_and_invalid_versions(self):
        values = [
            '', 'version: 1.10.0\n',
            'metadata:\n  version: 1.10.0\n  version: 1.10.0\n',
            'metadata:\n  version: 1.10\n',
            'metadata:\n  version: 01.10.0\n',
            'metadata:\n  version: 1.10.0-01\n',
            'version: 1.10.0\nmetadata:\n  version: 1.10.0\n',
            'metadata.version: 1.10.0\n',
            'metadata:\n  hermes:\n    version: 1.10.0\n',
            'metadata: {version: 1.10.0}\n',
            'metadata:\n  version: 1.10.0\nmetadata:\n  version: 1.10.0\n',
            'displayName: Example\nmetadata:\n  version: 1.10.0\n',
        ]
        for value in values:
            with self.subTest(value=value):
                self.entry.write_text('---\nname: example\n'+value+'---\n# Example\n')
                self.assertTrue(self.source()[1])

    def test_version_is_found_after_other_nested_metadata(self):
        self.entry.write_text('---\nname: example\nmetadata:\n  hermes:\n    category: tools\n  version: "1.10.0"\n  displayName: Example\n---\n')
        self.assertEqual(self.source()[1], [])

    def test_installed_skill_creator_accepts_metadata_and_rejects_top_level(self):
        validator = Path.home() / '.codex/skills/.system/skill-creator/scripts/quick_validate.py'
        if not validator.is_file():
            self.skipTest('Installed skill-creator validator is not available on this host')
        result = subprocess.run([sys.executable, str(validator), str(self.root)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.entry.write_text(self.entry.read_text().replace('metadata:\n  version:', 'version:'))
        result = subprocess.run([sys.executable, str(validator), str(self.root)], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Unexpected key(s)', result.stdout)

    def test_description_block_is_not_a_metadata_key(self):
        text = self.entry.read_text().replace('description: Validate a skill fixture.', 'description: |\n  version: examples are subject matter')
        self.entry.write_text(text)
        self.assertEqual(self.source()[1], [])

    def test_history_must_exist_and_match_current_once(self):
        for text in ['', '## Version 1.9.0\n', '## Version 1.10.0\n\n## Version 1.10.0\n',
                     '## Version 1.10.0\n\n## Version 1.11.0\n']:
            with self.subTest(text=text):
                self.history.write_text(text)
                self.assertTrue(self.source()[1])
        self.history.unlink()
        self.assertTrue(self.source()[1])

    def test_semver_prerelease_precedence(self):
        order = ['1.0.0-alpha', '1.0.0-alpha.1', '1.0.0-alpha.beta', '1.0.0-beta',
                 '1.0.0-beta.2', '1.0.0-beta.11', '1.0.0-rc.1', '1.0.0']
        self.assertEqual(sorted(reversed(order), key=gate.version_key), order)
        self.assertEqual(gate.version_key('2.14'), gate.version_key('2.14.0'))

    def test_old_and_current_labels_are_rejected_in_any_owned_directory(self):
        for directory in ['guides', 'templates', 'examples', 'concept-cards', 'support']:
            p = self.root / directory / 'note.md'
            p.parent.mkdir()
            for label in ['Current version: 1.10.0', '**Version**: 2.14',
                          'This wayfinder: 2.14', 'example v1.10.0',
                          'Current ledger-discipline\nprotocol version: 2.4']:
                with self.subTest(directory=directory, label=label):
                    p.write_text(label)
                    self.assertTrue(self.source()[1])
            p.unlink()

    def test_subject_matter_and_navigation_are_preserved(self):
        (self.root / 'guide.md').write_text('Rust 1.80 uses dependency version 1.10.0.\n\n```toml\nversion = "1.10.0"\n```\n\n## Version History\n\nSee [history](./version-history.md).\n')
        for name in ['history-api.md', 'history-of-undefined-and-null.md']:
            (self.root / name).write_text('Subject matter.\n### v4 Import Statement\n\n1. Consider snapshot testing\n2. Consider process testing\n')
        sources = self.root / 'sources'
        sources.mkdir()
        (sources / 'CHANGELOG.md').write_text('## Version 90.0.0\n')
        self.assertEqual(self.source()[1], [])

    def test_extra_history_and_versioned_filename_fail(self):
        for name in ['CHANGELOG.md', 'version-history-old.md', 'guide-v1.10.0.md']:
            p = self.root / name
            p.write_text('Old record.\n')
            self.assertTrue(self.source()[1])
            p.unlink()
        (self.root / 'guide.md').write_text('## Change History\n\n- 2026-09-06: Updated.\n')
        self.assertTrue(self.source()[1])

    def test_discover_unlisted_source_skill(self):
        p = self.repo / 'knowledge/new-skill/SKILL.md'
        p.parent.mkdir()
        p.write_text('---\nname: new-skill\nmetadata:\n  version: 1.0.0\n---\n')
        skills, errors = self.source()
        self.assertIn('new-skill', skills)
        self.assertTrue(any('missing sibling' in e for e in errors))

    def test_shared_history_sections_have_independent_versions(self):
        shared = self.repo / 'knowledge/biome'
        shared.mkdir()
        for name, version in [('biome-js-linter', '1.2.0'), ('biome-linter', '2.0.0')]:
            (shared / f'SKILL-{name}.md').write_text(f'---\nname: {name}\nmetadata:\n  version: {version}\n---\n')
        h = shared / 'version-history.md'
        h.write_text('## Skill: biome-js-linter\n\n### Version 1.2.0\n\nJS change.\n\n## Skill: biome-linter\n\n### Version 2.0.0\n\nWeb change.\n')
        self.assertEqual(self.source()[1], [])
        h.write_text(h.read_text().replace('### Version 1.2.0', '### Version 2.0.0'))
        self.assertTrue(self.source()[1])

    def test_package_rejects_stale_version_and_stale_history(self):
        self.assertTrue(self.package({'example/SKILL.md': self.entry.read_text().replace('1.10.0', '1.9.0')}))
        self.assertTrue(self.package({'example/version-history.md': self.history.read_text().replace('Updated.', 'Stale.')}))

    def test_package_rejects_misplaced_or_duplicate_history(self):
        self.assertTrue(self.package({'example/version-history.md': None, 'example/knowledge/example/version-history.md': self.history.read_text()}))
        self.assertTrue(self.package({'example/guides/version-history.md': self.history.read_text()}))

    def test_package_scans_guides_and_embedded_metadata(self):
        self.assertTrue(self.package({'example/guides/a.md': '**Version**: 1.10.0'}))
        self.assertTrue(self.package({'example/knowledge/example/ENTRYPOINT.md': self.entry.read_text()}))

    def test_package_requires_source_identity_and_handles_missing_source_history(self):
        self.assertTrue(self.package({'example/SKILL.md': self.entry.read_text().replace('name: example', 'name: unknown')}))
        self.history.unlink()
        archive = self.repo / 'example.zip'
        with zipfile.ZipFile(archive, 'w') as z:
            z.writestr('example/SKILL.md', self.entry.read_text())
            z.writestr('example/version-history.md', '## Version 1.10.0')
        skills, errors = self.source()
        gate.check_package(archive, skills, self.repo, errors)
        self.assertTrue(errors)

    def test_cli_returns_failure_for_noncompliant_source(self):
        self.history.unlink()
        result = subprocess.run([sys.executable, str(SCRIPT), '--repo', str(self.repo)],
                                capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('missing sibling', result.stderr)

    def test_staging_does_not_repair_duplicate_version_prose(self):
        self.entry.write_text(self.entry.read_text() + '\nCurrent version: 1.9.0\n')
        staged = self.repo / 'staged.md'
        subprocess.run([sys.executable, str(SCRIPT.parent / 'stage-skill-entrypoint'),
                        str(self.entry), str(staged), '--repo', str(self.repo)], check=True)
        self.assertIn('Current version: 1.9.0', staged.read_text())
        self.assertTrue(self.source()[1])


if __name__ == '__main__':
    unittest.main()
