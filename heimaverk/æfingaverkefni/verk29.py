# Create a program that takes an integer as input, let´s call it turns. This integer should indicate
# how many times the user wants to input a new integer. Next the program should let the user
# input turns many integers. The program should then print how many negative integers the user
# input, how many positive integers the user input, the sum of all the positive integers and the sum
# of all the negative integers the user input

turns = int(input("Enter a integer: "))
num_of_neg = 0
sum_of_neg = 0
sum_of_pos = 0
num_of_pos = 0
for x in range(0, turns):
    num = int(input("Enter a integer: "))
    if num < 0:
        num_of_neg += 1
        sum_of_neg += num
    else:
        num_of_pos += 1
        sum_of_pos += num
print("The number of negative numbers: ", num_of_neg, "and the sum of them is: ", sum_of_neg)
print("The number of positive numbers: ", num_of_pos, "and the sum of them is: ", sum_of_pos)