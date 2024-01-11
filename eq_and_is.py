# '==' 操作符比较对象之间的值是否相等
# 'is' 判断两个变量是否指向同一个内存地址，即它们是否是同一个对象

# 每个对象的身份标识都能通过函数 id(object) 获得

a = 10
b = 10
print(a == b)  # True
print(a is b)  # True

print(id(a))  # 140716025498328
print(id(b))  # 140716025498328


# 对于整型数字来说，以上 a is b 为True的结论，只试用于 -5 到 256 范围内的数字

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return (self.name == other.name and
                self.age == other.age)


emp1 = Employee("Jacky", 30)
emp2 = Employee("Jacky", 30)

print(emp1 == emp2)  # True
print(emp1 is emp2)  # False

# 如果不定制__eq__方法，默认 '==' 的行为跟 'is' 一样
