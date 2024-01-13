# metaclass 能够拦截 Python 类的定义

# 第一，所有用户定义的类，都是 type 这个类的实例。 类本身不过是一个名为 type 类的实例

class MyClass:
    pass


instance = MyClass()
print(type(instance))  # <class '__main__.MyClass'>
print(type(MyClass))  # <class 'type'>  MyClass类 是 type类的一个对象

a = 100
print(type(a))  # <class 'int'>  python中一切都是对象

# 第二，用户自定义类，只不过是 type 类的__call__运算符重载。
# 当我们定义一个类的语句结束时，真正发生的情况，是 Python 调用 type 的__call__运算符。
# class MyClass2:
#     data = 1

# 针对上面这个类定义， Python 真正执行的是下面这段代码：
# class = type(classname, superclasses, attributedict)

# 下面代码相当于定义了类 MyClass2
MyClass2 = type("MyClass2", (), {"data": 99})
instance2 = MyClass2()
print(f"instance2: {type(instance2)}, {instance2.data}")  # instance2: <class '__main__.MyClass2'>, 99
print(f"MyClass2: {type(MyClass2)}")  # MyClass2: <class 'type'>


print("-------------------------------------------------")


# 第三，metaclass 是 type 的子类，通过替换 type 的__call__运算符重载机制，“超越变形”正常的类。
# 一旦你把一个类型 MyClass 的 metaclass 设置成 MyMeta，MyClass 就不再由原生的 type 创建，而是会调用 MyMeta 的__call__运算符重载。
# 相当于下面的变化：
# class = type(classname, superclasses, attributedict)
# 变为了
# class = MyMeta(classname, superclasses, attributedict)


class MyMeta(type):
    def __init__(self, cls, name, bases):
        super().__init__(cls, name, bases)
        print("MyMeta")  # 这行代码会在定义MyClass3类之后打印


# 定义一个MyClass3的类就相当于 构造了一个MyMeta类的实例，所以可以通过MyMeta类的__init__方法感知类的创建
class MyClass3(metaclass=MyMeta):
    def __init__(self):
        print("MyClass3")
