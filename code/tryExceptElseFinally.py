#
# 这个文件演示 try / except / else / finally 的基本执行顺序。
# 它的用途是帮助初学者直接观察：代码先进入 try，出错时会走 except，
# 没有异常时会走 else，而 finally 不管有没有异常都会执行。
#
# 这里特意写成“同一个函数调用两次”：
# 第一次传入 2，展示成功路径 try -> else -> finally；
# 第二次传入 0，展示异常路径 try -> except -> finally。
# 这样写比只演示一种情况更直观，也能让初学者在同一个脚本里对比两条执行路线。
#
# 例子里固定使用 10 // divisor，是为了把注意力集中在异常流程本身，
# 避免引入多余概念，让学习者更容易把终端输出和各个代码块对应起来。
#
def showExecutionOrder(divisor: int) -> None:
    print(f"当前除数: {divisor}")

    try:
        print("1. 进入 try")
        # 固定使用 10 // divisor，初学者更容易看出“哪一行成功了”或“哪一行抛出异常”。
        result: int = 10 // divisor
        print(f"2. try 中计算成功，结果: {result}")
    except ZeroDivisionError:
        print("2. 进入 except")
        print("3. 捕获到 ZeroDivisionError")
    else:
        print("3. 进入 else")
    finally:
        print("4. 进入 finally")


def showTryExceptElseFinallyDemo() -> None:
    print("=== try / except / else / finally 示例 ===")
    print()

    print("【成功场景】")
    showExecutionOrder(2)
    print()

    print("【异常场景】")
    showExecutionOrder(0)
    print()

    print("说明:")
    print("1. try 先执行")
    print("2. except 只在出错时执行")
    print("3. else 只在没有异常时执行")
    print("4. finally 无论是否出错都会执行")


if __name__ == "__main__":
    showTryExceptElseFinallyDemo()
