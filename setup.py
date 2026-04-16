"""
Setup configuration for git-commit-message-validator.
Installs the package and registers the `commit-validator` CLI command.
"""

from setuptools import setup, find_packages
from pathlib import Path

long_description = (Path(__file__).parent / "README.md").read_text(encoding="utf-8")

setup(
    name="git-commit-message-validator",
    version="1.0.0",
    author="Your Name",
    author_email="you@example.com",
    description="Validate git commit messages against the Conventional Commits standard.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/git-commit-message-validator",
    packages=find_packages(exclude=["tests*"]),
    python_requires=">=3.9",
    install_requires=[],
    extras_require={
        "yaml": ["PyYAML>=6.0"],
        "dev": ["pytest>=7.4", "pytest-cov>=4.1", "flake8>=6.0", "black>=23.0"],
    },
    entry_points={
        "console_scripts": [
            "commit-validator=src.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Version Control :: Git",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    keywords="git commit conventional-commits linter hook cli",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/git-commit-message-validator/issues",
        "Source": "https://github.com/yourusername/git-commit-message-validator",
    },
)
