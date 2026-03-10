def showWithDemo() -> None:
    # 用 with 分别完成写入和读取，帮助初学者只关注“代码块结束后文件会自动关闭”这一件事。
    # 先写再读可以让脚本单独运行就看到完整结果，不需要依赖额外的已有文件。
    filePath: str = "code/withDemo.txt"

    print("=== with 基础示例 ===")
    print()

    print("【写入文件】")
    print(f"文件路径: {filePath}")
    # 这里的 with 是语法糖，核心目的是“先打开文件，执行代码块，最后自动关闭文件”。
    # 它大致等效于下面这段流程：
    #
    # file = open(filePath, "w", encoding="utf-8")
    # try:
    #     file.write("第一行：Hello Python\n")
    #     file.write("第二行：with 会帮我们自动关闭文件\n")
    # finally:
    #     file.close()
    with open(filePath, "w", encoding="utf-8") as file:
        file.write("第一行：Hello Python\n")
        file.write("第二行：with 会帮我们自动关闭文件\n")
    print("写入完成")
    print()

    print("【读取文件】")
    # 读取时也是同样的思路：
    #
    # file = open(filePath, "r", encoding="utf-8")
    # try:
    #     content = file.read()
    # finally:
    #     file.close()
    with open(filePath, "r", encoding="utf-8") as file:
        content: str = file.read()
    print("读取结果:")
    print(content, end="")
    print()
    print("说明: 离开 with 代码块后，文件会自动关闭。")


if __name__ == "__main__":
    showWithDemo()
