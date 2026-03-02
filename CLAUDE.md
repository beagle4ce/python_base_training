# CLAUDE.md

This file provides guidance to Claude  Code (claude.ai/code) when working with code in this repository.

## Project Overview

A Python training/practice project managed with `uv`. Requires Python 3.14+.

## Commands

```bash
# Run the main script
uv run python main.py

# Add a dependency
uv add <package>

# Run a Python file or script
uv run python <file.py>

# Run a single test (once tests are added)
uv run pytest tests/test_<name>.py::test_<function>

# Run all tests
uv run pytest
```

## Structure

- `main.py` — entry point, contains `main()`
- `pyproject.toml` — project metadata and dependencies (no deps currently)
- `uv.lock` — lockfile managed by `uv`
- `.python-version` — pins Python 3.14
