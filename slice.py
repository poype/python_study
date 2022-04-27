letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[1:5]) # ['b', 'c', 'd', 'e']

# 如果没有指定第一个索引，python将自动从列表头开始
print(letters[:5]) # ['a', 'b', 'c', 'd', 'e']

# 如果没有指定第二个索引，python将自动包含到列表最后一个元素
print(letters[1:]) # ['b', 'c', 'd', 'e']

# for循环遍历slice中的每个元素
for letter in letters[1:5]:
    print(letter)


# 复制列表，通过创建一个包含整个列表的切片复制列表
letters_copy = letters[:]
print(letters_copy) # 初始状态两者相同 ['a', 'b', 'c', 'd', 'e', 'f', 'g']

letters_copy.append('h')
letters.append('z')
print(letters_copy) # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(letters)      # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'z']
