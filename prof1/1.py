# Design an algorithm that generates the first n numbers in the following sequence:; 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …
# Make sure that you write up the algorithm before starting to code.
# Then implement the algorithm in Python. Put your algorihmic description as a comment in the program file. 
# During the design of your algorithm and your implementation, you should use git:



n = int(input("Enter the length og the sequence: "))
for i in range(1, n+1):
    if i == 1:
        current = first = i
    elif i == 2:
        current = second = i
    elif i == 3:
        current = third = i
    else:
        current = first + second + third
        first, second, third = second, third, current
    print(current)
