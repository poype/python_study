# import代码让python打开对应的文件，并将其中所有的代码都复制到这个文件中
# function.py文件中所有的代码都会执行一遍
import function

print('------------------')

full_name = function.get_full_name('marco', 'liu')
print(full_name)

# 导入特定的函数
from function import greet_user, describe_pet
# 采用这种导入方式，调用函数时就不需要再明确指定module名了
greet_user('Marco')
describe_pet('lucky')

# 导入函数时指定alias
from function import multiple_args as ma
ma('some message', 1, 2, 3, 4)

# 给module指定alias
import function as func
full_name = func.get_full_name('jacky', 'cai')
print(full_name)

# 导入模块中的所有函数，但最好不要这么做
from function import *

# 建立一个单独的文件夹作为package
# 注意在module文件夹中，必须包含__init__.py文件，只有包含这个文件，python才会认为它是一个package
# 如果module文件夹下没有__init__.py文件，会看到错误：No module named 'module.function_module'; 'module' is not a package
from module.function_module import test_func
test_func()

