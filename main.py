def main():
    print("Hello from base-training!")


# 当该文件作为主程序直接运行时，__name__ 的值为 "__main__"；
# 若被其他模块 import 导入，__name__ 则为模块名，此块不会执行。
# 这样既能直接运行，又能被复用为模块而不产生副作用。
if __name__ == "__main__":
    main()
