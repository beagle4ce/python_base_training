# CLAUDE.md

This file provides guidance to Claude  Code (claude.ai/code) when working with code in this repository.

## Project Overview

A Python training/practice project managed with `uv`. Requires Python 3.14+.

The primary goal of this repository is to teach Python fundamentals to beginners. Favor clarity, small runnable examples, and gradual concept building over completeness or production-style abstraction.

## Teaching Response Contract

When generating teaching-oriented content for this repository, use this order unless the user explicitly asks for something else:

1. 用简短中文说明“这段内容做了什么”。
2. 用简短中文说明“为什么这样写”。
3. 给出最小可运行示例。
4. 给出预期输出或运行结果。
5. 补充少量关键知识点或常见误区。

Additional rules:

- 默认面向 Python 初学者，优先帮助学习者理解语法与运行结果。
- 术语可以保留英文原名，但要配上简短中文说明。
- 一次请求如果涉及多个知识点，按由浅入深顺序展开，不要把多个新概念混在一段解释里。

## Teaching Guardrails

- 默认使用标准库，不主动引入第三方依赖，除非用户明确要求。
- 默认选择最直接、最容易解释的写法，不为了展示技巧而引入额外抽象。
- 除非用户明确要求，否则不要主动扩展到 decorators、descriptors、metaclasses、async / concurrency、复杂 typing、框架式工程结构等进阶主题。
- 如果用户明确要求进阶主题，先说明它属于进阶内容，再给最小可运行示例，不扩展成大型工程实现。
- 如果一个需求既能用简单函数实现，也能用复杂封装实现，默认选择更容易教学的简单版本。

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
这条仓库规则优先于通用工作流建议；TDD、流程技能或一般工程习惯都不能作为绕开它的理由。
在用户没有明确要求测试时，如需验证行为，优先直接运行脚本或示例，不创建 `tests/` 目录、测试文件或仅为测试新增的文档项。

类型注解必须精确，使用泛型形式而非裸类型：

- 用 `list[int]` 而非 `list`
- 用 `dict[str, int]` 而非 `dict`
- 用 `tuple[int, str]` 而非 `tuple`
- 若元素类型不确定，使用 `list[Any]` 并从 `typing` 导入 `Any`

默认采用 Pythonic 风格编写代码，但保留本仓库现有命名规则：类使用 `PascalCase`，方法和变量使用 `camelCase`，常量使用 `UPPER_SNAKE_CASE`。

优先选择符合 Python 习惯且便于初学者理解的写法，例如：

- 直接迭代而不是在索引无意义时手动 `for i in range(...)`
- `if items:` 而不是仅为判断是否为空而写 `if len(items) > 0:`
- `with open(...) as file:` 而不是手动 `open()` 后再 `close()`
- 标准库和内置能力优先，不为简单逻辑增加多余样板或包装层

Pythonic 不等于炫技。只有在更清晰时才使用推导式、解包等简洁写法，不要为了写得短而牺牲初学者可读性。

## Naming Conventions

命名规则：

- 下面的命名约定是本仓库的固定约束，优先于通用的 Python `snake_case` 惯例
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
├── basicType.py      — 基础类型赋值示例
├── collections.py    — 常见集合类型示例
├── greeting.py       — 列表遍历与字符串输出练习
└── pop_sort.py       — 排序算法练习
```
