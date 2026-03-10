from typing import Protocol


# Animal 协议：定义“会说话的对象”需要提供的 speak 方法。
# 这里使用 Protocol，是为了演示 Python 的鸭子类型接口：
# 不要求类显式继承 Animal，只要方法形状一致，就可以按 Animal 使用。
class Animal(Protocol):
    def speak(self) -> str:
        ...


# Dog 类：没有继承 Animal，但实现了 speak 方法。
# 这正是鸭子类型的关键点：关注“有没有这个方法”，而不是“是不是这个父类”。
class Dog:
    def speak(self) -> str:
        return "wang"


# Cat 类：同样没有继承 Animal，但也实现了 speak 方法。
# 因为方法签名一致，所以它也可以被当成 Animal 使用。
class Cat:
    def speak(self) -> str:
        return "miao"


# 统一调用函数：参数类型写成 Animal，表示这里只关心对象能否提供 speak 方法。
# 这样 Dog 和 Cat 都可以传进来，体现 Protocol 的接口约束作用。
def makeAnimalSpeak(animal: Animal) -> None:
    print(animal.speak())


if __name__ == "__main__":
    print("=== Protocol 鸭子类型示例 ===")
    print()

    dog: Dog = Dog()
    cat: Cat = Cat()

    print("【Dog】")
    makeAnimalSpeak(dog)
    print()

    print("【Cat】")
    makeAnimalSpeak(cat)
    print()

    print("说明: Dog 和 Cat 虽然没有继承 Animal，但因为都实现了 speak()，所以都能按 Animal 使用。")
