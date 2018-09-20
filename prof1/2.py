# Accept d1 and d2, the number of two dices, as input. First, check to see that they are in the proper range for dice. If not, print the message "Invalid input!"
# Otherwise, determine the sum.  If the sum is 7 or 11, print "Winner".
# If the sum is 2, 3 or 12, print "Loser". Otherwise print the sum.

d1 = int(input("Input first dice: "))
d2 = int(input("Input second dice: "))

if 0 < d1 <= 6 and 0 < d2 <= 6:
    sum = d1 + d2
    if sum == 7 or sum == 11:
        print("Winner")
    elif sum == 2 or sum == 3 or sum == 12:
        print("Loser")
    else:
        print(sum)
else:
    print("invalid input!")