# 通过while循环打印 1 ~ 5
current_number = 1
while(current_number <= 5):
    print(current_number)
    current_number += 1

print('-------------------')

# break退出循环
num = 1
while num < 10:
    print(num)
    num += 1

    if num > 6:
        break

print('-------------------')

# continue 只打印奇数
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue

    print(num)
    

    
