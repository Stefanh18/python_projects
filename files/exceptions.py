a = int(input("input a number: "))
b = int(input("input another number: "))

try:
    c = a // b
    print(c)
except:
    print("There was an error")