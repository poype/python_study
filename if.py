cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# python中的布尔值： True 和 False

# == 检查时是区分大小写的，使用下面的方式忽略大小写
# car.lower() == 'bmw'

# and 和 or 操作
if True and True:
    print('and')

if True or False:
    print('or')

# 关键字 in 检查特定的值是否包含在列表或元组中
print('audi' in cars) # True
print('gerry' in cars) # False

nums = (1, 2, 3, 4)
print(1 in nums) # True
print(11 in nums) # False

# 关键字 not in
print('audi' not in cars) # False
print('gerry' not in cars) # True

nums = (1, 2, 3, 4)
print(1 not in nums) # False
print(11 not in nums) # True

# if结构, else 和 elif 可以没有
score = 85

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 60:
    print('C')
else:
    print('D')

# 空列表作为if语句的条件时会被看成False
empty_list = []
if empty_list:
    print('there is element in list')
else:
    print('empty list') # 将打印这里

