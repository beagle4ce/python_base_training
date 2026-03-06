def showCollections() -> None:
    # 依次初始化常见集合类型，并打印一个基础调用结果。
    # 这样做是为了让脚本可以直接运行，同时保持每种类型只展示一种初始化和一个操作。
    print("=== Python 常见集合类型示例 ===")
    print()

    numberList: list[int] = [1, 2, 3]
    print("【list】")
    print("初始化: numberList = [1, 2, 3]")
    print(f"调用: numberList[0] -> {numberList[0]}")
    print()

    numberTuple: tuple[int, int, int] = (1, 2, 3)
    print("【tuple】")
    print("初始化: numberTuple = (1, 2, 3)")
    print(f"调用: numberTuple[0] -> {numberTuple[0]}")
    print()

    rangeValues: range = range(1, 4)
    print("【range】")
    print("初始化: rangeValues = range(1, 4)")
    print(f"调用: rangeValues[0] -> {rangeValues[0]}")
    print()

    textValue: str = "python"
    print("【str】")
    print('初始化: textValue = "python"')
    print(f"调用: textValue[0] -> {textValue[0]}")
    print()

    bytesValue: bytes = b"abc"
    print("【bytes】")
    print("初始化: bytesValue = b'abc'")
    print(f"调用: bytesValue[0] -> {bytesValue[0]}")
    print()

    byteArrayValue: bytearray = bytearray(b"abc")
    print("【bytearray】")
    print("初始化: byteArrayValue = bytearray(b'abc')")
    print(f"调用: byteArrayValue[0] -> {byteArrayValue[0]}")
    print()

    memoryViewValue: memoryview = memoryview(b"abc")
    print("【memoryview】")
    print("初始化: memoryViewValue = memoryview(b'abc')")
    print(f"调用: memoryViewValue[0] -> {memoryViewValue[0]}")
    print()

    numberSet: set[int] = {1, 2, 3}
    print("【set】")
    print("初始化: numberSet = {1, 2, 3}")
    print(f"调用: 2 in numberSet -> {2 in numberSet}")
    print()

    frozenNumberSet: frozenset[int] = frozenset({1, 2, 3})
    print("【frozenset】")
    print("初始化: frozenNumberSet = frozenset({1, 2, 3})")
    print(f"调用: 2 in frozenNumberSet -> {2 in frozenNumberSet}")
    print()

    userInfo: dict[str, str] = {"name": "Tom"}
    print("【dict】")
    print("初始化: userInfo = {'name': 'Tom'}")
    print(f"调用: userInfo['name'] -> {userInfo['name']}")


if __name__ == "__main__":
    showCollections()
