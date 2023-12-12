import copy

# 拷贝一维数组的四种方式
original_list = [1, 2, 3, 4, 5]

# 第一种拷贝方式 [:]
list1 = original_list[:]

list1[1] = 999
print(list1)  # 只有list1中第1个元素被修改了，original_list中的元素并没有变
print(original_list)

# 第二种拷贝方式 copy函数
list2 = original_list.copy()

list2[2] = 888
print(list2)  # 只有list2中第2个元素被修改了，original_list中的元素并没有变
print(original_list)

# 第三种拷贝方式 类似构造函数的方式
list3 = list(original_list)

list3[3] = 777  # 只有list3中第3个元素被修改了，original_list中的元素并没有变
print(list3)
print(original_list)

# 第四种拷贝方式  两个数组相加返回一个新的数组
list4 = original_list + []
print(list4)

list4[4] = 666  # 只有list4中第4个元素被修改了，original_list中的元素并没有变
print(list4)
print(original_list)

# 深拷贝二维数组，注意是深拷贝
original_matrix = [[-1 for _ in range(3)] for _ in range(3)]

# 使用copy模块中的deepcopy方法实现深拷贝，深拷贝整个二维数组也就只有这一种方法
matrix2 = copy.deepcopy(original_matrix)
matrix2[0][0] = 100
print(matrix2)  # 只有matrix2中[0][0]元素被修改了，original_matrix中的元素并没有变
print(original_matrix)

# deepcopy 方法的注释
# Deep copy operation on arbitrary Python objects
