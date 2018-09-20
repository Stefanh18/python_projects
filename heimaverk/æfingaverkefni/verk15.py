# Create a program that lets the user input a single integer, lets call it multiplier. Next your
# program should print all the integers between 2 and 15 (2 and 15 included) multiplied by the
# value of multiplier.

my_int = int(input("Enter a integer: "))
x = 2

while 2 <= x <= 15:
    new_int = my_int * x
    print(new_int)
    x += 1