# Changelog

All notable changes to this project will be documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] — 2025-01-01

### Added
- Core regex-based validation engine (`src/validator.py`)
- CLI application with `argparse` (`src/cli.py`)
  - `--config` for custom config file
  - `--stdin` for git hook integration
  - `--json` for machine-readable output
  - `--verbose` for detailed breakdown
  - `--list-types` to display allowed commit types
- Git hook script (`hooks/commit-msg`) with user-friendly error output
- One-command hook installer (`install_hook.py`)
- JSON and YAML configuration support
- Logging to `logs/validator.log`
- 30+ unit tests with `pytest`
- GitHub Actions CI pipeline (lint + test matrix + end-to-end)
- Support for breaking change marker (`!`)
- Optional scope in commit messages `(scope)`
- `setup.py` and `pyproject.toml` for pip-installable package

### Supported commit types
`feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `perf`, `ci`, `build`

---

## [Unreleased]

### Planned
- Interactive commit message builder (step-by-step CLI wizard)
- VS Code extension
- GitHub App for PR status checks
- Pre-push hook to validate all commits in a branch
- Multi-line body and footer validation
