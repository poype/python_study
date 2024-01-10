__all__ = ["Car"]
# 如果一个模块文件中有“__all__”变量，则在其它文件中使用“from xxx import *”导入时，只能导入这个列表中的元素
# 由于Dog类不在这个列表中，所以在其它文件中用“import *”不会导入Dog类
# 但如果使用“from xxx import Dog”明确导入该类是可以正常import的
# __all__这个东西应该用处不大

class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Dog:
    pass


if __name__ == '__main__':
    print("in car file")  # 当car.py文件作为module被其它文件import时，__name__变量的值不是__main__，所以这句话不会打印
