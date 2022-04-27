# python根据缩进来识别一个代码块，缩进在python中不能乱用

nums = [1, 2, 3, 4, 5]
# 用for..in..便利整个列表。在for代码块中，想包含多少行代码都可以
for num in nums:
    print(num)
    print(f"power number: {num * num}")
    print("-------------------------")


# range函数生成一些列数
for value in range(5):
    print(value) # 打印0~4

print("--------------------------")

# 默认range函数生成的数字从0开始，可以设置数的起始位置
for value in range(1, 5):
    print(value) # 打印1~4

print("--------------------------")

# range函数还可以指定步长，下面的代码指定步长是2
for value in range(0, 11, 2):
    print(value) # 打印0, 2, 4, 6, 8, 10

print("--------------------------")

# 使用list函数将range函数的结果转换为列表
number_list = list(range(1, 5))
print(number_list)


