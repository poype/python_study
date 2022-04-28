# 从外部模块import一个类
from module.car import Car

car = Car('audi', 'a4', 2019)
print(car.get_descriptive_name())