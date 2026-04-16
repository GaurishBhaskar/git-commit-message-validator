# 🔍 Git Commit Message Validator

> A production-ready Python tool that enforces the [Conventional Commits](https://www.conventionalcommits.org/) standard in your Git workflow — with a CLI, Git hook integration, GitHub Actions CI, and full test coverage.

[![CI](https://github.com/yourusername/git-commit-message-validator/actions/workflows/ci.yml/badge.svg)](https://github.com/yourusername/git-commit-message-validator/actions)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-orange)](https://conventionalcommits.org)

---

## 📖 Overview

Poorly written commit messages make code history unreadable. This tool enforces a consistent, meaningful commit format that makes `git log` useful again — across your whole team, automatically.

It validates every commit message against the **Conventional Commits 1.0.0** standard:

```
<type>[(scope)][!]: <subject>
```

---

## ✨ Features

| Feature | Description |
|---|---|
| 🧠 Regex Validation Engine | Strict, configurable pattern matching |
| 💻 CLI Tool | Validate messages from the terminal |
| 🪝 Git Hook | Auto-blocks bad commits before they happen |
| ⚙️ Config Support | Custom types via JSON or YAML |
| 🧪 Full Test Suite | pytest with 30+ test cases |
| 🤖 GitHub Actions CI | Lint + test pipeline on push/PR |
| 📋 Logging | Validation attempts logged to file |
| 🔄 JSON Output | Machine-readable output for scripting |

---

## 📁 Project Structure

```
git-commit-message-validator/
├── src/
│   ├── __init__.py         # Package exports
│   ├── validator.py        # Core validation engine
│   └── cli.py              # CLI application (argparse)
├── tests/
│   ├── __init__.py
│   └── test_validator.py   # 30+ pytest test cases
├── hooks/
│   └── commit-msg          # Git hook script
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions CI pipeline
├── logs/                   # Auto-created, validation logs
├── config.json             # Default configuration
├── install_hook.py         # One-command hook installer
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/git-commit-message-validator.git
cd git-commit-message-validator
```

### 2. Set up a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate      # macOS/Linux
.venv\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install the Git hook (optional but recommended)

```bash
python install_hook.py
```

---

## 💻 Usage

## ✅ Valid vs ❌ Invalid Examples

| Message | Result | Reason |
|---|---|---|
| `feat: add login authentication` | ✅ Valid | Correct format |
| `fix(auth): resolve JWT expiry bug` | ✅ Valid | With scope |
| `feat!: remove deprecated API` | ✅ Valid | Breaking change |
| `feat(api)!: change response format` | ✅ Valid | Scope + breaking |
| `updated file` | ❌ Invalid | No type or colon |
| `bug fixed` | ❌ Invalid | No type or colon |
| `login changes` | ❌ Invalid | No type or colon |
| `update: fix something` | ❌ Invalid | `update` is not a valid type |
| `feat -add feature` | ❌ Invalid | Wrong separator |

---

## 📋 Supported Commit Types

| Type | Description |
|---|---|
| `feat` | A new feature |
| `fix` | A bug fix |
| `docs` | Documentation changes |
| `style` | Formatting, missing semicolons, etc. |
| `refactor` | Code change that's neither a fix nor feature |
| `test` | Adding or updating tests |
| `chore` | Maintenance tasks, dependency updates |
| `perf` | Performance improvements |
| `ci` | CI/CD configuration changes |
| `build` | Build system or external dependency changes |

---

## 🔮 Future Scope

- [ ] **Interactive mode** — step-by-step commit message builder
- [ ] **VS Code Extension** — inline validation while typing
- [ ] **GitHub App** — PR status checks for commit messages
- [ ] **Multi-line body/footer** validation
- [ ] **Pre-push hook** — validate all commits in a branch
- [ ] **Team analytics** — commit quality dashboard
- [ ] **Auto-fix suggestions** — suggest corrected messages

---

## 🤝 Contributing


1. Fork the repository
2. Create a feature branch: `git checkout -b feat/your-feature`
3. Make your changes with proper commit messages (the hook will enforce it!)
4. Add or update tests in `tests/`
5. Run `pytest tests/ -v` to confirm everything passes
6. Push and open a pull request


---


