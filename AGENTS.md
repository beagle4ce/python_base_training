# Repository Guidelines

## Project Structure & Module Organization
- `main.py` is the lightweight entry point for quick runtime checks.
- `code/` stores small practice modules and algorithm exercises.
- `pyproject.toml` defines project metadata and the supported Python version (`>=3.14`).
- `uv.lock` pins dependency resolution for reproducible local runs.
- Add future tests under `tests/` and mirror source module names with `test_<module>.py`.

## Teaching Mission
- This repository exists to teach Python fundamentals to beginners, not to showcase production-grade architecture.
- Optimize every change for readability, directness, and progressive learning so learners can understand one concept at a time.
- Prefer examples that can be run immediately from the command line and observed through clear output.

## Teaching Scope & Difficulty Control
- Default teaching scope: variables, basic types, conditionals, loops, functions, strings, collections, file basics, and small algorithms.
- Keep each example focused on one concept or one closely related concept group; avoid mixing many new ideas into the same script.
- Unless the user explicitly asks for them, do not introduce advanced topics such as decorators, descriptors, metaclasses, async, concurrency, complex typing patterns, or framework-style architectures.
- If an advanced topic is explicitly requested, state that it is an advanced topic first, then give the smallest runnable example that explains the core idea.

## Teaching Acceptance Criteria
- Prefer standard-library-only examples and single-file demonstrations unless the lesson clearly benefits from multiple files.
- Choose the most beginner-friendly implementation when multiple correct approaches exist.
- Avoid unnecessary abstractions such as factory layers, plugin systems, generic frameworks, or class hierarchies when direct code is enough.
- When scripts print results, keep the output sectioned and teaching-friendly so learners can match code to runtime behavior.

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
├── code/
│   ├── basicType.py
│   ├── collections.py
│   ├── greeting.py
│   └── pop_sort.py
```

## Code File Notes
- `main.py`: minimal executable entry containing `main()`.
- `code/basicType.py`: runnable examples showing direct assignment for common Python basic value types with teaching-friendly sectioned output.
- `code/collections.py`: runnable examples showing initialization and one basic operation for common collection types with teaching-friendly sectioned output.
- `code/greeting.py`: list iteration and formatted output practice.
- `code/pop_sort.py`: abstract sort interface plus bubble sort and quick sort examples.
- `README.md`: currently empty, so rely on source files and this document for project guidance.

## Build, Test, and Development Commands
- `uv sync`: create or refresh the local environment from `pyproject.toml` and `uv.lock`.
- `uv run --active python main.py`: run the entry script.
- `uv run --active python code/basicType.py`: run basic type assignment examples.
- `uv run --active python code/collections.py`: run common collection examples.
- `uv run --active python code/greeting.py`: run greeting practice code.
- `uv run --active python code/pop_sort.py`: run sorting demos.

## Coding Style & Naming Conventions
- Use Python 3.14+ features and precise type annotations such as `list[int]` and `dict[str, int]`.
- Classes use `PascalCase`; functions and variables use `camelCase`; constants use `UPPER_SNAKE_CASE`.
- Add concise Chinese comments for classes, methods, and non-trivial algorithm blocks, explaining both what the code does and why the approach was chosen.
- Keep functions focused on a single behavior and avoid unnecessary abstractions in training examples.
- Prefer straightforward syntax over clever or highly reusable patterns in beginner-facing code.
- Preserve each file's existing indentation style when editing; do not reformat unrelated lines just to normalize spacing.

## Testing Guidelines
- Unless the user explicitly requests tests, do not add unit tests or expand test coverage.
- When the user explicitly requests testing work, prefer `pytest` via `uv run --active pytest`.
- For algorithm exercises, when tests are explicitly requested, prioritize edge cases such as empty input, duplicate values, already-sorted input, and reverse-sorted input.
- If the user explicitly requests a new test file, keep it narrow and directly tied to the requested change.

## Documentation Maintenance
- When project structure changes, update the file tree and the affected file notes in this document in the same change.
- Keep guidance here aligned with `CLAUDE.md` when repository-wide conventions change.
- Do not document speculative files, commands, or workflows that are not present in the repository yet.

## Commit & Pull Request Guidelines
- Existing history uses short, direct commit messages such as `init project` and `update code`.
- Prefer small, imperative commits; add scope when helpful, for example `sort: handle duplicate pivot values`.
- Summarize behavior changes clearly in pull requests and include the commands used for verification.
- Include before/after CLI output when runtime behavior changes materially.
