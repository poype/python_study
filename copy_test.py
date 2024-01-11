# 深拷贝 和 浅拷贝
import copy

l1 = [1, 2, 3]
l2 = list(l1)

print(l1 == l2)  # True
print(l1 is l2)  # False

# 对于Tuple，copy会直接返回原来的对象
tup1 = (1, 2, 3)
tup2 = tup1[:]

print(tup1 is tup2)  # true

# 浅拷贝 shadow copy
l1 = [1, 2, ['a', 'b']]
l2 = l1[:]

l1.append(3)
print(l1)  # [1, 2, ['a', 'b'], 3]     l1 和 l2在第一层是分隔的
print(l2)  # [1, 2, ['a', 'b']]

l1[2].append('c')
print(l1)  # [1, 2, ['a', 'b', 'c'], 3]
print(l2)  # [1, 2, ['a', 'b', 'c']]    l1 和 l2两个列表中的第二个元素都改变了

# 深拷贝 deep copy
l1 = [[1, 2], [3, 4]]
l2 = copy.deepcopy(l1)

print(l1)
print(l2)

l1[0].append(100)
l1[1].append(200)

print(l1)  # [[1, 2, 100], [3, 4, 200]]
print(l2)  # [[1, 2], [3, 4]]    无论l1如何变化，l2都不变，l1和l2完全独立

# copy.deepcopy() 方法以递归的方式拷贝对象的值，拷贝的新对象与原对象没有任何关系
# copy.copy() 方法提供浅拷贝，适用于任何数据类型。





