# Create a program that accepts 2 integers as input and outputs the greater integer. If the integers
# are equal the program should print the text “the numbers are equal”.

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

if num1 > num2:
    print("The greater number is:", num1)
elif num2 > num1:
    print("The greater number is:", num2)
else:
    print("The numbers are equal")