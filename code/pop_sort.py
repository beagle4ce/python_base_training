# ASort 抽象类：定义排序算法的统一接口。
# 使用抽象基类强制所有排序子类实现指定方法，确保接口一致性，便于后续扩展更多排序算法。
from abc import ABC, abstractmethod


class ASort(ABC):

    # 冒泡排序抽象方法：子类必须实现此方法以提供具体的冒泡排序逻辑。
    # 定义为抽象方法是为了在接口层面约束所有排序实现类都具备该能力。
    @abstractmethod
    def bubbleSort(self, arr: list[int]) -> list[int]:
        pass


# CustomSort 类：继承 ASort 抽象类，提供具体的排序算法实现。
# 通过继承抽象基类，确保本类遵循统一的排序接口规范，便于多态调用和后续扩展。
class CustomSort(ASort):

    # 冒泡排序方法：通过反复比较相邻元素并交换位置，将列表从小到大原地排序。
    # 选择冒泡排序是因为其逻辑直观，适合练习基础排序思想；
    # 每轮外循环结束后，当前最大值已"冒泡"到末尾，故内循环范围逐轮缩小以避免无效比较。
    def bubbleSort(self, arr: list[int]) -> list[int]:
        # 使用类型注解 n: int 显式声明变量类型，虽然 Python 解释器能自动推断 len() 返回 int，
        # 但显式标注可提高代码可读性，让阅读者一眼确认 n 的类型，也便于静态类型检查工具（如 mypy）校验。
        n: int = len(arr)
        for i in range(n):
            # 每轮结束后，最大值已沉底，无需再比较已排序部分
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr


if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("排序前:", data)
    sorter = CustomSort()
    result = sorter.bubbleSort(data)
    print("排序后:", result)
