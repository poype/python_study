# 文件名和文件夹名称最好使用小写字母，并使用下划线代替空格，这是python的命名约定

# 无需任何关键字，通过赋值就可以定义一个变量
message = "Hello Python World!"

print(message)

# 双引号字符串，包含单引号
message1 = "it's a string"
print(message1)

# 单引号字符串，包含双引号
message2 = 'he said: "this is a test" '
print(message2)

# 字符串的一些方法
message3 = "ada lovelace"
print(message3.title()) # Ada Lovelace

message4 = 'Ada Lovelace'
print(message4.upper()) # ADA LOVELACE
print(message4.lower()) # ada lovelace

message5 = "    test    "
print(message5.rstrip()) # 只删除右边的空白
print(message5.lstrip() + "a") # 只删除左边的空白
print(message5.strip()) # 删除两边的空白

# F字符串，注意这里的变量名没有用驼峰的模式
first_name = 'Poype'
last_name = 'Liu'
full_name = f"{first_name} {last_name}"
print(full_name) # Poype Liu
print(f"Hello {full_name}") # Hello Poype Liu
print(f"Hello {full_name.upper()}") # Hello POYPE LIU

# f字符串是在3.6版本引入的，如果是之前的版本要用format方法
print("Hello {}".format(full_name)) # Hello Poype Liu