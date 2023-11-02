
with open('text_file') as file_handler:
    content = file_handler.read()

print(content)


# 函数open接受一个参数，要打开文件的名称。Python在当前执行的文件所在的目录中查找指定的文件。
# 函数open返回一个表示文件的对象(句柄)
# 关键字with确保在不再需要访问文件后将其关闭。由python负责妥善地打开和关闭文件。
# python没有块级作用域，虽然content变量是在缩进块中定义的，但在缩进块外也能够正常访问该变量

print('---------------------------------------------')

# 也可以调用open()和close()来打开和关闭文件，但这样做时，如果程序存在bug导致close()未执行，文件将不会关闭。
handler = open('text_file')
content2 = handler.read()
print(content2)
handler.close()

print('---------------------------------------------')

# 逐行读取文件
with open('text_file') as handler2:
    for line in handler2:
        print(line)

# print函数会增加一个换行符

print('---------------------------------------------')

# 写入文件
with open('text_file', 'a') as handler3:
    handler3.write("\nwrite operation test")
    handler3.write("\nanother line")
