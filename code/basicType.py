def showBasicTypes() -> None:
    # 依次展示常见基础类型的赋值方式，并打印当前变量值。
    # 这样做是为了让初学者先看清“变量 = 值”的最基本写法，避免被额外逻辑分散注意力。
    print("=== Python 常见基础类型示例 ===")
    print()

    age: int = 18
    print("【int】")
    print("赋值: age = 18")
    print(f"结果: age -> {age}")
    print()

    score: float = 95.5
    print("【float】")
    print("赋值: score = 95.5")
    print(f"结果: score -> {score}")
    print()

    complexNumber: complex = 3 + 4j
    print("【complex】")
    print("赋值: complexNumber = 3 + 4j")
    print(f"结果: complexNumber -> {complexNumber}")
    print()

    isReady: bool = True
    print("【bool】")
    print("赋值: isReady = True")
    print(f"结果: isReady -> {isReady}")
    print()

    message: str = "Hello Python"
    print("【str】")
    print('赋值: message = "Hello Python"')
    print(f"结果: message -> {message}")
    print()

    emptyValue: None = None
    print("【None】")
    print("赋值: emptyValue = None")
    print(f"结果: emptyValue -> {emptyValue}")


if __name__ == "__main__":
    showBasicTypes()
