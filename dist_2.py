user = {
    'name': 'poype',
    'age': 22,
    'degree': 'master'
}

# 通过items方法遍历字典中的每个key-value对
for key, value in user.items():
    print(f"key={key}, value={value}")

# items方法的返回值类似于列表，列表中的每个元素是一个key-value组成的元组
print(user.items()) # dict_items([('name', 'poype'), ('age', 22), ('degree', 'master')])

# 通过keys方法只遍历字典中每个元素的key
for key in user.keys():
    print(key)

print(user.keys()) # dict_keys(['name', 'age', 'degree'])

# 通过values方法只遍历字典中每个元素的value
for value in user.values():
    print(value)

print(user.values()) # dict_values(['poype', 22, 'master'])

