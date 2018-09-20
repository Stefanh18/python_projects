# Create a program that takes an integer as input, let´s call it turns. This integer should indicate
# how many times the user wants to input a new integer. Next the program should let the user
# input turns many integers. The program should then print how many negative integers the user
# input and how many positive integers the user input.

turns = int(input("Enter a integer: "))
neg = 0
pos = 0

for x in range(0, turns):
    num = int(input("Enter a integer: "))
    if num < 0:
        neg += 1
    else:
        pos += 1
print("This is the amount of negative numbers: ", neg)
print("This is the amount of positive numbers: ", pos)
