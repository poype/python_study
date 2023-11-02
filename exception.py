
try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")


# try-except-else

print("Give me two numbers, and I'll divide them")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break

    try:
        answer = int(first_number) / int(second_number)
    except ArithmeticError:
        print("You can't divide by zero!")
    except ValueError:
        print("You can only input a number!")
    else:
        print(answer)


# FileNotFoundError
try:
    with open('if2.py', mode='r', encoding='utf-8') as file_handler:
        content = file_handler.read()
    print(content)
except FileNotFoundError:
    print("file doesn't exist")



