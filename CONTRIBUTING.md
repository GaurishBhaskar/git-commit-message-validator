# Contributing Guide

Thank you for considering a contribution! Here's how to get involved.

---

## Getting Started

1. **Fork** the repository on GitHub
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/your-fork/git-commit-message-validator.git
   cd git-commit-message-validator
   ```
3. **Create a virtual environment** and install dev dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -e ".[dev,yaml]"
   ```
4. **Install the git hook** (so your own commits are validated!):
   ```bash
   python install_hook.py
   ```

---

## Making Changes

- Create a feature branch: `git checkout -b feat/your-feature`
- Write clean, modular Python code
- Add or update tests in `tests/test_validator.py`
- Run the test suite before committing:
  ```bash
  pytest tests/ -v --cov=src
  ```
- Run the linter:
  ```bash
  black src/ tests/
  flake8 src/ tests/
  ```

---

## Commit Message Format

This project enforces Conventional Commits (naturally). Your commits must follow:

```
<type>[(scope)][!]: <subject>
```

Examples:
```
feat: add step-by-step commit wizard
fix(cli): handle missing config file gracefully
docs: add contributing guide
test: cover custom YAML config loading
```

---

## Pull Request Checklist

Before opening a PR, confirm:

- [ ] All existing tests pass (`pytest tests/ -v`)
- [ ] New tests cover your changes
- [ ] Code is formatted with `black`
- [ ] `flake8` reports no issues
- [ ] Commit messages follow Conventional Commits
- [ ] `CHANGELOG.md` updated under `[Unreleased]`

---

## Reporting Bugs

Open an issue with:
- A clear description of the problem
- The commit message that caused unexpected behavior
- The Python version you're using (`python --version`)
- Steps to reproduce

---

## Feature Requests

Open an issue tagged `enhancement` with:
- What you'd like to see
- Why it would be useful
- Any relevant examples

---

Thanks again — every contribution helps make Git history more readable for everyone.
