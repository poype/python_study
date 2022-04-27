# 列表是可以修改的，元组是一系列不可修改的元素

# 元组使用圆括号，而非中括号
nums = (1, 2, 3, 4)
print(nums[2]) # 3

# nums[2] = 100 修改元组中的值会报错：TypeError: 'tuple' object does not support item assignment

# 遍历元组中的值
for num in nums:
    print(num)

