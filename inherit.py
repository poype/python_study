# 在Python中，object是一个内置的基类，所有的内置类型和用户定义的类都是它的子类。object类定义了所有对象的基本行为，例如创建对象、比较对象等。
# 当创建一个新的类时，如果没有明确指定该类的基类，那么这个类会自动继承自object。这意味着几乎所有的Python类都是object的子类。
#
# object类包含了一些特殊的方法和属性，例如：
# __init__()：在创建新对象时调用，用于初始化对象的状态。
# __str__()：返回对象的字符串表示形式。
# __repr__()：返回对象的详细字符串表示形式，通常与__str__()方法返回的结果相同。
# __eq__()：比较两个对象是否相等。
# __ne__()：比较两个对象是否不相等。
# __lt__()、__le__()、__gt__()、__ge__()：比较两个对象的大小关系。
# __call__()：允许对象被调用，即可以用obj()的方式来调用对象。
# __setattr__()、__getattr__()等：控制对象的属性的访问和修改。

# 在Python中，有几种类型的类不是object的子类，主要是以下几种：
#
# 元类：元类是创建类的类。它们通常用于修改类的创建过程。例如，type就是Python的一个内置元类。
# 内置类型：Python有一些内置类型，如整数、浮点数、字符串等，它们也是类，但不是object的子类。例如，int、float和str等。
# 其他特殊类型：还有其他一些特殊类型的类，如tuple、list、dict等，它们也不是object的子类。

# 在Python中，私有变量并不是真正的私有，因为Python并没有提供真正的私有变量机制。然而，可以通过一些约定来模拟私有变量的行为。
# 一种常见的约定是在变量名前面加上两个下划线（__），表示该变量是私有的。这种约定并不是强制性的，但被广泛接受并用于指导开发者的行为。
#
# 例如，以下是一个类，其中包含一个私有变量：
# class MyClass:
#     def __init__(self):
#         self.__private_var = 42
# 
# 在这个例子中，__private_var是一个私有变量，因为它前面有两个下划线。尽管如此，仍然可以通过实例的_MyClass__private_var属性来访问它。

# _xxx: 单下划线开始的成员变量叫保护变量，意思是只有类对象和子类对象能访问这些变量

class Base1:
    def __init__(self):
        print("Base1")


class Base2:
    def __init__(self):
        print("Base2")


# super().__init__() 只能调用第一个父类的构造函数
class Derived(Base1, Base2):
    def __init__(self):
        super(Derived, self).__init__()  # 这行代码只能调用Base1类的构造方法
        Base2.__init__(self)  # 为了调用其它父类的构造函数，只能明确调用
        print("Derived")

        self.__var = "test private var"  # 两个下划线开头定义的是私有变量

    def print_private_var(self):  # 类内部的方法可以访问私有变量
        print(self.__var)

    @staticmethod
    def test_static_method():
        print("test_static_method")


d = Derived()
# print(d.__var)  __var是私有变量, 只能由类内的函数访问
# 私有变量的原理其实是__var变量被解释器改名了，__var变量的真正名字是 _Derived__var,通过_Derived__var这个名字也可以在类外直接访问该变量

d.print_private_var()  # test private var

print("------------------------------")
Derived.print_private_var(d)  # 也可以像下面这样通过类调用对象的方法，但要传一个对象实例作为参数

print("----------------调用一个类的静态方法--------------")
Derived.test_static_method()
