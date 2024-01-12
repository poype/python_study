# Python中的装饰器就类似Sprint中的切面，或者是Java中的动态代理
import time
import functools

# 在 Python 中，函数是一等公民（first-class citizen），函数也是对象。
# 1. 可以把函数赋予变量
def func(message):
    print(f'Got a message: {message}')


send_message = func
send_message('hello world')  # Got a message: hello world, 相当于直接调用 func 方法


# 2. 可以把函数当作参数，传入另一个函数中
def receive_message(message):
    return 'Got a message: ' + message


def caller(func, message):  # 接收一个函数作为参数
    print(func(message))


caller(receive_message, 'hello world2')  # Got a message: hello world2, 将receive_message函数作为参数传给caller函数


# 3. 可以在函数里定义函数，也就是函数的嵌套
def outer_func(message):
    def inner_func(msg):
        print(f'Inner func receive message: {msg}')

    return inner_func(message)


outer_func("test inner method")  # Inner func receive message: test inner method


# 4. 函数的返回值也可以是函数对象（闭包）
def func_closure():
    num = 100

    def inner_func(message):
        print(f'Got a message: {message} {num}')

    return inner_func


test_closure = func_closure()
test_closure('test closure')  # Got a message: test closure 100


# --------------------装饰器开始--------------------
def decorator1(target_func):
    def wrapper():
        print('before target')
        target_func()  # 装饰器模式，在target方法的前后增加额外的功能
        print('after target')

    return wrapper


def test1():
    print('test decorator 111')


test1 = decorator1(test1)
test1()


# before target
# test decorator 111
# after target

# greet = decorator1(greet) 这种写法有点麻烦，可以利用注解形式实现相同效果
# 下面使用注解就相当于 test2 = decorator1(test2)
@decorator1
def test2():
    print("test decorator 222")


test2()


# before target
# test decorator 222
# after target


# 装饰器接收方法参数
def decorator2(target_func):
    def wrapper(*args, **kwargs):
        print(f"args: {args}")  # args: (100, '一百', False)  当使用 test3(100, "一百", False) 方式调用时args有值
        for key in kwargs:
            # 当使用 test3(int_value=200, str_value="二百", bool_value=False) 调用时args是空的，kwargs字典存储了每个参数的名字和值
            # key: int_value, value:200
            # key: str_value, value:二百
            # key: bool_value, value:False
            print(f"key: {key}, value:{kwargs[key]}")
        print('before target')
        target_func(*args, **kwargs)  # 将args 和 kwargs两个参数传给目标方法
        print('after target')

    return wrapper


@decorator2
def test3(int_value, str_value, bool_value):
    print(f"test decorator 333, {int_value}, {str_value}, {bool_value}")


test3(100, "一百", False)
test3(int_value=200, str_value="二百", bool_value=False)


# before target
# test decorator 333, 100, 一百, False
# after target


# 带有自定义参数的装饰器
def repeat(num):
    def decorator3(target_func):
        def wrapper(*args, **kwargs):
            for i in range(num):
                print('before target')
                target_func(*args, **kwargs)
                print('after target')

        return wrapper

    return decorator3


print("---------------------------------------------")


@repeat(2)
def test4(message):
    print(message)


test4('test decorator3')

# before target
# test decorator3
# after target
# before target
# test decorator3
# after target


print("----------------------------------------------------------")


# 类装饰器, 类装饰器主要依赖于函数__call__()，每当调用一个类的示例时，函数__call__()就会被执行一次
class Count:
    def __init__(self, target_func):
        self.target_func = target_func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):  # __call__方法就作为目标方法的代理方法
        self.num_calls += 1
        print('num of calls is: {self.num_calls}')
        self.target_func(*args, **kwargs)
        print("After target func")


@Count
def test5():
    print("test class decorator")


test5()

print("----------------------------------------------------------")


# 装饰器的嵌套，可以同时使用多个装饰器
@decorator1
@decorator2
def test6():
    print("测试装饰器嵌套")


# 就相当于一起加了两个个切面，执行顺序从里到外，相当于decorator1(decorator2(test6))
test6()

print("----------------------------------------------------------")


# 使用装饰器后，原函数还是原函数吗？
def decorator4(target_func):
    @functools.wraps(target_func)  # 保留目标方法的元信息
    def wrapper():
        print('before target')
        target_func()  # 装饰器模式，在target方法的前后增加额外的功能
        print('after target')

    return wrapper


@decorator4
def test7():
    print("test decorator 7777")


print(test7.__name__)  # wrapper
# test7() 函数被装饰以后，它的元信息变了。元信息告诉我们“它不再是以前的那个 test7() 函数，而是被 wrapper() 函数取代了
# 为了解决这个问题，我们通常使用内置的装饰器@functools.wrap，它会帮助保留原函数的元信息（也就是将原函数的元信息，拷贝到对应的装饰器函数里）。

# Python的装饰器就是利用闭包机制实现的装饰器模式，注解模式只是语法糖


print("----------------------------------------------------")


# 装饰器例子，日志记录
def log_execution_time(target_func):
    @functools.wraps(target_func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = target_func(*args, **kwargs)
        end = time.perf_counter()
        print(f'{target_func.__name__} method took {(end - start) * 1000} ms')
        return result

    return wrapper


@log_execution_time
def calculate(num1, num2):
    return num1 ** num2


print(calculate(100, 2))
