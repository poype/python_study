# input方法接受用户输入，参数是提示符
message = input("please input something: ")
print(f"you tell me {message}")

# 使用函数input时，python将用户输入解读为字符串，通过int()方法转换为整数
int_num = int(message)
print(int_num + 1)

# 通过float()方法转换成浮点数
float_number = float(message)
print(float_number + 1)

