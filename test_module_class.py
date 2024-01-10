# 从外部模块import一个类
from module.car import *
import time

car = Car('audi', 'a4', 2019)
print(car.get_descriptive_name())

time.sleep(1)
print("end")
# Python 模块（Module）就是一个python文件，以.py结尾。模块中可以定义函数，类和变量

# 只有该python文件作为程序入口时__name__变量才会是__main__，如果是作为module被其它文件import，下面的print语句不会执行
if __name__ == '__main__':
    print("in main file")


# dog = Dog() 会找不到Dog类
# print(dog)
