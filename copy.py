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


