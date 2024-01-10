# 魔术方法前后都由两个下划线包围：__XXX__

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 相当于Java中的toString方法，
    # 如果不定制__str__，则会打印对象的内存地址，类似 <__main__.Student object at 0x000002C8CBB07980>
    def __str__(self):
        return f"名字：{self.name}，年龄：{self.age}"

    # 相当于Java中的equals方法
    # 如果不定制__eq__，“==”默认检查的是两个对象的内存地址是否相同，即两个不同对象的比较结果一定是False
    def __eq__(self, other):
        return (self.name == other.name and
                self.age == other.age)


stu1 = Student("Jacky", 32)
print(stu1)

stu2 = Student("Jacky", 32)
print(stu1 == stu2)

