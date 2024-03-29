s1 = {1, 2, 3}  # 定义一个集合
print(s1)

s1.add(4)
print(s1)

s1.add(1)  # 1已经存在了，就不会再被添加了
print(s1)

s2 = {}  # 这样定义的不是空集合，而是一个空的字典
print(s2)

s3 = set()  # 定义一个空集合
s3.add(5)
s3.add(5)
print(s3)

# 集合是无序的，所以不支持下标索引访问


# remove元素
print(s1)  # {1, 2, 3, 4}
s1.remove(3)
print(s1)  # {1, 2, 4}

# 清空集合
s1.clear()
print(s1)  # set() 就表示空集合

# 集合中的元素数量
s4 = {1, 1, 1, 2, 3}
count = len(s4)
print(f"s4集合中的元素数量：{count}")

# 用 in 操作符判断一个元素是否在集合中存在
print(1 in s4)  # True
print(9 in s4)  # False

# 遍历集合中的元素
for e in s4:
    print(f"集合中的元素：{e}")

# 集合中的元素：1
# 集合中的元素：2
# 集合中的元素：3


tup = (1, 2, 2, 3, 5)
print(3 in tup)  # True
print(10 in tup)  # False

l = ['a', 'c', 'd', 'e', 'a']
print('a' in l)  # True
print('h' in l)  # False

d = {'a': 1, 'c': 3, 'e': 4}  # 对于字典，in 操作符判断是对应的key是否存在
print('c' in d)  # True
print('h' in d)  # False
print(1 in d)  # 判断的是key，不是value，1是value的值，不是key的值，所以是False

print(1 in d.values())  # 判断某个value是否存在，True
