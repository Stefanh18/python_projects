# Create a program that lets the user input an integer, lets call it size. 
# This integer should denote the size of a list. 
# Next you should let the user input size many values to a list. 
# Next you should let the user input a value, lets call it target. 
# If target is in the list the program should print “<target> is in the list“. 
# Otherwise it should print “<target> is not in the list“. 
# You can solve this with built in functions and the in operator but I recommend trying to 
# solve this without using builtin functions or the in operator as well (excluding .append()).

size = int(input("Enter the size of the list: "))
str1 = input("Enter numbers seperated by comma of the length {}: ".format(size))
list2 = str1.split(",")
final_list = []

for x in list2:
    final_list.append(x)
if len(final_list) == size:
    target = input("Enter the target: ")
    if target in final_list:
        print("{} is in the list".format(target))
    else:
        print("{} is not in the list".format(target))
else:
    print("Invalid input")


