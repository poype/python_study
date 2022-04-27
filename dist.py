# key-value结构
alien_0 = {
    'color': 'green',
    'points': 5
}
print(alien_0['color'])  # green
print(alien_0['points']) # 5
print(alien_0) # {'color': 'green', 'points': 5}

# 向字典增加新的key-value元素
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0) # {'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}

# 修改字典中的值
alien_0['color'] = 'red'
print(alien_0) # {'color': 'red', 'points': 5, 'x_position': 0, 'y_position': 25}

# 删除一个元素
del alien_0['color']
print(alien_0) # {'points': 5, 'x_position': 0, 'y_position': 25}

# 创建一个空的字典
alien_1 = {}
print(alien_1) # {}

# 用 [] 访问一个字典中没有的key会报错，下面的代码会报错
# print(alien_1['color']) 错误信息：KeyError: 'color'

# 方法get第一个参数指定key。第二个是可选参数，它指定当key不存在时返回的值
alien_1_color = alien_1.get('color', None)
print(alien_1_color) # None

# 如果不提供第二个可选参数，当key不存在时get方法返回None，所以下面这行代码与上面的代码完全相同
print(alien_1.get('color')) # None