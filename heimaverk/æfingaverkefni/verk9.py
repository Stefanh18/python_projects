# 9. Create a program that takes 3 integers as input and prints the integer with the lowest value.

first_int = int(input("Enter a integer: "))
sec_int = int(input("Enter a second integer: "))
third_int = int(input("Enter a third integer: "))

if first_int > sec_int and first_int > third_int:
    print(first_int)
elif sec_int > first_int and sec_int > third_int:
    print(sec_int)
else: 
    print(third_int)