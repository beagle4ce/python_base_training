# Repository Guidelines

## Project Structure & Module Organization
- `main.py` is the lightweight entry point for quick runtime checks.
- `code/` stores small practice modules and algorithm exercises.
- `pyproject.toml` defines project metadata and the supported Python version (`>=3.14`).
- `uv.lock` pins dependency resolution for reproducible local runs.
- Add future tests under `tests/` and mirror source module names with `test_<module>.py`.

## Current Code & File Layout (Filtered by `.gitignore`)
The snapshot below reflects the current tracked files. Keep this section in sync when files are added, removed, or renamed.

```text
.
├── .gitignore
├── .python-version
├── AGENTS.md
├── CLAUDE.md
├── LICENSE
├── README.md
├── main.py
├── pyproject.toml
├── uv.lock
└── code/
    ├── collections.py
    ├── greeting.py
    └── pop_sort.py
```

## Code File Notes
- `main.py`: minimal executable entry containing `main()`.
- `code/greeting.py`: list iteration and formatted output practice.
- `code/pop_sort.py`: abstract sort interface plus bubble sort and quick sort examples.
- `code/collections.py`: currently an empty placeholder for future collection exercises.
- `README.md`: currently empty, so rely on source files and this document for project guidance.

## Build, Test, and Development Commands
- `uv sync`: create or refresh the local environment from `pyproject.toml` and `uv.lock`.
- `uv run --active python main.py`: run the entry script.
- `uv run --active python code/greeting.py`: run greeting practice code.
- `uv run --active python code/pop_sort.py`: run sorting demos.
- `uv run --active pytest`: run the full test suite after tests are added.
- `uv run --active pytest tests/test_pop_sort.py::test_quick_sort`: run a single targeted test once the file exists.

## Coding Style & Naming Conventions
- Use Python 3.14+ features and precise type annotations such as `list[int]` and `dict[str, int]`.
- Classes use `PascalCase`; functions and variables use `camelCase`; constants use `UPPER_SNAKE_CASE`.
- Add concise Chinese comments for classes, methods, and non-trivial algorithm blocks, explaining both what the code does and why the approach was chosen.
- Keep functions focused on a single behavior and avoid unnecessary abstractions in training examples.
- Preserve each file's existing indentation style when editing; do not reformat unrelated lines just to normalize spacing.

## Testing Guidelines
- Use `pytest` via `uv run --active pytest` when the task explicitly includes testing work or when the repository already contains relevant tests.
- For algorithm exercises, prioritize edge cases such as empty input, duplicate values, already-sorted input, and reverse-sorted input.
- If you introduce the first test file in this repository, keep it narrow and directly tied to the change being made.

## Documentation Maintenance
- When project structure changes, update the file tree and the affected file notes in this document in the same change.
- Keep guidance here aligned with `CLAUDE.md` when repository-wide conventions change.
- Do not document speculative files, commands, or workflows that are not present in the repository yet.

## Commit & Pull Request Guidelines
- Existing history uses short, direct commit messages such as `init project` and `update code`.
- Prefer small, imperative commits; add scope when helpful, for example `sort: handle duplicate pivot values`.
- Summarize behavior changes clearly in pull requests and include the commands used for verification.
- Include before/after CLI output when runtime behavior changes materially.
