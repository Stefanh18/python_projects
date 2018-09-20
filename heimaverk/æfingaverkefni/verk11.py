# Create a program that takes 2 integers as input, let’s call them a and b. Next the user should be
# able to input another integer which we shall call choice. If choice is 1 then the program should
# add a and b together and print the result. If choice is 2 the program should subtract b from a and
# print the result. If choice is 3 the program should multiply a and b together and print the result. If
# choice is any other number the program should print the text: “invalid input.”

a = int(input("Enter a integer: "))
b = int(input("Enter second integer: "))
choice = int(input("Enter integer 1,2 or 3: "))

if choice == 1:
    new_int = a + b
    print(new_int)
elif choice == 2:
    new_int = a // b
    print(new_int)
elif choice == 3:
    new_int = a * b
    print(new_int)
else:
    print("invalid input")

# 1 þá a + b 
# 2 þá a // b
# 3 þá a * b
# e-h annað nr print invalid input