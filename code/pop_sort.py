# ASort 抽象类：定义排序算法的统一接口。
# 使用抽象基类强制所有排序子类实现指定方法，确保接口一致性，便于后续扩展更多排序算法。
from abc import ABC, abstractmethod
import random


class ASort(ABC):

    # 冒泡排序抽象方法：子类必须实现此方法以提供具体的冒泡排序逻辑。
    # 定义为抽象方法是为了在接口层面约束所有排序实现类都具备该能力。
    @abstractmethod
    def bubbleSort(self, arr: list[int]) -> list[int]:
        pass

    # 快速排序抽象方法：子类必须实现此方法以提供具体的快速排序逻辑。
    @abstractmethod
    def quickSort(self, arr: list[int]) -> list[int]:
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

    # 快速排序方法：采用分治策略，选取基准元素（pivot）将数组划分为两部分，递归排序后合并。
    # 选择快速排序是因为其平均时间复杂度为 O(n log n)，在大多数场景下性能优于冒泡排序；
    # 此处使用列表推导式实现分区，代码简洁直观，适合学习分治思想。
    def quickSort(self, arr: list[int]) -> list[int]:
        # 递归终止条件：当列表长度 <= 1 时，无需排序，直接返回。
        if len(arr) <= 1:
            return arr

        # 选取最后一个元素作为基准值（pivot）。
        # 选择末尾元素是为了实现简洁；在实际工程中可用随机选取或三数取中法优化最坏情况。
        pivot: int = arr[-1]

        # 将小于基准的元素收集到左分区。
        left: list[int] = [x for x in arr[:-1] if x <= pivot]
        # 将大于基准的元素收集到右分区。
        right: list[int] = [x for x in arr[:-1] if x > pivot]

        # 递归排序左右分区，再与基准值拼接，得到完整的有序列表。
        return self.quickSort(left) + [pivot] + self.quickSort(right)


if __name__ == "__main__":
    # 随机生成 10 个 1-100 之间的整数作为测试数据。
    data = [random.randint(1, 100) for _ in range(10)]
    print("排序前:", data)
    sorter = CustomSort()

    bubbleResult = sorter.bubbleSort(data[:])
    print("冒泡排序后:", bubbleResult)

    quickResult = sorter.quickSort(data[:])
    print("快速排序后:", quickResult)
