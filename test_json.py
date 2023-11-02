import json

numbers = [1, 2, 3, 4, 5, 6, 7]

json_str = '{"a":1, "b":2, "c":3}'

obj = json.loads(json_str)  # 将json字符串反序列化成对象
print(obj['a'])
print(obj['b'])
print(obj['c'])

obj['d'] = 4

print(json.dumps(obj))  # 将对象序列化成json字符串
