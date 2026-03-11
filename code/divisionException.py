def divideNumbers(divisor: int) -> int:
    # 这里使用整数除法，是为了把注意力集中在“除数为 0 会触发异常”这一件事上。
    # 固定写成 10 // divisor，初学者更容易看出是哪一行抛出了 ZeroDivisionError。
    return 10 // divisor


def divideWithoutHandling() -> None:
    print("当前层: 调用 divideNumbers(0)，这里不写 except。")
    divideNumbers(0)


def divideAndReraise() -> None:
    try:
        print("当前层: 调用 divideNumbers(0)，先观察异常。")
        divideNumbers(0)
    except ZeroDivisionError:
        # 当前层只补充说明，不真正解决问题，然后把原始异常继续交给上层。
        print("当前层: 已经捕获到 ZeroDivisionError，但这里不处理，继续向上抛出。")
        raise


def showAutoPropagation() -> None:
    print("【场景 1：异常自动向上抛出】")
    try:
        divideWithoutHandling()
    except ZeroDivisionError:
        print("上层: 捕获到 ZeroDivisionError，说明异常已经从下层传播到了这里。")
    print()


def showReraisePropagation() -> None:
    print("【场景 2：捕获后继续抛出】")
    try:
        divideAndReraise()
    except ZeroDivisionError:
        print("上层: 再次捕获到 ZeroDivisionError，说明 raise 把原始异常继续交给了上层。")
    print()


def showDivisionExceptionDemo() -> None:
    print("=== 整数除法异常示例 ===")
    print()

    showAutoPropagation()
    showReraisePropagation()

    print("说明: 如果当前层不处理异常，可以不写 except，或者在 except 里使用 raise 继续向上抛。")


if __name__ == "__main__":
    showDivisionExceptionDemo()
