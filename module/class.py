# 类的名称首字母大写
class Dog:
    """模拟小狗的类"""

    def __init__(self, name, age):
        """初始化属性"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗收到指令时蹲下"""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """模拟小狗收到指令时打滚"""
        print(f"{self.name} rolled over!")

# 创建类的实例，属性和方法都是public的
my_dog = Dog('Willie', 5)
my_dog.sit()
my_dog.roll_over()
print(my_dog.age)

# 继承
class BigDog(Dog):

    # 在父类基础上增加了weight属性
    def __init__(self, name, age, weight):
        super().__init__(name, age)
        self.weight = weight
    
    # 子类新增加的方法
    def display_weight(self):
        print(f"{self.name}'s weight is {self.weight}!")

    # 重写父类的方法
    def roll_over(self):
        print(f"{self.name} big big big rolled over!")

big_dog = BigDog('Boss', 8, 800)
big_dog.sit()
big_dog.roll_over()
big_dog.display_weight()
print(big_dog.age)
print(big_dog.weight)