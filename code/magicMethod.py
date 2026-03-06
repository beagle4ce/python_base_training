# 演示常见魔术方法的调用顺序，帮助初学者理解对象从创建到使用的过程。
class SampleClazzA:

  # __new__ 负责先创建实例，这里显式返回父类创建的对象，便于观察“先创建、后初始化”的流程。
  def __new__(cls) -> SampleClazzA:
    print("SampleClazzA Created")
    return super().__new__(cls)

  # __init__ 负责初始化已经创建好的实例，这里打印提示是为了直观看到它在 __new__ 之后执行。
  def __init__(self) -> None:
    print("SampleClazzA Initialized")

  # __str__ 决定 print(对象) 时显示的文本，返回固定字符串可以让输出结果更容易理解。
  def __str__(self) -> str:
    return "SampleClazzA"
  
  # 普通实例方法用来对比魔术方法和日常方法的调用方式，方便初学者观察区别。
  def myMethod(self) -> None:
    print("myMethod Called")


# 直接运行文件时，依次演示创建对象、打印对象和调用实例方法的输出。
if __name__ == "__main__":
  sampleCA: SampleClazzA = SampleClazzA()
  print(sampleCA)
  sampleCA.myMethod()
