# 一个列表中可以包含不同类型的元素
from turtle import color


colors = ['red', 'green', 'yellow', 1, 2, 3.14]
print(colors)

# 按照下标访问元素
print(colors[0])
print(colors[1])
print(colors[2])

# 下标-1表示最后一个元素, -2表示倒数第二个元素，以此类推
print(colors[-1]) # 3.14
print(colors[-2]) # 2
print(colors[-3]) # 1

# 修改对应下标的值
colors[0] = 'black'
print(colors)

# colors[6] = 'white'  这行代码会报错：index out of range

# 列表是动态的，可以对其增删元素
# 在列表末尾添加元素
colors.append('white')
print(colors) # ['black', 'green', 'yellow', 1, 2, 3.14, 'white']

# 在位置1处增加一个元素
colors.insert(1, 'orange')
print(colors) # ['black', 'orange', 'green', 'yellow', 1, 2, 3.14, 'white']

# 删除下标1的元素。可以使用del删除任意位置处的元素
del colors[1]
print(colors) # ['black', 'green', 'yellow', 1, 2, 3.14, 'white']

# 列表的尾部是栈顶
print(colors.pop()) # white
print(colors.pop()) # 3.14
print(colors.pop()) # 2
print(colors) # ['black', 'green', 'yellow', 1]

# 使用pop方法还能删除列表中任意位置的元素
print(colors.pop(1)) # green
print(colors) # ['black', 'yellow', 1]

# 如果你要从列表中删除一个元素，且不再以任何方式使用它，就使用del语句；
# 如果你要从列表中删除元素后还能继续使用它，就使用方法pop()。

# 根据值删除元素，remove方法只删除第一次出现的值
colors.remove(1)
print(colors) # ['black', 'yellow']

# colors.remove(1) 如果要删除的元素不存在，会报错：list.remove(x): x not in list

# 正向排序
nums = [5, 3, 6, 9, 1, 4, 2, 8, 7]
nums.sort()
print(nums)
# 逆向排序
nums.sort(reverse=True)
print(nums)

# 临时排序，sorted方法不会对列表本身产生副作用
nums_2 = [5, 3, 6, 9, 1, 4, 2, 8, 7]
print(sorted(nums_2))
print(sorted(nums_2, reverse=True))
print(nums_2) # [5, 3, 6, 9, 1, 4, 2, 8, 7] 列表本身不变

# 列表翻转
chars = ['a', 'b', 'd', 'c']
chars.reverse()
print(chars) # ['c', 'd', 'b', 'a']

# 列表长度 len
print(len(chars))