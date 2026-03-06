# CLAUDE.md

This file provides guidance to Claude  Code (claude.ai/code) when working with code in this repository.

## Project Overview

A Python training/practice project managed with `uv`. Requires Python 3.14+.

## Commands

```bash
# Run the main script
uv run --active python main.py

# Add a dependency
uv add <package>

# Run a Python file or script
uv run --active python <file.py>

# Run a single test (once tests are added)
uv run --active pytest tests/test_<name>.py::test_<function>

# Run all tests
uv run --active pytest
```

## Code Style

生成的代码中，所有类、方法和关键算法部分必须添加中文注释，注释需说明：

1. **做了什么** — 描述该段代码的行为
2. **为什么这样做** — 解释设计意图或技术原因

除非明确要求，否则默认不生成单元测试代码。

类型注解必须精确，使用泛型形式而非裸类型：

- 用 `list[int]` 而非 `list`
- 用 `dict[str, int]` 而非 `dict`
- 用 `tuple[int, str]` 而非 `tuple`
- 若元素类型不确定，使用 `list[Any]` 并从 `typing` 导入 `Any`

## Naming Conventions

命名规则：

- **类、方法、变量名** — 使用驼峰命名法（camelCase / PascalCase）
- **常量、枚举值** — 使用全大写字母加下划线分隔（UPPER_SNAKE_CASE）

```python
# 类名：PascalCase（大驼峰）
class SortAlgorithm:
    pass

# 方法名、变量名：camelCase（小驼峰）
def bubbleSort(arr: list[int]) -> list[int]:
    sortedResult = []
    return sortedResult

# 常量：UPPER_SNAKE_CASE
MAX_RETRY_COUNT = 3
DEFAULT_TIMEOUT = 30

# 枚举值：UPPER_SNAKE_CASE
from enum import Enum

class Color(Enum):
    BRIGHT_RED = 1
    DARK_BLUE = 2
```

## Structure

- `main.py` — entry point, contains `main()`
- `pyproject.toml` — project metadata and dependencies (no deps currently)
- `uv.lock` — lockfile managed by `uv`
- `.python-version` — pins Python 3.14

### code/ 目录

```
code/
└── pop_sort.py       — 排序算法练习
```
