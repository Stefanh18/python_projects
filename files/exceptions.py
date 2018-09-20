try:
    a = int(input("input a number: "))
    b = int(input("input another number: "))
except ValueError:
    print("there was an error")

try:
    c = a // b
    print(c)
except ZeroDivisionError as error:
    print(error)
except NameError as name_error:
    print(name_error)