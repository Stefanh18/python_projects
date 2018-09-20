# Create the same program as in assignment 20 with one change. Now the text “you picked
# <value>” where value is the number that was input should only be printed if that value is an odd
# number.
turns = int(input("Enter a integer: "))
x = 0
value = 0
for x in range(0, turns):
    value = int(input("Enter a integer: "))
    if value % 2 == 1:
        print("you picked", value, "where value is the integer the user input")
