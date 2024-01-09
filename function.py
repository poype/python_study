# 关键字def定义一个函数。文档字符串描述这个函数做什么，python会使用它生成函数的文档
def greet_user():
    """显示简单的问候语"""
    print("Hello World")


greet_user()


# 用相同的名字定义了一个有参数的函数，python并不支持函数重载。
# 定义了一个相同名字的函数后，上面定义的无参函数就不能再被调用了
def greet_user(username):
    '''显示增强版问候语'''
    print(f"Hello {username}")


# greet_user() TypeError: greet_user() missing 1 required positional argument: 'username'
greet_user("Poype")  # Hello Poype


def describe_pet(animal_type, pet_name):
    """显示宠物信息"""
    print(f"I have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")


# 函数的三种调用方式，当采用关键字实参调用函数时，关键字参数的顺序无关紧要
describe_pet('cat', 'jack')
describe_pet(animal_type='dog', pet_name='willie')
describe_pet(pet_name='lucy', animal_type='fish')


# 参数默认值，有默认值的参数必须放到参数列表中的最后
def describe_pet(pet_name, animal_type='dog'):
    """显示宠物信息"""
    print(f"I have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")


# 少提供一个参数，会使用animal_type参数的默认值
describe_pet('willie')
# 覆盖参数的默认值
describe_pet('lucy', 'fish')


# 函数返回值
def get_full_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()


print(get_full_name('poype', 'liu'))


# 支持任意数量的实参，多个参数是用类似tuple的结构封装的
def multiple_args(*args):
    print(args)  # (1, 2, 3, 4)
    # 遍历所有参数
    for arg in args:
        print(f"arg: {arg}")


multiple_args(1, 2, 3, 4)


def multiple_args(*args, size):
    print(args)
    print(size)


# 由于size参数放在*args的后面，所以这里必须明确指定参数名字
multiple_args(1, 2, 3, size="size value")


# 合理的处理方式应该把*args放在最后
def multiple_args(size, *args):
    print(args)
    print(size)


multiple_args("size value", 1, 2, 3)

print("##################################")

# 函数同时返回多个value
def multiple_rets():
    return 100, "test multiple return value", True


num, message, flag = multiple_rets()
print(num)
print(message)
print(flag)
