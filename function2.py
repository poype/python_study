def test_func_parameter(calculate_func):
    result = calculate_func(3, 5)
    print(f"计算结果是：{result}")


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


# 将函数作为另一个函数的参数，这是一种计算逻辑的传递，而非数据的传递
test_func_parameter(add)
test_func_parameter(sub)
test_func_parameter(mul)
test_func_parameter(div)


# lambda关键字，可以定义匿名函数
# 有名称的函数，可以基于名称重复使用。匿名函数，只能临时使用一次。
# 需要注意的是，lambda函数只能包含一个表达式，不能包含多条语句或复杂的逻辑。如果需要定义更复杂的函数，应该使用常规的函数定义方式。

test_func_parameter(lambda x, y: x + y)  # 无需写return语句，x + y会自动被return
