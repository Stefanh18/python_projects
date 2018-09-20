def instructions():

    print("l - for moving left")
    print("r - for moving right")
    print("Any other letter for quitting")

def number(position,l_r):
    if position == 10 and l_r == "r" or position == 1 and l_r == "l":
        return position
    else:
        if l_r == "l":
            position -= 1
        elif l_r == "r":
            position += 1
    return position

position = int(input("Input a position between 1 and 10: "))
l_r = "r"
while l_r == "l" or l_r == "r":
    instructions()
    l_r = input("Input your choice: ")
    position = number(position, l_r)
    print("New position is:", position)