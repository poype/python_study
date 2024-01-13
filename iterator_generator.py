# list set tuple dict 四种容器都是可迭代的
# 迭代器（iterator）提供了一个 next 的方法。调用这个方法后，你要么得到这个容器的下一个对象，要么得到一个 StopIteration 的错误

# 下面的 NumList 就是一个自定义的可迭代类型
class NumList:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        result = self.current
        self.current += 1
        return result


num_list = NumList(1, 5)

for i in num_list:  # 可迭代的对象都可以用 for...in...的形式遍历
    print(i)  # 打印 1 ~ 4

l = [i for i in range(10000)]  # 生成一个包含一万个元素的列表，这种方式会提前占用大量的内存
print(l)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, .....

t = (i for i in range(10000))  # 换成小括号，就变成了生成器，只有在你调用 next() 函数的时候，才会生成下一个变量，避免占用大量的内存。
print(t)  # <generator object <genexpr> at 0x000002548F5B6440>

# for i in t:
#     print(i)

print("-------------------------------------------------")
# 直接使用迭代器获取元素
it = iter(t)
print(next(it))  # 0
print(next(it))  # 1
print(next(it))  # 2
# 这种直接使用迭代器获取对象的方式，看着不是很面向对象，但这可能就是python的特点
# 如果python对象上不存在某个“应该存在”的方法，可以试着找一下是否有相应的全局函数存在


print("-------------------------------------------------")


# 自定义生成器
def generator1():
    yield 1
    yield 2
    yield False
    yield "test is last value"


it1 = iter(generator1())
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))

print(2 in generator1())  # True
print(3 in generator1())  # False

print("-------------------------------------------------")


# 定义一个无限生成器。迭代器是一个有限集合，生成器则可以成为一个无限集
def generator2():
    i = 1
    while True:
        yield i ** 3  # 每次next函数被调用时，获取的就是 yield 生成的值
        i += 1


it2 = generator2()
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))


