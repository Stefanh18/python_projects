# Create a program that takes an integer as input, let´s call it turns. This integer should indicate
# how many times the user wants to input a new integer. Next the program should let the user
# input turns many integers. The program should then print how many negative integers the user
# input.

turns = int(input("Enter a integer: "))
numb_of_neg = 0
for x in range(0, turns):
    numb = int(input("Enter a integer: "))
    if numb < 0:
        numb_of_neg += 1
print(numb_of_neg)